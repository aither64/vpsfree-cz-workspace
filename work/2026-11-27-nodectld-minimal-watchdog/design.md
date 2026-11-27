# Implementation and verification brief

Status: proposed implementation plan, not implemented or deployed.
Design owner: the current conversation lead; this tracking-only session has no
retained team roster. Scope and evidence are in [plan.md](plan.md) and
[state.md](state.md).

## Minimal mode

Use the existing mode policy in
`libnodectld/lib/nodectld/config.rb#AppConfig#load`. Add disabled values for
`export_mounts.enable` and `vps_os_release.enable` alongside the existing
minimal-mode settings. This keeps the meaning of minimal mode consistent at
initial load and normal reload. Do not use socket-existence detection: a missing
osctld on a standard node must remain visible as a fault.

The observed failure is in
`libnodectld/lib/nodectld/export_mounts.rb#update_all_worker`. Its constructor
already checks `enable?`, and its public update methods do likewise. The
VpsOsRelease singleton has the same configuration contract. Prefer correcting
the mode policy over adding scattered special cases or swallowing osctl errors.

Before editing, perform a bounded audit of `Daemon#init`, the minimal-mode
override and their periodic/refresh entry points. In particular, ensure that
the existing minimal gates for mount reporting, storage, VPS status, SSH keys,
accounting, dataset expansion and exporters remain sufficient. Any additional
change must address an actual osctld dependency inside the requested minimal-mode
contract; do not refactor unrelated node services.

Acceptance:

- A YAML configuration loaded in minimal mode disables both missed facilities,
  including after reload. Cover the existing precedence of mode overrides over
  configured enable flags; do not silently change that precedence.
- Constructing the disabled facilities starts no worker or AMQP channel, and
  their refresh/update calls invoke no osctl command.
- Standard mode still enables them by default; an explicitly disabled facility
  stays disabled there.
- A packaged mailer container with no `/run/osctl/osctld.sock` sends a queued
  message, survives the periodic boundary represented by the accelerated test,
  and remains able to send another message. Do not wait six real hours in CI.

Likely files: `libnodectld/lib/nodectld/config.rb`,
`libnodectld/spec/nodectld/config_spec.rb`,
`libnodectld/spec/nodectld/export_mounts_spec.rb`, and focused VpsOsRelease or
daemon-start coverage if needed to prove these behaviors.

## Restore the existing watchdog under systemd

The current unit in `nixos/modules/vpsadmin/nodectld/nixos.nix` bypasses the
wrapper with `--no-wrapper`. The wrapper and watchdog already exist in
`nodectld/lib/nodectld/cli.rb`; the monotonic stale-check policy is in
`libnodectld/lib/nodectld/transaction_watchdog.rb`.

The proposed unit runs the wrapper with its default enabled watchdog. Keep the
wrapper as the service's main process and the daemon as its child. Retain the
existing stdout/journal logging route and verify both wrapper diagnostics and
child output reach the journal/central logs.

Use these service semantics:

- `Restart=always`, retaining the current restart delay and start-rate limits.
  This covers a successful wrapper exit after watchdog recovery. An explicit
  `systemctl stop` suppresses automatic restart according to systemd semantics.
- `KillMode=mixed`: on normal unit shutdown, send TERM to the wrapper first;
  let its existing stop path terminate the child and escalate after 60 seconds.
  Keep whole-cgroup KILL as systemd's final cleanup, including orphaned children.
- Set an explicit `TimeoutStopSec` of 90 seconds, leaving margin beyond the
  existing 60-second child escalation. Verify the deadline in the generated
  unit and with a hung child. If measured wrapper cleanup cannot fit, adjust
  the service deadline with evidence rather than removing the bound.

Prefer this small service integration to a second watchdog implementation or a
new wrapper protocol. Preserve the 600/810/900-second warning/debug/restart
thresholds, bounded control-socket request and monotonic clock. Treat wrapper
changes as necessary only if focused tests demonstrate an integration defect.
If that changes the proposed semantics, update this brief before expanding work.

Acceptance:

- A daemon that still answers status but stops advancing transaction checks
  triggers the existing stale warning, transaction-loop backtrace and recovery.
- The old child is reaped and exactly one fresh daemon starts; queued work
  resumes. A successful watchdog exit cannot leave the service inactive.
- An unresponsive control socket does not hang the watchdog itself. A child
  that ignores TERM is killed after the bounded escalation period.
- Manual systemd stop stays stopped, restart produces one replacement, ordinary
  crash recovery works, and no orphaned child/control-socket owner survives.
- Check `nodectl restart`, `stop` and `update` against their existing NixOS and
  runit lifecycle contracts; document the normal systemd stop interface rather
  than assuming a control-socket exit request is the service manager's stop.
- vpsAdminOS continues using its existing runit wrapper invocation. No changes
  to node watchdog timing, service ownership or host-only functionality are
  introduced by the NixOS fix.

## Verification batches

### Quick checks before independent final review

Use `nix develop .#libnodectld` and the repository's normal Bundler environment.
Run relevant existing and extended specs:

- `spec/nodectld/config_spec.rb`
- `spec/nodectld/export_mounts_spec.rb`
- any added minimal-mode/VpsOsRelease behavior specs
- `spec/nodectld/transaction_watchdog_spec.rb`
- `spec/nodectld/cli_watchdog_spec.rb`
- `spec/nodectld/remote_commands/watchdog_status_spec.rb`
- `spec/nodectld/remote_commands/watchdog_debug_spec.rb`

Add coverage for actual recovery/exit semantics: the current CLI watchdog specs
cover socket reads/deadlines, not full wrapper restart behavior. Use a small
disposable process fixture where a process boundary is required; do not replace
the packaged systemd acceptance test with mocks.

Run the repository's declared RuboCop/Nixfmt/hooks for changed components. If
packaged Ruby metadata needs refreshing, use the documented scoped
`rake vpsadmin:gems` tasks without build IDs or first-party gem publication.
Evaluate the NixOS unit's command, restart policy, kill mode and timeout, and
compare the runit unit. Confirm selectors include new test/runtime paths with
`ruby tests/ci-selection-test.rb` and relevant `./test-runner.sh ls` filters.

Expected batch: minutes, excluding initial environment provisioning. Stop on a
first shared setup failure, diagnose it once, and rerun only affected checks.

### Real-service integration after final review

Reuse `tests/configs/nixos/vpsadmin-services.nix`, which already defines a
minimal-mode mailer container and optional Mailpit capture. Add a focused
RSpec-style scenario, tentatively
`tests/suite/admin/nodectld-minimal-watchdog.nix`, and register/select it through
the existing `tests/all-tests.nix` and CI selection/tag mechanisms.

Exercise normal mail delivery without osctld, periodic minimal-mode behavior,
stale polling with a responsive control socket, an unresponsive child, explicit
stop/restart and delivery after recovery. Use a fixture-only fault injection
and clock/threshold acceleration. Do not add production environment variables or
public timeout knobs solely to shorten the test. The responsive-socket case must
block transaction progress specifically; merely stopping the entire child does
not prove that branch. A separate stopped/unresponsive-child case covers the
hard recovery path.

Use the existing Mailpit helpers to prove the SMTP result and transaction-chain
completion. Inject the polling fault between messages rather than asserting
exactly-once recovery across a send/database-confirmation race. Preserve the
normal transaction queue and retry semantics.

Run the focused new scenario plus the relevant existing node-control and mail
smoke coverage, using actual names from `./test-runner.sh ls`:
`admin/nodectl-read-and-queue-control`,
`admin/nodectl-refresh-and-runtime-state`, and
`alerts/lifetime-and-daily-report` are candidate source selectors. Avoid blindly
running the full integration suite. Expected runtime is tens of minutes once
inputs are available; record the actual selected batch and stopping condition.
Use the monitor skill for long/uncertain checks and stop any unexpected local
kernel build under the workspace verification procedure.

## Compatibility, rollout and recovery

No schema, persisted-data, API, RPC payload or transaction-signature changes are
required. Existing standard-mode nodes retain their defaults. Minimal-mode
consumers deliberately stop requesting host-container information. Existing
mailer/DNS installations gain the watchdog when they take the new NixOS module;
changing only the daemon package while retaining an old generated unit is not
sufficient.

Before a separately authorized deployment, prepare the configuration channel pin
to the reviewed source, evaluate the target, build/dry-activate the exact
candidate, and inspect its service restart impact. Retain the deployed
generation and matching rollback build. Canary vpsadmin1: confirm wrapper plus
one child, watchdog-enabled invocation, normal transaction progression and no
osctld requests. Use existing/authorized mail work for production verification;
fault injection belongs in disposable tests. Observe normal operation across the
old six-hour failure boundary as an operational follow-up, not a six-hour CI test.

Rollback restores the recorded old generation. Persisted work remains readable,
but the old reliability defects return. Do not repair queues manually, claim
exactly-once delivery, or infer that this remediation explains the original
native hang. Capture `watchdog_debug` and relevant connection diagnostics on any
recurrence; deeper mysql2 investigation is a separate evidence-driven task.
