require 'json'
require 'rbconfig'
require 'rubygems'
require 'minitest'
require 'timeout'

features = $LOADED_FEATURES.grep(%r{/(?:minitest(?:/|\.rb)|timeout\.rb)})
specs = %w[minitest timeout].to_h { |name| [name, Gem.loaded_specs.fetch(name).full_gem_path] }
raise 'non-Nix Ruby or declared gems' unless RbConfig.ruby.start_with?('/nix/store/') &&
  specs.values.all? { |path| path.start_with?('/nix/store/') } &&
  features.all? { |path| path.start_with?('/nix/store/') }
raise 'ambient RubyGems path' unless Gem.path.all? { |path| path.start_with?('/nix/store/') }
metadata = JSON.parse(File.read(ENV.fetch('VPSFREE_KB_ENGINE_METADATA')))
raise 'wrong selected K source receipt' unless metadata['revision'] == '93a16d6cecb6bc847ec9335a3f170eb8b301ab56' &&
  metadata['source'] == '/nix/store/gjnf23p6sldxzy147iw0031x53z8gzy5-source'
puts JSON.pretty_generate(ruby: RUBY_DESCRIPTION, executable: RbConfig.ruby,
  minitest: Minitest::VERSION, timeout: Timeout::VERSION,
  gem_paths: Gem.path, gem_specs: specs, loaded_features: features,
  selected_k_revision: metadata['revision'], selected_k_source: metadata['source'])
