# Cluster controls verification

Final sources and branch series: [final-heads.md](final-heads.md).
Independent review: [review.md](review.md); narrow remediation is recorded in
the final-head inventory and state.

## Completed checks

- Focused Go cluster and HTTP/template tests, Ruby provider status and retained
  Start tests, JavaScript syntax and shell syntax passed. The corrected shared
  fixture environment is documented in the reusable setup note.
- The obsolete footer rendering assertion found by review was corrected;
  affected rendering/control tests passed on the final runtime commit.
- The final composed workspace/configuration deployment contract passed with
  runtime bc6b841 and extension 7157c80. Sibling inputs were preserved.
- Chromium and Firefox exercised the actual portal template and assets at
  1280px and 375px. Reveal keyboard behavior, Copy alignment and secret-safe
  feedback, clipboard failure, pending controls, Start failure/retry,
  preservation of the selected service tab, legacy Release-only providers,
  and Release cancellation/confirmation passed (14.86 seconds).
- [Runtime CI Check 38171425609](https://github.com/aither64/dev-workspace/actions/runs/38171425609)
  passed on bc6b841. The earlier failure was the confirmed obsolete rendering
  assertion, corrected before this new-head run.
- [Extension CI Check 38170807346](https://github.com/vpsfreecz/dev-workspace/actions/runs/38170807346)
  passed on 7157c80, including the packaged devcluster-check.

The fresh Luna/low long_checks watcher completed the entire local batch with
status 0 in about 1h 7m. Generic and extension flake checks, composed provider
smoke, and the final workspace flake check all passed. The generic check
includes host-module and session-recovery VM tests; the reboot fixture's portal
shutdown timeout was recovered and did not fail the test. No unexpected kernel
build or cancellation occurred. Full logs and exact exit status are retained
locally as long-checks.log and long-checks.status.

## Deployment and live VM

Host build, dry activation, host switch and application-profile switch passed.
Authenticated HTTPS returned HTTP 200/TLS 0; live app.js and style.css exactly
match the reviewed source. Portal/router services are active. See
[rollout.md](rollout.md) for generations and the transient-group check correction.

The owned disposable bridge VM's known-file Stop/Start/Release check passed
(status 0, phase complete, about 10 minutes), monitored by the fresh Luna/low
live_cluster_services utility. A file at /tank/cluster-controls-check containing
cluster-controls-disk-retention survived portal Stop and normal portal Start.
Both phases retained single topology and bridge network. After Stop the
provider advertised Start/Release; after Start it reported running/ready with
Stop/Release. Portal Release succeeded and removed the owned state directory.
The primary checked the log and directory absence; portal/router remain active.

Earlier verification attempts were diagnosed before correction. The first
reached initial readiness but
failed because the verification script omitted the documented -- separator
before the remote SSH command. That evidence is retained as
live-cluster-ssh-failure.*; the corrected check reuses the stopped cluster's
disks/configuration through normal retained Start. No source changes or reset.
The next attempt connected before guest network/SSH startup and failed with
No route to host. OSVM control-shell readiness precedes those services; console
evidence established that ordering. Logs are preserved as
live-cluster-network-wait.*. The corrected check probes SSH/tank readiness
before each file operation; it does not retry Start requests.
The final probes showed those transient startup errors resolve once services
are ready. No unexpected local kernel build or cancellation occurred. The same
retained disks were used until the final Release. No implementation or
verification work remains.
