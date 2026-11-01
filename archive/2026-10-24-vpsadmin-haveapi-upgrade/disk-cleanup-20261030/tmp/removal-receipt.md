# Bounded cleanup correction and removal

Removed only `/tmp/vpsadmin-haveapi-upgrade-kb-checks/rust-consumer/target`: **198,250,496 allocated bytes**
(189.07 MiB), measured immediately before deletion with
`du -sx --block-size=1` and independently matched by unique device/inode
`st_blocks * 512`. No regular hardlinks pointed outside this target.

The raw per-path sum was 209,715,200 bytes. It counted
11,464,704 bytes twice through hardlinks.
The prior209,711,104-byte walk also omitted the target directory's4,096 bytes.
These explain the earlier discrepancy; the consistent removed allocation is
198,250,496 bytes.

The lead accepted the clarified owner-chain rule. Exact old commands and final
synchronous exit0 prove ownership/completion; session records show no later
known reuse, detached owner, pending or recovery dependency. Rechecked stable
real path/device/inode, no symlinks/special files/mounts/loop backing, exact size
and source/manifest siblings. Standard fd-safe deletion completed; target is
absent and all four parent source/manifest entries retain inodes and hashes.
Parent rust-consumer, rust-shell, source inputs, all receipts and every protected
path/root remain. No process was stopped or privilege elevated.

The [original zero-removal receipt](receipt.md) and its unrelated inaccessible
interface findings are preserved honestly. This later [accepted bounded disposition](removal-result.json)
supersedes that refusal only for this completed private compiler cache.
No global process rescan was performed.

DF available: 49,467,441,152 → 49,665,601,536 bytes (net +198,160,384). This is an
observed filesystem delta under concurrent activity, separate from our measured
198,250,496-byte removal. No further cleanup/process remains active and the
session stays open.
