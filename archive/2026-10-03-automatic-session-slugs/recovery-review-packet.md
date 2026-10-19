# Related recovery review packet

This is a real related review turn after focused checks and all intended source
commits. Initial independent full review is in review.md; its immutable exact
inventory/diffs are retained under review-pass1/. Retain reviewer0, saved
purpose review/read_only/gpt-6.1-sol/xhigh, independent and unchanged. No model
or effort override and no fallback. External coordinator owns the lead; the
native root remains idle.

## Scope and applicable lanes

Overall risk remains high: persisted request/upload ownership, interrupted
writes, public recovery errors, worker dispatch, mixed versions and deployment.
Review general, architecture/repetition, scope/proportionality and
risk/compatibility for the runtime recovery changes and their exact consumers.
The rerun is justified because the fixes introduce private dispatch/confirmation
bookkeeping, an additive request-bound503 and the separate-request UX alternative
that pass1 did not assess. This is not a request to repeat unaffected provider
lanes or the unchanged binary-helper design; providerca0f3bc9 stays exactly the
pass1 source. Read the mandatory skill and all four lane references and the
applicable workspace/repository guidance. Perform the review directly, no
nested agents, application writes, ref/pin changes, actual Codex/browser/VM,
long tests, deployment, merge or lifecycle. Pure read-only/focused checks are
fine when useful; do not bypass the native Nix daemon restriction.

## Outcome and boundaries

User requested automatic dated slugs from the initial prompt, optional custom
name under Options, existing fork/plan/CLI contracts. The user explicitly chose
model naming with file/network action tools disabled and questions rejected
immediately; pure clock remains allowed. This boundary and provider implementation
are unchanged. No Codex upgrade, literal zero-tool claim, generalized cancellation,
rejection ledger, hostile-local-operator framework or arbitrary-root relocation
promise. Local host operator is trusted; remote clients remain untrusted.

Pass1 found two Important issues: a published running attempt could have no
worker after failed directory sync; stale-catalog rejection could leave a frozen
browser attempt with no usable continuation. The coordinator elected to fix both.
The accepted architect supplement (design.md, Accepted remediation design: R1
and R2) and recovery-report.md explain the selected bounded behavior. Assess it
independently; the report and test passes are evidence, not a conclusion to adopt.

R1: retain the exact published record, confirm its bytes and directory syncs
before acknowledgment/next effects, track one pending launch per request/attempt,
never automatically redispatch an already-dispatched stopped naming worker.
Expose explicit retry after its later write is confirmed; recover a retry's
published current attempt without another increment. Catalog claim replay
confirms file/directory durability. Collection completes/retains an accepting
intent's claim or aborts before expiry; it never consumes its pending dispatch.
Receipt retirement confirms compact mapping moves. New fixed JSON HTTP503:
code preparation_persistence_unconfirmed and exact requestId. The frozen browser
body may repair that exact bound error; generic503 or a mismatch cannot. Existing
404 still permits only identical replay, never clearing/reusing identity.

R2: retain Recover saved request and add Start a separate request in a new
noopener tab. Preserve original ID/body/settings/text/file selection/scope and
its recovery; original may still complete. New tab uses the current catalog,
newUUID/freshscope; no URL prompt, implicit data transfer, file release, old-scope
adoption or automatic submission. Copy saved text and deliberate reattachment
provide continuation. HTTP4xx or404 never proves global non-admission. A restored
attempted draft keeps its normal recovery, rather than being overwritten.

## Exact source and complete branch inventory

Worktrees are /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-automatic-session-slugs/{codex-web,dev-workspace,vpsfree-dev-workspace,workspace}.

| Repository | Remote/default base | Final head |
| --- | --- | --- |
| codex-web | 4c170393a96ed0a6ac2e43488d073f6fcab36132 | ca0f3bc980ca99454d000761aeee37b4b9bbafc3 |
| dev-workspace | 924c0ec28c41dd8b56aaf17f2212b302ca614899 | 0ed3237557d1cac494b39234c1a0ae455fb6cee6 |
| vpsfree-dev-workspace | 8f8d8ecf5031c40d3e4a4ee2e9425721fc035800 | d297d8c3b39c973c194e40e1a91fff40a1b4b1d0 |
| workspace | 1fa9c982b866a305bd1451f2c32f6d387d2dc1a3 | fe9b2ccb0178f15ecbe05dfb0a33fd7ada53597a |

All source worktrees/indexes are clean. branch-inventory.md contains complete
remote-default-to-head commit lists, statistics, final diffs and own incoming
diffs. recovery-final.diff is exact runtimeedcfc18-to0ed3237. Reconcile those
actual refs/diffs rather than trusting titles. Incoming bases remain runtime4ef
and extension399; workspace was rebased onto current sharedmasterad539340 before
final review, its prior pin patch was range-diff equivalent. New exact pins are
one consumer update each. The checked runtime tree hash is
e38e2be96608c43dedc76fbd4e8cecdfe57d9903, preserved byte-for-byte after consolidation.

Five runtime units: uploads802b3db, backend473e045, adapterabed217,
dependency2bf6d5e and frontend0ed3237. Temporary recovery fixups50f1d0a,
d5527ac and3e9fa3b are folded. Docs/tests were split with their owning units;
backend/browser rebase context conflicts were resolved without changing the
checked final tree. Adapter and dependency patches are unchanged, only their
parents changed. Final messages describe behavior and rationale.

Require an explicit whole-branch history conclusion for the cleaned new series
and migration provenance, building on pass1 rather than repeating unchanged
provider work. Identify any remaining obsolete approach, unused shim or repeated
pin update. No incoming database or namespace migrations. Preparation schema1
is direct; receipt1/2/3, catalog1 and authority/journal/manifest formats are
retained. R1 private bookkeeping adds no persisted version. Preserve exact
already-deployed runtime4ef298b30f9cdbdcfe02bf6526e0f69ecc9bf7b4 and extension
5b2e9a4bb95bcf4070d62da33b219ed3c5a33f12,
101d31264fb54cc39b2d0d9519a202d0705a7078,
f50c92bf146c3f3d93a5293e0c005f5fdb3a26e2,
399c33023a568a8d7a21e4e4df52829628720a28. They are published/deployed lineage,
including policy2-to3 and storage/bootstrap behavior, not unapplied experiments.
Inherited shared-master coordination commits belong to their respective owners.

## Ownership, docs and quick evidence

Runtime owns admission/recovery and uploads, consuming provider RunEphemeralTurn
through the unchanged naming adapter and exact Go/flakeca pin. Extension calls
runtime lib.mkPackage; workspace calls extension lib.mkPackage with both cluster
providers, siteConfig and retained teamConfig. Full extension lock comparison
versus deployed-extension baseline changed exactly runtime/provider. Workspace
baseline changed exactly extension/runtime/provider; all other nodes equal.
Actual selected runtime-contract JSON equals deployed full schema1/policy3.
No new host-migration VM trigger, per architect and pass1 reviewer; reassess if
these private recovery changes alter that boundary. Normal checks still required.

Owning feature documentation is dev-workspace/docs/session-preparations.md;
entry-point links in README/session/portal docs remain. test/README.md describes
registered pure contracts and prepared real browser fixture. Main applied the
required writing skill directly after facts settled. Session-only rationale,
heads/results and rollout are in plan.md/state.md/design.md/recovery-report.md/
rollout.md/verification-plan.md. Exact records are not release authorization.

Parent quick PASS against the preserved final tree:
- Go25 top-level tests, no skips; web2.364s. Selector
  ^Test(SessionPreparation|PreparationUpload|ShippedBrowserClientMatchesSessionAPI),
  owning Nix environment, TMPDIR=/tmp, GOWORK=off, -mod=readonly, browser opt-in unset.
  Includes six new web groups and upload confirmation, actual post-rename faults
  for accepting/running admission, retry, later base/reservation/failed worker,
  mapping replacement/move, generation refusal and actual-file collector retention.
  /tmp/automatic-session-slugs-remediation-quick-go.jsonl.
- Direct pure preparation Node19cases, including exact503 mismatch controls,
  stale409+404, lost response, unchanged old envelope/selection, separate fresh
  draft and restored attempted draft. Registered Go harness also passed.
- Five changed JS/CJS syntax entries, gofmt and git diff whitespace.
- Ruby existing creation/fork/reservation16runs223assertions, no failures/errors/
  skips1.460770s. /tmp/automatic-session-slugs-remediation-quick-ruby.log.
- Extension selected-contract source Ruby2runs149assertions, no failures/errors/
  skips3.731486s. /tmp/automatic-session-slugs-remediated-extension-quick.log.
- Workspace deployment contract4runs19assertions, no failures/errors/skips
  1.240694s. /tmp/automatic-session-slugs-remediated-workspace-quick.log.
- Actual declared extension checks.package drv and complete workspace default
  package evaluate. Prepared output /nix/store/wrfddxrfkzzpiqrxcvssmzkh96nm1arm-dev-workspace-0.2.0
  is NOT built or deployed. No declared hook framework/core.hooksPath; normal
  hooks/file-based commits used, no bypass.

Provider normal CI passed unchangedca in pass1. Fresh Luna watcher observes
new runtime normalCI37151688569 and extension37151890863, exact heads above.
Those automatic normal CI checks are not the postponed actual integration gates.
Do not claim a skipped hostVM job ran.

## Remaining release gates and requested report

No actual browser, exact-binary isolation, race, old-source compatibility,
full workspace package/VM check or deployment has run after remediation.
After findings reconciliation, parent owns those gates through fresh utilities.
Exact unchanged native Codex0.160.0 must prove actual original model metadata,
tool dispatch, clock/question behavior, active-provider cancellation and no
persisted utility thread/goal/memory effects; mocks/compile/schema alone cannot.
Real Chromium fixture must prove no-opener separate-tab ownership and old
completion/recovery. Existing team settings and old-source924 uploaded-state
fixture remain required. Forward-only user-profile deployment on aitherdev;
no host config changes or default-branch integration authorized. Retain sessions,
canaries, branches and ownership; no archive/delete/stop.

Return findings ordered by severity and lane with concrete source/commit
references, R1/R2 disposition and bounded remaining gaps. Explicitly assess
whole-branch history and migration lineage at final refs. If the alternative
needs adjustment, describe the smallest supported correction without introducing
speculative cancellation/ownership frameworks. Report to native lead and remain
available for coherent follow-ups. Parent records the report and owns decisions.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-automatic-session-slugs/
