---
lifecycle: active
---

# Proactive swap removal from 6.12.113

Current phase: staging integration. User authorized implementing the final plan and vpsAdminOS staging integration after quick checks and independent review. No kernel builds/boot/runtime/full-CI wait are pre-merge gates.

## Phase checklist

- [x] Verify exact session identity/environment and retained Full-team roster.
- [x] Resolve .113 patch inventory and final user decisions.
- [x] Refresh architect-owned design.md and commit substantive initial plan/state.
- [x] Reconstruct/publish Linux feature head (implementer0): 86d54e7adff82e632299b41a2d1397ccbec1cb9e.
- [x] Clean DAMON options and retire experimental tooling (implementer1); final pin/commit pending.
- [x] Commit exact final .113 kernel pin/hash and pass quick checks (implementer1): bf9bcb5e83f21d17561aad9416eeef2853d90956, final evaluation PASS88s.
- [x] Independent final review complete; I1-I4 narrowly fixed, directly reconciled, final pin/evaluation passed.
- [ ] Merge reviewed OS branch into remote staging (lead/coordinator).
- [ ] Kernel build/boot/runtime: subsequent user staging validation, not run here.

## Ownership and repositories

Architect0 completed the lead-accepted final brief; both implementers assigned complete packages and notified source work may proceed. Implementer0 will own Linux worktree/source/history; implementer1 will own OS cleanup, technical docs, quick checks and final pin. Both are ready with saved workspace_write access; settings retained. Lead owns tracking, acceptance and coordinated integration; no application edits by lead. OS feature worktree/branch registered at worktrees/2026-10-16-proactive-swap-patch-removal/vpsadminos, base 60f9ed1c153a734880e002b63d6ab7ed5fe87d0e; target refs/heads/staging. Linux materialization in progress.

OS baseline: 60f9ed1c153a734880e002b63d6ab7ed5fe87d0e (staging). Original .113 source: 11058eb4fe1cba30653e8e643546c13bc8bcd792. Upstream base: 7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e. Prior local-source gap was resolved by architect read-only HTTP/API inspection during planning; implementer must acquire exact source normally for execution. Partial-clone reads use GIT_NO_LAZY_FETCH=1 to avoid accidental lazy fetches.

## Final decisions and approval

- Latest 6.12.113 only; remove entire experiment including custom DAMON NUMA/quota controls.
- Retire experimental QEMU/tests/entry points; no legacy fixture support and no new normal-reclaim tests.
- No backward compatibility or rollback requirements: user confirms never deployed.
- Preserve all other kernel/ZFS pins and frozen outputs; upstream DAMON and unrelated product/safety patches remain.
- User: "I'd prefer if we could merge this after quick verification ... boot ... on staging nodes"; selected "staging (Recommended)" for vpsAdminOS merge target; subsequently "Implement the plan". Scope: vpsadminos refs/heads/staging only, new Linux feature publication. No existing Linux release/default ref rewrite, machine deployment or reboot approval.
- Mandatory final independent review remains required after exact committed deliverables and quick checks. Full CI may trigger but is not awaited. Build/boot/runtime acceptance remains pending for user.

## Verification and next action

Implementation assigned. Implementer0 accepted final brief and verified exact identity; explicit SSH fetch is acquiring the missing .113 source from codex/kernel-6.12-upgrade-20261017 in the existing partial clone. Linux SSH transfer completed and exact objects are being indexed; existing clone has ~39,533 packfiles and stale multi-pack-index, so implementer refreshes index only, preserving packs/refs. OS cleanup is coded (9 files, 647 deletions/2 insertions), no stale experiment references reported and ordinary memory-view tests unchanged; lead inspected diff. Hook configuration reviewed/signed normally. Fresh Luna/low watcher owns exact nix develop --command true to prepare declared OS environment, logs os-env.log and os-env-result.json. Formatting/hooks/evaluation/final pin remain pending; no builds/runtime/CI wait started. Initial root inspection confirms shared master, empty staged index, no declared root hook framework or pre-commit hook. Preserve all unrelated shared files/index. Next: accept each implementation report, final pin and quick checks, then assign independent final review.

## Documentation and session

See [plan.md](plan.md) and [design.md](design.md). Initial tracking commit: e9207a9d61f4700619d675297f7c03a12027e13c. No lifecycle/cleanup action authorized; leave session open.

## Implementation checkpoint

- OS cleanup coded: 9 files, 647 deletions/2 insertions. Lead inspected intended DAMON/tool/selector diff. Nixfmt and required Overcommit hooks passed in declared environment, no bypass; git diff --check passed. Other kernel/ZFS pins, ordinary memory-view tests and .6.18-specific prose unchanged.
- Exact Linux acquisition complete: 61 downstream commits above upstream .113. Architect/lead accepted unchanged inherited published prefix through108d4158fae3c0d0affb58491ee67b9f573b550e as actual feature base. Full upstream series still inventoried/reviewed, with legacy baseline stages/messages explicit. Drop six experiment owners then rebuild only suffix; consolidate CSS safety repairs and preserve iterator/affinity/NFS owners with current identity/provenance. No unrelated prefix overhaul.
- OS environment watcher PASS (40.85s), os-env.log/result. First no-build eval failed before assertions due path-flake missing revision metadata; owner reproduced/diagnosed existing channel-registration null interpolation, fixed only check input to git+file flake. Corrected fresh evaluation PASS exit0 in86s: all four default/selected .113 disabled/enabled configurations, drv paths/service/assertions/output+test discovery (25packages/186tests), failedAssertions=[] each; os-evaluation-git.log/result. Original failed evidence retained. Final pin-derived evaluation still pending. No build/runtime/full-CI wait.

Architect updated design.md with exact unchanged 50-commit consumed prefix, actual task base108d4158, complete upstream history review boundary, CSS fold/provenance and independent affinity/NFS treatment. Scope remains minimal; no unrelated history cleanup.

## Scoped implementation clarification

Exact owner inspection found a2425d1734ae mixes experimental accounting with ordinary sysinfo unlimited swap capacity correctness for cgroup-v1/v2. Dropping its full diff would regress existing ordinary views/tests even without proactive activity. Lead accepted a minimal standalone kernel/sys.c owner retaining the two ordinary unlimited branches, with full provenance, while all six experimental owners/behavior remain omitted. No new tests, runtime gate, generic saturation rewrite or experimental metadata. Architect directs implementer0 and records concrete source boundary.

Kernel source materialized and registered at worktrees/2026-10-16-proactive-swap-patch-removal/linux, feature branch2026-10-16-proactive-swap-patch-removal from exact task base108d4158fae3c0d0affb58491ee67b9f573b550e. Backup refs/heads/backup/2026-10-18-proactive-swap-patch-removal-6.12.113-original preserves11058eb4. Four retained suffix owners committed provisionally (iterator83a59ebf6d04, CSSv2def4b8a2613f, affinityb7609ccb76da, NFS7ab40a1fe08d), not final: minimal ordinary sysinfo owner and final source checks/publication remain. DAMON subtree/header/admin docs compare byte-identical with upstream .113. OS owner bundles cleanup/final pin in one coherent commit after final kernel publication; no placeholder pin stream.

## Final Linux source publication

Published SSH feature refs/heads/2026-10-16-proactive-swap-patch-removal at86d54e7adff82e632299b41a2d1397ccbec1cb9e. Exact inherited50-commit prefix retained; five new logical suffix owners (iterator/CSSv2/affinity/NFS/ordinary unlimited sysinfo v2). All six experimental commits absent ancestry. Quick source owner checks passed: diff --check old/new and task range; native checkpatch0errors0warnings on182lines; native DAMON subtree/header/docs byte-identical upstream; all28old-to-new changed paths within experimental file union; unchanged safety files and iterator/affinity/NFS stable patch-ID equivalence. Compilation/runtime not checked, no CI wait. OS owner notified exact final head for one archive/pin update. Full linux-source-inventory.md being finalized before independent review.

Linux complete inventory accepted for review preparation (linux-source-inventory.md): all61original owners, full55final upstream series, exact50prefix preservation, five logical new owners, 28-file constrained final diff150insertions/819deletions, no migrations. Architect report-based acceptance confirms final source conforms; this is not independent final review. Archive watcher PASS42.166s: exact86d54e7 archive root, Nix flat byte hash independently rehashed in Python, sha256-qOskH2ecF3n0yzNE2F9vo7voFS1flXZo8Dc9h8MzxPM=. OS owner notified to finish pin/commit/publish before final evaluation/review.

## Final OS deliverable and review gate

OS published clean bf9bcb5e83f21d17561aad9416eeef2853d90956 on session feature branch, exact base60f9ed1c153a734880e002b63d6ab7ed5fe87d0e, one coherent commit10paths/4insertions/649deletions; complete final diff/series inspected by lead. Final .113 Linux revision86d54e7 and SRI verified. Final no-build Nix matrix PASS exit0 in88seconds, all4configs exact URL/SRI/service/assertions/output+test discovery25packages/186tests, evidence os-evaluation-final.log/result. Required hooks/formatting passed, no build/runtime/CIwait. All intended application changes committed in both repos; final review packet ready. Risk HIGH (host/tenant memory and removed Nix interfaces), all four review lanes, saved independent reviewer0 Sol/xhigh/read_only selected without settings override.

## Independent review findings (review in progress)

Reviewer0 reported Important source-visible ordinary reporting regressions from restoring prefix: cgv1 meminfo unlimited branch unreachable/zero; finitecgv1 free computed from host rather than container capacity; unlimitedhost-zero-swap proc/swaps must be header-only; finitecgv2 max may be below current so sysinfo/meminfo free subtraction needs zero clamp. Lead accepted narrow fixes under ordinary-view retention; implementer0 owns source/provenance/version/checks and architect brief clarification. No newtests/runtime/fullCIgate. Reviewer finishing consolidated ordinary-view/history/pin inspection before final source republish. Original reviewedheads86d54e7/bf9bcb5e retained; OS owner holds pending single revisedsource handoff and folded finalpin. Session-owned unmerged feature may be lease-rewritten with reviewedhead backup, no pre-existing release/defaultrefs touched. Final accepted review/reconciliation not yet recorded; merge not submitted.

## Completed original independent review

reviewer0 (retained gpt-6.1-sol/xhigh/read_only, native thread01a14fe8-f792-70f0-aba5-d6b688155311) completed all4lanes on exact original Linux86d54e7/OSbf9bcb5e, full upstream/source/task histories and final pin. Complete original12300-character report preserved verbatim from that same-session native report call in review-report.md. No Blocking finding; Important I1-I4 exactly match the prepared15insertions/7deletions three-file ordinaryview corrections. Lead directly inspected that diff; implementer0 instructed finalize/fold ordinaryowner v3, backup reviewedsource, exactlease republish ownfeature, no release/default rewrite. Reviewer explicitly permits direct narrow-fix reconciliation without automatic full rereview.

History: exact50consumed prefix/inherited history debt explicitly assessed; no new task consolidationblocker, five logical suffix owners and one OS pin stream appropriate, no migrations. Original pin/linkage verified (reviewer could inspect receipts but not independently access archive storebytes in their environment). Subsequent exacthead hash proof will be freshly recorded with GCroot retention. Accepted Advisory: pre-existing ordinary proc/swaps byte-versus-KiB mismatch unchanged in original/finalsource, no scopeexpansion or runtimegate; user staging validation may expose this known baseline limitation. Compilation/runtime remain unverified.

## Narrow source remediation finalized

Linux final1dfea587406b7dd79973831d1677fb2418e5e9aa published/SSHverified after dated reviewed86d54e7 remote backup and exactlease update of OWN unmerged feature. Original11058 source/release/default refs unchanged. Ordinary owner foldedv3; first4suffix+50prefix unchanged, full55history. Lead directly inspected final15add/7del three-file committeddelta and reconciled I1-I4 (review-reconciliation.md). Final source quickchecks pass checkpatch0errors/0warnings227lines, diff/preservation checks. Fresh revised_archive_watcher owns exact revisedarchive hash/root/indirectGCroot verification before finalOSsingle-pin amendment. Merge remains unsubmitted pending finalpin/eval and final premerge inventory.

OS final correctedheadca3ff61a3931f0eb524543151d5d78a70f87bfc7 published exactlease after reviewedbf9bcb5e remote backup; only .113 rev/hash differs from reviewedtree, parent inspected delta. One logical commit10paths, clean; stagingbase60f9ed1c unchanged, nativecomparison refreshed, requiredhooks passed. Revised archivewatcher PASS~39s,246079556bytes, SRIsha256-IvyBosmZkpWxAK4Bz0sQ+RBwUQZwN+GtBxwjBY1lAdQ=, ownedindirectGCroot and proof retained, parent confirmed archive availability/root. Fresh revised_os_eval_watcher owns final four-case no-build checks on exactca3ff61a. No fullrereview needed for accepted requestednarrowfixes; review-reconciliation.md retains originalanchors/directinspection. Merge waits finaleval+remoteinventorycheck.

Final correctedOS no-build matrix PASS onca3ff61a, all4configs exact1dfea587/SRI/assertions/writes/output+test discovery. Watcher transparently recorded accidental duplicate invocation, bothpass, no sourcechange; no extra checks needed. Lead finalremote/head/cleantree/fulltaskhistory check passed. Reviewreceipt binds finalOSrange plus immutable originalreport and direct narrow-fix reconciliation. Integration request 8db9c04d-a44e-488d-9448-bf9d481bbf30 prepared for ONLY vpsadminos refs/heads/staging, no deployments/reservation.

## Integration 8db9c04d-a44e-488d-9448-bf9d481bbf30

Requested exact feature heads are integrated. See integration/8db9c04d-a44e-488d-9448-bf9d481bbf30/summary.md
and integration/8db9c04d-a44e-488d-9448-bf9d481bbf30/result.json for operation receipts. Feature refs and session retained.
