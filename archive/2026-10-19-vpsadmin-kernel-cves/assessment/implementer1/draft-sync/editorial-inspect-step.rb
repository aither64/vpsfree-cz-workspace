# Local assertions only for the released editorial three updates; no API calls.
require 'json'
require 'yaml'
require 'digest'
require 'fileutils'
require 'open3'
require '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
packet = __dir__
root = SecurityAdvisories::ROOT
prepared = JSON.parse(File.read("#{packet}/editorial-prepared.json"))
source = prepared.fetch('released_source_head')
raise 'No matching release binding' unless source == 'aa15ba719513d54c1e7942a085504777e4b7abfd' && source == prepared['source_candidate']
phase, cve = ARGV
git = lambda do |*args|
  out, status = Open3.capture2('git', '-C', root, *args)
  raise 'Git inspection failed' unless status.success?
  out.chomp
end
raise 'Wrong branch' unless git.call('branch', '--show-current') == '2026-10-19-vpsadmin-kernel-cves'
raise 'Frozen evidence changed' unless Digest::SHA256.file("#{root}/.state/evidence.json").hexdigest == prepared['frozen_evidence_sha256']
raise 'Original ledger changed' unless Digest::SHA256.file("#{packet}/ledger.json").hexdigest == prepared['prior_ledger_sha256']['ledger.json']
raise 'Previous update ledger changed' unless Digest::SHA256.file("#{packet}/updates-ledger.json").hexdigest == prepared['prior_ledger_sha256']['updates-ledger.json']
raise 'Previous final-three ledger changed' unless Digest::SHA256.file("#{packet}/final-three-ledger.json").hexdigest == prepared['prior_ledger_sha256']['final-three-ledger.json']
raise 'Hook/source override' if %w[OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED OVERCOMMIT_SKIP OVERCOMMIT_ONLY SKIP ONLY SECURITY_ADVISORIES_SOURCE_COMMIT].any? { |key| ENV[key] && !ENV[key].empty? }
hooks = git.call('rev-parse', '--git-path', 'hooks')
raise 'Hooks inactive' unless %w[pre-commit commit-msg].all? { |name| File.executable?(File.join(hooks, name)) }
raise 'Consumed prefix lost' unless system('git', '-C', root, 'merge-base', '--is-ancestor', prepared['preserved_consumed_head'], 'HEAD')
ledger_path = "#{packet}/editorial-ledger.json"
ledger = File.exist?(ledger_path) ? JSON.parse(File.read(ledger_path)) : { 'count' => 0, 'rows' => [] }
if %w[start guard plan].include?(phase)
  completed = ledger['rows'].map { |row| "advisories/#{row['cve']}/submission.yml" }
  prepared['starting_submission_sha256'].each do |path, sha|
    next if completed.include?(path)
    raise 'Unexpected starting baseline drift' unless Digest::SHA256.file("#{root}/#{path}").hexdigest == sha
  end
end
if phase == 'start'
  raise 'Already started' if File.exist?(ledger_path)
  raise 'Wrong source HEAD' unless git.call('rev-parse', 'HEAD') == source
  raise 'Wrong source feature count' unless git.call('rev-list', '--count', "ea6247687fd02417f87e1e5593fecd8b9055925d..HEAD") == '78'
  raise 'Dirty worktree/index' unless git.call('status', '--porcelain', '--untracked-files=all').empty?
  old = prepared['prior_ledger_sha256'].keys.flat_map { |name| JSON.parse(File.read("#{packet}/#{name}"))['rows'] }
  ancestors = git.call('rev-list', 'HEAD').lines.map(&:chomp)
  raise 'Old recovery boundaries lost' unless old.length == 66 && old.all? { |row| ancestors.include?(row['checkpoint_sha']) }
  raw = " M advisories/CVE-2026-53260/submission.yml\n"
  raise 'Porcelain whitespace handling broken' unless raw.chomp[3..] == 'advisories/CVE-2026-53260/submission.yml'
  File.write(ledger_path, JSON.pretty_generate(ledger) + "\n")
  puts 'START exact78-commit released source/clean index+worktree/111baselines/66oldboundaries/frozen61904/hooks/chomp PASS'
  exit
end
raise 'Wrong exact order' unless prepared['order'][ledger['rows'].length] == cve
row = prepared['rows'].find { |item| item['cve'] == cve }
expected = ledger['rows'].last&.fetch('checkpoint_sha') || source
path = "advisories/#{cve}/submission.yml"
%w[analysis.md advisory.yml evaluation.json].each do |name|
  raise 'Reviewed file drift' unless Digest::SHA256.file("#{root}/advisories/#{cve}/#{name}").hexdigest == row['file_sha256'][name]
end
advisory = SecurityAdvisories::Advisory.load(cve)
evaluation = JSON.parse(File.read("#{root}/advisories/#{cve}/evaluation.json"))
raise 'Dossier digest mismatch' unless advisory.digest == row['desired_dossier_digest'] && evaluation['dossier_digest'] == advisory.digest
raise 'Public attributes differ' unless advisory.advisory_attributes == row['desired_public_attributes']
raise 'Node counts differ' unless evaluation['nodes'].length == 13 && evaluation['completeness']['states'] == row['desired_node_counts']
reconciler = SecurityAdvisories::Reconciler.new(client: nil)
desired = evaluation['nodes'].map { |node| reconciler.send(:desired_node_status_attributes, node).merge('node' => node['node_id']) }
raise 'Desired node fields differ' unless desired == row['desired_node_projection']
raise 'RT notes remain' if cve != 'CVE-2026-64387' && desired.any? { |node| node['en_note'] || node['cs_note'] }
old_path = row['retained_snapshot_path']
raise 'Old raw receipt changed' unless Digest::SHA256.file(old_path).hexdigest == row['retained_snapshot_sha256']
old = JSON.parse(File.read(old_path))
raw_dir = "#{root}/.state/draft-sync-editorial/#{cve}"
case phase
when 'guard'
  raise 'Unexpected HEAD' unless git.call('rev-parse', 'HEAD') == expected
  raise 'Dirty source/index' unless git.call('status', '--porcelain', '--untracked-files=all').empty?
  baseline = YAML.safe_load_file("#{root}/#{path}")
  raise 'Prior baseline mismatch' unless baseline['schema_version'] == 2 && baseline['advisory_id'] == row['advisory_id'] && baseline['remote_content_revision'] == row['previous_content_revision'] && baseline['remote_digest'] == row['previous_remote_digest']
  FileUtils.mkdir_p(raw_dir, mode: 0o700)
  puts "GUARD #{cve} id=#{row['advisory_id']} revision=#{row['previous_content_revision']} HEAD=#{expected} clean/frozen/baselines/hooks/fields PASS"
when 'plan'
  raise 'Dry-run changed source' unless git.call('rev-parse', 'HEAD') == expected && git.call('status', '--porcelain', '--untracked-files=all').empty?
  plan = JSON.parse(File.read("#{raw_dir}/dry-run.json"))
  raise 'Unexpected create/identity' unless plan['dry_run'] == true && plan['create_advisory'] == false && plan['advisory_id'] == row['advisory_id'] && plan['cve'] == cve
  raise 'Plan public/digest/node fields differ' unless plan['advisory'] == row['desired_public_attributes'] && plan['dossier_digest'] == advisory.digest && plan['node_statuses'] == desired
  puts "PLAN #{cve} id=#{row['advisory_id']} create=false exactpublic/13nodes PASS states=#{row['desired_node_counts']} predictedrevision=#{row['expected_final_revision']}"
when 'readback', 'checkpoint'
  snapshot = JSON.parse(File.read("#{raw_dir}/apply.json"))
  parent = snapshot.fetch('advisory')
  raise 'Remote identity/state/revision drift' unless parent['id'] == row['advisory_id'] && parent['state'] == 'draft' && parent['content_revision'] == row['expected_final_revision'] && parent['external_id'] == "vpsfreecz/security-advisories/#{cve}"
  reconciler.send(:verify_desired_snapshot!, advisory, evaluation, snapshot)
  raise 'CVE child identities changed' unless snapshot['cves'] == old['cves']
  raise 'Node child identities changed' unless snapshot['node_statuses'].to_h { |node| [node['node_id'], node['id']] } == old['node_statuses'].to_h { |node| [node['node_id'], node['id']] }
  baseline = YAML.safe_load_file("#{root}/#{path}")
  raise 'New schema2 baseline mismatch' unless baseline['schema_version'] == 2 && baseline['advisory_id'] == parent['id'] && baseline['remote_content_revision'] == parent['content_revision'] && baseline['remote_digest'] == snapshot['digest'] && baseline['dossier_digest'] == advisory.digest && baseline['source_commit'] == expected
  if phase == 'readback'
    raise 'HEAD changed' unless git.call('rev-parse', 'HEAD') == expected
    raise 'Unexpected changed paths' unless git.call('status', '--porcelain', '--untracked-files=all').lines.map(&:chomp) == [" M #{path}"]
    puts "READBACK #{cve} id=#{parent['id']} draft revision=#{parent['content_revision']} exactCVE/externalID/ENCS/13nodes/times/notes/childIDs/schema2 PASS"
  else
    head = git.call('rev-parse', 'HEAD')
    raise 'Checkpoint lineage/scope mismatch' unless git.call('rev-parse', 'HEAD^') == expected && git.call('diff-tree', '--no-commit-id', '--name-status', '-r', 'HEAD') == "M\t#{path}"
    raise 'Dirty source/index' unless git.call('status', '--porcelain', '--untracked-files=all').empty?
    log = File.read("#{raw_dir}/commit.log")
    raise 'Normal hook pass missing' unless log.include?('All pre-commit hooks passed') && log.include?('All commit-msg hooks passed')
    ledger['rows'] << { 'cve' => cve, 'advisory_id' => parent['id'], 'state' => parent['state'], 'content_revision' => parent['content_revision'], 'checkpoint_sha' => head, 'node_counts' => row['desired_node_counts'] }
    ledger['count'] = ledger['rows'].length
    File.write(ledger_path, JSON.pretty_generate(ledger) + "\n")
    puts "CHECKPOINT #{ledger['count']}/3 #{cve} id=#{parent['id']} draft revision=#{parent['content_revision']} HEAD=#{head} clean normalhooksPASS"
  end
else
  raise 'Unknown local assertion phase'
end
