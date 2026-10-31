# frozen_string_literal: true

require 'minitest/autorun'
require 'tmpdir'
require 'fileutils'
require 'open3'
load File.expand_path('../bin/compact-session-storage', __dir__)

class TrackingIgnoreTest < Minitest::Test
  RECORDS = %w[plan.md portal.yml raw.log notes/summary.md notes/portal.yml notes/raw.log].freeze

  def with_tracking_ignore_fixture
    Dir.mktmpdir('tracking-ignore-') do |workspace|
      tracking_git(workspace, 'init', '--quiet')
      File.write(File.join(workspace, '.gitignore'),
                 File.read(File.expand_path('../.gitignore', __dir__)))
      File.write(File.join(workspace, '.git/info/exclude'),
                 "/work/sensitive-session/\n/archive/sensitive-session/\n")
      yield workspace
    end
  end

  def tracking_git(workspace, *args, expected_status: 0)
    output, error, status = Open3.capture3(
      {'GIT_CONFIG_GLOBAL' => File::NULL, 'GIT_CONFIG_NOSYSTEM' => '1'},
      'git', '-C', workspace, *args
    )
    assert_equal expected_status, status.exitstatus, "git #{args.join(' ')}: #{error}"
    output
  end

  def write_tracking_records(workspace, root)
    RECORDS.each do |record|
      path = File.join(workspace, root, record)
      FileUtils.mkdir_p(File.dirname(path))
      File.write(path, 'synthetic fixture')
    end
  end

  def test_tracking_ignore_preserves_private_roots_and_descendants
    with_tracking_ignore_fixture do |workspace|
      %w[work archive].each do |tracking|
        root = "#{tracking}/sensitive-session"
        [false, true].each do |create|
          write_tracking_records(workspace, root) if create
          ["#{root}/", *RECORDS.map { |record| "#{root}/#{record}" },
           "#{root}/future/nested/summary.md", "#{root}/future/portal.yml"].each do |path|
            tracking_git(workspace, 'check-ignore', '--quiet', '--', path)
          end
        end
      end
    end
  end

  def test_tracking_ignore_stages_only_ordinary_retained_records
    with_tracking_ignore_fixture do |workspace|
      expected = ['.gitignore']
      %w[work archive].each do |tracking|
        %w[ordinary-session sensitive-session].each do |slug|
          write_tracking_records(workspace, "#{tracking}/#{slug}")
        end
        RECORDS.reject { |record| record.end_with?('.log') }.each do |record|
          expected << "#{tracking}/ordinary-session/#{record}"
        end
      end
      tracking_git(workspace, 'add', '-A')
      assert_equal expected.sort, tracking_git(workspace, 'ls-files', '-z').split("\0").sort
    end
  end

  def test_tracking_ignore_detects_explicit_private_root_overrides
    with_tracking_ignore_fixture do |workspace|
      %w[work archive].each do |tracking|
        root = "#{tracking}/sensitive-session/"
        FileUtils.mkdir_p(File.join(workspace, root))
        tracking_git(workspace, 'check-ignore', '--quiet', '--', root)
        File.open(File.join(workspace, '.gitignore'), 'a') { |file| file.puts "!/#{root}" }
        tracking_git(workspace, 'check-ignore', '--quiet', '--', root, expected_status: 1)
      end
    end
  end
end

class StorageRetentionTest < Minitest::Test
  def with_fixture
    Dir.mktmpdir do |root|
      workspace = File.join(root, 'workspace')
      state = File.join(root, 'state')
      authority = File.join(root, 'authority')
      runtime = ENV.fetch('DEV_WORKSPACE_RUNTIME_SOURCE')
      FileUtils.mkdir_p([workspace, state])
      File.symlink(runtime, File.join(state, 'profile'))
      options = {workspace: workspace, state: state, authority: authority,
                 runtime: runtime, tracking_only: true, apply: false}
      yield options
    end
  end

  def tracking(options, slug, lifecycle = 'archived')
    path = File.join(options[:workspace], 'archive', slug)
    FileUtils.mkdir_p(path)
    File.write(File.join(path, 'state.md'), "---\nlifecycle: #{lifecycle}\n---\n")
    File.write(File.join(path, 'plan.md'), 'retain summary')
    File.write(File.join(path, 'portal.yml'), "schema: 1\nrepositories: []\nartifacts: []\n")
    File.write(File.join(path, 'raw.log'), 'discard log')
    path
  end

  def creation_record(options, slug, record = {'state' => 'ready'})
    locks = File.join(options[:workspace], 'worktrees', '.locks')
    FileUtils.mkdir_p(locks)
    path = File.join(locks, "#{slug}.creation.json")
    File.write(path, JSON.generate({'schema' => 3, 'slug' => slug}.merge(record)))
    path
  end

  def test_preview_does_not_write_and_apply_is_repeatable
    with_fixture do |options|
      path = tracking(options, 'old-session')
      creation = creation_record(options, 'old-session')
      original_creation = File.binread(creation)
      preview = SessionStorageCompactor.new(options).run
      assert_equal 1, preview.first['trackingFiles']
      assert File.file?(File.join(path, 'raw.log'))
      refute File.exist?(options[:authority])
      # Shared tracking lock requires a real Git common directory.
      system('git', 'init', '--quiet', options[:workspace], exception: true)
      result = SessionStorageCompactor.new(options.merge(apply: true)).run
      assert_equal 1, result.first['trackingFiles']
      refute File.exist?(File.join(path, 'raw.log'))
      assert_equal 'retain summary', File.read(File.join(path, 'plan.md'))
      assert_equal 0, SessionStorageCompactor.new(options.merge(apply: true)).run.first['trackingFiles']
      assert_equal original_creation, File.binread(creation)
    end
  end

  def test_apply_rechecks_selected_runtime_after_transition_admission
    with_fixture do |options|
      path = tracking(options, 'old-session')
      command = SessionStorageCompactor.new(options.merge(apply: true))
      command.define_singleton_method(:with_lock) do |lock_path, mode, &block|
        if lock_path == File.join(options[:state], 'transition.lock')
          replacement = File.join(options[:state], 'replacement-runtime')
          FileUtils.mkdir_p(replacement)
          File.unlink(File.join(options[:state], 'profile'))
          File.symlink(replacement, File.join(options[:state], 'profile'))
        end
        super(lock_path, mode, &block)
      end
      error = assert_raises(RuntimeError) { command.run }
      assert_includes error.message, 'selected installed runtime'
      assert File.file?(File.join(path, 'raw.log'))
    end
  end

  def test_recovery_preview_and_apply_finish_compact_payload_cleanup
    with_fixture do |options|
      tracking(options, 'old-session')
      creation_record(options, 'old-session')
      workspace = options[:workspace]
      system('git', 'init', '--quiet', workspace, exception: true)
      system('git', '-C', workspace, '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.test',
             'commit', '--quiet', '--allow-empty', '-m', 'retained head', exception: true)
      head = IO.popen(['git', '-C', workspace, 'rev-parse', 'HEAD'], &:read).strip
      ref = 'refs/dev-session-archives/fixture/head'
      system('git', '-C', workspace, 'update-ref', ref, head, exception: true)
      record = {'path' => 'sample', 'common_dir' => File.realpath(File.join(workspace, '.git')),
                'head' => head, 'branch' => 'fixture'}
      identity = "#{File.basename(workspace)}-#{Digest::SHA256.hexdigest(workspace)[0, 16]}"
      root = File.join(options[:state], 'archived-worktrees', identity, 'old-session', 'fixture')
      destination = File.join(root, Digest::SHA256.hexdigest('sample'))
      FileUtils.mkdir_p(File.join(destination, 'files'))
      File.write(File.join(root, 'inventory.json'), JSON.generate('schema' => 3, 'worktrees' => [record]))
      File.write(File.join(destination, 'record.json'), JSON.generate(record.merge('format' => 3, 'kind' => 'committed', 'head_ref' => ref)))
      payload = File.join(destination, 'files', 'raw.log')
      File.write(payload, 'discard ' * 1000)
      outside = File.join(workspace, 'outside')
      File.write(outside, 'keep external data')
      File.symlink(outside, File.join(destination, 'files', 'outside-link'))
      selected = options.merge(tracking_only: false, recovery_only: true)
      preview = SessionStorageCompactor.new(selected).run.first
      assert_operator preview['recoveryBytes'], :>, 0
      assert File.file?(payload)
      result = SessionStorageCompactor.new(selected.merge(apply: true)).run.first
      assert_operator result['recoveryBytesRemaining'], :<, result['recoveryBytes']
      refute File.exist?(File.join(destination, 'files'))
      assert_equal 'keep external data', File.read(outside)
      assert_equal head, IO.popen(['git', '-C', workspace, 'rev-parse', ref], &:read).strip
      repeated = SessionStorageCompactor.new(selected.merge(apply: true)).run.first
      assert_equal repeated['recoveryBytes'], repeated['recoveryBytesRemaining']
    end
  end

  def test_legacy_file_snapshot_compacts_after_completed_creation
    with_fixture do |options|
      tracking(options, 'old-session')
      creation_record(options, 'old-session')
      workspace = options[:workspace]
      system('git', 'init', '--quiet', workspace, exception: true)
      system('git', '-C', workspace, '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.test',
             'commit', '--quiet', '--allow-empty', '-m', 'retained head', exception: true)
      head = IO.popen(['git', '-C', workspace, 'rev-parse', 'HEAD'], &:read).strip
      group = File.join(options[:state], 'original-worktrees')
      source = File.join(group, 'sample')
      system('git', '-C', workspace, 'worktree', 'add', '--quiet', '--detach', source, head, exception: true)
      File.write(File.join(source, 'build-output'), 'disposable ' * 1000)
      admin = IO.popen(['git', '-C', source, 'rev-parse', '--absolute-git-dir'], &:read).strip
      record = {'path' => 'sample', 'common_dir' => File.realpath(File.join(workspace, '.git')),
                'admin_dir' => admin, 'head' => head, 'branch' => nil}
      identity = "#{File.basename(workspace)}-#{Digest::SHA256.hexdigest(workspace)[0, 16]}"
      root = File.join(options[:state], 'archived-worktrees', identity, 'old-session', 'fixture')
      destination = File.join(root, Digest::SHA256.hexdigest('sample'))
      selected = options.merge(tracking_only: false, recovery_only: true)
      # Preview loads the selected runtime without changing archive data.
      SessionStorageCompactor.new(selected).run
      recovery = DevSession::ArchiveRecovery.new(root, group, DevSession::CommandRunner.new(out: $stderr, err: $stderr))
      recovery.capture_legacy!([record])
      assert_equal 2, JSON.parse(File.read(File.join(root, 'inventory.json')))['schema']
      assert File.file?(File.join(destination, 'files', 'build-output'))
      assert_equal [record], recovery.records

      result = SessionStorageCompactor.new(selected.merge(apply: true)).run.first
      assert_operator result['recoveryBytesRemaining'], :<, result['recoveryBytes']
      assert_equal 3, JSON.parse(File.read(File.join(root, 'inventory.json')))['schema']
      assert_equal 'committed', JSON.parse(File.read(File.join(destination, 'record.json')))['kind']
      refute File.exist?(File.join(destination, 'files'))
      refute File.exist?(File.join(destination, 'admin'))
      assert_equal [record], recovery.records
    end
  end

  def test_incomplete_or_invalid_creation_records_preserve_tracking
    [
      {'state' => 'preparing'},
      {'state' => nil},
      {'state' => 'ready', 'slug' => 'another-session'}
    ].each do |record|
      with_fixture do |options|
        path = tracking(options, 'old-session')
        creation_record(options, 'old-session', record)
        result = SessionStorageCompactor.new(options.merge(apply: true)).run.first
        assert_equal 'lifecycle or tracking sync is unfinished', result['skipped']
        assert File.file?(File.join(path, 'raw.log'))
      end
    end
  end

  def test_malformed_creation_record_does_not_abort_other_archives
    with_fixture do |options|
      blocked = tracking(options, 'blocked-session')
      tracking(options, 'ready-session')
      creation = creation_record(options, 'blocked-session')
      File.write(creation, '{invalid')
      creation_record(options, 'ready-session')
      rows = SessionStorageCompactor.new(options).run.to_h { |row| [row['slug'], row] }
      assert_equal 'lifecycle or tracking sync is unfinished', rows['blocked-session']['skipped']
      assert_equal 1, rows['ready-session']['trackingFiles']
      assert File.file?(File.join(blocked, 'raw.log'))
    end
  end

  def test_ready_creation_does_not_override_pending_tracking_sync
    with_fixture do |options|
      path = tracking(options, 'old-session')
      creation_record(options, 'old-session')
      receipt = File.join(options[:state], 'tracking-sync', Digest::SHA256.hexdigest(options[:workspace]), 'old-session.json')
      FileUtils.mkdir_p(File.dirname(receipt))
      File.write(receipt, JSON.generate('state' => 'pending'))
      result = SessionStorageCompactor.new(options.merge(apply: true)).run.first
      assert_equal 'lifecycle or tracking sync is unfinished', result['skipped']
      assert File.file?(File.join(path, 'raw.log'))
    end
  end

  def test_active_tracking_and_pending_journal_are_preserved
    with_fixture do |options|
      active = tracking(options, 'active-session')
      pending = tracking(options, 'pending-session')
      FileUtils.mkdir_p(File.join(options[:workspace], 'work', 'active-session'))
      locks = File.join(options[:workspace], 'worktrees', '.locks')
      FileUtils.mkdir_p(locks)
      File.write(File.join(locks, 'pending-session.archive.json'), '{}')
      creation_record(options, 'active-session')
      creation_record(options, 'pending-session')
      rows = SessionStorageCompactor.new(options).run
      assert rows.all? { |row| row['skipped'] }
      assert File.file?(File.join(active, 'raw.log'))
      assert File.file?(File.join(pending, 'raw.log'))
    end
  end
end
