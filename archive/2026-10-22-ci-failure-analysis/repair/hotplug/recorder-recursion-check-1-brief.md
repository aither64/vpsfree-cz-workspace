# Recorder recursion completeness: source-only packet

The lead selected the source correction in design.md, “Selected recorder
program-recursion completeness correction”. This package is prepared for
inspection and separate native-check selection. No new native C syntax,
compile, mock binary, package, CLI or BPF operation has run.

## Frozen source and check files

| File | SHA256 |
| --- | --- |
| `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos/tests/suite/kernel/livepatch-6.12.95/hotplug-recorder.c` | `55a154cc791c52abc487e036df66c901096031f4e415d4545697979816c3f1a3` |
| `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos/docs/os/testing.md` | `e7d938bedf4371819f5e68fd47a1516b1d16faa956d387ff67bac6f0a7aa89dd` |
| `repair/hotplug/shutdown-check.c` | `e2c44086c1fecc6d51d81d1c45ebb939a78b942c9e74ac1c42a54f38e5a9c3ab` |
| `repair/hotplug/pre-recursion-shutdown.inc` | `64101d60fb2a56fa67f853ba3170b46f64f7dc9304a63a6f4b467e859dc72a97` |
| `repair/hotplug/old-shutdown.inc` | `3ee25442fb60badaabfe8a733fe673db647f8efcd2b767fe69f36c5923a616b2` |
| `repair/hotplug/run-recursion-check-1.sh` | `dd2c3ac72cd574bd8ddedb1961cd24f001dfcb743c3300835307799231a45e58` |

Original accepted C4bf11e25/docs a5fddc49, checker cba46a46, old include3ee25442
and old native script81d83188 have exact mode-preserving original copies in
recursion-check-1-preparation/. The inventory also records all existing root
session scripts/packets, old check raw/evidence, BPF/header/Nix/qualification.
No owner0 packet, first-seven history/source, monitor helper or Git action changed.
The only mutated originals are shipping C, existing diagnostics docs section
and the session actual-C checker. New session evidence includes one exact
pre-recursion helper extraction and one proposed native-check script.

## Source behavior

Keep QUERY before attachment; disable; GLOBAL1; existing live perf-link missed
snapshots; destroy/null every perf/raw link; GLOBAL2. Inside the successful
stable phase, before object close, the new helper enumerates all object programs
through existing owned descriptors. Expected perf/raw family counts come from
the same attachment-array counts passed to shutdown (eleven/four in this fixture),
with no second name registry. Empty, partial, extra or invalid-family coverage
fails. No unloaded/invalid FD is silently skipped as success.

Each request zero-initializes bpf_prog_info, supplies its full capacity and
requires native API success, returned length covering the END of recursion_misses
without exceeding supplied capacity, nonzero native program ID, and native type
matching that program's libbpf type and the expected kprobe/raw family. A
field-end prefix can pass; unsupported zero-filled tails cannot. Names identify
diagnostics only, including truncated native names. A failed/nonzero counter
marks failure and later program reads, final ring/maps/bytes and owned cleanup
still run. Failed grace/destruction yields no stable counter query. Abort and
prior failure remain monotonic.

New program=<name> id=<id> recursion_misses=<count> evidence has explicit
whole-loaded-program-lifetime/all-CPU scope. It conservatively includes setup,
disabled-window and non-CPU127 suppression with no baseline subtraction.
Existing probe=<name> missed=<count> and capture-cutoff scope are unchanged.
Docs add only the corresponding paragraph; original prefix and full suffix
remain byte-identical. No event ABI, BPF/header/recipe/qualification, pins,
attachment scheme, limits, decoder, persistence, migration or fleet coordination
changes. Old binaries cannot establish this new completeness obligation.

## Prepared controlled regression

The existing checker includes the actual corrected C behind fake native
boundaries. All original41 cases remain, with extra assertions that failed
barriers/destruction never query stable program counters. The32 added prepared
cases make73 total: each of15 raw/perf counters independently nonzero while link
misses/maps/bytes agree; late raw and perf increments at grace2; empty/missing/
extra programs; invalid FD, API failure, missing ID, wrong native type in either
family, invalid libbpf family; exact field-end success, short-by-one/zero/oversize
length failure. Every other read and owned cleanup must continue. Fakes assert
zero-initialized request bytes, all15 unique reads before object close, preserved
actual cleanup and final map/byte behavior. The long full name differs from the
fake kernel-truncated name without forcing failure.

Two cases call the accepted two-grace helper extracted verbatim except its
function name from preserved4bf11 source: zero link losses/maps/bytes can return
success despite a late raw or perf program miss. The preexisting original
9bea shutdown-race fixture is retained independently. These cases are PREPARED,
not executed. Userspace fakes do not prove kernel barriers or real loss-free BPF.

## Exact proposed native operation, not selected here

One fresh Luna/low full-access/never utility, only after lead selection:

```sh
DEV_SESSION_SLUG=2026-10-22-ci-failure-analysis \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
/run/current-system/sw/bin/systemd-run --user --scope \
  --unit=ci-failure-hotplug-recursion-check-1 \
  --property=MemoryMax=1073741824 --property=MemorySwapMax=0 \
  --property=TasksMax=32 --property=CPUQuota=200% \
  /nix/store/bhv6xyvqw6gjs3j488gi1z6wdv18bdpa-coreutils-9.11/bin/timeout \
  --signal=TERM --kill-after=5s 120s \
  /nix/store/jnyfsf2mp08d1xyz2m72ic2vz2kcx0sd-bash-5.3p9/bin/bash \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-ci-failure-analysis/repair/hotplug/run-recursion-check-1.sh
```

No trailing argument. Source/check/header/include/tool hashes are checked before
work. Exact cached GCC15.3 wrapper dy6j7267... and libbpf1.7 headers l0j5869...
are reused; no Nix evaluation/substitution/build or dependency installation.
The script performs -fsyntax-only on shipping C, compiles only the session check
with function/data sections and linker GC, and runs only that fake binary.
Uncalled loader code is discarded; no real libbpf is linked for the check.
No BPF object compilation/load/verifier/attach/probe or runtime experiment.

Fresh required-absent attempt:
/tmp/ci-failure-analysis-2026-10-22/hotplug/recursion-check-1, child tmp/.
No root changes. Expected native scratch/output growth below8MiB;128MiB physical
ceiling covers temporary/output coexistence and receipts, with independent
40GiB free floor and128MiB admission margin. Per-receipt cap1MiB for syntax,
compile and check logs, aggregate output/receipt forecast below4MiB. FSIZE is
unlimited and core0. Scope hard1GiB/noSwap/CPUQuota200%/TasksMax32, no daemon
builder; outer120+5s. Expected duration a few seconds, not a hard completion
claim. Script checks floor/physical between phases; a selected watcher must
sample real st_blocks/scope/children/sharedfree and cancel the authenticated own
operation on breach, retaining limits/gaps. Sampling may miss peaks/overshoot.
No helper framework or monitor change is proposed.

After execution the utility must retain native exit/elapsed, log statuses,
binary/source hashes, native scope/PID-birth identities and bounded canonical
own-reference effects proof with protected/unreadable/FD/truncation gaps, on
either outcome. No retry, foreign signal, cleanup or inference from parent exit.
Unknown effects retain watcher/roots/raw for lead-directed reconciliation.

## Preparation checks and current limits

Bash-n for the proposed script, Python AST and static source/scope proof passed.
The scope proof checks326 frozen byte/mode identities unchanged, the only three
mutated originals, existing41-case body preservation, exact baseline extraction,
original docs prefix/full suffix, and shipping C equality after removing only
stddef include/new helper/one stable call. Cached tool/header hashes match;
none were invoked. New attempt is absent; no process/capacity probe was used.
The static-check allowed-path bookkeeping initially mixed relative/absolute
checker spellings; that checker-only comparison was corrected, then the full
proof passed. No C or mock execution occurred.

Previous41 native cases and packagezm13->kpkc/build4 are historical evidence for
C4bf11, not validation of the new C. New native checks, exact new derivation and
packaged compile/CLI, owner8 fold/messages, affected review, CAS/publication and
all runtime remain separately held. Build4 guard stays INCOMPLETE with scanner
limits; no old evidence is upgraded. First-seven/owner0 history remains frozen.
All roots, old scripts, raw attempts and original sources remain retained.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-ci-failure-analysis/
