# Effective early mount selection: source and static receipt


## Current frozen checkpoint: bare target operands

The parent's exact evaluated thirty-fixture batch reached declared/fresh but
failed source/target identity after status0. The retained complete debug trace
shows a bare equality operand `/var/lib/nixos` in generated dispatch while the
early call's quoted target was rewritten. Consequently dispatch missed the
selected callback and fell through the ordinary path. The log target had the
same boundary. Original artifacts remain untouched; `dynamic-scope/` preserves
the prior checkpoint plus copies of shell-debug.log, shell-debug-root and its
fresh/output trace.

Only the shell test changed. Two sed expressions now additionally rewrite the
complete bare operand `= <configured-target> ]` and `= /var/log ]`, emitting a
quoted disposable target. The closing operand boundary prevents `/var` from
matching `/var/log` or other descendants; no blanket ancestor substitution was
added. Existing quoted replacements and every scenario/assertion remain.
`bare-target-correction.patch` records the exact incremental edit. All other
nine frozen technical files, production bytes, guide and empty index remain
unchanged.

All prepared static checks passed again. `rewrite-boundaries/` retains a
static text-only extraction of the actual rewrite function, input/expected/
actual files and results: 96 cases across `/var`, `/var/lib`, `/var/lib/nixos`
and `/var/log`, three quoting forms and near/descendant paths. Only text
transformation ran; no generated callbacks, mount doubles, allocation marker,
Nix or runtime were executed by this member. Parent owns re-execution of the
already evaluated thirty-fixture batch and remaining checks.

Current shell SHA256: `c777c0a922cbcf09a1b2d9858bdeb8dccf15b5adc5859dce6fc82d3d58a73f6e`.
Current full technical patch SHA256: `dfd8efa2ca86ca5b21365036a754193d629fe2e78e8f944a42c448cf63c5e571`.
Bare-target correction patch SHA256: `0ff2a02531498a8bf0ed3ce50bd856cc80c50c31e0d6ebdaaaf101b7401943b6`.

## Prior checkpoint: shell dynamic scope

Parent's corrected normal check completed all three release assertions and
generated the derivation, then failed in its first shell fixture with
`backing: unbound variable`. Derivation:
`/nix/store/1dl0ckzz2ab0dsxwbzd78lsqm25si04y-nixos-container-persistence.drv`.
Bash dynamic scope resolved the command double's `backing` reference to the
adapter's unassigned local `backing`; `source` and `target` also collided.
This failure is in the test harness, not evidence of raw mount failure.

Only `tests/nixos-container-persistence-shell.sh` changed since the effective
options checkpoint. All harness state referenced by command doubles now uses
`fixture_` names. No scenario, operation, assertion or production byte changed.
`dynamic-scope-variable-map.txt` records the ten names. Reversing exactly those
renames yields the pre-correction harness byte-for-byte. All other nine frozen
technical files match the previous hashes; the guide and empty index are
preserved.

`effective-options/` preserves the prior current artifacts, pre-correction
harness and copies of the parent's persistence log/status evidence.
`initial/` still retains the earlier assertion failure checkpoint.
`dynamic-scope-correction.patch` contains this exact variable-only delta.
All prepared parser/formatter/Bash/static Ruby/whitespace checks passed again.
No member Nix evaluation/build, harness execution, runtime, staging, commit or
ref operation occurred. Parent will run the corrected harness against the
already evaluated thirty invocations, then continue remaining checks. The
normal full check remains required after final source/rebase.

Dynamic-scope checkpoint shell SHA256: `c0c02033b6376c9d5001c6aadf302d5cfe1f9d5d83b5cc3a6a6c33139a50934c`.
Dynamic-scope checkpoint full technical patch SHA256: `3aa72517d456473bdd359784013935dd1e96f8d19a66c6206c42dc09afea110d`.
Dynamic-scope correction patch SHA256: `8262cf9c9571808cf615aca83c5050d5a6c5ca758a3950471227e49294972434`.

## Effective-options assertion correction

The parent's initial normal pure check failed at the 25.11 direct-filesystem
assertion before the build's shell phase. Original log/status remain in
`../effective-mounts-quick/`. Its separate successful `direct-probe.json`
reports all adapter/order/source terms true on all three inputs; only the
nonbind option-string term is false. Effective nonbind options are
`x-initrd.mount,defaults,mode=0755`; effective rbind options are
`x-initrd.mount,rbind,ro`. The assertion had searched the requested options
rather than the complete merged string. This is a test expectation correction,
not an observed raw-module failure.

Only three test files changed after the initial freeze: persistence eval,
check and shell. The evaluator now derives both escaped complete option
strings from the effective entries and separately requires the originally
requested tokens. Each shell fixture exports its selected effective options
through a quoted check argument. The shell retains the original required-token
checks and compares the recorded remount options by exact equality with
`remount,<full effective options>`, retaining mount-count and data assertions.
No upstream option marker is hardcoded.

`initial/` preserves the initial receipt, patch, hashes, static logs/templates
and the three pre-correction tests. `effective-options-correction.patch` is
the exact incremental diff. The other seven frozen technical files, including
all four raw modules, are byte-unchanged from `initial/owned-sha256.json`.
The guide remains lead-owned and untouched. The refreshed `technical.patch`
and `owned-sha256.json` describe the current ten-path frozen snapshot.

The prepared static suite passed again: all nine parsers, nixfmt, Bash syntax,
static Ruby syntax, whitespace, empty index and latest-stable equality. No
Nix evaluation/build, shell fixture execution, runtime, hook operation,
staging, commit or ref action was launched by this member. Parent must rerun
the normal full pure check before continuing the remaining verification batch:

```sh
nix build .#checks.x86_64-linux.nixos-container-persistence --no-link --print-build-logs
```

Effective-options checkpoint technical patch SHA256:
`3cb94f7119cc03444554ce1f51233a36a42296ed93e3bf95a9786b2bba44c2f6`.
Incremental correction patch SHA256:
`0f8ec302a5b35209a92ee7782cedad534047dbc93aeef68485b23dcc5f0b9117`.

Implementation is frozen and unstaged on
`f2b1960dc94ed73936b97f961514dbab164bfbe3`, base tree
`28183c576eb408cbf8acefa5f5cd21e7550b68e0`. No refs or index changes.
The lead's separate `docs/containers/nixos.md` diff is preserved and excluded
from this technical patch and hash inventory.

Verified session/current matches the developer binding; both environment
markers are absent. Live roster revision 18 retains implementer0 ready with
gpt-6.1-sol, xhigh and workspace_write. The accepted full design was read,
SHA256 `c80fea979d8fe48c48d98b78a81b21dd8ea596e31d0c45e8eda296abdb1382b9`.
Applicable current workspace procedures and restored product AGENTS/patch
version/history policy were read. No instruction/history changes were made.

## Exact technical inventory

Ten assigned paths changed:

- The four self-contained raw modules at stable/vpsadminos-25.11.nix,
  stable/vpsadminos-26.05.nix, stable/vpsadminos.nix and unstable/vpsadminos.nix
  under os/lib/nixos-container.
- tests/nixos-container-persistence-eval.nix
- tests/nixos-container-persistence-shell.sh
- tests/nixos-container-persistence-check.nix
- tests/fixtures/nixos-persistence-guests.nix
- tests/suite/dist-config/nixos-persistence-upgrade.nix
- tests/nixos-container-modules-eval.nix

`technical.patch` contains only these paths. `owned-sha256.json` records each
exact SHA256. No production inputs, locks, stateVersion, selectors, backend,
host, daemon, API, KB or other technical source changed.

## Causal implementation

The raw modules now select enabled effective non-root early entries covering
/var/lib/nixos or /var/log, including /var, /var/lib and direct filesystem
declarations. They use the effective device/type/options/dependencies after
module merging. Bind/rbind classification uses option tokens.

Finite required membership is keyed by mountPoint using genericClosure and
the pinned utils.fsBefore relation. It adds transitive predecessors only to
the checked callback membership; the existing upstream earlyMountScript still
owns ordering, cycles and the single execution sequence. No sorter, scheduler,
phase or replay was introduced.

Selected binds prepare only absent directories, preserve live directory
identity and existing metadata, and check configured mount/remount results.
Required predecessor binds require existing directory sources and do not
initialize them. Selected non-bind filesystems and non-bind predecessors check
type/options/operation and exact mountpoint without directory device checks.
All required failures explicitly exit the activation parent before users,
including failed remounts at still-present mountpoints. Matching binds retain
their configured remount path; conflicting binds are not replaced or stacked.

The unchanged recursive helper explicitly creates each absent level as 0755.
There is no owner/mode repair, allocation/map change or deferred metadata phase.
Ordinary callbacks, full promotion, legacy backend guard, priority90,
dry/mkForce and standalone behavior retain their existing contracts.

## Tests prepared, not executed

The normal pure check is retained. Evaluation assertions cover actual pinned
25.11, 26.05 and unstable, ancestor-only persistence without exact state/log
entries, direct bind/nonbind and rbind, effective source/type/options/depends,
disabled and three near-prefix controls, root-only behavior, transitive and
explicit prerequisites, source-before-real-allocator, source-once, global order
and cycle reporting, ordinary/backend exact baseline equality, dry omission,
guest mkForce, standalone copying and latest-stable equality.

The shell gate consumes thirty release/layout fixtures: ten layouts on each
of the three inputs. Layout-aware command doubles cover exact/ancestor binds,
direct bind/rbind/nonbind, declared bind/filesystem backing, transitive and
explicit dependencies, and an unrelated callback that may fail without making
allocation fatal. Cases preserve restrictive existing metadata and payload,
check 0755 missing parents, matching remount options/no stacking, wrong live
sources/results, absent backing, still-present failed required remount,
non-directory/dangling paths and injected dirname/mkdir/mountpoint errors.
The nonbind positive uses a regular-file device token, so applying directory
preparation/identity to it cannot pass. These markers prove shell control flow
only; no shell case has been executed in this assignment.

The registered suite declares exactly these twelve scripts:

```text
upgrade-25.11
upgrade-26.05
upgrade-unstable
root-backed-26.05
declared-backing-26.05
dependent-mount-26.05
storage-failures-26.05
fresh-26.05
ancestor-var-26.05
ancestor-var-lib-26.05
direct-filesystem-bind-26.05
fresh-ancestor-26.05
```

Fixture layout data supplies actual mount pairs, allocation-state backing,
source directory, expected metadata, optional log backing and absent exact
mountpoints. Ancestor fixtures replace exact state/log declarations. Their
merged early-set absence is asserted during generation construction. Direct
filesystem and all three nonbind controls assert no exact systemd state/log
entries. As the lead requested, nonbind controls force systemd.mounts=[] and
use only direct fileSystems /var/log while the healthy live allocation-state
mount remains available.

Adoption still changes only compatibility source at the old-to-new boundary,
with dynamic accounts, unchanged inputs/stateVersion22.11/storage and no old
restart. Native bounded store copying, profile seeding, /nix0755 setup and
the failure-only readiness wrapper are unchanged. Snapshots check both live
IDs and visible/backing maps; actual state-directory identity; declared mount
identity/options/count1; zero exact state/log mounts for ancestor layouts;
machine-id, payload checksum/owner; source metadata/inode; and explicit payload
directory account ownership/mode0750.

Custom exact state sources are pre-provisioned before boot/accounts/data as
numeric42:43/mode0710 solely to exercise preservation of existing directory
metadata; this does not set either dynamic account's IDs. Ancestor /var and
/var/lib sources are provisioned root:root0755 so service traversal is healthy.
Fresh exact/ancestor sources remain absent until candidate initialization,
explicitly expect root:root0755 despite the configured0710 request, and retain
that metadata through all later identity/data assertions. This is initial
fixture provisioning, not changing saved guest content.

Storage-failures retains its real allocator/complete trace positive control,
adds a direct tmpfs log activation control before real Perl allocation, and
adds ancestor bind/conflict, direct nonbind mount/remount and required backing
remount failures. The required-remount fault uses an invalid tmpfs size and
proves its mountpoint remains present afterward. Negatives retain explicit
exit1, no executed real allocator, unchanged passwd/group/maps/payload and
healthy snapshots outside their private mount namespace. No acceptance check
was relaxed.

## Static evidence and remaining checks

All approved static checks passed: nine Nix parsers, prepared nixfmt --check,
Bash syntax for the shell test and extracted helper/store/readiness fragments,
prepared Ruby -c on the combined static suite template, whitespace, empty index
and latest-stable byte equality. Exact commands/statuses are in
`static-checks.log`/`static-checks.json`. The static Ruby template includes all
conditional bodies with inert Nix placeholders. The helper template omits only
generated tuple-dispatch rows. Neither is an evaluated final script.

`prepare.py` additionally proves identical persistence blocks in all four raw
files, raw content outside that block unchanged, original promotion/ordinary
fallback/recursive helper unchanged, native store/profile and readiness code
unchanged, and selector mock changed only by its inert boot.specialFileSystems
field. `source-comparison.txt` records the results.

No Nix evaluation/build, shell test execution, VM/runtime, hook batch,
staging/commit/ref/push or roster/lifecycle action was launched. Actual option
merging, generated scripts and runtime remain pending parent verification;
this receipt makes no upgrade acceptance claim. No material design deviation
was needed. The lead owns prose, history reconstruction, hooks and final review.

Parent-owned normal dependent commands, through a fresh watcher:

```sh
nix build .#checks.x86_64-linux.nixos-container-persistence --no-link --print-build-logs
nix develop --profile result/config-imports-dev-shell --command bash tests/nixos-container-eval.sh
./test-runner.sh ls 'dist-config/nixos-persistence-upgrade*'
nix develop --profile result/config-imports-dev-shell --command overcommit --run
```

Optional exact export for evaluated snippets, assertions and all twelve normal
suite scripts (including the source contracts needed for KB reconciliation):

```sh
nix develop --profile result/config-imports-dev-shell --command nix eval --impure --json --file /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/persistence-effective-mounts-static/exports.nix
```

The export was parsed/formatted only. It is a session artifact, not another
product runner. Parent final committed-head template checks, independent review
and authorized twelve-script/image runtime gates remain in the accepted design.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-12-streamline-vpsadminos-config-imports/
