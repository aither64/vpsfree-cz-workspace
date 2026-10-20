require_relative '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories/lib/security_advisories'
require 'digest'
class NoOperatorPeriodNetwork
  attr_reader :calls

  def initialize
    @calls = 0
  end

  def method_missing(name, *_args, **_kwargs)
    @calls += 1
    raise "Unexpected external client call #{name}"
  end

  def respond_to_missing?(_name, _include_private = false)
    false
  end
end
root = SecurityAdvisories::ROOT
path = File.join(root, '.state/evidence.json')
expected = '61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274'
raise 'snapshot drift' unless Digest::SHA256.file(path).hexdigest == expected
snapshot = JSON.parse(File.read(path))
client = NoOperatorPeriodNetwork.new
reconciler = SecurityAdvisories::Reconciler.new(client:)
rows = %w[CVE-2026-53260 CVE-2026-72069 CVE-2026-64387].map do |cve|
  advisory = SecurityAdvisories::Advisory.load(cve)
  evaluation_path = File.join(advisory.directory, 'evaluation.json')
  before = Digest::SHA256.file(evaluation_path).hexdigest
  reviewed = reconciler.load_evaluation(advisory)
  fresh = reconciler.evaluate(advisory, evidence: snapshot, persist: false)
  raise "postcommit conclusion drift #{cve}" unless reviewed.except('evaluated_at') == fresh.except('evaluated_at')
  raise "evaluation file written #{cve}" unless Digest::SHA256.file(evaluation_path).hexdigest == before
  { cve:, full_Reconciler_evaluation_match_excluding_only_evaluated_at: true,
    evaluation_file_sha256: before, states: fresh.dig('completeness', 'states'), file_unchanged: true }
end
paths = Dir.glob(File.join(root, 'advisories', 'CVE-*'))
raise 'dossier inventory not111' unless paths.length == 111
paths.each do |directory|
  advisory = SecurityAdvisories::Advisory.load(File.basename(directory))
  evaluation = reconciler.load_evaluation(advisory)
  raise "digest drift #{advisory.cve}" unless evaluation.fetch('dossier_digest') == advisory.digest
end
raise 'snapshot written' unless Digest::SHA256.file(path).hexdigest == expected
raise 'external requests made' unless client.calls == 0
receipt = { postcommit_normal_Reconciler: rows, all111_loader_and_normal_evaluation_read_checks: 'PASS',
            snapshot_sha256: expected, external_requests: client.calls, evaluation_file_writes: 0,
            no_tests_repeated: 'Retains177/0focused and targeted lint receipts; only requested postcommit reproduction run.' }
File.write(File.join(__dir__, 'operator-period-postcommit-check.json'), JSON.pretty_generate(receipt) + "\n")
puts JSON.pretty_generate(receipt)
