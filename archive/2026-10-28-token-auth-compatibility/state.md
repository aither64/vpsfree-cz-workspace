---
lifecycle: archived
---
# Go token-auth documentation compatibility

Complete: fix merged to HaveAPI master, backported to the supported 0.31 line,
and published as [HaveAPI 0.31.2](https://github.com/vpsfreecz/haveapi/releases/tag/v0.31.2).
All reviews/checks/publication/destination verification passed. No remaining work
or blockers. Session remains open; no archive/delete/stop/cleanup action requested
or performed. No infrastructure deployment or downstream pin update was in scope.

## Phase checklist

- [x] Verified exact session identity and retained team
- [x] Architect diagnosis/design and compatibility brief
- [x] Fix and real JSON-boundary regression committed, quick checks passed
- [x] Independent complete master review and broader verification
- [x] Explicitly authorized master fast-forward integration
- [x] Provenance-preserving 0.31 backport and separate 0.31.2 metadata
- [x] Independent complete release review and all 11 candidate CI workflows
- [x] Release-branch integration and annotated tag, remote proofs
- [x] Tagged build, retained artifact inspection and protected publication
- [x] Public registry hashes, GitHub assets, PHP mirror and Packagist verified

## Exact branches and release

| Registration | Feature branch | Initial base | Final head | Verified remote target |
| --- | --- | --- | --- | --- |
| haveapi | 2026-10-28-token-auth-compatibility | 2fc2b8f86c71a6062434bb60a24e174b20c1a520 | 2f5156262baaf137800c17a9321e617c2b5df1d5 | master same exact head |
| haveapi-0-31 | 2026-10-28-token-auth-compatibility-0.31 | d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42 | 819bba5110e089465535ecd71ca2eb37a7d39caa | haveapi-0.31 same exact head |

Canonical repository git@github.com:vpsfreecz/haveapi.git; clean feature worktrees
under worktrees/2026-10-28-token-auth-compatibility/{haveapi,haveapi-0-31}.
Comparisons captured before each integration. Branches retained.
Annotated v0.31.2 object 815c033be8cfca22822d0b2f80c022e959c5d0c4 peels to
819bba5110e089465535ecd71ca2eb37a7d39caa. Master source cherry-picked as
5a016f080bf39c184f71f6b15f904fc165448d6f; range-diff differs only by provenance
trailer. Source fix one logical commit; release one source plus one metadata
commit. No obsolete history, repeated updates or migrations.

User's initial task explicitly authorized HaveAPI master integration, then 0.31
backport and patch publication. Protected publication approved only after exact
tag artifact verification; no separate infrastructure deployment authorization
was inferred. No state/protocol/schema/SDK-runtime changes; ordinary package
upgrade/rollback safe. Server and optional Go generator retain existing matching
version requirement.

## Acceptance evidence and owners

Architect0 owned [design.md](design.md); implementer0 owned code/regressions,
backport, metadata, quick checks/hooks and commits. Lead accepted scope, wrote
release prose with user-facing writing skills, coordinated independent review,
verified integration/publication and maintained records. Other implementers
remained available; narrow shared-file scope used one executor.

Regression red established original warning after actual saved String/live Symbol
assertions. Fixed Go specs 77/0 on master and backport; real mounted standalone
profile checks passed, covering actual JSON-copy boundary. Tests cover String/
Symbol pairs, separate header/query drift, unsupported scalars and missing
providers/descriptors. Broader server adapter/profile checks 30/0. Lint and all
declared hooks passed without bypass. All 10 local external dependency graphs
unchanged by make version.

Same retained independent reviewer0, thread 01a1819c-2087-7e82-ba00-70dedf8cdf0d,
gpt-6.1-sol/xhigh/read_only, no fallback or overrides. Conservative High risk for
auth metadata/publication; all four mandatory lanes. Both reviews no findings,
explicit clean whole-history/no-migrations/no-repeated-stream conclusions:
[master review](review-master.md), [release review](review-release.md).

Master CI: Go 40658113568, performance 40658113525, lint 40658113520,
i18n 40658113538 passed. Release candidate all 11 workflows passed at 819bba51,
including all-component build 40660354757 and performance 40660354784.
Tagged workflow [40661462796](https://github.com/vpsfreecz/haveapi/actions/runs/40661462796)
and release-branch build 40661462440 passed. Artifact 12804711465,
release-40661462796; native manifest/package verifier passed, 11 files/12 tools/
10 locks. Manifest SHA256 4ba5e7dba199b1d92d28f23f9d080b4331adacf39fb9d398838a99733ce1b8b9.
Protected approval deployment 7381398498; publication completed 09:20:15 UTC.

All five RubyGems identities/SHA256, npm integrity, both PyPI file hashes and all
12 GitHub release asset digests match retained artifacts. PHP master/tag
52cf471406593edd42db32a6b61156522318dac9 records exact HaveAPI source;
Packagist 0.31.2 indexes that same source/dist reference. See
[release receipt](release-receipt.md) and [implementation report](implementation.md).
No live token request needed; actual request authentication unchanged.

Both short merge claims 0a36a19c-b210-428e-abfc-c195c6b22fbc and
d3a67997-bcf8-436b-ac9c-5f29a07af4db released, resulting states verified.
No machine reservations, unfinished mutations or watchers. Temporary clean merge
checkouts retained; no session cleanup invoked. Initial plan commit 4cb9ebb37;
subsequent records consolidated locally under normal tracking-commit cadence.
Reusable setup lesson: notes/haveapi/2026-10-28-hook-and-session-shell-boundaries.md.

Next action: use matching 0.31.2 packages in consumers when ready; no action
remains in this authorized task.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-token-auth-compatibility/
