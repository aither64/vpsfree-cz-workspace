# frozen_string_literal: true

require 'fileutils'
require 'minitest/autorun'
require 'stringio'
require 'tmpdir'

load File.expand_path('../libexec/workspace-host', __dir__)

class WorkspaceHostTest < Minitest::Test
  def test_registry_selects_the_longest_matching_root_and_requires_a_name_outside_multiple_roots
    Dir.mktmpdir('workspace-host-test') do |directory|
      first = make_workspace(directory, 'first')
      nested = make_workspace(first, 'nested')
      registry = registry_at(directory)
      registry.register(
        name: 'first', root: first, hostname: 'first.workspace.example.test',
        aliases: [], replace: false
      )
      registry.register(
        name: 'nested', root: nested, hostname: 'nested.workspace.example.test',
        aliases: [], replace: false
      )

      assert_equal('nested', registry.select(cwd: nested).fetch('name'))
      error = assert_raises(VpsfreeWorkspaceHost::Error) do
        registry.select(cwd: directory)
      end
      assert_includes(error.message, '--workspace NAME')
      assert_equal('first', registry.select(name: 'first', cwd: directory).fetch('name'))
    end
  end

  def test_registry_is_private_and_rejects_duplicate_hosts
    Dir.mktmpdir('workspace-host-test') do |directory|
      first = make_workspace(directory, 'first')
      second = make_workspace(directory, 'second')
      registry = registry_at(directory)
      registry.register(
        name: 'first', root: first, hostname: 'first.workspace.example.test',
        aliases: ['old.example.test'], replace: false
      )

      assert_equal(0o600, File.stat(registry.path).mode & 0o777)
      error = assert_raises(VpsfreeWorkspaceHost::Error) do
        registry.register(
          name: 'second', root: second, hostname: 'old.example.test',
          aliases: [], replace: false
        )
      end
      assert_includes(error.message, 'duplicate workspace hostname')

      File.chmod(0o644, registry.path)
      assert_raises(VpsfreeWorkspaceHost::Error) do
        VpsfreeWorkspaceHost::Registry.new(registry.path)
      end
    end
  end

  def test_registry_replace_keeps_the_workspace_root_immutable
    Dir.mktmpdir('workspace-host-test') do |directory|
      first = make_workspace(directory, 'first')
      second = make_workspace(directory, 'second')
      registry = registry_at(directory)
      registry.register(
        name: 'vpsfree-cz', root: first, hostname: 'old.workspace.example.test',
        aliases: [], replace: false
      )

      error = assert_raises(VpsfreeWorkspaceHost::Error) do
        registry.register(
          name: 'vpsfree-cz', root: second, hostname: 'new.workspace.example.test',
          aliases: [], replace: true
        )
      end

      assert_includes(error.message, 'unregister vpsfree-cz first')
      assert_equal(first, registry.find('vpsfree-cz').fetch('root'))
      updated = registry.register(
        name: 'vpsfree-cz', root: first, hostname: 'new.workspace.example.test',
        aliases: ['old.workspace.example.test'], replace: true
      )
      assert_equal(first, updated.fetch('root'))
      assert_equal('new.workspace.example.test', updated.fetch('hostname'))
    end
  end

  def test_unregister_stops_instance_services_and_removes_the_registry_entry
    Dir.mktmpdir('workspace-host-test') do |directory|
      root = make_workspace(directory, 'workspace')
      config = File.join(directory, 'config', 'registry.json')
      state = File.join(directory, 'state')
      runtime = File.join(directory, 'runtime')
      authority = File.join(runtime, 'vpsfree-cz', 'authority')
      FileUtils.mkdir_p(authority)
      File.write(File.join(authority, 'old.json'), "old authority\n")
      VpsfreeWorkspaceHost::Registry.new(config).register(
        name: 'vpsfree-cz', root:, hostname: 'vpsfree-cz.workspace.example.test',
        aliases: [], replace: false
      )
      host = UnregisterHost.new(
        env: {
          'HOME' => directory,
          'PATH' => ENV.fetch('PATH'),
          'VPSFREE_WORKSPACES_CONFIG' => config,
          'VPSFREE_WORKSPACES_STATE' => state,
          'VPSFREE_WORKSPACES_RUNTIME_DIR' => runtime
        },
        out: StringIO.new,
        err: StringIO.new
      )

      assert_equal(0, host.run('workspace-host', ['unregister', 'vpsfree-cz']))
      assert_empty(VpsfreeWorkspaceHost::Registry.new(config).entries)
      disable = host.commands.find do |command|
        command[0, 4] == ['systemctl', '--user', 'disable', '--now']
      end
      refute_nil(disable)
      assert_includes(disable, 'workspace-portal@vpsfree-cz.service')
      assert_includes(disable, 'workspace-codex@vpsfree-cz.service')
      assert_includes(disable, 'workspace-tmux@vpsfree-cz.service')
      refute(File.exist?(File.join(runtime, 'vpsfree-cz')))

      replacement = make_workspace(directory, 'replacement')
      registered = VpsfreeWorkspaceHost::Registry.new(config).register(
        name: 'vpsfree-cz', root: replacement,
        hostname: 'replacement.workspace.example.test', aliases: [], replace: false
      )
      assert_equal(replacement, registered.fetch('root'))
    end
  end

  def test_unregister_restores_units_and_clients_after_a_partial_disable_failure
    Dir.mktmpdir('workspace-host-test') do |directory|
      root = make_workspace(directory, 'workspace')
      config = File.join(directory, 'config', 'registry.json')
      state = File.join(directory, 'state')
      VpsfreeWorkspaceHost::Registry.new(config).register(
        name: 'vpsfree-cz', root:, hostname: 'vpsfree-cz.workspace.example.test',
        aliases: [], replace: false
      )
      host = FailedUnregisterHost.new(
        env: {
          'HOME' => directory,
          'PATH' => ENV.fetch('PATH'),
          'VPSFREE_WORKSPACES_CONFIG' => config,
          'VPSFREE_WORKSPACES_STATE' => state
        },
        out: StringIO.new,
        err: StringIO.new
      )

      assert_equal(1, host.run('workspace-host', ['unregister', 'vpsfree-cz']))
      refute_nil(VpsfreeWorkspaceHost::Registry.new(config).find('vpsfree-cz'))
      enable = host.commands.find do |command|
        command[0, 4] == ['systemctl', '--user', 'enable', '--now']
      end
      refute_nil(enable)
      assert_equal([:quiesced], host.restored)
    end
  end

  def test_quiesce_ignores_a_manifest_from_another_codex_runtime
    Dir.mktmpdir('workspace-host-test') do |directory|
      root = make_workspace(directory, 'workspace')
      config = File.join(directory, 'config', 'registry.json')
      state = File.join(directory, 'state')
      runtime = File.join(directory, 'runtime')
      slug = '2026-09-06-old-runtime'
      manifest_dir = File.join(root, 'work', slug)
      FileUtils.mkdir_p(manifest_dir)
      File.write(
        File.join(manifest_dir, 'portal.yml'),
        portal_manifest('thread-old', '/run/old/app-server.sock', 'ready')
      )
      VpsfreeWorkspaceHost::Registry.new(config).register(
        name: 'vpsfree-cz', root:, hostname: 'vpsfree-cz.workspace.example.test',
        aliases: [], replace: false
      )
      host = QuiesceHost.new(
        env: {
          'HOME' => directory,
          'PATH' => ENV.fetch('PATH'),
          'VPSFREE_WORKSPACES_CONFIG' => config,
          'VPSFREE_WORKSPACES_STATE' => state,
          'VPSFREE_WORKSPACES_RUNTIME_DIR' => runtime
        },
        out: StringIO.new,
        err: StringIO.new
      )

      assert_empty(host.send(:quiesce_sessions))
      assert_empty(host.commands)
    end
  end

  def test_dev_session_dispatch_binds_the_registered_workspace_runtime
    Dir.mktmpdir('workspace-host-test') do |directory|
      root = make_workspace(directory, 'workspace')
      config = File.join(directory, 'config', 'registry.json')
      state = File.join(directory, 'state')
      runtime = File.join(directory, 'runtime')
      codex = File.join(directory, 'codex')
      File.write(codex, "#!/bin/sh\necho 'codex-cli 1.2.3'\n")
      File.chmod(0o755, codex)
      VpsfreeWorkspaceHost::Registry.new(config).register(
        name: 'vpsfree-cz', root:, hostname: 'vpsfree-cz.workspace.example.test',
        aliases: [], replace: false
      )
      host = CapturingHost.new(
        env: {
          'HOME' => directory,
          'PATH' => ENV.fetch('PATH'),
          'VPSFREE_WORKSPACES_CONFIG' => config,
          'VPSFREE_WORKSPACES_STATE' => state,
          'VPSFREE_WORKSPACES_RUNTIME_DIR' => runtime,
          'VPSFREE_WORKSPACES_SYSTEM_CODEX' => codex
        },
        out: StringIO.new,
        err: StringIO.new
      )

      Dir.chdir(directory) do
        assert_equal(0, host.run('dev-session', ['--workspace', 'vpsfree-cz', 'list']))
      end
      environment, command, arguments = host.captured
      assert_equal('vpsfree-cz', environment.fetch('VPSFREE_WORKSPACE_NAME'))
      assert_equal('dev-session', File.basename(command))
      assert_includes(arguments, root)
      assert_includes(arguments, File.join(runtime, 'vpsfree-cz', 'app-server.sock'))
      lock_index = arguments.index('--transition-lock')
      assert_operator(lock_index, :<, arguments.index('--'))
      assert_equal(File.join(state, 'transition.lock'), arguments.fetch(lock_index + 1))
      assert_equal('list', arguments.last)
    end
  end

  def test_cluster_commands_hold_the_shared_host_transition_lock
    Dir.mktmpdir('workspace-host-test') do |directory|
      root = make_workspace(directory, 'workspace')
      config = File.join(directory, 'config', 'registry.json')
      state = File.join(directory, 'state')
      VpsfreeWorkspaceHost::Registry.new(config).register(
        name: 'vpsfree-cz', root:, hostname: 'vpsfree-cz.workspace.example.test',
        aliases: [], replace: false
      )
      FileUtils.mkdir_p(state)
      lock_path = File.join(state, 'transition.lock')
      owner = File.open(lock_path, File::RDWR | File::CREAT, 0o600)
      owner.flock(File::LOCK_EX)
      host = ClusterHost.new(
        env: {
          'HOME' => directory,
          'PATH' => ENV.fetch('PATH'),
          'VPSFREE_WORKSPACES_CONFIG' => config,
          'VPSFREE_WORKSPACES_STATE' => state
        },
        out: StringIO.new,
        err: StringIO.new
      )
      result = Thread.new do
        host.run('vpsadmin-devcluster', ['--workspace', 'vpsfree-cz', 'status', '2026-09-06-test'])
      end
      sleep 0.05
      assert_nil(host.captured)
      owner.flock(File::LOCK_UN)
      owner.close

      assert_equal(0, result.value)
      refute_nil(host.captured)
    ensure
      owner&.close unless owner&.closed?
    end
  end

  def test_public_finalize_refuses_a_running_development_cluster
    Dir.mktmpdir('workspace-host-test') do |directory|
      root = make_workspace(directory, 'workspace')
      config = File.join(directory, 'config', 'registry.json')
      state = File.join(directory, 'state')
      codex = File.join(directory, 'codex')
      File.write(codex, "#!/bin/sh\necho 'codex-cli 1.2.3'\n")
      File.chmod(0o755, codex)
      VpsfreeWorkspaceHost::Registry.new(config).register(
        name: 'vpsfree-cz', root:, hostname: 'vpsfree-cz.workspace.example.test',
        aliases: [], replace: false
      )
      error_output = StringIO.new
      host = FinalizeHost.new(
        env: {
          'HOME' => directory,
          'PATH' => ENV.fetch('PATH'),
          'VPSFREE_WORKSPACES_CONFIG' => config,
          'VPSFREE_WORKSPACES_STATE' => state,
          'VPSFREE_WORKSPACES_RUNTIME_DIR' => File.join(directory, 'runtime'),
          'VPSFREE_WORKSPACES_SYSTEM_CODEX' => codex
        },
        out: StringIO.new,
        err: error_output
      )

      assert_equal(
        1,
        host.run(
          'dev-session',
          ['--workspace', 'vpsfree-cz', 'finalize', '2026-09-06-test', '--as-is']
        )
      )
      assert_includes(error_output.string, 'development clusters are still running')
      assert_empty(host.commands)
    end
  end

  def test_public_finalize_uses_the_private_cli_parser_for_options_and_slug
    Dir.mktmpdir('workspace-host-test') do |directory|
      root = make_workspace(directory, 'workspace')
      config = File.join(directory, 'config', 'registry.json')
      state = File.join(directory, 'state')
      codex = File.join(directory, 'codex')
      File.write(codex, "#!/bin/sh\necho 'codex-cli 1.2.3'\n")
      File.chmod(0o755, codex)
      VpsfreeWorkspaceHost::Registry.new(config).register(
        name: 'vpsfree-cz', root:, hostname: 'vpsfree-cz.workspace.example.test',
        aliases: [], replace: false
      )
      host = FinalizeHost.new(
        env: {
          'HOME' => directory,
          'PATH' => ENV.fetch('PATH'),
          'VPSFREE_WORKSPACES_CONFIG' => config,
          'VPSFREE_WORKSPACES_STATE' => state,
          'VPSFREE_WORKSPACES_RUNTIME_DIR' => File.join(directory, 'runtime'),
          'VPSFREE_WORKSPACES_SYSTEM_CODEX' => codex
        },
        out: StringIO.new,
        err: StringIO.new
      )
      host.cluster_active = false
      argv = [
        '--workspace', 'vpsfree-cz', 'finalize', '--check',
        '2026-09-06-Foo_bar', '--as-is'
      ]

      assert_equal(0, host.run('dev-session', argv))
      command, arguments = host.commands.fetch(0)
      assert_equal('dev-session', File.basename(command))
      assert_equal(['finalize', '--check', '2026-09-06-Foo_bar', '--as-is'], arguments.last(4))
    end
  end

  def test_switch_retains_codex_with_the_profile_generation_and_restarts_as_one_pair
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))

      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))

      assert_equal(1, host.send(:profile_generation))
      assert_equal(
        File.realpath(paths.fetch(:system_codex)),
        File.realpath(host.send(:generation_codex, 1))
      )
      assert_equal(File.realpath(paths.fetch(:system_codex)), File.realpath(host.send(:active_codex)))
      assert_includes(host.events, [:configured])
      assert_includes(host.events, [:consumers_restarted])
    end
  end

  def test_switch_rejects_a_nonactivating_profile_change
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))

      assert_equal(
        1,
        host.run('workspace-host', ['switch', '--source', paths.fetch(:source), '--no-start'])
      )
      refute(File.exist?(host.instance_variable_get(:@profile)))
    end
  end

  def test_busy_switch_keeps_the_old_codex_and_retries_only_the_pending_update
    with_transition_host(busy: ['vpsfree-cz/active']) do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))

      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      assert_equal(File.realpath(paths.fetch(:old_codex)), File.realpath(host.send(:active_codex)))
      assert(host.send(:pending_codex_update?, File.realpath(paths.fetch(:system_codex))))
      refute_includes(host.events, [:consumers_restarted])

      host.busy = []
      assert_equal(0, host.run('workspace-host', ['reconcile-codex', '--pending-only']))
      assert_equal(File.realpath(paths.fetch(:system_codex)), File.realpath(host.send(:active_codex)))
      refute(host.send(:pending_codex_update?))
      assert_includes(host.events, [:consumers_restarted])

      checks = host.events.count { |event| event.first == :codex_checked }
      assert_equal(0, host.run('workspace-host', ['reconcile-codex', '--pending-only']))
      assert_equal(checks, host.events.count { |event| event.first == :codex_checked })
    end
  end

  def test_rollback_selects_the_retained_codex_for_the_previous_profile_generation
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))

      second_package = make_package(paths.fetch(:root), 'package-two')
      second_codex = make_codex(paths.fetch(:root), 'codex-two')
      host.candidate = second_package
      host.instance_variable_set(:@system_codex, second_codex)
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      assert_equal(2, host.send(:profile_generation))

      assert_equal(0, host.run('workspace-host', ['rollback']))
      assert_equal(1, host.send(:profile_generation))
      assert_equal(File.realpath(paths.fetch(:system_codex)), File.realpath(host.send(:active_codex)))
      assert_includes(host.events, [:router_restarted])
      assert_includes(host.events, [:consumers_restarted])
    end
  end

  def test_failed_switch_restores_the_previous_profile_and_codex_pair
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      first_codex = File.realpath(host.send(:active_codex))

      host.candidate = make_package(paths.fetch(:root), 'package-two')
      host.fail_activation = true
      assert_equal(1, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))

      assert_equal(1, host.send(:profile_generation))
      assert_equal(first_codex, File.realpath(host.send(:active_codex)))
      assert_includes(host.events, [:profile_selected, 1])
      assert_includes(host.events, [:consumers_restarted])
    end
  end

  def test_failed_link_install_restores_the_previous_profile_and_codex_pair
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      first_codex = File.realpath(host.send(:active_codex))

      host.candidate = make_package(paths.fetch(:root), 'package-two')
      host.fail_links = true
      assert_equal(1, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))

      assert_equal(1, host.send(:profile_generation))
      assert_equal(first_codex, File.realpath(host.send(:active_codex)))
      assert_includes(host.events, [:profile_selected, 1])
      assert_includes(host.events, [:consumers_restarted])
    end
  end

  def test_failed_switch_generation_is_not_eligible_for_later_rollback
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))

      host.candidate = make_package(paths.fetch(:root), 'failed-package')
      host.fail_activation = true
      assert_equal(1, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      refute(File.exist?(host.send(:profile_generation_path, 2)))
      assert_nil(host.send(:generation_codex, 2))

      host.candidate = make_package(paths.fetch(:root), 'working-package')
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      assert_equal(2, host.send(:profile_generation))

      assert_equal(0, host.run('workspace-host', ['rollback']))
      assert_equal(1, host.send(:profile_generation))
      assert_equal(File.realpath(paths.fetch(:system_codex)), File.realpath(host.send(:active_codex)))
    end
  end

  def test_failed_codex_adoption_restores_the_previous_pair
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      previous = File.realpath(host.send(:active_codex))
      replacement = make_codex(paths.fetch(:root), 'codex-replacement')
      host.instance_variable_set(:@system_codex, replacement)
      host.fail_restart = true

      assert_equal(1, host.run('workspace-host', ['reconcile-codex']))

      assert_equal(previous, File.realpath(host.send(:active_codex)))
      assert_equal(previous, File.realpath(host.send(:generation_codex, 1)))
      assert_operator(host.events.count { |event| event == [:consumers_restarted] }, :>=, 2)
    end
  end

  def test_failed_rollback_restores_the_original_generation_pair
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      host.candidate = make_package(paths.fetch(:root), 'package-two')
      second_codex = make_codex(paths.fetch(:root), 'codex-two')
      host.instance_variable_set(:@system_codex, second_codex)
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      host.fail_restart = true

      assert_equal(1, host.run('workspace-host', ['rollback']))

      assert_equal(2, host.send(:profile_generation))
      assert_equal(File.realpath(second_codex), File.realpath(host.send(:active_codex)))
      assert_includes(host.events, [:profile_selected, 2])
    end
  end

  def test_suspend_quiesces_sessions_before_disabling_the_user_services
    with_transition_host do |host, paths|
      host.send(:root_codex, paths.fetch(:old_codex), paths.fetch(:current_root))
      assert_equal(0, host.run('workspace-host', ['switch', '--source', paths.fetch(:source)]))
      host.events.clear

      assert_equal(0, host.run('workspace-host', ['suspend']))

      assert_equal(:sessions_quiesced, host.events.fetch(0).first)
      disable = host.events.find do |event|
        event[0, 4] == [:command, 'systemctl', '--user', 'disable']
      end
      refute_nil(disable)
      assert_includes(disable, '--now')
      assert_includes(disable, 'workspace-codex@vpsfree-cz.service')
      assert_includes(disable, 'workspace-tmux@vpsfree-cz.service')
    end
  end

  private

  class CapturingHost < VpsfreeWorkspaceHost::Host
    attr_reader :captured

    private

    def exec_with_workspace(entry, command, *arguments)
      @captured = [@env.to_h.merge('VPSFREE_WORKSPACE_NAME' => entry.fetch('name')), command, arguments]
    end
  end

  class ClusterHost < VpsfreeWorkspaceHost::Host
    attr_reader :captured

    private

    def system_env!(environment, command, *arguments)
      @captured = [environment, command, arguments]
    end
  end

  class FinalizeHost < VpsfreeWorkspaceHost::Host
    attr_reader :commands
    attr_accessor :cluster_active

    def initialize(**options)
      super
      @commands = []
      @cluster_active = true
    end

    private

    def capture_env!(_environment, command, *arguments)
      if File.basename(command).include?('dev-session')
        separator = arguments.index('--')
        request = arguments.drop(separator + 2)
        slug = request.find { |argument| !argument.start_with?('-') }
        "https://vpsfree-cz.workspace.example.test/#{slug}/\n"
      else
        found = cluster_active && File.basename(command) == 'vpsadmin-devcluster'
        JSON.generate('schema' => 1, 'found' => found)
      end
    end

    def system_env!(_environment, command, *arguments)
      @commands << [command, arguments]
    end
  end

  class UnregisterHost < VpsfreeWorkspaceHost::Host
    attr_reader :commands

    def initialize(**options)
      super
      @commands = []
    end

    private

    def system!(*argv)
      @commands << argv
    end

    def quiesce_sessions(_entries)
      []
    end
  end

  class QuiesceHost < VpsfreeWorkspaceHost::Host
    attr_reader :commands

    def initialize(**options)
      super
      @commands = []
    end

    private

    def capture_env!(environment, command, *arguments)
      @commands << [environment, command, arguments]
      "quiesced terminal: #{arguments[-2]}\n"
    end
  end

  class FailedUnregisterHost < VpsfreeWorkspaceHost::Host
    attr_reader :commands, :restored

    def initialize(**options)
      super
      @commands = []
    end

    private

    def quiesce_sessions(_entries)
      [:quiesced]
    end

    def restore_quiesced_sessions(sessions)
      @restored = sessions
    end

    def system!(*argv)
      @commands << argv
      if argv[0, 4] == ['systemctl', '--user', 'disable', '--now']
        raise VpsfreeWorkspaceHost::Error, 'injected partial disable failure'
      end
    end
  end

  class TransitionHost < VpsfreeWorkspaceHost::Host
    attr_accessor :busy, :candidate, :fail_activation, :fail_links, :fail_restart
    attr_reader :events

    def initialize(candidate:, busy:, **options)
      super(**options)
      @candidate = candidate
      @busy = busy
      @events = []
    end

    private

    def capture!(*argv)
      return "#{candidate}\n" if argv[0, 2] == ['nix', 'build']
      super
    end

    def system!(*argv)
      if argv[0, 3] == ['nix-env', '--profile', @profile]
        if argv[3] == '--set'
          generations = Dir["#{@profile}-*-link"].filter_map do |path|
            File.basename(path)[/-(\d+)-link\z/, 1]&.to_i
          end
          current = generations.max.to_i + 1
          generation = profile_generation_path(current)
          File.symlink(argv.fetch(4), generation)
          File.unlink(@profile) if File.symlink?(@profile)
          File.symlink(File.basename(generation), @profile)
          @events << [:profile_set, current]
          return
        elsif argv[3] == '--rollback'
          target = previous_profile_generation
          File.unlink(@profile)
          File.symlink(File.basename(profile_generation_path(target)), @profile)
          @events << [:profile_rolled_back, target]
          return
        elsif argv[3] == '--switch-generation'
          target = Integer(argv.fetch(4), 10)
          File.unlink(@profile)
          File.symlink(File.basename(profile_generation_path(target)), @profile)
          @events << [:profile_selected, target]
          return
        elsif argv[3] == '--delete-generations'
          target = Integer(argv.fetch(4), 10)
          File.unlink(profile_generation_path(target))
          @events << [:profile_deleted, target]
          return
        end
      end
      if argv[0, 4] == ['systemctl', '--user', 'restart', 'workspace-router.service']
        @events << [:router_restarted]
      else
        @events << [:command, *argv]
      end
    end

    def root_codex(command, root)
      package = File.dirname(File.dirname(File.realpath(command)))
      FileUtils.mkdir_p(File.dirname(root))
      File.unlink(root) if File.symlink?(root)
      File.symlink(package, root)
    end

    def install_links
      @events << [:links_installed]
      if fail_links
        self.fail_links = false
        raise VpsfreeWorkspaceHost::Error, 'injected link installation failure'
      end
    end

    def configure_user_services
      @events << [:configured]
    end

    def activate_installed(_command)
      configure_user_services
      if fail_activation
        self.fail_activation = false
        raise VpsfreeWorkspaceHost::Error, 'injected activation failure'
      end
      reconcile_codex_update(defer_busy: true)
    end

    def quiesce_sessions
      raise VpsfreeWorkspaceHost::Error, busy.join(', ') unless busy.empty?
      @events << [:sessions_quiesced]
      []
    end

    def wait_for_codex_sockets
      @events << [:codex_ready]
    end

    def restore_quiesced_sessions(_sessions)
      @events << [:sessions_restored]
    end

    def check_codex(command)
      @events << [:codex_checked, File.realpath(command)]
    end

    def busy_codex_sessions
      busy
    end

    def restart_codex_consumers
      @events << [:consumers_restarted]
      if fail_restart
        self.fail_restart = false
        raise VpsfreeWorkspaceHost::Error, 'injected consumer restart failure'
      end
    end
  end

  def registry_at(directory)
    VpsfreeWorkspaceHost::Registry.new(File.join(directory, 'config', 'registry.json'))
  end

  def make_workspace(parent, name)
    root = File.join(parent, name)
    %w[repos work worktrees].each { |item| FileUtils.mkdir_p(File.join(root, item)) }
    root
  end

  def make_codex(parent, name)
    package = File.join(parent, name)
    command = File.join(package, 'bin', 'codex')
    FileUtils.mkdir_p(File.dirname(command))
    File.write(command, "#!/bin/sh\necho 'codex-cli 1.2.3'\n")
    File.chmod(0o755, command)
    command
  end

  def make_package(parent, name)
    package = File.join(parent, name)
    command = File.join(package, 'bin', 'workspace-host')
    FileUtils.mkdir_p(File.dirname(command))
    File.write(command, "#!/bin/sh\nexit 0\n")
    File.chmod(0o755, command)
    package
  end

  def host_environment(directory, config:, runtime: File.join(directory, 'runtime'), system_codex: nil)
    system_codex ||= make_codex(directory, 'codex-system')
    {
      'HOME' => directory,
      'PATH' => ENV.fetch('PATH'),
      'VPSFREE_WORKSPACES_CONFIG' => config,
      'VPSFREE_WORKSPACES_STATE' => File.join(directory, 'state'),
      'VPSFREE_WORKSPACES_RUNTIME_DIR' => runtime,
      'VPSFREE_WORKSPACES_PROFILE' => File.join(directory, 'state', 'profile'),
      'VPSFREE_WORKSPACES_SYSTEM_CODEX' => system_codex
    }
  end

  def with_transition_host(busy: [])
    Dir.mktmpdir('workspace-host-transition-test') do |directory|
      root = make_workspace(directory, 'workspace')
      config = File.join(directory, 'config', 'registry.json')
      VpsfreeWorkspaceHost::Registry.new(config).register(
        name: 'vpsfree-cz', root:, hostname: 'vpsfree-cz.workspace.example.test',
        aliases: [], replace: false
      )
      source = File.join(directory, 'source')
      FileUtils.mkdir_p(source)
      old_codex = make_codex(directory, 'codex-old')
      system_codex = make_codex(directory, 'codex-system')
      candidate = make_package(directory, 'package-one')
      environment = host_environment(directory, config:, system_codex:)
      host = TransitionHost.new(
        candidate:, busy:, env: environment, out: StringIO.new, err: StringIO.new
      )
      yield host, {
        root: directory,
        source:,
        old_codex:,
        system_codex:,
        current_root: File.join(directory, 'state', 'codex', 'current')
      }
    end
  end

  def portal_manifest(thread_id, socket, state)
    YAML.dump(
      'schema' => state == 'creating' ? 2 : 1,
      'slug' => 'ignored-by-host',
      'codex' => { 'thread_id' => thread_id, 'socket_path' => socket },
      'creation' => { 'state' => state }
    )
  end
end
