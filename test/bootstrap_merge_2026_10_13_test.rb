# frozen_string_literal: true

# Reuse the owning runtime's private-Git fixture rather than copy its protocol.
require File.join(ENV.fetch('DEV_WORKSPACE_TEST_SOURCE'), 'test/workspace_coordination_test')
if ENV['DEV_WORKSPACE_INSTALLED_PACKAGE']
  load File.join(ENV.fetch('DEV_WORKSPACE_INSTALLED_PACKAGE'), 'libexec/.workspace-host-wrapped')
end
require_relative '../lib/bootstrap_merge_2026_10_13'
require 'stringio'

class BootstrapMerge20261013Test < WorkspaceCoordinationTest
  def setup
    super
    configure_machine
    owner('installation')
    manifest_path = File.join(@workspace, 'work/installation/portal.yml')
    manifest = YAML.safe_load(File.read(manifest_path))
    manifest['codex'] = {}
    File.write(manifest_path, YAML.dump(manifest))
    @owner = @engine.owner('installation', bootstrap: true)
    feature(@owner)
    head = git('-C', @bare, 'rev-parse', 'installation').strip
    @reservation, = deployment(@owner, submit: false)
    @engine.store.transaction do |data|
      value = data['reservations'].fetch(@reservation['id'])
      value['state'] = 'deployed_review'
      value['revision'] += 1
    end
    proof_path = File.join(@workspace, 'work/installation/deployed.json')
    File.write(proof_path, JSON.generate('outcome' => 'passed', 'candidatePackage' => @package,
      'reservation' => {'id' => @reservation['id'], 'ownerId' => @owner['id']}, 'sourceHeads' => {'code' => @base}))
    proof = {'kind' => 'verification', 'path' => proof_path, 'sha256' => Digest::SHA256.file(proof_path).hexdigest}
    @plan = {'schema' => 1, 'workspace' => @workspace, 'workspaceName' => @entry['name'], 'slug' => @owner['slug'],
      'ownerId' => @owner['id'], 'reservationId' => @reservation['id'], 'selectedPackage' => @package,
      'profileToken' => DevWorkspaceProfileIdentity.token(@profile), 'catalogDigest' => @engine.catalog.digest,
      'repositories' => {'code' => {'head' => head, 'target' => 'refs/heads/master'}},
      'evidence' => evidence(@owner) + [proof], 'deploymentEvidence' => proof,
      'source' => {'kind' => 'user_instruction', 'reference' => 'initiating conversation: conditional integration after creation fix',
                   'quote' => "ok, after you'll deploy the fix, you can merge the changes"}}
    engine, entry, package = @engine, @entry.merge('root' => @workspace), @package
    klass = Class.new(BootstrapMerge20261013) do
      define_method(:package_root) { package }
      define_method(:codex_for_package) { |_package| '/bin/true' }
      define_method(:registry) do
        result = Object.new
        result.define_singleton_method(:find) { |name| entry if name == entry['name'] }
        result
      end
      define_method(:coordination_engine) { |_entry| engine }
      define_method(:instance_runtime) { |_entry| {authority: entry['authority'], codex: entry['socket']} }
      define_method(:sleep) { |_seconds| nil }
    end
    @driver = klass.new(env: {'HOME' => @tmp, 'PATH' => ENV.fetch('PATH'), 'DEV_WORKSPACES_STATE' => @state,
                             'DEV_WORKSPACES_PROFILE' => @profile}, out: StringIO.new, err: StringIO.new)
    @engine.define_singleton_method(:dispatch) do |job|
      path = attempt_path(job['attempt'], 'request.json')
      WorkspaceCoordination.atomic(path, worker_request(job, store.read['owners'].fetch(job['ownerId'])))
      raise 'private worker failed' unless WorkspaceCoordination::Worker.new(path, fixtures: true).run == 0
    end
    @preparation = request('repository' => 'code')
  end

  def test_dated_preparation_retries_retain_the_exact_bundle
    first = @driver.operate(@plan, @preparation, prepare: true)
    assert_equal first, @driver.operate(@plan, @preparation, prepare: true)
    error = assert_raises(WorkspaceCoordination::Error) { @driver.operate(@plan, @preparation.merge('repository' => 'unapproved'), prepare: true) }
    assert_match(/outside the approved/, error.message)
    assert_empty @engine.store.read['jobs']
  end

  def test_dated_driver_contention_returns_retryable_busy_error
    @engine.store.lock(BootstrapMerge20261013::ACTION) do
      error = assert_raises(WorkspaceCoordination::Error) { @driver.operate(@plan, @preparation, prepare: true) }
      assert_equal 75, error.code
      assert_empty @engine.store.read['jobs']
    end
  end

  def test_dated_execution_and_completed_retry_use_one_real_worker
    execution = @driver.operate(@plan, @preparation, prepare: true)
    before = @engine.store.read['reservations']
    result = @driver.operate(@plan, execution)
    assert_equal 'succeeded', result['state']
    assert_equal @plan['repositories']['code']['head'], git('ls-remote', @remote, 'refs/heads/master').split.first
    assert_equal result, @driver.operate(@plan, execution)
    data = @engine.store.read
    assert_equal 1, data['jobs'].length
    assert_equal before, data['reservations']
    assert_empty data['outbox']
    assert_equal @plan['repositories']['code']['head'], git('-C', @bare, 'rev-parse', 'installation').strip
  end

  def test_dated_retry_after_approval_only_reuses_its_identity
    execution = @driver.operate(@plan, @preparation, prepare: true)
    original = @engine.method(:mutate)
    refused = false
    @engine.define_singleton_method(:mutate) do |owner, action, input, **keywords|
      if action == 'submit' && !refused
        refused = true
        raise WorkspaceCoordination::Error, 'fixture interruption before submit'
      end
      original.call(owner, action, input, **keywords)
    end
    approvals = @engine.store.read['approvals'].length
    assert_raises(WorkspaceCoordination::Error) { @driver.operate(@plan, execution) }
    assert_equal approvals + 1, @engine.store.read['approvals'].length
    assert_empty @engine.store.read['jobs']
    assert_equal 'succeeded', @driver.operate(@plan, execution)['state']
    assert_equal approvals + 1, @engine.store.read['approvals'].length
  end

  def test_dated_wrong_condition_changed_evidence_and_generation_refuse
    bad = Marshal.load(Marshal.dump(@plan))
    bad['source']['quote'] = 'deployment only'
    assert_raises(WorkspaceCoordination::Error) { @driver.operate(bad, @preparation, prepare: true) }
    bad = Marshal.load(Marshal.dump(@plan))
    bad['profileToken'] = 'changed'
    assert_raises(WorkspaceCoordination::Error) { @driver.operate(bad, @preparation, prepare: true) }
    File.write(@plan['deploymentEvidence']['path'], '{}')
    assert_raises(WorkspaceCoordination::Error) { @driver.operate(@plan, @preparation, prepare: true) }
    assert_empty @engine.store.read['jobs']
  end

  def test_dated_other_owned_pending_job_refuses_before_claim
    snapshot = @engine.prepare_merge(@owner, 'code', evidence(@owner))
    job = @engine.mutate(@owner, 'submit', request('kind' => 'merge', 'dependsOn' => [], 'approvalId' => approval(@owner, snapshot), 'reservationId' => nil, 'snapshot' => snapshot))
    error = assert_raises(WorkspaceCoordination::Error) { @driver.operate(@plan, @preparation, prepare: true) }
    assert_equal 75, error.code
    assert_nil @engine.store.read['jobs'][job['id']]['attempt']
  end

  def test_dated_shared_master_keeps_unrelated_files_and_index
    root = @workspace
    git('init', '--initial-branch=master', root)
    git('-C', root, 'remote', 'add', 'origin', @remote)
    git('-C', root, 'fetch', 'origin', 'master')
    git('-C', root, 'checkout', '-B', 'master', @base) # isolated disposable fixture only
    git('-C', root, 'fetch', @bare, 'installation')
    head = git('-C', @bare, 'rev-parse', 'installation').strip
    git('-C', root, 'branch', 'installation', head)
    @catalog['repositories'] = {'workspace' => {'remote' => @remote}}
    @catalog['machines']['machine']['configurationRepository'] = 'workspace'
    install_catalog
    @engine = engine
    manifest_path = File.join(root, 'work/installation/portal.yml')
    manifest = YAML.safe_load(File.read(manifest_path))
    manifest['repositories'] = [{'name' => 'workspace', 'project' => 'workspace', 'branch' => 'installation', 'default_branch' => 'master'}]
    File.write(manifest_path, YAML.dump(manifest))
    @engine.store.transaction do |data|
      data['reservations'][@reservation['id']]['integrationObligations'] = [{'repository' => 'workspace', 'target' => 'refs/heads/master'}]
    end
    @plan['repositories'] = {'workspace' => {'head' => head, 'target' => 'refs/heads/master'}}
    proof = @plan['deploymentEvidence']
    v = JSON.parse(File.read(proof['path']))
    v['sourceHeads'] = {'workspace' => @base}
    File.write(proof['path'], JSON.generate(v))
    proof['sha256'] = Digest::SHA256.file(proof['path']).hexdigest
    @plan['catalogDigest'] = @engine.catalog.digest
    new_engine = @engine
    @driver.define_singleton_method(:coordination_engine) { |_entry| new_engine }
    @engine.define_singleton_method(:dispatch) do |job|
      path = attempt_path(job['attempt'], 'request.json')
      WorkspaceCoordination.atomic(path, worker_request(job, store.read['owners'].fetch(job['ownerId'])))
      WorkspaceCoordination::Worker.new(path, fixtures: true).run
    end
    File.write(File.join(root, 'unrelated'), 'another session')
    git('-C', root, 'add', 'unrelated')
    File.write(File.join(root, 'base'), 'dirty tracked data')
    index = git('-C', root, 'diff', '--cached', '--binary')
    execution = @driver.operate(@plan, request('repository' => 'workspace'), prepare: true)
    assert_equal 'succeeded', @driver.operate(@plan, execution)['state']
    assert_equal 'refs/heads/master', git('-C', root, 'symbolic-ref', 'HEAD').strip
    assert_equal index, git('-C', root, 'diff', '--cached', '--binary')
    assert_equal 'dirty tracked data', File.read(File.join(root, 'base'))
    assert_equal 'another session', File.read(File.join(root, 'unrelated'))
  end

  def test_dated_systemd_driver_exit_preserves_and_resumes_the_original_job
    skip 'explicit systemd check only' unless ENV['BOOTSTRAP_MERGE_SYSTEMD_TEST'] == '1'
    @engine.singleton_class.remove_method(:dispatch)
    @driver.define_singleton_method(:sleep) { |seconds| Kernel.sleep(seconds) }
    source = File.join(ENV.fetch('DEV_WORKSPACE_INSTALLED_PACKAGE'), 'libexec/workspace-coordination-execution')
    started, hold = File.join(@tmp, 'started'), File.join(@tmp, 'hold')
    File.write(hold, 'wait before mutation')
    wrapper = File.join(@package, 'bin/workspace-host')
    FileUtils.mkdir_p(File.dirname(wrapper))
    File.write(wrapper, <<~SCRIPT)
      #!#{RbConfig.ruby}
      require #{source.inspect}
      if ARGV.first == 'coordination-worker'
        WorkspaceCoordination::Worker.class_eval do
          alias_method :original_fixture_merge, :merge
          define_method(:merge) do
            File.write(#{started.inspect}, Process.pid.to_s)
            sleep 0.05 while File.exist?(#{hold.inspect})
            original_fixture_merge
          end
        end
        exit WorkspaceCoordination::Worker.new(ARGV.last, fixtures: true).run
      elsif ARGV.first == 'coordination-reconcile'
        exit WorkspaceCoordination::Worker.new(ARGV.last, fixtures: true).reconcile
      end
    SCRIPT
    File.chmod(0o700, wrapper)
    execution = @driver.operate(@plan, @preparation, prepare: true)
    driver = fork { @driver.operate(@plan, execution); exit! 0 }
    deadline = Process.clock_gettime(Process::CLOCK_MONOTONIC) + 20
    until File.file?(started)
      raise 'private systemd worker did not start' if Process.clock_gettime(Process::CLOCK_MONOTONIC) > deadline
      sleep 0.05
    end
    original = @engine.store.read['jobs'].values.first
    Process.kill('TERM', driver)
    Process.wait(driver)
    driver = nil
    assert Process.kill(0, Integer(File.read(started)))
    File.unlink(hold)
    result = @driver.operate(@plan, execution)
    assert_equal 'succeeded', result['state']
    assert_equal original['id'], result['jobId']
    assert_equal original['attempt'], result['attemptId']
    assert_equal 1, @engine.store.read['jobs'].length
    assert_equal @plan['repositories']['code']['head'], git('ls-remote', @remote, 'refs/heads/master').split.first
  ensure
    if driver
      Process.kill('TERM', driver) rescue Errno::ESRCH
      Process.wait(driver) rescue Errno::ECHILD
    end
    if original
      ["workspace-operation-#{original['attempt']}.service", "workspace-reconcile-#{original['attempt']}.service"].each do |unit|
        Open3.capture3('systemctl', '--user', 'stop', unit)
        Open3.capture3('systemctl', '--user', 'reset-failed', unit)
      end
    end
  end

  def test_dated_claimed_retry_never_redispatches_the_original_attempt
    execution = @driver.operate(@plan, @preparation, prepare: true)
    original = @engine.method(:dispatch)
    dispatches = 0
    @engine.define_singleton_method(:dispatch) do |job|
      dispatches += 1
      raise WorkspaceCoordination::Error, 'fixture driver stopped after claim' if dispatches == 1
      original.call(job)
    end
    assert_raises(WorkspaceCoordination::Error) { @driver.operate(@plan, execution) }
    original_job = @engine.store.read['jobs'].values.first
    # The ordinary runtime requires operator recovery when no durable request was
    # published. Ensure this route invokes recovery rather than dispatching again.
    recovered = nil
    @engine.define_singleton_method(:dispatch_reconciliation) do |job|
      recovered = job['attempt']
      raise WorkspaceCoordination::Error.new('claim without request requires operator recovery', 5)
    end
    error = assert_raises(WorkspaceCoordination::Error) { @driver.operate(@plan, execution) }
    assert_match(/no durable worker request/, error.message)
    assert_nil recovered
    assert_equal 1, dispatches
    assert_equal 1, @engine.store.read['jobs'].length
  end
end
