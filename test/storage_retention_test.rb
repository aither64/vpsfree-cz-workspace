# frozen_string_literal: true

require 'minitest/autorun'
require 'tmpdir'
require 'fileutils'
load File.expand_path('../bin/compact-session-storage', __dir__)

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

  def test_preview_does_not_write_and_apply_is_repeatable
    with_fixture do |options|
      path = tracking(options, 'old-session')
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

  def test_active_tracking_and_pending_journal_are_preserved
    with_fixture do |options|
      active = tracking(options, 'active-session')
      pending = tracking(options, 'pending-session')
      FileUtils.mkdir_p(File.join(options[:workspace], 'work', 'active-session'))
      locks = File.join(options[:workspace], 'worktrees', '.locks')
      FileUtils.mkdir_p(locks)
      File.write(File.join(locks, 'pending-session.archive.json'), '{}')
      rows = SessionStorageCompactor.new(options).run
      assert rows.all? { |row| row['skipped'] }
      assert File.file?(File.join(active, 'raw.log'))
      assert File.file?(File.join(pending, 'raw.log'))
    end
  end
end
