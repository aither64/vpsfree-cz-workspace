# Complete retained node24 hard-lockup search

## Status and scope

**Complete for all 181 identified retained node24 files through the fixed
snapshot cutoff: zero hard-lockup mentions or detections.** All
89,603,613,857 bytes were searched successfully in 402 seconds (6m42s), at about
222.89 MB/s. The 19 matched lines are boot/version labels, not hard-lockup
reports. No same-boot recovery episode exists to classify in this corpus.

The user explicitly requested every retained node24 log, superseding the earlier
cluster sampling budget. This package searches node24 alone and leaves
panic/watchdog policy unchanged. Zero forwarded matches cannot establish that
no hard lockup occurred, or that changing panic policy has no operational risk.

The session identity, both environment markers and same-session roster were
verified before this work. The retained workspace AGENTS, session,
documentation and verification guidance applies. Production access is read-only
as `root@log.int.prg.vpsfree.cz`; no trust, service, configuration, source, ref,
workload or lifecycle mutation is authorized or performed. One sequential
collector runs at low CPU and I/O priority. No second remote scanner is used.

## Corpus discovery and fixed cutoff

Named-host/IP discovery under `/var/log/remote/` to depth six found only
`/var/log/remote/cz.vpsfree/nodes/prg/node24`. DNS resolves the supplied hostname
to `172.16.0.34`; no directory for that IP or alternate node24 spelling was
found, and the parent node hierarchy contains no symlink aliases. No additional
relocated/alias path was identified. This cannot discover an undocumented alias
whose name has no known relation to node24; no unrelated host is treated as an
alias without evidence.

The node24 directory contains **181 regular, uncompressed files**: 180 daily
rotations and the current `log`. It contains no legacy-named, nested,
compressed or nonregular entry. The manifest records magic-based compression
classification in addition to names.

[Snapshot manifest](node24-hardlockup-manifest.tsv) was recorded at epoch
`1792523256` (2026-10-20 21:07:36 CEST). It contains each file's device, inode,
byte size, modification/change times, first content timestamp, final content
timestamp within its byte cutoff, trailing-newline status, compression and path.

- Total snapshot size: **89,603,613,857 bytes (83.450 GiB)**.
- Actual retained content begins **2026-04-23 00:00:01.261611 CEST**.
- Current prefix ends **2026-10-20 21:07:36.802428 CEST**.
- Current file cutoff: **359,236,720 bytes**, device 74, inode 204420. It ends
  with a complete newline at that cutoff.
- Largest retained file: 2,669,968,761 bytes.
- The 180 rotation suffixes run from 20260424 through 20261020 without a
  missing calendar date; actual first/last content timestamps, rather than
  suffixes alone, define the retained time span above.

The current log can continue to grow, but later appends are outside the fixed
search. Every input was read only through its manifest size. The collector
recorded pre/post device, inode, size, mtime and ctime and checked for a
missing/replaced or truncated file. Final reconciliation accounted for every
manifest row, verified all immutable rotations, and found no mismatch.

## Final coverage receipt and directory reconciliation

The [coverage receipt](node24-hardlockup-coverage-receipt.json) records:

| Check | Result |
| --- | --- |
| Manifest rows / distinct successful completions | 181 / 181 |
| Completed snapshot bytes | 89,603,613,857 |
| Server elapsed time | 402 seconds |
| Broad hard-lockup mentions / detector episodes | 0 / 0 |
| Matched boot/version label records | 19 |
| Grep status 0 / status 1 | 5 files / 176 files |
| Timeout, retry, read/identity/metadata error or partial file | None |
| New / missing paths in final directory inventory | 0 / 0 |
| Immutable rotations changed | 0 of 180 |

[Final inventory](node24-hardlockup-final-inventory.tsv), recorded at epoch
`1792523743` (2026-10-20 21:15:43 CEST), contains the same 181 paths. Every
rotation's device, inode, size, mtime and ctime still matches its original
manifest and both per-file observations. The current log remains device 74,
inode 204420 and grew from 359,236,720 to 361,554,913 bytes. Its
**2,318,193 post-cutoff append bytes are unsearched** and do not alter the fixed
snapshot coverage claim. No new file/rotation boundary appeared.

The exact covered content interval is April 23 00:00:01.261611 through
October 20 21:07:36.802428 CEST. Pre-retention records, events never forwarded,
unknown undocumented aliases, and later appends remain outside that claim.
The lead reported independent local corroboration of the 181-file/zero-mention
result by implementer2; no artificial episode classification was requested.

## Search procedure and evidence

The [collector output](node24-hardlockup-search-output.txt) retains source-labeled
matches and per-file begin/end status, elapsed time and identity observations.
The same byte pass collects kernel boot/version labels to support later
episode chronology. The actual search expression is case-insensitive and broad
enough to retain configuration/detector mentions for classification:

```sh
timeout 25s nice -n 15 ionice -c 3 bash -o pipefail -c \
  'head -c "$1" "$2" | env LC_ALL=C grep -aHnEi --label="$2" "$3"' \
  node24scan "$snapshot_bytes" "$file" \
  'hard[ _-]*lockup|Linux version |kernel input vpsadminos=|kernel vpsAdminOS .*with kernel'
```

Status 0 means at least one broad mention or boot label, not necessarily a hard
lockup. Status 1 means neither class matched. A successful full byte read with
status 0 or 1 is required for every retained file; pipeline errors and timeouts
are distinct failures. All hard-lockup mentions must be retained and classified;
the scan continues after detections so it can account for the complete corpus.
Soft lockups, RCU stalls, hung tasks and configuration mentions are not counted
as hard-lockup detections.

All matched records are retained separately in
[node24-hardlockup-matches.txt](node24-hardlockup-matches.txt). The completed
6m42s pass was within the initial 6–8 minute estimate. Files with status 0
matched boot/version labels; none matched the hard-lockup expression. No file
needed a rerun, and no additional remote scanner was launched.

## Episode analysis standard

For each detection, retain exact host/time/CPU, kernel version and available
stack. Compare the boot before and after it, account for replayed messages,
and inspect bounded same-boot control/kernel chronology. Later logging by other
CPUs is only continued activity; it does not prove that the reported CPU
recovered. Fresh reports for the same CPU may be stronger evidence only after
the platform owner checks the actual kernel's warned-flag state machine and
excludes hotplug, watchdog toggles/reinitialization and replay.

Implementer2 independently classifies locally extracted episodes; the architect
owns confidence/synthesis. No candidate was found in this full node24 search,
so no source-directed episode context or recovery inference is required.
Historical cluster evidence from another node is recorded
separately in [cluster-hardlockup-history.md](cluster-hardlockup-history.md).

The retained node24 history therefore provides no logged example of either a
fatal or self-recovered hard-lockup detection. It cannot quantify how often an
unlogged future detection might recover, or certify that enabling panic is
safe. The user is considering a node24-only policy trial; no setting was changed
or test executed by this investigation.
