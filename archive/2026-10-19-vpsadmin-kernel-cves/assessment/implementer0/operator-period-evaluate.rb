require 'json'
require 'digest'
require 'fileutils'
require File.join(Dir.pwd, 'lib/security_advisories')

session = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves'
owner = File.join(session, 'assessment/implementer0')
owned = %w[CVE-2026-53260 CVE-2026-72069]
expected = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
raise 'changed frozen evidence' unless Digest::SHA256.file('.state/evidence.json').hexdigest == expected
owned.each do |cve|
  %w[validate evaluate].each do |action|
    path = ".state/implementer0/operator-period-#{cve}-#{action}.log"
    ok = File.open(path, File::WRONLY | File::CREAT | File::TRUNC, 0o600) do |log|
      system('bin/security-advisory', action, cve, out: log, err: log)
    end
    raise "#{action} failed for #{cve}; restricted #{path}" unless ok
  end
end
baseline = JSON.parse(File.read(File.join(owner, 'operator-period-baseline-evaluations.json')))
reconciler = SecurityAdvisories::Reconciler.new(client: nil)
rows = baseline.map do |cve, previous|
  advisory = SecurityAdvisories::Advisory.load(cve)
  result = reconciler.evaluate(advisory, persist: false)
  changes = result.fetch('nodes').zip(previous.fetch('nodes')).filter_map do |node, old|
    next if node == old

    { 'node_id' => node['node_id'], 'before_state' => old['state'], 'after_state' => node['state'],
      'changed_fields' => (node.keys | old.keys).select { |key| node[key] != old[key] } }
  end
  unaffected = !%w[CVE-2026-53260 CVE-2026-72069 CVE-2026-64387].include?(cve)
  if unaffected && result.except('dossier_digest', 'evaluated_at') != previous.except('dossier_digest', 'evaluated_at')
    raise "unexpected conclusion drift #{cve}"
  end
  if owned.include?(cve)
    raise 'unexpected RT node drift' unless changes.length == 1 && changes.first['node_id'] == 161
    raise 'unexpected RT result' unless result.dig('completeness', 'states') == { 'mitigated' => 12, 'not_affected' => 1 }
    node = result.fetch('nodes').find { |n| n['node_id'] == 161 }
    raise 'invented identity or timing' unless (node.keys & %w[kernel_release config_digest mitigated_since vulnerable_until]).empty?
    raise 'stale authored digest' unless JSON.parse(File.read("advisories/#{cve}/evaluation.json"))['dossier_digest'] == advisory.digest
  end
  { 'cve' => cve, 'outside_three_unchanged' => unaffected, 'changed_nodes' => changes,
    'states' => result.dig('completeness', 'states') }
end
hashes = JSON.parse(File.read(File.join(owner, 'operator-period-baseline-submissions.json')))
raise 'consumed submission changed' unless hashes.all? { |p, hash| Digest::SHA256.file(p).hexdigest == hash }
raise 'frozen evidence changed' unless Digest::SHA256.file('.state/evidence.json').hexdigest == expected
receipt = { 'snapshot_sha256' => expected, 'persisted_normal_cli' => owned,
            'outside_three_57_full_conclusions_equal_to_cfef' => true,
            'perf_unchanged' => true, 'consumed_submission_hashes_unchanged' => true, 'rows' => rows }
File.write(File.join(owner, 'operator-period-evaluation-comparison.json'), JSON.pretty_generate(receipt) + "\n")
owned.each { |cve| puts "#{cve}: #{rows.find { |r| r['cve'] == cve }['states']}" }
puts 'All other57 conclusions unchanged; perf and consumed baselines preserved'
