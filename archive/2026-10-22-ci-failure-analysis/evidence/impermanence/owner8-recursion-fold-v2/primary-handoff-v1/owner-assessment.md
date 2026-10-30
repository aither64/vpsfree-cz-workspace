# Primary CAS retained outcome and read-only reconciliation

The intended primary handoff is attained: feature ref/HEAD is exactly
`f74629fa4046089e2c53d0cb0e3ba7ef5b178e82`, tree
`1bbd234662cbe595e781dcba4c0b43c5a839f15e`, parent
`39b6f68f245d6ebddf40a5ffc8e2e9485a9a8a17`. Index entries and worktree match
that tree; all peer bytes/modes/links and other refs are preserved. The native
batch nevertheless exited1 on an incorrect index-byte assertion after CAS.
This is a reconciled mutation outcome, not a successful batch or monitoring
guard. No retry or repair mutation is needed to attain the selected Git state.
Window release and subsequent gates remain the lead's decision.

Session/environment matched before action. Assessment used only retained
bytes, read-only Git with OPTIONAL_LOCKS0/NO_LAZY_FETCH1, complete worktree byte
comparisons and the separately selected single PID stat attempt. No write-tree,
index override, source/script edit, Git mutation, Nix/test/build, broad scan,
live scope/df/du query, signal, rollback, retry or cleanup ran. New evidence is
this assessment, an ordinary copy of current index and the targeted PID receipt.

## Exact failure cause

Full native stream30319B was read, SHA256
`ea5c537379882f6fd8a7497575b1832e11461f67205a4ad3020286ea2ca9492f`.
Retained launcher receipts are scope-command1/log-reader0; final line is
`HANDOFF_EXIT status=1 phase=post-CAS-verification`. The native expected-old CAS
executed at1792802462.417689. Primary symbolic ref, f746/tree1bbd, empty staged
diff, empty worktree diff and empty all-untracked status passed before the
failing compare at1792802462.519681. Later scripted preservation/ref checks did
not run; independent read-only checks below supply their actual conclusions.

I saved `shared-index.staged` before native `write-tree`, then incorrectly
required the later index to remain byte-identical. The failure is explained
by that command's cache-tree materialization, not altered staged content:

| Index | Bytes | SHA256 |
| --- | ---: | --- |
| original before | 279716 | `e9ea5d77e99442aec4ae52038c76a57c2ed418ceffecda32c2dd6a189b86a741` |
| staged, before write-tree | 279572 | `77ce71bb4263062a0b50077be39d14fdcbb06d42937c7bd2a364aab20305d2db` |
| after / current | 279716 | `7ff9f22afaf6d1121b81f00df150116df5f7438176f0232e4051ec1eb6980723` |

Pure in-memory parsing validated all three DIRC/version2 index SHA1 trailers.
All2404 entry records, including paths/stat fields/modes/blob IDs/stages/flags,
are byte-identical staged->after/current through zero-based offset259419.
Their common header/entry-region SHA256 is
`29a20812be929a5237c3e85cefc252501dd194fcf0df98f29b88fd8c06f4dc74`.
Only the TREE extension and consequent final checksum differ. Its header starts
at offset259420. First mismatch, one-based259427, is extension-length byte
0x4e->0x4f:20124->20268B payload. Before/after TREE header bytes are
5452454500004e9c /5452454500004f2c.

Exactly seven invalidated cache-tree nodes (entry count-1, no OID) become valid:
root, docs, docs/os, tests, tests/suite, tests/suite/kernel and
tests/suite/kernel/livepatch-6.12.95. Root now records2404 entries and exact
1bbd2346 tree; unaffected cache-tree nodes are identical. No other extension
exists. A pure in-memory reconstruction from staged index modes/paths/blob IDs
independently hashes to1bbd234662cbe595e781dcba4c0b43c5a839f15e without writing
objects, index or tree. Native read-only ls-files--stage versus final ls-tree
also matches every2404 mode/OID/stage0 entry.

Preserved index mtimes establish the change during the recorded write-tree:
staged1792802461508524533ns; after/current1792802461531524654ns. Native
write-tree starts1792802461.520426 and returns expected tree1792802461.535199;
the current index mtime1.531524654 lies inside that interval and before CAS.
It remains byte/mtime-equal the retained after copy throughout diagnosis.
This exact byte/semantic/time/order evidence accounts for the failed assertion;
no corruption, competing writer or race is inferred. Failed scripts/raw/index
snapshots remain unchanged. [current-primary-index.bin](current-primary-index.bin)
retains ordinary current bytes279716B, SHA7ff9f22a above.

## Completed mutation and preservation

Read-only Git establishes primary symbolic HEAD
`refs/heads/2026-10-22-ci-failure-analysis`, exact f746/tree1bbd/parent39b6,
no staged diff, no worktree diff and empty all-untracked status. Exact feature
reflog's final raw row records old9bea27c93beb22d08c3be2eb481bce4ef57300a6
to newf74629fa4046089e2c53d0cb0e3ba7ef5b178e82 at1792802462+0200.
Only that selected ref differs from saved refs.before; all3537 other refs
remain exact. Existing dated old9bea and old19562 backup refs still resolve to
their literal old objects. Isolated checkout remains clean detached f746.

Current C55a154cc791c52abc487e036df66c901096031f4e415d4545697979816c3f1a3
and docs e7d938bedf4371819f5e68fd47a1516b1d16faa956d387ff67bac6f0a7aa89dd
equal final committed blobs and isolated bytes. All7643 primary regular files
were independently rehashed against retained before/staged/fold manifests;
all9026 path/type/mode/symlink-target records equal current and retained data.
This includes ignored/untracked peer files. No source bytes were written by
CAS or diagnosis. These comparisons are non-atomic reads, not future guarantees.

First7 exact objects/metadata still match retained originals, ending39b6f68f.
Exactly8 owners remain. All8 bodies byte-equal the frozen selected files, packet
7ee808179b9b92f8beb17ef043bcb21cfbdb3f4d58b619eaacbfde9980ebc79a;
owner8 messagebad75411 and previously accepted authors/dates/<=80 widths hold.
Complete846bb->f746 full-index patch is exact
aeaffe319be8d716f78c351597724eda52454671f5a20bbbbfb966c21134ef32;
retained staged9bea->f746 patch002ccfe8 already matched natively before CAS.
The eight-owner/no-migrations/no-repeated-stream history conclusion remains
bound by unchanged first7 and exact selected owner8 delta. No ninth fixup or
new source was introduced. Lead's narrow source-fix disposition is retained;
no independently reviewed-newhead or branch-ready claim is made.

All21 originals in preservation.md remain byte/mode/hash equal; current native
scripts retain acceptedfa44adf3/2ed266db, oldCAS remains obsolete/unchanged.
No new commit/hook run occurred in this operation; prior ordinary hook passes
and unsuppressed preference warnings remain in owner8 assessment. No nontrace
warning occurs here beyond the explicit failed cmp; raw remains authoritative.

## Effects reconciliation and limits

Native stdout genuinely records scopeci-failure-primary-handoff-v1.scope and
InvocationIDa4778c7707b1434e948dfe3b9b4b0a98. Retained post-run scope query0
is not-found/inactive/emptyCG. No actual live launcher/timeout/batch births,
ancestry or independently authenticated InvocationID/canonicalCG/inode tuple
were captured. StdoutID is genuine but cannot supply missing live authority.
No historical identities are invented; monitoring remains **INCOMPLETE**.

Consumed the finalized ONE [scan receipt](utility-run/owner-refscan-result.json),
18852B, SHA256
`80f62fe9cef35f87bdce1523ab0f57ea9342ce6107d643b8043a013338db4afa`.
Read its full code too (SHAf01bda7de61b78f8ac93cdcc6767f6df98f8cd930c494a7e6dc0837a929f208d).
Its operation label incorrectly names recorder-recursion-build-1; actual literal
and canonical references/code target primary-handoff-v1 primary/isolated/admin,
scratch/watch and both handoff script paths. Old TASK/BASE strings are unused
by collection. Raw label/code are preserved, not overwritten or rerun.

The scan reports1521processes/4917FD entries,4661 readable FDs,
0.8609037008136511seconds, no process truncation, four128FD caps.676protected
cwd/root/exe views each,680protected FD directories,256FD-target denials,
canonicalization/process-exit races and truncated128-record gap details remain.
One nonself ambiguous positive is PID2872887/birth1211024721, argv[2]
referencing new scratch, value2652B/SHAaf229641. The receipt does not retain
that argv's content, complete role or ancestor identity; no observer exemption
is justified merely by timing or digest.

Lead selected exactly ONE current targeted attempt, retained in
[targeted-ownref-reconciliation.json](targeted-ownref-reconciliation.json),647B,
SHA256 `81002c91d5b0eef8bdc46b2200f27b93a902fb8cc753d3bfa4dffa45361a5624`.
The exact PID's single stat attempt returned FileNotFoundError/ENOENT.
Attempts:stat1;argv/cwd/root/exe/cgroup/parent-stat/parent-argv/FD all0.
Elapsed0.00008249469101428986s, within5s/1MiB bounds. No retry, signal or
broad scan followed. This is literal current absence, not proof of historical
role, exit cause, descendants or protected effects ending. The historical
positive is preserved; it is not reclassified as an authenticated observer.

Retained trace spans1792802459.244120..1792802462.523313:
3.279193 wall-clock seconds; largest positive adjacent gap0.778402s; one
interleaved adjacent gap-0.000029s. These are trace observations, not monotonic
native-duration/cadence proof. Endpoint positive allocated-root growth is
5951488B: fresh scratch5881856B +watch69632B; commonGit/evidence/primary/
isolated allocated endpoints unchanged. Apparent endpoints are retained too;
commonGit apparent grows138B despite allocated endpoint0. Shared free space
136633495552->136627523584B, decline5971968B, both above40GiB. No new capacity
query ran. No continuous resources, true peaks, exclusive quota or owned df
attribution is established. No cancellation is recorded. Native timer/stream
controls do not repair missing live monitoring or protected views.

The CAS goal is attained and the precise assertion failure reconciled through
read-only evidence. Batch exit1 and monitoring INCOMPLETE remain permanent
facts. No CAS rerun, script fix, source mutation, rollback or cleanup occurred
or is proposed here. Git window remains RESERVED pending lead decision;
publication/discovery/runtime and branch readiness remain held.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/
