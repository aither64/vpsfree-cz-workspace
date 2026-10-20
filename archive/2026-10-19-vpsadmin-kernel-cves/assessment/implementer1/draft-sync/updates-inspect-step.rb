# Local assertions for the three released updates. No API or remote writes.
require 'json'
require 'digest'
require 'yaml'
require 'fileutils'
require 'open3'
require '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
packet = __dir__
root = SecurityAdvisories::ROOT
prepared = JSON.parse(File.read("#{packet}/updates-prepared.json"))
phase, cve = ARGV
ledger_path = "#{packet}/updates-ledger.json"
git = lambda do |*args|
  out, status = Open3.capture2('git', '-C', root, *args)
  raise 'Git inspection failed' unless status.success?
  out.chomp
end
raise 'Wrong branch' unless git.call('branch', '--show-current') == '2026-10-19-vpsadmin-kernel-cves'
raise 'Frozen snapshot changed' unless Digest::SHA256.file("#{root}/.state/evidence.json").hexdigest == prepared['frozen_evidence_sha256']
raise 'Original ledger changed' unless Digest::SHA256.file("#{packet}/ledger.json").hexdigest == prepared['original_60_ledger_sha256']
raise 'Hook override' if %w[OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED OVERCOMMIT_SKIP OVERCOMMIT_ONLY SKIP ONLY SECURITY_ADVISORIES_SOURCE_COMMIT].any? { |key| ENV[key] && !ENV[key].empty? }
hooks = git.call('rev-parse', '--git-path', 'hooks')
raise 'Hooks missing' unless %w[pre-commit commit-msg].all? { |name| File.executable?(File.join(hooks, name)) }
raise 'Consumed ancestry lost' unless system('git', '-C', root, 'merge-base', '--is-ancestor', '8d1413efb041ab410d1a629c34d8aaf921439901', 'HEAD')
if phase == 'start'
  raise 'Already started' if File.exist?(ledger_path)
  raise 'Wrong released head' unless git.call('rev-parse', 'HEAD') == prepared['source_candidate']
  raise 'Dirty source/index' unless git.call('status', '--porcelain', '--untracked-files=all').empty?
  start = { 'source_head' => prepared['source_candidate'], 'submission_sha256' => Dir.glob("#{root}/advisories/*/submission.yml").to_h { |path| [path.delete_prefix("#{root}/"), Digest::SHA256.file(path).hexdigest] } }
  File.write("#{packet}/updates-start.json", JSON.pretty_generate(start) + "\n")
  File.write(ledger_path, JSON.pretty_generate({ 'count' => 0, 'rows' => [] }) + "\n")
  puts 'START exact released HEAD/clean source/frozen evidence/normal hooks/consumed ancestry PASS'
  exit
end
ledger = JSON.parse(File.read(ledger_path))
raise 'Out of exact update order' unless prepared['order'][ledger['rows'].length] == cve
row = prepared['rows'].find { |item| item['cve'] == cve }
expected = ledger['rows'].last&.fetch('checkpoint_sha') || prepared['source_candidate']
submission_path = "advisories/#{cve}/submission.yml"
%w[analysis.md advisory.yml evaluation.json].each do |name|
  raise 'Reviewed dossier/evaluation drift' unless Digest::SHA256.file("#{root}/advisories/#{cve}/#{name}").hexdigest == row['file_sha256'][name]
end
advisory = SecurityAdvisories::Advisory.load(cve)
evaluation = JSON.parse(File.read("#{root}/advisories/#{cve}/evaluation.json"))
raise 'Dossier digest mismatch' unless advisory.digest == row['dossier_digest'] && evaluation['dossier_digest'] == advisory.digest
raise 'Wrong node counts' unless evaluation['nodes'].length == 13 && evaluation['completeness']['states'] == row['desired_node_counts']
old_path = "#{root}/.state/draft-sync/#{cve}/apply.json"
raise 'Retained readback changed' unless Digest::SHA256.file(old_path).hexdigest == row['retained_remote_snapshot_sha256']
old = JSON.parse(File.read(old_path))
public_keys = %w[name en_summary en_description en_response cs_summary cs_description cs_response]
raise 'Public attributes changed' unless advisory.advisory_attributes == old['advisory'].slice(*public_keys)
raw = "#{root}/.state/draft-sync-followup/#{cve}"
reconciler = SecurityAdvisories::Reconciler.new(client: nil)
case phase
when 'guard'
  raise 'Unexpected HEAD' unless git.call('rev-parse', 'HEAD') == expected
  raise 'Dirty source/index' unless git.call('status', '--porcelain', '--untracked-files=all').empty?
  raise 'Prior baseline changed' unless Digest::SHA256.file("#{root}/#{submission_path}").hexdigest == row['file_sha256']['submission.yml']
  baseline = YAML.safe_load_file("#{root}/#{submission_path}")
  raise 'Wrong prior draft/revision/digest' unless baseline['schema_version'] == 2 && baseline['advisory_id'] == row['advisory_id'] && baseline['remote_content_revision'] == 13 && baseline['remote_digest'] == row['previous_remote_digest']
  FileUtils.mkdir_p(raw, mode: 0o700)
  puts "GUARD #{cve} id=#{row['advisory_id']} priorrevision=13 HEAD=#{expected} clean snapshot/hooks/digests/order PASS"
when 'plan'
  raise 'Dry-run changed source' unless git.call('status', '--porcelain', '--untracked-files=all').empty? && git.call('rev-parse', 'HEAD') == expected
  plan = JSON.parse(File.read("#{raw}/dry-run.json"))
  raise 'Wrong update plan' unless plan['dry_run'] == true && plan['create_advisory'] == false && plan['advisory_id'] == row['advisory_id'] && plan['cve'] == cve
  raise 'Plan texts/digest differ' unless plan['advisory'] == advisory.advisory_attributes && plan['dossier_digest'] == advisory.digest
  desired = evaluation['nodes'].map { |node| reconciler.send(:desired_node_status_attributes, node).merge('node' => node['node_id']) }
  raise 'Plan node rows differ' unless plan['node_statuses'] == desired
  puts "PLAN #{cve} id=#{row['advisory_id']} create=false exacttexts/13nodes PASS states=#{row['desired_node_counts']}"
when 'readback', 'checkpoint'
  snapshot = JSON.parse(File.read("#{raw}/apply.json"))
  parent = snapshot.fetch('advisory')
  raise 'Unexpected remote identity/state/revision' unless parent['state'] == 'draft' && parent['external_id'] == "vpsfreecz/security-advisories/#{cve}" && parent['id'] == row['advisory_id'] && parent['content_revision'] == row['predicted_content_revision']
  reconciler.send(:verify_desired_snapshot!, advisory, evaluation, snapshot)
  raise 'CVE association identity changed' unless snapshot['cves'] == old['cves']
  raise 'Node row identities changed' unless snapshot['node_statuses'].to_h { |node| [node['node_id'], node['id']] } == old['node_statuses'].to_h { |node| [node['node_id'], node['id']] }
  baseline = YAML.safe_load_file("#{root}/#{submission_path}")
  raise 'New baseline mismatch' unless baseline['schema_version'] == 2 && baseline['advisory_id'] == parent['id'] && baseline['remote_content_revision'] == parent['content_revision'] && baseline['remote_digest'] == snapshot['digest'] && baseline['dossier_digest'] == advisory.digest && baseline['source_commit'] == expected
  if phase == 'readback'
    raise 'HEAD changed' unless git.call('rev-parse', 'HEAD') == expected
    changed = git.call('status', '--porcelain', '--untracked-files=all').lines
    raise 'Unexpected changed paths' unless changed.length == 1 && changed.first[3..].strip == submission_path
    puts "READBACK #{cve} id=#{parent['id']} draft revision=#{parent['content_revision']} exactCVE/externalID/texts/13nodes/times/notes/childIDs/schema2 PASS"
  else
    head = git.call('rev-parse', 'HEAD')
    raise 'Wrong checkpoint parent/path' unless git.call('rev-parse', 'HEAD^') == expected && git.call('diff-tree', '--no-commit-id', '--name-status', '-r', 'HEAD') == "M\t#{submission_path}"
    raise 'Dirty source/index' unless git.call('status', '--porcelain', '--untracked-files=all').empty?
    log = File.read("#{raw}/commit.log")
    raise 'Normal hook success absent' unless log.include?('All pre-commit hooks passed') && log.include?('All commit-msg hooks passed')
    ledger['rows'] << { 'cve' => cve, 'advisory_id' => parent['id'], 'state' => parent['state'], 'content_revision' => parent['content_revision'], 'checkpoint_sha' => head, 'node_counts' => row['desired_node_counts'] }
    ledger['count'] = ledger['rows'].length
    File.write(ledger_path, JSON.pretty_generate(ledger) + "\n")
    puts "CHECKPOINT #{ledger['count']}/3 #{cve} id=#{parent['id']} draft revision=#{parent['content_revision']} HEAD=#{head} clean normalhooksPASS"
  end
else
  raise 'Unknown operator assertion phase'
end
