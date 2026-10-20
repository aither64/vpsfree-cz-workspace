require_relative '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
require 'json'
require 'digest'
session_root = File.expand_path('../..', __dir__)
root = SecurityAdvisories::ROOT
ids = JSON.parse(File.read(File.join(session_root, 'assessment/packages.json'))).fetch('groups').fetch('implementer2')
requirements = JSON.parse(File.read(File.join(__dir__, 'requirements.json'))).fetch('rows').to_h { |row| [row.fetch('cve'), row] }
evidence_path = File.join(root, '.state/evidence.json')
raise 'frozen snapshot changed' unless Digest::SHA256.file(evidence_path).hexdigest == '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
evidence = JSON.parse(File.read(evidence_path))
rows = ids.map do |cve|
  advisory = SecurityAdvisories::Advisory.load(cve)
  evaluation = JSON.parse(File.read(File.join(root, 'advisories', cve, 'evaluation.json')))
  raise "digest mismatch #{cve}" unless evaluation.fetch('dossier_digest') == advisory.digest
  raise "snapshot mismatch #{cve}" unless evaluation.fetch('evidence_digest') == evidence.fetch('evidence_digest')
  %w[required_options required_sysctls history_required_since affected_node_roles].each do |field|
    raise "declaration mismatch #{cve}:#{field}" unless advisory.platform.fetch(field) == requirements.fetch(cve).fetch(field)
  end
  raise "unexpected override #{cve}" unless advisory.platform.fetch('history_start_overrides').keys == ['126']
  raise "incomplete node set #{cve}" unless evaluation.dig('completeness', 'node_set_complete') && evaluation.fetch('nodes').length == 13
  { cve:, dossier_digest: advisory.digest, states: evaluation.dig('completeness', 'states'), declaration_match: true }
end
receipt = { snapshot_sha256: Digest::SHA256.file(evidence_path).hexdigest, rows:, count: rows.length,
            check: 'normal loader validation, dossier/evaluation digests, evidence digest, requirements equality and exact Node126-only override PASS' }
File.write(File.join(__dir__, 'final-package-checks.json'), JSON.pretty_generate(receipt) + "\n")
puts "20 owned dossiers and evaluations: final digest/catalog/scope checks PASS"
