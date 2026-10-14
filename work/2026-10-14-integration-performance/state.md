---
lifecycle: active
---

# 2026-10-14-integration-performance

Ready, awaiting merge approval. Optimizations1–5 are implemented, verified and
deployed to aitherdev. This initiative remains active because all four final
feature heads are unmerged and its machine reservation remains held for review.

## Phase checklist

- [x] Accepted scope, lead-owned design and initial tracking committed6415d3ac.
- [x] Implementation and focused checks complete in four feature worktrees.
- [x] Independent review complete; narrow Go metadata consumer follow-up validated.
- [x] Full package, Ruby, browser, extension, workspace and CI checks passed.
- [x] Three driver/build benchmarks recorded, including a separate cache miss.
- [x] Ordered system/profile rollout and live acceptance passed.
- [ ] User approval to merge the four feature branches into master.
- [ ] Final integration and reservation completion after that approval.

## Final branches

Branch2026-10-14-integration-performance in each registered worktree under
worktrees/2026-10-14-integration-performance/:

| Project | Published head |
| --- | --- |
| dev-workspace | 832d9f1a6a21337dd44063ddf39f7a88cfc95450 |
| vpsfree-dev-workspace | 767dfd587e346168e1443e65ccdb67ce748f3fe3 |
| workspace | ee8645664ed75c7069c259d9e888a8ad334c7f76 |
| vpsfree-cz-configuration | d28926183eb9f1dc427ed597819cf157796ade88 |

Complete series, bases and diff digests: review-inventory.json. Three coherent
runtime commits; one extension/adoption commit each; configuration docs plus one
generated pin. No obsolete approaches, redundant pin streams or migrations.
Source originals retained in scoped refs. Shared master was never rewritten.

## Verification and performance

verification-core.json and verification-results.json retain exact commands,
heads, exit statuses and timings. All final checks passed, including CI38647942844.
689Ruby tests across11shards passed; Go-only metadata remediation preserved the
exact Ruby aggregate derivation. Source-filter tests prove portal-only reuse.
Focused admission4/13, integration17/76, certificate4/8, extension recipe3/8,
artifact registration10/101 and affected package-layout checks passed.

Main verification/preparation phase25m17s. Three disposable driver runs took
0.696/0.690/0.675s active administration; zero queue. Exact workspace/aitherdev
builds in parallel took138.3/163.1s. Comparable warm workspace builds were
1.273/1.354/1.288s; one cache-miss rebuild309.7s is retained separately. Missing
Nix outputs prevented that sample being called warm; package root is retained.
The complete live workflow target remains unverified because feature merges are
not authorized. See performance.md and performance-results.json.

Full verification initially found the Go package reader rejecting new metadata;
fixed and fully rechecked. Failed attempt logs retained with attempt-ef82 prefix.
Earlier CI synthetic package fixture omitted required libraries; repaired and
focused regression passed. Configuration hook first failed outside its Nix shell;
retained checkout was initialized and original hook replayed, without bypass.
Superseded CI cancellation returned HTTP403 due token scope; final CI passed.

## Review and documentation

review-final-summary.md distinguishes independent review through ef82f595 from the
narrow832d9f1a parser follow-up. Review packets/remediation retained. Reviewer
Astra/xhigh fallback, native01a13c61-bcf5-7e90-8c9b-085f4f9127ae; roster:null.
Generic integration/coordination docs own contracts; extension/workspace docs
own recipe/policy adoption; configuration operations guide owns site procedure.
Individual rollout and timing: rollout.md. No package/profile rollback or format
migration is introduced. Profile recovery stays forward-only.

## Deployed ownership and acceptance

System jobb3b7277b-9384-4938-8f72-2ff3661b2cd0 and profile job
414ed9ee-3059-4677-9564-3cf11109f8ee succeeded. Reservation
75f8a0ac-59c5-43e4-8703-31f4e32b015c remainsdeployed_review for vpsfree:aitherdev.
Selected application/nix/store/hycsrx1zywpgcv3q7jyavj8rwr0x3154-dev-workspace-0.2.0.
System/profile agree on/nix/store/hhhbcsinndg1z08r50a6xba7fwymgr9x-nixos-system-aitherdev-26.05.20261012.7993f34.
Capabilities, recipe, mappings and CLI options verified; backendHTTP200 and TLS
frontendHTTP401 without credentials. Owned notifications delivered through the
separate worker. Evidence: live-runtime-acceptance.json/live-coordination-status.json.

## Next action and retained state

User direction “Implement the plan.” authorized the planned rollout, not merging.
Next action is explicit integration direction for these four repository/master
pairs; then refresh/review/check only changes actually required by moved bases.
Preserve reservation, feature refs, sources, artifacts, GC roots and session.
No finish/release, archive, delete or stop was run or authorized. The native root
01a13c21-6660-7c32-a6ed-07b2620940aa remains notification-only; parent owns work.

A Luna/low watcher owned the first full attempt. Subsequent native follow-up was
refused for v2 subagents, so monitoring visibly fell back to parent with bounded
waits; no watcher model was substituted. Unexpected kernels were not built.
Preserve unrelated shared index/files; final checkpoint stages only curated owned
records and excludes raw logs, HTML, transient requests and secret-bearing data.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-integration-performance/
