# Package D: resolver controls and native boot diagnostics

The initial osctld environment probe stopped before tests; the lead has now
authorized normal declared osctld setup as a verification prerequisite. Its
actual shell uses `/tmp/dev-ruby-gems`, not a checkout-local `.gems`; absence
of the latter did not prove global cache absence. The exact standard command
below is prepared for the root's fresh watcher, with a five-minute initial
budget. D has not launched it. No spec/production edit, check, barrier or thread
exists yet; the stale-snapshot model remains neither confirmed nor refuted.
The initial [probe record](native-lineage.md#exact-e175-shutdown-unit-reproduction-prerequisite-unavailable)
remains historical evidence, not a permanent setup prohibition.



## Declared osctld setup command (pending)

**Prelaunch command below is superseded; do not execute it.** The entire
historical `givmi...-libosctl-native-local` output is now absent, as verified
by the lead. Its old successful receipt remains historical, not a current
binding. The root has launched a first-stage normal osctld setup without that
path; it reports actual bindings and optional native availability. D launches
no parallel setup. If native is unavailable, the selected ordinary continuation
is only `(cd ../libosctl && bundle exec rake compile)` inside the same declared
osctld shell/bundle, followed by loading and hashing the actual checkout
`libosctl/lib/libosctl/native.so`. Current source/output native paths are absent.
No osctld-native compile is needed by the released three spec loading paths.
Setup and prototype remain pending; no application/spec edit has occurred.


Run from the primary worktree's `osctld/` directory. This invokes the actual
`mkRubyBundlerShell` hook, which selects the two locked path inputs, installs
Bundler only if absent, and runs ordinary `bundle install`. It generates the
normal ignored development lock/cache without updating source pins. The
production package lock is a different manifest and is not copied into place.

```sh
nix develop '..#osctld' --max-jobs 0 --builders '' \
  --option allow-import-from-derivation false \
  --command env RUBYLIB=/nix/store/givmi31xrbr231gxnry1xc2ggb5s4imf-libosctl-native-local/lib \
  ruby -rjson -rdigest -rrbconfig -rbundler -e '
    abort "declared Ruby differs from cached native ABI" unless RUBY_VERSION == "3.4.11"
    Bundler.setup
    require "rspec/core"
    require "libosctl/native"
    native = $LOADED_FEATURES.find { |p| p.end_with?("/libosctl/native.so") }
    netlink = ENV.fetch("NETLINKRB_PATH")
    lxc = ENV.fetch("RUBY_LXC_PATH")
    abort "declared source/native binding unavailable" unless [native, netlink, lxc].all? { |p| p && p.start_with?("/nix/store/") && !p.match?(/[\r\n]/) }
    gemfile = Bundler.default_gemfile.to_s
    lockfile = Bundler.default_lockfile.to_s
    puts JSON.generate(ruby: RbConfig.ruby, ruby_version: RUBY_VERSION, bundler: Bundler::VERSION, gemfile: gemfile, lockfile: lockfile, lock_sha256: Digest::SHA256.file(lockfile).hexdigest, bundle_path: Bundler.bundle_path.to_s, native: native, netlinkrb_path: netlink, ruby_lxc_path: lxc)
  '
```

Nix local/remote builds are disabled; ordinary declared Bundler dependency
setup and signed cache fetches are authorized. The root watcher owns the
five-minute client/group bound, full log and terminal reconciliation. Stop on
an unexpected kernel/old-Nix/heavy closure, or record the exact uncached Nix
derivation rather than lifting build limits blindly. Possible small declared
frontend outputs are the normal shell environment and `osctld-config.json`;
no actual cold dependency has been established. Any additional native target
must be named from an actual error, not built speculatively. The readiness
callback prints only the finite declared paths/versions and generated-lock
hash, with cached native binding restored inside the selected shell. It runs
no daemon or unit example; D resumes the released spec prototype after setup.

Latest read-only native triage: [exact-e175 addendum](native-lineage.md#exact-e175-native-run-41865572140-shutdown-failure).
Final counts are **109 groups / 323 scripts, 108 successful groups / one failed**;
106 was an intermediate status with two groups still running. The sole failure
is `osctl/ct-passwd` teardown: its body passes, `poweroff -f` returns 0, then
the VM fails to exit within 900 seconds while stage 3 repeatedly reports tank
held by `self_shutdown`. Prior image/device and three cgv1 boot-failure cases
all actually pass. Exact shutdown-holder state is missing; no root-cause fix,
flakiness or feature/baseline attribution is claimed. The artifact hash and
five-file safe extraction are recorded; no CI/API/Git/Nix/test/VM/source action.
The original 81/207 implementation receipts below remain preserved for their
recorded version. The lead/architect own any next diagnostic or fix; full
new-head native plus nine-row acceptance remains blocked.


## OSVM observation fallback: source frozen, quick checks pass

The lead selected the architect's finite observation fallback after the complete
cache plan required material guest-image builds. Implementation is on primary
`ad8991fe6d48ec06fb7cf7d64f15af7578d37e7a` plus exactly four unstaged owned
paths. The detached exact-5235 source, 16 livepatch feature paths, locks, pins,
guest configuration and CI workflows were not changed. Session/env/live roster
and retained Sol/xhigh/workspace_write were reverified before edits; applicable
workspace/repository instructions and the published brief were read.

`Machine#start` passes the same actual argv once, retaining the existing
spawn/PID/reaper/console order. A bounded-size proc identity read occurs while
the child remains unreaped; the launch event is written after the handoff.
Identity capture and launch logging share an observation deadline, capped by
the remaining original startup deadline. A distinct local timeout bounds proc
I/O even while `OsVm::TimeoutError` is masked; expired budget skips that read.
Any pending original startup timeout still propagates through normal rollback.
Only fixed safe Nix-store input paths, numeric CPU/memory/boot fields and owned
PID/start time are retained. Unknown/ambiguous paths and options are explicitly
unavailable/omitted; no raw config, argv, environment, kernel parameter text or
exception messages are logged. There is no file hashing in the spawn section.

When the existing boot wait raises, its original exception object propagates
after at most ten seconds of shell-independent observation. A pinned proc
directory and PPID/start-time checks prevent reads from following PID reuse;
missing/changed/exited processes end collection. Fixed host counters and at most
32 task state/wait-channel rows enter the existing machine log. There is no
guest command, external host command, signal, wait/reaping or process-state
write in the collector. Read/log errors cannot replace the original failure;
a launch-log error cannot roll back a successful start. Helpers remain
protected, with no new runner API, option, mode or artifact.

Validation using the retained declared Ruby 3.4.11, exact cached native extension
and test-runner bundle (including explicit `BUNDLE_PATH`):

- The two changed spec files: **81 examples, 0 failures**, seed 50896,
  1.32s example time. [Log](package-d-osvm-spec.log),
  [exit receipt](package-d-osvm-spec.exit).
- Complete existing OSVM unit suite: **207 examples, 0 failures**, seed 39087,
  7.38s example time. This checks both machine spins and existing startup,
  deadline, rollback, reaper, disk, shell and CLI paths.
  [Log](package-d-osvm-suite.log), [exit receipt](package-d-osvm-suite.exit).
- Declared RuboCop: four files inspected, no offenses.
  [Log](package-d-osvm-rubocop.log), [exit receipt](package-d-osvm-rubocop.exit).
- `git diff --check` passes. No Nix files changed, so Nixfmt is inapplicable.

New controls cover safe omission/duplicate flags, a real owned child's proc
files without reaping/signaling it, missing/reused/unowned/exited PID rejection,
identity changing during capture, unsafe executable/wchan text, the task cap,
collection timeout, log/read failures and exact exception preservation, normal
startup, QEMU spawn failure and unchanged startup-deadline rollback. Initial
Bundler commands failed before tests because `BUNDLE_PATH` was omitted; A's
retained exact prefix corrected that invocation without installation or shell
realization. Four early test failures were overbroad `Dir.open` expectations
that caught fixture cleanup; the controls were narrowed to the target task
directory. Final checks above pass.

The lead's precommit acceptance inspection identified an unbounded initial proc
read inside the masked spawn handoff. The follow-up caps that read and the
launch record with one shared deadline, without extending/resetting the caller's
deadline. Four focused regressions cover blocked reads with no deadline or a
normal future deadline, skipping I/O after spawn consumes the startup budget,
and an exact pending asynchronous startup error preserved through ordered
reaper activation/kill/join rollback. These are mocked child operations, not VM
launches. The prior 77/203 pass receipts remain preserved for the old version:
[focused](package-d-osvm-before-bound-spec.log),
[full suite](package-d-osvm-before-bound-suite.log),
[lint](package-d-osvm-before-bound-rubocop.log).

Frozen source SHA256:

| Owned path | SHA256 |
| --- | --- |
| `osvm/lib/osvm/machine.rb` | `8f4ebdc91fc3d303e6c61b3c7f850066e14e6a8463a6d19f96894330e65ba67e` |
| `osvm/lib/osvm/machine_log.rb` | `9fd3f18555bedb875468c7701acaee88dc97327c03cabeb3617ce1a8b9306a50` |
| `osvm/spec/osvm/machine_spec.rb` | `922c9887e069a609ba1efa191eacd0e2e36c129f0ca1d6c1c7255b5eced8988d` |
| `osvm/spec/osvm/machine_log_spec.rb` | `0b35767db2978c1d349908c21f900cb82b8cc351ba572e8ea4ed38d253df22ea` |

Exact diffstat: **4 files, +653/-1**: machine.rb +167/-1, machine_log.rb +27,
machine_spec.rb +430, machine_log_spec.rb +29. Near-code comments record the
identity, bounded-read and exception-preservation invariants. Only fixed log
action/field/unavailability tags were added; no user workflow or user-facing
prose changed. This is host-test diagnostics, with no guest ABI/persisted
production-state/fleet rollout requirement.

D performed no index/commit/fetch/rebase/push, Nix evaluation/realization,
build/copy/VM, CI/API or lifecycle action during implementation. All owned
check clients are terminal; source is frozen for A's serialized separate
observational commit with normal hooks. Affected independent review of the
complete final series and exact-final-head full native plus all nine lifecycle
rows remain required. The original boot failure is not waived or explained
by this observation change. No merge/deployment readiness is claimed.

[Native evidence and cache-plan chain](native-lineage.md#selected-osvm-observation-fallback).
Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>.

## Retained resolver-control receipt

Implementation and independent host controls pass. All 24 tests passed in
12.283 seconds after narrow final-review R1/R2 follow-ups. The complete
21-control implementation was reviewed at `4fc0f375`; the lead owns narrow
finding reconciliation and final shared Git/check sequencing. D's review-fix
source is stable. C confirmed the emitted R2 record passes both actual consumers.

Owner: implementer2, retained Sol/xhigh, workspace_write. Session/env binding
and live roster/access verified. Baseline is clean vpsAdminOS staging
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`.

Scope: `tests/fixtures/livepatch/test_probe_sites.py` and tiny source fixtures
under `tests/fixtures/livepatch/probe-sites-tests/`. B owns resolver/packaging;
A owns initial hooks. Lead serializes Git writes and the utility slot. No
committed module blobs, kernel builds, producer/pin/lock changes, deployment
or lifecycle actions.

The harness will use B/architect0's stable public contract, not resolver
internals or a second schema. Initial independent control matrix:

| Boundary | Positive evidence | Negative controls |
| --- | --- | --- |
| Artifact binding | Captured digest accepts exact tiny ELF | Missing/malformed/wrong digest; bytes changed after capture |
| Function identity | Exact symbol survives section placement/padding | Missing/duplicate symbol or prefix symbol substituted for function |
| Call boundary | Relocation resolves the opcode and instruction length | Relocation displacement cannot become a probe offset; non-call bytes rejected |
| NULL destructor | 32/64-bit MOV/XOR establishes the complete pointer value | 8/16-bit MOV/XOR retains seeded nonzero upper RDX bits |
| Fragment owner | Inline allocation and standalone `inet_frag_create` emit valid finite records | Existing namespace/callee/context/ABI failures remain required |
| FUSE identity | `fuse_ref_page` selects the qualified finish call despite the other finish call | Wrong/missing/ambiguous inline context, callee, object namespace or ordinal |
| Entry hold | Fentry followed by a safe preprologue boundary | Arg0 clobber, changed stack/frame or unsupported prefix |
| TCP arithmetic | Widen-before-increment/multiply/add with live operands; supported register reassignment | Wrong widths, wrap-before-widen, clobbered result/input, ambiguous comparison or inline context |
| Harmless metadata | Debug line and function/section displacement do not alter semantic selection | Removed required inline metadata fails explicitly |

The accepted public boundary is `resolve_site(witness, module, sha256,
fuse_module=None, sdk_vmlinux=None)` and full `resolve(...)`, with
`ResolutionError` for unsupported/missing/ambiguous semantics. No private
selector or decoder entry point is used. The harness asserts the agreed
`schema_version`/`module_sha256`/`symbol_pos` fields and nine finite keys.

The sources and 24 unittest methods are authored. Three entry functions and
the original FUSE callee use tiny assembly; C always-inline wrappers produce
real compiler DWARF for FUSE's two paths, fragment allocation and TCP arithmetic.
Fixture labels independently identify expected offsets. Macro variants change
source semantics, rather than manufacturing a resolver-selected instruction.
One special-relocation positive changes only the tiny ELF's section-name
metadata through pyelftools, preserving real relocation entries/link/target.
GNU objcopy regenerates relocation names from the target, so it did not create
that positive fixture by itself; no parser implementation is duplicated.

Quick evidence so far:

- Source Python AST parses.
- Eighteen C variants and three assembly sources compile, and a tiny candidate
  links, in 2.4 seconds using the repository-pinned GCC wrapper at
  `/nix/store/0592hadxldzhhd3ppc6nskslzd39fwlz-gcc-wrapper-15.3.0`.
- Independent `addr2line` confirms the two FUSE paths and fragment/TCP inline
  identities in compiler-produced DWARF. This is fixture validity evidence,
  not a resolver or runtime pass.

B owned the shared dependency/tool/first siteChecks run. Nineteen tests passed;
one fixture-construction error preceded resolver invocation:
`Elf_Shdr.build` requires pyelftools header Containers, while the helper had
converted them to plain dictionaries. D retained the original header Containers
and changed only this fixture helper. No selector predicate/assertion weakened.

The complete quick rerun passed all 20 tests in 9.357 seconds (9.8 seconds
including process startup), using declared prepared Python
`/nix/store/fqw818l3l2i7m1z0pbi051f3cxc71bg3-python3-3.13.17-env/bin/python`,
the pinned compiler above and already-local binutils 2.46. Command:
`python tests/fixtures/livepatch/test_probe_sites.py -v`, with explicit
`CC`/`OBJCOPY` paths and `PYTHONDONTWRITEBYTECODE=1`.
Log: [package-d-controls.log](package-d-controls.log).

Required real-artifact follow-up: the original FUSE function schedules
`mov %rdi,%rdx` between `push %rbp` and `mov %rsp,%rbp`. Its selected hold is
before the push, so none of that later prologue has executed. The independent
positive fixture now emits this scheduling and uses a fixture-authored symbol
to verify the selected one-byte preprologue hold instruction. Existing
pre-hold stack/frame and argument-clobber negative controls remain unchanged.
The complete 21-test rerun passed in 9.183 seconds (process 9.594 seconds),
using the same prepared environment. Log:
[package-d-controls-scheduled-prologue.log](package-d-controls-scheduled-prologue.log).
Only `callee.S` and the public test file changed; no parser edits or new utility
were needed. Both B and the lead received the pass; sources are frozen again.

Final review follow-ups, scoped by the lead from [final-review.md](final-review.md):

- **R1:** the independent callback-release source seeds RDX with
  `0x1122334455667788`, then varies MOV/XOR zero definitions. All four partial
  8/16-bit controls reject; all four zero-extending/full 32/64-bit controls
  accept. B owns the selector correction. D tests the public semantic boundary,
  without calling the resolver's zero/register helpers.
- **R2:** a real noinline standalone `inet_frag_create` fixture contains the
  `mod_timer` relocation. Public resolution succeeds and the independent marker
  assertion preserves owning function, namespace, call length, context, frame
  and callee checks. The unmodified complete nine-site record from public
  `resolve()` is [package-d-review-r2/sites.json](package-d-review-r2/sites.json),
  with [generation log](package-d-review-r2/generation.log) and disposable tiny
  candidate/SDK/FUSE ELFs alongside. C received this exact emitted record and
  module/header context to exercise both actual consumers, rather than changing
  a JSON symbol by hand.

The R2 artifact's module SHA256 is
`2661f92926a71222c0704d8254906b931a9b21a1f1bdfc3bc197d02369c5814a`,
ELF64 `EM_X86_64`, build ID `dc3f284334b1ee75df109cd5bc38c9b8bde6145e`.
Its fragment record owns `.text` symbol `inet_frag_create` (size 29), call
offset 14/length 5, and qualified `vmlinux:mod_timer` position 0. This is
independent host contract evidence, not runtime qualification of any module.

All 24 tests passed in 12.283 seconds (process 12.689 seconds), using the
prepared environment and `PYTHONDONTWRITEBYTECODE=1`. Log:
[package-d-controls-review.log](package-d-controls-review.log).
Only `sites.c` and `test_probe_sites.py` changed for these review fixes. No
parser edit, generic API, new utility or Git mutation was performed. B received
the stable control sources for declared siteChecks; C owns the consumer results.

C's [actual-record interop log](package-c-r2-interop-fixed.log) records eight
passing checks through the actual common and fragment consumers. Both accept
the current normal `inet_frag_find` record and the unchanged complete
resolver-emitted standalone `inet_frag_create` record above; both reject the
unrelated `inet_frag_alloc` name in each context. C independently checked the
tiny candidate's digest against that record and reports its persistent
consumer suite at 34 examples, zero failures. This closes D/C's requested
record-interop evidence; it remains a host contract check, not live-guest
qualification. No source edit or additional check was needed for this handoff.

B and the lead received the pass and stable source boundary. B owns final
siteChecks packaging and actual current-module resolution; parser follow-ups
remain B's package. D owns any subsequent independent control findings. No
duplicate Nix preparation/watcher, Git/index mutation or commit was launched.
The lead accepted D's 20/20 receipt and froze these sources except requested
findings. A owns one coherent combined feature stage/commit after all packages
are checked, with no tracked unstaged changes for Overcommit to auto-stash.
No separate D/B commit or Git slot was granted. The remaining combined
commit/hooks, actual-module proof and independent review belong to the lead's
execution flow; D remains available for assigned follow-up findings.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>.


## Exact-e175 shutdown unit reproduction — complete diagnosis

The [confirmed interleaving and environment receipt](native-lineage.md#exact-e175-shutdown-unit-reproduction-confirmed-source-interleaving)
supersedes the earlier setup-only stop/proposals. Final declared-osctld bundle
and patched Ruby/native loads pass. Prototype scope is one existing spec file,
167 added lines; daemon spec and production files are unchanged. Source exact
e175; spec SHA256 `ffbf243eb5bb1404961ed1495c6b8429f285cd9a60a34742772a8dd9cf4d9925`.

Focused result: **2 controls pass, 1 intentional red**. Requested three files:
**23 pass, same 1 intentional red**. Real winner export removes the pool and
completes while its thread stays alive holding the outer lock; loser then
retries the removed object with actual self_shutdown ResourceLocked. Abort and
cleanup join both threads and release the lock. All clients are reaped; no
production process, VM, Git/index or CI action was launched. Whitespace passes.

Full commands/stdout/stderr/exits:
`package-d-osctld-native-patched.*`,
`package-d-shutdown-unit-focused-progress.*`,
`package-d-shutdown-unit-three-files.*`.
The native load/setup failures and unused formatter invocation remain retained
as environment evidence. Source is frozen for the lead's diagnosis decision;
the intentionally red prototype is neither committed nor a finished fix.

The source defect is confirmed; attribution of the earlier 900-second VM
failure remains unproven. The linked note proposes the smallest pending-pool
reconciliation boundary and lists abort/marker/exception/ownership invariants.
Production correction, final review and full native/nine-row acceptance remain
separate and unreleased. Lead owns state integration and any scope decision.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>.


## Production shutdown fix — unit verification preparation

The user approved the separate production correction. The four owning paths are
`osctld/lib/osctld/daemon.rb`, `osctld/lib/osctld/commands/self/shutdown.rb`,
`osctld/spec/osctld/commands/heavy_system_spec.rb`, and `osctld/spec/osctld/daemon_spec.rb`.
The previous intentional-red command/output remains historical source proof.
The first finished-contract run passes 45 examples in 1.45 seconds (3.031 total),
[receipt](package-d-shutdown-fix-unit-marker.exit). An additional inspection fix
removes pending restart intent recreated by the unchanged CLI after accepted
abort; its existing final-tail abort example now covers that event. No new
message is introduced: the existing `shutdown aborted` error is reused.

Full-suite command for the root's fresh watcher (not launched by D):

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos/osctld
env GEM_HOME=/tmp/dev-ruby-gems \
  GEM_PATH=/tmp/dev-ruby-gems:$PWD/lib \
  BUNDLE_PATH=/tmp/dev-ruby-gems BUNDLE_GEMFILE=$PWD/Gemfile \
  NETLINKRB_PATH=/nix/store/jh718ag4jr33p20vj3pay0d6r6h108fj-source \
  RUBY_LXC_PATH=/nix/store/7ayldlmwj1pi7yh8d6665jsngj0rpdpb-source \
  RUBYOPT=-rbundler/setup \
  PATH=/nix/store/z30vypx0r6mgbfs0a86m6vd3s7pk07sb-ruby-3.4.11/bin:/tmp/dev-ruby-gems/bin:/usr/bin:/bin \
  /nix/store/z30vypx0r6mgbfs0a86m6vd3s7pk07sb-ruby-3.4.11/bin/ruby \
  /tmp/dev-ruby-gems/bin/bundle exec \
  /nix/store/z30vypx0r6mgbfs0a86m6vd3s7pk07sb-ruby-3.4.11/bin/ruby -S rspec
```

Equivalent literal argv/cwd/allowlisted bindings:
[package-d-shutdown-fix-full-unit.command.json](package-d-shutdown-fix-full-unit.command.json).
There are 210 spec/support files; full-suite timing is unproven, so D does not
self-launch it. A 120-second initial owned-client bound is reasonable for these
unit tests. The apparent 10-second child sleeps in runner specs are tested via
0.1-second timeout or immediate kill/reap; 60-second NFS child sleeps use a
0.05-second worker bound and explicit reap. Existing test cleanup owns these
fixture children. Stop and reconcile owned client/descendants on timeout, missing
binding/native loads or unexpected non-unit/heavy work; do not realize an
environment or rerun automatically. No VM/kernel/Nix operation is part of this
command. Wait for D's final source freeze before the watcher reads the files.


### Source frozen for the full osctld unit check

The recreated-CLI-marker check passed 1/1 in 0.02554 seconds RSpec / 1.674
seconds total ([receipt](package-d-shutdown-fix-cli-marker.exit)). Declared root
RuboCop 1.75.8 passes all four files, no offenses, 6.097 seconds
([receipt](package-d-shutdown-fix-rubocop-final.exit)); whitespace passes.
The root lint context must unset `GEM_PATH`, `BUNDLE_PATH`, and `RUBYOPT`, as in
A's actual hook receipt, so packaged rexml/mutex_m remain in Gem.path. No gem
installation or Nix entry was used for lint. No Nix source changed; Nixfmt is
inapplicable to this Ruby-only package. Earlier missing-gem and formatting
failures remain retained with their corrected outcomes.

Final frozen SHA256 values before the root utility's full owning-suite run:

| Owned file | SHA256 |
| --- | --- |
| `osctld/lib/osctld/daemon.rb` | `96869f2dc3c99ef6843062f58f5bb80a32b6488da3c3c36e7846212fa1a830ca` |
| `osctld/lib/osctld/commands/self/shutdown.rb` | `dcea32b51a87e5e3bd1d4d117d42cab6e9b2e31901d66bddac21e363585e2fe7` |
| `osctld/spec/osctld/commands/heavy_system_spec.rb` | `ea6a362d8cbb31813e597ec422cf037f4b04ff6a1b105865ab3a4436a4596aff` |
| `osctld/spec/osctld/daemon_spec.rb` | `cd4278dc046315f5cfbd0febf5200bd163b45976446ab97da6d4c0de742b41d8` |

Against published e175: four files, 714 insertions / 53 deletions. Production
stats: daemon 112 changed lines, self/shutdown 84; specs 358 and 213 added lines.
The historical +167-line red prototype has been replaced with finished
coalescing contracts, while its full red logs and hashes remain preserved.
D will not edit the frozen paths while the root's utility reads them; the full
suite result is pending, so this is not a completed verification claim.


The production contract is a per-daemon ephemeral active outcome, admitted
before snapshots. The owner runs resource work outside the mutex; abort remains
responsive. Normal success confirms only after real export tails and command
hold cleanup. All owner exits publish completion and wake waiters; captured
waiters keep their original record across a subsequent request. Non-abort
errors retain restart intent; accepted abort removes it, including an unchanged
CLI's subsequently recreated pending marker. Only the owner begins/reset-abort;
joined callers do neither. Existing `shutdown aborted` wording is reused.

Cleanup tracks each acquisition before interruption can separate it from its
ownership list, attempts every still-owned hold in reverse order, skips removed
and foreign holds, and keeps an initiating error when cleanup also fails. No
foreign unlock, generic manipulation change or export-hook bypass is added.
The active record owns lock lifetime; a still-live setup/client thread does not.

Compatibility: no CLI/wire API, option, stored format, marker modes or migration
is added. Existing clients keep success/error behavior; joined clients may
receive no intermediate owner progress. Process restart discards only the
in-memory gate and still resumes via the existing marker. No coordinated fleet
update is required. A code rollback loads the same state and restores the old
race risk. No daemon restart, live deployment or integration was performed.
Near-code comments explain the non-obvious ownership, interruption and marker
rules; no existing public workflow/marker documentation needs a format update.

Historical VM attribution remains unknown. Final committed independent review,
focused real graceful-shutdown VM acceptance, restored 14400-second qualification,
and exact-head full native/nine-row CI remain separate required checks, not
waived by unit proof. The temporary 300-second diagnostic source belongs to C
and was untouched. No session/runner/infrastructure lifecycle action occurred.


### Full-suite loader classification and one conventional correction

The root's first actual all-spec invocation exited 1 after 1.932 seconds,
before any examples. Source hashes matched the frozen four paths before and
after. The prior wrapper did not launch because my restricted descriptor PATH
omitted bare `timeout`; the root's absolute `/run/current-system/sw/bin/timeout`
correction is recorded separately in `.launcher-error`. This is one launched
unit command, not two test runs or a product assertion failure.

The full stderr exposes the original missing provider: `lxc/lxc` from declared
ruby-lxc `7ayldlm.../lib/lxc.rb:2`, reached by
`console/console_spec.rb:6` -> `console/console.rb:3` -> `console/tty.rb:4`.
RSpec's `load_file_handling_errors` then tries to load its absent
`rspec/core/did_you_mean` diagnostic helper, masking that original LoadError.
The focused files do not require LXC; `.rspec` and `spec_helper` are unchanged.
No helper or dependency was deleted/replaced to bypass this error.

The final current-hash focused three-file run passes **45/45**, RSpec 1.4 seconds,
2.831 seconds total, exit 0:
[package-d-shutdown-fix-target-final.stdout](package-d-shutdown-fix-target-final.stdout),
[exact command](package-d-shutdown-fix-target-final.command.json).

One already cached declared native provider is available:
`/nix/store/mw4mbwjkimmd3aw03j0l246fg4s28ahv-ruby3.4-ruby-lxc-1.2.4.vpsadminos.6`.
Its existing deriver
`/nix/store/xk5a5laibkarqyg4ba6ax8npwwav1pd6-ruby3.4-ruby-lxc-1.2.4.vpsadminos.6.drv`
explicitly references the same 7ayldlm source and patched Ruby z30, plus the
current `os/overlays/osctl.nix` native ownership patch
`os/packages/ruby-lxc/initial-cwd-owned-storage.patch`. The installed C differs
from the raw source only by that declared patch; raw C byte equality is not
claimed. Deriver SHA256:
`05220719c51c783b1d0ab17ae93e24548b9d7e7e927fb20548e73294395a3a3c`.

Add only this native extension directory to `RUBYLIB`:

```text
/nix/store/mw4mbwjkimmd3aw03j0l246fg4s28ahv-ruby3.4-ruby-lxc-1.2.4.vpsadminos.6/lib/ruby/gems/3.4.0/extensions/x86_64-linux/3.4.0/ruby-lxc-1.2.4.vpsadminos.6
```

The bounded `require 'lxc'` smoke passed in 0.920 seconds, exit 0, under the
same osctld Gemfile/lock/actual patched Ruby. `Gem.loaded_specs['ruby-lxc']`
still identifies source 7ayldlm; the loaded native SHA256 is
`60fe2b69e94e8fe707276a1e69f0b977c4e0f184274b30d5b141e005f7205e6f`.
[Smoke proof](package-d-shutdown-fix-lxc-load.stdout) and full command/error/exit
are retained. This loads a library only, without creating an LXC container.

The exact corrected all-unit command is
[package-d-shutdown-fix-full-unit-with-lxc.command.json](package-d-shutdown-fix-full-unit-with-lxc.command.json).
It retains the actual successful target PATH instead of the unnecessarily
restricted initial descriptor PATH, adds the verified extension-only RUBYLIB,
and keeps all other bindings, cwd and normal all-spec argv. The original
command/failed logs remain intact. No network, Nix, installation, compilation,
source edit, bundle update, pin change or full-suite rerun was performed by D.
All quick clients are reaped. All four frozen hashes and the development lock
remain unchanged; root owns the one corrected full-unit invocation.


### Final complete code handoff — broader suite unavailable

The corrected all-unit invocation with the LXC native directory exited 1 after
2.265 seconds, before examples. Its static `result.json` verifies all four
source hashes before/after. Original error: `repository_spec.rb:4` loads
`osctld/repository.rb:3`, which requires `filelock`. RSpec's absent
`did_you_mean` diagnostic helper masks this original LoadError again.

`filelock` is **declared**, not an undeclared cross-gem fixture dependency:
osctld's gemspec requires `osctl-repo`; `osctl-repo/osctl-repo.gemspec:30`
requires filelock. Development lock SHA3169e57f pins filelock 1.1.1 and archive
SHA256 `5207258374370a75d5927b2eaf9b831732d224e48ce56c318e8308c7cdcabb20`.
Exact published e175 already has both the require and this dependency. The
selected `/tmp/dev-ruby-gems/ruby/3.4.0/gems/filelock-1.1.1` exists, but its
`lib/filelock.rb` does not. No cache-deletion cause is established.

One existing declared-version provider was selected for the permitted load-only
check: `/nix/store/8m795ayrivirbdvm5nklrlq8wifcj0af-ruby3.4-filelock-1.1.1`.
Deriver `8j25s7ddnmnbcy98n9mmnw1lv1x229xw` uses z30 Ruby and fetch deriver
`9a17kxya6cg61in7rfc8xniw6n3z5br6-filelock-1.1.1.gem.drv`; the latter records
exactly the locked SHA above. Its ordinary gem `lib` directory was added only
to the load check's RUBYLIB alongside the accepted LXC extension directory.
The old incomplete gem tree was not altered, purged or replaced.

The **one allowed `--dry-run`** then exited 1 after 2.326 seconds before
examples. It advanced past filelock and exposed the next missing declared
library: `utmp_reader_spec.rb:3` -> `osctld/utmp_reader.rb:1` -> `bindata`.
`bindata ~>2.5.0` is directly declared in the osctld gemspec, lock version 2.5.1;
`/tmp/dev-ruby-gems/ruby/3.4.0/gems/bindata-2.5.1/lib/bindata.rb` is absent.
Exact e175 already requires it at that same owning source line. RSpec's missing
diagnostic helper is again secondary. Full dry-run command/stdout/stderr/exact
exit: `package-d-shutdown-fix-full-unit-dry-run.*`.

**Stop:** the normal all-spec suite cannot load in this partially materialized
existing declared gem cache. No additional provider hunt, installation,
manifest/pin/source change, cache purge, dry-run or full-suite retry is selected.
This is an environment/load limitation before assertions; it neither proves a
product regression nor establishes whole-suite green. Root/reviewer own the
coverage disposition and next accepted check.

The implementation handoff is complete within its four-file boundary:

- Final frozen-source targeted suite: **45 examples, zero failures**, RSpec
  1.4 seconds / 2.831 total, `package-d-shutdown-fix-target-final.*`.
- Recreated-CLI-marker regression: **1/1 pass**. Declared root RuboCop 1.75.8:
  **four files, zero offenses**. Whitespace passes.
- Four hashes, lock SHA3169e57f and local native SHA0a0b9449 remain unchanged.
  Exact final four-file diff and the compatibility/rollback/lifetime rationale
  are recorded above; `package-d-shutdown-fix.patch` is the owned-only snapshot.
- All D smoke/check clients are terminal and reaped. Source remains frozen;
  no production/thread/VM/CI/Git/index/deployment/session-lifecycle action was
  performed by D beyond the accepted source and unit work.

The root's broader-suite attempts and D's load-only dry-run are explicitly
failed pre-example verification attempts, separate from passing targeted unit
assertions and the historical intentional red. No whole-head acceptance or
historical incident attribution is claimed. Root/A own the separate purpose
commit, committed independent review and approved further acceptance work.


## Focused runtime shutdown acceptance audit — 41913307185

**Complete bounded audit; focused acceptance passes for its recorded inputs.**
This is a local evidence read only. The lead reports the separate production
commit `645927e22809a29c67ffd59c072e553e05e2a72b` and four independent review
lanes accepted without findings. Retained Sol/xhigh/workspace-write and exact
session/environment binding were reverified. No application file was edited.

Run [41913307185](https://github.com/vpsfreecz/vpsadminos/actions/runs/41913307185),
attempt 1, is canonically completed/success, workflow_dispatch on this session's
branch and exact head 645927. Retained `status-final.json` / `jobs-final.json`
record build job 126866267072 success (21:08:54–21:31:54Z, 23 minutes) and native
job 126879025475 success (21:31:56–21:37:07Z, 5m11s). Native raw log lines 1–4
identify runner `gh-runner2.int.vpsadminos.org`, runner ID 4793 in job metadata,
version 2.338.0. Lines 248–251 bind suite `ci`, selection `osctl/ct-passwd`,
source 645927 and Git tree `299cfa2389b40ada478090e58ff0039b32303d04`.
The command uses `tests/test-configs/ci.nix` (native log line 165), with
`TEST_RUNNER_PREBUILD=true` and `STOP_ON_FAILURE=true` (lines 235/238).

Independent ZIP verification: artifact **13365581790**, name
`os-test-logs-41913307185-1-native`, exactly **10,943 bytes**, SHA256
`0481aab90784e44aa39af786ee2eb761819578793944b15fc022aa4a83205a7b`,
matching GitHub inventory and watcher receipt. All eight members were listed
and checked for absolute/traversal/backslash/drive paths, duplicates, encryption
and symlinks before extraction. Only five owning case logs/result plus top-level
`test.log` were extracted (six files, 12,391 uncompressed bytes), into
[package-d-shutdown-focused-evidence](package-d-shutdown-focused-evidence/).
The unrelated prebuild log and VM-shared-filesystem log were not extracted.
Full safe member listing/ZIP binding and selected-file hashes are retained in
that directory's JSON receipts. No earlier evidence was overwritten.

All detailed case timestamps below are **2026-11-04 +0100**, one hour ahead of
UTC. The exact group is `osctl/ct-passwd`, one selected `default` script:

| Evidence | Recorded event |
| --- | --- |
| [test-runner.log:1](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-d-shutdown-focused-evidence/os-test-osctl__ct-passwd-506834be/test-runner.log:1), [machine log:27](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-d-shutdown-focused-evidence/os-test-osctl__ct-passwd-506834be/machine-log.log:27) | Script starts 22:35:12 and finishes successfully at 22:36:45 in **93.08s**; stop begins at 22:36:45. |
| [shell log:239](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-d-shutdown-focused-evidence/os-test-osctl__ct-passwd-506834be/machine-shell.log:239) | `poweroff -f` starts 22:36:45, returns **status 0** at 22:36:48, elapsed **3.57s**. Output includes pool tank export, both container stops, and unregistering users/groups/containers. |
| [console:122](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-d-shutdown-focused-evidence/os-test-osctl__ct-passwd-506834be/machine-console.log:122) | Runit leaves stage 2, enters stage 3, grabs pools/containers, prints “and down we go”, leaves stage 3, performs normal guest process termination and powers off; kernel prints **`reboot: Power down`** at guest monotonic 98.697465s. |
| [machine log:33](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-d-shutdown-focused-evidence/os-test-osctl__ct-passwd-506834be/machine-log.log:33) | **QEMU exits status 0 at 22:36:57**. Only afterward the cleanup `kill` event records **`SIGNAL: NONE`**, followed by destroy at 22:36:57. |
| [result](package-d-shutdown-focused-evidence/os-test-osctl__ct-passwd-506834be/test-result.txt), [test.log:9](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-d-shutdown-focused-evidence/test.log:9) | Whole group is **`expected_success`**; one script of one test succeeds in **105.29s**. Native raw lines 366–369 agree, and canonical native “Evaluate test results” step succeeds. |

The recorded stop-to-QEMU-exit interval is approximately **12 seconds**, far
below the existing **900-second** stop budget. The logs record second-resolution
wall times rather than the deadline clock itself. Body/group durations leave
12.21 seconds for the remainder of the test. Guest runit's normal KILL-to-processes
message is part of its successful stage-3 poweroff; **no host cleanup TERM or
other QEMU signal supplies this exit**. The host-side evidence is the ordered
`qemu_exit STATUS: 0` followed by `kill SIGNAL: NONE`, not merely workflow green.
This satisfies the focused body's and actual graceful-shutdown acceptance.

Actual launch identity is in [machine log:7](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-03-livepatch-fixture-failures/package-d-shutdown-focused-evidence/os-test-osctl__ct-passwd-506834be/machine-log.log:7):

- Owned QEMU PID **3615709**, start-time ticks **146244762**;
  QEMU `/nix/store/kanckc6ljipqzjsrvj4aqaf87a4rhswr-qemu-host-cpu-only-for-vm-tests-10.2.4/bin/qemu-kvm`.
- Kernel `/nix/store/b043pwyanxjfz22hbiibv5wipqqcl932-linux-6.12.113/bzImage`;
  initrd `/nix/store/p1a2p526kvg1zsz7j5wwmg68i9m1z2zm-initrd/initrd`.
- **Guest system** `/nix/store/kkn64gyc0nwnljmdv0n9k2big66vxm5p-vpsadminos-system-vpsadminos-26.05.git.645927e`;
  squashfs `/nix/store/7p3jx1cw6x6x6h8v78jh2dazh1wphy00-squashfs.img`.
- Direct boot, 8192 MiB, four CPUs/four cores, one thread/socket.

The separate build's `BUILD_OUT` is
`/nix/store/han02zlbiyirwgdk0x9gffgc9n3wdmwn-vpsadminos-system-vpsadminos-26.05.git.645927e`
(build log line 383); it is **not substituted for the actual guest system path**
above. The recorded launch kernel is 6.12.113; no retained guest `uname` or full
Linux version banner independently reports the running version. No equality
with the earlier native guest inputs or omitted historical tuple is claimed.
The logs also do not establish that overlapping shutdown callers occurred in
this successful VM: deterministic unit controls establish that contract.

Remaining gates: this is one focused native script, not full native coverage.
Lifecycle job 126879028741 and current livepatch sites capture were skipped.
The optional full owning-unit suite remains unavailable for the documented
pre-example cache/load reasons; final 45 focused controls, marker and lint proof
remain intact. Any lead-selected 300-second diagnostic sibling needs its own
source/input binding and acceptance. Final restored **14400-second** qualification
and exact-final-head full native plus all nine lifecycle rows, with their identity,
health and recovery requirements, remain required before conditional integration.
No waiver, integration, deployment or lifecycle permission is inferred.

The earlier 900-second teardown failure and unknown holder/restart/export
history remain preserved in [native-lineage.md](native-lineage.md). This pass
establishes correct shutdown on these packaged inputs; it does not retrospectively
attribute or explain that old failure. Audit complete, no owned process or
pending command; no API/download/poll/build/eval/Git/VM/CI action was performed.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>.


## Cancelled bda1 AMD-fresh evidence accounting — complete

Local retained evidence only: run **41921632759**, attempt 1, job **126907163579**,
exact source **`bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf`**. This does not relabel
old evidence with the current 13b head. Session/environment and retained
Sol/xhigh/workspace-write were reverified. The lead's authoritative cancellation
boundary is one request at **2026-11-05 00:04:04.227Z**, canonical completed/
cancelled at 00:04:58Z. The raw job notices cancellation at **00:04:48.299Z**
(line 313). No current-run, Intel or cancelled-native evidence was inspected.

Independent artifact check: **13375257923**, exactly **362,242 bytes**, SHA256
`fc6e2781684a2ea39841b2e5dec05cd32b7bd95851e893333fbae7882a3c23f9`.
All **70** ZIP members pass absolute/traversal/backslash/drive, duplicate,
encryption and symlink checks. The raw job is 81,098 bytes, SHA256
`a851553b59d54f923b87c5d3028d288ea8ce9258532b03d582e4564d2c3f1119`.
[Selected evidence](package-d-diagnostic-300s-fresh-cancel-evidence/) retains
all small result/runner logs and top summary, safe launch/teardown records,
identity files, scan classifications and bounded excerpts; no full shell or
unrelated prebuild payload was extracted.

**Actual case accounting:** 22 selected (20 fresh and two retention), nine
started, **eight `expected_success` result files**, one unfinished without a
result, **13 not started**. No expected-failure or unexpected-result file is
present. The final whole-row summary is absent; the canonical row is cancelled,
not passed. All eight completed cases finished before the cancellation request.
UTC times (start/finish dates are November 4 except the noted midnight crossing):

| Started order | Variant | UTC start | UTC completion | Result |
| --- | --- | --- | --- | --- |
| 1 | amd-fresh-v5-8 | 23:30:06 | 23:34:17 | expected_success |
| 2 | amd-fresh-v6-5 | 23:34:17 | 23:38:29 | expected_success |
| 3 | amd-fresh-v6-10 | 23:38:29 | 23:42:43 | expected_success |
| 4 | amd-fresh-v6-6 | 23:42:43 | 23:46:57 | expected_success |
| 5 | amd-fresh-v6-2 | 23:46:57 | 23:51:09 | expected_success |
| 6 | amd-fresh-v5-7 | 23:51:09 | 23:55:24 | expected_success |
| 7 | amd-fresh-v5-9 | 23:55:24 | 23:59:38 | expected_success |
| 8 | amd-fresh-v5-10 | 23:59:38 | Nov 5 00:03:50 | expected_success |
| 9 | amd-fresh-v6-9 | Nov 5 00:03:50 | unfinished | no result |

Top `test.log` lines 25–68 and raw job lines 274–312 agree with the individual
result files. Every completed case's machine log records QEMU status 0 and
subsequent `kill SIGNAL: NONE`, followed by destroy, before cancellation; no
completed case has a recorded teardown failure. The 13 unstarted selections
are v5-1..6, v6-1/3/4/7/8, and both retention variants. There is no whole AMD-fresh
or full lifecycle pass claim.

**No recorded pre-cancellation kernel/boot/loader/shutdown fault** was found in
the selected evidence. All nine retained consoles were scanned; shell **OUTPUT**
blocks were scanned separately so embedded check/grep command text is not
mistaken for a kernel event. No actual BUG/WARNING, soft lockup, RCU stall, hung
task, stack trace, `module_enable_text_rox`/CSD stall, or CPU127 scheduler/hotplug
warning signature appears. The broad shell scan's 25 warning hits are all
userspace `ipset test klp_pre_ip 192.0.2.129` membership messages, each **status
0**, not kernel faults; their command/status context is preserved. Completed
runner records include pre/post-transition cumulative-health checks and the
successful activation/disable trace controls. No C/old-5235 source investigation
was needed because no real matching fault was found.

The unfinished v6-9 record needs a precise limit. It starts at 00:03:50Z and
launches QEMU PID **1221044**, start ticks **146919850**, at 00:03:51Z. Its runner
begins evaluating the example at **00:04:09Z**, after the request boundary.
The console records predecessor `livepatch_6` enabling and patching complete.
The last shell command is **`touch /run/livepatch-nfs/mnt/klp-nfs-lock`**, begun
**00:04:14Z**, also after the request, with no END/status/result before the
artifact snapshot. An earlier bridge-readiness probe returns status 2 and
execution continues; it is not recorded as an example failure. No target
livepatch_7 activation, natural exception or timeout is recorded for this case.
This is **incomplete NFS setup within the cancellation window**: neither a
product pass nor proof that cancellation caused the unreturned command.
The snapshot lacks facts to decide whether it would complete without cancel.
Raw job lines 526–531 later terminate orphan processes; QEMU PID 1221044 is
terminated at **00:04:52.418Z**, after the cancellation notice and artifact
upload. That termination is not a pre-cancel teardown fault or successful exit.

Available input binding is preserved, without reconstructing an omitted tuple:
artifact identity records producer `qi47yi2g9kp89dv0h8jxwndm89vbq6az`, module
SHA256 `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`,
sites output `aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3`, source bda1 and captured Inputs
`604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`.
The actual launch records name frozen kernel
`/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage`,
initrd `h3v4nwmsn39wph7apj7q6bg8hn58rv3x`, guest system
`cfh4f9rhajva2kdjixrsg2vbxq5mpvh4-vpsadminos-system-vpsadminos-26.05.git.bda1f5d`,
squashfs `vy497aihsz9i954ydsdfz9mnhrh6svyn`, QEMU 10.2.4, direct boot,
8192 MiB/four CPUs. Only recorded paths/digests are claimed; no current-head
or historical-input equivalence is inferred.

Bounded accounting/triage complete, with no new source, diagnostic design,
retry, waiver or historical-cause gate. Original natural aged-v5 fault and
other lifecycle evidence remain owned by C/root and are not discarded based
on cancellation. D created no VM/utility/test or persistent process and made
no source/Git/API/download/poll/eval/build/lifecycle action. All local read and
extraction commands are terminal; no owned process remains. Current run
41938327930 and its sole watcher were untouched.


## Final-F paired Intel representative acceptance

**Current package status: COMPLETE — v5 and v6 PASS for their independently
recorded final-F inputs and original representative assertions.** This is exactly
the paired Intel representative package, not whole-matrix qualification. The sole final
CI watcher remains root's owner; D made no API, download, poll, test, runtime,
evaluation/build, Git mutation, source edit or infrastructure/lifecycle action.
Session/environment and live retained Sol/xhigh/workspace-write settings match.

Read the complete final shipping review, current accepted shipping/runtime
brief and C's full ordinary300 acceptance as contract context only. No C
runtime result is transferred. Read-only primary guard confirms committed
F `56b9363db1f1039e5d684dadc260cdffe7497e08`, clean tracked source/index, new
lock SHA256 `67487674fa38049fede8047dbf8d7302971a3b19ea2866cf6f954e3a2e5ad656`.
Original profile SHA367dd4ce, qualification SHAa965f3e3 and common SHAa7f231c2
match the final review. All provenance refs/roots remain untouched.

### Intel representative v5 — completed artifact audit

Final full push run **42079730277**, attempt 1, job **127437736616** is reported
canonically successful in 9m35s. Artifact **13442077306**,
`os-test-logs-42079730277-1-livepatch-intel-representative-v5`, independently
matches **53,818 bytes** / SHA256
`d97ed42d1e70bf6943571269d9b20353ce43addf785342d3e87b506651a4bb98`.
All **15** members are safe unique normalized relative regular files, no
directories/symlinks/traversal/encryption. Safety validation preceded body reads.
[Selected v5 evidence](package-d-final-f-intel-representative-evidence/v5/)
retains tiny identity/sites/result/runner/console/launch files and bounded
numbered windows; the 353,383-byte shell was streamed (6957 lines, 436 commands),
not extracted or dumped. The main 72 windows are 25,961 bytes; state-consumption
windows add 2009 bytes. The stream summary records complete counts/output hashes.
An initial first-line-only OUTPUT parser was corrected to full multiline
blocks before acceptance conclusions; this was an analysis correction, not a
runtime fault or source change.

Captured source is exact F and captured Inputs matches the new lock above.
Normal producer/module are qi47yi2g9kp89dv0h8jxwndm89vbq6az livepatch_7-6.12.95;
module SHA256 is `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
Sites output aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3 has independently hashed JSON
SHA256 `093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`,
schema_version1, the same module digest and exactly the agreed nine site keys.
Guest shell lines 54/63/72/81/90 directly pass frozen uname6.12.95 and corrected/
sites/exact v5 (`b31f6440…927984`)/v6 (`960b13f1…5efe3`) hashes. Exact v5 loads,
converges enabled1/transition0, and is removed after replacement; v6 remains
forbidden. Those negative module checks are expected status1, not failures.

Actual launch: PID **3667855**, start ticks **153703971**; QEMU package10.2.4
kanckc6l, frozen kernel **050sh2hfrnpc8j5abr2npp7bnlxvpb8a**/bzImage, initrd
**h3v4nwmsn39wph7apj7q6bg8hn58rv3x**/initrd, actual guest system
`/nix/store/9xr1k1dqplrh9rj2v17d2fq7in1y9y2i-vpsadminos-system-vpsadminos-26.05.git.56b9363`,
squashfs **ahmmqqvindh02cr7xa717n3r5i3wmpi1**. Direct boot, eight cores/vCPUs,
one thread/socket, 8192MiB. Guest uname and retained dmesg self-report6.12.95;
GenuineIntel, kvm_intel, /dev/kvm and three KVM smokes pass. **Host runner name/
runner software version are UNAVAILABLE** in the supplied artifact/metadata;
none is borrowed from an old run.

| Required v5 representative property | Direct evidence (original shell command lines) |
| --- | --- |
| Actual representative envelope | MemTotal8136200KiB at1019 fits8192MiB; getconf8 at954; ten running snapshots validate16384tasks/ready16383/eight CPUs/all eight actual-affinity/progress/perf fields, PID21504. This is not the100000-task/128CPU aged profile. |
| Applicable age/progress | Minimum age0; actual host-monotonic age67.4297915s in runner6. All18 ordinary progress counters strictly advance across the ten observed snapshots; five bounded progress waits terminate0. |
| Original CPU hotplug before AND after transition | CPU7 offline/online/getconf/progress checks at2215–2260 and3125–3170; runner7–9/35–37 reports cumulative health complete on both sides. |
| Shared activation/convergence and disable bound | One successful activation attempt, total2.5264984s; disable/convergence6.4620095s, each below the shared1800s ceiling. Predecessor disabled/removed; corrected module disabled/removed and absent. |
| Original callbacks and trace integrity | All21 ordinary lifecycle/callback counts match after replacement and after disable (42 rows); Intel's SVM callback is correctly0. Both ordinary per-CPU stats reads have16 overrun/commit-overrun values, all0. No retired codec/native-completeness claim. |
| State/data and NFS/SCTP/TUN/KVM | NFS data equality before/after replacement0; aged nonblocking flock expected1 retains the lock; release and holder-gone checks0. SCTP/TUN readiness, live/progress checks and final exit statuses pass; KVM smoke and task patch_state=-1 at3381 pass. |
| Both full active migrations | PID21504 ->A at3498/status0/0.06s and ->B at4722/status0/0.07s; membership checks4407/5275 plus fresh all-counter progress and cumulative health pass after each. |
| Strong stop and resource recovery | Population/SCTP/TUN exit tests5760/5769/5778 all0; stopped5787 and tasks1 5796 pass. Stress stop/gone wait/removal5814–5841 succeeds; consumed IPSET/NFT/bridge/netns/XFRM state and TAP/A/B deletion succeed through5946. All48 ordinary trace-event cleanup commands return0. |
| Final health/completion/teardown | Fourteen cumulative dmesg reads all0 from the same baseline524, seven64-fork/RCU-delay health cycles, no original fault-pattern match; preserved console also has none. Successful source flow reaches completed=true after final checks; ordinary hooks do not raise. Stop18:22:46Z, QEMUexit0 at18:22:57Z, then killSIGNALNONE/destroy. |

The case is `kernel/livepatch-qualification@intel-representative-v5/default`:
example224.81s, script262.36s, whole test273.22s, result **expected_success**.
The actual command assertions and payload checks above establish the pass;
job/step/upload success alone is not used as assertion proof. Best-effort shared
cleanup is not promoted to stronger unlogged postconditions. Early DNS/readiness
polls and expected absence/flock statuses are distinguished in the stream summary.
This one successful insertion exercises no EBUSY/failure-retention branch.

### Intel representative v6 — completed artifact audit

Same full push run **42079730277**, attempt1, exact F; completed job
**127437736350** is successful, 18:13:32–20:44:47Z (2h31m15s). Saved
`native-failed-artifacts.json`/`native-failed-jobs.json` explicitly map this
successful Intel job and artifact; their filenames do not classify Intel as a
failure. Artifact **13452306751**, exact name
`os-test-logs-42079730277-1-livepatch-intel-representative-v6`, independently
matches **2,622,864 bytes** / SHA256
`d1397a8574cec614e6a1c7e92792981bdf06f95c4d0ec93c1d16a54b072ed735`.
All **21** members are safe unique normalized relative regular files, no
symlink/directory/traversal/encryption; safety preceded body reads.
[Selected v6 evidence](package-d-final-f-intel-representative-evidence/v6/)
retains tiny identity/sites/runner/result/console/launch files, the stream summary
and bounded numbered command windows. Target shell **488,771 bytes / 8020
universal-newline lines / 434 commands** was streamed, never fully extracted or
dumped. There are104 selected windows (40,304 bytes) plus33 small counter/state/
baseline windows (10,402 bytes); full migration traces and unrelated payloads
remain solely in the original ZIP. An analysis assertion initially assumed no
console regex matches; inspecting its two matches corrected that assumption
before acceptance, as described below. No runtime/source failure is inferred
from that analysis correction.

**Actual selection is two groups**, not one: shared test.log1–5 lists the
Intel representative-v6 group and auxiliary `osctl/nfs-cancellation-native110`.
Intel's own test.log10–12 and runner3–5 show example **222.99s**, script
**253.82s**, whole Intel test **261.94s**, result **expected_success**. The
auxiliary starts after Intel and shared summary93–94 records2 scripts/2 tests
successful. Only selection/result accounting is claimed for that auxiliary;
its shell/console/prebuild payload was not extracted or audited. The longer
job duration is not assigned to an Intel test phase or used as failure evidence.

Captured Source is exact **F**, Inputs is the final lock
`67487674fa38049fede8047dbf8d7302971a3b19ea2866cf6f954e3a2e5ad656`.
This artifact's own capture names normal producer/module qi47yi2g9kp89dv0h8jxwndm89vbq6az
and module SHA256
`7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`.
Its independently hashed sites JSON is
`093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`,
schema1, matching module digest and exact nine agreed keys. Guest assertions
at shell54/63/72/81/90 verify uname6.12.95 and corrected/sites/exact v5
(`b31f6440…927984`)/v6 (`960b13f1…5efe3`) hashes. Exact v6 loads at1349,
converges enabled1/transition0 at1376, is replaced/removed at2930/2948;
forbidden v5 remains absent1340/2939. Negative statuses are expected assertions
or bounded convergence polls, not example failures.

Actual v6 launch records PID **2861633**, start ticks **155253711**; QEMU
10.2.4 package kanckc6l, frozen kernel **050sh2hfrnpc8j5abr2npp7bnlxvpb8a**/bzImage,
initrd **h3v4nwmsn39wph7apj7q6bg8hn58rv3x**/initrd, actual system
`/nix/store/l3f4741gav7v028d80k06k2wwkp1l067-vpsadminos-system-vpsadminos-26.05.git.56b9363`,
squashfs **rbw5iqbji3ha6gwf90kgknw66m86y4m9**. Direct boot, eight cores/vCPUs,
one thread/socket,8192MiB. These are this row's launch facts, not v5's guest
closure. **Host runner name/software version remain UNAVAILABLE** in supplied
artifact/metadata. No omitted version or independent running-image/notes digest
is reconstructed.

| Required v6 representative property | Direct evidence (original shell command lines) |
| --- | --- |
| Actual representative envelope | GenuineIntel959, getconf8 at968, kvm_intel/device/KVM smokes360/369/977/986/995/3369 all0. MemTotal8136196KiB at1033 fits8192MiB. Ten valid running snapshots (1785–6418) retain PID31396/16384tasks/ready16383/eight actual-affinity/progress/perf fields. |
| Applicable age/progress | Configured minimum0, observed host-monotonic age67.7232564s in runner6. All18 counters strictly advance across all nine adjacent snapshot comparisons; five original bounded freshness predicates finish0. Five network counters rise across aging, post-replacement threshold checks3324–3360 pass, TUN counts10→242→359. No100000-task/14400s claim. |
| Original pre/post CPU hotplug and health | CPU7 offline/readback/online/getconf at2211–2238 and3121–3148 all0; fresh progress2256/3166 and runner7–9/32–34 cumulative-health completion pass on both sides. |
| Shared activation/disable/convergence | One insertion at2912/status0; runner10 total2.6238811s. Disable6559/status0 and terminal absence6622/status0; runner35 total6.5121857s. Both below original shared1800s ceilings; module removed6756 and absent6765. |
| Original callbacks/trace integrity | Independent recount of both retained ordinary traces matches21 events per phase, and all42 runner comparison rows match. Intel SVM cb0=0. Both ordinary per-CPU stats contain16 overrun/commit-overrun values, all0. No observer/native-codec claim. |
| State/data, NFS/SCTP/TUN/KVM | NFS content equality2092/3387 and sync2101 pass; held flock2110 returns required1; release6774/holder-gone6783 return0. SCTP/TUN readiness and live/progress checks pass; patch_state=-1 at3378 and three KVM smokes pass. Consumed IPSET/NFT/bridge/netns/XFRM state remains valid. |
| Both full active migrations | PID31396→A at3495/status0/0.08s and →B at5256/status0/0.09s; membership4939/6332, post-return fresh progress5007/6400 and cumulative health pass. Original180s migration bounds unchanged. |
| Strong stop/resource recovery | Population/SCTP/TUN exit0 at6819/6828/6837; stopped6846/tasks1 6855. Stress stop6873/gone6891/pidfile removal6900 all0. State consumption6909/6918 and all strong resource deletions6933–7005 succeed; all48 ordinary trace cleanup commands return0. |
| Final health/completion/graceful teardown | Fourteen cumulative dmesg reads from fixed baseline538, seven64-fork/6s RCU-delay cycles, no original fault-pattern match. Final body health7076, shutdown diagnostics and completed=true source flow, then shared-hook health7515 and cleanup succeed. Poweroff8009/status0, console228 Power down; stop19:44:12Z, QEMUexit0 at19:44:20Z, then killSIGNALNONE/destroy. |

**Boot diagnostic boundary is explicit.** Console35/69 records Spectre-V2
warnings at guest12.865659/13.724482s: “Unprivileged eBPF is enabled with eIBRS
on, data leaks possible via Spectre v2 BHB attacks!” Existing final source
`tests/suite/kernel/livepatch-6.12.95-common.nix:2423–2431` explicitly establishes
Intel/KVM before the example baseline and retains this preexisting BHB boot
diagnostic. Recorded dmesg counts923/932 are537, establishing cumulative
baseline538 before target work. All14 later cumulative reads have no original
fault-pattern match. This is no whole-console-zero claim, new suppression,
health waiver or scheduler/RCU fault attribution; replacement warnings remain
covered by the unchanged original checks.

All36 nonzero commands are individually classified in the stream summary:
initial DNS retry (then success), required module/tlshd absence/held-flock
assertions, bounded readiness/progress/convergence/exit polls (then terminal
success), or best-effort cleanup probes after strong completion. No unfinished
command or natural example/teardown exception appears. One successful insertion
provides no EBUSY/failure-retention negative-branch proof. Best-effort shared
cleanup does not replace the strong body predicates.

### Paired completion

| Row | Artifact | Actual Intel result | Whole Intel test | Activation / disable |
| --- | --- | --- | --- | --- |
| representative-v5 |13442077306|expected_success|273.22s|2.5264984s /6.4620095s|
| representative-v6 |13452306751|expected_success|261.94s|2.6238811s /6.5121857s|

Both independent cases satisfy their original final-F representative contracts
for their own captured source/lock/module/sites/guest launch inputs. Final
read-only source guard remains exactF, empty tracked/index changes, and the
same lock/profile/qualification/common hashes recorded above. Old receipts and
provenance remain intact. D made only local immutable-evidence reads and writes
inside this owned evidence directory/receipt; no test/runtime/CI/API/network/
source/Git mutation, utility, deployment or lifecycle action. All D commands
are terminal, no owned process. Full CI remains with its sole watcher; native
failure assessment is separately A-owned and is not waived by this pair.

### Paired-package limits

These representative results do not qualify separate FUSE/TCP/fragment/main/
aged/native rows, original14400 aging, the whole F matrix or any later head.
No old fault cause, nonrecurrence, warning waiver, health relaxation or EBUSY
negative-branch proof follows. Retired observer host/native-codec fields are
out of scope; original probes, cumulative health, migrations and recovery stay
required. Root owns final runtime accounting and integration. All D read clients
are terminal, no owned process; session remains OPEN.

## Current M — retained mknod attachment evidence prerequisite

**COMPLETE: local retained evidence does not supply the numeric failed attach
or container-init target/lifetime.** This finite prerequisite adds monitor
chronology; it releases no observation wrapper, source remedy or retry. Session/
environment and live retained implementer2 Sol/xhigh/workspace-write matched.
Read the complete current native-blocker design/M brief and corrected A native
audit. Paired Intel and older receipts above remain intact; auxiliary NFS and
N preparation remain exclusively A-owned.

Native artifact **13451362488**, `os-test-logs-42079730277-1-native`, independently
matches **2,915,717 bytes**, SHA256
`943693242af142cf2bd2f9b468ac470130b328c527dbfdf85604fdf985f3db34`.
All822 members are safe unique normalized relative regular files, no directories/
symlinks/traversal/encryption; verification preceded selected body reads. Binding
remains run42079730277/attempt1/native127437736021/exactF56b9363, lock67487674.
Only `os-test-kernel__misc-16014281/` metadata/relevant retained windows were
inspected, with no duplicate full-native audit or unrelated console reads.
[Selected M evidence](package-d-mknod-retained-evidence/) contains the relevant
inventory, compact target summary and **11,406 bytes** of numbered windows;
no complete shell/diagnostic/archive extraction.

Actual failed input is **cgv2/6.18.49**, kernel
`/nix/store/x64477x3mxlzqkmvijvakf33an9vcbrz-linux-6.18.49/bzImage`, system
`/nix/store/xv1h49qrvmzmlnxd5inpcp3yfmcxbhc3-vpsadminos-system-vpsadminos-26.05.git.56b9363`,
8CPU/8192MiB (`cgv2-log.log:7–24`). **QEMU host PID688526/start155023243 is
not a guest container-init/attach PID.** No6.12.113 or NFS `.95.7` input is
substituted.

There is no standalone failed-container log ZIP member. Failure diagnostics
**do retain** `/tank/log/ct/kmisc-mknod-2d92.log.destroyed`: directory listing
`cgv2-failure-diagnostics.log:1937` records **zero bytes**, and its two captured
sections3953/3963 have **no content**. Thus a retained path exists but supplies
no attach record. Global `/var/log/osctld` entries provide these bounded facts
(all dated2026-11-05; displayed local time+0100):

| Event | Actual time / original retained anchor |
| --- | --- |
| Pool/user/group monitor starts |20:02:45.178050, diagnostics2055|
| Wrapper PID3394 reattached, then STARTING |20:02:46.430604/.466402, diagnostics2076/2078|
| RUNNING state recorded |20:02:47.638974, diagnostics2104|
| Block-device payload completes0 |20:02:47–50, cgv2-shell1.log171–175|
| Character-device exec returns1/ESRCH before proven payload |20:02:50–52, shell180–188; runner23/30–32|
| Existing prefix cleanup issues `ct del -f --prune` |20:02:54–56, shell205–209|
| Container exit0, STOPPING, STOPPED recorded |20:02:55.209758/.209832/.285551, diagnostics2274–2276|
| Exit promise / target pool-user-group monitor exits |20:02:55.598415/.975570, diagnostics2294/2309|
| Diagnostic date; target already absent from init_pid listing |20:02:56.203912210, diagnostics6/1613–1627|

These are monitor observations, not continuous init/namespace liveness proof.
The exit and monitor-stop records occur **after cleanup deletion begins**;
no pre-failure target exit or target restart is recorded. Do not infer that
cleanup caused or disproved the preceding attachment failure. The cleanup
command's shell status0 also includes `|| true` and is not promoted to proof
of every internal operation.

Numeric3394 is explicitly labelled **wrapper** (diagnostics2076/2077).
Numeric3455 appears only in the pre-mount idmapped user-namespace path
`/proc/3455/ns/user` (2094); it is **not identified as init or the failed LXC
attach target**. The later `ct ls ... init_pid` snapshot omits the deleted
mknod container. No retained numeric init/attach PID, starttime, namespace/pidfd
binding, target lifetime at failure or target restart record resolves that gap.
The exact `__attach_namespaces_pidfd:711`/`lxc_attach:1695` ESRCH output does not
identify the failed syscall/selected pidfd or prove `mknod` executed.

The finite completion criterion is met: this local artifact adds post-cleanup
monitor chronology and proves the retained target log is empty, while the
required target/lifetime fact remains **UNAVAILABLE**. Further observation or
exact packaged LXC source work requires the separately named lead release;
no wrapper or production/test behavior was implemented. No LXC/store/source/
network lookup, API/download/poll, Git/eval/check/build/VM, lifecycle action,
new utility or process was launched. All local read/excerpt commands terminal;
no owned process. SourceF stays frozen and session OPEN. Current sole watcher
is root's replacement `ci_final_resume`/handle85791; no CI observation by D.

## Current FINAL074 Intel representative-v5 retained runtime audit

**COMPLETE/PASS for this row's recorded original representative contract;
root ACCEPTED in the subsequent v6 assignment.** Only Intel representative-v5 of run42204546740,
attempt1, exact marker-free **074ca3882eaa2a26cbb446c37f97b6800d32cbb2** is
covered. ParentF56b9363/tree1c5fb6bc19e2713f70ec2311f5b44b8b841eed77,
lock67487674 and original profile367dd4ce are independently bound by the
read-only source guard; source/index are unchanged. Session/current/environment
and ready retained implementer2 Sol/xhigh/workspace-write match. Applicable
workspace/repository/patch-policy/verification/documentation guidance and the
original architect/current qualification contract were read or reused unchanged.
No old F/H/Hprime runtime, manifest, ABI or closure is used as new measurement.

### Immutable binding and actual selection

Saved `intel-repv5-complete-jobs.stdout` binds job **127853589353** to canonical
`vpsfreecz/vpsadminos`, PRIMARY branch, exact074/run42204546740/attempt1,
completed/success **2026-11-06 10:54:58–11:38:00Z** (43m2s), labelintel-kvm,
runner **gh-runner3.int.vpsadminos.org /10916**. Runner software version is
**UNAVAILABLE** in the supplied metadata/artifact. No old version is transferred.
Saved artifact metadata binds **13499900483**, exact name
`os-test-logs-42204546740-1-livepatch-intel-representative-v5`.
Independent whole-ZIP measurement is **1,209,495 bytes**, SHA256
`ac7a24ad65d7cddccfbab9b82ca4555f1feaacd0e4ce55c547a8370e61d91d12`.
All **15** members are safe unique normalized unencrypted relative regular
files, no directories/links/traversal. Canonical binding and safety preceded
body reads. Supplied job/artifact/download collectors have exit0/empty stderr;
D did not repeat collection or use any API/network operation.

Actual test.log1–4 selects **one script/one group**,
`kernel/livepatch-qualification@intel-representative-v5/default`; runner3–5
records **one example**, successful **216.23s**, script **245.97s**. Test.log10–13
records whole test **253.34s**, one successful test; result is
**expected_success**, no pending/skipped/failed example. Job elapsed time is
not assigned to a body phase. [Selected current-row evidence](package-d-final-marker-free-evidence/intel-representative-v5/)
contains tiny identity/sites/runner/result/console/launch files, original-line
windows, compact summary and index. The **362,595-byte primary shell** was
streamed: **7026 universal-newline lines/431 complete commands**. The second
shell is20bytes, only `SHELL: diagnostics`, **zero commands**. No full primary
shell/archive or8.8MB prebuild payload was extracted/read. Main114 bounded
windows are43,968bytes;46 probe/policy windows add17,107bytes. Original unabridged
payload remains in the retained ZIP.

### Current capture, manifest and guest inputs

All **six actual row fields** exactly match B's **FINAL074** build capture
(`package-b-final-marker-free-build-evidence/capture-notes.json`), without
using F values as an allowlist: Source074, Inputs
`67487674fa38049fede8047dbf8d7302971a3b19ea2866cf6f954e3a2e5ad656`, normal
Producer `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`, its
Module `/lib/modules/6.12.95/extra/livepatch_7.ko`, module bytes SHA256
`7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`, and Sites
`/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`.
Build measurement and the row's normal workflow guards supply that selected
producer/module binding; D did not download/re-hash production module bytes.
Production artifact remains metadata-only/outside this package.

This row's own5121-byte JSON independently hashes to
`093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`.
It supplies schema1/matching module SHA/ELF64 EM_X86_64/build_id
`fd8cbfe4c314ddac8f35d87bee4bb8b909e479d5`, **exact nine keys**, all finite
section/symbol/offset/instruction bounds, kinds/frames/inlines/callees and register
widths required by the actual consumer. ABI records are node0/timer56/lock96/
connect_worker1600 with valid ordering/bounds. FUSE original-callee hold/return
and TCP64-bit needed/32-bit mss+reordering contracts are present. These are
independent current manifest measurements, not an ELF/disassembly or loaded-memory
measurement; build capture alone did not print manifest SHA/roster/layout.

Actual guest guards at shell54/63/72/81/90 return0 for uname6.12.95 and
corrected/sites/exact released-v5 (`b31f6440…927984`)/v6 (`960b13f1…5efe3`)
file hashes. Exact v5 insertion/convergence succeeds (enabled1/transition0
at1377); v6 is forbidden1341/2921. v5 is replaced/removed2912/2930;
v7 is disabled/converged5632, removed5766 and absent5775. Expected absent
modules and bounded convergence polling are not rewritten as failures/zeroes.
File hashes do not claim an independently measured loaded module-memory SHA.

Actual launch `machine-log.log:7–24`: host PID **1981284**, start ticks
**160975437**, QEMU10.2.4 packagekanckc6l, frozen kernel
`/nix/store/050sh2hfrnpc8j5abr2npp7bnlxvpb8a-linux-6.12.95-frozen-boot/bzImage`,
initrdh3v4nwmsn39wph7apj7q6bg8hn58rv3x, **this row's** system
`/nix/store/3h49a59j22871539fxbh1gj9ghm1bij7-vpsadminos-system-vpsadminos-26.05.git.074ca38`,
squashfs4c6znic94xpm7356406ir7vzxgf2fysb. Direct boot/8cores/vCPUs/1thread/
1socket/8192MiB. This recorded path plus ordinary guest guard is the frozen-boot
proof scope; no independent running-image/notes digest or full guest source
revision was measured. The build toplevelg2dpq0rw is not substituted for this
actual launched guest system.

### Body assertions, health and recovery

All line anchors below refer to this row's primary shell; runner/console anchors
are explicitly labelled. Summary retains original command statuses/counters and
full-output hashes, rather than treating job green as assertion proof.

| Original representative requirement | Recorded outcome |
| --- | --- |
| Intel/KVM/resources | GenuineIntel960/getconf8 969/kvm_intel/device0; KVM smokes369/996/3341 print `kvm smoke passed`. MemTotal **8136192KiB** at1034 fits source90–100% of8192MiB. Two cgroup mems guards1702/1721 read back node0/effective0. |
| Population/age/progress | Ten running snapshots1776–5430: PID30180/16384tasks/ready16383/exact8 progress/perf/actualCPU fields; all18 counters strictly advance across every adjacent snapshot. Wakeups60→13951, fork_exec2→219. Actual host-monotonic age **67.1979172s**, profile minimum0, not14400. Five network counters441/440→717→788 with later post-replacement threshold checks passing; TUN10→243→348. |
| Original CPU hotplug before AND after | CPU7 offline/read0/online/getconf8 at2202–2229 and3103–3130 all0; original bounded fresh-progress waits and cumulative health complete on both sides (runner7–9/32–34). No health baseline reset after hotplug. |
| Shared admission/transition deadline | One successful candidate insertion2894/status0; total **2.4513382s** (runner10). Disable5569/status0, terminal convergence5632/status0; total **6.3519587s** (runner35). Each below the original shared **1800s** bound. No rejected insertion/EBUSY/failure-retention branch executes. |
| Original callback/admission probes |24 ordinary probes/3 insmod filters install successfully. Independent recount of both ordinary traces2939/5641 matches21 source-defined lifecycle/callback values per phase; all42 runner rows match, Intel SVM cb0 correctly0. Both per-CPU stats have16 overrun/commit-overrun values each, all0. Admission return rows retained, without lock-holder/errno diagnosis. |
| State/data/NFS/SCTP/TUN/patch state | Fixed NFS string equality2083/3359 and sync2092 succeed; held flock2101 returns required1; release5784/holder-gone5793 return0. SCTP readiness, no-early-exit, release/exit0 and TUN activity/exit0 pass. KVM and task patch_state=-1 at3350 pass. IPSET/NFT/bridge/netns/XFRM state is consumed after the replacement/disable. |
| Both active migrations | PID30180→A3467/status0/**0.07s**, →B4356/status0/**0.06s**; membership4041/5344, post-return fresh all-counter progress4109/5412 and health succeed. Original180s bound retained; all10 trace/policy cleanup/restore commands3476–5335 return0. |
| Strong stop/resource cleanup | Population/SCTP/TUN exit tests5829/5838/5847 all0; stopped5856/tasks1 5865. Stress stop5883/gone5901/pidfile removal5910 succeed. IPSET/NFT readback5919/5928 and bridge-down5943 plus all eight strong deletions5952–6015 return0. All48 ordinary event cleanup operations return0. Shared best-effort probes are not stronger unlogged postconditions. |
| Final health/completion/teardown |14 cumulative dmesg reads all0 from fixed baseline **539** (recorded prior counts538 at924/933); seven64-fork/6s RCU-delay cycles. No original fault-pattern match after baseline, including final body6024/6085 and shared-hook6461/6522. Shutdown diagnostic setup returns0 and successful source flow reaches completed=true. Poweroff7015/status0, console207 `Power down`; stop **11:37:42Z**, QEMUexit0 **11:37:50Z**, then killSIGNALNONE/destroy. |

Console45/66 retains Intel Spectre-V2/eIBRS/eBPF BHB warnings at guest11.638899/
12.345089s, **before** the example baseline. Existing common source2423–2431
explicitly establishes Intel/KVM before that baseline and retains this boot
diagnostic; replacement warnings remain covered. There is no whole-console-zero
claim, new suppression, warning waiver or health-score invention.

All **33 nonzero commands** are individually classified: initial DNS retry
then success; required absent modules/tlshd/held-flock results; bounded readiness/
progress/convergence/exit polling followed by the identical predicate's success;
and optional shared-cleanup absence probes. All431 commands have terminal
metadata. No actual example failure or incomplete primary/diagnostics command
is recorded; no blanket status-zero rewrite or invented errno branch.

### Measurement limits and handoff

The ordinary `sctp-hold` helper creates/binds/connects/accepts sockets, signals
readiness, waits for release, then closes. It exercises held association lifetime,
**not an SCTP data payload or post-transition payload readback**. TUN completion
counts/exit0, the fixed NFS string/flock and the actual state readbacks have their
source scope; no broader packet/data, NFS admission-barrier or unlogged readback
is invented. There is **no kprobe_profile/per-probe nmissed measurement** in this
successful single-attempt case; zero overruns and required callback counts do
not manufacture a zero-missed-hit result. Nine catalog contracts are validated,
but separate current-site FUSE/TCP/fragment/other main injections are outside
this one qualification example. Retention/EBUSY-negative branches, scale-aged
original14400, representative-v6, native, other rows and overall final acceptance
remain separately unqualified by this package. Old failure causes are untouched.

No source/check/test/eval/ELF/build/VM, API/network/download/poll, Git/settings/
node, lifecycle/cleanup or new utility action. All local read/record clients are
terminal, no owned process/waiting client; **capacity free, subsequently root accepted**.
Root retains sole overall watcher/reaper732/99892 and later artifact allocation.
Session OPEN; existing F/E/H/native/mknod histories and source freeze preserved.

Handoff transport note: `report_to_lead` completion message
`ad654611-697a-4299-b923-b3877ebd6803` returned “could not be confirmed” on
three exact same-ID/message attempts. Delivery is **unconfirmed**, not assumed
failed or acknowledged; retry this same ID if reconciliation is needed. The
complete audit above is retained locally, acceptance remains pending, and no
waiting client/process was left.

Root subsequently read the saved COMPLETE v5 receipt and explicitly accepted
it in the v6 assignment. The original reporting transport uncertainty above is
preserved; no further old-message retry or substantive v5 check was performed.

## Current FINAL074 Intel representative-v6 entire-row runtime audit

**COMPLETE/PASS for BOTH actually selected scripts; root acceptance PENDING.**
This is exact marker-free **074ca3882eaa2a26cbb446c37f97b6800d32cbb2**,
run42204546740/attempt1/PRIMARY/canonicalvpsfreecz/vpsadminos. It includes the
v6 qualification **and all65 native110 NFS examples**. No F/H/Hprime/v5 runtime,
manifest, ABI or guest closure is transferred. Session/current/environment and
retained ready implementer2 Sol/xhigh/workspace-write match. Applicable full
workspace/repository/patch-policy/verification/docs guidance, current original
qualification and reviewed provider/writer contracts were read/reused unchanged.
Frozen source074/parentF/tree1c5/lock674876/original14400/profile367dd remain the
assigned binding; D performed no Git operation or source/check/eval/runtime action.

### Independent row binding and complete selection

Saved `intel-repv6-complete-jobs.stdout` explicitly binds **127853589357**,
completed/success **2026-11-06 10:54:58–12:38:26Z**, runner
**gh-runner2.int.vpsadminos.org /4793**, labelintel-kvm, same run/attempt/head/
PRIMARY branch. Runner software version is **UNAVAILABLE** here; no old header
version is borrowed. Saved artifact metadata binds **13502991129**,
`os-test-logs-42204546740-1-livepatch-intel-representative-v6`.
Independent whole ZIP is **126,774 bytes**, SHA256
`55b17dfc04d9292a83980f77ef0782d1cb30057e7cd5d31bc7937e33a784d606`;
all **21** members are safe unique normalized unencrypted relative regular files,
no directories/links/traversal. Canonical binding and member safety preceded body
reads. Existing collectors are exit0/empty stderr; no download/API/poll repeated.

Actual prebuild descriptor line1 and test.log1–5 select exactly:

- `kernel/livepatch-qualification@intel-representative-v6`, arguments
  vendorintel/profilerepresentative/predecessorv6, empty testArgs;
- `osctl/nfs-cancellation-native110`, empty testArgs/templateArgs.

The unchanged NFS source tag explicitly places native110 on the representative-v6
row; this is ordinary selection, not an accidental additional baseline/default
consumer. Runtime order is native110 first, then qualification. Every ordinal
appears once with matching start/success: **65+1=66 examples, two scripts/tests,
both expected_success**, no pending/skipped/repeated/failed example. Shared
summary test.log94/99–101 reports native5651.56s, qualification268.02s, total
5919.58s/two successful tests. Job/prebuild/whole-test/example times stay distinct.

[Current-row selected evidence](package-d-final-marker-free-evidence/intel-representative-v6/)
retains tiny identity/sites/runner/result/launch/console files, summaries/index,
one descriptor line and bounded original-line windows. Qualification primary
shell was streamed **429,560 bytes/7526 lines/431 commands**; its20-byte diagnostic
shell is only a header, zero commands. Native110 primary shell was streamed
**959,998 bytes/32840 lines/3023 commands**. Neither complete primary shell,
archive or46,013-byte prebuild was extracted. Retained windows: qualification116/
46,820bytes plus probe-policy17,107bytes; NFS116/40,886bytes plus four exact
nested-writer/PID windows13,815bytes. Full originals remain in the immutable ZIP.

### V6 qualification: own current identity and original assertions

All six **this row's actual** identity fields equal B's FINAL074 capture:
Source074, Inputs
`67487674fa38049fede8047dbf8d7302971a3b19ea2866cf6f954e3a2e5ad656`, normal
producer `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`,
its exact `/lib/modules/6.12.95/extra/livepatch_7.ko` module, SHA256
`7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f`, and Sites
`/nix/store/aiqijlwh2w2wz79d6hvcqm1p9kzl4lv3-livepatch-candidate-sites`.
Own JSON independently measures SHA256
`093cf255a38db5275b62370da8bac1297781e48e2ae3245c1c5b5e1ceeb23ed1`,
schema1/matching moduleSHA/exact nine keys/ELF64 EM_X86_64/build_idfd8cbfe4…9d5,
ABI node0/timer56/lock96/connect_worker1600. Every bounded text/symbol offset/
instruction, kind/frame/inline, callee, FUSE return/hold and register-width contract
matches the actual consumer. No old manifest or unprinted build layout is used.

Guest guards shell54/63/72/81/90 pass uname6.12.95 and corrected/sites/released-v5
(`b31f6440…927984`)/v6 (`960b13f1…5efe3`) file hashes. Exact v6 inserts and
converges enabled1/transition0 at1344; v5 remains forbidden1326/2897.
Replacement removes v6 sysfs2888/module2906; v7 converges, disables and is
removed6266. These file guards do not measure loaded-memory module bytes or
independent running-boot/ELF notes.

Actual qualification launch `machine-log.log7–24`: PID **3711392**, start ticks
**160276291**, QEMU10.2.4/kanckc6l; frozen050sh2h…/bzImage, h3v4nwm…/initrd,
system `/nix/store/sjawj3jkwxpz7mhn5z22lykj6736php9-vpsadminos-system-vpsadminos-26.05.git.074ca38`,
squashfs4kh6v63f213j08gr74m43n2pawd1lml8. Direct/8cores/vCPUs/1thread/socket/
8192MiB. This system differs from v5 and no closure equality is inferred.

| V6 qualification contract | Direct original-shell evidence |
| --- | --- |
| Representative envelope | GenuineIntel945/getconf8 954/kvm_intel/device guards and KVM smokes369/981/3327 pass. MemTotal **8136200KiB** at1019 fits source range. Cgroup mems1669/1688 read0/effective0. Ten valid snapshots1743–5929 keep PID20946/16384tasks/ready16383/exact8 actualCPU/progress/perf fields. |
| Age/progress/network | Actual age **67.5779976s**, required minimum0. All18 counters advance across all nine adjacent reads; wakeups5→13583/fork_exec1→213. Five network counters293→571→642, TUN11→244→357 and later threshold/progress predicates pass. No original14400/scale-aged claim. |
| Pre/post loaded CPU hotplug | CPU7 offline/read0/online/getconf8 at2169–2196 and3080–3107 return0. Fresh progress2214/3125, runner phase completions and unchanged cumulative health pass on both sides. |
| Original shared transition bounds | One activation at2870/status0, total **2.3495534s**; disable6068/status0, total **6.5349615s**; each <1800s. No rejected admission/EBUSY/failure-retention branch executes. |
| Callback/probe integrity |24 ordinary probes/3 insmod filters install0. Independent recount of both traces matches all21 source lifecycle/callback values per phase;42 runner rows match, Intelcb0=0. Two ordinary stats reads contain32 total overrun/commit-overrun values, all0. No per-probe nmissed/profile measurement exists. |
| State/data/held work | NFS fixed-content2050/3345/sync2059 pass; held flock2068 returns required1; release6284/holder-gone6293 return0. SCTP association readiness/live/release/exit and TUN activity/exit pass. Task patch_state=-1 at3336 and KVM pass. IPSET/NFT/bridge/netns/XFRM state survives to consumption. |
| Both full migrations | PID20946→A3453/0/**0.07s**, →B4773/0/**0.06s**, membership4458/5843, fresh post-return progress4526/5911 and health pass under original180s bound. All10 migration policy/trace cleanup restores return0. |
| Strong stop and recovery | Exit0 population/SCTP/TUN6329/6338/6347; stopped6356/tasks1 6365. Stress gone6401/pidfile removal, state readback, bridge-down/eight deletions through6515 and all48 event cleanup commands pass. |
| Final health/completion/teardown |14 cumulative dmesg reads from **524** all0/no original pattern match; prior line counts523 at909/918. Seven64-fork/6s RCU-delay cycles, final body6524/6585/shared-hook6961/7022 and completed=true flow pass. Example219.2s/script256.7s/whole268.02s. Poweroff7515/0, console195 Power down; stop12:38:04Z, QEMU0 **12:38:15Z**, then SIGNALNONE/destroy. |

All33 qualification nonzero commands have explicit source roles: required
absence/held-flock negatives, initial DNS retry then success, bounded readiness/
progress/convergence/exit polls with identical-success successors, or optional
cleanup probes. Both consoles in this artifact contain **no searched original
fault pattern/call-trace/lockup/hung-task/segfault/corruption match**; no inherited
v5 boot warning is invented. Ordinary SCTP still tests held association lifetime,
not transmitted payload/readback. Separate FUSE/TCP/fragment/main injections,
loaded-memory SHA, nmissed and rejection branch remain outside this example.

### Native110 NFS: all65 actual examples and four real writer outcomes

The current script's65 unique names exactly match current source:16 per NFS
4.1/4.2/3/4.0, plus the one NFS3 legacy-server example. Actual execution order
is4.1→4.2→3→4.0. Each ordinal1..65 has one evaluation and one success; no
baseline/defaultNFS selection is invented. Four25-cycle examples take
798.53/788.80/787.02/793.22s. Script **5636.96s**, whole test **5651.56s**,
result expected_success. This is new074 body evidence, not Hprime acceptance reuse.

Source file independently hashes **a16c480099d6a7be08d8b5631c340d92b050e6e107993d2702329e78aa54612b**;
exact38-line writer **c17bc4c34fe480df26e5353f3342c48594bd83b63ce2819ee16b5f7fa157a2b6**.
Both nested shell-quoting layers of each **actual logged command** were decoded
without execution or token substitution. All four `-e` payloads are byte-equal
that current source; ordinary provider is
`/nix/store/hyrhia8cgzghr216z0r5wnbsqg7gbb9x-ruby-3.4.11/bin/ruby`.
Each nsenter target equals its own preceding init_pid result:

| NFS version | Preceding PID read → actual writer line / target | Writer / outer elapsed |
| --- | --- | --- |
|4.1|3327→3373 /13267|0.001s /0.28s|
|4.2|11334→11380 /43879|0.001s /0.25s|
|3|19469→19515 /75294|0.001s /0.28s|
|4.0|27486→27532 /106038|0.001s /0.25s|

All four commands exit0 and log **busy_count=0/outcome=success**. The exact
executed source's only success path requires unbuffered full2-byte `1\n`
syswrite, successful close, then immediate exact `File.read == "1\n"` before
success. This establishes actual control-flow/outcome barriers, not independent
syscall tracing. **No real EBUSY retry occurs**, and no F incident lock-holder/
errno branch is diagnosed. Original30s monotonic/50ms retry policy and enclosing
machine timeout remain unchanged; no blocked-write preemption claim is made.

All original example families complete for all applicable versions: outage/hard
retry and payload recovery; shared mounts/surviving neighbor; kernel-blocked
mount; graceful stop fallback; remote holder/waiter isolation; processless child
netns; irreversible admission/descendants; daemon restart/handle recapture;
unexpected init exit; dirty-file PID1 exit; exact modes/permissions; all-superblock
drain; corrected mount race; repeated-cancel idempotence; fresh-state restart/
remount;25 forced stop/restart cycles, plus legacy NLM server shutdown. Selected
current counters/output predicates supplement all65 source assertions:

- **8** payload cmp0 and **4** matching local/server SHA256 pairs;53 surviving
  neighbor writes0. All173 normal mounts0 have the immediate `/proc/mounts`
  hard/not-soft/not-softerr readback. Eight reachable admission refusals are
  required status32, elapsed2.38–3.14s under15s. Four racing mount drains return0,
  4.82–5.74s under60s.
- **153** stop commands0, **163** starts0;144 state reads (140stopped/4running),
  **108** fresh zero-state guards0, eight descendant readbacks exactly1/1,
  four processless namespace PID reads empty. All100 cycle0..24 writes0
  (each cycle four occurrences); four init-command resets and four retained
  child-netns release cleanups return0.
- All four600/600 and per-server644 mode predicates pass; tenant reads endrc1
  and writes are denied; terminal reset writes reject invalid0 as required.
  Four NFS sysfs/cancellation dmesg checks are empty. Eight daemon restarts,
  eight trace removals,20 explicit unmounts and304 ensure-rule-deletion
  commands return0. Source ensure/recovery is not replaced by a job-green claim.

Native110 statuses are **2828 zero +187 one +8 status32 =3023 commands**.
Every195 nonzero is classified against source:132 intentional unfinished-writer
negatives, one writer readiness poll then success, retained-lock/contender,
tenant permission/reset/legacy-I/O negatives, initial pool/export readiness or
stopped-state polls, and the eight expected admission refusals. No unexpected
example fail/pending/retry is recorded; no blanket status-zero rewrite. An audit
classifier initially omitted the quoted per-server permission command and an
inventory regex initially missed the indented legacy example; both analysis
parsers were corrected against actual source/output before conclusions.

### Native110 inputs, health and final two-profile disposition

Native guest own uname guard at shell128 returns0 and prints **6.12.110**.
Actual direct launch PID **3708786**, start ticks **159711134**, QEMU10.2.4/
kanckc6l, kernel `/nix/store/lmpawpr8hajsi87xj3fxmp97lzkm9bl4-linux-6.12.110/bzImage`,
initrd2dk12yviddyq27w26aimd8m7jnjxjiih, system
`/nix/store/kiyhxjmzx8sma9y7gb7m16y97dsxpwhr-vpsadminos-system-vpsadminos-26.05.git.074ca38`,
squashfsvkvfvss11s93fr225gqp7d5ammbjmzdn;4cores/vCPUs/1thread/socket/8192MiB.
These are this script's recorded paths/version, not qualification's frozen.95
inputs or Hprime's system. Source declares native livepatch service disabled;
no separate runtime service-status or loaded-module/site hash is measured.
Disk10G remains source declaration: omitted OTHER_ARGUMENTS supplies no runtime
size receipt. Source074/lock binding is current canonical job/row context;
full guest physical self-snapshot/sourceRevision/dirty/lock-byte measurement
is unavailable rather than inferred from the system version label.

All421 native console lines have no searched fatal/warning/trace/lockup/hung-task/
segfault/corruption signature. Original OSVM monitored checks and65 source body/
ensure hooks complete; no additional universal final-health score/assertion is
invented. Native poweroff records normal pool/container shutdown and unregister,
console421 Power down; stop12:33:32Z, QEMUexit0 **12:33:47Z**, then SIGNALNONE/
destroy. Qualification's own210-line console and graceful exit are accounted
above. Both actual VMs complete independently with no cleanup signal supplying
an apparent body pass.

| Current FINAL074 profile row | Actual scripts/examples | Audit disposition |
| --- | --- | --- |
| Intel representative-v5 /13499900483 |qualification1/1|COMPLETE/PASS, root ACCEPTED; prior reporting uncertainty preserved|
| Intel representative-v6 /13502991129 |qualification1/1 +native11065/65|COMPLETE/PASS for both, root acceptance PENDING|

This two-profile summary is D's bounded evidence result, **not whole CI/native/
main/aged or aggregate acceptance**. Original14400 is unchanged but inapplicable
to representative minimum-age0; no later v6 dependency or waiting client is
retained. Main semantic injections, defaultNFS/native/other rows/old fault causes
and root acceptance/integration remain separate. Production ZIP stays metadata
only. No source/check/test/eval/ELF/build/VM, API/network/download/poll, Git,
settings/node/lifecycle/cleanup/new utility/run/retry/integration action. All D
read/record clients terminal, no owned process; **capacity free**. Root sole
watcher/reaper732/99892 untouched, session OPEN.

Completion transport: one ordinary `report_to_lead` submission, message ID
`17507835-47e4-4a19-b6b3-08b41a687b04`, returned “could not be confirmed”.
Delivery is unconfirmed; no retry loop or waiting client was retained. Root can
inspect this saved COMPLETE receipt; reuse that same ID only if reconciling the
same report. Capacity remains free and acceptance pending.
