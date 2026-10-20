# Local operator assertions only: no API client or reconciliation writes.
require 'json'
require 'digest'
require 'yaml'
require 'fileutils'
require 'open3'
require '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
root = SecurityAdvisories::ROOT
packet = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves/assessment/implementer1/draft-sync'
phase, cve = ARGV
order = JSON.parse(File.read("#{packet}/order.json"))['cves']
ledger = JSON.parse(File.read("#{packet}/ledger.json"))
raise 'Out of approved order' unless order[ledger['rows'].length] == cve
expected = ledger['rows'].last&.fetch('checkpoint_sha') || 'd23040cd3f3e8e33677dafdeb8e59cc83466e17b'
git = lambda do |*args|
  out, status = Open3.capture2('git', '-C', root, *args)
  raise 'Git inspection failed' unless status.success?
  out.strip
end
raise 'Wrong branch' unless git.call('branch', '--show-current') == '2026-10-19-vpsadmin-kernel-cves'
raise 'Frozen snapshot changed' unless Digest::SHA256.file("#{root}/.state/evidence.json").hexdigest == '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
raise 'Hook environment override' if %w[OVERCOMMIT_DISABLE OVERCOMMIT_DISABLED OVERCOMMIT_SKIP OVERCOMMIT_ONLY SKIP ONLY SECURITY_ADVISORIES_SOURCE_COMMIT].any? { |key| ENV[key] && !ENV[key].empty? }
hooks = git.call('rev-parse', '--git-path', 'hooks')
raise 'Hooks missing' unless %w[pre-commit commit-msg].all? { |name| File.executable?(File.join(hooks, name)) }
advisory = SecurityAdvisories::Advisory.load(cve)
evaluation = JSON.parse(File.read("#{root}/advisories/#{cve}/evaluation.json"))
raise 'Dossier digest differs' unless evaluation['dossier_digest'] == advisory.digest
raise 'Unexpected node count' unless evaluation['nodes'].length == 13
raw = "#{root}/.state/draft-sync/#{cve}"
submission_path = "advisories/#{cve}/submission.yml"
reconciler = SecurityAdvisories::Reconciler.new(client: nil)
case phase
when 'guard'
  raise 'Unexpected HEAD' unless git.call('rev-parse', 'HEAD') == expected
  raise 'Dirty source/index' unless git.call('status', '--porcelain', '--untracked-files=all').empty?
  raise 'Unexpected baseline' if File.exist?("#{root}/#{submission_path}")
  FileUtils.mkdir_p(raw, mode: 0o700)
  puts "GUARD #{cve} HEAD=#{expected} clean snapshot/hooks/digest/order PASS"
when 'plan'
  raise 'Dry-run dirtied source' unless git.call('status', '--porcelain', '--untracked-files=all').empty?
  raise 'HEAD changed' unless git.call('rev-parse', 'HEAD') == expected
  plan = JSON.parse(File.read("#{raw}/dry-run.json"))
  raise 'Unexpected existing draft or plan' unless plan['dry_run'] == true && plan['create_advisory'] == true && plan['advisory_id'].nil? && plan['cve'] == cve
  raise 'Plan texts/digest differ' unless plan['advisory'] == advisory.advisory_attributes && plan['dossier_digest'] == advisory.digest
  desired = evaluation['nodes'].map { |row| reconciler.send(:desired_node_status_attributes, row).merge('node' => row['node_id']) }
  raise 'Plan nodes differ' unless plan['node_statuses'] == desired
  puts "PLAN #{cve} create=true texts/exactnodes PASS states=#{evaluation['completeness']['states']}"
when 'readback'
  raise 'HEAD changed' unless git.call('rev-parse', 'HEAD') == expected
  snapshot = JSON.parse(File.read("#{raw}/apply.json"))
  parent = snapshot.fetch('advisory')
  raise 'Unexpected remote identity/state' unless parent['state'] == 'draft' && parent['external_id'] == "vpsfreecz/security-advisories/#{cve}" && parent['id'].is_a?(Integer) && parent['content_revision'].is_a?(Integer)
  reconciler.send(:verify_desired_snapshot!, advisory, evaluation, snapshot)
  baseline = YAML.safe_load_file("#{root}/#{submission_path}")
  raise 'Baseline differs' unless baseline['schema_version'] == 2 && baseline['advisory_id'] == parent['id'] && baseline['remote_content_revision'] == parent['content_revision'] && baseline['remote_digest'] == snapshot['digest'] && baseline['dossier_digest'] == advisory.digest && baseline['source_commit'] == expected
  changed = git.call('status', '--porcelain', '--untracked-files=all').lines
  raise 'Unexpected changed paths' unless changed.length == 1 && changed.first[3..].strip == submission_path
  puts "READBACK #{cve} id=#{parent['id']} state=draft revision=#{parent['content_revision']} exactCVE/texts/13nodes/times/notes/baseline PASS"
when 'checkpoint'
  head = git.call('rev-parse', 'HEAD')
  raise 'Wrong checkpoint parent' unless git.call('rev-parse', 'HEAD^') == expected
  raise 'Wrong checkpoint paths' unless git.call('diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD') == submission_path
  raise 'Dirty source/index' unless git.call('status', '--porcelain', '--untracked-files=all').empty?
  snapshot = JSON.parse(File.read("#{raw}/apply.json"))
  parent = snapshot.fetch('advisory')
  reconciler.send(:verify_desired_snapshot!, advisory, evaluation, snapshot)
  ledger['rows'] << { 'cve' => cve, 'advisory_id' => parent['id'], 'state' => parent['state'], 'content_revision' => parent['content_revision'], 'checkpoint_sha' => head, 'node_counts' => evaluation['completeness']['states'] }
  ledger['count'] = ledger['rows'].length
  File.write("#{packet}/ledger.json", JSON.pretty_generate(ledger) + "\n")
  puts "CHECKPOINT #{ledger['count']}/60 #{cve} id=#{parent['id']} draft revision=#{parent['content_revision']} HEAD=#{head} clean"
else
  raise 'Unknown local inspection phase'
end
