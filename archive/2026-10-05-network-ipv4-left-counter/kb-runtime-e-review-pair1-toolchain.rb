require 'json'
require 'rbconfig'
require 'rubygems'
require 'minitest'
require 'timeout'
require 'digest'

features = $LOADED_FEATURES.grep(%r{/(?:minitest(?:/|\.rb)|timeout\.rb)})
specs = %w[minitest timeout].to_h { |name| [name, Gem.loaded_specs.fetch(name).full_gem_path] }
raise 'non-Nix Ruby or gems' unless RbConfig.ruby.start_with?('/nix/store/') &&
  specs.values.all? { |path| path.start_with?('/nix/store/') } &&
  features.all? { |path| path.start_with?('/nix/store/') }
raise 'ambient RubyGems path' unless Gem.path.all? { |path| path.start_with?('/nix/store/') }
receipt = JSON.parse(File.read(ARGV.fetch(0)))
raise 'wrong selected D receipt' unless receipt['revision'] == '51aba080b264c28f5584867b6cf006bf423ae2f3' &&
  receipt['source'] == '/nix/store/y7r40b5h4hd44jfzan4kv1zar3rxmyyl-source' &&
  ENV.fetch('DEV_WORKSPACE_HOST_SOURCE') == receipt['source'] &&
  ENV.fetch('DEVCLUSTER_RUNTIME_CONTRACT') == File.join(receipt['source'], 'portal/internal/session/runtime-contract.json')
receipt.fetch('files').each do |name, digest|
  raise "selected D bytes differ: #{name}" unless Digest::SHA256.file(File.join(receipt.fetch('source'), name)).hexdigest == digest
end
metadata = JSON.parse(File.read(ENV.fetch('VPSFREE_KB_ENGINE_METADATA')))
raise 'wrong selected K receipt' unless metadata['revision'] == '68aa33b451a14eb7bf4b2f1a090a8e5a2f80b52e' &&
  metadata['source'] == '/nix/store/r1b23g240p4yr44f5qgh3zhaj89qjmy0-source'
raise 'wrong immutable K metadata path' unless ENV.fetch('VPSFREE_KB_ENGINE_METADATA') == '/nix/store/3l8p07gyra3xfmpqsdadmlc4m3maw90i-vpsfree-kb-runtime-source.json'
raise 'canonical metadata receipt bytes differ' unless File.binread(ENV.fetch('VPSFREE_KB_ENGINE_METADATA')) == File.binread(ARGV.fetch(1))
raise 'K lock digest differs' unless metadata.fetch('lock_sha256') == '49db9a81f9777fe390a74d72543a90ee7705c2c05effec9d75b18c9173230ad2' && Digest::SHA256.file(File.join(metadata.fetch('source'), 'flake.lock')).hexdigest == metadata.fetch('lock_sha256')
require File.join(metadata.fetch('source'), 'cluster/lib/kb_source')
selected = KbRuntime::Software.new(metadata)
raise 'wrong selected backend/OS' unless selected.metadata.fetch('inputs').fetch('vpsadmin').fetch('rev') == '5d5527a67315c18b595345aa6996d7724c1ed071' && selected.metadata.fetch('inputs').fetch('vpsadminos').fetch('rev') == '6bdf458fd9105379860234ff33d352e55844f08f'
lock = JSON.parse(File.read('flake.lock'))
root = lock.fetch('nodes').fetch(lock.fetch('root')).fetch('inputs')
k = lock.fetch('nodes').fetch(root.fetch('kb-runtime'))
d = lock.fetch('nodes').fetch(root.fetch('dev-workspace'))
raise 'E selected K/D pair differs' unless k.fetch('locked').fetch('rev') == metadata.fetch('revision') && d.fetch('locked') == receipt.fetch('locked').reject { |key, _| key == '__final' }
puts JSON.pretty_generate(ruby: RUBY_DESCRIPTION, executable: RbConfig.ruby,
  minitest: Minitest::VERSION, timeout: Timeout::VERSION,
  gem_paths: Gem.path, gem_specs: specs, loaded_features: features,
  selected_d_revision: receipt['revision'], selected_d_source: receipt['source'],
  selected_k_revision: metadata['revision'], selected_k_source: metadata['source'],
  selected_k_metadata: ENV.fetch('VPSFREE_KB_ENGINE_METADATA'), selected_k_lock_sha256: metadata['lock_sha256'],
  selected_k_fixture_sha256: metadata['fixture_sha256'])
