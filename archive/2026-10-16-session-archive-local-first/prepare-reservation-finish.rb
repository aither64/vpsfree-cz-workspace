# Generate owned completion evidence; this script does not finish the reservation.
require '/home/aither/.local/state/dev-workspaces/profile/libexec/workspace-coordination-execution'
require '/home/aither/.local/state/dev-workspaces/profile/libexec/workspace-integration'

root = '/home/aither/workspace/ai/vpsfree.cz'
slug = '2026-10-16-session-archive-local-first'
records = File.join(root, 'work', slug)
profile = '/home/aither/.local/state/dev-workspaces/profile'
engine = WorkspaceCoordination::Engine.new(state: File.dirname(profile),
  package: profile, profile: profile, workspace: root,
  entry: {'root' => root, 'name' => 'vpsfree-cz'})
run = JSON.parse(File.read(File.join(engine.store.root,
  'integrations/71b716d8-19d6-4dc5-8943-65701610ccfe.json')))
raise 'integration is incomplete' unless run.fetch('phase') == 'complete'
owner = engine.store.read.fetch('owners').fetch(run.fetch('ownerId'))
raise 'wrong retained owner' unless owner.fetch('id') == '99e4bed1-b56a-4b71-b15d-2ba2e49bcacb'
raise 'wrong initiative' unless owner.fetch('slug') == slug && owner.fetch('workspace') == root
reservation = engine.store.read.fetch('reservations').fetch('5f379baf-3837-4ec3-a2ce-4900fbd8d45e')
raise 'wrong reservation owner' unless reservation.fetch('ownerId') == owner.fetch('id')
raise 'reservation is not awaiting completion' unless reservation.fetch('state') == 'deployed_review'

def evidence(root, records, name, kind)
  path = File.join(records, name)
  {'kind' => kind, 'path' => path.delete_prefix(root + '/'),
   'sha256' => Digest::SHA256.file(path).hexdigest}
end

final = run.fetch('request').fetch('repositories').map do |item|
  operation = run.fetch('operations').fetch(item.fetch('repository'))
  snapshot = operation.fetch('snapshot').fetch('operation')
  raise 'final prepared head differs' unless snapshot.fetch('featureHead') == operation.fetch('expectedHead')
  item.slice('repository', 'target').merge('head' => snapshot.fetch('featureHead'))
end
proofs = JSON.parse(File.read(File.join(records, 'final-merge-equivalence-proofs.json')))
verification = evidence(root, records, 'reservation-final-verification.json', 'verification')
mappings = %w[workspace vpsfree-cz-configuration].map do |name|
  review_ref = evidence(root, records, "deployed-#{name}-review.json", 'review')
  review = JSON.parse(File.read(File.join(root, review_ref.fetch('path'))))
  operation = run.fetch('operations').fetch(name)
  snapshot = operation.fetch('snapshot').fetch('operation')
  mapping = {'repository' => name, 'target' => 'refs/heads/master',
    'from' => review.fetch('head'), 'fromBase' => review.fetch('base'),
    'to' => snapshot.fetch('featureHead'), 'toBase' => snapshot.fetch('comparisonBase'),
    'relation' => 'certified_equivalent', 'approvalId' => operation.fetch('approvalId')}
  path, = engine.repository(owner, name)
  proof = WorkspaceCoordination::Certification.new(engine).verify_proof(path, proofs.fetch(name), mapping)
  raise 'final certificate differs' unless proof == proofs.fetch(name)
  receipt = {'schema' => 1, 'ownerId' => owner.fetch('id'),
    'reservationId' => reservation.fetch('id'), 'mapping' => mapping,
    'originalReview' => review_ref, 'proof' => proof, 'verification' => verification}
  name_in_records = "reservation-equivalence-#{name}.json"
  destination = File.join(records, name_in_records)
  if File.exist?(destination)
    raise 'retained completion evidence differs' unless JSON.parse(File.read(destination)) == receipt
  else
    File.write(destination, JSON.pretty_generate(receipt) + "\n")
  end
  mapping.merge('evidence' => evidence(root, records, name_in_records, 'equivalence'))
end
engine.validate_replacements(owner, reservation, mappings, final)
request = {'schema' => 1, 'requestId' => SecureRandom.uuid,
  'expectedRevision' => reservation.fetch('revision'), 'deploymentWorkFinished' => true,
  'evidence' => "#{verification.fetch('path')} (sha256:#{verification.fetch('sha256')})",
  'finalHeads' => final, 'replacements' => mappings}
destination = File.join(records, 'reservation-finish-request.json')
raise 'finish request already exists; retain its request ID' if File.exist?(destination)
File.write(destination, JSON.pretty_generate(request) + "\n")
puts JSON.generate(request.slice('requestId', 'expectedRevision', 'finalHeads'))
