require 'json'
require 'digest'
require File.join(Dir.pwd, '.state/implementer0/operator-period-parent-runtime/lib/security_advisories')

owner = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-vpsadmin-kernel-cves/assessment/implementer0'
client = Object.new
def client.get(*) = raise('unexpected external read')
def client.post(*) = raise('unexpected external write')
def client.put(*) = raise('unexpected external write')
def client.delete(*) = raise('unexpected external write')
reconciler = SecurityAdvisories::Reconciler.new(client: client, root: Dir.pwd)
def reconciler.remote_from_submission(*) = nil
def reconciler.find_remote(*) = nil

evidence = JSON.parse(File.read('.state/evidence.json'))
rows = %w[CVE-2026-53260 CVE-2026-72069].map do |cve|
  advisory = SecurityAdvisories::Advisory.load(cve, root: Dir.pwd)
  reviewed = JSON.parse(File.read("advisories/#{cve}/evaluation.json"))
  old = reconciler.evaluate(advisory, evidence: evidence, persist: false)
  old_storage = old.fetch('nodes').find { |n| n['node_id'] == 161 }
  raise 'parent falsely resolves exclusion' unless old_storage['state'] == 'unknown'
  raise 'new result not resolved' unless reviewed.fetch('nodes').find { |n| n['node_id'] == 161 }['state'] == 'not_affected'
  error = nil
  begin
    reconciler.sync(advisory, evaluation: reviewed, dry_run: false, evidence: evidence)
  rescue SecurityAdvisories::Error => e
    error = e
  end
  raise 'parent pre-write drift guard did not reject' unless error&.message&.include?('per-Node conclusions differ')
  { 'cve' => cve, 'parent_loader_accepts_additive_map' => true, 'parent_storage' => 'unknown',
    'new_storage' => 'not_affected', 'normal_parent_sync_prewrite_rejects' => error.message,
    'external_requests' => 0 }
end
File.write(File.join(owner, 'operator-period-parent-runtime-proof.json'), JSON.pretty_generate(
  'parent' => 'cfef162049f632016c9e67bca0e400c58c8618d2',
  'isolation' => 'Exact lib blobs retained in ignored .state; no checkout/ref/index mutation; fake client forbids all external requests',
  'rows' => rows
) + "\n")
puts 'Exactcfef old loader conservativeunknown and normal sync prewrite drift rejection PASS for both RT dossiers'
