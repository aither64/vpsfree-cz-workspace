# Retained storage-profile rollout

## Status

Prepared execution record, updated 2026-10-03. Provider implementation,
independent review and direct corrections are complete. Default/compatible
checks, required host migration and the real retained-services fixture passed.
The latter proves services-only preservation and interrupted-copy/new-boot
behavior; its hold remains `starting_copied` and unreleased. Historical failures
and focused corrections remain recorded in [state](state.md).

The rebased consumer pin is published at `6d1b9c4d` on actual review base
`93389c33`; independent runtime/provider/consumer composition review completed
with no findings in all four HIGH-risk lanes. The six-stage quick batch, all
four root checks, new package realization and installed runtime/contract/helper/
Codex source-byte proof passed. No workspace
package activation, registered-cluster boot or populated-cluster provisioning
has occurred for this slice. The cluster remains stopped with retained disks.
The earlier reset authorization does not apply to the user-created VPS.

The [current brief](design.md) owns behavior and ordered acceptance;
[state](state.md) records implementation and verification. This record will
hold exact operator selections and outcomes as the authorized trial proceeds.

## Sources

| Component | Selection | Status |
| --- | --- | --- |
| API | `46b3bf6f9549eaf579053bc296ebf19c417bb848` | Reviewed, directly remediated, published; API CI 27/27 passed. |
| Generic runtime | `4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4` | Reviewed, published on `924c0ec2`; schema 1/policy 3. |
| Provider | `399c33023a568a8d7a21e4e4df52829628720a28` | Published on `8f8d8ecf`; rebased composition reviewed without findings. Original functional reviews/direct corrections retained. Host migration passed at `f36`, native fixture at `45d7ce88`; unchanged relevant bytes/inputs support carrying those observations forward. |
| Workspace consumer | `6d1b9c4d63d900dbe8fe5b8790c8f92b28ab0b25` | Published on `93389c33`; complete one-commit pin reviewed without findings or migrations. New package built and verified; unselected. |
| OS | `8d05dc3ae1fb71c1385609990acdf093af49ceec` | Previously reviewed/published provider source, unchanged. |
| React | `aa2f60b89df65d2f987be48784ed42bab7010833` | Unchanged selected path source; honest embedded provenance remains separate. |

Default-branch integration and production/shared deployment are not authorized.
The provider's default API/OS inputs stay unchanged; use the selected
same-session sources for the enabled checks and trial.

## Pre-boot evidence

- [x] Private cold recovery copy and exact resident config/toplevel evidence
  preserved at `/tmp/storage-profile-cold-recovery-20261002.9b7dxg0i`.
- [x] Selected resident init and systemd debug-generator bytes corroborated on
  the copy; selected override directory empty. This is not recursive closure
  or bootability proof. The copied filesystem needs journal recovery.
- [x] Final provider complete-series review; no obsolete history or migrations.
- [x] Important CatchUp loading correction and focused fresh-reader check.
- [x] Required host-migration VM, exact `f36f15d7`, exit 0 in 5m34s;
  private logs `/tmp/storage-profile-host-migration.r4JiK7`, cleanup complete.
- [x] Default-pin definition/app correction (`37057284522`), default/compatible
  checks, owning folds, affected review and direct root-lifetime fix.
- [x] Real retained-services fixture: masks, zero old-seed starts, allocation
  preservation, interrupted copy and exact new boot, at `45d7ce88`.
  Holds remain `starting_copied`; no full-cluster release is claimed.
- [x] Independent complete consumer review, all four HIGH-risk lanes, no findings.
- [x] Published consumer and built package with equal packaged host/tools contract.
- [ ] Supported workspace package activation from an external idle terminal.
- [ ] Immediate cluster ownership/address-availability recheck before boot.

The first explicit retained-services app attempt exited 1 after 7m30s at
`eee1998`, logs `/tmp/storage-profile-retained-services-watch.P9e3XA`. The
resident configuration built and was rooted; the enabled overlay failed when
`cp` tried to overwrite copied read-only fixture hooks. A bounded builder fix
and focused realization precede another native attempt. No guest, seed or
payload result was obtained, and the retained registered cluster is untouched.
The actual corrected overlay then passed focused realization and source
comparisons in 52s, evidence `/tmp/storage-profile-overlay-build.8cDI5F8c`.
The two copy-mode changes were folded into the profile owner, leaving the
fixture patch unchanged. Published clean `75fb840` is now under a fresh native
retry; no retained-data or release result has been obtained yet.
The retry exited 1 after 455s, logs `/tmp/storage-profile-retained-services-retry`.
Both configs built and stayed rooted. The native entrypoint then created its
log before its constructor's empty-directory check, so no guest started.
Initialization order is being corrected without weakening the artifact guard.
The actual no-guest startup check then passed in about 14s. Its verified
one-file fix was amended into the fixture owner as `78ffa6f`; original guards
and native scenario/results remain unchanged. A utility checked the wrong file
during preflight and ran zero checks; a fresh literal-path handoff now owns the
real retry at `/tmp/storage-profile-retained-services-78.W0DG89VX`.
That retry exited 1 after 680s. The first disposable guest booted, then the one
native example failed in stage 1 after 216.23s. Private shell evidence identifies
MariaDB ERROR 1064 at the fixture's unquoted `offset` column. A narrow quoting
correction and actual disposable database check precede the next attempt;
cleanup completed without touching the registered cluster. Maintenance masks,
allocation preservation, copy and exact new boot remain unproved.
The exact namespace UPDATE then passed PREPARE against the real API46 automatic
disposable schema in 38s, executing no update. Normal owning amend/publication
created `3175df0`, preserving the first three commits and changing only that
SQL line. The actual compatible native retry is now running at
`/tmp/storage-profile-retained-services-3175.6ka7ukno`; no physical result is
inferred from the parser check.
The retry exited 1 after 421s, sole example 218.63s at stage 2. The initial
guest, mutation/projections and stop completed; resident inventory validation
refused before masked boot because `vpsadmin-rabbitmq-setup.service` is absent
from the fixed masks. The hold remains `held`, with no bound runner/candidate.
Architect0 is resolving that bounded completeness correction. Parent confirmed
no owned QEMU/virtiofs process remains; retained artifact directories/pid files
are evidence. No maintenance-mask, copy, new-boot or live-cluster proof follows.
The approved correction adds only the RabbitMQ setup mask, retaining policy and
record version 1 and all unknown-writer/trigger refusals. Focused tests passed
2/21 and the current helper validated both exact sealed closures without a
guest. Normal owning fold/publication created `1743940`, preserving profile
and native fixture patches. A fresh actual native retry is running at
`/tmp/storage-profile-native-1743.i0ldpjza`; no old boot is grandfathered as new
mask evidence.

## Package activation boundary

Prepared, not executed. Required review, both VM gates, source publication,
generated pin and composed-package checks are complete. Reviewed source head:
`6d1b9c4d63d900dbe8fe5b8790c8f92b28ab0b25`. Built package:
`/nix/store/zmwh78dk1vjh2b91qnibjl682rb8hmwc-dev-workspace-0.2.0`.
Host/tools canonical contract bytes match schema 1/policy 3 and SHA256
`33acdc50fa6b7ed94f84d1f7f1db0af8d76d7d57d2e721cbb6a204a96b27c0d1`.
The package proof also checked reviewed host/session/provider helpers and
selected Codex `4c170393` source bytes. Evidence:
`/tmp/storage-profile-rebased-package.xnradz5x`, exit 0 in 245.623s, parity 1.
Public comparison capture records exact base `93389c33` and head `6d1b9c4d`.
Remote backup refs preserve exact pinned runtime/provider dependencies; their
names and readback results are recorded in [state](state.md). This does not
integrate any default branch.
Use the normal installed command from the external terminal:

```sh
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-23-storage-redesign/workspace
```

Run it from an external terminal while the lead and every ready member are idle,
with no pending requests or submissions. This is a profile-wide transition;
the operator must account for ready sessions in other registered workspaces
and the normal terminal/service rebind. The active lead must not invoke it as
an idle probe or arrange background activation. No activation is scheduled.
After the operator reports success, verify the public selected package/provider
before the maintenance trial. Preserve retained state on refusal and recover
forward through the same or a newer reviewed compatible public package.

Successful activation can support an early merge of this narrow workspace pin
without waiting for the storage redesign. That merge requires explicit approval
for workspace `master`, a current comparison and fast-forward integration.
Future repins must preserve the maintenance-aware provider together with policy
3 or newer. The session and remaining storage feature branches stay active.

## Maintenance and preservation

Pending. Use the reviewed typed maintenance/copy/copied-config path. Keep old
application writers masked from initial services boot. Once reachable, collect
a fresh private logical DB backup and baseline of existing VPS/catalog,
namespace/map, package/assignment and allocation rows. Bind the copy receipt to
the actual services closure and preserving marker; never use an unmasked old
seed as fallback. Record actual boot IDs, generations and release outcome here
without dumping private configuration or credentials.

## Useful storage acceptance

Pending. Provision configured backup/NAS roots through normal chains after
nodes are ready, then templates and repeat-safe catch-up. Preserve the existing
VPS files, quota, source retention and history; catch-up does not rotate.

Dedicated ordinary-member VPS and NAS fixtures must prove actual A/S1/full
then changed B/S2/incremental destination payloads, common base and tree/branch
identity. Observe an automatic cycle and exercise 3/5 rotation on fixtures
only. Repeat provisioning and a supported services update; verify stable
schedule counts and preserved original VPS/allocations. Leave the useful
profile active with PHP, React and API access.

## Retirement evidence

Host/AR semantics passed the focused checks; actual retained-boot retirement
and services replacement remain pending. Retirement keeps `enable:true,enrollment:false`
so later boots preserve assignments and do not recreate future defaults or
enrollment. Normal services replacement must establish the effective selection
in all relevant workers before cleanup. Loaded inspection must agree with the
desired boolean. Stop profile dispatch, let admitted work settle, and remove
only owned enrollment/configuration rows under ordinary locks; keep all
datasets, backups, packages and user assignments. Failure leaves scheduling
stopped and remaining rows available for retry. Re-enrollment is explicit true
selection followed by normal provision, not automatic boot cleanup.

## Limits

Storage1's logical copies share its existing disk; they are not independent
failure domains. Retention settings are rotation targets, not hard space caps.
Preserve both consumed API migrations and additive schema. Production strict,
identity publication, physical quiet, repair readiness and APPLY remain off.
