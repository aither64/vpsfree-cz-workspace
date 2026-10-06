# Verified Codex and portal rollout

Both deployments and acceptance checks passed on 2026-10-02. The user later
authorized integration; all four final source heads are now merged and pushed.
See [integration.md](integration.md). The session remains open and runtime is
unchanged by the later reference-only commit.

## Deployed source snapshot and selected generations

- Generic dev-workspace: 40838aa28c8433e42a4a3fbed4586a3df0146de9.
- Site extension: c56f981a950ab763b71dc91c59e8b5256d478851.
- Configuration: 028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d.
- Full consuming workspace: c5d8bed5fcd3bc01ce18831ea680aac7edfd68ee.

These four deployed heads are committed, pushed and independently whole-branch
reviewed. Generic4bec201 subsequently adds only upstream/removal comments and
documentation, with its own completed review; consumers retain generic408
because there is no runtime/pin change. All source worktrees are clean. Their complete
series and no-migrations inventory are in [final-review.md](final-review.md);
finding reconciliation is in [final-review-result.md](final-review-result.md).

Aitherdev uses system generation156, built confctl generation
2026-10-02--14-04-08, with output
`/nix/store/zg389q4q7hcxxl7agg0y5nxdb3xpcz4h-nixos-system-aitherdev-26.05.20261001.4feb8eb`.
System codex and the Home Manager codex-ds wrapper use assembled package
`/nix/store/53p8l7hck9kca8jcyy6fcpw5iysdfmj6-codex-package-0.160.0`.
System switch passed at 12:25:30 UTC, including both confctl health checks.
Dry activation identified only dbus-broker reload and home-manager/nginx
restarts; the kernel is unchanged and no reboot occurred.

The separately deployed user-profile generation79 selects the full consuming
package `/nix/store/9g8wd2fppjgq1bvcwkscsbp5r1wb9yk9-dev-workspace-0.2.0` and
bundled Codex `/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0`.
The first switch selected this generation but its older initiating helper
miscompared registration against its old bundled Codex. Supported same-source
forward retry through the now-selected dispatcher passed at 12:32:46 UTC.
No manual relink, marker edit, rollback, forced interruption or state restore
was used. Detailed failed/successful evidence is retained in [state.md](state.md).

## Acceptance

- Quick evaluation/syntax/focused tests and declared configuration hooks passed.
- Provider CI 36999356818 and extension CI 36999495059 passed on the exact heads.
- Full consuming package, flake checks and review-UI assets passed.
- Browser checks passed at 981, 1024, 1100, 1200, 1280, 1440 and 390px. Desktop
  controls fit one row at 1280/1440; mobile wrapping, Apply/Cancel, drafts/reload,
  saving/error display and containment/non-overlap remain covered.
- Generated 0.160.0 protocol validation passed. Disposable old159/new160/old159
  readers preserved settings, explicit fork settings and an unloaded queued
  thread; six private SQLite integrity checks and no-task-start assertions passed.
- Both consumer packages passed isolated plain startup, resume/fork screens,
  daemon copying/restart/version/stop checks. Native updater copies retain store
  dependencies; they are not independent GC roots.
- Live ordinary system CLI startup passed without --no-daemon or a model prompt.
  Native daemon CLI, managed package and actual server all reported 0.160.0.
  codex-ds strict-config help passed without a paid model request.
- Workspace Codex, portal and router units are active. Actual Codex executable
  is the selected native160 binary; portal executable is selected9g. No pending
  Codex reconciliation remains.
- Authenticated stable HTTPS URL returned 200 with local-CA verification 0.
  Live app.js and style.css exactly match reviewed source, and the removed
  unsaved-settings notice is absent. The initial generic-CA curl failure was a
  probe setup error; certificates and authentication were not changed.

Final CLI/service evidence is verification-live-2.log (its final generic-CA
curl exits 60); the independent corrected HTTPS/asset gate is
verification-portal-1.log/status 0. State/daemon gates are
verification-runtime-5.log/status 0 and verification-daemon-1.log/status 0.
Logs are local transient evidence, not portal artifacts.

## State and recovery

Before candidate access to live state, seven SQLite stores received verified
online per-database backups, completed 12:15:29 UTC, outside Git/portal. This is
not a globally frozen snapshot or a lossless rewind. Private transcripts and
database contents were not published. Synthetic failure history, including one
unauthenticated HTTP 401 from an earlier incorrect loaded-queue fixture, remains
documented in state.md. Verification made no paid model requests and did not
restore real state.

Old system generation155, workspace profile78 and Codex root78 remain retained,
as do the new generation roots. Workspace recovery stays forward-only through
the supported switch entry points. Do not restore SQLite backups over writers
or prune closures still needed by copied native daemon packages. The native
daemon updater remains independent of the Nix pin.

Integration was separately approved and completed; no operator action remains.
Deployment/integration does not authorize archival or stopping the session.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-codex-package-portal-settings/
