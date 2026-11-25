# Current-build livepatch tests: execution plan

Architect0, retained Astra/xhigh. Implementation baseline:
`vpsfreecz/vpsadminos@dd188397abe37d0bc33f4c5dfb3605206ce5e326` in this
session's registered worktree. The user subsequently authorized implementation
with **“implement it”**, as relayed in the lead's implementation assignment.
Lead's fresh fetch confirms staging remains at this exact baseline. That
authorization does not include integration, deployment, lifecycle actions or
an input freeze. Architect owns this design; implementers own application/test
edits, and the lead serializes Git mutations and tracks execution/verification.

## Current diagnostic status and user decisions

**Current checkpoint: H failed native prebuild; one-file correction brief complete.**
Exact56b9363/run42079730277 attempt1 is terminal FAILURE, with321/323 native
scripts and107/109 groups passing; root accepts all nine lifecycle audits
at their own scope. The
[current native blocker packages](#current-final-f-native-blocker-packages)
separate a bounded LXC attachment diagnosis from a test-only NFS caller
protocol correction. Both native failures remain unwaived. Original14400/full
exact-final native+9 and conditional merge gates remain. Earlier final
preparation paragraphs below are retained history.

N74297e's implementation,20 controls and ALL4/HIGH review are now accepted.
Its source-identical skip-message sibling Hc916a804/run42176307860 failed
evaluation of `pkgs.ruby_vpsadminos`, before any selected VM/writer ran. The
[current correction package](#current-h-provider-correction-package) replaces
that unavailable attribute and closes the actual-context verification gap.
A's source remains frozen pending root allocation; no implementation or new
run is released here. No additional LXC diagnostic is required to correct N.

**Accepted ordinary prerequisite.**
Exact802898/run42057169147 passed the complete selected aged-v5 case, including
post-health, disable, migrations, workload/resource stop and graceful teardown.
Root accepted C's full audit and the ordinary ALL4/HIGH review. No further
shortened matrix or collector refinement is required. A's fresh target
preflight confirms exactd2fe, one flake.lock-only unstable-input update after
base2951, with primary645927/ordinary802898/instrumented08e refs unchanged.
The [retained preparation brief](#accepted-final-preparation-package) was
subsequently executed through F. That short ordinary pass did not supply
native, other rows/main semantic cases, original14400 or final-target
qualification. Current evidence remains under the native blocker section and
root's row acceptance; earlier paragraphs below are retained chronology.

The user requested reduced aging “until the problems are identified and
fixed”. The lead selected **300 seconds temporarily for diagnosis**. C's
checked one-file patch is saved as `package-c-diagnostic-aging.patch`, SHA256
`c46380fdc1f05abd76fd975e25321d40ee2e37a15fdbcdb59c1ff42810554dde`.
The reviewed/published production head 645927 currently has original 14400
with the comment absent. The saved patch is now used by diagnostic head
`bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf`, run `41921632759`, before
final full-profile qualification.
Keep 128 vCPUs, 16 GiB, 100000 tasks, full recovery, strict health, boot and
predecessor checks. **Restore 14400 before the final four-hour qualification
after fixes.** Never present five-minute diagnostic success as full aged
acceptance. No final acceptance gate or historical evidence is removed.

The operator owns “updating all gh runners”; the session owns no runner
activation, trust repair or prebuild. Run `41865572140` is canonically
completed/cancelled after A's one cancellation of the known failed run:
retain five lifecycle passes, the native failure and four cancelled lifecycle
rows. Focused shutdown dispatch `41913307185` is the preceding checkpoint.
Diagnostic run `41921632759` supplied the pre-transition scale-aged-v5
hotplug failure and distinct low-memory-v5 pass. Later one-case run
`41938327930`, source `13b658f67c37418d6bbf91316ea7b3c6db99fe17`,
failed during observer enable. Its successor
`b361b8c600bc1d50c237a68ca5413d38be9a0e99` / `41951210319` is also terminal
failure: actual early arming and healthy CPU127 capture passed, then loader
liveness and the activation deadline failed. No current CI/watcher or new
run is released. See the
[bounded scheduler package](#bounded-scheduler-hotplug-evidence-package).
Later loader-only diagnostics culminated in exact 08e/run42040026542, also
terminal RED. Host coverage and insertion passed their bounded scopes, but
native capture and ordinary post-transition qualification did not complete.
The [current disposition](#accepted-loader-csd-and-owned-host-evidence-package)
recommends retiring the temporary observers and preparing one ordinary 300s
case; root has not released preparation or a run through this document.
Final exact-head native and all nine full-profile lifecycle rows remain required.

D completed the shutdown source-race reproduction: focused 3 examples have
two passing controls and one intentional red; the three-file set has 24
examples, 23 passing and that same red. The initial environment block and
later bounded declared-environment preparation remain retained evidence.
The user has accepted the
[production correction](#accepted-shutdown-fix-acceptance-and-scope) as a
separate commit. D's implementation/quick checks are complete, all four lanes
of [committed review](shutdown-fix-review.md) passed without findings, and
`645927e22809a29c67ffd59c072e553e05e2a72b` is published. The accepted
[diagnostic-head route](#conditional-diagnostic-head-and-final-verification-package)
has advanced to its separate diagnostic run. C's temporary age patch remains
separate from production; current diagnostic failure is not final acceptance.

## Outcome and established feasibility

Ordinary CI will test the current normal module, tolerate harmless binary and
layout movement, and preserve precise current-build witnesses. Remove the
historical candidate allowlist; retain exact released predecessors, frozen
boot identity/ABI and recovery behavior. Neither an input freeze nor a
historical-witness lane is proposed. Missing, ambiguous or incompatible probe
semantics must fail before installation, with the affected witness named.

[probe-elf-feasibility.md](probe-elf-feasibility.md) establishes the finite
current sites from restored signed-cache artifacts. The examined old/current
pair has identical executable sections and code relocations; only debug
strings/debug relocations/build-ID note differ. No instruction drift was
observed in that pair. FUSE has two similar calls distinguished by inline
identity; TCP exposes its completed wide result at a comparison. These facts
establish a credible implementation target, not runtime/ABI qualification.
[probe-redesign.md](probe-redesign.md) owns the detailed argument, frame and
semantic contracts; [design.md](design.md) owns the decisions and history.

## Small shared contract

1. The existing CI build job captures the realized normal `.95` producer,
   module path and SHA-256 once, with checkout/input identity. Resolve sites
   from those bytes. Pass module identity and the site-record output to every
   dependent row using ordinary job outputs and the existing cache/artifact
   mechanisms; include the small site output in the existing cache publication.
2. Each row resolves its fixture and verifies it matches the captured producer
   and digest. Export the existing module/SHA variables and one new
   `VPSADMINOS_LIVEPATCH_CORRECTED_SITES` store path. Local runs realize/capture
   once before test discovery. Never hash an unrealized output during Nix eval.
3. A test-only host resolver reads ELF symbols, ordinary and `.klp.rela`
   relocations, inline DWARF and decoded instructions. Use pyelftools/Capstone
   from the repository's current Nix package set to avoid a handwritten ELF
   decoder or broad text-parser compatibility layer. These dependencies are a
   bounded packaging choice; availability/cost was not checked in this plan.
4. Emit `sites.json`: schema version, module digest/ELF identity and nine
   enumerated witness records. Each has exact symbol/object/position, section,
   inline/callee context, function-relative site and instruction length,
   approved observation/entry-hold kind, and required register-width/frame
   predicates. FUSE also records its original callee and exact caller-return
   construction. ABI member offsets are separate validated type facts.
5. Require exactly one valid site per witness. Consumers verify digest,
   completeness and bounded field types, then resolve unique module-qualified
   runtime symbols. No guest virtual addresses, arbitrary probe programs,
   guessed offsets, source-line pins or historical checksum belong in the
   resolver contract. The guest verifies the module bytes before using sites.

The checksum proves which artifact was selected and copied, not that it is
independently qualified. Test outcomes and callback counts remain independent
expectations. Source/ABI or compiler transformations outside the finite
supported predicates fail explicitly; offset, debug-line, section-placement
and supported register-allocation movement do not require repinning.

### Accepted implementation interface

The lead accepted B's final field names below; A/B/C/D may implement against
this contract immediately. This records the settled interface without adding
a design gate. There are no alternate field names or compatibility aliases.

The top-level JSON shape is the following template. `WITNESS` expands to each
of the nine keys in the table below; paths, symbols, offsets, sizes and register
roles come from validated inputs. Numeric values in this template are
illustrative except `schema_version: 1` and `elf_class: 64`.

```json
{
  "schema_version": 1,
  "module_sha256": "64lowerhex",
  "elf": {"elf_class": 64, "machine": "EM_X86_64", "build_id": "hex"},
  "abi": {
    "sock_xprt_connect_worker": 1600,
    "inet_frag_timer": 56,
    "inet_frag_node": 0,
    "inet_frag_lock": 96
  },
  "sites": {
    "WITNESS": {
      "object": "livepatch_7", "symbol": "caller_name", "symbol_pos": 0,
      "section": ".text", "symbol_size": 123, "offset": 5,
      "instruction_length": 1, "kind": "entry_hold",
      "frame": "preprologue", "inline": null,
      "registers": {"arg0": {"register": "rdi", "width": 64}}
    }
  }
}
```

All common site fields shown above are present in all nine records. Offsets
are relative to the named symbol; require nonnegative offsets, positive
instruction lengths and `offset + instruction_length <= symbol_size`.
`symbol_pos: 0` requires one exact module-qualified defined caller symbol,
without guessing an ordinal. Consumers enforce the recorded symbol bounds
when constructing runtime addresses. ABI offsets must agree between matching
candidate and boot SDK types; none of the illustrated values becomes a pin.

Runtime clarification after CI run `41740116653`, corrected by independent
review: the module's kallsyms list also contains relocated imports. The final
kernel formatter lowercases non-exported module types. Both existing lookup
queries must exclude `U` **and** `u` rows before the unchanged exact-one definition
check. Match exact name and `NF == 4`/exact module, or native `NF == 3`.
Keep defined data symbols valid and reject duplicate defined rows without
deduplicating equal addresses. Original FUSE position 1 and accepted positions
0/1 are unchanged. This needs no new field/schema or section-range lookup;
[design.md](design.md#accepted-runtime-lookup-correction-november-4) records
the current ELF, full frozen-kernel formatter path and superseded uppercase-only
decision. No generic GNU `nm` type meaning overrides this kernel output contract.

| Exact `sites` key | `kind` | `frame` | Required inline context |
| --- | --- | --- | --- |
| `svm_entry` | `entry_hold` | `preprologue` | `null` |
| `nft_insert_entry` | `entry_hold` | `preprologue` | `null` |
| `sunrpc_worker_entry` | `entry_hold` | `preprologue` | `null` |
| `fuse_finish` | `callee_entry_hold` | `observe_only` | `fuse_ref_page` |
| `sunrpc_shadow_alloc` | `call_observe` | `observe_only` | `null` |
| `sunrpc_callback_claim` | `call_observe` | `observe_only` | `null` |
| `sunrpc_callback_release` | `call_observe` | `observe_only` | `null` |
| `inet_frag_timer` | `call_observe` | `observe_only` | `inet_frag_create` |
| `tcp_mtu_size` | `tcp_size_observe` | `observe_only` | `tcp_mtu_probe` |

`kind` and `frame` have only the enumerated values in this table. Registers
use canonical 64-bit x86 names `rax`, `rbx`, `rcx`, `rdx`, `rsi`, `rdi`, `rbp`,
`rsp`, `r8` through `r15`, with `width` restricted to 32 or 64. Entry records
use role `arg0`; call observations include `arg0` when used. TCP has exactly
`needed` (64), `reordering` (32) and `mss` (32). The resolver validates each
role's semantics and liveness; register text cannot supply arbitrary programs.

For FUSE, the common record describes the **candidate caller's call**, not the
installed hold address. It additionally has
`return_offset = offset + instruction_length` and this nested original-callee
record, with actual resolved values:

```json
"callee": {
  "object": "fuse", "symbol": "fuse_copy_finish", "symbol_pos": 1,
  "section": ".text", "symbol_size": 123, "offset": 5,
  "instruction_length": 1, "frame": "preprologue"
}
```

The original callee's position comes from the exact
`.klp.sym.fuse.fuse_copy_finish,1` namespace and one verified matching symbol
in the raw original FUSE ELF. Its offset is the validated safe entry/post-fentry
hold site. Other call records use
`callee: {object: "vmlinux", symbol: "<validated target>", symbol_pos: 0}`.
C's narrow helper parameter is `probe_caller_return`: configure while disabled,
compare the entry-stack caller PC before count/capture/hold, and reset when
the probe address becomes zero. Keep existing resume/teardown guards.

The CLI always resolves all nine records:

```text
python probe-sites.py --module MODULE --sha256 CAPTURED64HEX \
  --fuse-module RAW_ELF --sdk-vmlinux FILE [--output FILE]
```

Emit JSON on stdout when `--output` is absent. Validate strict lowercase
64-hex SHA-256 and actual module equality before decoding. Unsupported,
missing or ambiguous semantics produce a witness-key diagnostic on stderr
and exit 1. There is no generic CLI selection mode. The public testing API is
`resolve_site(witness, module, sha256, fuse_module=None, sdk_vmlinux=None)`
returning one site dict, and
`resolve(module, sha256, fuse_module, sdk_vmlinux)` returning the full JSON
dict. Only the finite nine witness keys are accepted; failures raise
`ResolutionError`. Per-key tests need only relevant inputs: module for entries,
original FUSE and inline DWARF for FUSE, SDK/candidate types for RPC/fragment,
and inline DWARF plus the typed block for TCP.

`probe-sites.nix` accepts `{ pkgs, candidateModule, bootKernel ?
(import ../../../os/packages/linux/boot-6.12.95.nix).kernel }` and returns
`resolver`, `siteChecks` and `candidateSites`. The latter is a directory with
`sites.json`. The wrapper extracts/decompresses exactly one original FUSE ELF
using xz/zstd as applicable and uses `bootKernel.dev/vmlinux`; the imported
livepatch symbol name alone cannot validate that callee. `siteChecks` compiles
D's tiny source fixtures with `stdenv.cc` and uses packaged pyelftools/Capstone;
it must be independent of candidate/SDK realization and kernel compilation.

A exports `candidateProducer`, `candidateModule` and the `corrected` symlink.
The existing build job captures producer/module/SHA/sites once; all dependent
rows verify that identity. The JSON digest path is `module_sha256`. NFS/SCTP
validate the supplied environment digest as strict lowercase 64-hex; no
`builtins.hashFile` of an unrealized module is introduced.

## Packages and dependency order

Owners are retained existing members under the accepted implementation
assignment. Lead serializes shared-file edits and Git writes. Package A first
prepares hooks and the declared Nix environment; B/C/D use the accepted finite
record interface above to connect their code.

| Package / owner | Exact source boundary | Dependencies and completion evidence |
| --- | --- | --- |
| A — identity / implementer0 | `tests/fixtures/livepatch/default.nix`, `.github/workflows/ci.yml`, `tests/suite/kernel/livepatch-nfs-transition.nix`, `tests/suite/kernel/livepatch-sctp-common.nix` | Remove candidate allowlist, retain predecessor checks, capture once in build job and verify all rows against it. Wire B's exports after its interface is settled. No normal producer/boot/lock change. |
| B — resolver / implementer1 | New `tests/fixtures/livepatch/probe-sites.py` and `probe-sites.nix` | Implement only the nine contracts in the linked reports. Export independent `siteChecks` and realized-module `candidateSites` attributes through A's fixture wiring. B owns parser/selector code and packaging; no runtime test edits. |
| C — witnesses / implementer3 | `tests/suite/kernel/livepatch-6.12.95-common.nix`, `tests/suite/kernel/livepatch-inet-frag.nix`, `tests/suite/kernel/livepatch-6.12.95/livepatch_test_probe_main.c`, `docs/os/testing.md`, new `test-runner/spec/test_runner/livepatch_runtime_sites_spec.rb` | Consume A/B identity and records; replace candidate literals and stale grep offsets; add the narrow FUSE filter and TCP value/receiver checks. Add meaningful consumer validation/negative controls in the existing spec framework. Preserve frozen boot sites, existing profiles and recovery. No `.S` or general register-reader change planned. |
| D — resolver controls / implementer2 | New `tests/fixtures/livepatch/test_probe_sites.py` and small source fixtures under `tests/fixtures/livepatch/probe-sites-tests/` | Independently encode the positive/negative contract below against B's stable interface. Small host ELF/assembly fixtures, not a kernel build or a committed historical module. B packages these through `siteChecks`; coordinate additions without editing B's resolver. |

A and B/D can start independently after the contract is accepted. C can prepare
receiver/filter work while B implements records, then connect only stable keys.
One combined branch must pass quick checks before review. Lead reconciles docs,
checks the full diff/history and routes consequential deviations through the
architect. Do not add production options, a registry mode, a separate historical
lane, input pins or a general disassembly service.

## Required witness implementation

- **SVM, NFT and TLS entry holds:** validate the real fentry boundary and the
  first safe preprologue instruction, with arg0 and entry stack preserved.
  Never replace `+5` blindly with a function entry. Keep repair/batch/ownership
  assertions and registration/miss checks.
- **FUSE:** select the `fuse_ref_page` inline call to the qualified
  `.klp.sym.fuse.fuse_copy_finish,1`, not the other `fuse_try_move_page` call.
  Hold at the resolved original callee's validated entry/post-fentry point;
  filter on the exact selected caller return PC **before** counting, capture
  or hold-slot acquisition. Add one optional return-PC predicate to the existing
  C helper, reset with probe teardown. Validate the callee namespace/position,
  ftrace compatibility and entry stack. Preserve arg0 copy-state, unlocked
  request and caller frame. This avoids redirecting an established interior
  frame through the entry trampoline. There is no spin/interior fallback.
- **SUNRPC allocation, claim and release:** use the three finite current call
  sites and existing non-holding counters. Preserve the allocation-path
  witness, matched worker after ownership transfer, pending disable and exactly
  one matching transport release. Do not substitute global helper hits.
- **Fragment:** resolve current timer registration in the appropriate
  allocation inline/function context, retaining native-unlocked/unhashed versus
  current-linked/locked observations and zero misses. Validate timer/node/lock
  member offsets against matching SDK/candidate type data before memory reads.
- **TCP:** match inline `tcp_mtu_probe` and the typed arithmetic/comparison
  sequence: zero-extend reordering before wide add-one/multiply, add probe size,
  then unsigned comparisons of the completed value. Bind register roles and
  liveness, not fixed spellings or `+0x7f9`. Use tracefs read-only GPR fetches,
  scoped to the known sender/workload, to require a sample with
  `reordering == UINT_MAX`, `mss > 0` and `size_needed > UINT_MAX`. This is an
  independent overflow property, not an entry-hit replacement. Store the
  existing receiver's stream, wait for EOF/exit, and verify exactly 8 MiB of
  the known zero payload as well as sender success. No new network helper is
  needed. Unsupported semantics or missing samples fail; no historical or
  weaker behavioral fallback is enabled by default.

Keep frozen-boot gate/offset contracts separate. All actual import CRCs must
match the boot SDK; the historical count of 711 is not a future-payload limit.
Production loader image/notes guards, `dontStrip` and predecessor anchors stay.

## Verification sequence and stopping conditions

For the November 4 runtime-lookup followup, C changes only the two existing
lookup methods in `livepatch-6.12.95-common.nix` and `livepatch-inet-frag.nix`
and their existing `livepatch_runtime_sites_spec.rb` controls. Exercise the
actual rendered AWK queries with native `T`, target-module `t`, same-module
lowercase `u` (the actual formatter case), uppercase `U` as a separate control,
unrelated/misnamed module, data-symbol, either-case import-only and duplicate-defined
fixtures, including equal-address duplicate definitions and positions 0/1.
After quick checks and review, rerun the real fragment witness and required
final-head CI; lookup success alone is not proof of timer ordering. No new
resolver, descriptor, source input or kernel build is part of this correction.
The [initial C receipt](package-c-runtime-symbol-failure.md) records 53 passing
consumer examples after six demonstrated regression failures, plus
format/lint/parse checks, for the superseded uppercase-only filter. Review
blocked that version: its lowercase-`u` preservation expectation was incorrect.
Replace it with both-case rejection, retaining real defined-data controls.
The complete [independent review](defined-symbol-review.md) contains one
Blocking finding, DS1. Lead accepted this bounded remedy and released C's
three-path correction plus receipt update. After relevant checks and commit,
lead owns focused inspection and finding reconciliation under the review
workflow; reuse unaffected review evidence. Actual fragment/final-head CI
acceptance remains pending and is not established by host fixture success.

**Quick, before final review:** declared hooks/formatting and changed Nix/Ruby/C
checks; host resolver controls; actual current cached-module site generation
and manifest/producer identity comparison; rendered test discovery and script
checks. A bounded SDK-backed test-helper compilation may be quick only after
its dependency closure is inspected; otherwise use the long-check workflow.
Current/historical artifact comparison may be reused as evidence for this
baseline, never as an ordinary historical allowlist.

Required negative controls:

- Wrong/malformed/missing digest, changed module after capture, different row
  producer, wrong record digest/schema and absent/duplicate symbols fail before
  any guest address is installed. Corrupt predecessor/boot identity still fails.
- Harmless padding/placement/debug-line/register-role changes retain selection;
  missing or ambiguous call/inline metadata, wrong object/ordinal, relocation
  displacement mistaken for opcode, unsupported prefix/frame or type widths
  fail. FUSE's other finish call must be rejected as the intended caller.
- TCP wrap-before-widen and wrong-width instruction fixtures fail the semantic
  predicate; wrapped result samples fail the independent property. Preserve
  register liveness checks. Do not require a locally rebuilt kernel/module for
  these host controls. Truncated/corrupt receiver output and sender-only success
  fail the data check.
- FUSE wrong return PC/unrelated caller cannot count, capture or hold; filter
  teardown cannot affect later probes. Wrong worker/transport, stale data-layout
  descriptor and missed events cannot satisfy SUNRPC/fragment assertions.

**Then:** commit all intended source/tests/docs, run mandatory independent
final review of the complete branch and history (no migrations), and reconcile
findings. Planning documents alone do not trigger that review.

**Long, after review:** fresh utility watchers run focused current-build
positive/negative witness cases first, then the existing nine AMD/Intel rows,
both predecessors, lifecycle/kernel-identity, main/perf/TUN/SCTP/NFS/fragment
and native `.110` continuity. FUSE acceptance requires target-only hold,
correct unlocked copy-state, reliable stack containing the intended caller,
release/resume and original abort/transition behavior. TCP must reach the
comparison with the declared precondition and wide value, with complete receiver
integrity. No functional pass may replace these properties. Full-scale cases,
independent callback counts, health checks, deadlines and recovery stay intact.

## Baseline refresh check package

A owns the authorized mechanical refresh of `742eb30..5235bfd` onto exact
`54b4313404cea35b58ebb9df951ae75e27c44971`, preserving the tested old ref.
First prove patch/range equivalence, unchanged commit message and all sixteen
feature blobs, with no unexplained source/index changes. A substantive conflict
or feature change stops for the lead. No new feature source edits are proposed.
The incoming source-identity integration and compatibility rationale are in
[design.md](design.md#accepted-baseline-refresh-onto-54b4313).

Run the following existing checks from the refreshed repository root, using
the declared test-runner environment (or the already verified exact cached
equivalent with its native-library receipt). These are commands for A's
execution package, not checks performed by the architect:

```sh
nix develop .#test-runner --command bundle exec rspec -I test-runner/spec \
  test-runner/spec/test_runner/repository_source_spec.rb \
  test-runner/spec/test_runner/cli/command_spec.rb \
  test-runner/spec/test_runner/prebuild_nix_spec.rb \
  test-runner/spec/test_runner/livepatch_runtime_sites_spec.rb
nix eval --impure --raw --option allow-import-from-derivation false \
  --file tests/source-version-eval.nix
nix eval --impure --raw --option allow-import-from-derivation false \
  --file tests/channel-revision-eval.nix
```

The first three spec files cover private-index preservation, captured
commit/snapshot stability and included extras, scoped environment restoration,
and propagation of the framework through direct/batch evaluation. The existing
livepatch consumer specs cover their intersection with this runner version.
`source-version-eval.nix` tests the real test OS constructor and revision
precedence/security evidence, including provider mismatch, unknown/dirty,
explicit overrides and legacy framework. `channel-revision-eval.nix` evaluates
known/unknown channel revisions without building the channel or guest. Keep
cached environment reuse bounded; long/uncertain setup/checks use the existing
fresh utility policy and stop unexpected kernel or old-Nix compilation.

Capture exactly one IFD-disabled Nix identity tuple on the refreshed head:

```sh
nix eval --impure --json --option allow-import-from-derivation false --expr '
  let
    f = import ./tests/fixtures/livepatch {};
    b = import ./os/packages/linux/boot-6.12.95.nix;
    identity = p: { drvPath = p.drvPath; outputPath = p.outPath; };
  in {
    candidateProducer = identity f.candidateProducer;
    candidateModule = f.candidateModule;
    corrected = identity f.corrected;
    resolver = identity f.resolver;
    siteChecks = identity f.siteChecks;
    candidateSites = identity f.candidateSites;
    boot = identity b.kernel;
    sdk = identity b.kernel.dev;
    config = identity b.kernel.configfile;
    bootCompiler = identity b.toolchain;
  }'
```

Use `outputPath` as the JSON field name: an attribute set containing `outPath`
can serialize as a store-path string and lose the requested `drvPath` field.
Bind this finite tuple to the refreshed commit, lock digest and existing
receipt values. Read actual module/site digests only from already realized
verified outputs; do not hash unrealized outputs during evaluation. Compare
the normal producer/module with the existing `qi47...` receipt and sites with
`aiqijl...`, retaining exact full paths in A's result. Equal paths/derivations
and unchanged resolver/control sources/tools can support their respective
prior receipt reuse. If identities differ, report the concrete difference;
do not build speculative closures or treat old `7c4d...` bytes as a required
allowlist. A different system/test closure from new version metadata is
expected and does not invalidate the current-build testing policy.

On the new CI run, the unchanged build/row identity checks must capture the
new checkout once and still agree on producer/module/SHA/sites/lock. Audit
the runner's `sourcePath`, `revision`, `shortRev`, `dirty` and guest
`revision`, `revisionDirty`, `versionSuffix`/security evidence against the
actual provider/snapshot, using existing outputs and logs. Matching-provider
guests must carry the captured full revision; included extras may legitimately
make the snapshot dirty. Never replace this with an assumed clean flag or
equate version metadata with module qualification. No new logging framework
or product source instrumentation is requested.

After quick checks and the normal hooked commit, give the retained independent
reviewer the old/new exact ranges, equivalence evidence, tuple and check
receipts. Scope review to the incoming source-identity/guest construction
interaction and once-captured livepatch interface, plus complete final
history/no-migration conclusions; reuse unaffected prior review. Publication
and full final-head CI follow under the lead. All nine lifecycle rows, native,
FUSE/TCP/fragment and positive frozen-boot identity witnesses remain required.
Latest-image device-unit verification stays blocking; do not waive it or
expand the unchanged wrong-image PATH control. Existing active workflows stay
under their existing owner. Architect performs no Git/CI/build/VM mutation.

## Packaged dependency refresh onto 2951a63

This is the current baseline-specific execution brief. The already reviewed
`54b4313..dc74bcd` two-commit series is stopped before publication; its remote
feature is still old5235. The lead accepted the bounded go decision for A's
complete mechanical refresh onto exact `2951a632c4254a44747a8da326e3dde897eaa0e2`;
no further architecture approval is pending.
[Design rationale](design.md#packaged-dependency-baseline-refresh-onto-2951a63)
records the separate bootstrap bundle and whole-repository source-gem input
effects. No application edits, new dependency pins or regeneration are needed.

1. Preserve reviewed dc74 and its old base/range. Replay both purpose commits
   onto exact2951; verify range-diff/patch equivalence, unchanged raw messages
   and all twenty feature file modes/blobs. Confirm the only incoming changes
   remain the paired `osctl-env-exec` lock/gemset version/hash update. Stop on
   conflicts, a changed feature patch or another baseline advance; return to
   the lead rather than silently expanding the package. Keep ordinary hooks
   and final whitespace/history/no-migration checks.
2. On the actual refreshed head, run the existing ten-field IFD-disabled tuple
   command above exactly once, with `outputPath` field names. Compare against
   `package-a-osvm-identity.json` and the declared module/sites/SDK receipts.
   Unchanged paths and actual verified bytes support their existing scoped
   evidence; a difference requires explanation before reuse. Do not restore
   a historical digest gate or launch speculative builds.
3. Record the affected package and representative guest/runner build identities
   in one bounded, evaluation-only command from the refreshed repository root:

   ```sh
   nix eval --impure --json --option allow-import-from-derivation false --expr '
     let
       f = builtins.getFlake (toString ./.);
       p = import f.inputs.nixpkgs.outPath {
         system = "x86_64-linux";
         overlays = [ f.overlays.default ];
       };
       identity = x: { drvPath = x.drvPath; outputPath = x.outPath; };
     in {
       osctlEnvExec = identity p.osctl-env-exec;
       osctl = identity p.osctl;
       osctld = identity p.osctld;
       testRunner = identity f.packages.x86_64-linux.test-runner;
     }'
   ```

   This confirms the new packaged input is evaluable and records the affected
   identities; it does not realize them or certify the new gem bytes. No
   old-head reevaluation is needed where no comparable receipt exists. The
   normal CI build/cache path validates required new outputs. Stop any
   unexpected local kernel/old-Nix/heavy build; use the existing monitor policy
   for uncertain-duration authorized checks.
4. Reuse D's 81 focused/207 full OSVM and A's 99 integration examples only after
   comparing their exact loaded source/spec files, declared Ruby/native paths
   and Bundler inputs with the recorded receipts. The incoming bootstrap lock
   is not those test bundles. Do not automatically rerun unaffected suites or
   relabel old successes as new-head runs. If one of those bindings changes,
   run only the corresponding existing suite under its declared environment.
   The two metadata evaluation receipts likewise remain scoped to their
   unchanged code/locked inputs. No `bundle update`, `make gems` or local
   bootstrap-package build belongs to this refresh.
5. Give the retained reviewer the old/new exact ranges, paired lock change,
   recipe/source-gem consumer assessment, equivalence and tuple/receipt results.
   Assess this packaged-input interaction and complete two-commit
   history/no-migration lineage; reuse `osvm-boot-evidence-review.md` and prior
   reviews for unchanged feature code. Then A/lead may publish through the
   ordinary reviewed path and require full **exact-final-head** native plus
   all nine lifecycle rows and semantic/boot/recovery witnesses. Retain the
   old unclassified cgv1 failure; old-head CI is not new-head evidence.

No new diagnostic source or generic check framework is authorized by this
addendum. The current runner/guest source-version contract and once-captured
module SHA/sites checks remain unchanged. Conditional integration approval
still depends on patch equivalence and complete final-head CI; this go decision
authorizes no merge, deployment or lifecycle action.

## One native boot diagnostic before replacement CI

**Current status: local debug stopped; lead selected D's four-file OSVM logging
fallback below.** The
[complete preflight](native-lineage.md#complete-cache-preflight-material-guest-image-builds-required)
and [D's summary](package-d-result.md) record successful normal instantiation
and standard-cache query, with 55 planned builds including material image
derivations `5dni4...`/`kfndpk...`, two OS systems and Ruby outputs. There was
no kernel/old-Nix build in that list, but it did not provide a warm full
closure. This is configured-cache evidence, not exhaustive remote absence or
an outage. No local realization/copy/build/VM occurred; the old5235 detached
checkout remains retained. No further debug/cache attempt is released.

D completed the selected observational implementation and quick checks. A
committed it as `dc74bcdadef75f181934bad2178afb589c34644c`; the
[final affected review](osvm-boot-evidence-review.md) passed. Reviewed ad899 and
its sixteen feature blobs are unchanged. A now owns the later 2951 baseline
refresh/check package, still pending here, and retains serialized
Git/commit/publication ownership. The architect launches nothing. The
[design decision](design.md#native-early-boot-failure-bounded-next-verification)
and [D's evidence](native-lineage.md#updated-image-native-run-41811208607-boot-readiness-failure)
bind the unresolved three-script before-hook failure to one old5235 cgv1.
The old image/device cases now pass for their observed inputs; they and this
new failure must not be conflated.

Stopped original debug recipe, retained as history and rationale:

1. Preserve reviewed `ad8991fe...`. A supplies an owned checkout/source at
   exact `5235bfd57c92bc05a25946937fe77f9803fe1c93`; do not substitute the new
   source-identity baseline. D uses the recorded ordinary CI configuration,
   `tests/test-configs/ci.nix`, the exact cgv1 script and a fresh session-owned
   test state directory. Preparation may include both configured machines
   even though only cgv1 will start. Preflight the actual unstable-6.18.49
   kernel/initrd/system/runner closure with cache-only policy. Stop on cold
   kernel, old Nix or other heavy material builds; no retries or bypasses.
2. Enter the existing `test-runner debug kernel/vpsadminos#cpu-view-cgroups-v1`
   route with that test configuration/state path. `Command#debug` and
   `TestEvaluator#interactive` already retain prepared `config.json` and a Pry
   context. Start only `cgv1.start(wait_for_boot: false)`; do not run the full
   CPU test, `start_all`, or the three repeated 1200-second hooks.
3. Before waiting, record safe prepared inputs and the actual owned process.
   `name`, `start_kernel_params`, `running?`, `can_execute?`, `start` and
   `wait_for_boot` are public. PID/config readers are protected; use prepared
   `config.json` and narrowly read-only Pry inspection of `@qemu_pid`, not a
   new public API. Bind PID to this runner's child, executable and `/proc`
   start time; reject a disappeared/reused PID. Parse selected actual argv
   fields in memory and emit only validated input paths, CPU/memory settings
   and approved boot parameters. Hash kernel/initrd/config without printing
   raw config, argv, environment or unknown extra-option values.
4. Perform one separate `cgv1.wait_for_boot(timeout: 1200)`, retaining any
   original exception in the receipt. Capture the same finite host state at
   return/timeout before exiting Pry: process state, elapsed CPU counters,
   thread count/RSS and at most 32 owned task state/wait-channel records, with
   a short collection deadline (at most 10 seconds). File disappearance or
   denied access is evidence unavailability, not a replacement exception.
   Do not infer guest PC, kernel progress or host pressure from these alone.
5. Preserve normal console/shell/machine logs plus the redacted identity
   receipt, then leave through existing runner teardown. D reconciles owned
   runner/QEMU effects and reports once. Do not repeat a green or red attempt.
   Boot success is only readiness for this newly recorded input tuple. It
   neither proves historical input equality nor clears the old failure by
   calling it flaky. The lead chooses the next action from this evidence.

The actual preflight met the material-build stop condition. The lead selected
the following finite, D-owned shell-independent evidence package before the
next full CI:

| File boundary | Required behavior |
| --- | --- |
| `osvm/lib/osvm/machine.rb` | Reuse the actual spawn inputs/PID for a small allowlisted launch record; on `wait_for_boot` failure collect bounded nonshell host facts through nonpublic helpers, then re-raise the original exception. |
| `osvm/lib/osvm/machine_log.rb` | Add fixed launch/boot-wait-failure events to the existing per-machine log; no arbitrary config/argv/environment dump. |
| `osvm/spec/osvm/machine_spec.rb`, `osvm/spec/osvm/machine_log_spec.rb` | Cover safe identity fields and omission/redaction, missing/reused/exited PID, bounded task count, collection errors preserving the same exception, and unchanged spawn/reaper/rollback/teardown behavior. |

This captures the missing evidence before the existing
`tests/runner/extensions/vpsadminos_logs.rb` `can_execute?` guard without a new
runner API or guest-shell dependency. Do not edit that hook merely to run its
guest script against an unavailable shell. Avoid expensive hashing inside the
spawn critical section, unbounded host commands or diagnostic exceptions that
roll back a successfully started VM. Keep original deadlines and recovery.
No QMP/monitor, vCPU-register engine, disassembler, guest kernel/config change
or new mode is included. If this finite boundary cannot supply the needed
facts, return the named limitation to the lead rather than expanding it.

The observation change's quick specs/hooks, A's separate purpose commit dc74
and affected independent review are complete. Preserve the reviewed feature
patch through the pending baseline refresh and checks before publication and exact-final-head
full native plus all nine lifecycle rows and witnesses. A later green run is
acceptance for its own recorded inputs, not a retrospective explanation of
run `41811208607`.

## Old aged-v5 liveness verification disposition

Historical disposition: the lead accepted the architect's bounded finding and
**GO for the already launched exact-e175 full CI `41865572140`**, then owned
by the root's sole `ci_e175_final` watcher. That run is now canonically
completed/cancelled after the later native failure and user steering; the
[current status](#current-diagnostic-status-and-user-decisions) supersedes
continuation of that run. The architect has performed no CI action or
fresh test. [C's old-attempt receipt](package-c-old-aged-v5-triage.md) and
the [source-grounded design rationale](design.md#old-aged-v5-loader-liveness-failure-and-current-run-disposition)
remain separate from any new result. This historical finding itself released
no retry, cancellation, dispatch or source change.

The old5235 aged-v5 failure is cumulative kernel-health rejection after a
loader/SMP-call stall; it predates superseded-run cancellation. Transition
completion/callback counts do not satisfy health. Exact module/sites/frozen
SDK identities remain reusable only within their proven scope. Baseline
package/source-identity changes prevent whole-input equality, and neither
those changes nor OSVM boot-wait logging demonstrates a loader fix.

1. The original disposition required the watcher/root to accept or reject
   that run under full native plus all nine lifecycle/witness gates, including
   actual captured identities, profile/age/boot/predecessors and recovery.
   Preserve original health exceptions and first-fault/console evidence.
2. A green result at the final full profile can qualify its exact head;
   do not relabel old5235 as passed, flaky, resource-caused or explained.
   There is no new product gate requiring explanation of every historical
   fault. The lead retains final semantic/identity/recovery and complete
   history/current-target acceptance under the user's conditional approval.
3. **Only an analogous current-head failure triggers the next diagnostic
   package**, with one implementer selected by the lead. First retain its
   original result and compare its actual input/first-fault records. No
   automatic additional job or expensive repeat follows.
4. That package's missing facts are narrowly defined: loader CSD
   queue/target/function/entry/exit progress, correlated to the caller and
   first-fault time; and aligned owned-QEMU/vCPU scheduling/run-queue-delay
   observations. Existing all-CPU NMI stacks stay enabled. Reuse the fixed
   `csd_queue_cpu`/`csd_function_entry`/`csd_function_exit` event contract and
   existing qualification tracing/host identity facilities where applicable;
   the current CSD collection covers later cgroup migration, not activation.
   A later ring tail or recovered guest snapshot must not be represented as
   first-fault evidence. Collection bounds, dropped/unavailable evidence and
   clock/identity association must be explicit.

There is no application implementation package to release now. If the trigger
occurs, the owner returns the smallest concrete diagnostic-only file boundary
before changes or another long check; the facts above are its finite question,
not permission to build a new engine. Preserve callback accounting, workload,
watchdog policy, 1800-second activation ceiling, health assertions, original
exceptions and teardown/recovery. No QMP framework, new kernel/probe resolver,
input pin, production change or broader audit is part of this decision.

## Exact-e175 shutdown unit reproduction

**Completed diagnosis scope, retained as history:** D owned a bounded
test prototype only. The
architect's [source finding](design.md#exact-e175-native-shutdown-failure-bounded-reproduction)
and [D's runtime evidence](native-lineage.md#exact-e175-native-run-41865572140-shutdown-failure)
are separate. Current native cleanup is a real failed required check. No
production behavior change, Git operation, VM or CI retry is part of this
package. The lead has subsequently released only the bounded ordinary
declared-environment preparation described below.

**File boundary:** extend the existing
`osctld/spec/osctld/commands/heavy_system_spec.rb` for the contention scenario;
use `osctld/spec/osctld/daemon_spec.rb` only for the setup/import/resume ordering
test if needed. The existing `manipulable_spec.rb` is a control, not a reason
to change lock behavior. No application file or generic test framework changes.
Retain existing ordinary tests. Add a separate context that avoids the old
`lockable` fake, which always succeeds, and the existing unconditional
`Pool::Export.run` success stub.

**Finite scenario and expected red:**

1. Use the real `Manipulable::ManipulationLock`, `Self::Shutdown#execute`/
   `grab_pools`, `Commands::Base` nested command behavior and pool-export
   lock/database-removal path. Stub only unrelated external work (ZFS/LXC,
   hooks, empty ancillary registries), not lock acquisition, same-thread
   ownership, pool-list cloning/removal or command completion. A faithful
   fixture pool must include the actual `Manipulable` module.
2. With queues/barriers, hold the real pool lock as import would. Start a
   client-side shutdown, prove it has taken a list containing tank and seen
   the import holder, and stop it at a controlled retry boundary. Release
   import; let the other thread execute shutdown and finish export/removal.
   Keep that winning thread alive behind a barrier, modeling setup's later
   server join. Do not depend on scheduler luck, sleeps or repeated stress.
3. Resume the losing command. Assert the pool is absent from the live DB,
   its retained object is still locked by the winning command, and the loser
   again receives `ResourceLocked` with the real `self_shutdown` holder.
   The desired contract is completion after the other shutdown completed;
   current code is expected to fail that assertion at a bounded checkpoint,
   not after 900 seconds. Record both command/thread identities and each
   ordered checkpoint in the local test receipt.
4. Use a finite join/queue deadline (at most five seconds per wait) only as
   a test-harness safeguard. On every exit, release all fixture barriers and
   use the modeled abort path to let the loser leave its loop; join owned
   threads. Do not asynchronously interrupt a lock holder or leave threads
   alive. Verify single-shutdown completion and existing same-thread re-entry
   controls pass, so a fixture failure cannot masquerade as the defect.

The optional daemon-spec case establishes only that serving begins before
import and a marker after import can invoke a second shutdown. It must not
assert that the historical guest restarted or followed that ordering. If real
export releases the lock, the second command refreshes its list, or production
ordering prevents the overlap, report that falsification and stop. Do not
manufacture the expected red by replacing those behaviors with stubs.

**Declared quick environment and command:** use the repository-declared
osctld development/test environment (`.#osctld`), with its
actual Ruby/Bundler, osctld Gemfile/lock, bundle path, `NETLINKRB_PATH` and
`RUBY_LXC_PATH` recorded. The initial existing-environment probe hit the
previous cache-only stop condition. The lead then authorized ordinary
declared `.#osctld` preparation through a fresh watcher with a five-minute
budget. Stop on kernel, old-Nix or guest builds, missing inputs beyond that
budget or any broader environment project. Do not substitute the test-runner
bundle, update dependency declarations or repair runner trust. From the
repository's `osctld/` directory, the finite command is:

```sh
bundle exec rspec spec/osctld/commands/heavy_system_spec.rb \
  spec/osctld/daemon_spec.rb spec/osctld/manipulable_spec.rb
```

First run the new named example and its immediate controls using RSpec's
existing `--example` selector, then this focused file set only if useful to
separate the expected regression from collateral fixture failures. Retain the
intentional red command/output as diagnosis; do not mark it passed or commit
a failing suite as a finished fix. Use the monitor policy if an operation is
uncertain/long; only the bounded preparation above is released, with no
kernel build or broader environment project.

**Return once:** exact source/bundle bindings, prototype diff, ordered
interleaving, expected failure versus controls, thread reconciliation, and
whether the model is confirmed or falsified. Confirmation establishes a
source-level concurrency defect only. It does not identify the failed VM's
actual owner, restart sequence or export progress. No new diagnostic
instrumentation or long check followed automatically. The confirmed proof
led to the separately proposed and now user-accepted correction below, with
explicit abort, restart-marker, exception/lock-lifetime and duplicate-request
semantics. Final exact-head native/nine-row and
recovery acceptance remains unchanged and currently unsatisfied.

## Accepted shutdown fix: acceptance and scope

**User accepted; implemented, reviewed and published at 645927.**
The user answered **“Fix here as a separate commit (Recommended)”** to the
current-chat `request_user_input_async` call
`call_7ccafe3d4e8749109837706d8a32a8c7`. That question covered this production
shutdown correction, coalesced requests, preserved abort/errors/export hooks
and full CI. The lead released the complete package below. The
[accepted design](design.md#accepted-production-shutdown-coordination)
requires one active shutdown per daemon, overlapping callers join
its result, and command-owned locks end with that operation. Existing unit
proof establishes the source defect, not the historical VM's actual interleaving.
Current native cleanup remains a required failed check, not an aged-test issue.

| Active owner/file boundary | Concrete work |
| --- | --- |
| D: `osctld/lib/osctld/daemon.rb` | Private per-instance shutdown mutex/condition/current completion record; internal `run_shutdown` owner/join path; existing begin/abort/confirm marker operations coordinated with completion. No wire API or new option. |
| D: `osctld/lib/osctld/commands/self/shutdown.rb` | Enter coordination before snapshots; retain the body in a protected helper; record each owned acquisition and release still-owned holds on all exits before the result is published. |
| D: existing `heavy_system_spec.rb`, `daemon_spec.rb`; `manipulable_spec.rb` as control | Replace the intentional-red test's old concurrent-owner ordering with the new admission/completion contract; add the finite behavior controls below. Keep original failing logs as proof. |
| A/root | Prepare the separate production-purpose commit and focused-CI route; serialize Git/publication and obtain required committed affected review before runtime acceptance. Keep C's frozen diagnostic-age delta separate. |

Do not preserve the old reproduction's barrier that requires the second
shutdown to export while the first is waiting on import: the new gate must
prevent that state. New barrier tests start one owner and one joined caller;
release import and the owner's export tail explicitly, then require both to
finish. Use real manipulation locks and command/export paths, with only
external work isolated as in the reproduction. No timing races or long sleeps.

Required quick controls:

1. Both arrival orders (setup owner/client joiner and client owner/setup
   joiner), plus ordinary duplicate clients: one pool snapshot/export sequence,
   no completion of the joiner before the owner finishes post-removal
   `SendReceive.deploy` and post-export hooks, both successful afterward.
2. Pause/fail the real export tail after database removal: absence from the
   DB is not completion. No premature confirmation or successful joiner;
   the initiating failure reaches all callers, held resources and the gate
   are released, and ordinary non-abort failure preserves pending marker intent.
3. Abort while the owner waits for import or after partial acquisition:
   abort remains responsive, releases owner-held resources, removes the marker
   and fails all joined requests. A duplicate must not reset the abort flag
   or recreate confirmation. Cover abort during the final export tail and
   the completion/abort ordering at the gate. A later fresh request can start.
4. Owner success/exception/abort with its thread kept alive: no retained
   command-owned lock; nested re-entry remains safe; already released and
   differently owned holds are not unlocked; a cleanup failure does not
   replace the original error. Include exceptions during partial acquisition.
5. Existing pending/confirmed marker modes, empty-pool success and restart
   resume remain valid. Waiters observe their original operation's outcome
   even if a subsequent request starts before they wake. No persisted
   synchronization state or migration is introduced.

Use the same declared environment and focused three-file command in the unit
brief, followed by affected formatting/hooks and independent committed review.
The expected-red prototype must become a genuine green contract test; do not
delete its regression coverage or count its historical red as a passing suite.

The one focused dispatch `41913307185` is now active; the following remains
its acceptance contract, not permission for a second launch. The first VM
acceptance is **one
focused `./test-runner.sh test osctl/ct-passwd` run including real graceful
shutdown**, from the repository root with its declared cache policy. Accept only a
completed body, stage-3 shutdown and QEMU exit before the existing stop timeout,
without cleanup TERM supplying the apparent success. Preserve launch input
identity, shell/console/runner/machine logs and the original exception on
failure. Stop and inspect a failure; no blind repeat or timeout increase.
Use a fresh watcher, and stop unexpected kernel, old-Nix or unrelated guest
builds under the existing policy. Runner updates remain operator-owned; do
not turn this package into runner activation, trust repair or prebuild work.

That focused pass is not whole-head acceptance or historical incident proof.
Proceed through the conditional 300-second diagnostic cycle below while
diagnosis remains unresolved. Only after diagnostic problems are settled,
restore 14400 seconds before final exact-head full native plus all nine lifecycle
rows, including the restored four-hour qualification and all
health/identity/recovery requirements. The user approval releases this
production fix and its quick-check package; it does not change existing
conditional merge gates or authorize deployment or runner-infrastructure
work. A/root own the later focused-CI route. Historical incident attribution
remains unknown, without a new generic historical-root-cause gate.

## Conditional diagnostic head and final verification package

### Current final-F native blocker packages

**COMPLETE design; HOLD native acceptance and integration.** The full
[native audit](native-lineage.md#current-final-f-native-audit),
[shipping review](final-shipping-review.md) and
[source assessment](design.md#current-final-f-native-blockers) bind F
`56b9363db1f1039e5d684dadc260cdffe7497e08`, d2fe and lock67487674.
Readiness/review is not runtime success. Preserve the terminal F run's
immutable artifacts and all retained refs; no cancellation, retry,
publication, implementation or external operation is authorized by this brief.

N has a sufficient test-file brief; M's source prerequisite is complete but
its proposed observation wrapper is held as insufficient. Root owns further
allocation and later Git/hook sequencing; architect owns these docs only.
A is the audit/identity clarification peer,
B supplies existing Intel comparison facts, C/D retain their own row scopes.
They receive no new investigation from this document.

**N: success-required NFS control protocol — implemented/reviewed, runtime held.**

The following source/check brief was executed as exact N74297e, parent F;
[accepted review](native-nfs-protocol-review.md) has no findings. The later
[H correction package](#current-h-provider-correction-package) now
controls the next N action; the source instructions below do not allocate
another implementation or permit a direct full-CI push.

- Sole application path: `tests/suite/osctl/nfs-cancellation-common.nix`.
  Replace the direct positive `shutdown_tree` echo in the mount-race example
  with the finite writer described in design. Do not change the kernel patch,
  daemon, production package/pin, workflow, NFS options, network outage or
  negative permission/value assertions. The same example serves default and
  native110 across all declared NFS versions; preserve baseline selection.
- Historical provider assumption corrected by H: ruby_vpsadminos is the
  osctld runtime but is absent from this test-function package set. The
  [current package](#current-h-provider-correction-package) supersedes only
  its interpolation and availability proof. File/Errno/monotonic need no gem, and
  the current host-side nsenter/unshare/sysfs route supplies the same authority
  and namespace. Use inline code with normal escaping, not a new utility or
  guest package. Retain the original machine command timeout;30s bounds
  retries of returned EBUSY, not a claim to interrupt blocked writes.
- Only EBUSY from opening/syswriting this same control is retryable. Check the
  monotonic budget before another attempt; sleep at most50ms and no longer
  than time remaining. Use `File#syswrite` and require the full two-byte
  `1\n` write, close and readback1. Close/readback errors do not retry a write.
  A permanent EBUSY, any other errno, partial write, false/malformed readback,
  command failure or cancellation remains a failed example. Preserve the
  errno/count/elapsed outcome, original ensure rule removal and every later
  mount/isolation/stopped/restart/data assertion. No fresh namespace per retry,
  generic shell `until`, `machine.succeeds_with_retries`, fallback control or
  EBUSY-as-pass assertion.
- Quick proof: parse/format Nix and parse/lint the exact embedded Ruby using
  the already declared cached project environment. Exercise that actual writer
  with immediate success, EBUSY then success, perpetual EBUSY/deadline, EPERM
  and ENOENT immediate failure, partial write and bad readback. Check no attempt
  starts after budget expiry and that an interrupted operation propagates.
  These are caller controls, not a simulated kernel. Reuse the existing
  daemon spec's transient/permanent-busy evidence for its unchanged scope;
  no daemon suite/environment restoration or kernel build is needed.
- After normal commit and affected independent review, root may separately
  release the existing default/native110 NFS cases as an affected batch.
  Acceptance requires actual write success/readback1 plus all65 examples,
  existing payload/isolation/restart/health and VM recovery for the selected
  input. A retry count is evidence, not a causal lock-holder diagnosis.
  Failure/exhaustion/inactive control stops for a named assessment, not another
  run, longer deadline, new probe or kernel remedy. Exact-F failure stays in
  its audit even if the corrected caller later passes.

**M: exact attach source COMPLETE; target-fd evidence capability STOP.**

- Actual failed input is cgv2,6.18.49,8CPU/8192MiB and F system. F's source
  selects LXC6.0.6 pin267e7844; no independent guest LXC-byte query was made.
  Do not target generic6.12.113 or copy NFS's `.95.7` identity.
  [D's completed retained-log prerequisite](package-d-result.md#current-m--retained-mknod-attachment-evidence-prerequisite)
  supplies an empty destroyed log, RUNNING before execution and exit after
  cleanup, without a numeric init/attach target. Wrapper3394/userns3455 are
  not proven targets. Do not repeat that extraction or treat the later exit
  as the cause of the preceding failure.
- Root corrected its acquisition grant to recipe-authoritative vpsfreecz/lxc,
  exact267e7844 and source hashvBj6P6301thjQVkjSnDQ6SPiFnl+4Uxrc3DQeBQkGwA=.
  Exactly three single bounded raw requests (attach.c, directly referenced
  commands.c and syscall_wrappers.h) returned200. Exact URIs, sizes and
  per-file SHA256 are in the [design receipt](design.md#current-final-f-native-blockers)
  and files in existing `package-d-mknod-retained-evidence/`. They do not
  prove the full source NAR hash or realized guest package; no other source,
  clone, checkout, provider/input change, build or runtime was performed.
- Source maps711 to the actual `setns` of the monitor-supplied init pidfd,
  using the requested/inherited namespace mask.1695 is its transient-child
  failure path before the payload clone1714. Earlier fdinfo-PID decoding,
  proc opening, signal0 and accepted support probe do not establish target
  liveness at that later call. Exact PID/fd/mask/kernel ESRCH branch remain
  unproved. There is no justified kernel/LXC/exec behavior correction.
- The existing local lxc-attach argv/options expose no log-level/output
  route in this test call. Even TRACE's inspected messages lack the received
  fd plus decoded PID at the failing call: namespace-choice names and
  transient-worker IDs are different facts. The optional PID message in
  `do_attach` is after the failed phase; terminal log_fd is not this record.
  Consequently neither a verbosity-only change nor separate `osctl` init
  snapshots meets the target-fd evidence requirement. **Do not implement the
  previous misc.nix snapshot wrapper or run it as a purported remedy.**
- Minimal next prerequisite is a supported way to obtain one directly bound
  attach-call record: container/path, transient identity, actual pidfd and
  decoded target identity, namespace mask, syscall result/saved errno and
  contemporaneous target lifetime. That capability is unavailable through
  the inspected current test/logging route. Root must select any separately
  scoped attach-local mechanism before design/implementation; this brief
  does not add a probe, tracing framework, daemon/kernel/provider change or
  source edit. No further fetch or optional source audit is required here.
- Source inspection/line mapping and request digest accounting complete this
  prerequisite; no executable check/test was run. Any later accepted evidence
  mechanism must preserve single execution, original errors/cancellation,
  both random device examples, six script jobs, exact guest, health and
  cleanup, with finite output and identity-loss reporting. Its actual
  implementation/check/review and one-run scope must be specified then,
  without weakening ESRCH or forcing fallback. A non-recurrence does not
  waive F. There is no automatic observation implementation or run release.

Both scopes preserve user authority: current-module tests and the separately
approved shutdown fix do not authorize a new production kernel/daemon/provider
remedy. If M's evidence points to one, return a concrete proposal to root for
the user decision. N's protocol correction is a test contract adjustment;
root must accept it before edits. This does not depend on explaining every
historical failure or reopen the retired collectors.

Each later implementation owner supplies exact old/new range, changed purpose,
provider/source bindings, quick-check results and remaining runtime limits.
Keep tested F and all old evidence; use normal PRIMARY Bundler/hooks and the
patch-series ownership policy, with A/root selecting history disposition.
Do not hide an independent baseline test repair inside shutdown coordination
or the current-module resolver. All intended changes must be committed and
affected independent review completed before any separately released run;
new findings stop there. Root retains final exact-head native+ALL9/original14400,
then-current target/input assessment and ordinary conditional staging merge.
No six-image exception covers either failure; those six and latest-device
scripts actually passed F. No weakened health/deadline/stress/recovery gate,
automatic whole-matrix repeat, node setting or lifecycle action is included.

### Current H provider correction package

**COMPLETE sufficient implementation/check brief for root allocation to A;
no execution release.** The [source/evidence assessment](design.md#current-h-prebuild-failure-and-provider-correction)
binds terminal Hc916a804/run42176307860 attempt1 to the exact missing-attribute
error during two-test prebuild. Metadata selection succeeded; no selected
guest, writer or NFS example ran. The existing build and host runner execution
are not guest/provider success. All read/collection clients are terminal.

1. **Guard, preserve and change one interpolation.** In the existing owned
   N/H checkout, A's later complete package must first bind clean Hc916a804,
   retained marker-free N74297e, common parent F56b9363, treec2899100,
   lock67487674, exact old source SHA2beb7a72 and writer SHAc17bc4c3.
   Preserve all old refs, failed-run artifacts and accepted reviews before
   any amendment. Only application path is
   `tests/suite/osctl/nfs-cancellation-common.nix`; replace
   `${pkgs.ruby_vpsadminos}/bin/ruby` with `${pkgs.ruby}/bin/ruby` at853.
   No changes to the38-line writer, other source, package overlays, guest
   package list, workflow, lock, profiles, deadlines or recovery. This uses
   the existing standard Ruby package, not an ambient executable or new
   dependency/provider project. Unexpected source/input difference stops.
2. **Prove the real package context before freeze.** Use one finite cached,
   offline, evaluation-only check through the candidate's existing
   `flake.lib.testFramework.makeTestLib` and `makeSingleTest`, as used by
   `test-runner/nix/evaluate-tests.nix`'s direct-test path. Bind source and
   lock, `x86_64-linux`, the flake's locked `nixpkgsPath`, actual
   `tests/test-configs/ci.nix`, `configuration=null`, and empty test arguments.
   For each of `osctl/nfs-cancellation` and
   `osctl/nfs-cancellation-native110`, force exactly
   `(testLib.makeSingleTest { test = path; args = {}; }).value.test.config.testScripts.default.script`.
   This uses the actual suite, make-test overlays and Nix interpolation;
   metadata-only `testMeta`, Nix parse, mock `pkgs` or a substituted Ruby
   token do not meet it. Save the rendered strings/provider path and result.
   Disable import-from-derivation and lock writes; do not force `test.json`,
   `testBatch`, image/toplevel/closure builds or run `test-runner ls`.
   This is a compact check expression in existing evidence, not a new
   repository check harness/API.
3. **Bind the declared provider without assuming guest equality.** Evaluate
   ordinary `ruby.outPath` in the outer test import and the repository's
   existing OS overlay set from the same locked nixpkgs/source inputs;
   require the rendered command's Ruby path to match that declared provider.
   Retain the source proof that guest defaults install ordinary `ruby` and
   neither selected test overrides that declaration. A package-path match
   is not whole-closure equality or evidence that a VM executed it. Do not
   add the missing ruby_vpsadminos overlay merely to satisfy the test.
   If cached inputs cannot evaluate, package paths differ, or the declared
   executable is unavailable for the bounded controls, stop with the exact
   missing input/path and proof limit. No realization, fetch, bootstrap,
   guessed store path, global overlay or provider fallback is part of this
   quick package. Root resolves that named prerequisite, not another run.
4. **Close the missed check with the actual writer and call site.** Retain
   the old20 controls as historical evidence; rerun that existing finite
   suite with the newly evaluated, already-realized declared interpreter.
   Extract the writer from the candidate and require unchanged38-line bytes.
   Check the rendered full Ruby scripts and existing nested Shellwords/Bash
   assembly with their real provider path, requiring decoded `-e` payload
   equality. Cover existing immediate/transient/permanent EBUSY, nonbusy
   errno, partial write, close/readback errors, deadline/sleep cap and SIGINT
   controls; no new kernel model. Apply declared cached Nix parse/formatter,
   Ruby parse/RuboCop, whitespace and ordinary commit hooks. Preserve the
   exact outside-interpolation source comparison, workflow/lock/profile
   bytes and both consumers' selection. No broad daemon suite, guest/kernel
   build or unrelated feature rerun. A failed quick check is a stop.
5. **Fold into the same fourth purpose, then affected review.** A owns the
   later normal PRIMARY-bound Bundler/hook/message-file amendment after
   preserving exact oldN/H backups. Produce marker-free N-prime with parent
   F; preserve the first three objects/messages and N's authorship, update
   the owner's truthful version/development history under patch policy.
   Do not leave a fifth repair/WIP commit or merge/revert H. Record exact
   old/new bases/heads, complete ranges, one-line intentional delta,
   writer equivalence, inputs/tools/checks, no migrations and no repeated
   input stream. The previous provider-availability claim is superseded;
   the old review records remain intact. Root invokes the same eligible
   reviewer, retained settings, for affected ALL4/HIGH provider/consumer/
   checks/history review after the final source is committed and quick
   checks pass, reusing unchanged F/protocol review where justified. This
   was a newly discovered defect, not a prior review's requested narrow fix;
   do not treat it as step9 rubber-stamping. New findings stop publication.

**Separate later publication/runtime boundary.** After root accepts that
package/review, A may prepare a new source-identical skip-message sibling
under the retained [focused route](#reviewed-n-focused-preparation-package),
with exact absent/expected-old guards preserving failed H and old N. Record
the new source/provider revision; it cannot inherit H/F paths or closures.
No workflow/source selector change, direct marker-free push that starts full
CI, or automatic rerun of42176307860. Root owns a separately released guarded
publication, terminal ref proof, actual no-duplicate event reconciliation,
and ONE existing focused dispatch after command ownership is released.

The unchanged focused inputs must yield exactly default/native110,65 examples
each, all four real writer success/full-write/close/barrier outcomes per
consumer, their actual declared Ruby execution and guest/source/kernel
identity, all integrity/state/health/recovery checks and graceful teardown.
Baseline's unchanged four controls remain outside this selection. Capture
tuple/guest module-site SHA remains unavailable in this focused workflow;
normal production artifact metadata is not a guest measurement. Use actual
job cardinality rather than inventing nine skipped jobs. Any new evaluation,
provider, NFS or cleanup failure stops for named assessment, without another
launch, permissive errno assertion or budget increase. H supplies no NFS
qualification; both F native failures and final then-current-target/exact
FINAL native+ALL9/original14400/conditional merge gates remain unwaived.
Pending LXC scope only governs extra LXC diagnostics. Session stays OPEN.

### Reviewed N focused preparation package

**Retained accepted route, already executed for failed H.** The current
provider correction above is prerequisite to a successor; this section is
not authorization to repeat H. Its historical source hashes and check-reuse
claims apply to the original message-only N-to-H package.
The [design](design.md#reviewed-n-affected-runtime-and-delivery-route) resolves
the existing selector, skipped capture/lifecycle behavior, baseline exclusion,
identity limits and acceptance. Root allocates one complete package to A after
capacity confirmation; no assignment is sent by architect. A owns the short
checkout/ref/index/message/hook window and reconciles/releases it before review
or waits. N's test source remains frozen. No new tool, collector, workflow,
runtime provider, registration or cleanup is part of preparation.

1. **Guard retained bindings before any mutation.** Require primary exact
   F56b9363db1f1039e5d684dadc260cdffe7497e08 and marker-free candidate branch
   `2026-11-03-livepatch-fixture-failures-native-nfs-protocol` at exact
   N74297e22953f5f3186d7fcdcfe304eba10fb84f7, parent F. Preserve that N ref
   as the reviewed delivery candidate; all14 prior provenance refs, tested
   heads, detached5235 and retained source roots stay intact. Verify clean
   source/index and ownership before reusing the existing unregistered N
   checkout. Do not move primary or overwrite N. Guard a proposed temporary
   branch `2026-11-03-livepatch-fixture-failures-nfs-focused` absent, or exact
   previously reconciled H if resuming this package; any other value stops.
   Preparation needs no network or source re-evaluation. Root's later
   publication must perform its own fresh remote/ref checks.
2. **Create only the message sibling.** In A's owned checkout, create the
   temporary branch from exact N and perform a normal message-file amend
   adding one isolated `[skip ci]` paragraph. Preserve the original author,
   subject and all other N message bytes. Use the established absolute
   PRIMARY Ruby/Gemfile/ignored-lock/.gems/Bundler binding and mandatory
   hooks; ordinary signature setup is allowed only within A's separately
   released window. The shared bare signature key may change normally;
   reconcile/report it, never copy or bypass it. Result H is not guessed:
   it must retain parent F and tree
   `c2899100faba19cdd022229b60693f4cc88391ce`. N and H are siblings, not a
   new fifth source purpose. No source selector, age, tag, workflow/action,
   configuration or lock edit; no new worktree registration. A hook-induced
   source delta or unowned state is a stop, not permission to repair scope.
3. **Exact evidence and bounded quick proof.** Supply raw N/H commits,
   ordered d2fe..N and d2fe..H ranges, mode/blob/tree equality and identical
   binary F..N/F..H patches. Expected sole path remains
   `tests/suite/osctl/nfs-cancellation-common.nix`,+42/-2,blob0a15d61d,
   source SHA2beb7a72; stable patch ID
   `e0d9a10859dfa1d0dfb3dc93b00a9c6a5695d194`; diff SHAef9ddeac.
   Preserve full exact hashes from [A's packet](package-a-result.md#n-test-only-protocol-candidate-committed-for-affected-review),
   lock67487674 and first three exact objects/messages. Prove message delta
   only the isolated marker, plus expected committer/hash changes; record
   that H becomes a different provider revision despite tree equality.
   Retain normal hook outcomes and no-migration/no repeated-input-stream/
   no-obsolete-source conclusions. Temporary skip wording is intentional
   evidence-only history, not final-shipping eligibility.
4. **Reuse only unchanged checks and inspect the actual selector.** The
   accepted20 writer controls, exact38-line snippet SHA c17bc4c3, Nix/Ruby
   parse/format/lint and escaping results remain bound to the unchanged
   source/tools. Do not rerun that suite or build/evaluate guests merely for
   a message change. Normal hooks still run. A finite cached Ruby check may
   exercise the actual `TestScript#path_matches?`/`TagFilters` consumers with
   the two positive singleton paths, baseline non-ci tag and unrelated
   paths; require exactly two positive matches. Cross-check ordinary
   discovery, source tags, `-- "$TEST_PATTERN"`, lifecycle/capture guards,
   push filter and full workflow/profile byte equality. This is static
   selection proof, not a Nix listing or future runtime inventory. No
   `test-runner ls`, evaluation, compiler/module/ELF query, environment
   bootstrap or unrelated feature test is needed for this package.
5. **Reuse review with an explicit affected history conclusion.** Preserve
   reviewer0's accepted ALL4/HIGH84ca8bb8 review of d2fe..N and F shipping
   review. Submit H and the exact equivalence/message/trigger packet to the
   same eligible reviewer for only the affected publication/source-identity
   and complete-history boundary at retained HIGH risk, reusing unchanged
   implementation review. Keep the member's saved model/effort.
   Do not repeat the original feature audit or call tree equality a review
   certificate. The mandatory policy's installed certified-equivalence
   exception may replace this additional turn only if root actually supplies
   its required original reviewer/range/decision/migration receipt and
   independent reconstruction for H; no such certificate is presumed here.
   Any new substantive finding/source change requires its normal affected
   owner/check/review path. Complete preparation ends with exact H/ref,
   clean state, terminal command accounting and Git ownership released.

**Later root-only publication and one focused dispatch.** This is a separate
release, after original run42079730277 is terminal and all command ownership
is released. No overlap with that run, even though H suppresses push CI.
The pending LXC user scope question applies only to extra LXC diagnostics;
it is not a prerequisite for this N-specific route.

- Fresh canonical remote/ref and local identity guards bind primary F,
  retained exact N, reviewed H and the chosen temporary branch. The remote
  temporary ref must be absent for creation, or already exactly H for a
  reconciled resume. Do not overwrite an unexpected branch, publish N or
  push primary. Record then-current staging as context; target movement
  alone need not rewrite this deliberately F-anchored temporary experiment,
  while final shipping still requires then-current-target assessment.
- Publish only H with the appropriate absent/exact expected-old guard and
  normal hooks. The isolated skip paragraph prevents the automatic full
  push recipe; explicit workflow dispatch is independent of that marker.
  Release command ownership after terminal publication/ref proof. Reconcile
  actual branch/head/event runs once before dispatch. An unexpected push
  run, uncertainty or already queued/in-progress eligible H dispatch stops
  a second launch; root owns any necessary disposition, not automatic
  cancellation/retry. A terminal failed H attempt is not permission to repeat.
- Release **one existing workflow162100852** dispatch to that exact branch
  with these literal inputs:

  ```text
  test_suite=ci
  test_pattern=osctl/nfs-cancellation*
  test_tag=ci
  prebuild=true
  stop_on_failure=false
  proxy_lock_full_matrix=false
  zfs_tags=functional
  zfs_test_body=
  ```

  Bind the resulting head H, branch/run/attempt/event and actual input log;
  don't assume API submission alone launched that head. If the dispatch
  response is uncertain, reconcile the same request before any repeat. Only
  after the old sole watcher is terminal does root allocate a fresh policy
  watcher for this one run. No new observer/client/runtime is launched by
  this design or A preparation.

**Focused acceptance and exact limitations.** Normal build/prebuild must
finish; unexpected local kernel/provider construction is not a reason to
bootstrap an environment. The build's ordinary package upload remains, but
module/sites capture and all nine lifecycle rows must be skipped because
the pattern is nonempty. No aged14400/300 fixture or kernel/misc is selected.
Actual native inventory must be exactly default and native110, one script
and65 examples each, zero unexpected skips/retries, preserving4CPU/8192MiB/
10GiB disk and all existing runtime bounds. Require actual Ruby provider
execution, four successful race writer outcomes per consumer (including
full syswrite/close/exact barrier readback), all later admission/mount/
neighbor-payload/stop/restart/remount, idempotence/25-cycle/permission/data
checks, normal health monitoring, resource cleanup and graceful QEMU0.
Busy counts may be zero; they neither identify F's EBUSY cause nor waive a
failed attempt. Preserve original failure and recovery accounting.

Baseline is not in this focused selection: ordinary discovery lacks its
opt-in and `ci` excludes its sole `livepatch-amd` tag. Its **four**, unchanged
soft-error/absent-control/neighbor/recovery examples remain later main-AMD
coverage, not an unexecuted65-example pass or a new focused-run prerequisite.
No extra tag/API/opt-in is added to force it into this workflow.

Record runtime source/tree H, lock, actual build/provider/system/kernel/
initrd/squashfs/QEMU and Ruby executable, and both actual uname guards
(.95.7/default and .110/native). H changes captured source/provider revision;
same source tree does not establish identical closures. The focused capture
step is skipped, so module/sites tuple and per-row identity artifact are
unavailable by design. A production artifact digest remains package evidence;
the shared boot-service case does not separately hash the guest module/sites.
Do not invent this assertion, reuse F identities as actual H observations or
weaken the later full-workflow current-module/site capture contract.

Any failure, selection/identity mismatch, missing completion, provider error,
timeout or teardown gap yields one bounded audit and STOP. No blind rerun,
changed errno acceptance, larger budget, node setting or misc retry. A success
qualifies only these affected consumers on H and is not a final successor
qualification or retrospective F native pass.

**Return to delivery after root accepts the affected evidence.** Retain H
as diagnostic evidence outside shipping. Return to marker-free N (or its
explicitly assessed successor), with the NFS repair a separate fourth purpose;
no amend/revert/merge of the diagnostic message sibling is necessary. Root/A
then perform fresh target/input/old-new range/history and relevant quick/review
work, preserving all tested heads/messages and migration provenance. Any
substantive target conflict or new production behavior returns for scope;
do not transfer old derivations, whole closures or runtime by file equality.
After proper committed review and no-duplicate event reconciliation, require
actual exactFINAL native+ALL9/original14400 with full source/module/sites,
semantic/health/data/recovery acceptance. Root decides the timing of that
new final qualification; neither this plan nor LXC's pending scope silently
changes its gates. The user's conditional vpsadminos→staging integration is
still unsatisfied; neither F failure is covered by the historical image
exception. No merge, deployment, session lifecycle or cleanup action follows
from completing this brief.

### Accepted final preparation package

**Retained brief, executed through reviewed/published F and its current run.**
No further300s cycle is an invented prerequisite. Read the full
[ordinary acceptance](package-c-scheduler-hotplug-preparation.md#current-ordinary300-runtime-acceptance-audit)
and [ordinary review](ordinary-300s-review.md) for their exact scope: selected
case802898/run42057169147 passes current-module identity, 100000tasks/393.406s,
pre/post CPU127 health,21 callback counts after both phases, activation836.777s
and disable1178.274s below1800, two full migrations, all exits0/stopped/tasks1,
stress/resource cleanup, final health/completion and graceful QEMU0. Native
was skipped and the remaining final suite was not executed. Retain missing
raw-job/runner-version fields as unavailable; no re-download is needed.

**Satisfied target dependency.** [A's scoped preflight](package-a-final-target-preflight.json)
proved staging `d2fe1489f0b0b213fb247aeee6e081d349adaf42`, parent
`2951a632c4254a44747a8da326e3dde897eaa0e2`, and matching primary
`645927e22809a29c67ffd59c072e553e05e2a72b`, ordinary
`802898590a035a845981959df7dd0ba4b9103f95`, instrumented
`08e3d0f910d5cc7140e2eb532497218f52e94a16`. Git was released at
2026-11-05T17:10:30.910007Z. Complete incoming2951..d2fe is one commit,
only `flake.lock` +3/-3; d2fe..actual is empty. Architect read the retained
commit and consumers: only unstable revision/hash/time changes, affecting
unstable templates and generated stable/unstable guest locks. Stable nixpkgs
selection and all feature/kernel/runner/workflow source bytes are unchanged;
this is not derivation, package-tree or whole-guest equivalence. The
[design source assessment](design.md#conditional-post-focused-diagnostics-and-final-qualification)
establishes the bounded refresh rationale.

**One complete A package, no application redesign:**

1. **Preserve and refresh shipping lineage only.** Preserve an exact owned
   backup ref for tested645927 before rewriting; verify all existing
   diagnostic/provenance refs and source checkouts remain intact. In the
   session's primary feature, replay2951..645927 onto exactd2fe, keeping the
   three purpose boundaries: current-module semantic witnesses8169b818,
   OSVM boot evidencee1751c9, approved shutdown coordination645927. No
   age/observer/one-row/host-sampler/codec/debug-thread purpose enters the
   final ancestry, even by merge followed by revert. Primary already has
   original14400/comment absent and full native+9 workflow; verify those
   bytes rather than transplanting a diagnostic tree. A changed target,
   dirty/unowned state, conflict or substantive patch change stops for root.
2. **Finalize messages and hooks.** Remove only the isolated temporary
   `[skip ci]` paragraph from its owning production commit. Preserve the
   first three purposes, authorship and remaining truthful message content;
   a pure patch-equivalent transplant adds no semantic version claim.
   Use the established absolute PRIMARY Ruby/Gemfile/ignored-lock/.gems/
   Bundler hook binding, normal mandatory hooks and message-file workflow.
   No hook bypass, autostash/reset, environment bootstrap or source-only
   trigger edit. All intended content/messages must be committed. Let F
   denote the actual resulting head; do not guess it. A owns the short Git
   window and reconciles/releases it before checks/review waits and records.
3. **Supply complete lineage and input evidence.** Inventory old range
   2951..645927 versus new d2fe..F, all three ordered commits, complete final
   diff/modes, raw message differences, range-diff/patch IDs and intentional
   baseline lock delta. Prove feature blobs match except a specifically
   assessed conflict; none is expected from this nonoverlapping lock change.
   Record all retained tested/nonancestor diagnostic heads and exclude them
   from shipping. Retain explicit no-migration/no repeated-input-stream
   conclusions and existing shutdown approval. Record new source revision,
   lock digest and source/version propagation; do not transfer old closures,
   systems, module digests or old-head CI success by source-byte equality.
4. **Run only relevant quick checks.** After the final commit, use the
   existing cached declared environment for this changed-input check:

   ```sh
   nix eval --impure --json --option allow-import-from-derivation false \
     --file tests/nixos-container-templates-eval.nix
   ```

   It checks actual generated stable/unstable minimal/impermanence locks,
   revision propagation and module equivalence without building tarballs.
   Capture the existing ten-field IFD-disabled identity expression in
   [Baseline refresh check package](#baseline-refresh-check-package) exactly
   once on F, with `drvPath`/`outputPath` (not coercing `outPath`) fields:
   candidateProducer, candidateModule, corrected, resolver, siteChecks,
   candidateSites, boot, sdk, config, bootCompiler. Bind both receipts to F
   and its lock. Compare available retained tuple/source/control/tool/loaded
   bundle receipts before reusing prior Ruby/OSVM/resolver/SDK/module checks;
   no automatic suite rerun or old-head re-evaluation. A changed identity
   invalidates only its relevant reuse and requires a named explanation;
   old7c4d is not an allowlist. Do not hash unrealized paths or build speculative
   closures. Normal CI performs required fresh builds/cache publication.
   Finish normal formatter/lint/hooks/whitespace and source/history checks.
   Long or uncertain authorized checks use a fresh policy watcher; stop on
   missing prerequisites, unexpected local kernel/old-Nix/heavy compilation
   or failure rather than starting an environment project. No retired
   collector controls, additional300s run or whole unrelated suite is needed.
5. **Affected committed independent review.** Supply F, complete old/new
   ranges, input-consumer assessment, checks and raw message/lineage evidence
   for ALL4/HIGH review: general, architecture/repetition,
   scope/proportionality, risk/compatibility. Reuse prior reviews only for
   unchanged source/input scope; do not ask for a rubber stamp. Require an
   explicit whole-series/history/migration conclusion and preservation of
   original semantic/health/recovery gates, full workflow/original14400,
   source-version capture and absence of skip/WIP/diagnostic/revert residue.
   New findings stop publication until the owning affected fix/check/review
   path is complete; any material behavior change returns to root for scope.

**Later publication and qualification, only after separate root release.**
Recheck actual staging and primary/retained refs, reviewed F and clean source;
a target change returns for the relevant assessment/refresh/review. Publish
only the shipping feature with an exact expected-old-primary lease and normal
hooks; retain645927 and all diagnostic evidence. An unchanged-tree/message-only
push may not match path filters. Bind an actual eligible full exact-F run;
only if none exists after bounded no-duplicate reconciliation may root release
one existing workflow162100852 dispatch with `test_suite=ci`, empty
`test_pattern`, `test_tag=ci`, `prebuild=true`, `stop_on_failure=false`,
`proxy_lock_full_matrix=false`, `zfs_tags=functional`, empty `zfs_test_body`.
One fresh sole watcher; no automatic duplicate or blind retry.

Require the normal build to capture current producer/module/SHA/sites/source/
lock once and every dependent row/guest to verify that binding. Require
actual native and **ALL9** lifecycle/semantic rows, original scale-aged14400,
all profile/resource envelopes, frozen boot/predecessors, real FUSE/TCP/fragment
and other required witnesses, original deadlines, cumulative kernel health,
rollback/state/data integrity, stop/recovery and graceful teardown. A sites
JSON or the old ordinary pass is not execution of the other semantic cases.
Any new failure gets one named evidence assessment and its normal remedy;
no warning waiver, buffer/timeout growth or speculative kernel/node fix.

**Existing integration scope, not new authority:** user “all right, so when
the CI passes, you can merge it” conditionally covers vpsadminos→staging.
The separate “missing opensuse image is temporarily, ignore it” exception
covers only the six explicit Leap16.1 image-not-found scripts recorded in
[native-lineage.md](native-lineage.md), not all failures in those groups.
Keep every script scheduled. A latest-device-unit or other functional failure
is blocking and cannot inherit that exception; no new exception is granted.
Only after all required final outcomes under that exact scope and fresh
target/history/equivalence/hooks checks may root perform the ordinary approved
ff-only integration through its short merge claim and remote verification.
Read the selected coordination guide then; never hold a claim during checks,
review or CI. This preparation brief performs/releases no merge, deployment,
node setting, cleanup or session lifecycle action. Operator infrastructure
ownership and all earlier failure evidence remain unchanged.

### Retained intermediate diagnostic route

The following sequence is historical: its diagnostic dependency is satisfied
by root's accepted ordinary802898 case. It does not add another shortened
matrix or historical-root-cause gate before the current final preparation.

**Status: the diagnostic-head preparation/run steps are now executed through
bda1 / 41921632759; final-delivery steps remain conditional.** The original
release dependency was root acceptance of focused 41913307185. A owns history/checkout,
saved-patch application, quick checks, hooked commit, evidence and later
publication. C is the patch-identity clarification peer; architect owns this
brief. Root alone accepts the focused result, allocates the package and
releases any subsequent long run after committed review. Roster readiness
does not allocate work. Current feature/run and sole watcher stay untouched.

1. **Retain the production anchor.** Use exact accepted
   `645927e22809a29c67ffd59c072e553e05e2a72b`, base
   `2951a632c4254a44747a8da326e3dde897eaa0e2`, or a later explicitly accepted
   reviewed fix. Preserve its primary ref/worktree. Prepare an ordinary
   session-owned diagnostic ref/checkout, suggested name
   `2026-11-03-livepatch-fixture-failures-diagnostic-300s`, as retained test
   evidence, not an additional delivery registration. Verify ownership and
   absence/exact intended identity before creating/reusing it; never overwrite
   an unrelated ref. No lifecycle/unregister/delete operation or cleanup.
2. **Commit the finite diagnostic input.** Apply only saved patch
   `c46380fdc1f05abd76fd975e25321d40ee2e37a15fdbcdb59c1ff42810554dde`
   to `tests/suite/kernel/livepatch-qualification.nix`. Original source hash
   is `367dd4ce864b36c4807cb974857d7b58e22b18bb51343ad2724757132da12f2f`;
   diagnostic source hash is
   `2fb34cb01efc54b9ec0fa96af20805bbe49bb986c977e5ad86e0b374244411d3`.
   Any mismatch is a named input change for assessment, not permission to
   refresh the patch. Its only value change is
   `shapes.scale-aged.ageSeconds`: 14400 to 300, retaining 128 vCPUs,
   16384 MiB and 100000 tasks. The distinct `representative` profile stays
   8 vCPUs/8192 MiB/16384 tasks/age 0; other zero-age profiles and fresh
   retention settings remain unchanged. Preserve all other file content. Use the
   established cached formatter/Nix parse/whitespace/exact-diff checks and
   normal hooks; no kernel/guest rebuild is part of preparation. Commit a
   clearly temporary diagnostic change, without a new skip directive.
3. **Review before the long trigger.** Supply the committed diagnostic
   parent/head, sole changed path, quick results, saved patch and original
   production review to root for affected independent review. Reuse unchanged
   production/unit/ELF receipts only at their actual input scope; do not
   reopen unrelated implementation lanes. Record explicitly that this head
   is diagnostic and will not enter final feature ancestry. Do not publish
   before review/root release: ordinary push is a possible immediate CI launch.
4. **Run one existing full diagnostic matrix.** After accepted review and
   root release, A publishes only that diagnostic ref using the ordinary
   SSH/hook route and records exact remote proof. Bind an actual eligible
   full push run if present. If none exists, root may release one existing
   workflow `162100852` unfiltered dispatch after bounded no-duplicate
   reconciliation and fresh exact-ref guard. Inputs: `test_suite=ci`,
   `test_tag=ci`, empty `test_pattern`, `prebuild=true`,
   `stop_on_failure=false`, `proxy_lock_full_matrix=false`,
   `zfs_tags=functional`, empty `zfs_test_body`. Never dispatch a duplicate.
   The normal build captures producer/module/SHA/sites/source once and all
   dependent rows verify it. Require actual native selection and all nine
   lifecycle rows with unchanged health, witnesses, identity and recovery;
   label the `scale-aged` profile 300 seconds. One fresh sole watcher owns
   the run. A green is shorter diagnostic coverage, not four-hour acceptance.
5. **Resolve current diagnostic outcomes.** Root accepts the results and
   determines when the current diagnostic problems are settled. A failure
   gets a named bounded investigation/fix; no blind repeat, weaker assertion
   or assumption that source metadata fixed it. Further production changes
   stay in their owning reviewed commits; the temporary profile remains
   isolated. Do not start four-hour aging while that diagnosis is unresolved.
   This does not require proving every historical failure's cause.
6. **Prepare final delivery from production, not diagnostic history.** Return
   to the retained reviewed production lineage with 14400/comment absent;
   do not merge/cherry-pick the temporary commit or add its revert. Retain
   diagnostic refs/checkouts/results. Preserve tested 645927, remove only the
   isolated `[skip ci]` paragraph from the production commit in the released
   Git window, and prove tree/patch/message equivalence. All intended source
   and final message must be committed before final affected review/history
   reconciliation. Inventory the complete final base-to-head series: no
   diagnostic/revert/WIP residue or skip marker; separate production fix
   retained; no migrations. Refresh/changed-target issues return to root for
   their bounded assessment rather than expanding this package silently.
7. **Qualify the exact final head once.** After accepted final review, root
   releases A's guarded publication and final full run. Publish the rewritten
   feature only with the freshly verified exact expected-old-head lease,
   retaining its tested predecessor ref and reconciling remote effects.
   A message-only amend
   can have no changed paths, so do not promise automatic push CI. Bind an
   actual eligible full run or perform one existing unfiltered dispatch with
   the inputs above after fresh exact-head/no-duplicate reconciliation. No
   artificial source edit to trigger CI. Require full native plus all nine
   lifecycle rows, restored 14400-second `scale-aged` aging, actual
   semantic/identity/recovery evidence and ordinary conditional merge checks.
   Neither focused645927 nor diagnostic-head runtime results substitute for
   exact-final-head acceptance; source/version/guest input identities differ.

The original preparation deliverable was A's committed one-file diagnostic
head, quick-check/equivalence receipt and affected-review packet, after focused
acceptance. That route has reached the run; the current next diagnostic
deliverable is bounded below. Review/launch remain real package boundaries, not per-command
permission requests. No new approval of the already user-directed temporary
shortening is needed. Rollback is return to the retained production
ref/profile; no deployment or persistent-state conversion is involved.
Operator-owned runner updates, original recovery contracts and the existing
cache/build policy remain unchanged. The earlier skip-removal-then-immediate-
four-hour route is superseded; no workflow or generalized campaign system
is added.

## Bounded scheduler-hotplug evidence package

**Historical decision for bda1:** GO for the remaining already-running
`41921632759` rows under the existing sole watcher. They still provide
distinct profile/predecessor/native evidence. Keep aged-v5 job
`126907163490` failed; its successful CPU return/progress is not a health
pass. HOLD blind retries and final 14400-second advancement while root
disposes of this current diagnostic failure. This is no new historical
root-cause gate and releases no CI action. Root alone decides any later
guarded cancellation after evidence is secured.

Dependencies are [C's completed receipt](package-c-diagnostic-300s-aged-v5-triage.md)
and the [pinned source interpretation](design.md#diagnostic-scale-aged-v5-cpu-offline-warning).
The fault is predecessor `6.12.95.5`, before candidate activation; the old
loader/CSD package is not applicable. Runqueue count two/only stopper printed
does not identify the second scheduling entity or the initiating cause.

**Original owner: C, under root's released conditional implementation/commit
package**, with A for immutable checkout/ref identity. That implementation
ran at 13b; its preparation/cleanup lifetime below is superseded by the
[setup-order remedy](#capture-setup-order-remedy-package). Site, fields and
identity/data requirements remain. This is finite
diagnostic preparation, not a kernel fix or an automatic reproduction run.
The accepted caller-site simplification changes no capture-field or behavior
contract and releases no additional check or runtime action.

1. **Validate one frozen-kernel observation point using retained inputs.**
   Use the exact frozen-boot SDK/ELF and pinned source already associated
   with `050sh2…` and v5 `b31f6440…7984`. Confirm that the compiled
   observation is the **pre-CALL instruction at `sched_cpu_dying+0xc3`**,
   with its five-byte call to `dl_server_stop` and relevant type layouts.
   The preceding validated LEA at `+0xbc` supplies RDI=`rq+0x968`; RBX
   holds `rq`. Both source and compiled flow place this observation after
   the warning/dump, before fair-server dequeue, while holding the same
   runqueue lock. Preserve unique native NF3 symbol/base lookup, exact
   frozen notes/ELF identity, instruction boundary/length/target and
   blacklist/excluded-range guards for this caller address. Check that
   the entity's `rq` agrees with RBX and that the entity is its embedded
   `fair_server`. Do not assume symbol names alone prove these properties,
   guess offsets/register meanings, or use a probe at a different moment
   as equivalent evidence. No restoration, kernel build, Nix/toolchain
   project or new module resolver is implied; report unavailable retained
   inputs or an unprobeable/unsupported site as the bounded blocker.
2. **Prepare the smallest existing tracefs capture if that contract holds.**
   The intended source boundary is
   `tests/suite/kernel/livepatch-6.12.95/qualification.rb` only, plus its
   existing evidence receipt. Use the existing guest tracefs facility for
   this finite caller instruction and CPU127. The earlier global callee
   `dl_server_stop+5` probe is superseded: observing the caller prevents
   unrelated callee invocations from entering probe handling. Remove the
   callee `$stack0` return-PC fetch/filter; it has no such meaning at this
   caller point. Preserve all entity/runqueue checks and capture fields.
   Capture monotonic event time/CPU, runqueue `nr_running` and `nr_pinned`,
   class counts, and fair-server queue membership and active/throttled/defer
   state using validated field widths/bitfields. Preserve the existing
   console task dump and CPU online/offline/progress timeline. The minimum
   decisive record must distinguish an enqueued synthetic server from
   unexplained runnable/pinned work; an active flag alone is insufficient.
   Named hotplug masks are useful only if available with the same validated
   capture, not a reason to add another mechanism. No trace of 100000 task
   migrations, broad register dump, host scheduling engine, new C probe,
   SDK/candidate schema or production source change is in this package.
3. **Bound capture and failure handling.** Enable only around the existing
   pre-transition offline/online operation, with a bounded owned trace
   buffer and finite event scope. Keep the hotplug commands, population,
   deadlines and cumulative dmesg baseline unchanged. Capture on success
   as well as failure, retaining the earliest warning; disable/remove only
   the owned events in ensure, preserve the original exception and normal
   workload/recovery teardown. Missing metadata, unsupported fetch
   expressions, site/identity mismatch or absent decisive fields must be explicit
   diagnostic incompleteness, never a passed health/qualification result.
   If existing tracefs cannot express this bounded safe observation, stop
   and return the precise missing capability; do not expand into a new
   instrumentation subsystem or silently change kernel inputs.
4. **Preparation acceptance and later runtime gate.** The owner returns
   exact frozen ELF/SDK bindings, resolved caller/type evidence, finite
   fetch expressions, source diff and ordinary cached Ruby parse/style
   checks. Review checks that the probe is at the validated caller CALL,
   unrelated `dl_server_stop` calls cannot enter it, mismatched type/identity cannot be used,
   buffer bounds and cleanup preserve the original failure, and no health
   predicate/profile changed. Do not substitute a userspace model of
   `nr_running` for actual scheduler proof. All intended diagnostic source
   must be committed and affected-reviewed before root can release one
   separately bounded same-profile 300-second check under the standard
   cache/watcher policy. No long run is authorized now. Runtime acceptance
   requires a correctly bound event/fields and retained health outcome;
   a clean run without the warning narrows nothing about the old initiating
   cause. If the warning recurs, queue membership plus counters discriminate
   the fair-server hypothesis from residual-task/pinning/accounting cases.

No production/kernel correction is selected. A confirmed scheduler defect
would require a precise separate correction and root/user scope decision;
the accepted shutdown fix does not authorize it. Preserve exact boot/notes,
predecessor digests, 128 CPUs/16384 MiB/100000 tasks, 300-second diagnostic
age, all watchdog/health/witness/recovery checks and final 14400 acceptance.
There is no migration, persistent format, service API or coordinated fleet
update. Diagnostic rollback is return to the retained diagnostic input
without the observational delta; it does not convert failed evidence into
a pass. Retain refs and receipts; no cleanup or lifecycle action follows.

## Proposed one-case diagnostic launch route

**Root accepted and executed this finite boundary at 13b / 41938327930;
no new run or workflow edit is released by this record.** The steps below
retain the original launch recipe and f412 preparation anchor. A later
remedy run must instead bind its newly committed/reviewed successor of 13b;
the original head must not be reused as proof of the changed code. For the
original route, A owned the complete workflow, official
action-reference verification, quick-check, normal-commit and combined-review
package. C's observation is committed at
`f41262be6759876709c35677b847da1f6ba53eec`, parent bda1, only
`qualification.rb` (+132/-1); root reports 17 controls plus parse/lint
passed and Git ownership released. C supplies its final receipt; those
checks do not replace combined committed review.
Current remote/runtime bda1 and its sole watcher remain untouched. There
must be no second watcher/run without root's later release and utility-slot
reconciliation.

Existing dispatch cannot select this one lifecycle row: nonempty
`test_pattern` skips capture and lifecycle; native lacks livepatch opt-in
and accepts only `ci`/`proxy-exec` tags; empty pattern schedules native+9.
These are source-proven rejects, not failed runtime experiments. The exact
case is `kernel/livepatch-qualification@amd-scale-aged-v5` (`#default`),
with tag `livepatch-qualification-amd-scale-aged-v5`. Current source and
original job `126907163490` log lines 252–266 show one selected instance.

1. **One temporary execution file, on diagnostic ancestry only.** In
   `.github/workflows/ci.yml`, add an explicitly temporary `if: ${{ false }}`
   to the native `test` job and reduce the existing lifecycle matrix to:

   ```yaml
   include:
     - vendor: amd
       runner: amd-livepatch
       label: amd-scale-aged-v5
       tag: livepatch-qualification-amd-scale-aged-v5
       large: true
   ```

   Preserve build, identity capture/cache outputs, lifecycle condition and
   body, opt-in environment, one-job admission, artifact/result/cleanup
   behavior and existing timeouts. No action-reference replacement or
   unrelated workflow refactor is part of this proposal; the owner follows
   applicable workflow/action-reference verification guidance and brings
   a required scope change to root. No new workflow/input/profile or native
   tag escape hatch. No source-only trigger edit.
2. **Prepare and review the exact execution head.** A owns this workflow
   file and serialized Git/publication; C keeps its one-file capture boundary.
   Keep bda1 as the retained prior diagnostic anchor and use C's exact
   f41262be6759876709c35677b847da1f6ba53eec as the workflow commit's
   preparation parent. The future head `D` must contain that observation
   and the temporary workflow delta,
   with the existing 300-second scale-aged profile. Record full `D`, base,
   changed paths, C receipt and normal cached YAML/workflow checks/hooks;
   perform affected committed review before publishing. Review explicitly
   checks the sole matrix row, skipped native job, unchanged capture/env,
   resource/profile/health/recovery contracts and diagnostic-only ancestry.
   Do not assign a guessed future SHA or treat C's commit alone as the
   reviewed execution head.
3. **One guarded qualifying run, after root release.** Retain the existing
   diagnostic branch/ref; confirm local and intended remote `D` and the
   expected old remote head before publication. The workflow/test paths can
   start an ordinary push run: publication itself requires run release.
   Bind that actual exact-`D` run if eligible. Only if no eligible run exists
   after bounded no-duplicate reconciliation may root release one existing
   workflow `162100852` (`.github/workflows/ci.yml`) dispatch at that exact
   verified diagnostic ref, with these literal inputs:

   ```text
   test_suite=ci
   test_pattern=
   test_tag=ci
   prebuild=true
   stop_on_failure=false
   proxy_lock_full_matrix=false
   zfs_tags=functional
   zfs_test_body=
   ```

   Keep both string selectors shown empty. For an ordinary push, existing
   defaults produce the same empty-pattern capture and lifecycle route;
   record the actual event rather than inventing dispatch inputs. Never
   dispatch a duplicate or use `ci-unstable`/`zfs-full`. The native-only
   `stop_on_failure` input does not alter this single lifecycle row.
4. **Required selection and input evidence.** Expect one build job plus
   exactly one AMD aged-v5 lifecycle job and native skipped, with `[1/1]`
   selecting `kernel/livepatch-qualification@amd-scale-aged-v5`, script
   `default`. Preserve `VPSADMINOS_ENABLE_LIVEPATCH_TEST=1`, the captured
   producer/module/SHA/sites/source/lock outputs and every row/guest
   equality check. Require the new source identity `D`, frozen `.95`
   boot/notes and archived-v5 digest, 128 guest CPUs, 16384 MiB, 100000
   tasks and 300-second age. Keep `large:true` and the existing
   `--max-cpus 128 --cpu-overcommit ceil(128/host_cpus)` calculation;
   memory admission remains unchanged. Record actual host/runner, QEMU,
   kernel/initrd/system paths and launch identity; a source-version change
   means the complete system input is not literally the old bda1 input.
5. **One outcome, then stop.** The assigned sole watcher escalates an
   unexpected selection, identity/profile/capture guard failure or deadline;
   it does not retry or change checks. Retain the bound pre-CALL record,
   warning/dmesg and original test outcome with uploaded artifacts and
   teardown status. Require CPU127, consistent entity/RBX/runqueue and
   embedded-fair-server identity, and actual pinned/runnable/class counts,
   queue-membership and server-state data; a probe hit alone is insufficient.
   Interpret the captured counters alongside the health outcome, without
   promoting the fair-server hypothesis to cause from static feasibility.
   Diagnostic evidence can be complete while qualification
   remains red. A green requires the entire original case, including its
   health, activation/recovery and graceful QEMU exit; never force recovery
   past existing quarantine rules to make it green. A nonrecurrence does
   not explain the earlier warning. Root accepts the result and chooses any
   next package; no automatic rerun/full matrix/four-hour escalation.

This avoids repeating unrelated native/eight lifecycle rows, not the
unchanged build/cache preparation. Previously cold local closures and cached
metadata alone do not justify reviving a local VM/preflight/build package.
Final acceptance still requires the exact production head with original
14400, full native+9 and all established gates. Keep age/observation/workflow
commits and their evidence on retained diagnostic ancestry, excluded from
delivery rather than reverted into it. Rollback is returning to the retained
diagnostic inputs or production ref as appropriate; no guest/kernel update,
production deployment, persistent migration or cleanup is authorized.

## Capture-setup order remedy package

**Implemented/reviewed at b361; early arming, capture and pre-hotplug health
now passed in actual runtime.** Normal late observer release remains
unexercised because drain was unconfirmed after the later activation failure.
The steps below retain that accepted lifetime contract; the next proposed
package is the loader/CSD evidence brief below. Historical 13b capture was
incomplete, not a reproduced scheduler warning or passed health phase. Use
[C's actual runtime audit](package-c-scheduler-capture-runtime-audit.md) and
[the pinned source distinction](design.md#current-capture-setup-failure-and-lifetime-remedy).
C is the proposed sole implementation owner after its audit acceptance;
A owns the normal history/fold/publication window. File boundary remains
`tests/suite/kernel/livepatch-6.12.95/qualification.rb` only. Existing
one-build/one-aged-v5 workflow, source inputs and field schema stay unchanged.

1. **Separate ownership lifetime from recording lifetime.** Refactor the
   current helper into small preparation, recording and release helpers
   within the same file. Keep finite instance/event/arm/recording state at
   example scope so after-hooks can reconcile it; no generic resource class
   or runner API. Retain the exact current AMD/v5/128CPU/16384MiB/100000-task
   selector; other profiles do nothing. Check exclusive absence of the
   owned private instance/event before creation. Track an attempted command
   whose effects are uncertain separately from acknowledged creation/arm;
   never infer rollback from an exception. Do not remove a preexisting
   unrelated resource.
2. **Prepare early.** Immediately after
   `wait_for_patch(machine, previous_name, 1)`, before
   `prepare_transition_state` or any stress/population start, verify the
   existing v5/notes/native-site contract and prepare the same 64-KiB,
   mono, CPU127, overwrite-off instance, definition and filter. Verify its
   `current_tracer` is `nop`; do not switch a tracer under load. Clear the
   private buffer here, enable the event and require successful enable
   acknowledgement/readback while `tracing_on` remains 0. Only successful
   preparation permits workload creation. Preserve 10-second control
   budgets; a failure stops before stress, preserves its original error
   and makes one bounded owned cleanup attempt with no population present.
   An uncertain enable is not silently retried or treated as disabled.
3. **Record late without arm/disarm.** At the unchanged pre-transition
   hotplug location, verify prepared state and turn only the private
   `tracing_on` ON. Call the original hotplug body unchanged. In its ensure,
   turn recording OFF and retain the existing trace/decoded fields,
   loss/miss/profile checks and original-exception precedence. No new
   event registration, enable/disable, clock/mask/buffer reset or deletion
   belongs in this window. The early buffer is new and recording was OFF;
   there is no need for a late clear. A recording-toggle/read failure is
   still diagnostic INCOMPLETE; no guarantee of prompt execution follows
   from avoiding the text-patch path.
4. **Release after drain, with bounded failure behavior.** On the normal
   path, use the existing successful `exit/sctp.exit/tun.exit`, population
   `state=stopped`/`tasks=1` and `stop_stress` completion, then disable/delete
   the owned event and remove its instance before final health and
   `@qualification_completed=true`. Confirm acknowledged cleanup; a new
   cleanup failure must prevent a success result. Make release idempotent
   for already-released or never-created state, without retrying an
   uncertain mutation blindly. On failure/cancellation delivered through
   existing ensures/hooks, preserve the original failure and pre-cleanup
   evidence, then existing stop/release/CPU restoration. Use the reserved
   diagnostics channel for bounded reconciliation if the primary shell is
   occupied. Attempt observer disarm/delete only when actual workload-drained
   evidence is available (or workload never started); a stop request alone
   is insufficient. If drain or command effects are unconfirmed, leave
   recording OFF where acknowledged, report incomplete owned cleanup and
   preserve ordinary failed-VM teardown. Do not add a long drain wait,
   process killer, patch reversal, background cleanup or retry loop. A hard
   runner/guest termination cannot promise ensure execution; retain actual
   teardown evidence instead of claiming in-guest removal.
5. **Finite quick controls and review packet.** Reuse the current actual-
   helper host harness and its decoder negatives. Add order/failure controls
   showing early enable/readback before workload start, nop/OFF rejection,
   no hotplug after partial setup/enable timeout, recording-only commands
   around both successful and failing hotplug, original-error preservation
   when capture/cleanup also fails, no disarm before confirmed drain, and
   successful owned cleanup before completion. Cover an unconfirmed drain,
   uncertain enable effect, cancellation through the owned ensure path,
   and nonselected profile without weakening
   missing-record, identity, type, queue-membership or loss/miss checks.
   Run normal cached Ruby parse/style checks and the finite harness; report
   exact commands/results and diff. No kernel, Nix/guest build or VM is a
   quick prerequisite. All intended source must be normally committed/folded
   by the owner and receive affected independent review before root can
   release another one-case execution; 13b's prior review does not certify
   this ordering change.
6. **Later one-case runtime acceptance, only after release.** Use the
   accepted same-profile route at the exact new committed/reviewed head.
   Require early arming acknowledgement plus nop/OFF state before workload;
   actual 100000 tasks/128CPU/16GiB and age >=300; private recording around
   the original CPU127 hotplug; finite bound counter/queue/flags record,
   loss/miss evidence and original health outcome. Require actual late
   cleanup/drain and graceful teardown for a passing qualification. A valid
   capture with the original warning stays red; an enable/read/cleanup
   timeout remains incomplete, not a scheduler diagnosis. One outcome ends
   the package for root assessment; no automatic repeat, timeout increase,
   four-hour escalation or warning exemption.

No production correction or product-scope approval is needed for this proposed
diagnostic ordering alone. Kernel/scheduler causality is still unproved;
source identifies possible synchronization, not the timed-out command's
actual wait. Keep all watchdogs, exact boot/notes/predecessors/current module,
same rare pre-CALL and fields, recovery/quarantine and temporary ancestry.
Rollback returns to retained diagnostic code/evidence, not to a manufactured
pass. Primary 645927/original 14400 and final full native-plus-nine gates
remain untouched. No additional investigation, runtime or cleanup is launched
by this plan.

## Incoming staging d2fe and the next anchored diagnostic

**Recommendation: retain exact reviewed c08 for the temporary experiment;
do not automatically refresh either branch.** Root owns acceptance and any
later execution release. The [incoming assessment](design.md#incoming-staging-d2fe-temporary-diagnostic-disposition)
records the complete one-commit/one-path range and consumer evidence. This
supersedes the old assumption that the next diagnostic publication must find
staging at2951; it does not change the diagnostic's source base or waive a
fresh target guard.

The frozen bindings for that later package are:

- reviewed local diagnostic `c08a59956c4a905e5a787046251234a615c7e807`,
  parent `b361b8c600bc1d50c237a68ca5413d38be9a0e99`, base
  `2951a632c4254a44747a8da326e3dde897eaa0e2`;
- observed staging `d2fe1489f0b0b213fb247aeee6e081d349adaf42`;
- unchanged expected primary remote
  `645927e22809a29c67ffd59c072e553e05e2a72b` and old diagnostic remote
  `23db05954b7b69c382a696ff6d202d5654c2c52c`;
- the four reviewed source hashes and retained source roots in
  [A's stopped publication receipt](package-a-raw-tick-publication.json).

1. **Root/A guard and publication, only after release.** Preserve c08's seven
   owner objects/messages and tested predecessors. A's ordinary fresh guard
   must compare actual staging with d2fe and the two owned remotes with the
   values above, plus clean local c08/reviewed source. Another difference
   stops for bounded reassessment; never rewrite the expected values to
   whatever a fetch returns. No rebase, lock update, source amendment or
   primary push is needed for this experiment. If accepted, publish exact
   c08 through the already specified exact-old diagnostic lease and hooks.
   This document is not an execution or integration authorization.
2. **Reuse the committed review for its actual source.** c08's ALL4/HIGH
   no-findings review and quick receipts remain bound to unchanged c08;
   this read-only incoming-target assessment adds no source change or
   automatic review rerun. Do not relabel them as reviewing d2fe or its
   new dependency. No Nix evaluation, package restoration, kernel/ELF query,
   environment preparation or extra suite is required merely to retain
   this anchor.
3. **One existing diagnostic route, separately released.** Require an actual
   qualifying run bound to exact c08. Use the existing push-triggered run,
   or one existing unfiltered dispatch only after bounded no-duplicate
   reconciliation establishes that no qualifying run exists. Do not assume
   a publication automatically triggers it or edit source to force a trigger.
   Keep one build plus `kernel/livepatch-qualification@amd-scale-aged-v5/default`,
   native skipped, exact frozen95/v5,128CPU/16384MiB/100000tasks/300s.
   The build captures its normal producer/module/SHA/sites once; retain all
   per-row integrity checks, source/version records, host readiness, clocks,
   health,1800 deadline and recovery. Record actual resulting identities;
   no store-output equality to a refreshed d2fe tree is presumed. This is
   the next no-host-frequency diagnostic, not a blind retry or final pass.
4. **Final delivery remains a separate latest-target package.** Before final
   review/integration, assess then-current staging and refresh the delivery
   tree as required, with patch/history equivalence and source/input receipts.
   For this incoming delta, review scope is the unstable container-template/
   persistence inputs, embedded template lock metadata and refreshed source
   identities, plus any actual integration conflicts; unchanged Linux/.95/
   runner code needs no speculative rewrite. Do not claim refreshed module,
   SDK, runner or guest derivation equality from the file inventory. Reuse
   evidence only for exact proven unchanged inputs. Restore14400 and require
   full exact-final-head native plus nine lifecycle rows and all identity,
   semantic, kernel-health and recovery witnesses. No c08/300s outcome
   substitutes for that contract or broadens conditional merge approval.

Remaining risks are the still-unproved actual host baseline/capture and loader
cause, plus unmeasured outputs of a future refreshed input graph. The default
ref advance itself supplies no expected fix for those faults. All earlier
failed attempts and bindings remain evidence. No implementation, Git writer,
network, CI, node or lifecycle action was performed for this assessment.

## Accepted loader CSD and owned-host evidence package

**Disposition completed:** root accepted ordinary802898/run42057169147;
the current next package is [final delivery](#conditional-diagnostic-head-and-final-verification-package).
Collector work remains stopped. The 08e analysis and ordinary sibling packet
below are retained history, not a request for another300s run or allocation.
[The full 08e audit](package-c-scheduler-hotplug-preparation.md#current-08e-bounded-runtime-audit)
is accepted evidence, not qualification. Exact
`08e3d0f910d5cc7140e2eb532497218f52e94a16` / run42040026542 remains RED:
178 complete fixed-map samples/22784 rows and actual provider round trip
passed; 100000 tasks aged 337.867s, pre-CPU127 health and the healthy 1/0/loss0
record passed; PID143049 insertion returned 0 in 905.74s, activation 906.502s
below 1800, enabled=1/transition=0. End-marker EBADF, partial all-CPU stats
with real drops, identity/callback/export timeouts and missing population
exit leave native completeness, post-health and recovery unproved. A size
readback of 67 versus expected 64 neither explains those timeouts nor repairs
lost events. No further source/transport optimization is needed to choose
this disposition; the actual reservation/timeout causes remain unknown.

The seventh owner's 918 added handwritten lines are diagnostic machinery.
Continuing to repair its complete-window contract is not presently necessary
to exercise the original product contract. Retire both temporary observers
for the next case, not any ordinary assertion. The prior loader and dying-rq
health results remain bounded evidence; their removal does not prove they
caused earlier faults. A successful ordinary case will not explain old faults.

**One complete preparation package, if accepted by root:** A owns the
session-local ref/checkout, exact replay, quick checks, normal commit and
history packet; C is available for existing-source clarification. Architect
owns this brief. No parallel application package, source investigation or
collector work is needed. Root separately owns review acceptance/publication
and any single runtime release.

1. **Retain tested history and use the ordinary source anchor.** Leave
   primary645927, diagnostic08e and every earlier ref/evidence intact. Prepare
   a new same-session diagnostic evidence ref/checkout, suggested
   `2026-11-03-livepatch-fixture-failures-ordinary-300s`, outside final delivery
   ancestry and without a new delivery registration. Start from retained
   `bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf`: verify its exact parent is
   `645927e22809a29c67ffd59c072e553e05e2a72b` and its sole source delta is the
   saved age patch SHA256
   `c46380fdc1f05abd76fd975e25321d40ee2e37a15fdbcdb59c1ff42810554dde`.
   A mismatch stops preparation; do not reset/rewrite old refs. This reuses
   the ordinary source plus the user's temporary age choice, rather than
   applying inverse edits to 08e's collector.
2. **Only one new execution-purpose file.** Reuse the established temporary
   workflow delta from `538706790c459bfefae4593bf963fa0d37961870` to
   `b361b8c600bc1d50c237a68ca5413d38be9a0e99`: `.github/workflows/ci.yml`
   sets native `test.if` to `${{ false }}` and retains only the existing
   lifecycle include `{vendor: amd, runner: amd-livepatch,
   label: amd-scale-aged-v5, tag: livepatch-qualification-amd-scale-aged-v5,
   large: true}`. Preserve normal build/capture/opt-in/artifacts/admission/
   timeout/teardown behavior. No loader wrapper or host sampler is included.
   A verifies the retained delta before replay; do not transplant the 08e
   workflow. Relative to primary, the only changed paths must be this
   workflow and `tests/suite/kernel/livepatch-qualification.nix` (scale-aged
   14400→300 plus the existing comment). Qualification.rb, common.nix,
   normal producer, resolver, fixtures, boot and recovery source equal primary.
   Exclude dying-rq purpose538706 and loader purpose08e completely; retain
   their refs without a revert commit. All original hotplug, health and
   current-module semantic witnesses remain in ordinary source.
3. **Quick checks and committed review.** Prove the exact parent/range and
   two-path final diff, saved age-patch equality, primary qualification/common
   equality, single lifecycle row, skipped native and unchanged normal
   captured producer/module/SHA/sites plus opt-in environment. Use the
   established cached Nix parse/nixfmt and YAML/workflow checks and normal
   hooks; reuse unchanged ordinary Ruby/resolver/producer receipts only for
   their exact inputs. No new test framework, kernel/build/preflight or
   retired collector tests are required. Follow applicable action-reference
   guidance for the workflow; an unavoidable extra change returns to root.
   Commit before affected independent review of the two temporary deltas,
   original assertion/recovery preservation and complete history. Preserve
   earlier reviewed implementation evidence; no unrelated re-audit. The review
   must explicitly confirm that no ordinary fix or semantic witness was lost
   with the diagnostic purposes. Record future head D, not a guessed SHA.
4. **One later run only after review and root release.** Guard exact D,
   intended new ref and primary; record the actual staging target (last known
   d2fe), applying the existing anchored-diagnostic disposition rather than
   silently refreshing either source. A changed relevant contract returns to
   root. Publication can trigger CI: bind the actual eligible exact-D push
   run, or only after bounded no-duplicate reconciliation use one existing
   workflow162100852 dispatch with `test_suite=ci`, empty `test_pattern`,
   `test_tag=ci`, `prebuild=true`, `stop_on_failure=false`,
   `proxy_lock_full_matrix=false`, `zfs_tags=functional`, empty `zfs_test_body`.
   One fresh sole watcher, one build plus one
   `kernel/livepatch-qualification@amd-scale-aged-v5/default`, native skipped.
   No local cold-closure VM route, blind repeat or extra matrix is implied.
5. **Acceptance is the ordinary case, not insertion alone.** Require newly
   captured current normal-module/sites identity shared by build/row/guest,
   exact frozen .95 boot/notes and archived v5, actual 128 CPUs/16384MiB/
   100000 tasks/at least300s, original CPU127 hotplug and cumulative health,
   existing callback/semantic assertions, activation within1800, complete
   post-transition health, workload stop, recovery and graceful teardown.
   Capture existing runner/shell/console/launch/artifact evidence. Do not add
   a historical current-module digest gate, a new observer or the retired
   capture-completeness requirement. New source/config/system identities
   must be recorded; no whole-input equality with 08e or latest staging.
   Any identity/selection/health/activation/stop/recovery failure is RED and
   ends this package with one named outcome assessment. No automatic retry,
   timeout growth, stress reduction, new instrumentation or production fix.

This is removal of temporary test observation, not a production/kernel/API or
persistent-state change. Rollback means selecting a retained ref for a separately
authorized check; no deletion, session lifecycle action or deployment is involved.
Root can accept this conventional scoped route without a new user product
decision. A genuine production correction or health-policy change would require
its own scope decision. A 300s green settles only this case; root still assesses
remaining shortened profiles/problems before restoring14400 and the reviewed
then-current final head's full native+9/identity/health/recovery gates. There is
no universal requirement to explain every historical cause before qualification,
and no old failure is waived by nonrecurrence.

### Retained loader package through 08e (not the next execution brief)

The remainder preserves the former source/capture contract and rationale.
It was implemented, reviewed and exercised through 08e. Any future-tense
allocation, seventh-owner amend or run instruction below is superseded by
the proposed ordinary-case route above, not an outstanding implementation task.

**Historical c08→08e packet:**
[C's final audit](package-c-scheduler-hotplug-preparation.md#current-c08-raw-tick-runtime-audit)
is the incident authority. Initial 128-map readiness is proven, later host
coverage and native trace completeness are not. Candidate insertion success
does not supply post-health/recovery qualification. Root owns acceptance and
release of the finite two-file packet below. Source `23db`, run42003244138,
failed with command status127 before its first header/snapshot/ready/map.
Preserve [C's audit](package-c-scheduler-hotplug-preparation.md#current-23db-baseline-runtime-audit)
and tested `23db`; the later operator value 100 does not establish the job's value.
This is a host command/provider/PATH prerequisite failure, not evidence of a
clock regression, kernel fault or LC1 recurrence. Its precise environment
cause need not be guessed to remove a prerequisite with no consumer.
User-supplied deployment context is a VPS
runner sharing its vpsAdminOS node's kernel; root recommends no node-wide
change merely for this capture. No setting mutation is authorized. The
[9805 runtime audit](package-c-loader-csd-runtime-audit.md) remains FAIL at
the early combined stats/CLK_TCK gate; the later operator result stats=0,
CLK_TCK=100 does not recover the original job's missing values. No stress,
aging, activation, actual TID map or host sample was reached by that run.
The earlier stats=1 and positive-CLK_TCK contracts are superseded, not
retroactively passed.
This is the design for C's next complete source/check packet, not an
implementation or runtime release. Mapping, ownership and clock validation
remain pre-stress runtime gates. C supplies the accepted
[b361 runtime audit](package-c-scheduler-lifetime-runtime-audit.md); A later
owns normal commit/history/publication and architect owns this brief.
Routine clarification is direct with architect/A; consequential deviations
return to root. The b361
first softlockup belongs to the first returned EBUSY, not the third unknown-
PID timeout. No second artifact audit, kernel correction or new run is assigned.

Accepted files: `tests/suite/kernel/livepatch-6.12.95/qualification.rb`,
temporary `.github/workflows/ci.yml`, one narrowly scoped
`tests/suite/kernel/livepatch-6.12.95/loader_host_sched.sh`, and
`tests/suite/kernel/livepatch-6.12.95-common.nix`. The helper uses
the CI job's existing Bash and procfs, not a new environment or generalized
collector. No OSVM/test-runner API, protected-field access, kernel/probe,
resolver or profile change. All changes remain outside delivery ancestry.
The fourth-path naming, baseline clocks and unused-frequency removal are
already implemented. This refinement needs only `loader_host_sched.sh` and
qualification.rb's capture/consumer code; workflow/common.nix stay unchanged. No kernel/
runner-API change is proposed. All four original paths
remain one coupled **seventh loader-evidence purpose after b361**. A folds
this refinement into that owner after C's freeze, retaining tested `c08`, `23db`,
`9805` and the
old/new range inventory, all six earlier objects/messages and LC1 review
history. Do not fold into dying-rq `538706`. The new capture contract requires
affected ALL4/HIGH review before publication or any separately released run;
LC1's earlier focused reconciliation does not approve this contract.

**Current two-file execution packet after c08.** The following changes refine
steps 3–7 below; all five events, callbacks, attempt/PID association, first-fault
logic, original 1800s/health/recovery and source/boot/profile bindings remain.

- **Required host scope:** keep strict initial discovery and validation of
  the complete unique 128 vCPU index/TID/start/label map. Subsequent snapshots
  iterate that fixed map only, opening each required task through the pinned
  QEMU proc directory and checking its exact start and label before/after
  data reads. Preserve QEMU PID/start/exe, test-child ancestry and final
  snapshot revalidation. Required disappearance/reuse/rename or unknown data
  is terminal; no retry, replacement discovery or reattachment. Do not
  collect incidental per-thread rows after readiness. Emit the explicit
  scope `required_vcpu_threads=128`; total QEMU thread count remains a
  required bounded sanity value (128..256) at both ends, but equality across
  those reads is not required. Retain the initial enumeration cap and all
  clock/output limits. The old 131-row partial sample remains incomplete.
- **Metadata before payload:** stop/join the public-console observer, attempt
  the existing end marker when applicable, then perform the existing one-shot
  OFF/readback/freeze bracket. A failed marker remains an accumulated error.
  Collect and immediately persist actual attempt/PID files, frozen notes/
  source and callback identities, tracing_on/current_tracer/clock/cpumask/
  buffer/overwrite and five event enable/filter readbacks, plus the 128 CPU
  stats blocks. Use bounded small command outputs (each 10s, metadata capped
  at 128 KiB) and write owned files under the existing state directory before
  any large read. Record each unavailable item; do not abort collection of
  independent small metadata merely because another item failed. Validate
  exact CPU coverage and existing loss/full predicates without weakening
  them. Metadata invalidity is retained even if a payload can be saved.
- **One bounded compressed transfer:** use the existing public diagnostic
  shell with 10s, no retries. Run the following native pipeline inside the
  declared guest Bash with `-e -o pipefail`, surrounded by fixed begin/end
  framing. Use constant paths/arguments and ordinary shell quoting:

  ```sh
  head -c 67108865 "$trace" | gzip -1 -c | head -c 2097153 | base64 -w0
  ```

  Limits are 64 MiB decoded native text and 2 MiB compressed bytes; the extra
  byte detects overflow. Emit a fixed header before the pipeline and a footer
  only after pipeline status 0. Raw-limit or compressed-limit truncation
  cannot count as successful capture. Bound
  encoded output before Base64 decoding (four-thirds of the compressed
  cap+1 plus fixed framing). Strictly decode Base64; validate compressed
  length; incrementally inflate through the declared `Zlib::GzipReader` /
  `StringIO` facilities with a decoded cap+1 and full EOF/CRC/length checks.
  Reject trailing data, concatenated members, corruption, missing framing,
  nonzero status, timeout or either limit. Do not guess a limit hit is EOF.
  Do not use unbounded GzipReader.read or an uncompressed whole-trace cat.
- **Native evidence and acceptance:** save complete decoded native text to
  an owned .log under TEST_RUNNER_STATE_DIR and its sizes/host digest/status
  to .txt, then run the existing actual native decoder/PID-file crosscheck.
  Print paths and compact counts, not the complete trace, in the runner log.
  Existing artifact globs already upload these suffixes; no workflow edit
  is needed. A failed transfer's bounded shell log and previously saved
  metadata remain useful, but never supply complete pending/token/loss
  conclusions. Preserve first error and all later capture failures. The
  window-closed marker stops host observation; it does not override failed
  native evidence or declare qualification success. Keep post-drain-only
  destructive cleanup and explicit unknown cleanup until VM teardown.

Ready/map/status formats and the existing wrapper EXIT contract are unchanged.
New raw trace and metadata files use the existing private test-state/artifact
route; no persistent guest format, production component or deployment changes.
Returning to the frozen primary tree removes this temporary diagnostic behavior.

Provider proof is limited and concrete: `os/modules/config/system-path.nix`
declares bashInteractive/coreutils/gzip and adds corePackages to systemPackages;
the common test does not remove that core set. `test-runner/nix/package.nix`
executes its declared ruby_vpsadminos, with Base64 explicitly in Gemfile /
runner-deps.lock. Retained declared Ruby3.4.11 contains default Zlib3.2.3,
StringIO3.1.2 and Digest3.2.0 gemspecs/native extensions. Use those facilities
inside qualification, not ambient wrapper Ruby. Quick checks must exercise
actual requires and the codec in the declared cached environment; stop on
missing providers instead of installing/bootstrap/fallback. Before stress,
the future runtime checks exact guest executable availability and a tiny
round trip through the same public command/consumer. No runtime or codec
check was executed during design, and throughput within 10s remains unproved.

Pinned trace source evidence: a238 `trace.c:6899–6956` / ring-buffer reserve
`:4550–4584` distinguish reservation refusal from a proven incident cause;
`ring_buffer.c:3475–3482,5051–5069` records full/no-overwrite drops;
`trace.c:8354–8415` provides independent per-CPU metadata. `trace` uses
seq-file iteration (`:4590–4675,4773–4808,5000–5007`); do not replace it with
consuming trace_pipe or write/truncate it. Keep filters/clock set only early:
clock writes reset buffers (`:7061–7090`), filter changes can synchronize
(`trace_events_filter.c:2346–2368`). The actual c08 full/disabled/other
reservation cause stays unknown. Public pull_file (`machine.rb:740–741`,
`shared_dir.rb:62–69`) uses a copy with the 900s machine default and has no
timeout parameter; it is not selected or wrapped with speculative cancellation.

Required checks operate on actual helpers/consumers: strict initial discovery;
later incidental TID removal/addition and bounded count changes accepted with
exactly 128 fixed rows; every required-TID disappearance/reuse/name change still
rejected; wrong ancestry/exe/caps/clocks still rejected. Exercise actual gzip/
Base64/Ruby round trips and rejection of missing footer, nonzero pipeline,
bad Base64, CRC/trailer damage, extra member/data and both cap+1 cases. Test
metadata persisted before a payload exception, and loss/full/failed-marker
remaining INCOMPLETE despite a valid payload. Keep original activation error,
observer join, host status/EXIT, missing drain and cancellation controls.
Reuse only unchanged common/workflow/provider-input receipts for their scope;
run declared Ruby/Bash parse/lint and affected real-helper controls before
freeze. C delivers both paths/checks/limits together; A amends the seventh
owner retaining tested c08/six prefixes and the complete old/new inventory.
Affected committed review precedes any separately released single run. A new
runtime must prove complete fixed-vCPU coverage and complete bounded native
transport with valid metadata/identity/loss/clock relations; successful
insertion alone, or useful but partial evidence, is insufficient. If the
compressed route cannot meet the fixed limits, stop with the exact gap; no
automatic timeout/buffer increase, retry or fourth application path.

**Settled fourth-path launch composition.** C's prior
[three-path STOP](package-c-scheduler-hotplug-preparation.md#current-loader-evidence-launch-naming-prerequisite)
correctly identified disabled thread naming. Root now accepts this sole
launch-input amendment in common.nix. Define the finite selector in its
existing `let` and add the option inside the existing qualifying `boot.qemu`
configuration:

```nix
loaderHostDiagnostic =
  qualifying
  && qualification.id == "amd-scale-aged-v5"
  && qualification.vendor == "amd"
  && qualification.predecessor == "v5"
  && qualification.cpus == 128
  && qualification.memory == 16384
  && qualification.tasks == 100000
  && qualification.ageSeconds == 300;

# Within the existing boot.qemu attribute set:
extraQemuOptions = lib.mkIf loaderHostDiagnostic (
  lib.mkAfter [ "-name" "debug-threads=on" ]
);
```

Use the existing list option, preserving other contributed options. No new
flag, environment escape, machine override, runner API or QMP mechanism.
`tests/make-test.nix:255` forwards `qemuCfg.extraQemuOptions` when the machine
has no override, as here. OSVM `vpsadminos_machine.rb:162–175` places its
initial `-name os-vm-machine` before `expanded_extra_qemu_options`; the latter
only substitutes `@OSVM_TMPDIR@` (`machine.rb:1037–1041`). Thus the literal
appended pair reaches QEMU unchanged and all previous arguments retain order.

Exact retained QEMU archive
`/nix/store/bywm812fafb6rq5dz06ifzb3z36brx7n-qemu-10.2.4.tar.xz`
(flat SRI `sha256-ghtUW5LxZeV93cysUHfXbU1DaiJllbiBOtWTBrv9B0Y=`)
provides the parsing proof. In `system/vl.c:388–414`, `name` has implied key
`guest` and `merge_lists=true`; `:3516–3523` parses each `-name`, then
`:3731–3740` calls early option processing after the CLI loop. `:2584–2587`
dispatches `parse_name`, whose `:554–569` enables the explicit debug flag and
reads the retained guest name. In archive member `util/qemu-option.c`,
`:608–643` returns the existing unnamed list for repeated mergeable options;
`:743–836` parses `debug-threads=on` as an explicit key and appends only that
key, and `:881–946` connects this to the noisy CLI parser. Per-key reads use
reverse lookup (`:224–271`), so a later value for a supplied key wins; no
later `guest` value is supplied here. These are source observations, not a
QEMU execution result. C's receipt records all four declared patches and
postPatch as not changing these naming/topology paths.

Retain that exact source/patch/runtime-QEMU binding: `qemu-options.hx:1266–1280`
explicitly disclaims stable thread-name API. The pre-stress gate must still
validate actual guest logical CPU/APIC identity, the fixed topology's
QEMU cpu_index mapping, and the unique owned TID/start identity with its
expected `CPU N/KVM` label; enabling labels alone proves none of those facts.
Record the new diagnostic head and actual configuration/system/launch
identities plus the explicit naming pair. This is a changed launch input,
not whole-guest equality with b361. Primary 645927 and the 14400-second
profile remain untouched; returning to them removes this diagnostic option.

1. **Prepare native events before stress.** After exact v5/boot-notes
   checks, create one owned private `nop` instance, recording OFF, global
   guest trace clock, 64 KiB per CPU (8 MiB for 128 CPUs), overwrite OFF and
   all 128 CPUs included. Clear/configure/enable here, with acknowledged
   state/readbacks. Reuse native unique-symbol lookup for the two callbacks
   `do_flush_tlb_all` and `do_kernel_range_flush`; filter the existing
   `csd_queue_cpu`, `csd_function_entry`, `csd_function_exit` on their `func`.
   Filter existing `ipi_send_cpu`/`ipi_send_cpumask` on callback
   `generic_smp_call_function_single_interrupt`. Verify actual event formats
   and filters; absent/ambiguous symbols or unsupported event fields stop
   before population. This is existing tracepoint configuration, not new
   instrumented code. Event setup/teardown can synchronize; keep it outside
   the full population just like the accepted lifetime remedy.
2. **Bind the activation attempts and observation window.** Start private
   recording immediately before the first normal candidate insertion.
   Give each existing attempt an ordinal/token, write it and the actual
   guest PID to an owned state file and `trace_marker`, then `exec insmod`
   from that same guest process. Retain original module/locale, returned
   status/EBUSY rules, attempts, and the single cumulative 1800-second budget.
   Do not rely on buffered stdout as the only PID record. Before/after
   marker commands retain the existing host shell send/reply timestamps;
   record guest uptime in the same bounded command. No late event enable,
   filter reconfiguration or buffer reset between attempts. Preserve full
   health baseline and the earlier CPU127 capture.
3. **Freeze the first-fault interval without changing behavior.** Use one
   finite example-owned observer of the existing public `console_output`,
   starting at the activation-window cursor. On the first new softlockup
   marker, record its guest text and host observation time and make one
   bounded reserved-diagnostics-channel recording-OFF attempt. It must not
   cancel insertion, alter watchdog/panic policy or consume the primary
   shell. If no fault occurs, stop recording at activation return/failure.
   Always stop/join this local observer in the owning ensure; no delayed
   background cleanup. Unknown recording effects are reported, not retried.
   Preserve earliest data with no-overwrite, collect all per-CPU loss/full
   statistics, and reject gaps caused by missing records, saturation or
   an unacknowledged freeze as incomplete evidence. Buffer bounds cannot
   guarantee a complete fault window in advance; do not silently grow them.
   Later post-timeout reads must be labelled as such if no freeze succeeded.
4. **Decode only what the native events prove.** Queue records need the
   origin CPU/PID/time, target CPU, callsite, function and CSD token. Entry/
   exit need target header CPU/time, function and the same token. Target
   header PID is the interrupted task, not necessarily the issuing insmod.
   Dispatch records add target CPU/mask and dispatch callsite/callback.
   Join within the attempt/window and ordered reuse of a token; local calls
   can use NULL CSD. Queue-without-entry is not proof of a sent IPI or target
   starvation; dispatch-without-entry is not proof of delivery; entry-without-
   exit means outstanding at the freeze, not permanent deadlock. Loss-free
   history must distinguish one outstanding operation from repeated progress.
   A reused CSD whose earlier queue is outside the window remains unknown.
5. **Collect only owned host process facts.** The temporary job wrapper
   starts/joins the finite Bash sampler with its exact state directory and
   test-process ownership; ordinary CI cancellation/exit must reap it.
   Use the existing exact case `qemu-launch` record for PID/start ticks/exe
   and verify that process belongs to this job's test-runner child ancestry.
   Pin/revalidate the proc identity before reads, rejecting reuse/exit;
   never attach to a PID merely named qemu. After the strict initial map,
   sample only its fixed128 required vCPU TID/start/labels as specified above;
   incidental task lifetime/coverage is not part of later samples. Target two-second sampling
   intervals and record actual sample times/gaps; this is not a hard
   real-time guarantee. Retain 256 owned threads and 64 MiB caps. The
   3600-second cap uses an earlier wrapper origin as specified below, never
   a later origin that extends the allowance. Stop on exit/ownership loss/
   cap and report gaps. No argv/environment, credentials, unrelated process
   scan, global tracing, privileges or scheduler setting changes.

   Use **one baseline contract**, irrespective of node schedstats settings.
   Remove sysctl and per-TID schedstat reads, including the positive-runtime/
   slices checks. Required data remains the bounded owned stat records:
   PID/PPID/start/thread-count identity, fixed QEMU/vCPU labels and map,
   state, processor field, and nonnegative user/system CPU ticks. Preserve
   `user`, `sys` and `cpu` sample keys. Remove the host `getconf CLK_TCK`
   call, its locals/readiness errors and positive-value validation. Emit
   `CLK_TCK=UNAVAILABLE cpu_units=proc_stat_ticks` in the baseline header;
   update qualification's summary accordingly. The frequency is not queried,
   assumed or needed for this contract. No provider, PATH adjustment,
   fallback, ambient Ruby dependency or replacement clock utility is needed.
   Leave guest `getconf _NPROCESSORS_ONLN` checks untouched. Zero tick
   baselines are legitimate. Compare
   counters only for the same pinned TID/start identity; decreases make
   the affected progress interval unavailable, not evidence of no execution.
   Current helper lines159–164 only compare these raw counters; lines68–72
   cap elapsed runner uptime. The removed lines249–257 only gate and log
   frequency. Qualification line575 only describes that header; ready/map/status
   consumers and workflow completion checks never convert CPU values.
   Raw deltas are tick counts only: no seconds, CPU percentage, resolution
   guarantee or cross-host rate comparison. Pinned proc source establishes
   the fields; it does not establish the actual node's tick frequency.

   Add only the two ordinary `/task/TID/status` fields
   `voluntary_ctxt_switches` and `nonvoluntary_ctxt_switches`, read through
   the already pinned proc directory with a finite 16-KiB input bound and
   identity recheck. Valid nonnegative zero counts are accepted. Missing,
   unreadable, duplicate, malformed or oversized supplemental status data
   yields explicit `UNAVAILABLE` plus a fixed reason, not invented zero and
   not loss of the otherwise valid baseline. Never print the full status
   file. These counts measure switch events, not runnable duration.

   Keep old sample keys `runtime`, `wait` and `slices` explicitly
   `UNAVAILABLE`, with a header explaining that schedstat metrics are not
   collected by this contract; do not opportunistically fill them on a
   node where stats happen to be enabled. CPU ticks are not nanosecond
   schedstat runtime, and switch counts are not replacements for timeslices
   or wait duration. Pinned Linux a238 `fs/proc/array.c:398–403,571–612,642`
   supplies these ordinary fields; `kernel/sched/core.c:6668–6726` updates
   the switch counters independently of dynamic schedstats. In contrast,
   `fs/proc/base.c:514–525` may print `0 0 0` when sched-info accounting is
   off. The actual node kernel/version and proc virtualization remain
   unknown, so readable field shape/identity is checked at runtime.
6. **Host readiness and time association are release conditions.** The job
   must establish the required ordinary proc data, clock
   observations and owned map without changing the runner or node. Missing
   required data/permission/interpreter or ownership fails explicitly before
   stress; no SSH or infrastructure repair fallback. Missing supplemental
   context-switch data does not select another mode. Preserve the existing
   `ready.txt` grammar (`qemu PID START EXE` and exactly 128 `vcpu INDEX TID
   START` rows), guest map, request and completion markers. Ruby does not
   parse sample counters: it still requires status exactly `sampling`;
   the wrapper still requires `^complete:` after join for an otherwise
   successful case. `INCOMPLETE:` remains terminal for missing required
   capture, never the label for deliberately unavailable wait metrics.
   Put baseline capability/units/limits in samples.log and print that scope
   in qualification's evidence summary. No schema negotiation or new API.
   Bind vCPU thread labels to the actual fixed topology and guest CPU/APIC
   identity; equal numeric labels alone do not prove a guest-target mapping.
   If that mapping is unproved, stop the combined evidence package rather
   than assert target starvation.

   **Clock correction within the same three paths:** before spawning sampler
   or test child, the wrapper reads and validates its runner-visible
   `/proc/uptime` and passes that finite value as the helper's fourth internal
   argument. Log it as `origin=wrapper_before_children` with its wall read
   bracket. The helper takes elapsed differences only against subsequent
   readings of its inherited uptime view. This bounds it to 3600 seconds
   including launch preparation, conservatively earlier than the former
   intended launch deadline. The already-corrected cap contains no
   `start_ticks / CLK_TCK` arithmetic; start ticks remain identity tokens.
   Removing the unused frequency gate changes no clock calculation.
   Require valid forward progress across sampling intervals; invalid,
   regressing or stalled clock readings terminate required evidence with
   a specific reason. All reads retain start/end bounds and observed gaps.
   No ambient Ruby dependency is introduced in the Bash wrapper/sampler.

   Pinned `fs/proc/array.c:585–587` applies a time-namespace boottime offset
   to process starts; `fs/proc/uptime.c` similarly offsets kernel uptime,
   and `kernel/time/namespace.c:179–192` shows distinct monotonic/boottime
   offsets. A VPS may have a further proc view such as LXCFS; this is a
   possibility, not an observation of this runner. Neither source nor later
   CLK_TCK=100 proves equal clock bases in the actual job. Label sampler
   values runner-proc-uptime, Ruby values runner-CLOCK_MONOTONIC, and guest
   values guest-uptime/trace-global. Preserve UTC/EPOCHREALTIME observations.
   Add host wall/monotonic send/reply brackets around the existing
   request/ready handshake: the first sampler snapshot is inside that
   observed interval, without assuming equal absolute bases. Keep the
   existing attempt/guest-marker/freeze brackets and their uncertainty.
   Do not directly subtract across domains or assign point timestamps to
   an interval. There is no cross-domain delta tolerance or additional
   forward-jump check: require nonregressing observations within a snapshot/
   command bracket and forward progress across the two-second sampling
   intervals in the required named clock view. Reject malformed/regressing/
   stalled required observations as above. Retain forward wall changes as
   raw uncertainty, without a guessed correction, arbitrary failure threshold
   or inference of descheduling. Missing brackets or associations not
   established by the recorded intervals remain explicitly unavailable;
   do not claim a complete aligned fault window from those relations.
   No generic clock-calibration subsystem.
7. **Preserve error, drain and review boundaries.** Read/freeze evidence
   before existing failed-transition cleanup. Disable/unregister events
   only after acknowledged normal workload drain; unknown effects or drain
   preserve the original failure and explicitly incomplete cleanup until
   ordinary VM teardown. No forced patch reversal or timeout extension.
   Quick controls exercise real helper ordering, attempts/PID markers,
   fault/no-fault observer shutdown, incomplete/lost traces and original
   errors. Add a real-helper success fixture whose representative PATH has
   the already-required standard utilities but no getconf, plus a sentinel
   getconf that fails/records any invocation and must never be called. Do
   not make the whole PATH empty or install a provider. Replace obsolete
   positive/missing/invalid-CLK_TCK expectations with the literal unavailable
   header and absence of CPU time-conversion/frequency claims. Exercise the
   actual qualification summary/ready/status consumer and wrapper EXIT for
   success, existing nonzero failure, cancellation and incomplete required
   host coverage; do not substitute a model of those consumers.
   Actual-helper proc fixtures must accept stats=0 or absent stats
   files, zero CPU/switch baselines, and missing supplemental switch fields
   with explicit unavailable output; prove no schedstat/sysctl reads/writes
   and no numeric substitutes for wait. Reject malformed required stat,
   wrong/reused PID/TID and incomplete/permuted-invalid maps. Keep raw-counter
   zero/increase/decrease and valid permuted-logical-CPU cases.
   Clock fixtures give uptime a different base from process-start ticks,
   prove the cap uses only the pre-child origin, and exercise regression,
   stalled readings, gaps, discontinuous alignment, cancellation and caps.
   Exercise unchanged ready/status parsing and actual EXIT preservation:
   legitimate baseline completion succeeds, missing required host coverage
   rejects nominal success, original nonzero/cancellation wins. Use the
   declared cached Ruby/Bash parse/lint and existing controls/hooks. Reuse
   unchanged common.nix parse/nixfmt/selector receipts with exact source
   binding; do not rerun an unrelated suite. No full Nix evaluation,
   whole-environment build, QEMU launch or VM is required for quick controls.
   The complete committed packet
   gets the root-specified ALL4/HIGH independent review before root may authorize one existing
   exact-head same-profile one-build/one-aged-v5 run. Do not use current
   b361, 9805, 23db or c08 runtime as proof of these new controls.

Runtime success means the unchanged five-event guest CSD/dispatch contract,
actual pre-stress ownership/APIC/TID/baseline readiness, bounded samples with
usable time brackets through the activation window, and unchanged health/
recovery. Missing optional switch counts or deliberately uncollected wait
metrics are declared limitations, not failed baseline collection. CPU-time
or switch-count growth shows thread progress, not a particular guest callback;
state R is a sampled runnable/running state, and the processor field is not
proof of execution at that instant. No tick growth at finite sampling/tick
resolution is not proof of starvation. The baseline cannot quantify runnable
wait or separate host descheduling, blocking/KVM behavior and guest-side
causes by itself. Any future isolated/dedicated-node experiment for that
specific missing evidence needs a separate proposal; it is not a prerequisite
to baseline capture or a reason to enable accounting on production nodes.
A kernel warning or missed activation deadline keeps qualification RED even
with complete evidence. A clean run does not explain old faults. Failure to
capture the required facts returns the precise gap to root; no blind repeat,
automatic broader tracing or four-hour escalation. Primary 645927, frozen
boot/predecessors/current module, 128CPU/16GiB/100000 tasks/300s, watchdogs,
quarantine/recovery and final native+9/original14400 stay unchanged. Any
actual kernel correction requires a separate concrete scope decision.

## Cache, rollback and remaining proof points

Use the already published normal candidate and existing builder/cache ordering.
The small site output is additional test metadata, not a new kernel recipe.
The current builtin-ZFS configuration still has a plain-kernel `dev` dependency;
removing a hash does not remove it. Stop unexpected local kernel compilation
and resolve missing published outputs through the existing cache policy. Any
long/uncertain copy, build or test uses a fresh monitor utility.
The assigned utility may retain exact check artifacts with ordinary owned
indirect GC roots/outlinks during checks, because unrooted copied outputs have
disappeared. This is temporary verification ownership, not permission for a
kernel rebuild or session lifecycle action.

For bounded direct-CLI validation, the lead accepted one exact signed-cache
restore attempt for the frozen boot outputs. If unavailable, the installed
current `nix-store --restore` may unpack the tracked immutable NAR archives
into owned scratch after verifying their existing archive pins. Pass the actual
original FUSE ELF and SDK `vmlinux` explicitly to the resolver. Their immutable
bytes and type metadata, rather than the scratch pathname, are the required
inputs. This validates actual-input parsing/selection; it does not validate
the existing boot archive-helper derivation, its closure, `candidateSites`
realization or runtime behavior. The default wrapper remains on the existing
boot helper and full CI must check that package path. A dry run's old Nix and
util-linux prerequisites do not justify a boot-recipe change, new input pin or
old-Nix source-build project. Keep that packaging limitation explicit in the
check receipt.

Remaining implementation proofs are finite: structured-parser support for the
actual compressed/relocated DWARF, correct semantic/negative selection, FUSE
original-callee identity and reliable-stack behavior, and TCP sample liveness
and reachability. Existing ELF evidence supports each chosen direction but
does not claim those runtime checks passed. If one fails, stop that package and
bring the named constraint to the lead; do not silently change witness strength
or open an unbounded new resolver project.

Rollback is a test-branch revert; there are no new persistent formats, runtime
APIs or coordinated fleet updates. No production deployment or transition
reversal is part of this plan. Quarantine and original recovery rules remain.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
