require 'rubygems/package'
require 'json'
require 'tmpdir'
require 'open3'
require 'rbconfig'
require 'bundler'

gem_file, source_files_path, records, source_commit = ARGV
package = Gem::Package.new(gem_file)
package.verify
spec = package.spec
abort 'Incorrect package name or version' unless spec.name == 'confctl' && spec.version.to_s == '3.0.0'
abort 'Incorrect Ruby requirement' unless spec.required_ruby_version.to_s == '>= 3.3.0'
abort 'Missing CLI executable' unless spec.executables.include?('confctl')

source_files = File.binread(source_files_path).split("\0")
files = spec.files.sort
missing = source_files - files
abort "Missing source files: #{missing.inspect}" unless missing.empty?
extras = files - source_files
allowed_generated = source_files.grep(%r{\Aman/.*\.md\z}).flat_map do |path|
  base = path.delete_suffix('.md')
  [base, "#{base}.html"]
end + ['man/index.html', 'man/style.css']
abort "Unexpected package files: #{(extras - allowed_generated).inspect}" unless (extras - allowed_generated).empty?
abort 'Missing generated manpages' unless allowed_generated.all? { |path| files.include?(path) }
abort 'Local metadata or dependencies included' if files.any? do |path|
  path.match?(%r{\A(?:\.git|\.gems|\.bundle|\.bin|\.cache|\.rubocop_cache|pkg|work)(?:/|\z)})
end

Dir.mktmpdir('confctl-package-') do |dir|
  package.extract_files(dir)
  version_source = File.read(File.join(dir, 'lib/confctl/version.rb'))
  abort 'Incorrect packaged version constant' unless version_source.include?("VERSION = '3.0.0'")
  changelog = File.read(File.join(dir, 'CHANGELOG.md'))
  abort 'Missing software pin removal notice' unless changelog.include?('will be removed in v4')
  env = {
    'RUBYLIB' => File.join(dir, 'lib'),
    'GEM_HOME' => ENV.fetch('GEM_HOME'),
    'GEM_PATH' => ENV.fetch('GEM_PATH')
  }
  probe = <<~RUBY
    require 'confctl'
    root = File.realpath(ARGV.shift)
    abort 'Loaded confctl from outside the package' unless ConfCtl.root == root
    abort 'Incorrect loaded confctl source' unless $LOADED_FEATURES.include?(File.join(root, 'lib/confctl.rb'))
    abort 'Incorrect loaded package version' unless ConfCtl::VERSION == '3.0.0'
    load File.join(root, 'bin/confctl')
  RUBY
  output, status = Bundler.with_unbundled_env do
    Open3.capture2e(env, RbConfig.ruby, '-e', probe, dir, '--help')
  end
  abort "Packaged CLI failed: #{output}" unless status.success? && %w[inputs migrate swpins].all? { |name| output.include?(name) }
  puts 'Packaged CLI help includes inputs, migration and software pin commands'
end

File.write(File.join(records, 'gem-files.txt'), files.join("\n") + "\n")
File.write(File.join(records, 'gem-metadata.json'), JSON.pretty_generate({
  name: spec.name,
  source_commit: source_commit,
  version: spec.version.to_s,
  required_ruby_version: spec.required_ruby_version.to_s,
  files: files.size,
  generated_files: extras,
  executables: spec.executables,
  runtime_dependencies: spec.runtime_dependencies.map { |dep| [dep.name, dep.requirement.to_s] }
}) + "\n")
puts "Verified #{files.size} package files and generated documentation"
