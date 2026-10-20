require 'json'
require 'yaml'
session = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves'
worktree = '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories'
ids = JSON.parse(File.read("#{session}/assessment/packages.json"))['groups']['implementer1']
records = JSON.parse(File.read("#{session}/research/cve-evidence/range-records.json")).to_h { |r| [r['cve'], r] }
requirements = JSON.parse(File.read("#{session}/assessment/implementer1/requirements.json"))['rows'].to_h { |r| [r['cve'], r] }
rows = ids.map do |cve|
  data = YAML.safe_load_file("#{worktree}/advisories/#{cve}/advisory.yml")
  expected = records.fetch(cve)['fixes'][0]
  raise "Wrong exact 6.12 fix #{cve}" unless data['version_rules']['6.12']['fixed_commit'] == expected['sha'] && data['version_rules']['6.12']['fixed_in'] == expected['release']
  %w[required_options required_sysctls history_required_since affected_node_roles].each do |field|
    raise "Ledger disagreement #{cve}:#{field}" unless data['platform'][field] == requirements[cve][field]
  end
  primary = JSON.parse(File.read("#{session}/assessment/implementer1/primary/#{cve}/record.json"))['containers']['cna']
  primary['affected'].flat_map { |a| a['versions'] }.each do |v|
    next unless v['status'] == 'affected' && v['versionType'] == 'semver' && v.key?('lessThan')
    branch = v['version'].split('.')[0, 2].join('.')
    raise "Missing backport #{cve}:#{branch}" unless data['version_rules'][branch]['affected_from'] == v['version']
  end
  { cve: cve, release: expected['release'], exact_sha: expected['sha'], rules: data['version_rules'].length, requirements_match: true }
end
File.write("#{session}/assessment/implementer1/declaration-readback.json", JSON.pretty_generate({schema: 1, checked: rows.length, rows: rows}) + "\n")
puts "Readback verified #{rows.length} exact stable fixes, all declared backport starts and requirements maps"
