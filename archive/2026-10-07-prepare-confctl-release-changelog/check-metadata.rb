require 'bundler'
require 'json'

gemset = JSON.parse(File.read(ARGV.fetch(0)))
lock = Bundler::LockfileParser.new(File.read('Gemfile.lock'))
locked = lock.specs.to_h { |spec| [spec.name, spec.version.to_s] }
generated = gemset.transform_values { |spec| spec.fetch('version') }
abort "Lock/gemset version mismatch: #{locked.to_a - generated.to_a}; #{generated.to_a - locked.to_a}" unless locked == generated
lock.specs.each do |spec|
  expected = spec.dependencies.map(&:name).sort
  actual = gemset.fetch(spec.name).fetch('dependencies', []).sort
  abort "Dependency graph mismatch: #{spec.name}" unless expected == actual
end
minimum = Gem::Version.new('3.3.0')
Gem.loaded_specs.each_value do |spec|
  abort "#{spec.full_name} requires #{spec.required_ruby_version}" unless spec.required_ruby_version.satisfied_by?(minimum)
end
expected_version = ARGV.fetch(1)
require 'confctl/version'
abort 'Release version metadata mismatch' unless [ConfCtl::VERSION, locked.fetch('confctl'), generated.fetch('confctl')].all? { |v| v == expected_version }
puts "Lock/gemset versions and dependency graph agree for #{locked.size} gems; all activated gems support Ruby 3.3.0"
