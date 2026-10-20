require_relative '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
require 'digest'
require 'time'
root = SecurityAdvisories::ROOT
parent_loader = File.join(__dir__, 'operator-period-parent-advisory.rb')
parent_evaluator = File.join(__dir__, 'operator-period-parent-evaluator.rb')
eval(File.read(parent_loader).sub('class Advisory', 'class CifsParentAdvisory'), TOPLEVEL_BINDING, parent_loader)
eval(File.read(parent_evaluator).sub('class Evaluator', 'class CifsParentEvaluator'), TOPLEVEL_BINDING, parent_evaluator)
snapshot_path = File.join(root, '.state/evidence.json')
expected = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
raise 'snapshot changed' unless Digest::SHA256.file(snapshot_path).hexdigest == expected
snapshot = JSON.parse(File.read(snapshot_path))
collection = Time.iso8601(snapshot.fetch('collected_at'))
now = Time.utc(2026, 10, 20, 12)
rows = %w[CVE-2026-64387 CVE-2026-53260 CVE-2026-72069].map do |cve|
  current = SecurityAdvisories::Advisory.load(cve)
  parent = SecurityAdvisories::CifsParentAdvisory.new(current.data, directory: current.directory).validate!
  old = SecurityAdvisories::CifsParentEvaluator.new(parent, now:, evidence_time: collection,
                                                   kernel_configurations: snapshot.fetch('kernel_configurations'))
                                            .evaluate(snapshot.fetch('nodes'))
  fresh = SecurityAdvisories::Evaluator.new(current, now:, evidence_time: collection,
                                           kernel_configurations: snapshot.fetch('kernel_configurations'))
                                     .evaluate(snapshot.fetch('nodes'))
  committed = JSON.parse(File.read(File.join(current.directory, 'evaluation.json')))
  raise "normal evaluation digest mismatch #{cve}" unless committed.fetch('dossier_digest') == current.digest
  raise "normal evaluation conclusions mismatch #{cve}" unless committed.fetch('nodes') == fresh.fetch('nodes')
  raise "normal evaluation completeness mismatch #{cve}" unless committed.fetch('completeness') == fresh.fetch('completeness')
  if cve == 'CVE-2026-64387'
    raise 'empty-role runtime drift' unless old == fresh
    raise 'CIFS is not fully excluded' unless fresh.dig('completeness', 'states') == { 'not_affected' => 13 }
  else
    raise 'parent did not remain conservative for RT' unless old.dig('completeness', 'states') == { 'mitigated' => 12, 'unknown' => 1 }
    raise 'current RT state drift' unless fresh.dig('completeness', 'states') == { 'mitigated' => 12, 'not_affected' => 1 }
  end
  { cve:, dossier_digest: current.digest, parent_states: old.dig('completeness', 'states'),
    current_states: fresh.dig('completeness', 'states'), full_normal_evaluation_conclusions_match: true,
    empty_role_old_current_identical: cve == 'CVE-2026-64387' ? old == fresh : nil }
end
# Synthetic absent metadata: preserve both exclusion and ordinary safety gates.
fixture = SecurityAdvisories::Advisory.load('CVE-2026-46242', root: File.join(root, 'spec/fixtures'))
prior = SecurityAdvisories::CifsParentAdvisory.new(fixture.data, directory: fixture.directory).validate!
nodes = %w[node storage].each_with_index.map do |role, index|
  { 'node_id' => index + 1, 'node_name' => "fixture-#{role}", 'node_role' => role }
end
synthetic = [[], ['node']].map do |roles|
  fixture.platform['affected_node_roles'] = roles
  previous = SecurityAdvisories::CifsParentEvaluator.new(prior, now:).evaluate(nodes)
  current = SecurityAdvisories::Evaluator.new(fixture, now:).evaluate(nodes)
  raise 'synthetic role semantics changed' unless previous == current
  expected_states = roles.empty? ? { 'not_affected' => 2 } : { 'unknown' => 1, 'not_affected' => 1 }
  raise 'synthetic role gate failed' unless current.dig('completeness', 'states') == expected_states
  { roles:, states: expected_states, old_current_identical: true }
end
raise 'snapshot changed during proof' unless Digest::SHA256.file(snapshot_path).hexdigest == expected
receipt = { parent_revision: 'cfef162049f632016c9e67bca0e400c58c8618d2', snapshot_sha256: expected,
            parent_loader_sha256: Digest::SHA256.file(parent_loader).hexdigest,
            parent_evaluator_sha256: Digest::SHA256.file(parent_evaluator).hexdigest,
            current_loader_sha256: Digest::SHA256.file(File.join(root, 'lib/security_advisories/advisory.rb')).hexdigest,
            current_evaluator_sha256: Digest::SHA256.file(File.join(root, 'lib/security_advisories/evaluator.rb')).hexdigest,
            evaluations: rows, synthetic_role_gates: synthetic,
            limits: 'Offline only, classes isolated by name with original bodies; schema1 CIFS unchanged runtime, RT old runtime conservatively unknown. No API or file evaluation writes by proof.' }
File.write(File.join(__dir__, 'operator-period-parent-proof.json'), JSON.pretty_generate(receipt) + "\n")
puts JSON.pretty_generate(receipt)
