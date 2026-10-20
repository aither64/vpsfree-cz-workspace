require 'json'
r = SecurityAdvisories::Reconciler.new(client: nil)
rows = ARGV.map do |cve|
  advisory = SecurityAdvisories::Advisory.load(cve)
  committed = r.load_evaluation(advisory)
  reproduced = r.evaluate(advisory, persist: false)
  committed.delete('evaluated_at')
  reproduced.delete('evaluated_at')
  raise "complete evaluation mismatch: #{cve}" unless committed == reproduced
  { cve: cve, dossier_digest: advisory.digest,
    complete_result_equal_except_evaluated_at: true,
    loader_digest_verified: true, persisted: false,
    states: reproduced.fetch('completeness').fetch('states') }
end
puts JSON.pretty_generate(rows)
