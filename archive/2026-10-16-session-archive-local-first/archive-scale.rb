# Disposable acceptance fixture. All repositories and tracking are under with_workspace.
require '/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-session-archive-local-first/dev-workspace/test/dev_session_test'

SCALE_DIGESTS = Hash.new(0)
module ArchiveScaleDigests
  def tree_digest(root, **options)
    SCALE_DIGESTS[root] += 1
    super
  end
end
DevSession::ArchiveRecovery.prepend(ArchiveScaleDigests)

class DevSessionTest
  def test_archive_scale_local_closure
    with_archive_cleanup_fixture do |runner, workspace, slug, _common, checkout|
      count = 34_975
      length = 47_174
      block = ('synthetic archive acceptance contents\n' * 1400).b
      checkout_bytes = 0
      count.times do |number|
        directory = File.join(checkout, 'scale', format('%03d', number / 250))
        FileUtils.mkdir_p(directory)
        content = format('%08d', number) + block.byteslice(0, length - 8)
        File.binwrite(File.join(directory, format('%08d', number)), content)
        checkout_bytes += content.bytesize
      end
      assert_git_success('git', '-C', checkout, 'add', 'scale')
      assert_git_success('git', '-C', checkout, 'commit', '-m', 'synthetic clean scale checkout')
      tracking = File.join(workspace, 'work', slug, 'scale-artifacts')
      FileUtils.mkdir_p(tracking)
      tracking_bytes = 0
      tracking_content = ('synthetic retained tracking artifact\n' * 4000).byteslice(0, 134_904)
      7131.times do |number|
        File.binwrite(File.join(tracking, number.to_s), tracking_content)
        tracking_bytes += tracking_content.bytesize
      end
      runner.instance_variable_get(:@env)['DEV_WORKSPACE_DEFER_TRACKING'] = '1'
      runner.define_singleton_method(:require_linear_workspace_master_for_tracking!) do |**|
        raise DevSession::Error, 'synthetic remote unavailable'
      end
      commands = runner.instance_variable_get(:@command_runner)
      counts = Hash.new(0)
      ref_updates = []
      commands.define_singleton_method(:capture) do |arguments, **options|
        if File.basename(arguments.first.to_s) == 'git'
          operation = arguments.find { |item| %w[update-ref hash-object cat-file ls-tree status worktree fetch].include?(item) } || 'other'
          counts[operation] += 1
          ref_updates << arguments if operation == 'update-ref'
        end
        super(arguments, **options)
      end
      commands.define_singleton_method(:stream) do |arguments, **options, &block|
        counts['cat-file-stream'] += 1
        super(arguments, **options, &block)
      end
      SCALE_DIGESTS.clear
      started = Process.clock_gettime(Process::CLOCK_MONOTONIC)
      runner.archive(slug, as_is: true, explicit: true)
      elapsed = Process.clock_gettime(Process::CLOCK_MONOTONIC) - started
      archive_counts = counts.dup
      digest_calls = SCALE_DIGESTS.values.sum
      checkout_digest_calls = SCALE_DIGESTS[checkout]
      assert_operator(elapsed, :<, 720)
      refute(File.exist?(checkout))
      assert_equal('pending', runner.tracking_sync_receipt(slug).fetch('state'))
      refute(File.exist?(runner.send(:lifecycle_journal_file, slug, 'archive')))
      manifest = YAML.safe_load(File.read(File.join(workspace, 'archive', slug, 'portal.yml')))
      recovery = runner.archive_cleanup_recovery(slug, manifest.fetch('archive_operation_id'))
      record = recovery.records.first
      saved, destination = recovery.send(:read_record, record)
      assert_equal('git', saved.fetch('kind'))
      copied_bytes = Dir.glob(File.join(destination, 'files', '**', '*')).sum { |path| File.file?(path) ? File.size(path) : 0 }
      assert_equal(0, copied_bytes)
      assert_equal(0, archive_counts['fetch'])
      # One explicit head proof and one recovery batch, independent of file count.
      assert_equal(2, archive_counts['update-ref'])
      assert_equal(1, ref_updates.count { |arguments| arguments.include?('--stdin') })
      assert_equal(1, ref_updates.count { |arguments| arguments.any? { |item| item.start_with?('refs/dev-session-archives/') && item.end_with?('/head') } })
      runner.revive(slug, as_is: true)
      assert_equal('revive', runner.tracking_sync_receipt(slug).fetch('direction'))
      assert_equal('pending', runner.tracking_sync_receipt(slug).fetch('state'))
      assert_equal(format('%08d', count - 1) + block.byteslice(0, length - 8), File.binread(File.join(checkout, 'scale', format('%03d', (count - 1) / 250), format('%08d', count - 1))))
      assert_equal(tracking_content, File.binread(File.join(tracking, '7130')))
      result = {schema: 1, runtime_head: ENV.fetch('ARCHIVE_TEST_HEAD'), checkout_files: count,
                checkout_bytes: checkout_bytes, tracking_files: 7131, tracking_bytes: tracking_bytes,
                local_archive_seconds: elapsed, copied_working_file_bytes: copied_bytes,
                git_commands_during_archive: archive_counts, tree_digest_calls: digest_calls,
                checkout_tree_digest_calls: checkout_digest_calls, restored_and_coalesced: true}
      File.write(ENV.fetch('ARCHIVE_SCALE_RESULT'), JSON.pretty_generate(result) + "\n")
      puts JSON.generate(result)
    end
  end
end
