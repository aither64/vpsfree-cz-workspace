require_relative '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
require 'digest'
root = SecurityAdvisories::ROOT
session_root = File.expand_path('../..', __dir__)
paths = Dir.glob(File.join(root, 'advisories', 'CVE-*'))
raise 'inventory not111' unless paths.length == 111
rows = paths.map do |path|
  advisory = SecurityAdvisories::Advisory.load(File.basename(path))
  evaluation = JSON.parse(File.read(File.join(path, 'evaluation.json')))
  raise "evaluation digest mismatch #{advisory.cve}" unless advisory.digest == evaluation.fetch('dossier_digest')
  raise "evaluation CVE mismatch #{advisory.cve}" unless evaluation.fetch('cve') == advisory.cve
  { cve: advisory.cve, dossier_digest: advisory.digest }
end
current = SecurityAdvisories::Advisory.load('CVE-2026-64387')
raise 'not schema1' unless current.data.fetch('schema_version') == 1
raise 'roles not empty' unless current.platform.fetch('affected_node_roles').empty?
raise 'open boundaries changed' unless %w[6.6 6.12 6.18].all? do |branch|
  rule = current.version_rules.fetch(branch)
  rule.has_key?('fixed_in') && rule['fixed_in'].nil? && !rule.has_key?('fixed_commit')
end
raise 'mainline fix changed' unless current.fixed_from == '7.2.0'
raise '7.1 fix changed' unless current.version_rules.fetch('7.1').fetch('fixed_in') == '7.1.4'
editorial = JSON.parse(File.read(File.join(session_root, 'assessment/operator-period-cifs-lead-editorial.json')))
raise 'lead public text changed' unless Digest::SHA256.file(File.join(current.directory, 'advisory.yml')).hexdigest == editorial.fetch('sha256')
receipt = { inventory: rows.length, all_real_loader_and_digest_checks: 'PASS', all_cves_unique: rows.map { |r| r[:cve] }.uniq.length == 111,
            cifs_schema: 1, cifs_roles: [], cifs_fix_bounds_and_public_text: 'unchanged; lead receipt hash matches',
            per_dossier_digests: rows }
File.write(File.join(__dir__, 'operator-period-inventory-check.json'), JSON.pretty_generate(receipt) + "\n")
puts 'All111 real-loader/evaluation digest checks PASS; CIFS source bounds and lead text preserved'
