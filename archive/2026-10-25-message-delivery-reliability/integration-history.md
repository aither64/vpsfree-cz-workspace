# Integration preparation history

Historical checkpoints; current status is in [state](state.md).

---
lifecycle: active
---

# Message delivery reliability

Deployed and the original input block is recovered. All required verification,
including the selected-package lifecycle VM, passed. The user authorized merging all four existing feature branches into master and
releasing the owning aitherdev claim (quote: "merge and release"). Current phase:
refresh and verify current targets, then integrate in dependency order. Preserve
deployed source refs and release only after full integrated-lineage proof.

- [x] Reproduce and fix the pre-transmission deadline/receipt race.
- [x] Implement indexed SQLite receipts and safe import/forward recovery.
- [x] Complete independent review and resolve all findings.
- [x] Pass final builds and CI, including native creation/deletion and archive.
- [x] Deploy the exact reviewed composition; preserve ongoing Codex processes.
- [x] Verify live delivery, exact retry deduplication, naming and database integrity.
- [x] Recover and retire the original stale attempt without resending it.
- [x] Finish selected-package archive/revive VM acceptance and final handoff.
- [ ] Integrate only after explicit repository/target approval, then release the
  machine after verified effects and integrated deployed lineage.

## Outcome and evidence

Profile `/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0`
was selected successfully at 2026-10-25T13:09:24Z. No system activation was
needed: the built system differed only in confctl metadata and had no package
closure changes. Native Codex remains 0.163.0 and its daemon PID stayed 3387667.
Portal health passes. SQLite schema 1 is ready, integrity is ok, and both
schema-4 predecessor fences have mode 0600. Recovery is forward-only with a
package supporting submission schema/policy 1; retain database/WAL and durable
migration backups. Never restore a forensic backup over newer receipts.

Live send UUID `8a1e9a2e-5d88-4fea-8c0c-bae976a85a9c` was accepted in 421.69 ms;
identical retry returned the identical turn/receipt in 173 ms. Native history
contains one matching user message and the expected DELIVERY_CHECK_OK reply.
The installed naming child returned `message-retry-expiration` in 2328 ms using
its current `openai` provider and the deployed immutable catalog/instructions.
Its utility turn was ephemeral and private scratch was removed.

The exact original receipt in `2026-10-24-context-copy-performance-tests` was
still submitting and matched its reviewed canonical preimage. A fresh complete
history scan exhausted 20 pages, found no original UUID and matched the raw
source-plan digest. The original WebSocket writer-acquisition failure separately
proves non-transmission; missing history alone did not authorize repair.
The reviewed script took a consistent fsynced private SQLite backup and restored
only that exact row to prepared. Normal plan `action:recover` then returned
200/retired:true for the stale proposal. Replaying the same recovery returned the
same result. The original row is absent; all 214 remaining thread send receipts
were accepted at the post-repair snapshot. No obsolete implementation input or
mode change was sent. Native PID remained 3387667 and integrity stayed ok.

Evidence files: acceptance-summary.json, pre-activation.json,
post-activation-database.json, live-delivery-results.json,
original-repair-result.json, original-retirement-result.json,
original-retirement-replay.json and post-recovery-state.json. Raw logs and
canary code live under `/tmp/message-delivery-reliability-2026-10-25/`.
Private forensic backups are outside portal Files under
`~/.local/state/dev-workspaces/verification/message-delivery-reliability-2026-10-25/`.

## Ownership and exact deployed lineage

Claim `b47c3ec9-13cc-4449-b9b8-33753030694b`, owner
`d6122ac3-11f1-4040-883f-4771abdd35a1`, is held since 2026-10-25T12:49:50Z.
Managed coordination thread `01a172c4-ca9f-7c70-b3e5-b1290a0568eb` is the valid
notice recipient. It confirmed coordination standby; execution remains with
external investigation thread `01a17206-ed6f-78b3-b410-c7d6015b6777`.
The roster is null; no team member or other session was replaced.

All feature worktrees are under `worktrees/2026-10-25-message-delivery-reliability/`
on the identically named branch. Exact published and deployed heads:

| Repository | Head |
| --- | --- |
| codex-web | 8b60554bc10c2a6bcbf9732a8b77ad959c317036 |
| dev-workspace | 9634151b9836311c331a58880fbb4c46133fd98f |
| vpsfree-cz-configuration | 45683e38d3dc8e3ced20eae553f879e46ec84348 |
| workspace | 72e15700b241d75bcbc1eb8abf04542f70d9792f |

The newer deployed storage baseline ec53874b was retained exactly, including
archive recovery policy 3. Configuration and workspace pin streams are each
consolidated to one final update. Original baseline refs remain retained.
No feature content was merged into default branches. The configuration target
has newer unrelated changes; no final merge readiness is claimed before target
refresh, required checks and applicable equivalence/review gates.

## Verification and reviews

[Final affected review](retirement-review.md) has no findings, with explicit
whole-history, repeated-pin and migration-lineage conclusions. It reuses
[original review](review.md), [reboot review](reboot-review.md), and
[baseline review](baseline-review.md) for unchanged assessed behavior.
Retained independent reviewer: native `01a172a0-e739-7563-85b4-f3c8fc7f0ef2`,
actual gpt-6.1-sol/xhigh, read-only. Risk high; all four lanes were assessed.
All Important/Blocking findings were fixed; prescribed narrow fixes used skill
step 9 without redundant confirmation review. No delivery migration revision
preceded this rollout in production; the sole direct migration remains schema-3
JSON to SQLite user_version 1, with schema-4 fences and the reviewed orphan guard.

Library 8b60554 full tests and CI 40186532370 passed. Runtime CI
[40191223335](https://github.com/aither64/dev-workspace/actions/runs/40191223335)
passed fast, creation/deletion and archive jobs on exact 9634151b. Profile build
and its packaged checks passed (check phase 2m13s); configuration generation
`2026-10-25--13-07-30` built. Exact initial build was collected while waiting;
a rooted rebuild reproduced the same profile and passed in 569s before selection.
Composed-lock validation passes. All final feature heads were clean and exact at
activation. No owned build/rebuild/activation process remains.

[Selected-package lifecycle acceptance](post-deployment-lifecycle.md) passed
(exit 0; about 18m39s overall, VM script 884.77s). It used the exact installed
profile with the existing reviewed VM script, including archive/revive, shared
lock wait, portal restart, worker interruption, retained recovery metadata and
deferred tracking sync. All fixtures stayed in a disposable guest. Fresh
standalone utility `01a1733e-4bd4-7241-9c66-98d93fff6bbb`, verified gpt-6-luna/low,
full access/never, completed with no owned operation remaining. The output is
`/nix/store/99113yqjh101fkzc17yjmd1ry082zhp8-vm-test-run-dev-workspace-session-archive-lifecycle`.
The final portal remains healthy; daemon PID is still 3387667, whose service
start timestamp is 2026-10-18 12:08:01 CEST, before this activation.

## Documentation, recovery and handoff

Owning feature and recovery guidance remains codex-web/docs/submission-storage.md,
runtime docs/dev-sessions.md and docs/workspace-portal.md, and configuration
operations docs/operations/codex-providers-aitherdev.md. [Rollout](rollout.md)
records this individual deployment. [Design](design.md) retains invariants and
bounded corrections. [Review resolutions](review-resolutions.md) records findings.
[Implementation history](implementation-history.md) and
[deployment history](deployment-history.md) preserve superseded checkpoints.
Reusable notes cover Ruby aggregate fixtures, cancelled-CI failure logs and
retaining unselected builds with a GC root. Raw artifacts remain untracked.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-message-delivery-reliability/


## Merge approval and target refresh

The current user instruction "merge and release" approves codex-web,
dev-workspace, vpsfree-cz-configuration and workspace into refs/heads/master, plus
release of own aitherdev claim after verification. See merge-approval.json.
Library and runtime targets are ancestors of their reviewed/deployed heads and
need no rewrite. Configuration and workspace have absorbed the storage baseline
and advanced their pins; refresh only the final runtime pin on current targets,
preserving the exact deployed source heads on dedicated retained refs.

## Final integration preparation

Current phase: approved integration. Exact final heads are recorded in
[integration-final-heads.json](integration-final-heads.json). Library and runtime
retain their exact independently reviewed/deployed heads; their complete current
target ranges contain the assessed implementation without superseded pins or
fixups. Sole delivery migration a9086b0 is now deployed and unchanged.
Downstream feature branches each contain one final pin update atop current
master; deployed refs remain published. Fresh affected review is in progress.
Workspace Git tree equals the deployed tree; evaluating its final exact head
produces the installed derivation dzjigbrkh0lxn9ybr2dhh23w2awx99dp and output
48011krllhj3428878a8h55sb6x4wky0. Exact artifact identity, rather than tree equality
alone, permits reuse of installed package acceptance.

The first disposable configuration target checkout completed but its post-checkout
hook failed outside the Nix shell (missing gems). No claim was held. Repeating
its ordinary checkout in the repository Nix shell passed; final merge/push will
use that shell. Existing documented Nix/Overcommit setup remains applicable.

## Integration progress

Library 8b60554 and runtime 9634151b are now proved on remote master after
fast-forward-only merges; their short claims were released immediately.
Independent integration-refresh-review.md has no content findings and explicitly
accepts the downstream equivalent feature lineage and consolidated history.
Its concurrent tracking-only workspace master precondition is addressed by a
clean patch-equivalent rebase atop da52b2ca, preserving that other session record.
Exact final workspace head: a6ebab6b10a8d0806f4db9588e1433b568473990. Installed Certification
reconstruction proof and original review receipt are retained; no migrations or
substantive behavior changed. No extra behavioral suite is required solely for
the pin refresh. Any later deployment of the current full configuration must
build/check that exact target; its unrelated scheduled inputs were not activated.

Workspace final comparison is saved at e9144243..a6ebab6b (current remote
master at capture), including the preserved concurrent tracking commit da52b2ca.
A second request with narrower da52b2ca base correctly refused because that head
already has an immutable comparison; no stored comparison was edited. Review and
Certification bind the exact da52b2ca..a6ebab6b pin range independently.
Final rebased a6ebab6b evaluates to the SAME installed application derivation and
output (workspace-artifact-identity.json), so package acceptance remains exact.
