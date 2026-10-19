require 'minitest/autorun'
require 'tmpdir'
require 'fileutils'
require 'json'
require 'digest'
require 'yaml'
load '/nix/store/klrzzbd8zayqq6p3lc8cpgxniy8gdjsq-dev-workspace-0.2.0/libexec/workspace-portal/.dev-session-wrapped'
require_relative 'creation-provider-retained-seed-guard'

class RetainedSeedGuardTest < Minitest::Test
  def setup
    @tmp = Dir.mktmpdir
    @slug = 'retained'
    @tracking = File.join(@tmp, 'work', @slug)
    FileUtils.mkdir_p(@tracking)
    @goal = File.join(@tmp, 'goal')
    File.write(@goal, 'accepted request')
    @expected = {'workspace' => @tmp, 'slug' => @slug, 'threadId' => 'retained-root',
                 'goalSha256' => Digest::SHA256.file(@goal).hexdigest}
    @manifest = File.join(@tracking, 'portal.yml')
    @value = {'codex' => {'thread_id' => 'retained-root'}, 'creation' =>
      {'initial_goal_attempted' => true, 'initial_goal_sent' => false, 'goal_sha256' => @expected['goalSha256']}}
    File.write(@manifest, YAML.dump(@value))
    File.write(File.join(@tracking, 'plan.md'), 'developed plan')
    File.write(File.join(@tracking, 'state.md'), 'developed state')
    stat = File.stat(@tracking)
    @frozen = {'trackingDevice' => stat.dev, 'trackingInode' => stat.ino, 'files' =>
      Dir.children(@tracking).to_h { |name| p = File.join(@tracking, name); [p, {'sha256' => Digest::SHA256.file(p).hexdigest}] }}
    @runner = DevSession::Runner.allocate
    @runner.instance_variable_set(:@workspace, @tmp)
  end

  def teardown
    FileUtils.remove_entry(@tmp)
  end

  def run_guard(slug: @slug, accepted: true)
    @runner.instance_exec(slug, @goal, accepted, @expected, @frozen, &RETAINED_SEED_GUARD)
  end

  def test_exact_inputs_preserve_developed_tracking
    before = @frozen['files'].keys.to_h { |p| [p, File.binread(p)] }
    assert_nil run_guard
    assert_equal before, before.keys.to_h { |p| [p, File.binread(p)] }
  end

  def test_missing_proof_wrong_identity_and_modified_goal_refuse
    assert_raises(DevSession::Error) { run_guard(accepted: false) }
    assert_raises(DevSession::Error) { run_guard(slug: 'replacement') }
    File.write(@goal, 'another request')
    assert_raises(DevSession::Error) { run_guard }
  end

  def test_tracking_drift_and_initial_attempt_changes_refuse
    File.write(File.join(@tracking, 'plan.md'), 'changed plan')
    assert_raises(DevSession::Error) { run_guard }
    File.write(File.join(@tracking, 'plan.md'), 'developed plan')
    @value['creation']['initial_goal_attempted'] = false
    File.write(@manifest, YAML.dump(@value))
    @frozen['files'][@manifest]['sha256'] = Digest::SHA256.file(@manifest).hexdigest
    assert_raises(DevSession::Error) { run_guard }
  end
end
