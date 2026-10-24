# frozen_string_literal: true

# Unchanged prepare_merge_hooks validation program. ABI assertions follow it.
require 'json'
if File.file?('.overcommit.yml') && File.file?('Gemfile')
  require 'bundler'
  Bundler.setup
  require 'overcommit'
end
puts "WORKSPACE_MERGE_HOOK_ENV=#{JSON.generate(ENV.to_h.slice(*ARGV))}"

require 'rbconfig'
abort 'unexpected repository Ruby/API' unless RUBY_VERSION == '3.3.10' && RbConfig::CONFIG['ruby_version'] == '3.3.0'
gem_home = File.join(Dir.pwd, '.gems')
abort 'gem home escaped disposable source' unless ENV['GEM_HOME'] == gem_home

# Exercise the installed native files, in addition to Bundler specification checks.
require 'racc/parser'
require 'racc/cparse'
require 'prism'
require 'bigdecimal'
native_specs = %w[json racc prism bigdecimal].map do |name|
  spec = Gem.loaded_specs.fetch(name)
  abort "native gem escaped disposable source: #{name}" unless spec.full_gem_path.start_with?("#{gem_home}/gems/")
  abort "native extension is incomplete: #{name}" if spec.missing_extensions?
  { 'name' => name, 'version' => spec.version.to_s, 'extensionDirectory' => spec.extension_dir }
end
abort 'Overcommit did not load' unless Gem.loaded_specs.fetch('overcommit').version.to_s == '0.73.0'
puts "HAVEAPI_HOOK_ABI_PROOF=#{JSON.generate(
  'ruby' => RbConfig.ruby,
  'version' => RUBY_VERSION,
  'extensionApi' => RbConfig::CONFIG['ruby_version'],
  'gemHome' => gem_home,
  'bundler' => Gem.loaded_specs.fetch('bundler').version.to_s,
  'overcommit' => Gem.loaded_specs.fetch('overcommit').version.to_s,
  'nativeGems' => native_specs
)}"
