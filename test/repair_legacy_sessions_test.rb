# frozen_string_literal: true

require 'minitest/autorun'
require 'stringio'
require 'socket'
load File.expand_path('../bin/repair-legacy-sessions-2026-10-04', __dir__)

class RepairLegacySessionsTest < Minitest::Test
  Repair = LegacySessionRepair20261004
  SLUG = '2026-10-04-repair-fixture'
  PROSE = "# Original state\r\n\r\nComplete in prose is not authority.\r\n".b
  ROOT_ID = '01a10867-350b-7b02-8b91-99ddb173613c'

  class Interrupted < StandardError; end
  class FaultTool < Repair::Tool
    attr_accessor :fault

    def checkpoint
      super
      return unless fault && fault.call(@recovery)

      self.fault = nil
      raise Interrupted, 'disposable interruption after durable checkpoint'
    end
  end

  class CommitFaultTool < Repair::Tool
    def commit_row(row, progress)
      super
      raise Interrupted, 'Git commit completed before phase checkpoint'
    end
  end

  def setup
    @root = Dir.mktmpdir('repair-legacy-test-')
    @workspace = File.join(@root, 'workspace')
    @home = File.join(@root, 'home')
    @state = File.join(@home, '.local/state/dev-workspaces')
    @instance = File.join(@root, 'run/fixture')
    @generation = File.join(@root, 'package')
    @private = File.join(@root, 'private')
    [@workspace, @home, @state, @instance, @generation, @private, File.join(@instance, 'authority'), File.join(@home, '.codex')].each { |path| FileUtils.mkdir_p(path, mode: 0o700); File.chmod(0o700, path) }
    %w[repos work archive worktrees].each { |name| FileUtils.mkdir_p(File.join(@workspace, name)) }
    @env = ENV.to_h.reject { |key, _value| key.start_with?('DEV_', 'CODEX_') }
              .merge('HOME' => @home, 'CODEX_HOME' => File.join(@home, '.codex'), 'DEV_WORKSPACE_CODEX_HOME' => File.join(@home, '.codex'),
                     'DEV_WORKSPACES_STATE' => @state, 'DEV_WORKSPACES_RUNTIME_DIR' => File.dirname(@instance),
                     'DEV_WORKSPACES_PROFILE' => File.join(@state, 'profile'), 'DEV_WORKSPACE_NAME' => 'fixture',
                     'GIT_CONFIG_GLOBAL' => '/dev/null', 'GIT_CONFIG_SYSTEM' => '/dev/null', 'GIT_CONFIG_NOSYSTEM' => '1',
                     'GIT_AUTHOR_NAME' => 'Repair fixture', 'GIT_AUTHOR_EMAIL' => 'repair@example.invalid',
                     'GIT_COMMITTER_NAME' => 'Repair fixture', 'GIT_COMMITTER_EMAIL' => 'repair@example.invalid')
    FileUtils.mkdir_p(File.join(@home, '.config/dev-workspaces'), mode: 0o700)
    File.write(File.join(@home, '.config/dev-workspaces/registry.json'), JSON.generate('schema' => 1, 'workspaces' => [{ 'name' => 'fixture', 'root' => @workspace, 'hostname' => 'fixture.invalid', 'aliases' => [] }]))
    File.chmod(0o600, File.join(@home, '.config/dev-workspaces/registry.json'))
    FileUtils.mkdir_p(File.join(@generation, 'bin'))
    # These are explicit command collaborators, not native persistence/protocol.
    script = <<~SH
      #!/bin/sh
      printf '%s\\n' "$*" >> '#{@root}/proof.log'
      case " $* " in
        *" --mode threadless "*|*" team require-archive-ready "*)
          test ! -e '#{@root}/native-failure' || exit 1
          ;;
      esac
      test ! -e '#{@root}/busy'
    SH
    %w[workspace-portal dev-session].each { |name| File.write(File.join(@generation, 'bin', name), script); File.chmod(0o700, File.join(@generation, 'bin', name)) }
    @helper = File.join(@private, 'proof')
    File.write(@helper, script); File.chmod(0o700, @helper)
    codex = File.join(@generation, 'codex')
    File.write(codex, "#!/bin/sh\nprintf 'codex 0.160.0\\n'\n"); File.chmod(0o700, codex)
    @env['DEV_WORKSPACES_SYSTEM_CODEX'] = codex
    File.symlink(@generation, @env.fetch('DEV_WORKSPACES_PROFILE'))
    File.write(File.join(@state, 'transition.lock'), ''); File.chmod(0o600, File.join(@state, 'transition.lock'))
    @socket = UNIXServer.new(File.join(@instance, 'app-server.sock'))
    File.write(File.join(@instance, 'tmux.sock'), '') # No running tmux in source fixtures.
    git('init', '--initial-branch=master', @workspace)
    File.write(File.join(@workspace, '.gitignore'), "/repos/\n/worktrees/\n")
    tracking = File.join(@workspace, 'work', SLUG)
    FileUtils.mkdir_p(tracking)
    File.write(File.join(tracking, 'plan.md'), "# Plan\n")
    File.binwrite(File.join(tracking, 'state.md'), PROSE)
    File.write(File.join(tracking, 'artifact.txt'), 'original artifact')
    File.write(File.join(@workspace, 'peer.txt'), 'original peer')
    git('-C', @workspace, 'add', '.')
    git('-C', @workspace, 'commit', '-m', 'fixture: original tracking')
    git('-C', @workspace, 'remote', 'add', 'origin', 'git@github.com:fixture/workspace.git')
    git('-C', @workspace, 'update-ref', 'refs/remotes/origin/master', 'HEAD')
    git('-C', @workspace, 'symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/master')
    source = File.realpath(ENV.fetch('REPAIR_TEST_RUNTIME_SOURCE'))
    @source = File.join(@root, 'runtime')
    canonical = File.join(@workspace, 'repos/dev-workspace.git')
    git('clone', '--bare', '--shared', source, canonical)
    git("--git-dir=#{canonical}", 'remote', 'set-url', 'origin', 'git@github.com:aither64/dev-workspace.git')
    git("--git-dir=#{canonical}", 'worktree', 'add', '--detach', @source, Repair::RUNTIME)
    runtime = Repair::Runtime.new(@workspace, @source, @env)
    selected = runtime.selected_coordinates(@env)
    helpers = File.expand_path('../bin/repair-legacy-sessions-2026-10-04-threadless', __dir__)
    context = { 'schema' => 1, 'workspace' => @workspace, 'runtime_source' => @source, 'runtime_commit' => Repair::RUNTIME, 'runtime' => selected,
                'helper' => { 'executable' => @helper, 'sha256' => Digest::SHA256.file(@helper).hexdigest, 'runtime_commit' => Repair::RUNTIME,
                              'sources' => %w[main.go web/receipt_bridge.go].to_h { |name| path = File.join(helpers, name); [path, Digest::SHA256.file(path).hexdigest] },
                              'go_mod_sha256' => blob_digest('portal/go.mod'), 'go_sum_sha256' => blob_digest('portal/go.sum') },
                'maintenance_window' => { 'operator' => 'fixture', 'evidence_reference' => 'disposable test only', 'crash_hold' => 'test owns every disposable writer',
                                          'exclusions' => %w[portal automatic external].map { |kind| { 'kind' => kind, 'name' => kind, 'method' => 'simulated collaborator', 'verify' => [@helper] } } } }
    runtime.close
    @context = File.join(@private, 'context.json')
    Repair.durable_json(@context, context)
    @env['REPAIR_LEGACY_CONTEXT'] = @context
    @mapping = File.join(@private, 'mapping.json')
    @projection = File.join(@private, 'projection.json')
    @recovery = File.join(@private, 'recovery.json')
    write_mapping('root_thread_id' => nil)
  end

  def teardown
    @socket&.close
    FileUtils.remove_entry(@root) if @root && File.directory?(@root)
  end

  def git(*arguments)
    output, error, status = Open3.capture3(@env, 'git', *arguments)
    assert(status.success?, "fixture Git failed: #{error}")
    output.strip
  end

  def blob_digest(path)
    output, error, status = Open3.capture3('git', '-C', @source, 'show', "#{Repair::RUNTIME}:#{path}")
    assert(status.success?, error)
    Digest::SHA256.hexdigest(output)
  end

  def write_mapping(values)
    File.write(@mapping, JSON.generate('schema' => 1, 'workspace' => @workspace, 'sessions' => [{ 'slug' => SLUG, 'rationale' => 'reviewed disposable exact identity' }.merge(values)]))
  end

  def project(name, checkout: false)
    seed = File.join(@root, name)
    git('init', '--initial-branch=master', seed)
    File.write(File.join(seed, 'file'), name)
    git('-C', seed, 'add', 'file'); git('-C', seed, 'commit', '-m', 'fixture: contemporaneous default')
    base = git('-C', seed, 'rev-parse', 'HEAD')
    git('-C', seed, 'branch', SLUG)
    canonical = File.join(@workspace, 'repos', "#{name}.git")
    git('clone', '--bare', seed, canonical)
    git("--git-dir=#{canonical}", 'remote', 'set-url', 'origin', "git@github.com:fixture/#{name}.git")
    git("--git-dir=#{canonical}", 'update-ref', 'refs/remotes/origin/master', base)
    git("--git-dir=#{canonical}", 'update-ref', "refs/remotes/origin/#{SLUG}", base)
    git("--git-dir=#{canonical}", 'symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/master')
    git("--git-dir=#{canonical}", 'worktree', 'add', File.join(@workspace, 'worktrees', SLUG, name), SLUG) if checkout
    [canonical, base]
  end

  def preview
    output = StringIO.new
    Repair::Tool.new(['preview', '--workspace', @workspace, '--runtime-source', @source, '--session', SLUG, '--mapping', @mapping, '--json'], environment: @env, output: output).run
    File.write(@projection, output.string)
    JSON.parse(output.string)
  end

  def apply(type = Repair::Tool, fault: nil)
    tool = type.new(['apply', '--projection', @projection, '--recovery', @recovery], environment: @env, input: StringIO.new("y\n"), output: StringIO.new)
    tool.fault = fault if fault
    tool.run
  end

  def full_proof_calls(slug = SLUG)
    File.readlines(File.join(@root, 'proof.log')).count do |line|
      (line.include?('--mode threadless ') || line.start_with?('team require-archive-ready ')) && line.include?("--session-slug #{slug} ")
    end
  end

  def receipt_proof_calls
    File.readlines(File.join(@root, 'proof.log')).count { |line| line.include?('--mode receipts ') }
  end

  def test_full_native_proofs_bracket_writes_and_final_failure_retries_without_resetting_grace
    project('alpha')
    write_mapping('root_thread_id' => ROOT_ID)
    assert_empty(preview['sessions'].first['blockers'])
    before = full_proof_calls
    checkpoints = []
    error = assert_raises(Repair::Error) do
      apply(FaultTool, fault: ->(recovery) {
        phase = recovery['rows'][0]['phase']
        checkpoints << [phase, full_proof_calls - before, receipt_proof_calls]
        File.write(File.join(@root, 'native-failure'), 'final proof unavailable') if phase == 'grace_started'
        false
      })
    end
    assert_match(/proof failed/, error.message)
    assert_equal(3, full_proof_calls - before) # All-row preflight, entry, failed final proof.
    assert_equal(1, checkpoints.first[1])
    assert(checkpoints.drop(1).all? { |entry| entry[1] == 2 }, 'intermediate checkpoints repeated native discovery')
    assert_operator(checkpoints.last[2], :>, checkpoints[1][2])
    assert_equal('grace_started', Repair.read_json(@recovery)['rows'][0]['phase'])
    head = git('-C', @workspace, 'rev-parse', 'HEAD')
    grace = Dir[File.join(@state, 'auto-archive', '*', "session-#{SLUG}.json")].first
    saved_grace = File.binread(grace)
    File.unlink(File.join(@root, 'native-failure'))
    before = full_proof_calls
    apply
    assert_equal(2, full_proof_calls - before)
    assert_equal('complete', Repair.read_json(@recovery)['rows'][0]['phase'])
    assert_equal(saved_grace, File.binread(grace))
    assert_equal(head, git('-C', @workspace, 'rev-parse', 'HEAD'))
    before = full_proof_calls
    apply
    assert_equal(before, full_proof_calls)
  end

  def test_entry_native_failure_preserves_tracking_and_retry_observes_afresh
    project('alpha')
    assert_empty(preview['sessions'].first['blockers'])
    head = git('-C', @workspace, 'rev-parse', 'HEAD')
    before = full_proof_calls
    assert_raises(Repair::Error) do
      apply(FaultTool, fault: ->(recovery) {
        if recovery['rows'][0]['phase'] == 'prepared' && recovery['rows'][0]['targets'].empty?
          File.write(File.join(@root, 'native-failure'), 'entry proof unavailable')
        end
        false
      })
    end
    assert_equal(2, full_proof_calls - before)
    assert_empty(Repair.read_json(@recovery)['rows'][0]['targets'])
    assert_equal(PROSE, File.binread(File.join(@workspace, 'work', SLUG, 'state.md')))
    refute(File.exist?(File.join(@workspace, 'work', SLUG, 'portal.yml')))
    assert_equal(head, git('-C', @workspace, 'rev-parse', 'HEAD'))
    File.unlink(File.join(@root, 'native-failure'))
    before = full_proof_calls
    apply
    assert_equal(2, full_proof_calls - before)
    assert_equal('complete', Repair.read_json(@recovery)['rows'][0]['phase'])
  end

  def test_missing_checkout_multiple_projects_and_unknown_base_repair
    project('alpha'); project('beta')
    row = preview.fetch('sessions').first
    assert_empty(row['blockers'])
    assert_equal(%w[alpha beta], row.dig('target', 'manifest', 'repositories').map { |repo| repo['project'] })
    assert(row.dig('target', 'manifest', 'repositories').all? { |repo| !repo.key?('initial_base_sha') })
    before = git('-C', @workspace, 'rev-parse', 'HEAD')
    apply
    assert_equal("---\nlifecycle: active\n---\n".b + PROSE, File.binread(File.join(@workspace, 'work', SLUG, 'state.md')))
    assert_equal('original artifact', File.read(File.join(@workspace, 'work', SLUG, 'artifact.txt')))
    assert_equal(1, git('-C', @workspace, 'rev-list', '--count', "#{before}..HEAD").to_i)
    grace = Dir[File.join(@state, 'auto-archive', '*', "session-#{SLUG}.json")].first
    first = File.binread(grace)
    File.unlink(@recovery) # Runtime independence: normal manifest has no tool references.
    manifest = YAML.safe_load(File.read(File.join(@workspace, 'work', SLUG, 'portal.yml')))
    assert_equal(%w[artifacts repositories schema slug], manifest.keys.sort)
    assert_equal(first, File.binread(grace))
  end

  def test_dirty_checkout_is_metadata_evidence_and_its_content_is_preserved
    project('alpha', checkout: true)
    checkout = File.join(@workspace, 'worktrees', SLUG, 'alpha')
    File.write(File.join(checkout, 'file'), 'real dirty tracked content')
    File.write(File.join(checkout, 'untracked'), 'untracked content')
    before = git('-C', checkout, 'diff', '--binary')
    status = git('-C', checkout, 'status', '--porcelain=v1', '--untracked-files=all')
    row = preview['sessions'].first
    assert_empty(row['blockers'])
    assert_equal(true, row.dig('evidence', 'inventory', 'worktrees', 0, 'dirty'))
    refute(DevSession::ArchiveCleanup.discovery_shape?(row.dig('evidence', 'inventory')))
    apply
    assert_equal(before, git('-C', checkout, 'diff', '--binary'))
    assert_equal(status, git('-C', checkout, 'status', '--porcelain=v1', '--untracked-files=all'))
    assert_equal('untracked content', File.read(File.join(checkout, 'untracked')))
  end

  def test_bulk_artifacts_are_hash_only_and_only_metadata_paths_are_committed
    project('alpha')
    tracking = File.join(@workspace, 'work', SLUG)
    artifact = File.join(tracking, 'artifact.txt')
    File.write(artifact, 'staged artifact'); git('-C', @workspace, 'add', artifact)
    File.write(artifact, 'unstaged artifact')
    index = git('-C', @workspace, 'ls-files', '--stage', '--', artifact)
    File.write(File.join(tracking, 'plan.md'), 'uncommitted plan prose')
    bulk = File.join(tracking, 'bulk')
    FileUtils.mkdir_p(bulk)
    520.times { |number| File.write(File.join(bulk, number.to_s), 'small artifact') }
    large = File.join(bulk, 'large')
    File.open(large, 'wb') { |file| file.truncate(9 * 1024 * 1024) }
    source_head = git('-C', @workspace, 'rev-parse', 'HEAD')
    row = preview['sessions'].first
    assert_empty(row['blockers'])
    files = row.fetch('source').fetch('files')
    assert_operator(files.length, :>, 512)
    assert_equal(9 * 1024 * 1024, files.fetch('bulk/large').fetch('size'))
    assert_equal(Digest::SHA256.file(large).hexdigest, files.fetch('bulk/large').fetch('sha256'))
    refute(files.fetch('bulk/large').key?('bytes'))
    refute(files.fetch('artifact.txt').key?('bytes'))
    assert(files.fetch('plan.md').key?('bytes'))
    apply
    changes = git('-C', @workspace, 'diff', '--name-only', source_head, 'HEAD').lines.map(&:strip)
    assert_equal(%W[work/#{SLUG}/portal.yml work/#{SLUG}/state.md], changes.sort)
    assert_equal(index, git('-C', @workspace, 'ls-files', '--stage', '--', artifact))
    assert_equal('unstaged artifact', File.read(artifact))
    assert_equal('uncommitted plan prose', File.read(File.join(tracking, 'plan.md')))
    assert_equal(files.fetch('bulk/large').fetch('sha256'), Digest::SHA256.file(large).hexdigest)
    assert_equal('', git('-C', @workspace, 'ls-files', '--', large))
  end

  def test_historical_additions_union_missing_obligations_and_require_retained_commits
    common, base = project('alpha')
    git("--git-dir=#{common}", 'update-ref', '-d', "refs/heads/#{SLUG}")
    git("--git-dir=#{common}", 'update-ref', '-d', "refs/remotes/origin/#{SLUG}")
    deleted = 'deleted-historical-feature'
    write_mapping('root_thread_id' => nil, 'repositories' => [
      { 'project' => 'alpha', 'branch' => deleted, 'historical_commits' => [base] }
    ])
    row = preview['sessions'].first
    assert_empty(row['blockers'])
    assert_equal(deleted, row.dig('target', 'manifest', 'repositories', 0, 'branch'))
    refute(row.dig('target', 'manifest', 'repositories', 0).key?('initial_base_sha'))
    proof = row.dig('evidence', 'repositories', 0)
    assert_nil(proof.fetch('refs').fetch("refs/heads/#{deleted}"))
    assert_equal(base, proof.fetch('historical_commits').first.fetch('commit'))
    apply
    assert_nil(Repair.run('git', "--git-dir=#{common}", 'rev-parse', '--verify', "refs/heads/#{deleted}", optional: true))

    # Object existence alone is insufficient: this real commit has no retained ref.
    blob = git('-C', @workspace, 'rev-parse', 'HEAD^{tree}')
    unreachable = git('-C', @workspace, 'commit-tree', blob, '-m', 'fixture: unreferenced historical object')
    write_mapping('root_thread_id' => nil, 'repositories' => [
      { 'project' => 'workspace', 'branch' => 'master', 'historical_commits' => [unreachable] }
    ])
    assert_match(/no retained reachability/, preview['sessions'].first['blockers'].join)
    write_mapping('root_thread_id' => nil, 'repositories' => [
      { 'project' => 'workspace', 'branch' => 'master', 'historical_commits' => [blob] }
    ])
    assert_match(/not an existing full commit/, preview['sessions'].first['blockers'].join)
  end

  def test_historical_mapping_cannot_replace_an_automatic_obligation_or_go_unused
    _common, base = project('alpha')
    write_mapping('root_thread_id' => nil, 'repositories' => [
      { 'project' => 'alpha', 'name' => 'historical-alpha', 'branch' => 'deleted-feature', 'historical_commits' => [base] }
    ])
    row = preview['sessions'].first
    assert_empty(row['blockers'])
    assert_equal([SLUG, 'deleted-feature'].sort, row.dig('target', 'manifest', 'repositories').map { |repo| repo['branch'] }.sort)
    write_mapping('root_thread_id' => nil, 'repositories' => [{ 'project' => 'alpha', 'branch' => 'unproved-feature' }])
    assert_match(/unused repository mapping/, preview['sessions'].first['blockers'].join)
  end

  def test_workspace_historical_master_accepts_only_its_recorded_sequential_repair_commits
    second = '2026-10-04-repair-second'
    directory = File.join(@workspace, 'work', second)
    FileUtils.mkdir_p(directory)
    File.write(File.join(directory, 'plan.md'), "# Second plan\n")
    File.binwrite(File.join(directory, 'state.md'), PROSE)
    git('-C', @workspace, 'add', directory); git('-C', @workspace, 'commit', '-m', 'fixture: second source')
    base = git('-C', @workspace, 'rev-parse', 'HEAD')
    File.write(@mapping, JSON.generate('schema' => 1, 'workspace' => @workspace, 'sessions' => [SLUG, second].sort.map { |slug|
      { 'slug' => slug, 'root_thread_id' => nil, 'rationale' => 'reviewed direct workspace commit',
        'repositories' => [{ 'project' => 'workspace', 'branch' => 'master', 'historical_commits' => [base] }] }
    }))
    output = StringIO.new
    Repair::Tool.new(['preview', '--workspace', @workspace, '--runtime-source', @source, '--session', SLUG, '--session', second, '--mapping', @mapping, '--json'], environment: @env, output: output).run
    projection = JSON.parse(output.string)
    assert(projection.fetch('sessions').all? { |row| row['blockers'] == [] })
    File.write(@projection, output.string)
    before = [SLUG, second].to_h { |slug| [slug, full_proof_calls(slug)] }
    assert_raises(Interrupted) { apply(FaultTool, fault: ->(recovery) { recovery['rows'][0]['phase'] == 'complete' }) }
    assert_equal(3, full_proof_calls(SLUG) - before[SLUG])
    assert_equal(1, full_proof_calls(second) - before[second])
    first = git('-C', @workspace, 'rev-parse', 'HEAD')
    before = [SLUG, second].to_h { |slug| [slug, full_proof_calls(slug)] }
    apply
    assert_equal(before[SLUG], full_proof_calls(SLUG))
    assert_equal(2, full_proof_calls(second) - before[second])
    assert_equal('2', git('-C', @workspace, 'rev-list', '--count', "#{base}..HEAD"))
    final = git('-C', @workspace, 'rev-parse', 'HEAD')
    refute_equal(first, final)
    before = [SLUG, second].to_h { |slug| [slug, full_proof_calls(slug)] }
    apply
    assert_equal(before, [SLUG, second].to_h { |slug| [slug, full_proof_calls(slug)] })
    assert_equal(final, git('-C', @workspace, 'rev-parse', 'HEAD'))
  end

  def test_unrecorded_tracking_commit_and_dirty_content_drift_refuse_saved_retry
    project('alpha', checkout: true)
    checkout = File.join(@workspace, 'worktrees', SLUG, 'alpha')
    File.write(File.join(checkout, 'file'), 'original dirt')
    assert_empty(preview['sessions'].first['blockers'])
    assert_raises(Interrupted) { apply(FaultTool, fault: ->(recovery) { recovery['rows'][0]['phase'] == 'files_written' }) }
    File.write(File.join(checkout, 'file'), 'different dirt with the same dirty boolean')
    assert_match(/worktree\/native\/retained evidence changed/, assert_raises(Repair::Error) { apply }.message)
    File.write(File.join(checkout, 'file'), 'original dirt')
    File.write(File.join(@workspace, 'peer.txt'), 'external committed change')
    git('-C', @workspace, 'add', 'peer.txt'); git('-C', @workspace, 'commit', '-m', 'fixture: unrecorded outside commit')
    assert_match(/tracking HEAD changed/, assert_raises(Repair::Error) { apply }.message)
    assert_equal('files_written', Repair.read_json(@recovery)['rows'][0]['phase'])
  end

  def test_selected_socket_alias_keeps_logical_identity_and_requires_a_unix_target
    logical = @socket.path
    @socket.close
    File.unlink(logical)
    @socket = UNIXServer.new(File.join(@root, 'backend.sock'))
    File.symlink(@socket.path, logical)
    runtime = Repair::Runtime.new(@workspace, @source, @env)
    selection = -> { runtime.selected_coordinates(@env) }
    context = Repair::Context.new(@context, @workspace, @source, @env, selection: selection)
    assert_equal(logical, context.runtime['socket'])
    assert_equal(logical, context.child_environment['DEV_SESSION_CODEX_SOCKET'])
    assert_equal(Process.euid, File.stat(logical).uid)
    assert(context.check!)

    original = Repair.read_json(@context)
    [@socket.path, 'app-server.sock', File.join(@instance, './app-server.sock')].each do |coordinate|
      changed = Repair.read_json(@context)
      changed['runtime']['socket'] = coordinate
      Repair.durable_json(@context, changed)
      error = assert_raises(Repair::Error) { Repair::Context.new(@context, @workspace, @source, @env, selection: selection) }
      assert_match(/actual host registry\/profile\/runtime selection/, error.message)
    end
    Repair.durable_json(@context, original)
    File.unlink(logical)
    regular = File.join(@root, 'regular-file')
    File.write(regular, 'not a socket')
    File.symlink(regular, logical)
    error = assert_raises(Repair::Error) { Repair::Context.new(@context, @workspace, @source, @env, selection: selection) }
    assert_match(/owned Unix socket/, error.message)
  ensure
    runtime&.close
  end

  def test_registered_missing_refs_remain_obligations_and_structured_bases_are_real
    canonical, base = project('alpha')
    manifest = { 'schema' => 1, 'slug' => SLUG, 'repositories' => [{ 'name' => 'alpha', 'project' => 'alpha', 'github' => 'fixture/alpha', 'branch' => SLUG, 'default_branch' => 'master', 'initial_base_sha' => base }], 'artifacts' => [] }
    portal = File.join(@workspace, 'work', SLUG, 'portal.yml')
    File.write(portal, YAML.dump(manifest)); git('-C', @workspace, 'add', portal); git('-C', @workspace, 'commit', '-m', 'fixture: structured contemporaneous base')
    File.unlink(portal)
    git("--git-dir=#{canonical}", 'update-ref', '-d', "refs/heads/#{SLUG}")
    git("--git-dir=#{canonical}", 'update-ref', '-d', "refs/remotes/origin/#{SLUG}")
    row = preview['sessions'].first
    assert_empty(row['blockers'])
    assert_equal(base, row.dig('target', 'manifest', 'repositories', 0, 'initial_base_sha'))
    assert_nil(row.dig('evidence', 'repositories', 0, 'refs', "refs/heads/#{SLUG}"))
    apply
    assert_nil(Repair.run('git', "--git-dir=#{canonical}", 'rev-parse', '--verify', "refs/heads/#{SLUG}", optional: true))
  end

  def test_real_registered_checkout_empty_container_and_unknown_file_refusal
    project('alpha', checkout: true)
    FileUtils.mkdir_p(File.join(@workspace, 'worktrees', SLUG, 'empty'))
    row = preview['sessions'].first
    assert_empty(row['blockers'])
    assert_equal(['alpha'], row.dig('evidence', 'inventory', 'worktrees').map { |record| record['path'] })
    assert_includes(row.dig('evidence', 'inventory', 'containers').map { |record| record['path'] }, 'empty')
    apply
    assert(File.directory?(File.join(@workspace, 'worktrees', SLUG, 'alpha')))
    File.write(File.join(@workspace, 'worktrees', SLUG, 'empty/unknown'), 'do not adopt')
    assert_match(/unexpected|unknown/, preview['sessions'].first.fetch('blockers').join)
  end

  def test_retained_root_hold_hooks_and_unrelated_index_survive_once_only_retry
    project('alpha')
    write_mapping('root_thread_id' => ROOT_ID)
    File.write(File.join(@workspace, 'peer.txt'), 'staged peer'); git('-C', @workspace, 'add', 'peer.txt')
    before_index = git('-C', @workspace, 'ls-files', '--stage', '--', 'peer.txt')
    hook = File.join(@workspace, '.git/hooks/pre-commit')
    File.write(hook, "#!/bin/sh\nprintf 'hook\\n' >> '#{@root}/hooks.log'\n"); File.chmod(0o700, hook)
    source_stat = File.stat(File.join(@workspace, 'work', SLUG))
    identity = Digest::SHA256.hexdigest(JSON.generate(['session-observation-v1', @workspace, SLUG, source_stat.dev, source_stat.ino, ROOT_ID]))
    store = WorkspaceAutoArchive::Store.new(state_root: @state, workspace: @workspace)
    store.lock { store.write("session-#{SLUG}", 'slug' => SLUG, 'identity' => identity, 'hold' => true) }
    assert_empty(preview['sessions'].first['blockers'])
    assert_raises(Interrupted) { apply(FaultTool, fault: ->(recovery) { recovery['rows'][0]['phase'] == 'grace_started' }) }
    apply
    reset = store.session(SLUG).fetch('reset_at')
    apply
    assert_equal(reset, store.session(SLUG)['reset_at'])
    assert(store.session(SLUG)['hold'])
    assert_equal(before_index, git('-C', @workspace, 'ls-files', '--stage', '--', 'peer.txt'))
    assert_equal(["hook\n"], File.readlines(File.join(@root, 'hooks.log')))
    manifest = YAML.safe_load(File.read(File.join(@workspace, 'work', SLUG, 'portal.yml')))
    assert_equal(ROOT_ID, manifest.dig('codex', 'thread_id'))
    refute(manifest.key?('creation'))
  end

  def test_staged_file_and_files_written_interruptions_retry_exactly_and_drift_refuses
    project('alpha')
    preview
    assert_raises(Interrupted) { apply(FaultTool, fault: ->(recovery) { !recovery['rows'][0]['targets'].empty? }) }
    assert_equal(PROSE, File.binread(File.join(@workspace, 'work', SLUG, 'state.md')))
    assert_raises(Interrupted) { apply(FaultTool, fault: ->(recovery) { recovery['rows'][0]['phase'] == 'files_written' }) }
    original = File.read(File.join(@workspace, 'work', SLUG, 'artifact.txt'))
    File.write(File.join(@workspace, 'work', SLUG, 'artifact.txt'), 'drift')
    assert_raises(Repair::Error) { apply }
    File.write(File.join(@workspace, 'work', SLUG, 'artifact.txt'), original)
    before = full_proof_calls
    apply
    assert_equal(2, full_proof_calls - before)
    assert_equal('complete', Repair.read_json(@recovery)['rows'][0]['phase'])
  end

  def test_commit_before_checkpoint_retry_reuses_exact_commit_and_failed_window_writes_nothing
    project('alpha')
    preview
    before = git('-C', @workspace, 'rev-parse', 'HEAD')
    File.write(File.join(@root, 'busy'), 'window exclusion not established')
    assert_raises(Repair::Error) { apply }
    refute(File.exist?(@recovery))
    assert_equal(PROSE, File.binread(File.join(@workspace, 'work', SLUG, 'state.md')))
    assert_equal(before, git('-C', @workspace, 'rev-parse', 'HEAD'))
    File.unlink(File.join(@root, 'busy'))
    assert_raises(Repair::Error) do
      apply(FaultTool, fault: ->(recovery) {
        File.write(File.join(@root, 'busy'), 'window lost before replacement') unless recovery['rows'][0]['targets'].empty?
        false
      })
    end
    assert_equal('prepared', Repair.read_json(@recovery)['rows'][0]['phase'])
    assert_equal(PROSE, File.binread(File.join(@workspace, 'work', SLUG, 'state.md')))
    refute(File.exist?(File.join(@workspace, 'work', SLUG, 'portal.yml')))
    assert_equal(before, git('-C', @workspace, 'rev-parse', 'HEAD'))
    File.unlink(File.join(@root, 'busy'))
    assert_raises(Interrupted) { apply(CommitFaultTool) }
    assert_equal('files_written', Repair.read_json(@recovery)['rows'][0]['phase'])
    committed = git('-C', @workspace, 'rev-parse', 'HEAD')
    refute_equal(before, committed)
    native_before = full_proof_calls
    apply
    assert_equal(2, full_proof_calls - native_before)
    assert_equal(committed, git('-C', @workspace, 'rev-parse', 'HEAD'))
    assert_equal('complete', Repair.read_json(@recovery)['rows'][0]['phase'])
  end

  def test_genuine_ready_cli_creation_without_goal_is_preserved_through_its_existing_owner
    project('alpha')
    write_mapping('root_thread_id' => ROOT_ID)
    portal = File.join(@workspace, 'work', SLUG, 'portal.yml')
    manifest = { 'schema' => 1, 'slug' => SLUG, 'repositories' => [], 'artifacts' => [],
                 'codex' => { 'thread_id' => ROOT_ID, 'socket_path' => @socket.path, 'client_version' => '0.160.0' },
                 'creation' => { 'state' => 'ready', 'initial_goal_sent' => false } }
    File.write(portal, YAML.dump(manifest))
    locks = File.join(@workspace, 'worktrees/.locks')
    FileUtils.mkdir_p(locks)
    journal = File.join(locks, "#{SLUG}.creation.json")
    Repair.durable_json(journal, { 'schema' => 1, 'slug' => SLUG, 'goal_sha256' => nil, 'run_codex' => true, 'state' => 'ready' })
    original = File.binread(journal)
    row = preview['sessions'].first
    assert_empty(row['blockers'])
    assert_equal(manifest['creation'], row.dig('target', 'manifest', 'creation'))
    apply
    repaired = YAML.safe_load(File.read(portal))
    assert_equal(manifest['creation'], repaired['creation'])
    assert_equal(ROOT_ID, repaired.dig('codex', 'thread_id'))
    assert_equal(original, File.binread(journal))
  end

  def test_default_mapping_selects_real_evidence_and_cannot_replace_a_current_root
    common, base = project('alpha')
    git("--git-dir=#{common}", 'branch', 'main', base)
    git("--git-dir=#{common}", 'symbolic-ref', 'refs/remotes/origin/HEAD', 'refs/remotes/origin/main')
    assert_match(/ambiguous.*default/, preview['sessions'].first['blockers'].join)
    write_mapping('root_thread_id' => nil, 'repositories' => [{ 'project' => 'alpha', 'branch' => SLUG, 'default_branch' => 'master' }])
    assert_empty(preview['sessions'].first['blockers'])
    portal = File.join(@workspace, 'work', SLUG, 'portal.yml')
    File.write(portal, YAML.dump('schema' => 1, 'slug' => SLUG, 'repositories' => [], 'artifacts' => [],
                                'codex' => { 'thread_id' => ROOT_ID, 'socket_path' => @socket.path, 'client_version' => '0.160.0' }))
    assert_match(/cannot replace.*root/, preview['sessions'].first['blockers'].join)
    refute(File.exist?(@recovery))
  end

  def test_all_selected_rows_are_revalidated_before_any_tracking_write
    project('alpha')
    second = '2026-10-04-repair-second'
    directory = File.join(@workspace, 'work', second)
    FileUtils.mkdir_p(directory)
    File.write(File.join(directory, 'plan.md'), "# Second plan\n")
    File.binwrite(File.join(directory, 'state.md'), PROSE)
    git('-C', @workspace, 'add', directory)
    git('-C', @workspace, 'commit', '-m', 'fixture: second raw row')
    File.write(@mapping, JSON.generate('schema' => 1, 'workspace' => @workspace, 'sessions' => [
      { 'slug' => SLUG, 'root_thread_id' => nil, 'rationale' => 'exact fixture refs' },
      { 'slug' => second, 'root_thread_id' => nil, 'scope' => 'coordination_only', 'rationale' => 'reviewed empty fixture scope' }
    ]))
    output = StringIO.new
    Repair::Tool.new(['preview', '--workspace', @workspace, '--runtime-source', @source,
                     '--session', SLUG, '--session', second, '--mapping', @mapping, '--json'], environment: @env, output: output).run
    File.write(@projection, output.string)
    assert(JSON.parse(output.string)['sessions'].all? { |row| row['blockers'].empty? })
    File.binwrite(File.join(directory, 'state.md'), PROSE + "Later edit\n")
    assert_raises(Repair::Error) { apply }
    refute(File.exist?(@recovery))
    assert_equal(PROSE, File.binread(File.join(@workspace, 'work', SLUG, 'state.md')))
    refute(File.exist?(File.join(@workspace, 'work', SLUG, 'portal.yml')))
  end

  def test_archived_terminal_metadata_root_and_unknown_base_survive_without_active_grace
    _common, final = project('alpha')
    directory = File.join(@workspace, 'archive', SLUG)
    git('-C', @workspace, 'mv', File.join('work', SLUG), File.join('archive', SLUG))
    state = "---\nlifecycle: complete\n---\n".b + PROSE
    File.binwrite(File.join(directory, 'state.md'), state)
    manifest = { 'schema' => 1, 'slug' => SLUG, 'artifacts' => [], 'finalized_at' => '2026-10-04T00:00:00Z',
                 'codex' => { 'thread_id' => ROOT_ID, 'socket_path' => @socket.path, 'client_version' => '0.160.0' },
                 'repositories' => [{ 'name' => 'alpha', 'project' => 'alpha', 'github' => 'fixture/alpha',
                                      'branch' => SLUG, 'default_branch' => 'master', 'final_head_sha' => final }] }
    File.write(File.join(directory, 'portal.yml'), YAML.dump(manifest))
    git('-C', @workspace, 'add', directory)
    git('-C', @workspace, 'commit', '-m', 'fixture: genuine recorded terminal projection')
    write_mapping('root_thread_id' => ROOT_ID)
    row = preview['sessions'].first
    assert_empty(row['blockers'])
    apply
    assert_equal(state, File.binread(File.join(directory, 'state.md')))
    repaired = YAML.safe_load(File.read(File.join(directory, 'portal.yml')))
    assert_equal(ROOT_ID, repaired.dig('codex', 'thread_id'))
    assert_equal(final, repaired.dig('repositories', 0, 'final_head_sha'))
    refute(repaired['repositories'][0].key?('initial_base_sha'))
    assert_empty(Dir[File.join(@state, 'auto-archive', '*', "session-#{SLUG}.json")])
  end

  def test_unknown_scope_terminal_provenance_modern_creation_and_busy_refuse_before_receipt
    write_mapping('root_thread_id' => nil)
    assert_match(/scope/, preview['sessions'].first['blockers'].join)
    project('alpha')
    portal = File.join(@workspace, 'work', SLUG, 'portal.yml')
    File.write(portal, YAML.dump('schema' => 1, 'slug' => SLUG, 'creation' => {}, 'repositories' => [], 'artifacts' => []))
    assert_match(/creation/, preview['sessions'].first['blockers'].join)
    File.unlink(portal)
    File.write(File.join(@root, 'busy'), 'unknown native proof')
    assert_match(/proof failed/, preview['sessions'].first['blockers'].join)
    refute(File.exist?(@recovery))
    File.unlink(File.join(@root, 'busy'))
    FileUtils.mv(File.join(@workspace, 'work', SLUG), File.join(@workspace, 'archive', SLUG))
    assert_match(/terminal|provenance/, preview['sessions'].first['blockers'].join)
  end
end
