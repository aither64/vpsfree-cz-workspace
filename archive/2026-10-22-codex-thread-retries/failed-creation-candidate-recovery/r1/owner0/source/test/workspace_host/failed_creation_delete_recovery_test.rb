# frozen_string_literal: true

require_relative '../support/workspace_host_test_case'
require_relative 'suspension_test'
load File.expand_path('../../libexec/dev-session', __dir__) unless defined?(DevSession::Runner)

class WorkspaceHostTest < Minitest::Test
  class FailedCreationNoTerminal
    attr_accessor :terminal
    def session(*) = terminal
    def session_by_id(*) = nil
    def managed_session_identities = []
    def current_session_identity(*) = nil
  end

  class FailedCreationConfirmation < StringIO
    def tty? = true
  end

  module FailedCreationFaults
    attr_accessor :fixture_host

    private

    def advance_removal!(slug, removal, phase)
      super
      fail_deletion_fixture!(phase)
    end

    def move_to_removal_recovery!(source, recovery, name)
      fail_deletion_fixture!('during_move') if name == 'start.json'
      super
      fail_deletion_fixture!('after_move') if name == 'start.json'
    end

    def preserve_removed_state!(*args)
      super
      fail_deletion_fixture!('tracking_moved')
    end

    def fail_deletion_fixture!(phase)
      return unless fixture_host.deletion_fault == phase && !fixture_host.deletion_fault_fired
      fixture_host.deletion_fault_fired = true
      raise DevSession::Error, "injected deletion failure: #{phase}"
    end
  end

  module FailedCreationHostFixture
    attr_accessor :deletion_fault, :deletion_fault_fired, :confirmation_answer,
                  :turnover_before_lock, :native_turnover_before_lock, :native_turnover_command, :fixture_terminal, :reject_selected_protocol
    attr_reader :deletion_invocations

    private

    def with_transition_lock(mode = File::LOCK_EX, &block)
      if turnover_before_lock
        self.turnover_before_lock = false
        File.unlink(@profile)
        File.symlink(candidate, @profile)
      end
      if native_turnover_before_lock
        self.native_turnover_before_lock = false
        root = File.join(@state, 'codex', 'current')
        File.unlink(root)
        File.symlink(File.dirname(File.dirname(native_turnover_command)), root)
      end
      super(mode, &block)
    end

    def check_codex(command)
      super
      raise DevWorkspaceHost::Error, 'selected protocol fixture refused' if reject_selected_protocol
    end

    def failed_creation_delete_verifier(entry)
      runner = super
      inject_disposable_terminal(runner)
      runner
    end

    def inject_disposable_terminal(runner)
      terminal = FailedCreationNoTerminal.new
      terminal.terminal = fixture_terminal
      runner.instance_variable_set(:@tmux, terminal)
      runner.instance_variable_set(:@default_tmux, terminal)
      runner.instance_variable_set(:@tmux_injected, true)
      runner
    end

    def system_env_interactive!(environment, command, *arguments)
      (@deletion_invocations ||= []) << [environment, command, arguments]
      cli = DevSession::CLI.new(arguments, input: FailedCreationConfirmation.new(confirmation_answer || "yes\n"),
                               out: @out, err: @err, env: environment)
      owner = self
      cli.define_singleton_method(:runner) do
        value = super()
        owner.send(:inject_disposable_terminal, value)
        value.extend(FailedCreationFaults)
        value.fixture_host = owner
        value
      end
      status = cli.run
      raise DevWorkspaceHost::Error, 'ordinary deletion executor refused' unless status.zero?
    end
  end

  def test_failed_creation_candidate_public_entry_runs_ordinary_deletion_and_exact_replay
    with_failed_creation_candidate do |host, paths|
      initial = %i[start creation roster].to_h { |key| [key, File.binread(paths.fetch(key))] }
      token = host.send(:profile_link_token)
      assert_equal(0, invoke_failed_creation_candidate(host, paths), host.instance_variable_get(:@err).string)
      recovery = completed_failed_creation_recovery(host, paths)
      assert_equal(initial[:start], File.binread(File.join(recovery, 'start.json')))
      assert_equal(initial[:creation], File.binread(File.join(recovery, 'creation.json')))
      assert_equal(initial[:roster], File.binread(File.join(recovery, 'team.json')))
      assert_equal('removed', JSON.parse(File.read(File.join(recovery, 'recovery.json')))['phase'])
      refute(File.exist?(paths.fetch(:tracking)))
      refute(File.exist?(paths.fetch(:start)))
      assert_equal(token, host.send(:profile_link_token))
      assert_equal(paths.fetch(:predecessor), File.realpath(host.instance_variable_get(:@profile)))
      assert_equal(1, host.deletion_invocations.length)
      _, command, args = host.deletion_invocations.first
      assert_equal(File.join(paths.fetch(:candidate), 'libexec/workspace-portal/dev-session'), command)
      assert_equal(paths.fetch(:predecessor), args.fetch(args.index('--expected-host-generation') + 1))
      assert_equal(['delete', paths.fetch(:slug), '--as-is'], args[(args.index('--') + 1)..])
      refute_includes(args, '--transition-lock')
      refute_includes(args, '--force')
      assert_equal(0, invoke_failed_creation_candidate(host, paths))
      assert_equal(1, host.deletion_invocations.length, 'completed replay must not start another deletion')
      assert_equal(token, host.send(:profile_link_token))
      refute(host.events.any? { |e| %i[profile_set configured consumers_restarted].include?(e.first) })
      calls = File.readlines(paths.fetch(:calls), chomp: true).map { |line| JSON.parse(line) }
      refute(calls.any? { |call| (call & %w[start create bootstrap ensure-initial project/delete]).any? })
      assert(calls.any? { |call| call[0, 2] == %w[team prepare-delete] })
      assert(calls.any? { |call| call[0, 2] == %w[thread retire] })
      lock = File.open(host.send(:transition_lock_file), File::RDWR)
      assert(lock.flock(File::LOCK_EX | File::LOCK_NB), 'host must release exclusion before portal reconciliation')
      lock.close
      error = assert_raises(DevWorkspaceHost::Error) { host.send(:require_no_unfinished_lifecycle_operations!) }
      assert_includes(error.message, 'portal direct creation', 'ordinary portal still owns the failed receipt')
    end
  end

  def test_failed_creation_candidate_interrupted_ordinary_deletion_replays_one_operation
    %w[validated thread_retiring during_move after_move tracking_moved].each do |phase|
      with_failed_creation_candidate do |host, paths|
        bytes = File.binread(paths.fetch(:start))
        host.deletion_fault = phase
        assert_equal(1, invoke_failed_creation_candidate(host, paths), phase)
        assert(host.deletion_fault_fired, "fault was not reached: #{phase}: #{host.instance_variable_get(:@err).string}")
        journals = Dir.glob(File.join(File.dirname(paths.fetch(:start)), '*.removal.json'))
        if phase == 'validated'
          assert_equal(bytes, File.binread(paths.fetch(:start)))
          assert_empty(journals, 'pre-retirement failure keeps ordinary discard behavior')
        else
          assert_equal(1, journals.length)
          operation = JSON.parse(File.read(journals.first)).fetch('operation_id')
          assert_equal(0, invoke_failed_creation_candidate(host, paths), "#{phase}: #{host.instance_variable_get(:@err).string}")
          recovery = completed_failed_creation_recovery(host, paths)
          assert_equal(operation, JSON.parse(File.read(File.join(recovery, 'recovery.json'))).fetch('operation_id'))
          assert_equal(bytes, File.binread(File.join(recovery, 'start.json')))
          next
        end
        assert_equal(0, invoke_failed_creation_candidate(host, paths), host.instance_variable_get(:@err).string)
      end
    end
  end

  def test_failed_creation_candidate_refuses_unconfirmed_or_changed_context_before_effects
    %w[request root attempted missing_sent nonce start_slug oversized duplicate start_missing receipt_ready preparation_receipt member_project member_bootstrap fork archive migration authority terminal].each do |kind|
      with_failed_creation_candidate do |host, paths|
        case kind
        when 'request' then paths = paths.merge(request: '99999999-9999-4999-8999-999999999999')
        when 'root', 'attempted', 'missing_sent'
          x = YAML.safe_load(File.read(paths.fetch(:manifest)))
          x['codex']['thread_id'] = '22222222-2222-7222-8222-222222222222' if kind == 'root'
          x['creation']['initial_goal_attempted'] = true if kind == 'attempted'
          x['creation'].delete('initial_goal_sent') if kind == 'missing_sent'
          File.write(paths.fetch(:manifest), YAML.dump(x))
        when 'nonce', 'start_slug'
          x = JSON.parse(File.read(paths.fetch(:start)))
          x[kind == 'nonce' ? 'tmux_identity' : 'slug'] = kind == 'nonce' ? 'f' * 64 : 'wrong'
          File.write(paths.fetch(:start), JSON.generate(x))
        when 'oversized' then File.write(paths.fetch(:start), 'x' * 65_537)
        when 'duplicate' then File.write(paths.fetch(:start), '{"schema":1,"schema":1}')
        when 'start_missing' then File.unlink(paths.fetch(:start))
        when 'receipt_ready'
          path = paths.fetch(:receipt_path)
          x = JSON.parse(File.read(path)); x['state'] = 'ready'
          File.write(path, JSON.generate(x))
        when 'preparation_receipt'
          path = paths.fetch(:preparation_path)
          x = JSON.parse(File.read(path)); x['receiptId'] = '0' * 64
          File.write(path, JSON.generate(x))
        when 'member_project', 'member_bootstrap'
          x = JSON.parse(File.read(paths.fetch(:roster)))
          x['members'].first[kind == 'member_project' ? 'projectId' : 'bootstrapAttempted'] = kind == 'member_project' ? 'legacy' : true
          File.write(paths.fetch(:roster), JSON.generate(x))
        when 'fork', 'archive', 'migration'
          suffix = {'fork' => 'fork', 'archive' => 'archive', 'migration' => 'agent-teams-migration'}.fetch(kind)
          File.write(File.join(File.dirname(paths.fetch(:start)), "#{paths.fetch(:slug)}.#{suffix}.json"), '{}')
        when 'terminal'
          host.fixture_terminal = DevSession::Tmux::Session.new(id: '$fake', name: paths.fetch(:slug),
            mark: '1', slug: paths.fetch(:slug), workspace: paths.fetch(:entry).fetch('root'),
            identity_token: 'f' * 64, codex_thread_id: paths.fetch(:root_thread),
            codex_socket_path: host.send(:instance_runtime, paths.fetch(:entry)).fetch(:codex))
        when 'authority'
          directory = host.send(:instance_runtime, paths.fetch(:entry)).fetch(:authority)
          FileUtils.mkdir_p(directory)
          File.write(File.join(directory, paths.fetch(:slug) + '.json'), '{}')
          File.chmod(0o600, File.join(directory, paths.fetch(:slug) + '.json'))
        end
        assert_equal(1, invoke_failed_creation_candidate(host, paths), kind)
        assert_nil(host.deletion_invocations, kind)
        assert(File.directory?(paths.fetch(:tracking)), kind)
        assert_equal(paths.fetch(:predecessor), File.realpath(host.instance_variable_get(:@profile)), kind)
      end
    end
  end

  def test_failed_creation_candidate_source_profile_and_contract_are_exact
    %w[source turnover native protocol contract policy_zero policy_string current_contract].each do |kind|
      with_failed_creation_candidate do |host, paths|
        case kind
        when 'source' then host.executing_package = paths.fetch(:predecessor)
        when 'turnover' then host.turnover_before_lock = true
        when 'protocol' then host.reject_selected_protocol = true
        when 'native'
          host.native_turnover_command = make_codex(paths.fetch(:root), 'native-turnover')
          host.native_turnover_before_lock = true
        else
          package = kind == 'current_contract' ? paths.fetch(:candidate) : paths.fetch(:predecessor)
          path = File.join(package, 'share/workspace-portal/runtime-contract.json')
          x = JSON.parse(File.read(path))
          case kind
          when 'contract', 'current_contract' then x['trackingMaxBytes'] += 1
          when 'policy_zero' then x['turnRetrySessionPolicy'] = 0
          when 'policy_string' then x['turnRetrySessionPolicy'] = '1'
          end
          File.write(path, JSON.generate(x))
        end
        assert_equal(1, invoke_failed_creation_candidate(host, paths), kind)
        assert_nil(host.deletion_invocations, kind)
      end
    end
  end

  def test_failed_creation_candidate_preserves_ordinary_confirmation
    with_failed_creation_candidate do |host, paths|
      host.confirmation_answer = "no\n"
      assert_equal(1, invoke_failed_creation_candidate(host, paths))
      assert(File.exist?(paths.fetch(:start)))
      assert(File.directory?(paths.fetch(:tracking)))
      assert_empty(Dir.glob(File.join(File.dirname(paths.fetch(:start)), '*.removal.json')))
    end
  end

  def test_failed_creation_candidate_native_retirement_failure_retains_start_and_operation
    with_failed_creation_candidate do |host, paths|
      bytes = File.binread(paths.fetch(:start))
      File.write(paths.fetch(:fault_marker), 'fail')
      assert_equal(1, invoke_failed_creation_candidate(host, paths))
      path = paths.fetch(:start).sub('.start.json', '.removal.json')
      removal = JSON.parse(File.read(path))
      assert_equal('thread_retiring', removal.fetch('phase'))
      refute(File.exist?(paths.fetch(:start)))
      assert_equal(bytes, File.binread(File.join(removal.fetch('recovery'), 'start.json')))
      File.unlink(paths.fetch(:fault_marker))
      assert_equal(0, invoke_failed_creation_candidate(host, paths), host.instance_variable_get(:@err).string)
      completed = JSON.parse(File.read(File.join(removal.fetch('recovery'), 'recovery.json')))
      assert_equal(removal.fetch('operation_id'), completed.fetch('operation_id'))
    end
  end

  def test_failed_creation_candidate_replay_refuses_missing_or_conflicting_start_provenance
    %w[missing conflicting].each do |kind|
      with_failed_creation_candidate do |host, paths|
        host.deletion_fault = 'after_move'
        assert_equal(1, invoke_failed_creation_candidate(host, paths))
        removal_path = paths.fetch(:start).sub('.start.json', '.removal.json')
        removal = JSON.parse(File.read(removal_path))
        private_start = File.join(removal.fetch('recovery'), 'start.json')
        if kind == 'missing'
          File.unlink(private_start)
        else
          File.write(paths.fetch(:start), File.binread(private_start))
          File.chmod(0o600, paths.fetch(:start))
        end
        count = host.deletion_invocations.length
        assert_equal(1, invoke_failed_creation_candidate(host, paths), kind)
        assert_equal(count, host.deletion_invocations.length, 'invalid provenance reached ordinary executor')
        assert_equal(removal.fetch('operation_id'), JSON.parse(File.read(removal_path)).fetch('operation_id'))
      end
    end
  end

  def test_failed_creation_candidate_accepts_equal_policy_one_contract_without_selecting
    with_failed_creation_candidate do |host, paths|
      path = File.join(paths.fetch(:predecessor), 'share/workspace-portal/runtime-contract.json')
      File.write(path, JSON.generate(DevWorkspaceHost::RUNTIME_CONTRACT))
      token = host.send(:profile_link_token)
      assert_equal(0, invoke_failed_creation_candidate(host, paths), host.instance_variable_get(:@err).string)
      assert_equal(token, host.send(:profile_link_token))
    end
  end

  private

  def invoke_failed_creation_candidate(host, paths)
    host.run('workspace-host', ['recover-failed-creation-delete', '--source', paths.fetch(:source),
      '--workspace', 'example-workspace', '--session', paths.fetch(:slug), '--request-id', paths.fetch(:request)])
  end

  def completed_failed_creation_recovery(host, paths)
    root = File.join(host.instance_variable_get(:@state), 'removed', paths.fetch(:workspace_id))
    matches = Dir.glob(File.join(root, "*-#{paths.fetch(:slug)}-*"))
    assert_equal(1, matches.length)
    matches.first
  end

  def with_failed_creation_candidate
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      predecessor = File.realpath(host.instance_variable_get(:@profile))
      candidate = make_package(paths.fetch(:root), 'failed-creation-candidate')
      host.candidate = candidate
      host.executing_package = candidate
      host.extend(FailedCreationHostFixture)
      [predecessor, candidate].each do |package|
        contract = Marshal.load(Marshal.dump(DevWorkspaceHost::RUNTIME_CONTRACT))
        contract.delete('turnRetrySessionPolicy') if package == predecessor
        File.write(File.join(package, 'share/workspace-portal/runtime-contract.json'), JSON.generate(contract))
        executor = File.join(package, 'libexec/workspace-portal/dev-session')
        FileUtils.mkdir_p(File.dirname(executor))
        File.write(executor, "#!/bin/sh\nexit 0\n")
        File.chmod(0o755, executor)
      end
      entry = host.send(:registry).find('example-workspace')
      workspace = entry.fetch('root')
      slug = '2026-10-24-failed-recovery'
      request = '11111111-1111-4111-8111-111111111111'
      root_thread = '11111111-1111-7111-8111-111111111111'
      workspace_id = "#{File.basename(workspace)}-#{Digest::SHA256.hexdigest(workspace)[0, 16]}"
      state = host.instance_variable_get(:@state)
      portal = File.join(state, 'portal', workspace_id)
      preset = {'id' => 'delegated', 'name' => 'Team', 'description' => 'Disposable team',
        'catalogDigest' => 'a' * 64, 'teamDigest' => 'b' * 64, 'roles' => %w[lead reviewer0],
        'leadModel' => 'gpt-6.1-sol', 'leadEffort' => 'xhigh', 'leadInstructions' => 'Lead the task.',
        'members' => [{'address' => 'reviewer0', 'role' => 'reviewer', 'behavior' => 'reviewer',
          'purpose' => 'review', 'access' => 'read_only', 'model' => 'gpt-6.1-sol',
          'reasoningEffort' => 'xhigh', 'instructions' => 'Review assigned changes.'}]}
      nonce = 'd' * 64
      goal = "Disposable initial request.\n"
      receipt_id = 'e' * 64
      epoch = Digest::SHA256.hexdigest('')
      accepted = {'kind' => 'new', 'slug' => slug, 'goal' => goal, 'team' => preset['id'], 'catalogDigest' => preset['catalogDigest']}
      receipt = {'schema' => 3, 'workspace' => workspace, 'request' => accepted, 'receiptId' => receipt_id,
        'deletionHistorySha256' => epoch, 'attempt' => 2, 'state' => 'failed', 'phase' => 'initializing',
        'error' => 'Unknown reviewer start.', 'validated' => true, 'goal' => goal,
        'model' => preset['leadModel'], 'effort' => preset['leadEffort'], 'directTeam' => preset,
        'startedAt' => '2026-10-24T10:00:00Z', 'updatedAt' => '2026-10-24T10:00:01Z'}
      preparation = {'schema' => 1, 'workspace' => workspace, 'requestId' => request, 'inputVersion' => 1,
        'inputDigest' => 'f' * 64, 'snapshotDigest' => 'a' * 64, 'receiptId' => receipt_id,
        'attempt' => 1, 'state' => 'handed_off', 'phase' => 'initializing', 'slug' => slug, 'epoch' => epoch,
        'snapshot' => {'input' => {'rawPrompt' => goal}, 'goal' => goal, 'preset' => preset}, 'handoff' => accepted}
      runtime = host.send(:instance_runtime, entry)
      tracking = File.join(workspace, 'work', slug)
      FileUtils.mkdir_p(tracking)
      File.write(File.join(tracking, 'plan.md'), "# Disposable task\n")
      File.write(File.join(tracking, 'state.md'), "---\nlifecycle: active\n---\n# State\n")
      manifest = File.join(tracking, 'portal.yml')
      File.write(manifest, YAML.dump('schema' => 2, 'slug' => slug,
        'codex' => {'thread_id' => root_thread, 'socket_path' => runtime.fetch(:codex), 'client_version' => '1.2.3'},
        'creation' => {'state' => 'creating', 'initial_goal_attempted' => false, 'initial_goal_sent' => false,
                       'goal_sha256' => Digest::SHA256.hexdigest(goal)}, 'repositories' => [], 'artifacts' => []))
      locks = File.join(workspace, 'worktrees', '.locks')
      FileUtils.mkdir_p(locks)
      creation = File.join(locks, slug + '.creation.json')
      start = File.join(locks, slug + '.start.json')
      roster = File.join(state, 'codex-teams', workspace_id, slug + '.json')
      member = preset['members'].first.merge('index' => 0, 'threadId' => '', 'state' => 'creating',
        'projectId' => '22222222-2222-7222-8222-222222222222', 'createAttempted' => true,
        'addedAt' => '2026-10-24T10:00:00Z')
      records = {
        File.join(portal, 'creations', slug + '.json') => receipt,
        File.join(portal, 'session-preparations', request + '.json') => preparation,
        creation => {'schema' => 3, 'slug' => slug, 'goal_sha256' => Digest::SHA256.hexdigest(goal),
          'run_codex' => true, 'model' => preset['leadModel'], 'effort' => preset['leadEffort'],
          'direct_team' => preset, 'state' => 'creating', 'tmux_identity' => nonce},
        start => {'schema' => 1, 'slug' => slug, 'state' => 'creating', 'tmux_identity' => nonce},
        roster => {'schema' => 1, 'workspace' => workspace, 'slug' => slug, 'rootThreadId' => root_thread,
          'revision' => 1, 'createdAt' => '2026-10-24T10:00:00Z', 'updatedAt' => '2026-10-24T10:00:01Z', 'presetId' => preset['id'], 'catalogDigest' => preset['catalogDigest'],
          'teamDigest' => preset['teamDigest'], 'leadModel' => preset['leadModel'], 'leadEffort' => preset['leadEffort'],
          'leadInstructions' => preset['leadInstructions'], 'members' => [member]}
      }
      records.each do |path, object|
        FileUtils.mkdir_p(File.dirname(path), mode: 0o700)
        File.write(path, JSON.generate(object) + "\n")
        File.chmod(0o600, path)
      end
      calls = File.join(paths.fetch(:root), 'external-calls.jsonl')
      fault_marker = File.join(paths.fetch(:root), 'native-retirement-failure')
      # Ruby owns the real admission, phase writers, atomic moves and completion.
      # The external portal adapter checks call ordering; Go deletion tests own
      # unknown-reservation tombstones and confirmed native-thread retirement.
      helper = File.join(candidate, 'bin/workspace-portal')
      File.write(helper, <<~SCRIPT)
        #!#{RbConfig.ruby}
        require 'json'
        File.open(#{calls.dump}, 'a') { |file| file.puts JSON.generate(ARGV) }
        abort 'injected native retirement failure' if ARGV[0, 2] == ['thread', 'retire'] && File.exist?(#{fault_marker.dump})
        if ARGV[0, 2] == ['team', 'prepare-delete']
          record = JSON.parse(File.read(#{File.join(locks, slug + '.removal.json').dump}))
          abort 'wrong ordinary removal phase' unless record.fetch('phase') == (ARGV.include?('--check-only') ? 'validated' : 'thread_retiring')
        end
      SCRIPT
      File.chmod(0o755, helper)
      cluster = File.join(paths.fetch(:root), 'disposable-cluster')
      File.write(cluster, "#!/bin/sh\nif [ \"$1\" = cleanup-paths ]; then printf '%s\\n' '{\"schema\":1,\"paths\":[]}'; fi\n")
      File.chmod(0o755, cluster)
      catalog_path = host.instance_variable_get(:@env).fetch('DEV_WORKSPACES_EXTENSION_CATALOG')
      catalog = JSON.parse(File.read(catalog_path))
      catalog['clusterProviders'].each { |provider| provider['command'] = cluster }
      File.write(catalog_path, JSON.generate(catalog))
      host.events.clear
      yield host, paths.merge(predecessor:, candidate:, entry:, slug:, request:, workspace_id:,
                             tracking:, manifest:, start:, creation:, roster:, calls:, fault_marker:, root_thread:,
                             receipt_path: File.join(portal, 'creations', slug + '.json'),
                             preparation_path: File.join(portal, 'session-preparations', request + '.json'))
    end
  end
end
