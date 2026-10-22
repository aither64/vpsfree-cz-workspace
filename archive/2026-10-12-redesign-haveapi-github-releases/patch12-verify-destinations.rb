require File.join(Dir.pwd, 'utils/release/publish')

records = ARGV.fetch(0)
originals = File.join(records, 'patch12-tag-artifacts')
artifacts = HaveAPI::Release::Artifacts.new(Dir.pwd)
publisher = HaveAPI::Release::Publisher.new(artifacts, originals)
receipt = { 'source' => artifacts.source, 'version' => artifacts.version, 'tag' => artifacts.tag }
receipt['gems'] = HaveAPI::Release::GEMS.keys.to_h do |name|
  raise "Missing published gem: #{name}" unless publisher.gem_present?(name)
  puts "Verified published gem checksum: #{name}"
  [name, true]
end
raise 'Missing published npm version' unless publisher.npm_present?
receipt['npm_integrity_matches'] = true
puts 'Verified npm identity and retained tarball integrity'

Dir.mktmpdir('haveapi-0.29.12-publication-verification-') do |tmp|
  mirror = File.join(tmp, 'mirror')
  HaveAPI::Release.run('git', 'clone', '--quiet', '--branch', 'master', HaveAPI::Release::PHP_REPOSITORY, mirror)
  raise 'Published PHP tag not found' unless publisher.preflight_php(mirror)
  commit = HaveAPI::Release.capture('git', 'rev-parse', "#{artifacts.tag}^{}", chdir: mirror).strip
  head = HaveAPI::Release.capture('git', 'rev-parse', 'HEAD', chdir: mirror).strip
  raise 'PHP master does not match the released tag; inspect concurrent updates' unless head == commit
  receipt['php_commit'] = commit
  receipt['php_snapshot_and_source_match'] = true
  puts "Verified PHP tag snapshot, source provenance and master: #{commit}"
end

release = publisher.github_release
raise 'GitHub Release is not public' unless release && release.fetch('draft') == false
raise 'GitHub Release tag differs' unless release.fetch('tag_name') == artifacts.tag
File.write(File.join(records, 'patch12-public-github-release.json'), JSON.pretty_generate(release) + "\n")
receipt['github_release_id'] = release.fetch('id')
File.write(File.join(records, 'patch12-destination-helper-receipt.json'), JSON.pretty_generate(receipt) + "\n")
puts "Verified public GitHub Release lookup: #{release.fetch('html_url')}"
