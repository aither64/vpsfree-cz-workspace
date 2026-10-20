require 'json'
require 'digest'
require '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
session = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves'
root = SecurityAdvisories::ROOT
expected = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
raise 'Frozen snapshot changed' unless Digest::SHA256.file(File.join(root, '.state/evidence.json')).hexdigest == expected
ids = JSON.parse(File.read("#{session}/assessment/packages.json"))['groups']['implementer1']
identity = JSON.parse(File.read("#{session}/assessment/implementer0/livepatch-source-identities.json"))['unique_bound_tuples']
review = JSON.parse(File.read("#{session}/assessment/implementer1/livepatch-coverage.json"))
accepted = review['rows'].select { |r| r['decision'] == 'source_content_accepted' }.map { |r| r['cve'] }
rows = ids.map do |cve|
  advisory = SecurityAdvisories::Advisory.load(cve)
  evaluation = JSON.parse(File.read(File.join(root, 'advisories', cve, 'evaluation.json')))
  raise "Stale dossier digest #{cve}" unless evaluation['dossier_digest'] == advisory.digest
  raise "Wrong snapshot collection #{cve}" unless evaluation['collected_at'] == '2026-10-19T21:48:39Z'
  raise "Wrong node count #{cve}" unless evaluation['nodes'].length == 13
  overrides = advisory.data['platform']['history_start_overrides']
  raise "Unexpected history scope #{cve}" unless overrides.keys == ['126'] && overrides['126']['required_since'] == '2026-03-31T20:11:46Z'
  tuples = advisory.data['platform']['accepted_livepatches']
  raise "Unexpected tuple count #{cve}" unless tuples.length == (accepted.include?(cve) ? 3 : 0)
  raise "Unbound accepted tuple #{cve}" unless tuples.all? { |t| identity.include?(t) }
  counts = evaluation['nodes'].group_by { |r| r['state'] }.transform_values(&:length)
  { cve: cve, digest_matches: true, snapshot_collection_matches: true, exact_history_scope: true, accepted_tuple_count: tuples.length, states: counts, analysis_sha256: Digest::SHA256.file(File.join(root, 'advisories', cve, 'analysis.md')).hexdigest, advisory_sha256: Digest::SHA256.file(File.join(root, 'advisories', cve, 'advisory.yml')).hexdigest, evaluation_sha256: Digest::SHA256.file(File.join(root, 'advisories', cve, 'evaluation.json')).hexdigest }
end
File.write("#{session}/assessment/implementer1/final-validation.json", JSON.pretty_generate({ schema: 1, snapshot_sha256: expected, checked_count: rows.length, rows: rows, limits: ['74630 v6 partial inline correction withheld from full accepted mitigation', 'Storage timestamp-missing row excluded only by tenant workload role; no freshness certification', 'No Git commit, remote draft, publication or additional collection by owner'] }) + "\n")
puts "Final readback PASS: #{rows.length} exact dossier digests, frozen collection, lifecycle scope and reviewed tuple sets"
puts rows.group_by { |r| r[:states] }.map { |counts, group| "#{group.length} dossiers: #{counts}" }
