# Restore minimal-mode isolation and nodectld watchdog supervision

## Goal and authorized scope

Implement fixes for the two defects exposed by the November 27
vpsadmin1 mail outage: minimal-mode nodectld starts functionality requiring
osctld, and its NixOS service bypasses the existing transaction watchdog.

The user initially requested a read-only investigation without tracking, then
authorized this plan and tracking. The follow-up "yeah implement it" authorizes
implementation and explicitly requires the watchdog for DNS servers and all
other NixOS/systemd nodectld setups. Production deployment has not been requested. The user later authorized master
integration conditional on a passing specs workflow; that condition was met.

## Affected repositories

- **vpsadmin**: minimal-mode configuration, existing wrapper/watchdog integration
  with the NixOS service, focused regression coverage and operator documentation.
  Planning baseline: `99207a8dcd92f5907c52dbc99af52b30aa7ecac1` (`origin/master`).
- **vpsfree-cz-configuration**: eventual channel pin and deployment to
  `cz.vpsfree/vpsadmin/int.vpsadmin1`, following separate deployment direction.
  Planning baseline: `2f264616638f4baa464692c02bea9ea76d7ffdde` (`origin/master`).
- vpsAdminOS/runit is a compatibility consumer to verify, not a planned source
  change. No API, schema, client, mail-template or WebUI change is intended.

## Findings that determine the plan

1. `AppConfig#load` applies a minimal-mode override that disables many node
   facilities but omits `export_mounts` and `vps_os_release`. Both default to
   enabled. `Daemon#init` initializes their singletons unconditionally; they
   depend on their own enable checks.
2. The export-mount worker wakes every six hours and calls `osctl` even for an
   empty VPS list. Logs show repeated crashes on this mailer container, which
   correctly has no osctld. Installing osctld is not a remedy.
3. The NixOS module runs `nodectld --no-wrapper`. The watchdog is launched by
   `run_wrapper`, so systemd currently supervises only process existence.
4. The existing watchdog detects stale transaction polling independently of
   the status thread. It warns after 600 seconds, requests a backtrace after
   810 seconds, and requests recovery after 900 seconds. Its stop path sends
   TERM and escalates to KILL after 60 seconds.
5. A watchdog recovery sets the wrapper's stop flag and can exit successfully.
   The current systemd `Restart=on-failure` would not reliably restart this
   path even if `--no-wrapper` were removed.
6. The actual blocked call during this outage remains unknown. An idle mail
   queue, continuing status updates and failure to terminate support a stalled
   transaction loop; no pre-kill thread dump was captured. The plan fixes the
   demonstrated isolation and recovery defects without claiming to fix an
   unproven mysql2 cause.

See [state.md](state.md) for the incident timeline and
[design.md](design.md) for the implementation and verification brief.

## Implementation sequence

| Package | Proposed work | Acceptance |
| --- | --- | --- |
| A: minimal-mode configuration | Disable `export_mounts` and `vps_os_release` in the existing minimal-mode override; inspect neighboring startup and refresh paths for the same missing gate. Add focused configuration and disabled-service regression specs. | Mailer/DNS minimal mode needs no osctld at startup, on periodic activity, or on relevant refresh requests. Standard nodes retain these features. |
| B: systemd supervision | Run the existing wrapper with its watchdog enabled. Use `Restart=always` for wrapper exit recovery, `KillMode=mixed` so TERM reaches the supervising wrapper first, and an explicit stop deadline longer than the wrapper's 60-second escalation. Validate control commands and signal handling. | A stale transaction loop with a responsive status socket is diagnosed and replaced; an unresponsive child is killed within a bounded time; explicit systemd stop stays stopped. |
| C: integration and documentation | Extend the existing services/mailer fixture and Mailpit support with focused minimal-mode and watchdog scenarios. Update test discovery/selection as needed. Document service ownership, diagnostics, recovery and minimal-mode behavior. | Real packaged NixOS service recovers and resumes queued mail without osctld; node/runit smoke coverage passes; documentation matches tested behavior. |

Use one implementer for this small, related change set. Packages A and B can be
separate logical commits, followed by any shared integration coverage and docs.
The current conversation lead owns implementation in this tracking-only session,
which has no retained Codex team. A standalone independent reviewer and fresh
verification utilities use the installed catalog settings; no team was created.

Runtime verification also exposed a pre-existing typo in `nodectl stop` option
parsing. A separate one-line fix restores the existing command, including its
force flags and help output. Its shutdown semantics are unchanged.

## Compatibility and deployment

Preserve existing configuration keys, standard-mode defaults, transaction
formats, database state, watchdog timing and vpsAdminOS/runit behavior. Keep the
process watchdog outside the daemon so a blocked daemon cannot disable it.
The review correction adds a main-thread progress timestamp for deliberate
polling skips (pause, full queues and draining), preserving actual poll timestamps
and compatibility with older watchdog responses. See the design addendum.
Use normal systemd stop/restart semantics and retain a service-level final kill
deadline. Do not clear queues, change transaction completion flags or add an
osctld service to minimal-mode machines.

After implementation, committed quick checks and independent final review,
run the integration batch described in the design. Publish the feature branch;
integration into either repository's master requires explicit user direction.
An eventual configuration pin uses the owning confctl channel, with one final
logical pin update. Prepare and inspect the exact candidate and rollback
generation before any separately authorized deployment. Canary vpsadmin1 first,
then assess other NixOS minimal-mode services; do not combine this with a fleet
upgrade. Standard vpsAdminOS nodes do not require a coordinated rollout.

Rollback restores the previous package and service unit without a data migration,
but also restores the known watchdog and minimal-mode defects. A forced restart
can retry work whose external effect preceded its database confirmation; this
plan does not add an exactly-once mail-delivery guarantee.

## Documentation

Keep the outage timeline, revisions and rollout evidence here. During
implementation, add a concise owning-project operations page for nodectld and
link it from `docs/README.md`; link relevant transaction behavior from
`docs/transactions.md`. Explain minimal mode, wrapper/systemd responsibilities,
watchdog thresholds, obtaining the existing `watchdog_debug` response, and
bounded shutdown/restart. Configuration deployment receipts remain in this
session, not in configuration-repository documentation.

## Verification and delivery checkpoints

1. Create the initiative vpsadmin worktree from freshly fetched master; read its
   current instructions and install its declared hooks in the documented Nix
   environment. Recheck the source assumptions in this brief.
2. Add behavior-focused regression specs and run the focused libnodectld batch,
   required lint/hooks, Nix service evaluation and CI-selector checks.
3. Commit all intended implementation, tests and docs. Consolidate the complete
   branch history and provide its base/head, final diff and no-migrations
   conclusion to independent final review under `mandatory-change-review`.
   Routine plan preparation itself requires no automatic review.
4. Run the focused real-service integration batch after review, using the monitor
   skill for long or uncertain checks. Preserve production watchdog thresholds;
   accelerate only disposable test fixtures.
5. Publish and inspect applicable CI. Report implementation, review, integration
   results and deployment status separately. Seek integration/deployment direction
   only after the corresponding concrete result is reviewable.

## Next action

All four local integration scenarios, broader GitHub CI and the exact-final-head
specs workflow passed. The user-approved fast-forward into vpsadmin/master is
complete. Normal post-merge workflows run on the same commit. Production
deployment remains a separately authorized step.
