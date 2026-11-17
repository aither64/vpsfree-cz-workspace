# Stable kernel update integration handoff

Configuration remote `master` now contains `15e3b9af90276e41d19e6a33477add58e5f9a8c9`.
All three requested channels (`staging`, `os-staging`, `production`) pin OS
`f33f5fd1`, selecting stable kernel 6.12.118. Full graph/source/inventory checks
and [independent history review](review-c4.md) passed. Normal fast-forward,
SSH push and fresh remote proof succeeded; merge claim released and verified.
No machines deployed. [Configuration receipt](C4-evidence.md).

vpsadminos is merged into remote `staging` at
`f33f5fd10b53232b5670862f832f4ec5ea835e84`. Fast-forward, normal hooks/SSH push
and fresh remote verification succeeded; the repository merge claim is released.
The dynamic skill/process and stable 6.12.118 entry are now on staging.

Linux is never merged for this workflow. Its reviewed/tested source is published
on `vpsadminos-6.12.118` at
`3bba27296b6f4f4a2b1568d65cea6037368f229b`; all 50 original patches are preserved
unchanged. Dated/recovery branches retained, no downstream tag/default/floating
alias change. The OS pins the full source SHA and archive-byte hash.

Main CI on original OS ba7e99b passed build/cache and 110 tests with zero unexpected
results, including NFS cancellation, boot, module loading and both ZFS modes.
A clean patch-equivalent rebase over disjoint exporter dependencies and the
user-requested publication instructions retain the exact kernel/ZFS/input scope;
new composed OS closure is not called the previously tested exact head. New
[staging CI44167132711](https://github.com/vpsfreecz/vpsadminos/actions/runs/44167132711)
failed on exact `f33f5fd1`: build/cache passed, then GitHub lost
communication with the test runner. No assertion failure or completed test log
was uploaded. D5 confirmed workflow/test/kernel/ZFS inputs match the earlier
passing run. I5 runner inspection found an unhandled "Disk quota exceeded" diagnostic
write followed by runner ABRT. Automatic GC later freed 360.3 GiB; service
remains failed. No surviving attempt processes or terminal results were found.
Build passed; current-suite runtime qualification is incomplete. No restart or
rerun was performed. User accepts the earlier passing branch result and explicitly requests leaving
this as-is. No runner recovery, rerun or further investigation remains assigned;
the failed attempt retains its actual result. Both independent source/instruction reviews passed.
Separate old-kernel livepatch qualification failed before producer build on an
unchanged runner evidence path; [diagnosis](qualification-failure.md) retained.

Workspace policy exception is merged into remote `master` at
`9610ea74a70d4b9b9d0f2d9296ea4908c0d4725b` after explicit approval. Its three-file
commit passed checks and [D3 review](review-d3.md); fast-forward/push and fresh
remote proof succeeded, preserving unrelated shared changes. Repository claim
was released and verified. Linux publication replaces Linux default-merge
proof only; other repositories and lifecycle/recovery safeguards remain intact.

No deployment, archive/delete/stop or runtime/lifecycle workaround authorized.
Session remains active/open. Original README link retained; no unrelated writing
policy change. [Integration receipt](integration.md), [state](state.md),
[verification](verification.md), [catalog inputs](catalog-evidence.md),
[full Linux correspondence](linux-port.md), [review packet](review-packet.md).

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-17-stable-kernel-update/
