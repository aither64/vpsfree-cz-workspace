# Deliberately shared second-audit fixtures

Source: lead message f2e6d33d-6f94-45a7-98da-ea952957193f, independent2026-10-29-haveapi-security-review. These are synthetic local fixtures copied through approved communication; no peer-file access.

Compact VULN-03/VULN-04 fixture and corrected-assertion handoff follows. This is extracted from this audit's locally passing PoCs at ddf836fb; no source fix is proposed/applied here.

Shared fake executable for corrected tests:
```ruby
bin = File.join(directory, 'bin')
FileUtils.mkdir_p(bin)
%w[haveapi-cli curl].each do |name|
  path = File.join(bin, name)
  File.write(path, "#!/bin/sh\nprintf '%s\\0' \"$@\" > \"$CAPTURE\"\n")
  File.chmod(0o755, path)
end
capture = File.join(directory, 'arguments')
env = {
  'PATH' => "#{bin}:#{ENV.fetch('PATH')}",
  'CAPTURE' => capture
}
argv = File.binread(capture).split("\0", -1)[0...-1]
```
Execute extracted command text with:
```ruby
_stdout, stderr, status = Open3.capture3(env, 'sh', '-c', command)
expect(status).to be_success, stderr
```

VULN-03 — Ruby client CLI help

Synthetic action:
```ruby
action = Object.new
action.define_singleton_method(:examples) do
  [{ title: '', request: { name: payload }, response: {} }]
end
action.define_singleton_method(:resource_path) { ['widget'] }
action.define_singleton_method(:name) { 'update' }
action.define_singleton_method(:param_description) do |_direction, name|
  name == :name ? { type: 'String' } : nil
end
action.define_singleton_method(:namespace) { |_direction| :widget }

cli = Object.new
cli.define_singleton_method(:format_output) { |_action, _response, _out| nil }
```
Render with a deterministic executable name:
```ruby
out = StringIO.new
saved = $PROGRAM_NAME
$PROGRAM_NAME = 'haveapi-cli'
HaveAPI::CLI::ExampleFormatter.format_examples(cli, action, out)
source = out.string
$PROGRAM_NAME = saved
command = source.lines.find { |line| line.start_with?('$ ') }.delete_prefix('$ ')
```
Exact exploit input:
```ruby
marker = File.join(directory, 'request-value-executed')
payload = "$(printf request-value-confirmed > #{marker})"
```
Vulnerable ddf behavior: fake client exits successfully and marker contains `request-value-confirmed`.

Corrected assertions:
```ruby
expect(status).to be_success, stderr
expect(File.exist?(marker)).to be(false)
expect(argv).to eq([
  'widget', 'update', '--', '--name', payload
])
expect(source).to include(payload) # literal remains visibly documented
```
Also exercise complete dynamic tokens, not only the value: set `$PROGRAM_NAME`, resource path, action name and parameter name to strings containing spaces, apostrophes, `$()`, backticks, separators, newlines and Unicode. Expected fake argv remains one token per program argument, with option name dasherization preserved. Boolean true/false must remain `--flag`/`--no-flag`; preserve delimiter and existing value `to_s` behavior.

VULN-04 — response transcript copied as shell

Exact common renderer context:
```ruby
Context = Struct.new(
  :host, :base_url, :version, :resource_path, :resource, :action_name,
  :action, :sample, :detail,
  keyword_init: true
)
action = {
  method: 'POST', path: '/widgets/{widget_id}', auth: false,
  input: { layout: :hash, namespace: :widget, parameters: {} },
  output: {
    layout: :hash, namespace: :widget,
    parameters: { name: { type: 'String' } }
  }
}
sample = {
  path_params: [7], request: {}, response: { name: payload },
  status: true, message: 'ok', errors: nil
}
context = Context.new(
  host: 'docs.example',
  base_url: 'https://docs.example/api/',
  version: '1',
  resource_path: ['widget'],
  resource: {},
  action_name: 'show',
  action: action,
  sample: sample,
  detail: :simple
)
```
Current vulnerable extraction mirrors the Copy control's whole `code.textContent`:
```ruby
displayed = renderer.render(:example, context: context).fetch(:code)
copied = displayed.delete_prefix('$ ')
Open3.capture3(env, 'sh', '-c', copied)
```

Ruby CLI response fixture:
```ruby
marker = File.join(directory, 'ruby-cli-response-executed')
payload = "$(printf ruby-cli-response-confirmed > #{marker})"
displayed = HaveAPI::ClientExamples::RubyCli.render(
  :example, context: context
).fetch(:code)
```
Current displayed tail is materially:
```
 NAME:  $(printf ruby-cli-response-confirmed > MARKER)

```
Vulnerable proof: marker contains `ruby-cli-response-confirmed`.

Corrected request-only clipboard payload must execute with:
```ruby
expect(File.exist?(marker)).to be(false)
expect(argv).to eq([
  '-u', 'https://docs.example/api/',
  '--version', '1',
  'widget', 'show', '7'
])
expect(copy_payload).not_to include(payload)
expect(displayed_response_text).to include("NAME:  #{payload}")
```

curl response fixture:
```ruby
marker = File.join(directory, 'curl-response-executed')
payload = "$(printf curl-response-confirmed > #{marker})"
displayed = HaveAPI::ClientExamples::Curl.render(
  :example, context: context
).fetch(:code)
```
Vulnerable proof: whole-block execution creates marker containing `curl-response-confirmed`.

Corrected request-only clipboard payload must execute with:
```ruby
expect(File.exist?(marker)).to be(false)
expect(argv).to eq([
  '--request', 'POST',
  '--data-binary', JSON.generate(widget: {}),
  'https://docs.example/api/widgets/7'
])
expect(copy_payload).not_to include(payload)
expect(JSON.parse(displayed_response_text)).to eq(
  'status' => true,
  'message' => 'ok',
  'response' => { 'widget' => { 'name' => payload } },
  'errors' => nil
)
```

Preferred UI contract for VULN-04:
- Render request and response in separate elements/blocks with distinct language semantics.
- Mark the request element as the Copy source; the response stays visible but is never part of shell clipboard text.
- Browser asset test should click the real Copy button, capture `navigator.clipboard.writeText`, assert equality with the request element's complete text (including multiline continuations), and assert the response-only payload is absent.
- Preserve fallback/native-copy behavior and visible response status/message/data/errors.
- If a combined display is retained, every physical response line—including embedded newlines—must be inert shell comments, but request-only Copy is the clearer contract.

Exact original audit commands/results:
- `nix develop .#client-ruby -c bash -lc 'cd clients/ruby && bundle exec rspec ../../vulnerabilities/VULN-03/poc_spec.rb'`: 1 example, 0 failures.
- `nix develop .#server-ruby -c bash -lc 'cd servers/ruby && bundle exec rspec ../../vulnerabilities/VULN-04/poc_spec.rb'`: 2 examples, 0 failures.

For both fixes, retain the dual assertion: no marker proves inert shell data; exact argv proves the remediation did not silently corrupt the documented request.

