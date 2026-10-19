# One supervised recovery of the explicitly authorized retained creation.
require 'json'
require 'digest'
require 'tempfile'
require 'yaml'

root = '/home/aither/workspace/ai/vpsfree.cz'
slug = '2026-10-12-streamline-vpsadminos-config-imports'
predecessor = '/nix/store/klrzzbd8zayqq6p3lc8cpgxniy8gdjsq-dev-workspace-0.2.0'
candidate = '/nix/store/m12vcm73v1ld944ay9j284r5ikyi9x2n-dev-workspace-0.2.0'
profile = '/home/aither/.local/state/dev-workspaces/profile'
receipt_id = 'a9ea3ef892d5344be881fca8afc1eddfd09f4436dde6f79eeec407a43851e1c7'
directory = '/home/aither/.local/state/dev-workspaces/portal/vpsfree.cz-8a2a555cb2f65b33/creations'
raise 'selected predecessor changed' unless File.realpath(profile) == predecessor
receipt = JSON.parse(File.read(File.join(directory, "#{slug}.json")))
journal = JSON.parse(File.read(File.join(root, 'worktrees/.locks', "#{slug}.creation.json")))
unless receipt['schema'] == 3 && receipt['receiptId'] == receipt_id && receipt['attempt'] == 1 &&
       receipt['state'] == 'failed' && receipt['validated'] == true && receipt['workspace'] == root &&
       receipt.dig('request', 'kind') == 'new' && receipt.dig('request', 'slug') == slug &&
       journal['schema'] == 3 && journal['state'] == 'creating' && journal['slug'] == slug &&
       receipt['directTeam'] == journal['direct_team'] && receipt['model'] == journal['model'] &&
       receipt['effort'] == journal['effort'] && Digest::SHA256.hexdigest(receipt.fetch('goal')) == journal['goal_sha256']
  raise 'retained creation request changed; use its ordinary recovery'
end
raw = File.join('libexec/workspace-portal', '.dev-session-wrapped')
pattern = /^    def native_provider_arguments\n.*?(?=^    def update_native_client_version!)/m
old_method = File.read(File.join(predecessor, raw))[pattern]
new_method = File.read(File.join(candidate, raw))[pattern]
raise 'provider method delta differs from the reviewed fix' unless old_method && new_method &&
  old_method.sub('output = @runner.capture(', 'output, = @command_runner.capture(') == new_method
old_source = File.read(File.join(predecessor, raw))
new_source = File.read(File.join(candidate, raw))
raise 'installed helper changed' unless Digest::SHA256.hexdigest(old_source) ==
  '180c80420c6f444a2d939b44f930fbc0df8c1921cbdda6726564345b235119f1'
raise 'installed helper delta expanded' unless old_source.sub(old_method, new_method).split("\n", 2).last == new_source.split("\n", 2).last
manifest = YAML.safe_load(File.read(File.join(root, 'work', slug, 'portal.yml')))
thread_id = '01a1371c-24b8-7ac0-ab2d-5ed7a6bb2d4b'
raise 'retained conversation or initial attempt changed' unless manifest.dig('codex', 'thread_id') == thread_id &&
  manifest.dig('creation', 'initial_goal_attempted') == true && manifest.dig('creation', 'goal_sha256') == journal['goal_sha256']
load File.join(predecessor, 'libexec/.workspace-host-wrapped')
host = DevWorkspaceHost::Host.new
entry = host.send(:registry).find('vpsfree-cz')
raise 'registered workspace changed' unless entry && entry['root'] == root
load File.join(predecessor, raw)
DevSession::Runner.class_eval(new_method, 'reviewed-a10af6c4-provider-correction', 1)
require_relative 'creation-provider-retained-seed-guard'
frozen = JSON.parse(File.read(File.join(root, 'work/2026-10-13-workspace-coordination/creation-provider-recovery-tracking-frozen.json')))
expected = {'workspace' => root, 'slug' => slug, 'threadId' => thread_id, 'goalSha256' => journal.fetch('goal_sha256')}
accepted = false
DevSession::Runner.define_method(:seed_goal) do |requested_slug, goal_file|
  instance_exec(requested_slug, goal_file, accepted, expected, frozen, &RETAINED_SEED_GUARD)
end

host.send(:with_current_generation_lock, mode: File::LOCK_SH) do
raise 'selected predecessor changed during admission' unless File.realpath(profile) == predecessor
runtime = host.send(:instance_runtime, entry)
materialized = system(File.join(predecessor, 'bin/workspace-portal'), 'thread', 'require-materialized',
  '--thread-id', thread_id, '--cwd', File.join(root, 'work', slug), '--socket', runtime.fetch(:codex))
raise 'original conversation is not materialized' unless materialized
Tempfile.create(['.retained-goal-', '.txt'], directory) do |goal|
  Tempfile.create(['.retained-team-', '.json'], directory) do |preset|
    goal.write(receipt.fetch('goal')); goal.flush
    preset.write(JSON.generate(receipt.fetch('directTeam'))); preset.flush
    args = ['start', slug, '--as-is', '--exclusive', '--no-attach', '--goal-file', goal.path,
            '--json', '--team-preset', preset.path, '--model', receipt.fetch('model'),
            '--effort', receipt.fetch('effort'), '--creation-receipt-id', receipt_id,
            '--creation-evidence', File.join(directory, "#{slug}.#{receipt_id}.complete.json")]
    environment, command, arguments = host.send(:dev_session_invocation, entry, args, transition_lock: true)
    raise 'selected helper changed' unless command == File.join(predecessor, 'libexec/workspace-portal/dev-session')
    environment['DEV_SESSION_SLUG'] = slug
    environment['DEV_SESSION_WORKSPACE'] = root
    if ARGV == ['--inspect']
      puts JSON.generate('outcome' => 'prepared', 'selectedPackage' => predecessor,
        'receiptId' => receipt_id, 'slug' => slug, 'goalSha256' => journal['goal_sha256'],
        'teamDigest' => receipt.fetch('directTeam').fetch('teamDigest'),
        'methodSha256' => Digest::SHA256.hexdigest(new_method), 'ordinaryTransitionLock' => true)
    elsif ARGV.empty?
      accepted = system(File.join(predecessor, 'bin/workspace-portal'), 'thread', 'ensure-initial',
        '--thread-id', thread_id, '--cwd', File.join(root, 'work', slug), '--socket', runtime.fetch(:codex),
        '--input-file', goal.path)
      raise 'original initial request is not proven accepted' unless accepted
      exit DevSession::CLI.new(arguments, env: environment).run
    else
      raise 'use --inspect or no arguments'
    end
  end
end
end
