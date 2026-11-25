# Current-build livepatch test design

Owner: architect0, retained Astra/xhigh. Planning baseline is canonical
vpsAdminOS staging `dd188397abe37d0bc33f4c5dfb3605206ce5e326` in this session's
registered worktree. Session/environment binding and retained roster were
reverified. The user has now authorized the accepted implementation with
“implement it”; the lead confirmed the unchanged fresh staging baseline.
Architect retains design/document ownership and implementers own application
edits. Integration, deployment, lifecycle actions and input freezes remain
outside that authorization. Execution status belongs in the lead's state record.

## Current decision

Ordinary CI tests the current normal livepatch module. Capture its identity
once in the existing build job and verify the same bytes in every dependent
row and guest. Remove the historical candidate checksum allowlist. Preserve
exact released predecessor artifacts, frozen boot image/notes/ABI, independent
semantic expectations and original recovery behavior.

Precise witnesses also follow the current build. Use named probes where they
preserve the required semantic point; otherwise resolve and validate the finite
current-module sites from ELF relocations, inline DWARF and instructions. A
function entry cannot stand in for an internal call/arithmetic point without
preserving its argument, ownership and stack contract. Missing, ambiguous or
incompatible semantics fail clearly before probe installation. This tolerates
supported harmless placement/metadata/register changes, not arbitrary ABI or
source changes.

The actionable owner/file/dependency and acceptance brief is
[implementation-plan.md](implementation-plan.md). It keeps the existing test
matrix and current-build witness coverage. There is no producer-input freeze,
historical default lane or generalized instrumentation framework.

Exact FINAL074 `074ca3882eaa2a26cbb446c37f97b6800d32cbb2` is now integrated
into staging. Root accepted full CI42204546740, native323 scripts/109 groups,
all nine lifecycle audits and original14400 qualification before integration.
The separate automatic staging RSpec failure is assessed below. Earlier F/H,
provider-correction and temporary-run sections retain their historical scope;
they neither replace current acceptance nor waive their original failures.

## Current post-integration RSpec assessment

**COMPLETE: a caused unit-fixture omission; no implementation or retry released.**
Session/environment and live roster match the bound session; architect0 retains
Astra/xhigh/workspace_write/ready. This assessment reads saved evidence and local
source only. Integration of exact074 is complete, with the claim released before
CI observation; the accepted full-CI/runtime results remain valid for074.

**Bound evidence and actual failures.** Saved [run metadata](ci-final-marker-free-42204546740/post-integration-rspec-status.stdout)
and [job metadata](ci-final-marker-free-42204546740/post-integration-rspec-jobs.stdout)
bind RSpec42312639979/attempt1, push/staging, exact074, workflow256961877/rspec.yml,
job128217565806, FAILURE23:33:00–23:38:22Z on2026-11-06. The
[raw job log](ci-final-marker-free-42204546740/post-integration-rspec-job-log.stdout)
was independently verified before inspection:380349 bytes, SHA256
`e94facde6f2ca24780d1d924ea73d2de8e066d1e24810f5f7063c636c06d6141`.
Its [GET receipt](ci-final-marker-free-42204546740/post-integration-rspec-job-log.command.json)
binds the same job, exit0 and empty stderr; checkout log549–550 confirms074.

The failed step runs `nix develop .#vpsadminos -c bash
.github/workflows/scripts/run-rspec-all.sh`. Its final test-runner suite uses
the existing nested `.#test-runner` shell, `TMPDIR=/tmp`, Bundler/RSpec with
`test-runner/spec` plus the activation/restrict-dirs specs (wrapper96–106).
This is the hosted Ubuntu26.04.1 job, not a gh-runner guest. The log binds
Ruby3.4.11 z30 and RSpec-core3.13.7; the test-runner seed is44806. No claim of
equality with a local gem environment or VM closure follows from those facts.

Log3447–3669 reports exactly ten failures in
`test-runner/spec/test_runner/nfs_cancellation_kernel_release_spec.rb`:
all five release inputs for cumulative v7 and all five for native110.
Each raises at spec27 after `nix-instantiate --eval --strict --json --expr`
fails with **`attribute 'ruby' missing`**, common.nix853. RSpec loaded and ran
465 examples,10 failures; these ten fail during their fixture evaluation,
before executing the extracted uname assertion. The five unpatched-baseline
release cases pass. Log3713–3747 lists only test-runner as failed; all other
twelve suites pass, including osctld1576/1576. Expected fixture-error output
elsewhere is not another failed suite. The earlier local osctld preload
limitation is therefore not this job's failure.

**Causal boundary.** The spec19–23 constructs a deliberately minimal `pkgs`
attribute set containing only fake static-builder/writeScript paths and
`lib.optionalString`. It imports the common NFS file, evaluates the entire
`testScript`, then extracts and executes only its uname shell assertion.
074's fourth shipping purpose added the writer's `${pkgs.ruby}/bin/ruby`
interpolation without adding `ruby` to that fixture. Non-baseline script
evaluation now requires it; the baseline branch at common.nix273 excludes
the writer and does not force that attribute. Installing Ruby or changing
PATH cannot populate a literal Nix attribute set.

Read-only d2fe..074 comparison proves the dependency: the sole common.nix
change is074's +42/-2 writer patch; its base contains no Ruby interpolation.
The fixture is byte-identical at both heads, blob
`993bcf9f015f4ea4a1fc32fe03daae2051756b95`; rspec.yml, run-rspec-all.sh,
spec_helper.rb, flake.nix and flake.lock also have identical blobs. Thus this
is a **regression caused by the series' new caller dependency in an unchanged
unit fixture**, not an unrelated baseline failure, missing CI Ruby, Nix
installation failure or guest NFS/kernel failure. No base run was performed;
the source dependency and identical ten evaluation errors establish this
specific cause without claiming a historical whole-suite pass.

The [retained N-prime checks](package-a-result.md#n-prime-provider-correction-committed-review-accepted)
proved the real test/guest package provider and ran25 writer/parse/assembly
controls. They did not exercise this separate fake-package unit fixture.
Their accepted scope and full074 VM results remain intact; neither was Ruby
suite completion evidence. This is also distinct from H's unavailable
`ruby_vpsadminos` in the real outer test package set.

**Minimal follow-up brief for root allocation.** Sole owning repo/file is
vpsadminos `test-runner/spec/test_runner/nfs_cancellation_kernel_release_spec.rb`.
Add `ruby = "/unused-ruby";` to its existing fake `pkgs` set. Like the two
existing unused paths, it permits string interpolation only: the spec still
executes just the extracted uname command, never the writer or dummy Ruby.
Keep all15 positive/negative release expectations, strict evaluation failure,
real common.nix import and guard extraction unchanged. Do not catch/skip the
error, substitute the guard, import a full package environment, or change the
working production/test writer, provider, workflow, lock or any timeout.
No API/state/schema/deployment/recovery effect; rollback concerns only this
unit-fixture line and does not call for guest or node action.

After a separate release, quick proof is the existing15-example spec in the
declared test-runner environment, plus Ruby syntax/affected RuboCop and normal
hooks. Require all15 pass with the real Nix evaluator and no skipped examples;
the unchanged actual error is the negative evidence. Commit before independent
affected review (general and architecture lanes; low-risk nonexecuted test
fixture, retained reviewer settings), then the existing full RSpec command/job
must pass all13 suites, including the465-example test-runner batch. No new test
harness, fixture abstraction, provider bootstrap or kernel/guest build is needed.
Missing declared tooling, a new failure or a wider source delta stops for
assessment; no blind rerun or assertion/budget waiver.

074 is already merged: **never amend/rebase/rewrite074 or staging** to fold this
fix retrospectively. Prepare a normal successor test-fix commit referencing
the caused omission, retaining the four merged purposes and all provenance.
The affected packet must state this merged-history boundary and no migrations.
074's accepted full native+ALL9/original14400 evidence is preserved for that
exact head and unchanged product scope; it is not a new-head/closure certificate.
Root owns successor publication/integration and applicable final-head evidence
reuse. Both rspec.yml and full ci.yml match `test-runner/**`, so a normal push
can start both workflows: publication and actual run reconciliation need a
separate root decision, not an implicit full-matrix launch, filter edit or
cancellation. No duplicate-CI status was polled here. All read clients are
terminal; no owned process, source mutation or runtime action. Session OPEN.

## Current diagnostic authorization, November 4

The user directed: “you should indeed reduce the aging time until the
problems are identified and fixed”. The lead selected a **temporary
five-minute diagnostic age**. C's checked one-file change, 14400 to 300
seconds plus a comment, is now saved as
[package-c-diagnostic-aging.patch](package-c-diagnostic-aging.patch), SHA256
`c46380fdc1f05abd76fd975e25321d40ee2e37a15fdbcdb59c1ff42810554dde`.
Current source at reviewed/published
`645927e22809a29c67ffd59c072e553e05e2a72b` is restored to 14400 with that
comment absent. The saved patch is now used by the separate diagnostic head
`bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf` in run `41921632759`.
The 128-vCPU, 16-GiB,
100000-task envelope, strict health, full recovery, boot and predecessor
requirements remain. Restore **14400 seconds before final four-hour
qualification after the fixes**. A diagnostic green is not full aged
qualification and cannot replace that final evidence. The original profile
and its failure records remain preserved below.

The user also said “anyways, I'm updating all gh runners”. The operator owns
that update; this session has no runner activation, trust-repair or prebuild
package. A issued one cancellation for the known failed run `41865572140`;
the canonical result is completed/cancelled. Preserve its five lifecycle
passes, native failure and four cancelled lifecycle rows. The subsequent
focused run `41913307185` belongs to its existing acceptance receipt. Current
diagnostic run `41921632759` supplied the predecessor CPU-hotplug failure
and a distinct low-memory-v5 pass. The later one-row capture run
`41938327930` at `13b658f67c37418d6bbf91316ea7b3c6db99fe17` failed
observer setup. Its lifetime successor `b361b8c600bc1d50c237a68ca5413d38be9a0e99`,
run `41951210319`, obtained a complete healthy CPU127 snapshot and passed
pre-hotplug health, then failed activation with a loader/TLB/SMP softlockup
and later insertion timeout. No CI or watcher is active and no new run is released. The
[scheduler finding below](#diagnostic-scale-aged-v5-cpu-offline-warning)
does not establish a candidate-activation failure. Complete final
qualification remains unsatisfied.

D's deterministic shutdown reproduction now confirms the source-level race:
the focused three examples have two passing controls and one intentional red;
the three-file set has 24 examples, 23 passing and that same red. Its initial
environment block and the later five-minute declared-environment preparation
remain historical receipts. The user has now approved the
[production correction](#accepted-production-shutdown-coordination) as a
separate commit. Its implementation and quick checks are complete;
[committed independent review](shutdown-fix-review.md) passed all four lanes
with no findings, and the fix is published at 645927. This is not runtime
acceptance or proof of the failed VM's actual interleaving. The
[conditional next-phase route](#conditional-post-focused-diagnostics-and-final-qualification)
keeps shortened diagnostics before final four-hour qualification.

## Accepted runtime lookup correction, November 4

CI run `41740116653`, attempt 1, Intel main job `126293359412` reached the
fragment test at published head `48f2983e3cf6b5b72a21c254f744ad8e7d62a123`.
The native timer observation passed and v7 loaded with `enabled=1` and
`transition=0`. Candidate probe installation then stopped because the exact
name/module lookup returned two rows. This is a lookup-contract defect, not
evidence that the corrected timer ordering failed at runtime.

Evidence is retained in the verified artifact's
[runner log](ci-41740116653-intel-evidence/os-test-kernel__livepatch-inet-frag-144ad4d5/test-runner.log)
(line 8) and
[shell log](ci-41740116653-intel-evidence/os-test-kernel__livepatch-inet-frag-144ad4d5/machine-shell.log)
(lines 1100–1106). The addresses returned were `ffffffffc1c91f50` and
`ffffffff92f7fd20`. Its [site record](ci-41740116653-intel-evidence/livepatch-sites.json)
still binds SHA-256 `7c4d...8455f` to defined `livepatch_7:inet_frag_find`,
position 0, `.text`, size 1928 and probe offset 950. Architect independently
read the rooted current ELF: symbol 3422 is a local defined function in
section 13 (`.text`), value `0x44e50`, size 1928; symbol 5680 is a global
`NOTYPE`, `SHN_UNDEF` import of the same name, value/size zero. Exact module
qualification alone does not distinguish these entries after relocation.

C's [initial source and correction receipt](package-c-runtime-symbol-failure.md)
examined `elf_type()` only. Independent review found that this omitted the
final formatter; architect then read the complete relevant path at pinned
Linux `a2384967b90f24d2470c9eb15f0e66d938df7e08`:

- [kernel/module/kallsyms.c](https://raw.githubusercontent.com/vpsfreecz/linux/a2384967b90f24d2470c9eb15f0e66d938df7e08/kernel/module/kallsyms.c),
  lines 48–49, classifies the observed nonweak `SHN_UNDEF` import as `U`.
  `module_get_kallsym()` at lines 393–397 supplies that type and the export flag.
- [kernel/kallsyms.c](https://raw.githubusercontent.com/vpsfreecz/linux/a2384967b90f24d2470c9eb15f0e66d938df7e08/kernel/kallsyms.c),
  lines 581–584, transfers both into the iterator. `s_show()` at lines 742–752
  prints an exported module type in uppercase and a non-exported type in
  lowercase. The rooted candidate has no `__ksymtab` sections; this import
  therefore appears as lowercase `u` in `/proc/kallsyms`.

This type character is established from source and ELF evidence; the failed
guest query printed addresses only. The complete
[independent review](defined-symbol-review.md) reports one Blocking finding,
DS1, and reproduces both the lowercase-import ambiguity and import-only
mis-selection with the actual committed lookup methods.

The corrected bounded contract excludes **both `U` and `u`** in both existing
Ruby queries, for example `$2 != "U" && $2 != "u"`, before the unchanged
exact-one check. This is the pinned kernel's formatted type field, not GNU
`nm`'s unique-symbol convention. Require exact name plus `NF == 4`/exact module
for module lookup, or `NF == 3` for native lookup. Do not remove duplicate
defined rows even when their addresses coincide. Missing definitions and
multiple definitions continue to fail. Keep original FUSE callee position 1
and the existing accepted position values 0/1. The lead accepted this bounded
DS1 remedy after receiving the complete report and released C to correct the
same three paths and its evidence receipt.

This restores the already required **unique defined** symbol identity. The
digest-bound static resolver continues to validate executable section and
function size; runtime lookup selects its unique definition. No descriptor,
schema, section-relative symbol field or runtime section/core-range discovery
is required for this failure. Do not infer module ownership from address
prefixes or choose the first match. Do not restrict the shared helper to
`t`/`T`: it also resolves the legitimate data symbol `kvm_amd:x2avic_enabled`.
Only the two undefined-import spellings `U`/`u` are excluded; valid defined
text/data kinds remain eligible. This observation does not reinterpret other
type letters or widen the finite selector contract.

C owns the two lookup edits in `livepatch-6.12.95-common.nix` and
`livepatch-inet-frag.nix`, with regression coverage in the existing
`test-runner/spec/test_runner/livepatch_runtime_sites_spec.rb`. Test the actual
rendered AWK predicates with native `T`, target-module `t`, same-module `u`
(matching actual formatter behavior), uppercase `U` as a separate control,
unrelated/misnamed modules and defined data. Reject either-case import-only
input and two defined matches, preserving position behavior. B's resolver and Nix packaging
need no change. After quick controls and required review, the corrected
fragment witness must run and establish linked/locked current timer state
with zero missed events; then the required final-head CI must pass. The failed
run cannot establish that condition. There is no production, ABI, persisted
format or deployment compatibility change; rollback reverts this test-only
lookup change. Execution evidence remains in the lead's state record.

**Superseded uppercase-only decision:** the architect initially accepted
excluding only `U` and explicitly preserving `u`, based on the incomplete
`elf_type()` path. C implemented that decision and reported 53 passing consumer
examples after six regression failures, plus format/lint/parse checks. Those
results remain evidence for that version but do not validate the corrected
contract: the `u` preservation control was wrong. Review blocked unpublished
head `65d43eececbd0d13a3863c554e86e22680fbff84` before new CI. Preserve this
history and the receipt; replace that expectation with lowercase-import
rejection, then rerun relevant checks and committed review. Helper C and the
descriptor need no change. Actual fragment/final-head CI acceptance remains
pending. The lead owns focused inspection and review-finding reconciliation
after checks and commit; unaffected prior review evidence is reusable and no
automatic whole-branch review repeat is required by this design correction.

## Accepted baseline refresh onto 54b4313

The lead selected a standard patch-equivalent refresh from reviewed/published
`742eb30cb1a8b6766c85e915d26b0400e38244b1..5235bfd57c92bc05a25946937fe77f9803fe1c93`
onto canonical staging `54b4313404cea35b58ebb9df951ae75e27c44971`.
[A's incoming assessment](package-a-result.md#incoming-baseline-assessment-2026-11-04)
records the successful canonical SSH fetch: six incoming commits, eighteen
paths, and no overlap with the sixteen feature paths. This section is the
pre-refresh compatibility brief; it does not claim a refreshed head exists or
that it has passed checks. A owns the mechanical refresh and checks; the lead
owns review, publication, CI and any later approved integration.

The incoming CentOS/Rocky release-RPM updates do not alter the locked Linux,
livepatch, kpatch, overlay or fixture sources. Lock SHA-256 remains
`604e01bde4cf21e1532e9ed6e6cfb993da28439355ad7dceb5560447827c5baa`.
Nevertheless, `54b4313` changes shared runner/guest construction:
`RepositorySource` captures original commit and snapshot dirtiness using a
private index; the CLI scopes `TEST_RUNNER_SOURCE_INFO`; flake and direct
evaluation pass `sourceVersionModule` into `tests/make-test.nix`. OS version
and security-evidence metadata therefore change. `b19dbec8` also permits an
unknown channel revision. Disjoint feature files do not establish equal guest
or test closures.

The two identity contracts coexist. The existing build job still captures
checkout/lock, normal producer/module/SHA and sites once; every dependent row
must verify that same tuple. Runner source metadata describes the immutable
source snapshot used for evaluation and must not overwrite the captured
module digest or substitute for a host-to-guest byte check. For a matching
vpsAdminOS provider, guest revision/dirty/version suffix and security evidence
follow that snapshot. Foreign provider identity, unknown identity, explicit
overrides and legacy framework behavior remain as the incoming baseline
defines them. A clean Git index alone does not prove `dirty=false`: included
untracked/ignored snapshot files count. Invocation environment values must be
restored on success and exception.

The [refresh check package](implementation-plan.md#baseline-refresh-check-package)
uses the new baseline's existing source-capture/CLI/direct-framework specs and
two standalone evaluation checks, plus one bounded derivation/output tuple
comparison. Reuse earlier ELF, resolver-control or SDK/helper receipts only
for their exact unchanged artifact/tool/source identities. A changed producer
identity requires inspection and current-build qualification, not restoration
of an old checksum allowlist. Whole guest/test closure equality and old-head
runtime acceptance are not implied. Substantive conflicts, changed feature
patches or unexpected local kernel/old-Nix builds return to the lead.

After the refreshed head is committed and quick checks pass, require affected
independent review of source capture through guest metadata, the once-captured
livepatch identity interface, the preserved feature patch and complete final
history/no-migration conclusion. Reuse unaffected review evidence. Then require
full CI at the **exact refreshed final head**, including native and all nine
lifecycle rows and their semantic witnesses. Existing run `41773470432` and
the native-only run with ID prefix `418112` are evidence only for their recorded source/image identities; they
are not blanket new-head proof. The latest-image device-unit case remains
blocking. The four RPM bumps do not establish mutable OpenSUSE image identity;
the published 16.1/latest image still requires the ongoing/final verification.
The unchanged wrong-image negative-control PATH gap is retained as an existing
limitation, not an expansion of this refresh.

No new production schema, API, persistent format or coordinated node update
is introduced by the refresh. Preserve the prior tested ref/range and source
receipts for recovery; A must not silently resolve substantive conflicts.
Conditional approval for vpsadminos/staging persists only for an unchanged
feature patch and remains gated on required complete final-head CI. Neither
this design brief nor current partial CI satisfies that condition.

## Native early-boot failure: bounded next verification

The refreshed head `ad8991fe6d48ec06fb7cf7d64f15af7578d37e7a` passed its
quick checks and [affected source-identity review](source-identity-refresh-review.md).
It is not final-CI or merge ready. D's
[updated-image native diagnosis](native-lineage.md#updated-image-native-run-41811208607-boot-readiness-failure)
establishes that all six old explicit 16.1 cases and latest device units
actually pass at old head `5235bfd...`. That old-head image block is closed
for the observed inputs. Three new failures share one cgroup-v1 VM that never
reaches a test shell; all fail in boot/pool readiness before CPU/memory/tmpfs
assertions. The configured kernel is unstable 6.18.49. Neither the prior
successful same-head cgv1 nor the responding cgv2 proves complete input
equality or classifies the failure as flaky, resource-related or a regression.
Old artifacts omit the generated launch tuple, so no next check can recover it.

**Current decision: the lead selected the finite OSVM logging fallback and
released D's four-file implementation package.** The
[complete configured-cache preflight](native-lineage.md#complete-cache-preflight-material-guest-image-builds-required)
succeeded as a query but planned 55 builds, including two material mksquashfs
guest images, two OS systems and Ruby outputs. No kernel or old-Nix build was
listed; the full required closure was nevertheless not warm. This establishes
the configured-cache material requirement at query time, not an outage or
absence from every remote cache. No local realization, copy, build or VM ran;
the owned old5235 detached checkout is retained. The reviewed ad899 feature
patch remains unchanged. The observational delta is committed as
`dc74bcdadef75f181934bad2178afb589c34644c`, and its
[final affected review](osvm-boot-evidence-review.md) passed. A owns the later
2951 baseline refresh/check package; that refresh remains pending here.

**Historical first route, stopped at preflight:** one existing debug boot
conditional on cache-only preparation. D owned the diagnostic and receipt; A owned
serialized exact-source preparation. Use exact `5235bfd...`, its CI test
configuration and `kernel/vpsadminos#cpu-view-cgroups-v1`, leaving reviewed
`ad8991fe...` untouched. Inspect the selected unstable-kernel/test closure,
not the unrelated frozen-.95 local barrier. Stop if required material outputs
are unavailable without a kernel, old-Nix or other heavy build. A cache miss
is an environment result, not a reason to create another build project.

The existing route can improve evidence without product edits.
`Command#debug` builds the prepared `config.json` and enters
`TestEvaluator#interactive`; its Pry context retains the owned machines until
exit. Public `cgv1.start(wait_for_boot: false)` followed by a separate
`cgv1.wait_for_boot(timeout: 1200)` permits capture before and after a boot
timeout. Waiting inside `start` would invoke its existing rollback path; do
not use that shape or `start_all`. `qemu_pid`, `config` and `qemu_command` are
protected, not public APIs. Read the prepared file and, only in this diagnostic
Pry context, inspect the owned object's PID read-only; no new API is needed.

Capture only selected launch inputs and bounded host facts: source/test
identity, prepared config digest, resolved QEMU/kernel/initrd/system/squashfs
paths, kernel/initrd digests, CPU/memory/boot mode, approved nonsecret boot
parameters, owned QEMU PID and process start time, executable identity and
small status/task-state samples. Confirm PID ownership before and after
sampling. Do not retain raw configuration, arbitrary argv, environment or
credential-bearing extra options. Preserve the ordinary console/shell/machine
logs. The original timeout remains a failure; a read/collection error must
not replace it. No QMP, guest register inspection, kernel command-line change
or altered recovery behavior is part of this check.

This single attempt answers whether a stall recurs with **recorded new launch
inputs** and whether that owned process remains alive or exits. A successful
boot establishes that diagnostic's readiness only; it does not explain or
erase the old failure. Stop after one attempt and report the inputs and result.
If the cache route is blocked or the result leaves the failure unclassified,
do not substitute a blind full-CI retry. The bounded fallback before fresh CI
is conventional, shell-independent launch/failure evidence in existing OSVM
logging, as specified in the implementation plan. The complete preflight met
that stop condition; the lead has now selected this already-bounded fallback.
The debug recipe above remains history, not a release to resume local checks.

The selected fallback needs no QMP framework, runner API or new mode. D owns
`osvm/lib/osvm/machine.rb`, `machine_log.rb` and their two existing specs:
record an allowlisted launch identity at spawn and a bounded host snapshot
when `wait_for_boot` raises, before control reaches the after-script hook that
skips guests lacking a shell. Keep helpers nonpublic and use the existing log
artifact. Preserve the exact exception, spawn arguments, deadlines, process
ownership and teardown. D's quick checks, A's separate purpose commit dc74 and
the affected independent review are complete; the later baseline refresh and
exact-final-head CI remain pending.
This is a test-host diagnostic change, with no guest ABI, persisted production
state or fleet rollout implication. Final new-head full native and nine-row
CI, including all semantic witnesses, remains required.

## Packaged dependency baseline refresh onto 2951a63

Current reviewed, unpublished range is
`54b4313404cea35b58ebb9df951ae75e27c44971..dc74bcdadef75f181934bad2178afb589c34644c`,
with the sixteen-file livepatch commit followed by the four-file OSVM
observation commit. [Final affected review](osvm-boot-evidence-review.md)
passed. A correctly stopped publication
when canonical staging advanced to `2951a632c4254a44747a8da326e3dde897eaa0e2`;
the remote feature remains `5235bfd...`. No new refreshed head is claimed here.

**Disposition: the lead accepted go for the bounded mechanical refresh and
checks below; no further architecture approval is needed.** The sole incoming canonical commit changes
only `os/packages/osctl-env-exec/Gemfile.lock` and `gemset.nix` (+3/-3):
`rake-compiler` 1.3.2 to 1.3.3 and its matching gem hash. None of the twenty
feature files overlaps. Keep both independently meaningful feature commits,
their messages and exact file blobs; a substantive conflict or patch change
returns to the lead. The incoming canonical dependency update is not folded
into or reverted by this feature.

This is a real packaged input change. `os/packages/osctl-env-exec/default.nix`
uses `bundlerApp` with that directory as `gemdir`;
`tools/osctl-env-exec/osctl-env-exec.gemspec` declares `rake-compiler` among its
runtime bootstrap dependencies. Its unchanged executable delegates to
`Process.exec(*ARGV)`. The overlay exposes this package separately. No direct
selection of it in the inspected guest/test modules was found; do not infer
that every guest executes it or that the changed dependency is build-only.

There is also a concrete broader build-input path:
`os/packages/ruby-source-gem-config.nix` assigns the entire `repoPath` as
`src` for the source-backed OS gems. The incoming files therefore change the
source input used by ordinary guest packages such as osctl/osctld even when
their own Ruby files are identical. Channel construction copies `os/` when
enabled (QEMU/ISO; test base defaults it off), and the refreshed commit changes
captured source/version metadata. Whole guest/build-closure equality is not
claimed. This is compatible with the existing source-identity design and
requires final-head build/runtime validation, not a local gem-update project.

The host runner instead uses `test-runner/nix/{Gemfile,runner-deps.lock,gemset.nix}`;
the local spec bundle uses `test-runner/Gemfile{,.lock}`. Those files, declared
Ruby/native inputs, OSVM/runner/spec sources, `flake.lock`, Linux/livepatch/
kpatch/overlay sources and livepatch fixtures are unchanged by the incoming
commit. D's 81/207 and A's 99 checks can retain their original receipt scope
after exact source and execution-input comparison. Packaged runner identity
may still change through source-path references; that does not turn reused
host unit checks into a fresh packaged-runner or VM pass.

The [execution addendum](implementation-plan.md#packaged-dependency-refresh-onto-2951a63)
requires equivalence/history and lock consistency checks, one refreshed-head
ten-field livepatch/SDK comparison, and a small package/runner identity
evaluation. Reuse parser/ELF/helper evidence only where its exact artifact and
tool identities still match. No source/ABI/API/persisted-state migration or
coordinated fleet update is introduced. The incoming gem's behavior and bytes
are not independently qualified by its version label or this source review.
Affected independent baseline assessment precedes publication, using the
existing full review rather than repeating unrelated audits. Exact-final-head
full native plus all nine lifecycle rows and witnesses remain required. The
old cgv1 boot failure remains unclassified and unwaived; new logging improves
future evidence and does not explain the old stall. No old CI result transfers
to the new head.

## Old aged-v5 loader liveness failure and current-run disposition

Historical disposition before the native failure and later user steering:
the lead accepted **GO for the already launched exact-e175 run
`41865572140`**, retaining every existing qualification gate. That decision
authorized no cancellation, retry, new job or source change. The run has since
been cancelled once and is canonically completed/cancelled; see the
[current diagnostic authorization](#current-diagnostic-authorization-november-4).
A green result at the full qualification profile
would qualify its recorded inputs; it would not explain or waive the old
fault. There is no additional requirement to explain every historical failure
before a fresh head can qualify. Final acceptance still requires the complete
exact-head native/nine-row outcomes, semantic/identity/recovery checks and
the lead's current-target/history checks under the user's conditional approval.

[C's triage](package-c-old-aged-v5-triage.md) establishes a real failure in
old `5235bfd57c92bc05a25946937fe77f9803fe1c93`, run `41773470432`, aged-v5 job
`126392676352`. Verified artifact `13339254852` has SHA256
`d3c122101b7b02caeb56e5cf4c14aa2e0eae42527877ce3e55bd9a759d40341c`.
At guest uptime `14925.356780`, CPU25 reported a soft lockup in `insmod:9997`
on `6.12.95.5`. Activation eventually completed in 1061.789 seconds under
the 1800-second ceiling and callback counts matched, but the cumulative
health check after CPU127 hotplug correctly rejected the prior fault at
15:50:30Z, more than 26 minutes before the cancellation request. Later RCU,
stack-recursion and hung-task reports are retained, not treated as independent
proof of the initiating cause. The envelope was 100000 tasks, 128 vCPUs,
16 GiB and more than four hours under the exact v5 predecessor.

The owning invariant is **kernel health throughout the declared lifecycle**,
in addition to transition completion and callback counts. The health baseline
must continue to cover aging, activation and hotplug. Neither eventual
progress nor the fact that the assertion follows hotplug makes the earlier
loader fault acceptable or establishes hotplug as its cause.

The bounded local source inspection used pinned Linux
`a2384967b90f24d2470c9eb15f0e66d938df7e08` from the canonical local object:

- [`kernel/module/main.c`](https://github.com/vpsfreecz/linux/blob/a2384967b90f24d2470c9eb15f0e66d938df7e08/kernel/module/main.c#L2749)
  calls `module_enable_text_rox` during `complete_formation`, holding
  `module_mutex`, before `prepare_coming_module`/`klp_module_coming` and
  `do_init_module` for this load.
- [`strict_rwx.c`](https://github.com/vpsfreecz/linux/blob/a2384967b90f24d2470c9eb15f0e66d938df7e08/kernel/module/strict_rwx.c#L32)
  and [`set_memory.c`](https://github.com/vpsfreecz/linux/blob/a2384967b90f24d2470c9eb15f0e66d938df7e08/arch/x86/mm/pat/set_memory.c#L2118)
  establish text permissions. The captured `do_flush_tlb_all` path uses
  [`flush_tlb_all`](https://github.com/vpsfreecz/linux/blob/a2384967b90f24d2470c9eb15f0e66d938df7e08/arch/x86/mm/tlb.c#L1093),
  which synchronously calls all applicable CPUs.
- [`smp_call_function_many_cond`](https://github.com/vpsfreecz/linux/blob/a2384967b90f24d2470c9eb15f0e66d938df7e08/kernel/smp.c#L785)
  queues per-CPU call-single-data (CSD) work and waits for its lock to clear;
  the reported instruction bytes are consistent with that flag-wait loop.
  The trace locates stalled cross-CPU progress in loader permission/TLB work,
  not a demonstrated candidate callback failure. It does not prove which
  target/call stopped progressing or why, nor exclude predecessor/system
  interactions.

Existing watchdog all-CPU NMI stacks already cover the fault interval.
Qualification enables that capture. Its rolling CSD trace currently starts
only in the later `qualification_move_population` phase, which this attempt
did not reach. Thus no correlated queue/entry/exit history establishes the
loader's target CPU, callback identity or completion progress. The other
missing discriminator is time-aligned host/QEMU-vCPU scheduling evidence:
owned PID/start identity, vCPU-thread association and CPU/run-queue-delay
deltas at the event. The later guest load/memory snapshot supplies neither.
Host starvation, a kernel defect and a causal role for the large population
remain hypotheses; no resource/flakiness classification is justified.

[A's published-head and identity receipt](package-a-result.md) binds e175 to
`e1751c917f216897292ab0b893727a6e5553a540`. The ten-field livepatch/SDK tuple,
actual module SHA `7c4da9d6…e8455f`, site SHA `093cf255…23ed1` and relevant
qualification source remain unchanged in their recorded scope. Refreshing
the baseline and adding boot-wait observations supplies no demonstrated fix
for this loader stall. Source/version metadata and packaged guest inputs do
change, so these scoped equalities are not whole-VM/input equivalence. New
OSVM boot-failure snapshots do not observe an activation several hours after
a successful boot. Another outcome is fresh qualification, not a causal
experiment explaining the old failure.

The original disposition required no application package merely to let that
run conclude. For an analogous loader fault, the next owner gets the finite
[diagnostic trigger](implementation-plan.md#old-aged-v5-liveness-verification-disposition):
early-loader CSD target/progress plus aligned host/vCPU scheduling evidence,
retaining existing NMI capture. This loader finding releases no speculative
instrumentation, automatic expensive repeat, warning exclusion, input freeze
or kernel/recovery change. The user's later temporary diagnostic-age decision
above supersedes the prior no-age-reduction boundary only for diagnosis.
Quarantine and deployment limits remain unchanged.

## Exact-e175 native shutdown failure: bounded reproduction

The current native job `126712393207` in exact-e175 run `41865572140` fails
required cleanup. [D's complete triage](native-lineage.md#exact-e175-native-run-41865572140-shutdown-failure)
binds verified artifact `13353660471`, 2029818 bytes, SHA256
`5a52eb6403cc8d8d926657f2fa421d1d10ace8369799d124420e528b70277536`.
All 323 selected script bodies pass; 108 of 109 terminal groups succeed.
`osctl/ct-passwd` completes its body at 17:44:55Z, then fails its 900-second
QEMU exit wait at 17:59:58Z. QEMU exit 0 follows cleanup TERM and is not a
successful guest shutdown. This is an actual current-head blocker, separate
from the old cgv1 boot and aged-v5 loader faults. The run subsequently reached
canonical completed/cancelled after A's single cancellation; five lifecycle
passes and four cancelled rows remain recorded. No new long run has begun.

The selected shell log records the initial `poweroff -f` invocation reaching
pool export, stopping both containers and unregistering entities. The later
console reaches stage 3, then reports one `pool_import` holder and 897
`self_shutdown` holders while trying to grab tank. These records do not
identify the daemon PID/restart sequence, the holder thread or command
instance, whether that holder completed export, or its blocked operation.
The successful body precedes `TestEvaluator#do_run` cleanup, so the existing
unexpected-script failure hook does not collect this stop failure. The new
OSVM boot observation correctly records launch identity; it is not a
shutdown-thread diagnostic. No claim of feature causation, resource pressure
or flakiness follows.

The inspected source establishes this **possible interleaving**, not its
occurrence in this artifact:

1. `Daemon#setup` serves client requests before importing pools, then checks
   the shutdown marker and may run `Self::Shutdown` on its setup thread.
   Stage 3 separately invokes `osctl shutdown --force`; both the CLI and
   `Self::Shutdown` create the persistent marker. Thus client and setup
   shutdown commands can overlap around import. A restart is not required
   to construct this interleaving, but this incident's restart history is
   unknown.
2. `Self::Shutdown#grab_pools` retains a cloned pool list. If a different
   thread owns a pool manipulation lock, it catches `ResourceLocked` and
   retries that retained object once per second.
3. The winning shutdown manually acquires the pool lock. Its synchronous
   nested `Pool::Export` re-enters the same lock on the same thread, removes
   the pool from the database and returns. `ManipulationLock#acquire`'s
   already-owned branch deliberately does not release the outer hold;
   successful shutdown has no matching pool-lock release. A live winning
   thread can therefore retain that lock after the pool leaves the database.
4. A losing shutdown with the earlier list can continue retrying the removed
   object. The `self_shutdown` string identifies a command kind, not a
   thread: same-thread re-entry would succeed rather than raise this error.

Owning paths are `osctld/lib/osctld/{daemon,manipulable,exceptions}.rb`,
`commands/{base,self/shutdown,pool/import,pool/export}.rb`, `db/list.rb`,
`osctl/lib/osctl/cli/self.rb`, `os/modules/config/runit.nix`, and the
existing runner stop/ensure paths. The published feature inventory changes
OSVM observation and livepatch testing, not these osctld lock/command paths.
That source boundary does not prove identical guest inputs or exclude timing
effects; no baseline or feature attribution is established.

The lead initially selected only a cheap, deterministic **test prototype/reproduction**
owned by D, described in the
[execution brief](implementation-plan.md#exact-e175-shutdown-unit-reproduction).
That initial package released no production fix, runtime logging framework
or long retry. The reproduction subsequently confirmed the modeled defect;
the user has separately approved the correction below. Neither proves
that the recorded VM took this interleaving. Runtime attribution, if later
needed, requires the actual daemon/thread/command/holder and export-progress
facts; current `debug_thread_list` lists reaper-managed threads and does not
by itself identify the setup-thread holder. The lock registry describes
inclusive/exclusive locks, not manipulation-lock ownership.

The reproduction itself changes no API, persisted state, guest configuration,
deployment or recovery behavior. The separately accepted correction below
changes production shutdown concurrency within its explicit four-file scope.
Do not substitute a ready/initialized wait in the password test, force-release
another thread's lock, increase timeouts, skip cleanup or count TERM as success.

## Accepted production shutdown coordination

**User accepted; implementation active as a separate production-purpose commit.**
The user answered **“Fix here as a separate commit (Recommended)”** to the
current-chat `request_user_input_async` call
`call_7ccafe3d4e8749109837706d8a32a8c7`, whose question covered this osctld
shutdown race, coalesced requests, preserved abort/errors/export hooks and
full CI. The lead released D's complete four-file implementation and quick
checks. A retains later separate-commit/publication and focused-CI routing;
the architect owns prose only. The approval changes production-fix scope,
not runner-update ownership, final qualification or conditional merge gates.

D's frozen prototype changes only `heavy_system_spec.rb` (+167 lines, source
SHA256 `ffbf243eb5bb1404961ed1495c6b8429f285cd9a60a34742772a8dd9cf4d9925`).
The [focused progress receipt](package-d-shutdown-unit-focused-progress.exit)
and [three-file receipt](package-d-shutdown-unit-three-files.exit) retain the
intentional red: the live winner completes real export/database removal;
the loser retries its retained object with the real `self_shutdown` holder.
Both threads join and the fixture pool is unlocked during controlled abort
cleanup. This proves the constructed source defect. The failed VM's actual
winner, daemon restart history and export completion remain unknown.

Implement **one active shutdown operation per daemon**, admitted before any
pool/container snapshot. Concurrent callers join that operation and receive
its completed success or failure; they do not start overlapping exports or
automatically restart an aborted operation. A later request after completion
may start a new operation using the live database. This is a private
shutdown-specific mechanism, not a general command scheduler.

`OsCtld::Daemon` owns one process-lifetime mutex and condition variable,
initialized with the daemon, plus the current operation's small in-memory
completion record (`done`, `result`, `error`). An internal
`Daemon#run_shutdown { ... }` admits an owner or waits on the captured active
record. Waiters retain that record even if another operation starts before
they wake. The owner runs pool/container work outside the mutex; the active
record excludes a second owner. This leaves the independent abort command
able to run. Publish completion and wake all waiters on ordinary success,
abort or exception; do not strand the gate or report an interrupted attempt
as successful. No public command option, protocol field or persisted record
is added.

`Self::Shutdown#execute` delegates through that entry point to its existing
shutdown body. Only the owner begins shutdown, resets its abort flag and
performs export. Keep the existing marker and mode meanings: pending 000,
confirmed 100; the CLI's pre-request marker still protects restart recovery.
Coordinate abort/confirmation and result publication under the same brief
mutex section so an abort accepted during the active operation cannot be
overwritten by a waiting duplicate or followed by successful confirmation.
All joined callers observe that abort. Abort removes the marker; an ordinary
non-abort failure retains pending restart intent. A fresh explicit request
after abort may begin again. A process restart loses only the in-memory gate
and resumes from the existing marker as before.

Maintain command-owned lists from the first successful acquisition and release
still-owned container/pool holds in `ensure`, before publishing the operation's
outcome. This includes partial acquisition and exceptional exits. Nested
export's same-thread re-entry remains unchanged; already released container
holds are skipped. Never release another command's lock or change global
`Manipulable`. Keep the initiating exception if cleanup also fails. This
bounded lifetime belongs to the shutdown operation, not the longevity of its
client or setup thread. Abort does not newly re-enable pools or roll back
completed exports; retain existing recovery semantics.

Reject pending-list reconciliation as the complete fix. Real `Pool::Export`
removes its pool from `DB::Pools` **before** `SendReceive.deploy` and the
post-export hook; `Self::Shutdown` confirms only after exports return. A
waiter that drops the absent object could confirm shutdown and let stage 3
continue before that work completes or fails. A mutex that simply starts
every queued request anew also permits a duplicate to reset an accepted
abort. Joining the active result is the small conventional boundary that
preserves both completion and abort semantics without adding durable state.

Production changes are limited to `osctld/lib/osctld/daemon.rb` and
`osctld/lib/osctld/commands/self/shutdown.rb`, with existing focused specs
and short comments at those owning methods. No pool/import/export, generic
lock, CLI, runit, test-runner, VM or runner-infrastructure behavior changes
are included. There are no migrations, stored-data format or external API
changes and no coordinated fleet update. Older clients keep the same
success/error contract; a joined client may receive no intermediate progress
until the owner completes. Restarting/upgrading a live daemon is not authorized
here and must not be proposed as recovery for an active shutdown. Code rollback
retains the same state/marker format but restores the old race risk.

The [accepted package](implementation-plan.md#accepted-shutdown-fix-acceptance-and-scope)
is implemented, reviewed and published at 645927; the subsequent diagnostic
cycle is now running. Keep the shutdown fix separate from C's saved temporary
300-second diagnostic-age change. Follow the diagnostic cycle below before
final four-hour qualification; full exact-head native plus all nine lifecycle
rows, semantic/identity/recovery and existing conditional merge gates remain.
The operator owns all runner updates. No instrumentation or infrastructure
package is added by this approval.

## Conditional post-focused diagnostics and final qualification

### Current final-F native blockers

**Design assessment COMPLETE; both native failures remain blocking.** Shipping
preparation and ALL4/HIGH review completed for
`56b9363db1f1039e5d684dadc260cdffe7497e08` (F), base d2fe, lock
`67487674fa38049fede8047dbf8d7302971a3b19ea2866cf6f954e3a2e5ad656`.
The [final shipping review](final-shipping-review.md) is a source/history
assessment, not native acceptance. [A's full native audit](native-lineage.md#current-final-f-native-audit)
accounts for run42079730277 attempt1: 321/323 scripts and 107/109 groups pass.
That run is now terminal FAILURE and root has accepted all nine lifecycle
audits at their actual scope. The former sole watcher is terminal; this
assessment performs no CI observation or operation.
Retain F, all refs and original14400/full native+9 requirements unchanged.

The two failures have different source boundaries:

| Failure | Proven boundary | Smallest justified next package |
| --- | --- | --- |
| `kernel/misc#misc-mknod` | Exact pinned LXC source maps ESRCH to `setns` on the monitor-supplied init pidfd, before payload creation. Actual cgv2 guest is **6.18.49**, 8CPU/8192MiB. | Source prerequisite complete; current test/logging route cannot bind the failed pidfd target. Hold the insufficient snapshot wrapper and any retry or production correction. |
| `osctl/nfs-cancellation#default`, NFS3 race62/65 | The direct `shutdown_tree` write returns EBUSY on actual6.12.95.7. The kernel explicitly has a retryable pre-barrier path; the daemon handles it, but this test issues one shell echo. | One-file test correction implementing the existing errno-specific, success-required protocol; no kernel change. |

**Attachment boundary.** `tests/suite/kernel/misc.nix` runs the shared
`kernel/vpsadminos/misc.nix` scripts with six script jobs. The shared
`common.nix` explicitly selects the unstable6.18 downstream kernel and cgv2;
the saved launch is `/nix/store/x64477x3mxlzqkmvijvakf33an9vcbrz-linux-6.18.49/bzImage`
and system `/nix/store/xv1h49qrvmzmlnxd5inpcp3yfmcxbhc3-vpsadminos-system-vpsadminos-26.05.git.56b9363`.
The mknod script creates/starts one uniquely prefixed container, runs both
device examples, then deletes its own prefix. Its block example passes;
`kmisc-mknod-2d92` character example fails in2.53s at
`__attach_namespaces_pidfd:711` / `lxc_attach:1695`.
`ContainerControl::Commands::Exec` selects running execution and
`ContainerControl::Runner#lxc_attach_command` forks/execs `lxc-attach`, then
propagates its wait status. There is no payload retry or evidence that
`mknod` ran. Neither a device permission defect nor container exit, PID reuse,
namespace lifetime race, scheduling cause or shutdown regression is established.

**Completed exact-source prerequisite; current evidence capability STOP.**
[D's accepted retained-log receipt](package-d-result.md#current-m--retained-mknod-attachment-evidence-prerequisite)
finds the destroyed container log has zero bytes. The monitor records RUNNING
before execution and exit0/STOPPED after prefix cleanup begins, with no
recorded pre-failure exit/restart. This is not continuous target liveness.
Wrapper3394, the idmapped-mount user-namespace path for3455 and host QEMU688526
are not established container-init/attach-target identities.

The initial local-source gap was resolved by root's subsequent bounded raw
acquisition grant. Recipe `os/packages/lxc/default.nix:25–34` selects6.0.6,
**vpsfreecz/lxc@267e7844c122b9be56ca8a1ccc3d2f4d8986c326**, source hash
`sha256-vBj6P6301thjQVkjSnDQ6SPiFnl+4Uxrc3DQeBQkGwA=`. Root corrected its
initial `lxc/lxc` wording after this recipe check; no request went to that
repository. One raw request per following named path succeeded, without
redirect, retry, clone, checkout or input change. Local bytes are retained
under `package-d-mknod-retained-evidence/lxc-267e7844-*`.

| Exact source URI (commit fixed in every URL) | HTTP / bytes | Raw-file SHA256 |
| --- | --- | --- |
| [src/lxc/attach.c](https://raw.githubusercontent.com/vpsfreecz/lxc/267e7844c122b9be56ca8a1ccc3d2f4d8986c326/src/lxc/attach.c) | 200 / 54237 | `7b228f2a26f204e894f13ceb75579b201aa4eba48e75349c3d3f7d6fce58c0d9` |
| [src/lxc/commands.c](https://raw.githubusercontent.com/vpsfreecz/lxc/267e7844c122b9be56ca8a1ccc3d2f4d8986c326/src/lxc/commands.c) | 200 / 60038 | `b45478ab739b211a7b50bc8f994d330ce85bae0c47fc67861993011128e87eed` |
| [src/lxc/syscall_wrappers.h](https://raw.githubusercontent.com/vpsfreecz/lxc/267e7844c122b9be56ca8a1ccc3d2f4d8986c326/src/lxc/syscall_wrappers.h) | 200 / 5347 | `7d0b06791691950bb35ce2a7ba751463161fa290e7350f1bae509bf8a161187b` |

The latter two are direct dependencies for the monitor-fd acquisition and
setns wrapper. These digests identify the retrieved canonical exact-commit
files; they do **not** verify the full source NAR hash, realized package or
guest library bytes. No other source was acquired.

The pinned implementation now establishes the precise userspace boundary:

- `attach.c:440–475` obtains `ctx->init_pidfd` through the monitor's
  `LXC_CMD_GET_INIT_PIDFD`. `commands.c:643–681` returns its received fd;
  the callback sends `handler->pidfd`, not a fresh pidfd opened from an
  independently observed `osctl` PID. `attach.c:118–155` decodes `Pid:` from
  that received fd's `/proc/self/fdinfo`, opens `/proc/PID`, and checks the
  pidfd using signal0. Reaching the reported failure means those earlier
  steps did not stop this call; it does not establish liveness at the later
  namespace switch or recover a numeric PID from the logs.
- The preliminary time-namespace support probe (`attach.c:378–420`) accepts
  success, or EPERM/EUSERS with the required user-namespace flag. Its actual
  result is unrecorded. The reported ESRCH is **not** that probe's result.
- `attach.c:702–711` calls
  `setns(ctx->init_pidfd, options->namespaces | ctx->ns_inherited)` and logs
  the failure immediately. The conditional libc fallback in
  `syscall_wrappers.h:85–91` invokes `__NR_setns` directly. The failure is
  before the pidfd close at714, not a close error or a `mknod` errno.
- This executes in the transient fork child after the cgroup handshake and
  security barrier. `attach.c:1693–1698` logs `Failed to enter namespaces`
  and exits. The attached payload child is created only at1714, so this
  failing path never reaches payload creation/execution. No namespace-mask
  value, individual failing namespace or kernel-internal ESRCH branch is
  established by the text of that combined `setns` failure.

**Existing logging is insufficient.** The local
`ContainerControl::Runner#lxc_attach_command` supplies fixed container/path,
environment and cgroup options, forwards stdout/stderr and propagates status;
its current method/Exec options expose no per-call diagnostic log-level/output
parameter. More importantly, the retrieved call sites lack the required
fields even if TRACE output were enabled:418/475 give support/earlier-liveness
messages,777–784 describe named namespace choices, and1765/1797 describe the
transient worker. They do not log the received pidfd number and its decoded
target PID at709. The optional target-PID message1273 is in `do_attach`,
after the failing switch and payload clone, and is conditional on core
scheduling. `options->log_fd` at1599 is terminal logging, not a target-fd
receipt. Changing verbosity or log destination cannot supply absent fields.

Therefore the former separate-init snapshot proposal is **held as
insufficient**, not an observation implementation brief. Public state/PID,
stat and namespace snapshots may describe a container at their observation
times; they cannot bind the actual monitor-delivered fd or its target at
the failed `setns`. The minimal missing evidence is one directly associated
call record: container/name/path, attaching transient identity, actual pidfd
and decoded target identity, requested namespace mask, saved syscall result/
errno, and target/lifetime facts bracketing that same invocation. Current
supported test/logging output does not provide it. A different attach-local
evidence mechanism needs a separate explicit scope decision; none is designed
or released here. Do not launch a wrapper run that cannot answer this gap,
force legacy namespace-fd fallback, retry attachment, or infer target death,
PID reuse, a kernel bug or a scheduler cause. No production correction is
justified by this finite source result. N's separate test package is unaffected.

**NFS boundary, implemented by reviewed N below.** The failed host command enters init106849's network
namespace, creates a private mount namespace, mounts sysfs, then writes1 to
`/sys/fs/nfs/net/nfs_client/shutdown_tree`. The race deliberately blocks an
NFS mount using the two port2049 DROP rules. In the packaged production
patch, `nfs_netns_shutdown_store_common` rejects an inactive cancellation
facility with EBUSY; otherwise it validates host authority/value and calls
`nfs_shutdown_userns`. That calls `rpc_cancel_userns`, whose
`down_write_trylock(&pernet_ops_rwsem)` failure returns EBUSY **before**
publishing the admission barrier. Its comment explicitly requires a retryable
result when namespace initialization holds the lock. Source anchors are
`os/livepatches/bp-6.12.95-production.patch:3481`, `:2453`, `:14078`.
The actual incident does not identify which EBUSY path or any lock holder.

`osctld/lib/osctld/container/nfs_cancellation.rb:326` already retries only
`Errno::EBUSY`, sleeping at most50ms within the existing30s worker deadline;
its existing spec covers transient and permanent busy controls. The race at
`tests/suite/osctl/nfs-cancellation-common.nix:790` instead requires one echo
to succeed. This is a concrete caller-protocol mismatch independent of the
unproved incident branch. Retrying this specific rejected operation within
the existing protocol is not accepting EBUSY as terminal success or rerunning
a failed test until green.

The accepted implementation changes **only that shared race's positive host write** in
`nfs-cancellation-common.nix`. N/H used an explicit
`${pkgs.ruby_vpsadminos}/bin/ruby` provider. H disproved the earlier assumption
that osctld's separate OS package scope makes that attribute available to
this test function; the [current correction](#current-h-prebuild-failure-and-provider-correction)
supersedes that provider choice, not the writer protocol below.
Pass the snippet through ordinary Nix/Ruby shell escaping; no ambient Ruby,
new package, fetched dependency, file-transfer mechanism or framework.
Enter the namespace and mount sysfs once. Retry only open/write EBUSY on
that same control, at most50ms between attempts and within30s of the first
attempt; use an unbuffered `File#syswrite` of `1\n`, require its full two-byte
success, then close and require immediate barrier readback1 without retrying
readback/close errors as another write.
Other errno, malformed/false readback and exhaustion fail. Record busy count,
elapsed time and final outcome. The retry deadline cannot preempt a blocked
syscall: retain the existing outer machine-command timeout unchanged, with
no new unbounded wait. All remaining assertions retain their existing limits:
mount termination60s, reachable-network future-mount rejection15s, stopped
state, neighboring-client integrity, restart/remount and ordinary cleanup.
Negative permission/value tests and unpatched-baseline expectations stay exact.

The inspected test, exec/LXC recipe, NFS daemon, production patch and kernel
selection files have **no delta in d2fe..F**. Thus these contracts predate the
three shipping purposes. This does not prove the failures are unrelated to
all feature/environment interactions, nor equal guest/package closures.
[B's Intel default65/65](package-b-result.md#final-f-main-semantic-pair-audit)
and the two native11065/65 occurrences are comparison evidence only. Later
NFS examples63–65 do not complete failed example62. Both failed VMs exited0
without a kill signal; successful teardown does not repair either body.

The [implementation/check brief](implementation-plan.md#current-final-f-native-blocker-packages)
separates the independent test files, required observations, checks and stop
conditions. Root owns allocation and any later execution release. No
production/kernel/provider change is proposed; such a change would require
a concrete causal proposal and separate user product-scope decision beyond
current-module testing and the already approved shutdown coordination.
No API/schema/state migration, fleet update or deployment ordering is introduced
by these proposed test-only changes. Restore test source to roll them back;
guest cleanup/recovery remains the original contract. Both native blockers,
all semantic/health/recovery gates and conditional staging integration remain
unwaived; there is no universal historical-root-cause gate or new collector work.

### Current H prebuild failure and provider correction

**Assessment and minimal correction brief COMPLETE; HOLD execution.** Session,
environment and live roster were reverified: architect0 retains
Astra/xhigh/workspace_write. Only these two owned design documents and compact
selected evidence were written. A's source remains frozen; root chooses the
next preparation package. No source/check/evaluation/build/runtime action is
authorized by this assessment.

**Actual failure.** H `c916a804f4f107682a439febcfe7356b7b91f180`, parent F,
is the reviewed temporary sibling of marker-free N74297e, with identical tree
`c2899100faba19cdd022229b60693f4cc88391ce` and lock67487674.
[A's publication receipt](package-a-result.md#current-h-publication-and-affected-nfs-run-binding)
and [H review](nfs-focused-review.md) retain that history. Saved canonical
metadata binds workflow162100852, workflow_dispatch/run42176307860/attempt1,
created06:44:01Z: build127755464724 succeeded06:44:04–06:56:44Z; native127759679141
failed06:56:46–06:59:06Z. Capture was skipped. Actual jobs contain **one
unexpanded skipped lifecycle placeholder127759681135**, not nine individually
materialized skipped jobs. All observation/collection clients are terminal.

The native artifact13483926739 was independently bound:1676B, SHA256
`23dbcd55a9862a3992dcb65e4dd2e947996c359a88118420452a9478707ed731`, exactly
two safe unique regular members. The [101B test log](ci-nfs-focused-H-42176307860/architect-test-selected.txt)
and [2446B prebuild log](ci-nfs-focused-H-42176307860/architect-prebuild-selected.txt)
establish selected groups `osctl/nfs-cancellation` and
`osctl/nfs-cancellation-native110`, each with empty test/template arguments.
The [native command/error excerpt](ci-nfs-focused-H-42176307860/architect-native-job-log-selected.txt)
binds actual source H/tree, suite/tag `ci`, pattern `osctl/nfs-cancellation*`,
empty configuration and the failed `nix-build .../nix/evaluate-tests.nix`
invocation with `mode=testBatch`, `system=x86_64-linux`, `tests/test-configs/ci.nix`,
those exact two descriptors and `--max-jobs 11`. It exits1 with
**`attribute 'ruby_vpsadminos' missing`**, at tested source
`/nix/store/mp4zdk290fr4y3n459f1325pifjgffpc-source/tests/suite/osctl/nfs-cancellation-common.nix:853:35`.
The preparation-capacity line is not the failure cause.

This is an **N-introduced evaluation defect**. The host packaged test runner
was built/executed and selected both groups; prebuild then failed while
forcing their configuration text. No selected test VM, guest Ruby writer or
NFS assertion ran. The artifact has no per-case VM logs. The source-declared
two65-example scripts are not130 executed examples or a recurrence of F's
EBUSY. Actual guest launch/kernel/provider/module/site and cleanup outcomes
are unavailable, rather than failed guest observations. The separate normal
build logs system `g0vndsxl9rrw5k5p5g4bs38mjmn9gdz6` and production output
`qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95`; artifact13483986254
has only retained metadata here, not downloaded-byte or loaded-guest proof.
Raw native/build logs retain their verified SHA256
`6fa340c5dc0d1ff548ccb215ddc53d87221e15ed959d493f7303961435d6766f` /
`f9577a1ed45c7541762f7e9d928ed49a915bee2b7742a969e8b6ba2afc5a9924`;
escape stripping applies only to the numbered selected excerpts.

**Source contract and correction.** Exact H `tests/make-test.nix:39–49,80`
imports the test-function `pkgs` with the packages overlay and framework-input
attribute only. `os/overlays/packages.nix` does not define ruby_vpsadminos;
`os/overlays/ruby.nix` defines it in the separate OS overlay set. Thus the
earlier design/review provider-availability statement was incorrect. The
saved20 controls substituted a cached Ruby executable, and Nix syntax parsing
did not force this interpolation. Keep those records with their true scope;
they did not prove this package attribute available.

Recommend exactly **`${pkgs.ruby}/bin/ruby` at the same call site**, in the
same sole application file `tests/suite/osctl/nfs-cancellation-common.nix`.
Ordinary Ruby is an existing outer-test convention
(`tests/suite/osctl/image-repository-build-service.nix:22,33`) and an explicit
guest default package (`os/modules/config/defaults.nix:81–105`). The writer
uses standard File/Errno/monotonic facilities, not the osctld Ruby timer patch
or bundled gems. Verify the evaluated package binding as specified below;
the two package scopes are not assumed to have equal closures. Do not add
the OS overlay globally, install a provider, use ambient Ruby, or change
make-test/runner/workflow/input/kernel/daemon behavior.

Keep the exact38-line writer, namespace/authority,30s/50ms policy, full write,
close/readback, error/cancellation and all subsequent assertions unchanged.
The [implementation brief](implementation-plan.md#current-h-provider-correction-package)
requires evaluation of the **actual rendered script strings**, then checks
with the evaluated declared provider. Metadata-only discovery and a replaced
interpreter token are insufficient. No API/state/schema/migration or deployment
ordering changes; rollback is the owning test change, not a guest operation.

This caused fix folds into N's **fourth shipping purpose**, retaining old
N74297e, failed Hc916a804, F and every provenance ref/receipt. Root may later
allocate A's normal checked amendment and source-identical skip sibling;
neither is a fifth fixup commit, a merge/revert of H, or a runtime release.
Affected committed review must explicitly resolve the provider/check gap
before any guarded publication and one separately released focused attempt.
Both F native failures remain unwaived; pending LXC scope governs only extra
LXC work. No blind repeat, larger budget or automatic14400 escalation. Final
then-current-target, exact FINAL native+ALL9/original14400 and conditional
integration requirements remain unchanged.

### Reviewed N affected-runtime and delivery route

**Retained accepted preparation/history contract.** This route produced H;
its terminal prebuild failure and required correction are recorded above.
It does not release repeating H or publishing a successor.
[A's N packet](package-a-result.md#n-test-only-protocol-candidate-committed-for-affected-review)
and [accepted ALL4/HIGH review](native-nfs-protocol-review.md) bind marker-free
N `74297e22953f5f3186d7fcdcfe304eba10fb84f7`, parent
F `56b9363db1f1039e5d684dadc260cdffe7497e08`, tree
`c2899100faba19cdd022229b60693f4cc88391ce`. F..N is solely
`tests/suite/osctl/nfs-cancellation-common.nix`, +42/-2; its source SHA256 is
`2beb7a7299de0f744edb4ec84e79648795be98aa39c48736192990a3b54ce103`.
The lock remains67487674; 20 actual-writer controls, parsing/lint/escaping and
normal hooks passed. Review84ca8bb8 has no findings. These are preparation
facts, not packaged-provider or N runtime proof.

The original route was prepared while F/run42079730277 was active.
F is now terminal and root accepts all nine lifecycle audits, including
[C's aged-v5 audit](package-c-scheduler-hotplug-preparation.md#final-f-scale-aged-v5-original-four-hour-envelope)
with actual14400.598736s age. This does not transfer those results to N/H or
their successor. F's two native failures remain unwaived. The pending user question
concerns additional LXC diagnostics only. It does not block this N-specific
plan or impose a historical-cause gate on every later action.

**Recommendation: one source-identical message sibling for one existing
focused native dispatch, after F is terminal.** Publishing ordinary N now
would match the workflow's `tests/**` push filter and permit full native+9,
including another original14400 run. Instead A may, only after allocation,
preserve the exact marker-free N ref and prepare a new temporary sibling H
with parent F, identical tree and one-file patch, and only an appended
isolated `[skip ci]` message paragraph. Preserve N's author, subject and
other message bytes; H's committer/object/source-provider revision differs.
Use normal PRIMARY-bound Bundler/hooks and a message file. This is a
temporary publication control, not a new source or workflow selector. Keep
H outside final delivery ancestry; no diagnostic merge/revert, new delivery
registration or cleanup is needed. The existing N checkout may be reused
by sole A while N's existing branch remains pinned exactly.

The existing selector path is sufficient without application changes:

- `.github/workflows/ci.yml:333–336` appends one quoted `test_pattern` after
  `--`. `TestScriptList#matching` and `TestScript#path_matches?` use Ruby
  `File.fnmatch?` with `FNM_EXTGLOB`, then `Cli::TagFilters` requires `ci`.
  Singleton `default` scripts use the group path. Literal
  **`osctl/nfs-cancellation*`** therefore selects exactly the two current
  positive consumers below. The actual runtime inventory must confirm this;
  a future additional match is a selection change, not implicit permission.
- `tests/all-tests.nix:278–279` includes default/native110 in ordinary
  discovery. Baseline is in `livepatchTests`, requiring explicit livepatch
  discovery opt-in, and its only tag is `livepatch-amd`; the native workflow
  does not set that opt-in and requires `ci`. It is **not selected**, even
  though the textual glob would match its name if discovered. Do not add
  opt-in/tag/environment escape to include it. Its unchanged four-example
  branch does not execute N's writer and needs no extra focused run here.
- A nonempty pattern skips both build step153's current-module/sites capture
  and **all nine** lifecycle rows at396. The ordinary build job still builds
  the OS/production package, uploads that package and uses its existing cache
  path; focused native prebuild then builds the two selected test images.
  This is one existing workflow, with build plus native and skipped lifecycle
  jobs, not a promise of only one derivation/build operation.
- Keep `test_suite=ci`, `test_tag=ci`, `prebuild=true`,
  `stop_on_failure=false`, `proxy_lock_full_matrix=false`,
  `zfs_tags=functional`, empty `zfs_test_body`. No configuration override,
  script/example override or age change. Native retains `--jobs auto`,
  resolving to two selected groups, existing240-minute focused job/step and
  480-minute build bounds; no larger deadline. All logs upload for a nonempty
  pattern, with existing evaluation and upload-dependent cleanup semantics.

| Consumer | Selected scope and guest | Required outcome |
| --- | --- | --- |
| `osctl/nfs-cancellation#default` | One singleton script, 65 examples:16 for each NFS3/4.0/4.1/4.2 plus legacy-server case. Frozen6.12.95 boot, normal boot-enabled livepatch service, actual uname6.12.95.7. | All65 pass; all four race examples execute the new writer/provider, real full write/close/exact barrier1 and unchanged subsequent assertions. |
| `osctl/nfs-cancellation-native110#default` | Same65, native6.12.110 configuration, livepatch service disabled. | Same positive protocol and all65 assertions on its actual native input; no inherited default result. |
| `osctl/nfs-cancellation-baseline#default` | **Not selected here.** Unpatched frozen6.12.95, service forced off, four version-specific examples. | Final ordinary AMD coverage retains empty patch/unpatched guards, absent shutdown controls, forced-soft I/O error under reset within90s, surviving neighbor and recovered payload. Not65 examples or a positive writer case. |

Both selected machines retain default4vCPU/8192MiB and their10GiB tank disk,
original network/NFS options, script concurrency and all stress/permission/
state/data/isolation/restart/cleanup assertions. Read actual launch parameters
instead of inferring execution from this source declaration. There is no
300-second aging fixture in these NFS groups: the focused route satisfies the
shortened-diagnosis intent by excluding the aged matrix, without inventing a
new age/profile option or weakening NFS duration limits.

**Identity/completeness limits.** Bind one actual run/attempt/branch/H and
native source/tree log to H, unchanged lock, selected configuration and
reviewed N-equivalent test bytes. `test-runner.sh` captures HEAD, the repository
source snapshot carries revision/dirty state, and `source-version.nix` applies
it only to the matching provider source. H can therefore change generated
system/runner paths and revision labels despite tree equality. Record actual
provider/source/system, kernel/initrd/squashfs/QEMU paths, launch envelopes and
the concrete Ruby executable shown in each new writer command; require
provider execution and all four success outcomes per positive consumer.
Do not transfer N/F closures, old paths, elapsed outcomes or module identity.

The focused workflow deliberately supplies **no once-captured livepatch/sites
tuple or row livepatch-identity artifact**. Use the normal build's production
package artifact and logged output for their actual package scope; any digest
obtained from those bytes is an artifact digest, not a guest measurement.
The shared default NFS case verifies service-selected `.95.7` and source-bound
launch identity, not per-case module/site SHA. Preserve that accepted limit;
do not add a new assertion/source edit or silently fill absent site/capture
fields with F's qi47/7c4d/aiq values. Native110 and baseline have their own
declared identities. Full final qualification still requires the ordinary
once-captured module/site/source/lock flow and dependent-row checks.

Root separately sequences guarded publication and one workflow162100852
dispatch only after original F is terminal and all command owners release.
Check the temporary remote ref absent or exactly H, primary still expected F,
N still exact and marker-free, and no existing eligible H run. The push's
skip paragraph suppresses automatic push CI; it does not suppress explicit
workflow dispatch. Reconcile actual event/head/inputs before dispatch so an
unexpected push run, uncertain request or duplicate cannot start alongside it.
Do not publish N, push primary or mutate the workflow as a trigger workaround.

Focused acceptance needs both complete65-example outcomes, real provider/
protocol completion, all payload/integrity/state/health/recovery and graceful
VM teardown, with no unexpected skipped/retried example. Preserve diagnostics
and original errors on any failure. A timeout, permanent busy, other errno,
bad readback, source/selection mismatch or later assertion/teardown failure
returns to one named assessment; no automatic rerun, budget growth, kernel
proposal or `kernel/misc` retry to erase F. Baseline unavailability in this
focused selector is explicit and does not create a new interface project.

After accepted affected results, use the **retained marker-free N shipping
lineage**, or its properly reviewed then-current-target successor. Keep N
as an independent fourth purpose and first three purposes/messages intact
unless a truthful assessed refresh requires otherwise. Do not remove the
marker by amending H into delivery when N already exists. Root owns scope,
target/input assessment, appropriate history/affected committed review and
event reconciliation before **exact FINAL native+ALL9/original14400**.
Neither F's completed rows nor H's focused pass qualifies that successor or
retroactively passes either F failure. The LXC scope question is not a
universal gate; its functional failure still receives no waiver. Integration
remains under the user's unsatisfied conditional staging gates, with no
production/node/provider/deployment or lifecycle authority added.

The [complete A preparation and execution-boundary brief](implementation-plan.md#reviewed-n-focused-preparation-package)
defines exact guards, review reuse and stops. This design edits no source,
ref, manifest, runtime or environment and launches no checks.

### Accepted final preparation and ordinary prerequisite

**Retained preparation brief, now executed through reviewed F.** Root accepted
[C's complete ordinary-case audit](package-c-scheduler-hotplug-preparation.md#current-ordinary300-runtime-acceptance-audit)
and [ALL4/HIGH ordinary review](ordinary-300s-review.md) for exact
`802898590a035a845981959df7dd0ba4b9103f95` / run42057169147. The case
proves current captured module/site identity, 100000 tasks aged393.406s,
CPU127 pre- and post-transition cumulative health, all21 callback counts
after both phases, activation836.777s/disable1178.274s below1800, both full
migrations, all three exits0/stopped/tasks1/stress/resource cleanup, final
health/completion and graceful QEMU0. Native was skipped; other rows,
separate main semantic cases, original14400 and latest-target inputs remain
unqualified. No additional shortened matrix or historical-cause explanation
is required before preparing that final qualification. Temporary collectors
remain stopped; their failed outcomes are preserved, not waived.

[A's final-target preflight](package-a-final-target-preflight.json) finished
with Git released2026-11-05T17:10:30.910007Z. Actual staging is
`d2fe1489f0b0b213fb247aeee6e081d349adaf42`, parent
`2951a632c4254a44747a8da326e3dde897eaa0e2`. Primary645927,
ordinary802898 and instrumented08e remote refs match; all remain clean and
retained. The complete incoming range2951..d2fe is one commit, only
`flake.lock`, +3/-3; prior d2fe..actual is empty. Read-only inspection confirms
only nixpkgsUnstable revision/NAR hash/time changed: `0bb2eedc20e4739f29e8045034f2828ad7054f8f`
to `1d060086d60cb76a40cf37109f979d88a5bd6396`. No new pin is proposed.

This input is consumed by unstable NixOS templates (`flake.nix:365–435`)
and embedded into generated stable and unstable guest locks
(`os/lib/nixos-container/template-flake-lock.nix:55–57,73–78`). It can change
those guests/packages and their native compatibility checks. The framework,
normal .95 producer, packaged runner and OS defaults select stable nixpkgs
(`flake.nix:88–115,173–190,255–342`), whose lock node is unchanged. Linux,
boot/archive/SDK, patches/kpatch, overlays, module/fixture/resolver, runner,
workflow and gem source bytes receive no incoming edit. This does not prove
derivation/closure equality: changed self paths, lock and source-version
metadata are inputs too. The new nixpkgs package tree has not been audited
and no old module/guest/runtime identity is transferred to the final head.

Recommend a patch-equivalent refresh of only the three shipping purposes
from2951..645927 onto exactd2fe, retaining tested645927 and all temporary
refs outside final ancestry. Remove only the isolated skip-CI paragraph
through normal PRIMARY Bundler/hooks; preserve other truthful messages and
ownership. Primary already has original14400/full workflow. Never merge or
revert diagnostics into delivery. The [complete A preparation packet](implementation-plan.md#conditional-diagnostic-head-and-final-verification-package)
requires exact old/new ranges, patch/message/source comparisons, bounded
changed-input checks, fresh finite identity receipts and affected committed
ALL4/HIGH review before publication. No final SHA is guessed; a substantive
conflict or changed contract returns to root.

After review/root release, bind one actual exact-final-head full run or one
existing unfiltered dispatch after no-duplicate reconciliation. Require full
native plus all9 rows, original14400, actual FUSE/TCP/fragment and other
semantic witnesses, shared captured identity, health and recovery. The
existing six explicit Leap16.1 missing-image exceptions remain only that
symptom/scope; latest device-unit or any other functional failure is not
waived. Full success under that existing scope, fresh target/history/hooks
and ordinary integration checks precede the user's conditional vpsadminos→
staging merge. This brief authorizes no merge, deployment, node change or
lifecycle action. Failed checks/review/runtime require a named assessment,
not a blind repeat, more collector work or larger budgets.

### Historical intermediate diagnostic sequence

The following earlier sequence is retained as history. Its shortened-cycle
dependency has been satisfied by the accepted ordinary case above; it does
not require another diagnostic matrix before final preparation.

This accepted sequence has advanced to the separate bda1 diagnostic head and
run `41921632759`; the primary feature stays frozen at reviewed 645927.
The original dependency was root acceptance of focused `41913307185` body
and graceful shutdown evidence. The remaining final-qualification steps below
are conditional on root's acceptance of diagnostic outcomes; this record
does not release another run. Failure returns to bounded diagnosis, not an
automatic retry.

After accepted focused success, the next diagnostic cycle uses the existing
normal native plus nine lifecycle jobs with C's saved 300-second `scale-aged`
profile. This follows the user's explicit reduction direction while diagnosis
is unresolved; it does not jump directly from focused success to four-hour
aging. The patch changes only `shapes.scale-aged.ageSeconds` from 14400 to
300 plus its comment. Keep 128 vCPUs, 16384 MiB, 100000 tasks, other profiles, health,
identity, predecessor, witness and recovery checks unchanged. A five-minute
green is diagnostic evidence only. Neither changed metadata nor a passing
different run proves a historical fault fixed, and no blanket historical
root-cause gate is added. The distinct `representative` profile remains at
8 vCPUs, 8192 MiB, 16384 tasks and age 0; other zero-age profiles and fresh
retention settings remain unchanged.

A prepares an ordinary same-session **diagnostic evidence ref/checkout** from
the exact accepted production head, for example
`2026-11-03-livepatch-fixture-failures-diagnostic-300s`. It is not an additional
registered delivery feature whose 300-second head must merge. Preserve the
primary feature ref/worktree, all existing delivery registrations and their
completion obligations. Apply only saved patch `c46380…54dde`, commit the
temporary diagnostic delta with normal hooks, perform its quick checks and
committed affected review, then obtain root acceptance for one publication/run.
Keep original production base/head and diagnostic base/head, patch, review,
test identity and results separate in the existing receipts. Retain the
diagnostic ref/checkout/evidence; no lifecycle, unregister, deletion or cleanup
workaround is included.

The existing workflow is sufficient: no workflow, campaign mechanism, profile
option or trigger-only source edit is added. A qualifying ordinary push run
may supply the diagnostic matrix; otherwise root can release one existing
unfiltered dispatch after exact-head and no-duplicate reconciliation. A and
C provide routine history/patch clarification only until the package is
assigned. The minimal complete next package and exact acceptance sequence are
in [implementation-plan.md](implementation-plan.md#conditional-diagnostic-head-and-final-verification-package).

Only after root accepts the diagnostic outcomes and current problems are
settled does A return to the reviewed production lineage at original 14400,
excluding the diagnostic commit rather than reverting it into delivery
history. Remove the isolated temporary `[skip ci]` paragraph from the
production commit, preserve its tree/patch and other message content, commit
and reconcile affected review/history before publication. The final series
must contain no obsolete diagnostic/revert/WIP commit or skip marker. Retain
the tested old head and diagnostic evidence separately.

The earlier launch assumption that skip-marker removal leads immediately to
final four-hour CI is superseded by this intermediate diagnostic cycle.
Also, a message-only final amend preserves the tree: path-filtered push CI
must **not** be assumed to start. Bind an actual qualifying exact-final-head
full run, or release exactly one existing unfiltered dispatch after the
bounded no-duplicate check. Only complete final native plus all nine lifecycle
rows, including restored four-hour aging, can satisfy final acceptance and
the existing conditional merge gates. Final source identity/guest inputs are
new verification inputs even when reviewed production bytes are unchanged.

Rollback from this diagnostic phase means returning to the retained reviewed
production ref/profile; no guest deployment or persistent-state conversion
occurs. If diagnostics require another substantive fix or the target baseline
changes, root assigns the named affected package/review before another run.
There is no automatic retry or open-ended campaign, and runner updates remain
operator-owned.

## Diagnostic scale-aged-v5 CPU-offline warning

**Historical bda1 disposition: continue its already-running diagnostic rows;
retain this row as failed. Hold a repeat or progression to final 14400-second
qualification pending root's disposition.** The later 13b setup failure and
current hold are recorded below. This adds no
requirement to explain every historical failure. The low-memory-v5 success
reported by root at 22:48:20Z is distinct evidence; it does not waive the aged
row. C completed the observation implementation used by 13b; the lifetime
remedy below awaits root allocation. No new run or production correction is released.
Production 645927 stays frozen.

[C's complete classification](package-c-diagnostic-300s-aged-v5-triage.md)
binds job `126907163490`, diagnostic bda1, frozen boot `050sh2…`, exact
released v5 `b31f6440…7984`, and the supplied ZIP/hash. The selected
[console](package-c-diagnostic-300s-aged-v5-evidence/machine-console.log),
lines 140–182, contains the affinity fallback, warning and complete task dump.
At guest 697.996324 the CPU127 stopper reports `sched_cpu_dying.cold`,
`Dying CPU not properly vacated!`, and uname `6.12.95.5`. The dump says two
enqueued entities but prints only PID789 `migration/127`. PID31532 from the
earlier affinity message is **not identified as a second queued task**.
Offline/online writes, 128-online assertion and population progress all
completed before the cumulative health failure at 22:41:07Z. Age reached
390.501 seconds. Normal v7 bytes/sites were checked but activation was not
reached. The old loader/CSD follow-up does not apply to this initiating trace.

The owning source is canonical Linux
`a2384967b90f24d2470c9eb15f0e66d938df7e08`, selected by
`os/packages/linux/boot-6.12.95.nix`. Read-only local object inspection establishes:

- `kernel/sched/core.c`, `balance_hotplug_wait` and
  `sched_cpu_wait_empty` (around lines 8004 and 8270), require one runnable
  entity and no migration-disabled tasks before the stopper phase. The comment
  explicitly treats a later bound-task wakeup as failed hotplug evacuation.
- `sched_cpu_dying` (8322–8340) takes the runqueue lock and warns for
  `rq->nr_running != 1 || rq_has_pinned_tasks(rq)`. `rq_has_pinned_tasks`
  reads `nr_pinned`; this is kernel migration-disable accounting, not the
  userspace affinity mask. The observed count of two proves the first arm
  is met. The evidence does not establish whether the pinned arm also holds.
- `dump_rq_tasks` (8303–8319) prints `nr_running` but enumerates queued
  `task_struct`s, not all scheduling entities. `deadline.c`
  `__enqueue_dl_entity` → `inc_dl_tasks` increments both `dl_nr_running`
  and the runqueue's `nr_running`, including a deadline server. The fair
  server is stopped by `dl_server_stop` **after** the warning/task dump,
  still under the runqueue lock. An enqueued fair server is therefore a
  source-backed explanation for an extra counted entity absent from that
  task enumeration, but its actual presence in this incident is unmeasured.
- `select_fallback_rq` (3463–3533) emits “no longer affine” when it must
  broaden the permitted CPUs for evacuation. The qualification helper uses
  ordinary `pthread_setaffinity_np`; `task_population.c:90–155` treats
  `EINVAL` during CPU offline as expected and retries as the CPU returns.
  It does not invoke kernel `migrate_disable`. Source and logs establish
  no unsupported helper operation or justification to suspend its workload.

The predecessor contract is the exact archived v5, not a rebuilt module:
`tests/fixtures/livepatch/default.nix` checks its fixed digest, and C observes
that digest and completed v5 activation. The documented v1–v5 payload in
`docs/os/livepatches/6.12.95.md` does not list a scheduler/deadline change.
That manifest and the matching warning site support this source boundary;
they are not an independent audit of every predecessor replacement or proof
that no indirect predecessor interaction is possible.

**Unresolved:** actual `nr_pinned`, class/runqueue composition, fair-server
queue membership/flags and hotplug masks at the warning. A real task wakeup,
migration-disable state or other accounting fault has not been excluded.
There is no proof of a kernel bug, harmless warning, host starvation,
flakiness or current-feature causation. Subsequent successful CPU return does
not remove a recorded kernel-health failure.

The accepted capture point is the exact **pre-CALL instruction at
`sched_cpu_dying+0xc3`**, after the warning/task dump and before
`dl_server_stop` dequeues the server. The validated preceding LEA at `+0xbc`
sets RDI to the embedded entity (`rq+0x968`); RBX holds the runqueue. This
preserves the locked pre-dequeue contract while limiting probe handling to
this hotplug call path. Retain CPU127 and entity/runqueue relationship checks,
unique native NF3 symbol/base lookup, frozen notes/ELF identity, exact
instruction boundary/length/target and blacklist/excluded-range guards.
The earlier callee `dl_server_stop+5` point is superseded feasibility history.
Do not fetch/filter `$stack0` as a callee return-PC at the caller probe;
the exact validated call site supplies the caller identity. C records the
actual static proof; neither this acceptance nor that proof claims successful
runtime probe registration or incident causality. The
[execution brief](implementation-plan.md#bounded-scheduler-hotplug-evidence-package)
defines the one-owner scope and refusal conditions. A synthetic userspace
counter test would only restate this source and cannot reproduce kernel
hotplug ordering; it is not the next check.

Keep the 128-CPU/16-GiB/100000-task envelope, 300-second diagnostic age,
CPU127 offline/online/progress checks, cumulative health baseline, watchdog
capture and original recovery unchanged. Keep final 14400-second acceptance.
Do not move `dl_server_stop`, exempt this warning, alter affinity, or change
the boot/predecessor/kernel merely to obtain a pass. Any production scheduler
correction is a separate proposal requiring root/user scope decision beyond
the accepted shutdown fix. No persistent format, protocol, deployment or
fleet change follows from this diagnostic design.

## Proposed one-case scheduler diagnostic execution

**Root accepted this finite execution boundary, subsequently executed at
13b / 41938327930 with one build and one AMD case.** Its setup failure is
recorded below; no new run is released. For the original preparation,
C committed its one-file observation
at `f41262be6759876709c35677b847da1f6ba53eec`, parent bda1, with 17
controls and parse/lint checks reported; the later combined 13b review and
20 controls passed before execution. Bda1's aged-v5 failure remains failed.
Production 645927
and its 14400-second profile stay unchanged.

The existing `.github/workflows/ci.yml` has no supported input combination
that runs only this qualification case with the required identity contract:

- A nonempty `test_pattern` disables both the build's candidate/sites
  capture (line 153) and the complete lifecycle job (line 396). The native
  job does not export `VPSADMINOS_ENABLE_LIVEPATCH_TEST=1` and accepts only
  `ci`/`proxy-exec` tags. The qualification case carries neither tag.
- Empty `test_pattern` retains the correct build outputs and lifecycle
  opt-in, but schedules native and all nine lifecycle rows. `test_tag`
  controls native selection, not that lifecycle matrix.
- The exact discovered case is
  `kernel/livepatch-qualification@amd-scale-aged-v5` (`#default`), as shown
  by the original job log's `[1/1]` selection and `tests/all-tests.nix` plus
  the qualification template. `kernel/livepatch-qualification-aged-v5`
  is a descriptive shorthand, not the actual selector.

The accepted **temporary diagnostic-only `ci.yml` delta** skips the
native `test` job and retains only the existing `amd-scale-aged-v5` matrix
entry, unchanged, including `large: true`. Keep the entire build/capture/cache
path and lifecycle execution, artifact, result and cleanup steps. This uses
the existing AMD runner class, opt-in, tag and CPU-overcommit admission;
it introduces no dispatch option, profile, workflow or generic selector.
It runs one build job plus one AMD aged-v5 qualification job, with native
skipped, while retaining the build's existing checks,
not promising that the build is free or all outputs are already cached.

The [literal execution brief](implementation-plan.md#proposed-one-case-diagnostic-launch-route)
uses empty-pattern `ci` inputs and a fresh exact committed diagnostic head
containing C's observation plus the temporary execution delta. A/root own
its later preparation/publication/run binding after review and release.
All temporary age, observation and execution changes remain outside final
delivery ancestry; no workflow change ships. Existing local cache barriers
and retained ELF/SDK availability do not prove a warm full guest closure,
so a new local preflight/build/debug effort is not the shorter justified
route. No such local operation is proposed.

A complete capture may explain a **failed** qualification; it cannot turn
the warning into a pass. A passing case still needs original health,
identity, activation/recovery and graceful-teardown checks. Either outcome
is one diagnostic result, not full native-plus-nine or four-hour acceptance.
No production scheduler fix or warning exemption follows from route approval.

## Current capture-setup failure and lifetime remedy

**Historical result: 13b / `41938327930` failed diagnostic setup; original
hotplug/health was not reached.** Its lifetime remedy subsequently passed
early arming/capture/pre-hotplug health at b361; normal late observer release
remains untested, as recorded in the current loader section below.
[C's runtime audit](package-c-scheduler-capture-runtime-audit.md)
binds the exact source, artifact/hash and selected command/console evidence.
The aged workload reached 389.800 seconds at 128 CPUs/16 GiB/100000 tasks
under exact v5. Notes, native address, typed event definition and filter
writes succeeded. The event-enable command then timed out; disable and
global deletion also timed out. Private tracing-off and instance removal
succeeded. There is no arming acknowledgement, recording-on, hotplug-start,
runqueue/flags/profile record or current reproduction of the old warning.
Unavailable counters are not zero. Later QEMU exit 0 without a kill signal
proves failed-case VM teardown, not in-guest observer removal.

The selected replies end in each command's timeout-wrapper status 124,
with `replies_consumed`; no enable/disable command PID is tied to a wait
stack or later event readback. `osvm/lib/osvm/shell.rb:345–430` reserves
protocol and kill time within the supplied 10-second deadline, maps outer
124/137 to the logged -1/timeout and separately handles missing protocol
replies. Thus the 7.78-second enable interval is an operational command
timeout, not proof of deadlock, an unprobeable site, shell desynchronization
or an exact kernel wait duration. Ruby's unarmed flag does not establish
that a timed-out write had no kernel effect.

Pinned Linux `a2384967…` supports this narrow ordering hypothesis:

- `kernel/trace/trace_events.c:1564–1592` serializes `event_enable_write`
  on `event_mutex`, updates buffers and invokes event registration.
  `trace_kprobe.c:324–435,1773–1782` routes enable/disable to kprobes.
- `kernel/kprobes.c:1167–1191,2398–2452` uses kprobe/text mutexes and CPU
  hotplug read locking for the ordinary arm/disarm path. On x86,
  `arch/x86/kernel/kprobes/core.c:815–830` patches the breakpoint byte
  and calls `text_poke_sync`; `alternative.c:2311–2314` implements it
  with `on_each_cpu(..., wait=1)`. The optimizer also holds those locks
  while `synchronize_rcu_tasks()` runs (`kprobes.c:603–635`). Disable,
  unregister and deferred optimization can therefore involve patching,
  synchronization or lock waits. None is identified as the actual wait here.
- Private `tracing_on` uses `trace.c:9046–9078` (`rb_simple_write`) and
  `tracer_tracing_on/off`: for `current_tracer=nop`, there are no tracer
  start/stop callbacks (`trace_nop.c`). The buffer's on/off operations
  change atomic recording flags (`ring_buffer.c:4819–4852`); stopping
  wakes buffer waiters. This path does not enable/disarm the kprobe or
  perform its text-patch synchronization. It still takes a mutex and
  executes guest work: prompt completion under load is not yet proved.

**Recommend a one-file diagnostic lifetime correction, not a kernel fix:**
prepare and arm after exact predecessor activation/notes validation but
before `prepare_transition_state`, `start_stress` and population creation.
Keep the new private `nop` instance recording OFF throughout workload
creation and aging. At the existing pre-hotplug point, toggle only private
recording ON, run the unchanged hotplug/health body, then recording OFF and
collect the same bounded data. Keep the rare caller `+0xc3`, all fields,
identity guards, CPU127 filter and data acceptance unchanged. This moves
initial arming out of the stressed phase; asynchronous optimization means
it is not a guarantee that every later synchronization disappears.

The current observation ensure disables/deletes **before** the example's
after-hook requests population stop. Remove those destructive observer
operations from the hotplug window. On success, disarm/delete only after
the existing successful population exit/stopped/tasks=1 proof and
`stop_stress`, before final health/completion. On failure, preserve the
pre-cleanup snapshot and existing stop/release/recovery sequence. Only
attempt observer disarm/delete with positive workload-drained evidence;
otherwise keep private recording OFF, explicitly report incomplete in-guest
cleanup and let ordinary failed-VM teardown end the guest resource lifetime.
Do not stack patching retries behind an uncertain command, claim timed-out
effects absent, or add forced livepatch reversal.

[The bounded package](implementation-plan.md#capture-setup-order-remedy-package)
specifies partial setup, exception/cancellation, controls and later runtime
acceptance. Existing command budgets, 300-second envelope and all health,
watchdog/identity/recovery contracts remain; do not raise timeouts as the
remedy. The original fair-server hypothesis remains unresolved. No new
path/API, production source, boot/pin, persistent format, deployment or
fleet change is needed. All observational changes remain diagnostic-only;
final original-14400/native-plus-nine acceptance is unchanged.

## Incoming staging d2fe: temporary diagnostic disposition

**Recommend retaining exact reviewed diagnostic
`c08a59956c4a905e5a787046251234a615c7e807` on base
`2951a632c4254a44747a8da326e3dde897eaa0e2` for the next one-case experiment.**
Root owns acceptance and release; this assessment launches nothing. The
[publication guard receipt](package-a-raw-tick-publication.json) correctly
stopped before push when freshly fetched staging became
`d2fe1489f0b0b213fb247aeee6e081d349adaf42`. Primary remote645927 and
diagnostic remote23db still matched. All fetch effects were reconciled and
Git ownership released at10:45:44.403376Z.

Read-only canonical-object reconstruction gives one ordered incoming commit:

| Commit / direct parent | Purpose / complete changed-path inventory |
| --- | --- |
| `d2fe1489f0b0b213fb247aeee6e081d349adaf42` / `2951a632c4254a44747a8da326e3dde897eaa0e2` | `flake: nixpkgsUnstable 0bb2eedc2 -> 1d060086d`; only `flake.lock`, +3/-3 |

Only that node's `rev`, `narHash` and `lastModified` change. Revision moves
`0bb2eedc20e4739f29e8045034f2828ad7054f8f` →
`1d060086d60cb76a40cf37109f979d88a5bd6396`; NAR hash moves
`sha256-fiPJ88izTVucjeo2EQ3jk4aWmLg03I1D4vxnX2QjEgE=` →
`sha256-jQp1wKvbwWdLBASTXkSi/VYmDJ5AbBi1WvcMt9HWJC8=`.
The merge base of c08 and d2fe is exact2951. Base2951 and c08 share lock blob
`785582c0255f718d88b55498e60f16c3d1b3b303`; d2fe's lock blob is
`6b773b201e081358b9f48bf78378cb6301cceac0`. The incoming path has zero
overlap with the 27 paths in2951..c08.

This is a real input change for a future refresh. `flake.nix:365–435`
selects nixpkgsUnstable for unstable NixOS container templates, and
container persistence/release/evaluation tests consume it.
`os/lib/nixos-container/template-flake-lock.nix:55–57,73–78` also embeds
the unstable node in generated locks, including stable templates. No claim
is made about the uninspected new nixpkgs package tree or output equivalence.
By contrast, `flake.nix:88–115,173–190,255–342` selects stable `nixpkgs` for
the test framework, OS systems, normal `.95` livepatch producer and packaged
runner. The stable lock node and every non-lock source blob are unchanged:
Linux/boot archives/SDK recipes, payload/kpatch, overlays, fixtures/resolver,
QEMU/runner/workflow code, gem inputs and source-identity implementation.
This source inventory is not whole-derivation or guest-closure equality;
refreshing self/source paths and version metadata can change inputs too.

Advancing a remote default ref does not alter immutable c08 or its lock.
Its next job will still build/capture the **normal producer of c08**, then
verify that one producer/module/SHA/sites binding in the diagnostic row.
Keeping this temporary anchor isolates the host-frequency prerequisite
removal; it adds no production input freeze or historical digest allowlist.
There is no concrete changed contract requiring refresh before this bounded
experiment. A c08 result cannot qualify d2fe, establish the latest normal
module's identity, prove old causes, or satisfy final delivery gates.

The [execution disposition](implementation-plan.md#incoming-staging-d2fe-and-the-next-anchored-diagnostic)
keeps the reviewed source/history unchanged and records d2fe as the actual
target guard. Final delivery still needs the then-current target assessment,
appropriate refresh/equivalence and affected review, restored14400, and full
exact-final-head native plus nine lifecycle/semantic/recovery checks. No
merge, node change, new run or lifecycle action follows from this recommendation.

## Current loader/TLB fault and next evidence boundary

**08e disposition executed and accepted:** the ordinary300 sibling802898
passed its complete selected case. The current next preparation is
[final shipping qualification](#conditional-post-focused-diagnostics-and-final-qualification),
not another collector refinement or shortened run. The rationale and prior
limits below remain historical evidence; no original product health,
workload, semantic, deadline or recovery requirement was removed.

[C's complete 08e audit](package-c-scheduler-hotplug-preparation.md#current-08e-bounded-runtime-audit)
binds exact `08e3d0f910d5cc7140e2eb532497218f52e94a16` to terminal RED
run `42040026542`, with unchanged clean source. It establishes these limited
milestones:

- Strict fixed-map host sampling succeeded: 178 complete samples, 22784
  required-vCPU rows, stable 128-entry map and a final sample after the
  observation window. These are sequential sampled observations, not
  simultaneous snapshots, runnable-wait data or callback causation.
- Providers and the tiny public codec round trip passed. The full 100000-task,
  128-vCPU/16-GiB workload aged 337.867 seconds; pre-transition CPU127 hotplug
  and health passed, with the healthy bound record, 1 hit/0 misses/zero loss.
- Attempt 1, PID143049, returned 0 after 905.74 seconds; activation 906.502
  seconds was below 1800 and enabled=1/transition=0 passed. This is timely
  insertion, not post-transition health or full qualification.
- End-marker EBADF was followed by identity/callback/statistics/export
  failures. Only 55 CPU statistics blocks were complete, plus partial CPU55;
  24 complete blocks had actual dropped events. CPU0 had 1774 drops and
  69552 bytes. Size readback 67 differed from the expected 64. Native export
  yielded only its begin frame, no payload/footer or native.log. Missing
  population exit left drain unknown; guest resources remained until failed
  VM teardown, QEMU exit 0. Neither native completeness nor recovery is established.

The size predicate may be wrong, but its requested-versus-exposed semantics
are not needed to decide the next route: correcting it cannot recover the
already observed losses, complete the other 73 CPU blocks, or establish why
commands timed out. Reservation/transport causes and completion after timeout
remain unknown. No further pinned-source clarification or optimization is
needed for this disposition. A further capture refinement is not justified
as a prerequisite for the user's original module qualification. The seventh
owner has grown by 918 handwritten lines; successful readiness and sampling
are useful evidence, but the collector's loss-free export contract is an
internal diagnostic choice, not a product acceptance requirement.

**Smallest route:** prepare a separate session-owned diagnostic sibling from
reviewed production `645927e22809a29c67ffd59c072e553e05e2a72b`, changing
only `tests/suite/kernel/livepatch-qualification.nix` with the saved 300-second
patch and `.github/workflows/ci.yml` with the retained one-build/one-AMD-aged-v5,
native-skipped selection. Use the ordinary qualification body from primary
unchanged; the plan reuses exact bda1 for its already committed age-only delta.
Exclude both temporary observation purposes: dying-runqueue owner
`538706…` and loader owner `08e…`. Thus no new guest event, host sampler,
debug-thread launch option or capture/codec completion gate participates.
This removes diagnostic machinery, not the original CPU127 hotplug or
cumulative kernel-health assertions. It does not claim the machinery caused
any fault. Preserve all old refs, reviews and failed outcomes; do not rewrite
08e or turn its INCOMPLETE result into a pass.

The [execution brief](implementation-plan.md#accepted-loader-csd-and-owned-host-evidence-package)
defines source-equivalence checks and affected committed review before root
may release one run. A green must reach the ordinary post-transition health,
all existing callback/semantic checks, workload stop, recovery and graceful
teardown. Failure gets one named outcome assessment, not an automatic repeat
or a new collector. A clean run does not explain the old CPU127 or loader
faults. This recommendation needs root's scoped acceptance of retiring the
temporary observers; it needs no new product-health exception or node setting.
No unresolved product choice requires a user question. Primary 645927,
original 14400, latest-target assessment and final exact-head native+9 gates
are unchanged. No automatic move to those final runs follows a diagnostic pass.

### Retained loader-capture design through 08e (superseded as the next package)

The following records the earlier design and its evidence. Its future-tense
implementation/run instructions are historical; the disposition above now
governs the next proposed package. Both c08 and 08e were implemented, reviewed
and tested; neither achieved complete native capture or full qualification.

[C's complete c08 audit](package-c-scheduler-hotplug-preparation.md#current-c08-raw-tick-runtime-audit)
proves the first host snapshot/128-row APIC map, then an incomplete second
snapshot when previously incidental TID 1256854 could not be opened. The
cause of that disappearance is unknown. Later population/300s/pre-transition
health passed and PID 142464's insertion returned 0 after 819.6s; post-transition
health/full qualification did not pass. End-marker EBADF and a 10.01s trace
read timeout left only a fragment, with loss statistics/PID crosscheck
unreached. Missing drain exit left subsequent drain conditions unobserved;
observers remained until failed-VM teardown. These are distinct failures,
not evidence of a kernel defect, permanent deadlock or buffer saturation.

**Smallest next boundary: helper plus qualification.rb only.** Establish the
initial 128 vCPU map with the existing strict discovery. Thereafter sample
only those fixed TID/start/label identities. Incidental thread lifetimes and
counters are outside that stated scope; do not open them or claim complete
process-thread coverage. Keep owned QEMU/executable/ancestry revalidation,
all 128 identities, caps and clock guards. A missing/reused/renamed required
thread still fails immediately; never rediscover a replacement. Total QEMU
thread counts remain bounded by 256, but need not remain numerically identical
between samples. This defines legitimate scope without explaining the old
ENOENT or retroactively accepting its incomplete snapshot.

Pinned a238 source supplies the trace boundary: `kernel/trace/trace.c:6899–6956`
returns EBADF when marker event reservation fails.
`kernel/trace/ring_buffer.c:4550–4584` has several reservation-refusal
conditions; its no-overwrite full path increments
dropped events at 3475–3482. Actual refusal cause remains unproved.
`trace.c:8354–8415` exposes entries/loss/bytes counters independently of the
large payload. The ordinary `trace` file uses seq-file iterators
(`:4590–4675,4773–4808,5000–5007`), while changing trace clock resets buffers
(`:7061–7090`). Retain early filter/clock setup and OFF acknowledgement;
do not reset, refilter, consume trace_pipe or enlarge buffers to recover data.

After the existing end-marker attempt and one OFF/readback, save bounded
attempt/PID, instance/filter/clock/source and all 128 per-CPU loss/full metadata
**before** payload. Preserve failures and metadata even if later collection
fails. Export the frozen native text in one guest gzip/base64 pipeline through
public `machine.succeeds(..., timeout: 10, shell: :diagnostics)`, with 2 MiB
compressed and 64 MiB decoded caps and strict complete-stream checks. These are
export limits, not changes to 64 KiB-per-CPU trace buffers. Store bounded native
text/metadata as ordinary .log/.txt artifacts; print only summaries in the
runner log. A failed marker, nonzero loss/full buffer, timeout, cap hit,
partial/corrupt stream or missing identity relation stays INCOMPLETE.

Existing guest core packages provide Bash/coreutils/gzip; the declared runner
provides Base64 and Ruby's Zlib/StringIO facilities. This is source/package
feasibility, not proof the transfer fits 10s under load. Public pull_file was
examined and rejected here because its unparameterized copy inherits 900s.
No private paths, API/provider change, chunk/retry framework, timeout or
buffer increase is needed for the selected compressed route. The precise
pipeline, consumer checks, tests and stop conditions are in the
[implementation brief](implementation-plan.md#accepted-loader-csd-and-owned-host-evidence-package).
C later owns the complete two-file packet; A folds it
into the seventh owner, retaining tested c08 and the six earlier owners.
Affected committed review precedes any separately released one-case run.
The user explains that runners are VPSs on vpsAdminOS nodes, so enabling
`sched_schedstats` would affect the shared node. Root's recommendation is
no node-wide change merely for this diagnostic; this is a scope decision,
not an invented user prohibition or authorization to change a setting.
No host/node mutation, implementation or new run is released by this brief.

Reviewed source `23db`, run42003244138, remains a real readiness failure:
`INCOMPLETE: CLK_TCK command failed status=127`, before the first baseline
header, snapshot, ready record or actual TID map. The missing/unexecutable
command/PATH/provider boundary is established, not its precise environment
cause; the later operator value 100 is not the job's value. Preserve
[C's 23db audit](package-c-scheduler-hotplug-preparation.md#current-23db-baseline-runtime-audit)
and the tested source. It does not establish a clock regression, kernel fault
or LC1 recurrence. The earlier four-file loader source `9805ea20…` and its
[41972655273 audit](package-c-loader-csd-runtime-audit.md) remains a real
early readiness failure, before population, aging, hotplug or activation.
The shared error covered both the stats read/value and CLK_TCK validation;
the original job recorded neither. The later operator preflight reported
readable stats=0 and CLK_TCK=100, not those original job values. Actual
QEMU/TID mapping and baseline samples were unproved in those attempts; c08
subsequently established initial readiness, but not activation-window coverage.
The earlier stats=1 and positive-CLK_TCK requirements are superseded; both
failed attempts are preserved. That earlier raw-tick amendment changed the
helper and qualification's evidence-summary wording and is complete in c08.
The current two-file correction above additionally changes capture/consumer
code. Workflow, same-view cap and common.nix's exact naming guard stay as
implemented. C owns the later complete implementation/check packet; A owns
its history refinement.
[C's complete b361 audit](package-c-scheduler-lifetime-runtime-audit.md)
supplies attempt, identity, capture and recovery evidence. This meets the
old loader follow-up trigger at subsystem-signature level, not at common
cause or whole-input equality. No run, production correction or universal
historical-root-cause gate follows.

The early observer now has actual acceptance: one loss-free CPU127 pre-CALL
record, `nr_running=1`, `nr_pinned=0`, all recorded CFS/RT/DL counts zero,
empty fair-server node and flags `0xf1`; hits/misses 1/0. Pre-transition
hotplug/health passes. This healthy instant neither explains nor waives
bda1's earlier warning. The later first kernel fault is guest 765.904211,
CPU114, `insmod:142433`, uname `.95.5`, in loader permission/TLB work.

The attempt distinction is essential. The callback trace after the **first
returned EBUSY**, 02:20:01–02:31:04Z, associates PID142433 with that attempt.
The second EBUSY, 02:31:14–02:34:05Z, associates PID147541. The third command,
02:34:13–02:49:56Z, times out with **PID unknown**. Do not assign the first
softlockup directly to the third timeout. Later kernel patching completion,
`.95.7`, enabled=1/transition=0 do not establish a timely syscall return.
Recovery requests returned 0; the drain check stopped at a missing population
exit marker. Later conjuncts were unobserved. Observer removal was correctly
skipped, followed by QEMU exit 0 without a kill signal. Full qualification
and normal late observer release remain unproved.

Pinned `a2384967…` source bounds the fault:

- `kernel/module/main.c`, `complete_formation` / `load_module`, calls
  `module_enable_text_rox` before `prepare_coming_module` /
  `klp_module_coming` and `do_init_module` for that load. Thus the sampled
  wait is not execution of its new livepatch init/callback. The same first
  attempt later reached callbacks and returned EBUSY: progress eventually
  occurred; this is not a claim that callbacks never ran.
- `arch/x86/mm/pat/set_memory.c`, `mm/vmalloc.c` and `arch/x86/mm/tlb.c`
  match the captured alias-purge path. `flush_tlb_kernel_range` chooses
  `do_flush_tlb_all` or `do_kernel_range_flush` by range and synchronously
  invokes the applicable CPUs. The selected stack does not identify which
  branch, target or outstanding call stopped progressing.
- `kernel/smp.c:785–889` serializes per-origin/per-target CSD storage,
  records the queue event, links work, sends an IPI when required, executes
  the local callback and waits for synchronous CSD locks. Target processing
  emits entry/exit around the callback and clears the sync lock afterward.
  A wait may concern reused storage before a new queue or completion after
  queuing. Queue events precede linking and batch IPI dispatch; they alone
  do not prove an IPI was sent or received. Coalescing also prevents a
  one-to-one queue/IPI assumption.

All-CPU NMI/RCU stacks are useful interrupted-context samples, not a
target-associated CSD history, simultaneous snapshot or host scheduling
measurement. Missing replies, register RDX=0x26, elapsed time and later
load/memory cannot establish starvation, a target number, probe causation,
flakiness or a kernel defect.

Existing facilities suffice for a finite next guest capture: the three
`csd` events expose target/callsite/function/CSD and callback entry/exit;
the two existing `ipi_send_cpu`/`ipi_send_cpumask` events distinguish reaching
dispatch from only recording queue intent. Both dispatch events precede the
architecture send, so neither proves hardware delivery. Retained frozen
`.config` enables TRACEPOINTS/EVENT_TRACING/FTRACE/SNAPSHOT but disables
CSD_LOCK_WAIT_DEBUG. Do not invent a CSD-debug boot switch or add a probe.
The existing migration CSD recorder starts after activation and was too late.
The softlockup source does not itself call `ftrace_dump`; dump-on-oops alone
cannot promise a first-warning capture without changing panic policy, which
is outside this remedy.

The [accepted package](implementation-plan.md#accepted-loader-csd-and-owned-host-evidence-package)
prepares existing events early, records only activation, preserves a bounded
first-fault window, and pairs it with read-only samples of the **owned**
QEMU/vCPU threads. Guest and host clocks require explicit marker/bracket
alignment. Host identity, proc permissions, usable scheduling counters and
guest-CPU/vCPU-thread association remain required on each run. Initial c08
readiness proves these only for its first snapshot. Original loader-owner
boundaries remain qualification.rb, the temporary CI wrapper,
one finite Bash sampler and `tests/suite/kernel/livepatch-6.12.95-common.nix`.
The fourth path adds only diagnostic QEMU thread naming through the existing
`boot.qemu.extraQemuOptions` list, using `lib.mkAfter [ "-name"
"debug-threads=on" ]`. Gate it on non-null qualification with exact id
`amd-scale-aged-v5`, vendor `amd`, predecessor `v5`, 128 CPUs, 16384 MiB,
100000 tasks and age 300 seconds. All other profiles, including the original
14400-second profile, retain their options.

This resolves C's [three-path naming stop](package-c-scheduler-hotplug-preparation.md#current-loader-evidence-launch-naming-prerequisite)
without a private API or a guessed label. OSVM appends extra options after
its initial `-name os-vm-machine`. Exact QEMU 10.2.4 `system/vl.c` declares
the name list mergeable and parses it after CLI collection;
`util/qemu-option.c:608–643,743–836,881–946` reuses the same unnamed list
and adds the explicit `debug-threads` key without replacing `guest`.
Therefore the appended pair enables thread naming while preserving the
guest name and every other argument. The retained archive and declared-patch
evidence are linked in C's receipt; the plan records the precise source chain.
QEMU documents these labels as debugging, not a stable API: keep the exact
source binding and runtime guest-CPU/APIC → QEMU cpu_index → owned TID/name
validation. Record the new head/config/system and explicit naming option;
do not claim whole-guest input equality with b361.

The baseline requires owned per-thread stat identity/state/CPU fields and
raw user/system proc-stat ticks, with frequency explicitly unavailable.
In the superseded 23db helper, lines249–257 used CLK_TCK only for its gate and
header, while lines159–164 compared same-identity counters and lines68–72
capped elapsed uptime. Qualification reads ready/map/status; the workflow reads
completion status. Neither converts counters to time. c08 removed the unnecessary
command, validation and frequency claim; do not restore it, guess 100, add a
provider or change PATH.
Retain `CLK_TCK=UNAVAILABLE` in the metadata and label
`cpu_units=proc_stat_ticks`. No CPU-duration, percentage or cross-machine
rate comparison is supported. Guest `getconf _NPROCESSORS_ONLN` assertions
remain unchanged. Sample ordinary
voluntary/nonvoluntary context-switch counts when readable; explicitly mark
missing counts unavailable. Zero initial counters are valid. Do not read or
require schedstat accounting: runnable-wait duration, schedstat runtime and
timeslices are always **UNAVAILABLE**, never substituted with zero or context
switches. CPU-time growth proves some thread execution, not execution of the
guest callback; state R or unchanged tick counters cannot establish continuous
runnable wait, starvation, host scheduling causation or a kernel defect.

Pinned Linux `a2384967…` supports that distinction: `fs/proc/array.c`
emits adjusted per-task CPU time and context switches; `kernel/sched/core.c`
increments the switch counters on scheduling independently of the dynamic
schedstats gate. `fs/proc/base.c:514–525` can instead emit `0 0 0` for
schedstat when sched-info accounting is off. These source facts describe the
retained implementation and public fields, not a discovery of the actual
runner node's kernel version or performance. No overhead percentage or
shared-node safety guarantee follows from the official documentation's
general accounting-cost description relayed by root.

Correct the clock assumption too. Pinned `fs/proc/array.c:585–587` and
`fs/proc/uptime.c` apply time-namespace boottime offsets; a container may also
have a virtualized proc view. Do not assume the actual runner uses either
particular mechanism or subtract process-start ticks from its uptime.
Treat start ticks as proc identity. Use elapsed readings within the inherited
runner-visible uptime view, from a wrapper origin captured **before** spawning
sampler/test child; the 3600-second bound then conservatively includes launch
preparation. Reject unavailable/regressing/inconsistent clock observations.
Keep host request/ready and guest-marker send/reply brackets, sampled wall
times and actual gaps; label clock views and uncertainty instead of equating
host uptime, Ruby monotonic and guest trace bases. No cross-domain delta
tolerance or forward-jump detector is required. Validate observations within
each named domain; retain forward wall changes as raw timing uncertainty.
Claim only associations established by the recorded brackets. An unestablished
association remains unavailable and does not imply a scheduling stall.

Readiness now means the one baseline contract is usable, not global stats=1.
Existing ready/map records and sampling/complete/error state semantics remain;
samples explicitly declare the unavailable measurements. The five guest
events, attempt PID/first-fault window and all identity/health/recovery checks
stay required. This can identify guest CSD progress and correlate coarse host
thread progress; it cannot quantify runnable wait or prove its cause. A later
isolated/dedicated-node experiment could be proposed if that missing fact
becomes necessary, but is neither authorized nor a new production-node gate.

Quick checks cover a representative PATH without getconf, a must-not-call
getconf sentinel, real-helper raw-counter progress/decrease/zero cases,
unchanged status consumers and actual wrapper EXIT/error/cancellation.
Retain identity, clock-view/cap and stats-disabled regressions; reuse
unchanged workflow/common receipts only for their exact scopes. Sampling
still targets two-second intervals with measured gaps.
A folds the refinement into the seventh loader-evidence owner after b361,
retaining tested `c08`, `23db`, `9805` and the old/new range inventory plus the six earlier
objects/messages. Do not fold into dying-rq `538706` or erase the LC1 review
history. The changed contract needs affected ALL4/HIGH review before any
publication or separately released run; prior LC1 reconciliation is not that
review. This amendment needs no common.nix change or new environment.
No generic runner API, global scheduler trace, SSH access, dependency project
or production kernel change is justified. All existing profile, identity,
watchdog, health and recovery contracts remain.

## Superseded decisions

- The initial proposal froze all `.95` module build support to preserve the
  October digest. The user rejected that policy. The proposed input helper,
  producer rewiring and related pin changes are withdrawn.
- The next proposal separated instruction-layout witnesses onto a historical
  artifact. The lead withdrew it, and the user requested safe current-build
  witnesses. That split and its reduced ordinary coverage are withdrawn.

Earlier recommendations in [fixture-contract.md](fixture-contract.md) and
[ordinary-ci-checks.md](ordinary-ci-checks.md) are historical analysis, not the
current implementation contract. Their source/evidence inventories remain
useful. The current site contracts are
[probe-redesign.md](probe-redesign.md) and the measured feasibility report below.

## Finding and evidence

The strict fixture rejects different module bytes. Its normal producer consumes
moving build inputs while the fixture expects a fixed historical module digest.
The revised solution changes that test policy so ordinary CI tests current
normal-package bytes. The evidence below is unchanged by that policy decision.

The immediate cause is proven. The exact first byte-changing dependency or
commit has not been isolated; toolchain version names alone do not prove it.

| Identity | Evidence |
| --- | --- |
| Expected module SHA-256 | `573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d` |
| Historical independently measured SHA-256 | `573e8d1e05433be7c4eab361bb733e92977496f6437b43a4af1e5d21d2452d9d` (exact match) |
| Current measured module SHA-256 | `7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f` |
| Current producer | `/nix/store/qi47yi2g9kp89dv0h8jxwndm89vbq6az-livepatch_7-6.12.95` |
| Current producer derivation | `/nix/store/161r03nnqvqw9g2ar5kjsbz00zr7xydg-livepatch_7-6.12.95.drv` |
| Failing fixture derivation | `/nix/store/vg23dzka1i0dw28fy3kl4wssyms484yx-livepatch_7-exact-candidate.ko.drv` |
| Last observed nine-row green run | [40296454457](https://github.com/vpsfreecz/vpsadminos/actions/runs/40296454457), `d9be8c4bada590c0405df85444600d40e6f3caa6`, October 26 |
| First subsequent CI run | [41072532280](https://github.com/vpsfreecz/vpsadminos/actions/runs/41072532280), `05201326975fc19d20a545c52f651cce0420dbc9`, October 30; nine fixture-preparation failures |
| Repeated current failure | [41666620193](https://github.com/vpsfreecz/vpsadminos/actions/runs/41666620193), `dd188397abe37d0bc33f4c5dfb3605206ce5e326`, November 3; same failing fixture derivation |

The current output was copied from the signed vpsAdminOS cache, with both trust
and content verification passing. Running the fixture's checksum assertion
against those bytes returned exit 1. No kernel/livepatch compilation or VM was
needed. The checksum step precedes the runner; missing `test.log` is secondary,
not a runtime transition failure. Fedora changes are excluded by the identical
failure/derivation before Fedora 45 was added.

Evidence owners and durable receipts:

- [workflow-lineage.md](workflow-lineage.md): implementer0's canonical run/job
  and artifact evidence, bounded regression interval and unchanged relevant
  workflow/fixture/source files.
- [candidate-identity.md](candidate-identity.md): implementer1's exact module,
  signature/NAR, source/input graph and direct assertion evidence. Complete
  current recursive graph contains 2,874 derivations; raw JSON SHA-256
  `89db60eaa48659f58d6075aa969eea8dcfd9468632893f5ac8ecda57d8d54839`.
- [fixture-contract.md](fixture-contract.md): implementer3's producer/consumer
  map and original integrity/qualification policy; its freeze recommendation
  is superseded by [ordinary-ci-checks.md](ordinary-ci-checks.md), which records
  the revised digest flow and exact instruction/ABI witness inventory.
- [historical-candidate.md](historical-candidate.md): implementer2's historical
  metadata reproduces the green wrapper and producer from both the
  pin-introducing revision and last green revision. The corrected exact-target
  cache copy succeeded in 3.38 seconds; independent module hashing matches the
  expected digest, and content/signature verification passed. The earlier
  malformed copy was stopped and reconciled; its extra `.` operand is a tool
  invocation error, not evidence against historical artifact availability.

## Source mechanism and provenance

`tests/fixtures/livepatch/default.nix` takes current `pkgs`, imports the normal
OS with `livepatch-6.12.95-boot-base.nix`, checks its module against the constant,
then symlinks that module. The normal flake package `ci-livepatch-6_12_95` uses
the same boot-base configuration and service producer. Lifecycle tests load
the normal guest producer; other qualification tests consume the checked
fixture. Their linkage must remain explicit and verified.

The boot-base module preserves current kernel package metadata and native build
inputs while replacing boot out/dev/config with frozen outputs. The service
module separately freezes `.95` development/configuration inputs and prefixes
the original compiler for kpatch invocation. Its outer stdenv, `depsBuildBuild`,
kpatch-build package, native inputs and builtin-ZFS preparation still follow
current packages. The measured current graph combines GCC 15.2 for kpatch's
kernel compile with a GCC 15.3 stdenv/compiler dependency and ZFS configuration.
The historical support compiler is also labelled GCC 15.3, but has a different
store identity. Version labels do not isolate the changing dependency. The
pinned GCC itself includes binutils 2.46: the build log's 2.46 linker is
therefore not evidence of a broken PATH lock.

The expected digest was introduced at
`3ddca3e6b84017f37499568d3efaefa7c4e2e72f` with recorded independent producer,
711-symbol CRC and focused runtime checks. Its root stable Nixpkgs input is
`a033e66ab94a6bedf2c3d58d93a36319d3cbbbaf`, NAR
`sha256-yvkDdToRZ4IgPc9tSBzzCYJvTLf8n5eE3rgUkpCuD5A=`. The last green root
uses `1f607aa79b6356ed45d3cd3c8079c196e79efa2c`; the first red root uses
`6f06d204d8f2d8761d9da78778745974a3216381`. Relevant source files are unchanged
across that observed interval. Root Nixpkgs is lock node `nixpkgs_2`, not the
separate impermanence input named `nixpkgs`.

Both historical roots evaluate to producer
`/nix/store/6hiwxy4nmpnb18xmsn9a5mh5g8mb246p-livepatch_7-6.12.95` and checked
wrapper `/nix/store/m3ig6h5s0ldclfyl3mrss6n5psrw0j7d-livepatch_7-exact-candidate.ko`.
The latter matches the green CI artifact. The published cache deriver
`/nix/store/50irawqs0aaks9d6n2brj411hz4w4nhd-livepatch_7-6.12.95.drv`
matches pin-introducing evaluation exactly. Last-green evaluation instead has
deriver `/nix/store/maa7anq6rx7id4hwzc6z1fagv46xv9i6-livepatch_7-6.12.95.drv`:
Linux-fetch/ZFS derivation edges differ while the selected producer environment,
builder, arguments, source paths and output agree. Preserve this distinction.
The producer was copied successfully and its contents/trust verified with the
documented cache key and `--sigs-needed 1`. Its registered NAR is 172,084,880
bytes, SHA-256 `sha256-me0OAsawV0Tb1BaW+RIa1h0SJB8Zlnhz507vUI9gwDk=`
(base32 `0ff0c27m1vsfwxrpi5hr3wj147fn389gk5hnskdl8mxhqq10xvcr`). Its module's
independently measured digest is exactly `573e...`. The checked wrapper itself
is absent from that cache; it can be evaluated from source and does not need
to be cached to retrieve the underlying module. The complete historical graph
hashes and source inventories are retained in the linked receipt. Neither copy
is still running; no historical kernel/module build was performed.

Keep this module-input provenance distinct from the frozen **boot** producer
`c065fa2f8485399737e20e8ef9e44299d0766654`, whose root Nixpkgs is
`21a67dc470149f337cecafbe965d8d252a390518`. Reusing the boot package set alone
is not proof of reproducing the independently pinned v7 module.

## Current binary feasibility and selected witness design

[probe-elf-feasibility.md](probe-elf-feasibility.md) independently compares the
signed-cache current and historical modules. All executable sections, symbol
tables and code/data/livepatch relocation sections match. Of 2,322 named
sections, only `.debug_str`, `.rela.debug_info` and `.note.gnu.build-id` differ.
The measured `.text` SHA-256 is
`d5ae5fadc4b620e5ee25662af2babb8864040f4d3c0e8ac0cf8fef6321fe81d5` for both.
There is no observed instruction-layout drift in this pair. That explains why
a whole-file allowlist can reject harmless differences; it is not whole-module,
ABI or runtime equivalence proof, nor permission to trust later offsets.

Nine finite selectors cover three current post-fentry entry boundaries, the
FUSE caller, three SUNRPC calls, fragment timer registration and TCP's completed
size comparison. The host record is bound to the once-captured current module
and consumed through validated module-qualified runtime symbol lookup. Keep
fixed boot sites and data-layout checks separate. The detailed supported
operands, registers and inline identities are in the linked reports; do not
replace those semantics with source-line numbers or remembered offsets.

FUSE requires special care: two finish calls have the same callee and preceding
unlock. Inline `fuse_ref_page` identifies the intended call. Its established
interior frame does not satisfy an entry trampoline's contract. Instead, hold
at the actual original fuse callee's validated entry/preprologue boundary,
filtering the exact selected caller return PC before count/capture/hold. This
preserves copy-state and the original caller frame without adding an interior
alignment trampoline. Original callee namespace/position, safe stack and ftrace
compatibility must be verified; there is no spin/interior fallback.

TCP has a concrete current semantic observation: in inline `tcp_mtu_probe`,
validate widening before add-one/multiply and resolve the comparison with the
completed value live. A read-only trace observation must establish the intended
sender, `reordering == UINT_MAX`, positive MSS and `size_needed > UINT_MAX`.
Keep the 8 MiB transfer and add receiver EOF, length and exact-content checks.
This retains the arithmetic property and strengthens data integrity; a mere
`tcp_write_xmit` entry hit or behavioral-only substitution is not the plan.

The small return-PC filter extends the existing C test helper. No production
module, boot helper, root lock, assembler trampoline, generic register reader
or new discovery mode is planned. Test-only structured parsing uses standard
pyelftools/Capstone packages; availability/packaging and negative-control
robustness remain implementation checks, not conclusions of this investigation.

## Compatibility, verification and limits

The original livepatch package changes tests and preparation metadata; the
separately accepted shutdown correction changes osctld concurrency as specified
above. Neither adds a production schema, persistent format, external API,
protocol, deployment ordering or coordinated node update. Captured hashes
establish artifact identity/transfer integrity; only
actual test results establish the declared properties for those bytes and the
recorded boot identity. Callback counts, predecessor retention, downgrade
rejection, timeouts, task/memory/CPU shapes, kernel health, quarantine and
recovery rules remain independent and unchanged. Aging is temporarily 300
seconds only for diagnosis, with 14400 restored before final qualification.

The current normal module is already published. Its existing builtin-ZFS
preparation can require a separate plain-kernel development output when caches
are cold. Removing the checksum does not eliminate that dependency. Reuse
published outputs and stop unexpected local kernel builds under the existing
cache policy; no kernel rebuild is part of authoring or accepting this plan.

Implementation proceeds through the scoped packages, quick checks and negative
controls in [implementation-plan.md](implementation-plan.md), then committed
whole-branch independent review, focused runtime acceptance and the existing
long matrix. Fresh utilities monitor long/uncertain operations. These planning
records alone do not require automatic change review.

Finite remaining proof points are parser support for actual livepatch/DWARF
metadata, semantic selector robustness, FUSE original-callee identity and
reliable-stack hold behavior, and TCP live-value reachability. The cached ELF
shows viable anchors; no runtime test, import-CRC recomputation or resolver
implementation has been performed. An unsupported constraint must stop the
affected package and return to the lead. It must not silently select a stale
site, weaken a witness or revive the historical split.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
