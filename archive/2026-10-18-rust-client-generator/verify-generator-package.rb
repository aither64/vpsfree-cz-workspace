#!/usr/bin/env ruby
# Package acceptance only. No publication, Cargo invocation or checkout writes.
require 'digest'
require 'fileutils'
require 'json'
require 'open3'
require 'optparse'
require 'rbconfig'
require 'rubygems/package'
require 'tmpdir'

options = {}
OptionParser.new do |parser|
  %w[haveapi-root client-root expected-haveapi-head expected-client-head artifacts].each do |name|
    parser.on("--#{name} VALUE") { |value| options[name] = value }
  end
end.parse!
%w[haveapi-root client-root expected-haveapi-head expected-client-head artifacts].each do |name|
  abort "Missing --#{name}" unless options[name]
end
haveapi = File.realpath(options.fetch('haveapi-root'))
client = File.realpath(options.fetch('client-root'))
component = File.join(haveapi, 'clients/rust')
artifacts = File.expand_path(options.fetch('artifacts'))
abort 'Artifact directory must be new or empty' if File.exist?(artifacts) && !Dir.empty?(artifacts)
FileUtils.mkdir_p(artifacts)
git = lambda do |root, *arguments|
  stdout, stderr, status = Open3.capture3('git', '-C', root, *arguments)
  raise "Read-only Git command failed: #{stderr.lines.first}" unless status.success?
  stdout.strip
end
before = { 'haveapi_head' => git.call(haveapi, 'rev-parse', 'HEAD'),
           'client_head' => git.call(client, 'rev-parse', 'HEAD'),
           'client_status' => git.call(client, 'status', '--porcelain=v1') }
raise 'HaveAPI head differs from watcher brief' unless before['haveapi_head'] == options.fetch('expected-haveapi-head')
raise 'Client head differs from watcher brief' unless before['client_head'] == options.fetch('expected-client-head')
raise 'HaveAPI source is dirty' unless git.call(haveapi, 'status', '--porcelain=v1').empty?
raise 'Client checkout is dirty' unless before['client_status'].empty?
File.write(File.join(artifacts, 'input-receipt.json'), JSON.pretty_generate(before) + "\n")
gem_path = File.join(artifacts, 'haveapi-rust-client.gem')
stdout, stderr, status = Open3.capture3(
  { 'RUBYOPT' => nil, 'GEM_PATH' => nil }, RbConfig.ruby, '-S', 'gem', 'build',
  'haveapi-rust-client.gemspec', '--output', gem_path, chdir: component
)
File.write(File.join(artifacts, 'gem-build.log'), stdout + stderr)
raise "Gem build failed; see #{artifacts}/gem-build.log" unless status.success?
package = Gem::Package.new(gem_path)
package.verify
spec = package.spec
raise 'Wrong generator package identity' unless spec.name == 'haveapi-rust-client' && spec.version.to_s == '0.29.0'
raise 'Unexpected generator dependencies' unless spec.runtime_dependencies.map(&:name).sort == %w[haveapi-client tomlrb]
contents = package.contents.sort
required = %w[Gemfile.lock bin/haveapi-rust-client lib/haveapi/rust_client.rb
              lib/haveapi/rust_client/generator.rb template/action.rs.erb runtime/src/runtime/mod.rs]
raise 'Package is missing required generator sources' unless (required - contents).empty?
raise 'Private harness/tests leaked into package' if contents.any? { |path| path.start_with?('spec/', 'runtime/tests/', 'runtime/target/') || %w[runtime/Cargo.toml runtime/Cargo.lock runtime/src/lib.rs].include?(path) }
Dir.mktmpdir('haveapi-rust-package-') do |temp|
  extracted = File.join(temp, 'package')
  package.extract_files(extracted)
  inventory = contents.map do |path|
    packaged = File.join(extracted, path)
    source = File.join(component, path)
    raise "Packaged source differs: #{path}" unless File.binread(packaged) == File.binread(source)
    { 'path' => path, 'bytes' => File.size(packaged), 'sha256' => Digest::SHA256.file(packaged).hexdigest }
  end
  File.write(File.join(artifacts, 'package-inventory.json'), JSON.pretty_generate(inventory) + "\n")
  candidate = File.join(temp, 'candidate')
  FileUtils.mkdir_p(File.join(candidate, 'src'))
  FileUtils.cp(File.join(client, 'Cargo.toml'), File.join(candidate, 'Cargo.toml'))
  probe = File.join(artifacts, 'package-probe.rb')
  File.write(probe, <<~'RUBY')
    require 'bundler/setup'
    require 'json'
    require 'digest'
    packaged, client, output, receipt = ARGV
    $LOAD_PATH.unshift(File.join(packaged, 'lib'))
    require 'haveapi/rust_client/cli'
    raise 'Generator loaded from source checkout' unless HaveAPI::RustClient::Generator::ROOT == packaged
    args = ['generate', '--schema', File.join(client, 'schema/api-7.0.json'), '--api-version', '7.0',
            '--config', File.join(client, 'generator.toml'), '--output', output]
    raise 'Packaged generation failed' unless HaveAPI::RustClient::Cli.run(args.dup).zero?
    raise 'Packaged read-only check failed' unless HaveAPI::RustClient::Cli.run(args + ['--check']).zero?
    marker = '.haveapi-generated.json'
    expected = JSON.parse(File.read(File.join(client, 'src/generated', marker)))
    actual = JSON.parse(File.read(File.join(output, marker)))
    raise 'Packaged generation metadata/digests differ from actual client' unless actual == expected
    actual.fetch('files').each_key do |path|
      raise "Generated file differs: #{path}" unless File.binread(File.join(output, path)) == File.binread(File.join(client, 'src/generated', path))
    end
    loaded = $LOADED_FEATURES.select { |path| path.include?('/haveapi/rust_client') }
    # Bundler may read the source gemspec's version constant while activating
    # the locked path dependency. It is package metadata, not generator logic.
    activation_version = File.join(Gem.loaded_specs.fetch('haveapi-rust-client').full_gem_path, 'lib/haveapi/rust_client/version.rb')
    raise 'Activation metadata differs from packaged version' unless File.binread(activation_version) == File.binread(File.join(packaged, 'lib/haveapi/rust_client/version.rb'))
    loaded.reject! { |path| path == activation_version }
    raise 'Unpackaged generator library was loaded' unless loaded.all? { |path| path.start_with?(File.join(packaged, 'lib/')) }
    summary = actual.reject { |key, _value| key == 'files' }
    summary['rust_file_count'] = actual.fetch('files').keys.count { |path| path.end_with?('.rs') }
    summary['loaded_generator_files'] = loaded.map { |path| path.delete_prefix(packaged + '/') }.sort
    File.write(receipt, JSON.pretty_generate(summary) + "\n")
  RUBY
  stdout, stderr, status = Open3.capture3(
    { 'BUNDLE_GEMFILE' => File.join(component, 'Gemfile'), 'RUBYOPT' => nil, 'GEM_PATH' => nil },
    RbConfig.ruby, probe, extracted, client, File.join(candidate, 'src/generated'),
    File.join(artifacts, 'generation-receipt.json')
  )
  File.write(File.join(artifacts, 'generation.log'), stdout + stderr)
  raise "Packaged generation comparison failed; see #{artifacts}/generation.log" unless status.success?
end
raise 'HaveAPI head changed during package acceptance' unless git.call(haveapi, 'rev-parse', 'HEAD') == before['haveapi_head']
raise 'HaveAPI checkout changed during package acceptance' unless git.call(haveapi, 'status', '--porcelain=v1').empty?
raise 'Client head changed during package acceptance' unless git.call(client, 'rev-parse', 'HEAD') == before['client_head']
raise 'Client checkout changed during package acceptance' unless git.call(client, 'status', '--porcelain=v1') == before['client_status']
result = before.merge('result' => 'passed', 'gem_sha256' => Digest::SHA256.file(gem_path).hexdigest,
                      'package_file_count' => contents.length,
                      'comparison' => 'all generated Rust files and full ownership manifest byte-identical')
File.write(File.join(artifacts, 'result.json'), JSON.pretty_generate(result) + "\n")
puts JSON.generate(result)
