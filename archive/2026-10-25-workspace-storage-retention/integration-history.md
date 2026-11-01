---
lifecycle: active
---

# Workspace storage retention

Phase: all3 merges and aitherdev release complete; final remote CI observation. Tracking,
aitherdev deployment and explicit cleanup are authorized. Master integration and release are now authorized by the latest user instruction. The initiative stays active with its feature branches retained.

- [x] Implement committed-head archive recovery, compact tracking, sparse checkouts,
  filtered Nix inputs, 24-hour preparation/orphan retention and maintenance.
- [x] Commit and consolidate the three feature series; publish exact heads.
- [x] Independent four-lane review, focused follow-up and required remediation.
- [x] Focused Ruby/Go checks, complete composed package and five workspace checks.
- [x] Runtime CI: fast, browser archive/revival and native creation all pass.
- [x] Scoped aitherdev build, closure copy, dry activation and system switch.
- [x] Application selection, portal/naming/conversation continuity verification.
- [x] Recovery-only compaction, unused coordinator GC and ordinary Nix GC.
- [x] Record attributable cleanup results and hand off.
- [ ] Refresh configuration against newer upstream inputs, obtain integration
  approval, integrate exact final heads, then release aitherdev.

## Exact deliverables and verification

All owned worktrees are below `worktrees/2026-10-25-workspace-storage-retention/`.
Final published heads are in [final-heads.json](final-heads.json). Runtime ec53874b,
workspace564979a0, configuration2d33a9ca. No default branches integrated.

Reviews: [initial report](final-review.md), [focused follow-up](followup-review-report.md).
Risk high; all four lanes, gpt-6.1-sol/xhigh, read-only. Both reviews explicitly
confirm coherent history, single final pin streams and no DB migrations. Optional
private inventory1/2->3 conversion retains supported predecessor readers.
Requested receipt/automatic-eligibility/transition fixes pass focused regressions.

CI run40181077743 passed at exact runtimeec53874b. Full composed package passed
at workspaceb94ca3e2 (deployed-candidate-build.log/.exit,544s); a fresh Luna/low
watcher returned [success](final-build-watcher-report.md). A final mechanical scope
reduction changed only archive/; [complete derivation/input equality](archive-narrowing-build-identity.json)
proves that exact package verification remains applicable. All five final workspace
Nix checks passed. Source filtering preserves all619 non-tracking files and does
not reference the unfiltered workspace source. Maintenance command fixture passes
4 cases/23 assertions, including real Git, external symlink preservation and retry.

## Deployment

Exact rollout: [rollout.md](rollout.md). Held aitherdev claim:
`11ac5465-9fbe-42c0-839c-f4cce6c63ac0` (owner-only). System generation
`2026-10-25--10-35-36` built and copied; dry activation and no-reboot switch passed.
Both running system and system profile match
`/nix/store/1bnl145ln79094l10j60cp4631a69vww-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
Matching tested application is
`/nix/store/xjsni6q4ldh2anc8l1vn6zxjf64m4ska-dev-workspace-0.2.0`.
Candidate forward profile selection passed with the exact held claim/session.
Configured auto-rollback is preserved; Codex remains0.163.0.

Machine release requires verified effects AND integrated deployed feature lineage
under installed coordination policy. Keep this claim held while integration lacks
approval. No reboot, archive/delete of this initiative or other active work is
authorized. Preserve203 pre-existing unrelated shared-checkout modifications.

## Cleanup boundary

Completed recovery-only preview passed:137306112 allocated bytes eligible.
84 unfinished lifecycle/tracking records and8 nonterminal archives are skipped.
Historical deletion has been narrowed to17204 settled raw entries/843116977 logical
bytes. It preserves49116 raw entries/3526176691 bytes belonging to unfinished
archives, all Markdown and portal.yml. [Final manifest summary](settled-archive-deletion-summary.json).
Shared historical tracking is untouched until explicit integration approval.
Refresh maintenance/operation preflight immediately before any future archive-tree
merge; do not invalidate pending digests or bypass unfinished operations.

Baseline immediately before deployment: [before-deployment.json](before-deployment.json),
95339368448 bytes available; private recovery26.55GB, coordinator sources42.86GB,
integration scratch5.40GB, shared archives4.84GB. These are measured existing data,
not space already freed by this initiative. Cleanup results are recorded below.

## Evidence and documentation

Project behavior: runtime docs/dev-sessions.md, docs/session-archive-recovery.md,
docs/coordination-operations.md. Site maintenance: workspace and configuration
storage-retention operations guides. Commands, earlier fixture drift and decisions
are retained in [implementation history](implementation-history.md).

Created normally through dev-session start --no-codex --no-attach; this is owned
threadless tracking. No conversation was adopted or team roster created. Catalog
fallback reviewers and fresh utility watchers have their exact native identities,
models and execution policies in retained reports/logs. No secrets are recorded.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-workspace-storage-retention/


## Deployment verification and cleanup progress

System/app selection passed. postdeployment-runtime.json proves exact selected
paths, healthy portal, unchanged ordinary Codex PID/start time and socket inode.
Live isolated naming passed with workspace-archive-retention; no session created.
Authoritative machine claim remains held. Fresh Luna/low system/app watchers
reported success; complete operation logs and exit files are retained.

Recovery-only apply passed (13.7s): two completed archives reduced from137306112
to65536 allocated bytes, preserving committed heads. Pending/nonterminal skips
remain intact. Coordinator preview passed with retry:false,90 actions including
25 worktrees,60 dedicated roots and5 obsolete workspace profile generations;
27584114688 allocated checkout bytes collectible. Its protected reasons retain
current work, process-held sources and unfinished integrations.
Coordinator --apply --expire-unused is running under a fresh observation-only
watcher. Parent owns mutation/acceptance. Five owned transient environment/build
root links and the completed naming-check binary were retired.


## Final results and next action

Authorized implementation, review, deployment and cleanup are complete. The
portal remains healthy; ordinary Codex process/start time and socket identity
are unchanged after Nix GC. Live isolated naming succeeded. Final proof:
[final-health.json](final-health.json).

Observed available space increased by43030970368 bytes (40.08GiB), from88.65GiB
to128.72GiB. [Complete measurement](cleanup-results.json) and before/after snapshots
separate physical checkout reclamation from ordinary Nix GC:

- Coordinator sources:30277566464 allocated bytes reclaimed (28.20GiB).
- Two completed recovery archives:137240576 bytes reclaimed;64KiB metadata remains.
- Coordinator apply:26 worktrees,60 dedicated roots,5 obsolete profile generations;
  all91 planned actions removed, retry:false.
- Ordinary Nix GC:104 store paths removed,12.3GiB reported freed. No manual store
  deletion or profile-pruning outside the coordinator policy.
- Five owned transient build/environment roots retired. No unrelated QEMU/cache
  campaign cleanup. Shared archive tree remains unchanged pending integration.

84 unfinished lifecycle/tracking records,8 nonterminal archives, live dependency
roots and unfinished integrations remain protected. Historical deletion is
restricted to17204 settled raw entries (843116977 logical bytes), with zero pending
archive or Markdown/portal.yml removals. Refresh that safety preflight before any
future archive-tree merge. The narrowing was a direct reduction of destructive
scope under the accepted boundary; it changed no non-tracking source and its
complete package derivation/inputs are identical to the independently reviewed,
fully verified artifact. No further runtime design or migration was introduced.

Archive inventory schema3 has now been deployed and applied to the two completed
recovery archives. Treat it as consumed persistent state in future revisions;
retain policy3 readers and forward recovery. Pending predecessor operations were
not converted. No database migrations exist.

All three feature heads remain published and all owned worktrees are clean.
Runtime/workspace default refs are unchanged. Configuration master advanced from
the reviewed d12a7737 baseline to95f10b50 through automated channel/llm-agents
updates. Keep the tested deployed configuration2d33a9ca; before integration,
rebase its two-commit series onto fresh upstream, preserve the intended Codex
0.163.0/runtime contract and run the affected composition/build/review checks.
Do not silently turn storage maintenance into a Codex upgrade. Final remote proof:
[final-remote-proof.json](final-remote-proof.json).

Master integration is not authorized. Keep lifecycle:active, all feature refs and
owned worktrees. The exact aitherdev claim11ac5465-9fbe-42c0-839c-f4cce6c63ac0 is
still held (final-machine-claim.json). Release it only after verified deployment
and approved remote integration of the complete deployed feature lineage, as the
installed runtime policy requires. Deployment does not grant merge approval.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-workspace-storage-retention/


## Integration authorization

User explicitly said "ok, merge and release aitherdev" after the handoff.
This approves the storage-retention feature into master for dev-workspace,
workspace and vpsfree-cz-configuration, followed by normal aitherdev release.
Preserve reviewed scope, deployed policy3 state, refs and unrelated shared edits.
Configuration refresh may retain approval only with verified patch equivalence.

Both rebases completed without conflicts. Complete tree reconstruction and
identical range-diff series are in integration-equivalence.json. Workspace
upstream adds only concurrent tracking; config upstream is generated dependency
updates. Composition passes with runtimeec53874b and unchanged extension.
An affected general/risk follow-up uses the original standalone reviewer native
01a1727d-11a8-7f03-8ba0-ae0bb774a578; report integration-review-report.md.
No merge claim acquired until each target is prepared.


## Integration progress

Independent affected general/risk review passed without findings; see
integration-review-report.md. Runtimeec53874b is integrated and remote-proven;
its short merge claim released. Workspacee9144243 is integrated and remote-proven,
with shared tracking plus15 archive lifecycle locks held across preflight/merge;
all unrelated dirty tracked contents preserved and short merge claim released.
Complete package derivation and input identity remains unchanged after rebase.
Refreshed scoped configuration and final workspace/master CI checks are owned by
fresh Luna/low watcher01a17312-e7d4-7601-9c00-76b32bf1e639, full access/never
verified at launch. Machine claim remains held pending configuration integration.

The refreshed upstream root llm-agents selects system Codex0.164.0 (read-only
version evaluation recorded in rebased-root-codex-version.json). This is already
present in the target baseline; the feature patch changes only devWorkspace.
Do not activate that unrelated native upgrade. Installed system/application and
ordinary conversation remain the verified0.163.0 deployment. Independent review
accepts patch-equivalent feature lineage for machine release after remote proof;
the newer whole-system baseline need not be deployed for this merge.

Refreshed scoped system build and all5 workspace Nix checks passed. Built system
/nix/store/hp03j6c3aa74jp1qbvs6rzjczsgzahvf-nixos-system-aitherdev-26.05.20261021.da6dc0e
contains upstream-native0.164.0 and runtimeec53874b; it was built only, not deployed.
Existing tested system/application remains active. Runtime master CI40193848598
is still observed by the same operation watcher. Final rebased feature heads
are in final-heads.json; merge/release evidence remains per-repository.


All3 final feature heads are now remote-master ancestors, with retained feature
refs and clean owned worktrees (integrated-feature-proof.json). The configuration
merge ran ordinary hooks in its prepared Nix environment; all short repository
claims released. Fresh health and exact deployed-lineage equivalence are in
prerelease-health-and-lineage.json. Aitherdev claim11ac5465-9fbe-42c0-839c-f4cce6c63ac0
was normally released after verified ownership/health/integrated lineage, and
authoritative released status was re-read (released-aitherdev.json).
No unrelated baseline dependencies were deployed. Remaining only: merged runtime
CI watcher completion and final tracking reconciliation.
