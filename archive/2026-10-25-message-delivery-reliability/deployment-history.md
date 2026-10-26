---
lifecycle: active
---

# Message delivery reliability

Current phase: deployed, original message block recovered; final selected-package lifecycle verification. Implementation is
committed and published. The original receipt is untouched. No live migration,
profile switch, system activation or machine claim has occurred. Default-branch
integration is not authorized.

- [x] Reproduce the cancellation/write-boundary race and implement the delivery fix.
- [x] Implement SQLite receipts, migration recovery and browser retry behavior.
- [x] Complete original independent reviews and prescribed narrow fixes.
- [x] Preserve the newer deployed archive-policy-3 baseline.
- [x] Correct accepted creation source admission; focused checks pass.
- [x] Finish affected independent review; no findings remain.
- [x] Finish final candidate/CI checks.
- [x] Acquire aitherdev through the normal coordinator; own claim is held.
- [x] Activate and verify portal health, naming, native continuity and delivery.
- [x] Revalidate and retire the exact original stale attempt without resending it.
- [ ] Integrate only after explicit repository/target direction; release deployed
  machine ownership only under the installed retention policy.

## Diagnosis and implemented behavior

The reported lock is the WebSocket writer mutex. The deterministic regression
reproduces deadline expiry while persisting a submitting receipt, followed by
writer acquisition failure before transmission. Historical stage duration was
not measured. Claim-aware restoration now distinguishes proven unwritten sends
from true post-write uncertainty; uncertain sends are never blindly replayed.
The 15.2 MiB JSON ledger amplified admission cost; indexed SQLite WAL/FULL
transactions replace full-file rewrites. Browser retries retain the original UUID,
text, options and attachments and stop on uncertainty. Admitted plan sends
survive browser disconnects. Durable backups, predecessor fences and an orphan
backup guard preserve migration recovery. Upgrade is forward-only after SQLite
state exists; compatible packages must advertise submission schema/policy 1.

Two creation CI failures exposed a pre-existing nonblocking source EX admission
path. The exact historical holder is unknown; real controlled Go/Ruby tests prove
refusal against an identified SH reader. Browser queue reconciliation is a shared
reader on the same lock. Accepted source-bound fork workers now wait at both source
stages without destination locks, recheck source identity/lifecycle and retain
the existing four-minute worker deadline and process-group cancellation. Ordinary
CLI fork admission remains nonblocking. No new persisted schema or API change.

## Ownership and exact heads

The user enabled tracking after initially requesting none. A manually bound
external chat was rejected because its CWD was the workspace root; it was never
used for deployment. Supported initialization now provides managed coordination
thread 01a172c4-ca9f-7c70-b3e5-b1290a0568eb under this tracking directory. Portal
lookup works. Live roster is null; lead owns design/implementation, with an
independent retained standalone reviewer. External investigation thread remains
01a17206-ed6f-78b3-b410-c7d6015b6777.

All feature worktrees are under worktrees/2026-10-25-message-delivery-reliability/
on the identically named branch. Shared workspace stays on master with unrelated
changes preserved. Final published candidates:

| Repository | Head |
| --- | --- |
| codex-web | 8b60554bc10c2a6bcbf9732a8b77ad959c317036 |
| dev-workspace | 9634151b9836311c331a58880fbb4c46133fd98f |
| vpsfree-cz-configuration | 45683e38d3dc8e3ced20eae553f879e46ec84348 |
| workspace | 72e15700b241d75bcbc1eb8abf04542f70d9792f |

Exact selected predecessor runtime source is ec53874b6eea73bf65099cf19aa1a4bc5a3336aa,
verified by Git blob identity against its immutable source. Candidate runtime
rebased cleanly onto it and retains archiveRecoveryPolicy 3. Configuration retains
deployed baseline documentation, with one consolidated runtime pin. Workspace
preserves deployed storage/tracking changes through exact cherry-picks, replacing
the superseded baseline pin with one final update. Other initiative refs, live
files and claims were not modified. See baseline-review-packet.md and complete
Git history for inherited changes and consolidation. Native Codex remains 0.163.0;
extension and siblings are unchanged.

## Verification and review

Final library 8b60554 full Go suite passed (~23.1s), with CI 40186532370 green.
Focused runtime plan/browser/archive checks passed. Earlier full portal suite and
native 0.163 contract batch passed; exact evidence is preserved in
[implementation history](implementation-history.md). Current source-wait focused
test passes (~4.7s): both source stages, unchanged/replaced source, cancellation,
no native effects while waiting, exactly one fork and journal recovery. Ruby
syntax passes; package compatibility check passes (1 test, 28 assertions).
Final composed-lock check passes; all four worktrees are clean and whitespace
checks pass. Runtime vendor hash is sha256-SscgQ5vY4YUOLWhIk/HVrJdXQZYb+0nlxqBfgsSs2zA=.

Original reviews: [review.md](review.md) and [reboot-review.md](reboot-review.md).
The Important attachment-free retry finding and Advisory timing identifier finding
were fixed. The Blocking orphan-backup finding received its prescribed narrow
fail-closed guard; regression fails before/passes after, full suite green. No
redundant confirmation review was required under skill step 9.

Affected review reuses standalone native reviewer
01a172a0-e739-7563-85b4-f3c8fc7f0ef2, retained gpt-6.1-sol/xhigh, read-only.
Risk is high; four affected lanes plus complete history/pin/migration conclusions
are requested in [baseline-review-packet.md](baseline-review-packet.md). Report
pending in baseline-review.md. Original unavailable v2 reviewer report remains
preserved. Catalog digest 840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa;
full-access execution policy. Review continuation did not override saved settings.

The affected review confirmed baseline preservation, history/pin consolidation and
migration lineage. Its Important plan-lock finding was resolved by removing the
unintended expansion: verify_creation_source! defaults nonblocking, only fork
opts into waiting before destination/provider admission. Plan creation keeps its
existing behavior. Focused fork and existing plan tests pass (~4.56s). This narrow
scope reduction fits mandatory-review step9 without a confirmation rerun.

CI40189655484 on101a1850 was cancelled after the source-wait scope correction
superseded it. Fast and archive jobs passed; full logs nevertheless preserve a
real late creation/deletion failure before cancellation. The thread-retire CLI
omitted --user-state-root and read a schema4 fence as JSON3 (unknown storage
field). Full evidence: /tmp/message-delivery-reliability-2026-10-25/cancelled-baseline-all.log.
The caller audit also found ensure_portal_thread_idle! needs the selected store.
Both helpers now pass runner-owned workspace and state root. The strengthened
Ruby/Go deletion bridge fails before and passes after (~1.5s). The existing stop
fixture confirms owner forwarding and late active-turn refusal (1 test,
6 assertions, ~0.42s). Directly running the Ruby subfile lacked aggregate
ManagedTmux fixtures; running test/dev_session_test.rb with the exact name passes.
Focused source/fork tests still pass (~4.4s). Both fixes are folded into the
owning storage-integration commit; no fixup or repeated pin remains.

Same independent reviewer is assessing that small lifecycle store-ownership fix
through [retirement-review-packet.md](retirement-review-packet.md), all intended
changes/pins committed and quick checks passing. Report [retirement-review.md](retirement-review.md) has no findings; exact owner
forwarding, whole history/pin consolidation and migration lineage are sound. Final input identities are in retirement-final-heads.json.
The final source-wait scope reduction is context, not a redundant confirmation
request. No new schema, library revision or migration change exists.

Final runtime CI40191223335 tests exact9634151b. Superseded40190685438 was
cancelled after the follow-up push. Prior utility /root/baseline_ci_watch ended
with no running operation. Fresh utility /root/final_acceptance_checks (gpt-6-luna/low, full access) owns
the related final profile/configuration build and CI batch after the clean review.
See final-acceptance-task.md for exact commands and log/status paths. Do not accept a blind CI retry.

## Deployment and original-attempt recovery

Read-only coordinator status shows aitherdev held by storage-retention owner
6f07d9f6-42e9-406b-a669-33153fd41bab, claim
11ac5465-9fbe-42c0-839c-f4cce6c63ac0. Finish review and builds, then use the prepared
own request b47c3ec9-13cc-4449-b9b8-33753030694b to enter the ordinary queue.
Do not bypass or release the other claim. [Rollout](rollout.md) remains prepared.
The earlier policy-2 package build must not be selected.

Original target has advanced; do not resend its old Implement the plan request.
After compatible activation and complete fresh native history, restore only the
exact still-submitting unwritten receipt using recover-original-attempt.py with
its exact preimage/claim checks and fsynced backup outside portal Files. Then use
the normal plan recovery endpoint to retire the stale prepared attempt. If native
acceptance appears, reconcile it instead. The script passed disposable exact-row,
backup and refusal checks and has never touched live state.

## Documentation and evidence

[Plan](plan.md), [design](design.md), [rollout](rollout.md),
[review resolutions](review-resolutions.md), and
[implementation history](implementation-history.md) retain decisions and evidence.
Owning feature/upgrade contracts are codex-web/docs/submission-storage.md and
runtime docs/dev-sessions.md, docs/workspace-portal.md and
libexec runtime capability checks. Current source-wait behavior is documented in
docs/dev-sessions.md. Configuration operations remain in
docs/operations/codex-providers-aitherdev.md. Disposable logs/build records remain
under /tmp/message-delivery-reliability-2026-10-25/; live forensic backups belong
under the private verification state directory, never portal Files.

A no-op URL replacement accidentally overlapped two Nix lock updates; the first
failed at Git index.lock while the corrected update completed. Both processes are
finished. Final semantic input diff and composed-lock validation pass. No Git lock
was removed manually. Keep future same-worktree lock updates strictly sequential.

Session URL: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-message-delivery-reliability/


## Final acceptance and queued deployment

All final checks passed. See [acceptance summary](acceptance-summary.json).
Fresh utility /root/final_acceptance_checks completed its batch with no owned
operation remaining. Profile build and its full packaged check phase passed
(check phase 2m13s). Profile is
/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0.
Configuration generation 2026-10-25--13-07-30 built at
/nix/store/4vlqvvpb5s3vqzjsbik75k4wk4ly8r7c-nixos-system-aitherdev-26.05.20261021.da6dc0e.
CI [40191223335](https://github.com/aither64/dev-workspace/actions/runs/40191223335)
passed fast, creation/deletion and archive VM jobs on exact 9634151b. Host job is
not selected for this feature push; no host-module behavior changed.

The built system has no closure package change; its etc tree differs from the
live system only in confctl configuration-info.json and inputs-info.json. This
is an application-only rollout: use the user profile, without system activation.
The candidate preserves archive policy3 and publishes submission schema/policy1.
Native Codex stays 0.163.0.

Normal acquire at 2026-10-25T12:22:33Z returned waiting for own claim
b47c3ec9-13cc-4449-b9b8-33753030694b, owner
d6122ac3-11f1-4040-883f-4771abdd35a1. Aitherdev remains held by the storage-retention
session. The managed coordination recipient is valid and idle; coordinator will
notify it on grant. Do not poll or bypass the reservation; end the turn when
only resource waiting remains. No activation, live migration or original-attempt
repair has occurred. No owned build/test process remains.

On notification, verify exact held status and current selected source/generation
before the normal source profile switch. Preserve newer deployed behavior if
the baseline changed. Complete health, naming, native process continuity, SQLite
integrity and representative delivery acceptance. Then revalidate complete
original native history and use the exact-row repair plus normal stale-plan
recovery to retire the old attempt, never resend its obsolete implementation.
Default-branch integration remains unapproved; no merge readiness is claimed
against the advanced configuration target. Source branches remain published.


## Deployment resumed

Claim b47c3ec9-13cc-4449-b9b8-33753030694b is held since
2026-10-25T12:49:50Z; exact own identity verified. Selected profile remains xjsni6...
with the reviewed ec53874b baseline. All four final heads are exact and clean,
composed-lock validation and portal health pass, native PID is still3387667.
A private fsynced pre-activation JSON backup and exact original receipt preimage
are recorded in pre-activation.json. No profile selection or migration has begun.

Preflight found the unselected --no-link profile build had been garbage-collected
during the resource wait. The attempted native-executable path comparison failed
because the entire candidate store path was absent, not because native Codex
changed. Rebuild exact reviewed inputs with a temporary out-link GC root, verify
the expected output identity, then continue the ordinary claim-bound switch.

Exact rooted rebuild passed in569s and reproduced the reviewed profile48011... exactly. Native executable identity is identical to the selected predecessor. No owned rebuild process remains.


## Live deployment and original recovery

Profile48011... selected successfully at2026-10-25T13:09:24Z (activation exit0).
The native daemon remained PID3387667. Portal health passes. SQLite user_version1
is ready and integrity_check is ok, with both private schema4 predecessor fences.
See post-activation-database.json; migration imported the original receipt intact.

Live canary UUID8a1e9a2e-5d88-4fea-8c0c-bae976a85a9c was accepted in421.69ms; an
identical retry returned the identical receipt/turn in173ms. Native history has
one matching user message and one DELIVERY_CHECK_OK reply. See live-delivery-results.json.
The installed naming child produced message-retry-expiration in2328ms using its
current openai provider, unchanged native0.163 and exact catalog/instructions.
The canary used only an isolated ephemeral utility turn, with scratch removed.

A fresh complete original-thread scan exhausted20 pages, found no original UUID
and confirmed the original raw plan digest. The original WebSocket acquisition
error separately proves non-transmission; history absence alone was not relied
on. The exact-row recovery script matched its full preimage, took a fsynced
private SQLite backup and restored precisely the submitting receipt to prepared.
The normal action:recover endpoint returned200 with retired:true, discarding the
stale plan attempt without native input. Post-recovery originalRows is0 and all
214 remaining source-thread sends are accepted. Native PID is still3387667 and
database integrity remains ok. See original-repair-result.json,
original-retirement-result.json and post-recovery-state.json. Live backups remain
outside portal Files under private verification state.

The selected-composition post-deployment archive/revive test now runs in a
disposable NixOS guest, using the existing reviewed VM script with only its
package parameter bound to the exact installed profile. No live session lifecycle
action is performed. Fresh standalone native watcher01a1733e-4bd4-7241-9c66-98d93fff6bbb owns execution
with verified gpt-6-luna/low startup settings;
CLI explicitly danger-full-access/never and matching installed utility developer
instructions. See selected-lifecycle-task.md and temporary watcher/result logs.
After it returns, complete handoff and retain the machine claim pending separately
approved integration; no merge is authorized by continue.

The original stale-plan recovery endpoint was replayed with the same original
identity after retirement and returned200/retired:true again. Browser receipt
recovery therefore remains idempotent after the out-of-band exact-row repair.
