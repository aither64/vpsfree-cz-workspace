---
lifecycle: active
---

# Proactive swap removal from 6.12.113

Current phase: **merged into vpsAdminOS staging; user staging validation pending**.

## Phase checklist

- [x] Exact session/team identity verified; final design and initial tracking committed.
- [x] Linux experiment removed; final source published at1dfea587406b7dd79973831d1677fb2418e5e9aa.
- [x] DAMON options/tooling retired, only .113 pin/hash updated; one OS commitca3ff61a3931f0eb524543151d5d78a70f87bfc7.
- [x] Required hooks/source/history/format/byte-hash and final no-build Nix checks passed.
- [x] Independent final review completed; all four Important findings narrowly fixed and directly reconciled, no unresolved in-scope finding.
- [x] Authorized coordinated fast-forward merge to remote staging verified exactca3ff61a.
- [ ] User builds matching kernel/modules/ZFS, boots staging nodes and performs runtime validation. No premerge build/runtime/full-CI gate was required or run.

## Final repositories and ownership

| Repository | Worktree / branch | Final identity and disposition |
| --- | --- | --- |
| linux | worktrees/2026-10-16-proactive-swap-patch-removal/linux; branch2026-10-16-proactive-swap-patch-removal | 1dfea587406b7dd79973831d1677fb2418e5e9aa published, no existing release/default integration |
| vpsadminos | worktrees/2026-10-16-proactive-swap-patch-removal/vpsadminos; same feature branch | ca3ff61a3931f0eb524543151d5d78a70f87bfc7 merged into refs/heads/staging from60f9ed1c153a734880e002b63d6ab7ed5fe87d0e |

Architect0 owned final design/clarifications; implementer0 Linux/provenance/fixes; implementer1 OS/pin/hooks; reviewer0 independent final review (saved Sol/xhigh/read_only); lead accepted/reconciled and coordinated integration. Saved roster settings preserved, no members added/reconfigured. Utility watchers did not join roster.

## Accepted changes and evidence

Six full experimental owners omitted; exact50-commit inherited prefix kept, final5logical suffix/full55upstream series inventoried. Generic iterator, CSS lifetime/early guards, affinity, NFS remain. Ordinary-view ownerv3 preserves nonexperimental reporting corrections; no proactive state/custom quotas/scope restored. Native DAMON/header/admin docs compare upstream-identical. Other kernel/ZFS pins, frozen outputs, ordinary test files and .6.18-specific prose unchanged. No new tests.

Required OS hooks and Nixfmt passed in declared Nix environment (ambient Overcommit signatures differed; no bypass). Native sourcecheckpatch0errors/0warnings227lines and diff/preservation checks passed. Final archive246079556bytes verified Nix+Python and exactroot, SRIsha256-IvyBosmZkpWxAK4Bz0sQ+RBwUQZwN+GtBxwjBY1lAdQ=, owned indirectGCroot retained. Four final .113 default/explicit disabled/enabled configs passed offline/noIFD Nix eval on exactca3ff61a: no failed assertions, expectedURL/SRI/service writes,25packages/186tests discovered. No actual test execution/build/boot/fullCIwait.

See [handoff](handoff.md), [design](design.md), [source inventory](linux-source-inventory.md), [review](review-report.md), [reconciliation](review-reconciliation.md) and [final eval](os-evaluation-revised-final.log). Original review anchors86d54e7/bf9bcb5e remain under dated remote backups; original source11058eb4 untouched.

## Independent review and material limits

HIGH risk/all4lanes, retained reviewer0 Sol/xhigh/read_only. Original final review found four Important ordinary-reporting regressions (v1 unlimited/finite meminfo, finitev2 bounded free, zero-capacity proc/swaps). Implementer folded precisely15add/7del across3files into ordinaryv3; lead directly inspected finaldelta/history/provenance and newOS-only-pin delta, following mandatory narrow-fix policy; architect corroborated design. No automatic full rereview, no new framework/tests. No migrations/repeated pins/obsolete task suffix; unchanged consumed prefix debt explicitly assessed.

Advisory accepted: pre-existing proc/swaps byte/KiB mismatch remains, not introduced by removal. Compilation/linked modules/boot/runtime correctness remain unverified, user-owned. Watcher incidental duplicate evaluation (bothpass) and missing archive raw-log recovery are transparently documented in handoff/result evidence; no source impact or extra rerun.

## Authorization and integration proof

User selected latest6.12.113 only, never-deployed/no compatibility/rollback, remove whole experiment and tooling, no new normal-reclaim tests, quick verification/no fullCIwait, then explicitly chose vpsAdminOS staging and instructed implementing plan. No deployment/reboot/defaultLinux rewrite authorized.

Integration8db9c04d-a44e-488d-9448-bf9d481bbf30, mergejob162fcc38-0fa4-48f5-b343-4b3b7d9a2b84, outcomeapplied/verified/succeeded. Coordinator and independent SSHread prove remote stagingca3ff61a. Handoff eventd1706cc3-86ab-62fb-8128-fc27b1cabf16 generation0 acknowledged by matching root. [Operation receipts](integration/8db9c04d-a44e-488d-9448-bf9d481bbf30/summary.md). No machine reservation/deployment.

## Next action and session

User builds/boots merged staging kernel with matching modules; use storepath/buildidentity to distinguish unchanged6.12.113 version string. Optional existing memory-view v1/v2 and disabled/enabled DAMON smoke checks remain user-owned. Keep source feature/backup refs and worktrees; session remains active/open (Linux source-only publication and staging validation outstanding). No archive/delete/stop/cleanup action authorized.

Initial tracking e9207a9d61f4700619d675297f7c03a12027e13c; coordinator completion tracking672d86ca. Final ownership handoff checkpoint follows.
