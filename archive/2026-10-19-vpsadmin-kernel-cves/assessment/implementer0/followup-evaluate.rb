require 'json'
require 'digest'
require 'fileutils'
require File.join(Dir.pwd, 'lib/security_advisories')

session = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves'
owned = %w[CVE-2026-53260 CVE-2026-72069 CVE-2026-74753]
expected = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
raise 'frozen evidence changed' unless Digest::SHA256.file('.state/evidence.json').hexdigest == expected
FileUtils.mkdir_p('.state/implementer0', mode: 0o700)
owned.each do |cve|
  %w[validate evaluate].each do |action|
    path = ".state/implementer0/followup-#{cve}-#{action}.log"
    ok = File.open(path, File::WRONLY | File::CREAT | File::TRUNC, 0o600) do |log|
      system('bin/security-advisory', action, cve, out: log, err: log)
    end
    raise "#{action} failed for #{cve}; restricted log #{path}" unless ok
  end
end
if ARGV.include?('--owned-only')
  owned.each do |cve|
    result = JSON.parse(File.read("advisories/#{cve}/evaluation.json"))
    raise 'stale dossier digest' unless result['dossier_digest'] == SecurityAdvisories::Advisory.load(cve).digest

    puts "#{cve}: #{result.dig('completeness', 'states')}"
  end
  exit
end
baseline = JSON.parse(File.read(File.join(session, 'assessment/implementer0/followup-baseline-evaluations.json')))
ids = JSON.parse(File.read(File.join(session, 'approved-cves.json'))).fetch('cves')
reconciler = SecurityAdvisories::Reconciler.new(client: nil)
rows = ids.map do |cve|
  advisory = SecurityAdvisories::Advisory.load(cve)
  result = reconciler.evaluate(advisory, persist: false)
  old = baseline.fetch(cve)
  keys = %w[dossier_digest evaluated_at]
  changes = result.fetch('nodes').zip(old.fetch('nodes')).filter_map do |current, previous|
    next if current == previous

    { 'node_id' => current['node_id'], 'before_state' => previous['state'], 'after_state' => current['state'],
      'changed_fields' => (current.keys | previous.keys).select { |key| current[key] != previous[key] } }
  end
  {
    'cve' => cve,
    'all_conclusion_fields_unchanged' => result.except(*keys) == old.except(*keys),
    'changed_nodes' => changes,
    'states' => result.dig('completeness', 'states')
  }
end
raise 'unexpected conclusion drift' if rows.any? do |row|
  !row['all_conclusion_fields_unchanged'] && !owned.include?(row['cve'])
end
rows.select { |row| %w[CVE-2026-53260 CVE-2026-72069].include?(row['cve']) }.each do |row|
  raise 'RT drift beyond scoped operator note' unless row['changed_nodes'] == [
    { 'node_id' => 161, 'before_state' => 'unknown', 'after_state' => 'unknown', 'changed_fields' => ['notes'] }
  ]
end
baselines = JSON.parse(File.read(File.join(session, 'assessment/implementer0/followup-baseline-submissions.json')))
raise 'consumed baseline changed' unless baselines.all? { |path, hash| Digest::SHA256.file(path).hexdigest == hash }
raise 'frozen evidence changed' unless Digest::SHA256.file('.state/evidence.json').hexdigest == expected
receipt = { 'snapshot_sha256' => expected, 'persisted_normal_cli_cves' => owned,
            'comparison' => 'All approved60 evaluated in memory by normal Reconciler without API/persist',
            'unchanged_other59' => rows.reject { |r| r['cve'] == 'CVE-2026-74753' }.count { |r| r['all_conclusion_fields_unchanged'] },
            'other59_outcomes_unchanged_except_two_RT_storage_notes' => true,
            'rows' => rows, 'consumed_submission_baselines_unchanged' => true }
File.write(File.join(session, 'assessment/implementer0/followup-evaluation-comparison.json'), JSON.pretty_generate(receipt) + "\n")
owned.each { |cve| puts "#{cve}: #{rows.find { |r| r['cve'] == cve }.fetch('states')}" }
puts "Unchanged other59: #{receipt['unchanged_other59']}"
