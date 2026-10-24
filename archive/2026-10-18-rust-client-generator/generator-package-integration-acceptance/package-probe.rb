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
