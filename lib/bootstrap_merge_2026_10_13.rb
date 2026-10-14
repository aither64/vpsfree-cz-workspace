# frozen_string_literal: true

# Dated, supervised composition of the selected runtime's existing interfaces.
# Load its workspace-host first. This file owns no ledger or Git implementation.
class BootstrapMerge20261013 < DevWorkspaceHost::Host
  ACTION = 'bootstrap-merge-prepare-2026-10-13'
  KIND = 'bootstrap_merge_2026_10_13'

  def operate(plan, request, prepare: false)
    @plan = plan
    @plan_id = WorkspaceCoordination.digest(plan)
    @entry = registry.find(plan.fetch('workspaceName'))
    raise WorkspaceCoordination::Error, 'registered workspace changed' unless @entry && @entry['root'] == plan['workspace']
    @engine = coordination_engine(@entry)
    result = @engine.store.lock(ACTION, nonblock: true) do
      prior = !prepare && @engine.store.read['receipts'][request['requestId']]
      admission(prior && prior.dig('result', 'id')) do
        verify_condition!
      end
      prepare ? prepare_merge_request(request) : execute_merge_request(request)
    end
    raise WorkspaceCoordination::Error.new('another bootstrap merge driver is running; retry later', 75) if result == false
    result
  end

  private

  def admission(job_id = nil)
    with_coordination_session_admission(@entry, @plan.fetch('slug')) do
      @engine.current_generation!
      unless File.realpath(package_root) == @plan['selectedPackage'] && profile_link_token == @plan['profileToken'] &&
             @engine.catalog.digest == @plan['catalogDigest']
        raise WorkspaceCoordination::Error.new('frozen package/profile/catalog changed', 3)
      end
      @owner = @engine.existing_bootstrap_owner(@plan.fetch('slug'), @plan.fetch('ownerId'))
      data = @engine.store.read
      reservation = data['reservations'][@plan.fetch('reservationId')]
      unless reservation && reservation['ownerId'] == @owner['id'] && reservation['state'] == 'deployed_review' &&
             @plan.fetch('repositories').all? { |name, value| reservation['integrationObligations'].include?({'repository' => name, 'target' => value.fetch('target')}) }
        raise WorkspaceCoordination::Error.new('held reservation or integration scope changed', 4)
      end
      raise WorkspaceCoordination::Error.new('workspace is suspended', 5) if data['suspended']
      pending = data['jobs'].values.select { |job| job['ownerId'] == @owner['id'] && !WorkspaceCoordination::TERMINAL.include?(job['state']) }
      unless pending.all? { |job| job['id'] == job_id && job['kind'] == 'merge' }
        raise WorkspaceCoordination::Error.new('another bootstrap operation is pending; retain the supervised exclusion', 75)
      end
      yield
    end
  end

  def verify_condition!
    unless @plan.fetch('source') == {'kind' => 'user_instruction', 'reference' => 'initiating conversation: conditional integration after creation fix',
                                   'quote' => "ok, after you'll deploy the fix, you can merge the changes"}
      raise WorkspaceCoordination::Error.new('conditional merge direction changed', 4)
    end
    @plan.fetch('evidence').each do |ref|
      path = File.expand_path(ref.fetch('path'), @plan.fetch('workspace'))
      root = File.join(@plan.fetch('workspace'), 'work', @plan.fetch('slug')) + '/'
      unless File.realpath(path).start_with?(root) && Digest::SHA256.file(path).hexdigest == ref.fetch('sha256')
        raise WorkspaceCoordination::Error.new('frozen review/deployment evidence changed', 3)
      end
    end
    proof = @plan.fetch('deploymentEvidence')
    raise WorkspaceCoordination::Error, 'deployment evidence is outside the frozen evidence' unless @plan['evidence'].include?(proof)
    value = WorkspaceCoordination.parse(File.binread(File.expand_path(proof.fetch('path'), @plan['workspace']), WorkspaceCoordination::MAX_REQUEST + 1))
    unless value['outcome'] == 'passed' && value['candidatePackage'] == @plan['selectedPackage'] &&
           value.dig('reservation', 'id') == @plan['reservationId'] && value.dig('reservation', 'ownerId') == @plan['ownerId']
      raise WorkspaceCoordination::Error.new('successful reserved creation-fix deployment is required', 4)
    end
    @plan.fetch('repositories').each do |name, selected|
      path, _common, _remote, registration = @engine.repository(@owner, name)
      unless "refs/heads/#{registration.fetch('default_branch')}" == selected.fetch('target') &&
             @engine.capture('git', '-C', path, 'rev-parse', "#{registration.fetch('branch')}^{commit}").strip == selected.fetch('head') &&
             @engine.ancestor?(path, value.fetch('sourceHeads').fetch(name), selected.fetch('head'))
        raise WorkspaceCoordination::Error.new('reviewed registered head or deployed ancestry changed', 3)
      end
    end
  end

  def prepare_merge_request(request)
    WorkspaceCoordination.keys!(request, %w[schema requestId repository])
    selected = @plan.fetch('repositories').fetch(request.fetch('repository')) { raise WorkspaceCoordination::Error, 'repository is outside the approved installation scope' }
    receipt = nil
    admission do
      if @engine.store.read['receipts'].key?(request.fetch('requestId'))
        receipt = @engine.store.transaction { |data| @engine.store.request(data, @owner['id'], [ACTION, @plan_id], request) { raise WorkspaceCoordination::Error, 'preparation receipt disappeared' } }
      end
    end
    return receipt if receipt
    snapshot = @engine.prepare_merge(@owner, request['repository'], @plan.fetch('evidence'))
    unless snapshot.dig('operation', 'featureHead') == selected.fetch('head') && snapshot.dig('operation', 'target') == selected.fetch('target')
      raise WorkspaceCoordination::Error.new('prepared head differs from the reviewed inventory', 3)
    end
    bundle = @engine.save_artifact('kind' => KIND, 'ownerId' => @owner['id'], 'planId' => @plan_id,
      'snapshot' => snapshot, 'approvalId' => SecureRandom.uuid, 'executionId' => SecureRandom.uuid)
    admission do
      @engine.snapshot(@owner, snapshot, 'merge')
      @engine.store.transaction do |data|
        @engine.store.request(data, @owner['id'], [ACTION, @plan_id], request) do
          {'schema' => 1, 'artifact' => bundle.fetch('id'), 'requestId' => bundle.fetch('executionId')}
        end
      end
    end
  end

  def execute_merge_request(request)
    WorkspaceCoordination.keys!(request, %w[schema requestId artifact])
    bundle = @engine.artifact!(request.fetch('artifact'))
    unless bundle['kind'] == KIND && bundle['ownerId'] == @owner['id'] && bundle['planId'] == @plan_id && bundle['executionId'] == request['requestId']
      raise WorkspaceCoordination::Error.new('execution bundle differs from the frozen operation', 4)
    end
    snapshot = bundle.fetch('snapshot')
    operation = snapshot.fetch('operation')
    selected = @plan.fetch('repositories').fetch(operation.fetch('repository'))
    unless operation['featureHead'] == selected['head'] && operation['target'] == selected['target']
      raise WorkspaceCoordination::Error.new('bundle is outside the reviewed integration scope', 4)
    end
    submit = {'schema' => 1, 'requestId' => request['requestId'], 'kind' => 'merge', 'dependsOn' => [],
              'reservationId' => nil, 'snapshot' => snapshot}
    # Receipt-aware mutations must run before live snapshot validation on retry:
    # a successful worker has already changed its integration checkout.
    prior = @engine.store.read['receipts'][request['requestId']]
    id = prior && prior.dig('result', 'id')
    job = admission(id) do
      approval = @engine.mutate(@owner, 'approve', {'schema' => 1, 'requestId' => bundle.fetch('approvalId'), 'kind' => 'merge',
        'scope' => [{'repository' => operation['repository'], 'target' => operation['target']}],
        'source' => @plan.fetch('source'), 'reviewedSnapshot' => snapshot.fetch('id')})
      @engine.mutate(@owner, 'submit', submit.merge('approvalId' => approval.fetch('id')))
    end
    @err.puts "Retained merge job #{job.fetch('id')} for #{operation['repository']}"
    wait_merge(job.fetch('id'))
  end

  def wait_merge(id)
    loop do
      @engine.reconcile_attempts
      job = @engine.store.read['jobs'].fetch(id)
      if job['state'] == 'succeeded'
        return {'schema' => 1, 'jobId' => id, 'attemptId' => job['attempt'], 'state' => job['state'],
                'operation' => job['snapshot']['operation'].slice('repository', 'target', 'featureHead'), 'result' => job['result']}
      end
      if %w[failed canceled needs_refresh].include?(job['state'])
        raise WorkspaceCoordination::Error.new("merge #{id} is #{job['state']}; retain original evidence and use ordinary recovery", 5)
      end
      if WorkspaceCoordination::CLAIMED.include?(job['state'])
        unless File.file?(@engine.attempt_path(job.fetch('attempt'), 'request.json'))
          raise WorkspaceCoordination::Error.new("merge #{id} has no durable worker request; retain its claim for operator recovery", 5)
        end
        @engine.dispatch_reconciliation(job)
      else
        claimed = admission(id) { @engine.claim(owner_id: @owner['id']) }
        unless claimed.empty? || claimed.map { |value| value['id'] } == [id]
          raise WorkspaceCoordination::Error.new('unexpected bootstrap claim; do not dispatch it', 5)
        end
        claimed.each { |value| @engine.dispatch(value) }
      end
      sleep 2
    end
  end
end
