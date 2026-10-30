# Deliberately shared synthetic audit fixtures

Source: peer message9df6f470-bf3a-4f1a-b8a0-0c3d69a7dc70 from2026-10-29-haveapi-security-review. Copied through approved lead communication; no peer-file access.

Compact synthetic fixtures/assertions for both findings follow. These reproduce the exact locally confirmed paths without access to this session's worktree.

Common renderer fixture:
```ruby
action = {
  method: 'POST',
  path: '/widgets/{widget_id}',
  auth: false,
  input: {
    layout: :hash,
    namespace: :widget,
    parameters: { name: { type: 'String' } }
  },
  output: {
    layout: :hash,
    namespace: :widget,
    parameters: {}
  }
}
sample = {
  path_params: [7],
  request: { name: payload },
  response: {},
  status: true
}
```
RubyCli constructor:
```ruby
HaveAPI::ClientExamples::RubyCli.new(
  'docs.example', base_url, '1', ['widget'], {}, 'update', action
)
```
Curl constructor is identical except class `Curl`.

Use a temporary fake executable rather than a real client. It should write NUL-delimited `"$@"` to an environment-selected capture file, then exit 0. Execute copied documentation with:
```ruby
Open3.capture3(environment, 'sh', '-c', source.sub(/\A\$ /, ''))
```
For corrected-code regression assertions, require: shell status success, marker absent, and captured argv equal the intended literals. A shell fake can capture with `printf '%s\\0' "$@" > "$CAPTURE"`.

VULN-01 / Ruby CLI request-value fixture:
```ruby
marker = File.join(directory, 'request-value-executed')
payload = "'; printf request-value-confirmed > #{marker}; #'"
base_url = 'https://docs.example/api/'
source = renderer.example(**sample)
```
The vulnerable source rendered as:
```
$ haveapi-cli -u https://docs.example/api/ --version 1 widget update 7 -- \
              --name ''; printf request-value-confirmed > MARKER; #''
```
Locally confirmed vulnerable assertion: `File.read(marker) == 'request-value-confirmed'`.
Corrected-code assertions:
```ruby
expect(File.exist?(marker)).to be(false)
expect(captured_argv).to eq([
  '-u', 'https://docs.example/api/',
  '--version', '1',
  'widget', 'update', '7', '--',
  '--name', payload
])
```

VULN-01 / Ruby CLI base-URL fixture:
```ruby
marker = File.join(directory, 'base-url-executed')
base_url = "https://docs.example/api; printf host-confirmed > #{marker}; #"
source = renderer(base_url:).init
```
Locally confirmed vulnerable assertion: `File.read(marker) == 'host-confirmed'`.
Corrected-code assertions:
```ruby
expect(File.exist?(marker)).to be(false)
expect(captured_argv).to eq([
  '-u', base_url, '--version', '1'
])
```

VULN-02 / curl JSON fixture:
```ruby
marker = File.join(directory, 'request-value-executed')
payload = "$(printf request-value-confirmed > #{marker})"
base_url = 'https://docs.example/api/'
source = renderer.request(**sample)
```
The vulnerable `--data-binary` shell token contains the pretty JSON value inside double quotes, so the substitution executes. Locally confirmed vulnerable assertion: `File.read(marker) == 'request-value-confirmed'`.
Corrected-code assertions:
```ruby
expect(File.exist?(marker)).to be(false)
expect(captured_argv[0, 2]).to eq(['--request', 'POST'])
data_index = captured_argv.index('--data-binary')
expect(data_index).not_to be_nil
expect(JSON.parse(captured_argv.fetch(data_index + 1))).to eq(
  'widget' => { 'name' => payload }
)
expect(captured_argv.last).to eq(
  'https://docs.example/api/widgets/7'
)
```
Parsing the captured data instead of asserting pretty/compact whitespace permits the architect's chosen serializer while proving literal preservation.

VULN-02 / curl base-URL quote-breakout fixture:
```ruby
marker = File.join(directory, 'base-url-executed')
base_url = "https://docs.example/'$(printf host-confirmed > #{marker})'/api/"
payload = 'ordinary'
source = renderer(base_url:).request(**sample)
expected_url = "#{base_url}widgets/7"
```
The vulnerable rendered tail is:
```
'https://docs.example/'$(printf host-confirmed > MARKER)'/api/widgets/7'
```
Locally confirmed vulnerable assertion: `File.read(marker) == 'host-confirmed'`.
Corrected-code assertions:
```ruby
expect(File.exist?(marker)).to be(false)
expect(captured_argv.last).to eq(expected_url)
data_index = captured_argv.index('--data-binary')
expect(JSON.parse(captured_argv.fetch(data_index + 1))).to eq(
  'widget' => { 'name' => 'ordinary' }
)
```

Original local PoC results:
- `bundle exec rspec ../../vulnerabilities/VULN-01/poc_spec.rb`: 2 examples, 0 failures.
- `bundle exec rspec ../../vulnerabilities/VULN-02/poc_spec.rb`: 2 examples, 0 failures.
The fake executables made no network requests. Keep the marker-absence and literal-argv assertions together: marker absence proves no shell evaluation, while argv equality proves the fix did not corrupt the documented value.

