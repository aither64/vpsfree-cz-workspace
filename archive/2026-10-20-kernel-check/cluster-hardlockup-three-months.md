# Cluster hard-lockup history: three calendar months

Status: collection, final metadata reconciliation and implementer2's independent
local reconciliation complete.

**No forwarded hard-lockup detection was found in the available retained node
logs for the stated window and coverage.** All **1,221 selected files /
557,248,915,782 bytes** completed successfully in **2,344 seconds** (39 min 4 s;
237.73 MB/s). The inclusive hard-mention count is **zero**. This does not prove
that no machine stalled or that enabling panic would be safe.

Scope: all identified cluster node directories on `root@log.int.prg.vpsfree.cz`,
records dated **2026-07-20T00:00:00+02:00 through
2026-10-20T23:08:52+02:00**, inclusive. Snapshot metadata collection began at
that fixed upper timestamp and finished at 23:08:58 CEST. Each manifest entry
has its own byte extent captured before endpoint reads; later appends are outside
those extents, and records after the fixed timestamp are excluded locally.

## Inventory and selection

The inventory accounts for 3,477 regular files across 26 site/host directories
under `/var/log/remote/cz.vpsfree/nodes`. Every first/last captured timestamp
parsed; all captured extents ended with a newline. Magic/header inspection found
plain timestamp-prefixed text throughout, without compressed files, symlinks or
unexpected entries in this hierarchy. Three legacy names were inventoried:
`stg/node1/log.3`, `stg/node1/log-cisty`, `prg/node23/log.3`; their actual bounds
precede the requested window.

Actual first/last record timestamps, with a conservative fallback for inverted
bounds, unparseable timestamps or recent-mtime/old-content discrepancies, select
**1,221 files / 557,248,915,782 bytes** (557.249 decimal GB, 519 GiB). This includes
boundary rotations; selection does not rely on suffix dates. There were no
unparseable or inverted endpoints requiring fallback. Files ending before the
window and with old modification times are excluded rather than scanning all
1.186 TB of retention. Endpoint observations do not prove strict ordering of
every record in excluded historical files; arbitrary interior timestamp jumps
in such files cannot be excluded without a larger historical read.

Thirteen sources have selected records: `brq/node5`, `brq/node6`, `pgnd/node1`,
`prg/backuper2`, `prg/node19` through `prg/node25`, `stg/node1`, `stg/node2`.
Each has 94 selected files except `prg/backuper2` (93). Full per-host observed
retention and selected endpoint bounds are in the linked per-host coverage TSV.

Thirteen directories contain no retained records overlapping this window:
`brq/node2`, `brq/node4`, `pgnd/node2`, `prg/backuper`, `prg/nasbox`,
`prg/node1`, `prg/node7`, `prg/node8`, `prg/node9`, `prg/node10`, `prg/node11`,
`prg/node13`, `prg/node15`. These are retention gaps, not evidence of no events
on those machines during these three months.

Discovery covered the entire remote directory hierarchy and symlinks through
depth six. No additional node-name/relocated directory or symlink alias was
identified. The running collector service invokes rsyslog with a template
`/var/log/remote/%HOSTNAME%/log`; its configuration line references and directory
listing are retained. Four IP-named sources have router-style header tags,
`localhost` and `ssh` have their own distinct header identities, and named
machine/container/vpsadmin branches were kept outside the node scope. These
observations do not establish that no historical, undocumented unrelated alias
exists. No unrelated branch received a content scan.

## Collection method

One sequential collector, `nice -n 15 ionice -c 3`, started at 23:10:00 CEST.
Every selected file received a fresh read, including node24; no prior result
was reused. The source was bounded with `head -c <snapshot-bytes> <path>` and
searched with `LC_ALL=C grep -aHnFi --label=<path>` and fixed patterns:

```text
lockup
Linux version 
kernel input vpsadminos=
kernel vpsAdminOS 
```

The literal `lockup` prefilter covers every requested
`hard[ _-]*lockup` spelling, including `hard LOCKUP`, `hardlockup`,
`hard_lockup`, `hard-lockup`, and retains soft-lockup/other mentions for local
classification. Boot/version strings share the same byte pass. Full matching
output is saved without a match-count cap. Local classification normalized
outer timestamp offsets and checked the inclusive window. All matched records
parsed and were in-window; none required an ambiguous/out-of-window disposition.
Some snapshotted current files end at fractional timestamps after 23:08:52.000;
the exact upper time predicate still excludes those records if matched.

The pipeline uses `pipefail`; grep statuses 0 and 1 are valid while head/read
errors remain errors. Each attempt has an interruptible timeout of 30 seconds,
adaptively 60/120/240 seconds if needed. A timed-out partial attempt is not
counted as complete; attempt boundaries allow local de-duplication. Pre/post
device, inode, bytes, mtime and ctime are recorded. Immutable rotations must
match snapshot metadata exactly. Current files must retain device/inode and at
least the snapshotted bytes, permitting append-only growth. The final directory
inventory reconciles replacement, new paths, rotations and appends below.

## Final receipt and classification

The collector ran **23:10:00–23:49:04 CEST**, with 1,221 distinct successful
manifest extents and no pending files. There were 1,222 attempts: the 9,724,380,231
byte `brq/node5/log-20260820` rotation exceeded its initial 30-second timeout
(status 124), then completed in 29 seconds with the 60-second limit. Its metadata
stayed unchanged. The failed partial attempt emitted no matches and contributes
no completed coverage; only the successful attempt is counted. There are no
unresolved timeouts, read errors, identity errors or stderr records. No file was
skipped after a hit.

The full saved match output contains **253 unique source records**, each with a
parseable outer timestamp within the inclusive requested window:

| Classification | Records |
| --- | ---: |
| Boot/version labels | 157 |
| `softlockup_panic=1` boot command-line records | 96 |
| Other `lockup` mentions | 0 |
| `hard[ _-]*lockup` mentions or actual detector reports | 0 |
| Out-of-window or unparseable matched records | 0 |

These are record counts, including replayed/duplicated boot messages at distinct
source positions; they are not boot or episode counts. Configuration text is
not a detector warning. No hard-lockup episode exists in this collected window
to classify for same-boot survival or affected-CPU recovery. The earlier October
2022 staging episode belongs to a separate search outside this window.

Final metadata reinventory ran **23:49:11–23:49:16 CEST**. Both inventories
contain the same **3,477 paths** and 26 host directories, with **no new or missing
path**. All **3,464 noncurrent files** retain device/inode/size/mtime/ctime
exactly, including all **1,208 selected rotations**. All **13 current files**
retain device/inode with increasing size, consistent with append-only growth;
their **263,131,061 appended bytes** are outside the per-file snapshot extents
and were not searched. The detailed metadata receipt lists each current file's
cutoff, append delta and last observed timestamp. No new-file boundary needs
reconciliation. This is metadata verification, not a cryptographic comparison
of the remote file contents. The checksum list authenticates saved local
evidence, not unseen production contents.

Implementer2 independently recalculated file/byte coverage, attempt pairs,
resolved timeout, exact match/disposition equality, source-position uniqueness,
time filtering/classification, final path equality and metadata/appended-byte
totals from these local artifacts. Their final report passes with the same
counts and no discrepancy. They performed no second remote scan.

The result is bounded to identified node paths, the captured byte extents and
the outer record timestamps. Per-host endpoints do not establish uninterrupted
logging or every CPU's execution. Unforwarded events, events after the cutoff,
late-forwarded pre-cutoff records arriving beyond a captured extent, expired
retention, arbitrary interior timestamp jumps in excluded historical files,
and undocumented unrelated aliases remain outside this proof. Inactive
directories provide no three-month observation. No panic-policy conclusion
or production change follows from this negative search.

## Evidence files

- [Full inventory](cluster-three-month-inventory.tsv) and its [reader](cluster-three-month-inventory.pl).
- [Selected manifest](cluster-three-month-manifest.tsv).
- [Per-host coverage](cluster-three-month-host-coverage.tsv).
- [Remote hierarchy](cluster-three-month-hierarchy.txt), [collector routing](cluster-three-month-routing-evidence.txt), and [non-node header observations](cluster-three-month-alias-headers.tsv).
- [Collector script](cluster-three-month-collect.sh), [exact instantiated command](cluster-three-month-remote-command.sh), [search output](cluster-three-month-search-output.txt), and [stderr](cluster-three-month-search-stderr.txt).
- [Per-file completion status](cluster-three-month-status.tsv), [complete matches](cluster-three-month-matches.txt), [timestamp/classification dispositions](cluster-three-month-match-dispositions.jsonl), and [local reconciler](cluster-three-month-reconcile.py).
- [Coverage receipt](cluster-three-month-coverage-receipt.json), [final inventory](cluster-three-month-final-inventory.tsv), [metadata receipt](cluster-three-month-final-metadata-receipt.json), and [local evidence SHA256 checksums](cluster-three-month-evidence-sha256.txt).

The lead owns session state/portal updates and architect0 owns synthesis.
Implementer2 independently reconciled local evidence without another remote
scanner. No configuration, service, trust, kernel, panic policy, source/ref or
session lifecycle change is authorized or performed by this investigation.

Session portal: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/>.
