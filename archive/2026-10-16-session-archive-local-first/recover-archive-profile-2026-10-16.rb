# frozen_string_literal: true

# Source-only forward recovery of one approved attempt. Never releases ownership,
# changes a candidate, rewinds a phase, or replaces an activation/result receipt.
require '/nix/store/52w0v2bcl77igbnx53wx9062k9d0dy1w-dev-workspace-0.2.0/libexec/workspace-coordination'

module ArchiveProfileRecovery
  WORKSPACE = '/home/aither/workspace/ai/vpsfree.cz'
  SLUG = '2026-10-16-session-archive-local-first'
  STATE = '/home/aither/.local/state/dev-workspaces'
  PROFILE = "#{STATE}/profile"
  PACKAGE = '/nix/store/52w0v2bcl77igbnx53wx9062k9d0dy1w-dev-workspace-0.2.0'
  CANDIDATE = '/nix/store/hnip6n4palmf2lv5fkj84yp0wzfq4fjr-dev-workspace-0.2.0'
  SYSTEM = '/nix/store/fs7vyv2pgc878wbjskk9b4v86hp7n9ak-nixos-system-aitherdev-26.05.20261015.26f4107'
  OWNER = '99e4bed1-b56a-4b71-b15d-2ba2e49bcacb'
  THREAD = '01a145d0-7a59-7a03-af9f-a66366f5875f'
  RESERVATION = '5f379baf-3837-4ec3-a2ce-4900fbd8d45e'
  JOB = '457cea56-19de-4933-a846-c84b7e1b0ca8'
  SYSTEM_JOB = 'fc35728c-007d-4419-91b8-ab0cce78a837'
  ATTEMPT = '43beb3e1-bd94-4d4e-80b5-38b1cea1a7a2'
  APPROVAL = '597def4d-f62f-4c26-a3d2-20482a1ffba5'
  SNAPSHOT = 'sha256:82a8e0024f2fdb9ca67a1498436a9e02aac92df53a6daa5df076b905d47e76d7'
  ARTIFACT = 'sha256:cf6e98943bdc6f722a74c0a05ade9e2f7700b1f5cfac3523c43bd33ac5b47271'
  REQUEST = 'sha256:1bef7c0bff463a6323b3b5b5e79bf5a82260fdb22f14f69ec02247f0997b374b'
  TOKEN = '6753c554806fe7cd29a91f6bb6836d0e33c91b5b6859713cc159c42b05439a64'
  ERROR = "workspace-host failed: error: workspace package transition is blocked by unfinished session operations: vpsfree-cz/2026-10-16-idle-coordination-worker (creation); retry the matching dev-session command first\n"
  RECORD = "#{WORKSPACE}/work/#{SLUG}/profile-forward-recovery-journal.json"
  LOG = "#{WORKSPACE}/work/#{SLUG}/profile-forward-activation.log"

  def self.check(condition, message)
    raise message unless condition
  end

  def self.private_json(path)
    WorkspaceCoordination.private_read(path, limit: WorkspaceCoordination::MAX_REQUEST)
  end

  def self.validate(data)
    owner = data.fetch('owners').fetch(OWNER)
    check(owner.values_at('slug', 'workspace', 'thread', 'fence') == [SLUG, WORKSPACE, THREAD, nil], 'owner identity changed')
    job = data.fetch('jobs').fetch(JOB)
    check(job.values_at('ownerId', 'reservationId', 'kind', 'attempt', 'approvalId') ==
          [OWNER, RESERVATION, 'profile_activate', ATTEMPT, APPROVAL], 'attempt identity changed')
    check(job['state'] == 'reconciling', 'original attempt is no longer reconciling')
    check(job.dig('snapshot', 'id') == SNAPSHOT && job.dig('snapshot', 'operation', 'preparedArtifact') == ARTIFACT &&
          job.dig('snapshot', 'operation', 'candidatePackage') == CANDIDATE, 'approved snapshot changed')
    check(job['dependsOn'] == [SYSTEM_JOB] && data['jobs'][SYSTEM_JOB]['state'] == 'succeeded', 'system dependency changed')
    check(data['jobs'][SYSTEM_JOB].dig('result', 'observed', 'runningSystem') == SYSTEM, 'system receipt changed')
    check(job.dig('result', 'outcome') == 'unknown' && job.dig('result', 'requestDigest') == REQUEST &&
          job.dig('result', 'error') == ERROR, 'failure is not the exact preselection admission refusal')
    approval = data.fetch('approvals').fetch(APPROVAL)
    check(approval['ownerId'] == OWNER && approval['kind'] == 'deploy' && approval['reviewedSnapshot'] == SNAPSHOT &&
          approval['scope'].any? { |s| s['machine'] == 'vpsfree:aitherdev' && s['reboot'] == false && s['actions'].include?('profile_activate') },
          'deployment approval changed')
    reservation = data.fetch('reservations').fetch(RESERVATION)
    check(reservation['ownerId'] == OWNER && reservation['machine'] == 'vpsfree:aitherdev' &&
          %w[blocked_recovery held].include?(reservation['state']), 'reservation identity/state changed')
    unknown = reservation['history'].select { |h| h['outcome'] == 'unknown' }
    check(unknown.length == 1 && unknown[0]['attempt'] == ATTEMPT && unknown[0]['artifact'] == ARTIFACT,
          'another uncertain deployment exists')
    check(File.realpath('/run/current-system') == SYSTEM && File.realpath('/nix/var/nix/profiles/system') == SYSTEM,
          'live system changed')
    selected = File.realpath(PROFILE)
    check((selected == PACKAGE && DevWorkspaceProfileIdentity.token(PROFILE) == TOKEN) || selected == CANDIDATE,
          'profile no longer has the exact predecessor or forward candidate')
    artifact = private_json("#{STATE}/coordination/sources/#{ARTIFACT.delete_prefix('sha256:')}/artifact.json")
    check(artifact['id'] == ARTIFACT && WorkspaceCoordination.digest(artifact.reject { |k, _| k == 'id' }) == ARTIFACT &&
          artifact['candidatePackage'] == CANDIDATE && artifact['profileToken'] == TOKEN, 'prepared artifact changed')
    directory = "#{STATE}/coordination/attempts/#{ATTEMPT}"
    request = private_json("#{directory}/request.json")
    phase = private_json("#{directory}/phase.json")
    check(request['digest'] == REQUEST && WorkspaceCoordination.digest(request.reject { |k, _| k == 'digest' }) == REQUEST &&
          request.dig('job', 'id') == JOB && request.dig('job', 'snapshot', 'id') == SNAPSHOT,
          'original worker request changed')
    check(phase.values_at('attemptId', 'requestDigest', 'phase') == [ATTEMPT, REQUEST, 'profile_intent'], 'attempt phase changed')
    reservation
  end

  def self.record(stage)
    WorkspaceCoordination.atomic(RECORD, {'schema' => 1, 'ownerId' => OWNER, 'reservationId' => RESERVATION,
      'jobId' => JOB, 'attemptId' => ATTEMPT, 'snapshot' => SNAPSHOT, 'artifact' => ARTIFACT,
      'candidate' => CANDIDATE, 'stage' => stage, 'updatedAt' => Time.now.utc.iso8601})
  end

  def self.activation_with_lock(lock, log, command)
    interrupted = false
    handlers = %w[INT TERM].to_h { |signal| [signal, Signal.trap(signal) { interrupted = true }] }
    # The child retains the same open-file-description lock across both exec
    # wrappers. Even SIGKILL of this helper cannot admit another executor while
    # activate-prepared is still completing its owned activation work.
    pid = Process.spawn({'DEV_SESSION_SLUG' => SLUG, 'DEV_SESSION_WORKSPACE' => WORKSPACE},
      *command, chdir: WORKSPACE, out: log, err: log, lock.fileno => lock)
    begin
      _, status = Process.wait2(pid)
    rescue Errno::EINTR
      retry
    end
    warn 'Cancellation deferred until the admitted activation completed.' if interrupted
    status
  ensure
    handlers&.each { |signal, handler| Signal.trap(signal, handler) }
  end

  def self.run(execute)
    store = WorkspaceCoordination::Store.new(STATE)
    directory = "#{STATE}/coordination/attempts/#{ATTEMPT}"
    File.open("#{directory}/worker.lock", File::RDWR) do |lock|
      check(lock.flock(File::LOCK_EX | File::LOCK_NB), 'original worker/reconciler is running; retry later')
      validate(store.read)
      puts 'Exact owner, claim, approval, failure, predecessor, candidate and live system verified.'
      return unless execute

      record('verified')
      store.transaction do |data|
        reservation = validate(data)
        if reservation['state'] == 'blocked_recovery'
          # Keep the same machine owner and execution claim. The installed
          # activation guard otherwise rejects even this exact forward recovery.
          reservation['state'] = 'held'
          reservation['revision'] += 1
        end
      end
      record('forward_activation')
      begin
        File.open(LOG, File::WRONLY | File::CREAT | File::APPEND, 0o600) do |log|
          status = activation_with_lock(lock, log,
            ["#{PACKAGE}/bin/workspace-host", 'activate-prepared', '--artifact', ARTIFACT, '--attempt', ATTEMPT])
          check(status.success?, "original activation failed (#{status.exitstatus}); retain recovery and inspect #{LOG}")
        end
        check(File.realpath(PROFILE) == CANDIDATE, 'activation returned without selecting the approved candidate')
        record('activation_completed')
      rescue StandardError
        store.transaction do |data|
          reservation = data.fetch('reservations').fetch(RESERVATION)
          check(reservation['ownerId'] == OWNER, 'reservation owner changed during recovery')
          if reservation['state'] == 'held'
            reservation['state'] = 'blocked_recovery'
            reservation['revision'] += 1
          end
        end
        record('activation_failed')
        raise
      end
    end
    # Release the worker lock before normal reconciliation. The selected exact
    # candidate now supplies the proof the ordinary reconciler requires.
    check(system({'DEV_SESSION_SLUG' => SLUG, 'DEV_SESSION_WORKSPACE' => WORKSPACE},
      '/home/aither/bin/dev-session', 'coordination', 'reconcile', SLUG, JOB, '--as-is', '--json', chdir: WORKSPACE),
      'activation completed; ordinary reconciliation remains pending')
    record('reconciled')
  end
end

if $PROGRAM_NAME == __FILE__
  abort 'usage: ruby recover-archive-profile-2026-10-16.rb [--check | --execute]' unless ARGV.empty? || [%w[--check], %w[--execute]].include?(ARGV)
  ArchiveProfileRecovery.run(ARGV == ['--execute'])
end
