require_relative '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
require 'digest'
root = SecurityAdvisories::ROOT
fixture_root = File.join(root, 'spec/fixtures')
old_loader = File.join(__dir__, 'followup-runtime/advisory-old.rb')
old_evaluator = File.join(__dir__, 'followup-runtime/evaluator-old.rb')
eval(File.read(old_loader).sub('class Advisory', 'class PriorRoleAdvisory'), TOPLEVEL_BINDING, old_loader)
eval(File.read(old_evaluator).sub('class Evaluator', 'class PriorRoleEvaluator'), TOPLEVEL_BINDING, old_evaluator)
base = SecurityAdvisories::Advisory.load('CVE-2026-46242', root: fixture_root)
base.platform['affected_node_roles'] = []
base.validate!
prior = SecurityAdvisories::PriorRoleAdvisory.new(base.data, directory: base.directory).validate!
raise 'schema changed' unless base.data.fetch('schema_version') == 1
# Deliberately omit kernel, history, freshness and closure facts: role exclusion
# must not manufacture or require them. These are synthetic fixture Nodes only.
nodes = %w[node storage].each_with_index.map do |role, index|
  { 'node_id' => index + 1, 'node_name' => "fixture-#{role}", 'node_role' => role }
end
now = Time.utc(2026, 10, 20)
old = SecurityAdvisories::PriorRoleEvaluator.new(prior, now:).evaluate(nodes)
current = SecurityAdvisories::Evaluator.new(base, now:).evaluate(nodes)
raise 'role-exclusion semantics changed' unless old == current
raise 'not all roles excluded' unless current.fetch('nodes').all? { |row| row.fetch('state') == 'not_affected' }
base.platform['affected_node_roles'] = ['node']
prior.platform['affected_node_roles'] = ['node']
old_nonempty = SecurityAdvisories::PriorRoleEvaluator.new(prior, now:).evaluate(nodes)
current_nonempty = SecurityAdvisories::Evaluator.new(base, now:).evaluate(nodes)
raise 'nonempty role semantics changed' unless old_nonempty == current_nonempty
raise 'freshness/history bypassed' unless current_nonempty.fetch('nodes').first.fetch('state') == 'unknown'
raise 'storage role gate changed' unless current_nonempty.fetch('nodes').last.fetch('state') == 'not_affected'
receipt = {
  old_runtime_revision: '8d1413ef', old_loader_sha256: Digest::SHA256.file(old_loader).hexdigest,
  old_evaluator_sha256: Digest::SHA256.file(old_evaluator).hexdigest,
  current_loader_sha256: Digest::SHA256.file(File.join(root, 'lib/security_advisories/advisory.rb')).hexdigest,
  current_evaluator_sha256: Digest::SHA256.file(File.join(root, 'lib/security_advisories/evaluator.rb')).hexdigest,
  schema_version: 1, empty_role_loader_old_current: 'PASS',
  empty_role_evaluation_old_current_identical: true, empty_role_states: current.dig('completeness', 'states'),
  nonempty_role_evaluation_old_current_identical: true, nonempty_role_states: current_nonempty.dig('completeness', 'states'),
  limits: 'Offline synthetic fixture only; old classes isolated by name, unchanged method bodies. No assertion about CIFS historical scope and no production evidence/API read or mutation.'
}
File.write(File.join(__dir__, 'followup-empty-roles-proof.json'), JSON.pretty_generate(receipt) + "\n")
puts JSON.pretty_generate(receipt)
