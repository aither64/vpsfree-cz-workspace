# Ordinary CI against the current livepatch producer

Implementer3 addendum; proposal/source analysis only at clean vpsAdminOS
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`. Session identity and retained
Sol/xhigh settings reverified. No implementation, checks, builds, Git or runtime
mutations. This supersedes the historical-v7 acceptance/input-freeze
recommendation in [fixture-contract.md](fixture-contract.md) for ordinary
development CI, following the user's changed preference. Architect0 owns the
revised design. Existing comments forbidding dynamic candidate checksums record
the former policy; they do not override the new instruction.

## Separate the checks

| Check | Present source | Ordinary-CI disposition |
| --- | --- | --- |
| Historical v7 allowlist | `tests/fixtures/livepatch/default.nix:8-18,29,47-49` | Remove the `573e...` acceptance requirement and its source export. Keep `corrected` linked to the current normal producer. |
| Selected artifact identity | Main `livepatch-6.12.95-common.nix:34-39,476,2154-2163`; perf `:4-11,63-75` | Keep equality to the once-captured current producer digest. It detects wrong artifacts/copies, not historical qualification. Main already supports an environment-supplied expectation; perf checks it in the guest. |
| Direct historical imports | NFS `livepatch-nfs-transition.nix:26,35-39,93`; SCTP `livepatch-sctp-common.nix:30,55-58,144,177`; fragment `livepatch-inet-frag.nix:8,42,110` | Use the same captured current digest instead of importing the fixture's old constant. Require a nonempty valid digest in ordinary mode; keep Nix/guest equality assertions. |
| Exact released predecessors | Fixture `:20-25,51-56`; main `:38-39,477-478`; lifecycle `livepatch-lifecycle/6.12.95.nix` | Preserve exact released-v5 and shipped-v6 archives/digests and both migration variants. These identify historical states under test, not a current-candidate allowlist. |
| Boot identity/ABI | Frozen boot helper/archives; service `os/modules/services/livepatches/default.nix:24-39,365-373`; `livepatch-kernel-identity.nix` | Preserve exact boot bytes, notes/image guard, configuration and symbol CRC compatibility. Removing the v7 digest does not make same-version boot kernels interchangeable. Preserve `dontStrip` and loader/relocation failures. |
| Callback and workload counts | `livepatch-6.12.95/qualification.rb:12-34,197-218`; main runtime assertions | Preserve independent semantic expectations. Compute observations dynamically, not expected callback counts from the candidate or its trace. The comment about 711 CRCs is historical evidence, not a required import-count constant. Validate every actual import against the matching SDK. |

## Small digest/provenance change

The CI build job already produces and uploads the normal package
(`.github/workflows/ci.yml:137-153`). Capture that module's SHA256 once there,
alongside its producer output/derivation identity, and pass it to the dependent
lifecycle rows through ordinary job outputs or the existing artifact. Each row
builds/resolves `corrected`, checks that it selects the same producer artifact,
compares its bytes with that captured digest, and exports the existing
`VPSADMINOS_LIVEPATCH_CORRECTED_SHA256`. All guests verify that value. A local
invocation can build the current fixture first and capture once for that
invocation. Do not hash separately inside each guest or independently recapture
an expectation for each row while claiming the whole matrix tested one artifact.

Log the checkout SHA, clean/dirty source identity, lock/input identity, actual
producer derivation/output and module path, captured SHA256, and resolved guest
artifact. CI checkout/run identity can carry the source reference; retain it
with the existing module/test artifacts. A different selected producer or
guest digest still fails. Do not define `correctedSha256` using Nix
`builtins.hashFile` on an unrealized candidate: that moves building into
evaluation. Capture after realization using the normal build/prepare steps.

The mandatory hash-policy files are the fixture, CI workflow, NFS, SCTP and
fragment tests. Main needs its old policy comments reconciled and a clear
nonempty/format assertion if the common capture contract needs it; its current
hash equality can stay. Perf needs no functional hash change. No normal
producer, kernel helper, root lock, default kernel, predecessor archive or
matrix change is required by this policy. Document current-build testing versus
historical qualification in `docs/os/testing.md`.

## Layout audit: only current-candidate sites must change

All main-suite references below are in
`tests/suite/kernel/livepatch-6.12.95-common.nix`.

| Site | Actual target/use | Required handling |
| --- | --- | --- |
| FUSE `+0x329` | Frozen `fuse` module only (`:3084-3088`) | Retain with frozen boot identity. |
| FUSE `+0x369` | Boot `fuse` and current `fuse_copy_page` (`:3090-3094,3202-3206`) | Split boot and candidate selection. Candidate is the `fuse_copy_finish` call reached after `unlock_request`, not just an arbitrary instruction. |
| SUNRPC gate `+5/+6`, unowned hold `+0xb` | Frozen boot functions (`:2943-2947,2977-2981`) | Retain: production gates themselves depend on this exact frozen boot prologue. No reason to rewrite that architecture. |
| Entry `+5` | Boot/current `svm_vcpu_run` (`:2392-2439`), boot/current `nft_pipapo_insert` (`:3345-3401`), boot/current TLS worker (`:3696-3704,3819-3823`) | Validate the current function's entry/fentry instruction boundary before using a post-fentry hold. Symbol start is not an automatic substitute: an entry kprobe can conflict with ftrace, and the hold trampoline assumes a valid frame/stack position. |
| TCP `+0x7e0` | Current `tcp_write_xmit`, inlined cast-before-add MTU arithmetic (`:3509-3517`) | No reliable source-level function symbol denotes this interior arithmetic site. See bounded alternative below. |
| SUNRPC `+0x1ec` | Current `xs_connect` call to `klp_shadow_alloc` (`:4003-4011`) | Replace with current call-site identification or the existing allocation-failure observation scoped to the SUNRPC shadow ID/path. |
| SUNRPC `+0x56/+0x27` | Current drain calls `cancel_delayed_work_sync`; current release calls `klp_shadow_free` (`:3825-3835`) | Preserve same-worker claim-before-wait and exactly-once release observations, with current call sites or filtered named-callee probes. Named helper entry alone is at a different semantic point. |
| Fragment `+0x22f/+0x3b6` | Frozen native/current target `inet_frag_find` (`livepatch-inet-frag.nix:145-151`) | Keep frozen native offset; replace candidate literal. Retain hash-inserted/lock-held assertions, nonzero hits and zero missed hits. |
| Fragment `timer-56`, `timer+40`; SUNRPC worker `-0x640` | Structure member offsets (`livepatch-inet-frag.nix:65-76`; main `:3864`) | These are data-layout/ABI assumptions, not instruction addresses. Validate against matching headers/DWARF or obtain `offsetof` values from the existing SDK-built test helper. A removed candidate hash cannot certify them. |

The main file also embeds literal offsets in grep assertions; replacing only
the Ruby constants leaves those stale. Parameterize each assertion from its
selected site, retaining mandatory registration/hit checks.

## Bounded witness adaptations

Prefer the existing module-qualified symbol lookup. Stable named entry probes
already cover many witnesses and callback counts. An interior call cannot
generally be replaced with the enclosing function's start: argument registers,
lock state, ownership and trampoline stack assumptions differ. Static helpers
can be inlined/cloned; their names are not a guaranteed compiler interface.

For the finite call sites above, a small per-witness selector may locate the
unique required call in the actual candidate's named function using its ELF
symbols/relocations and instruction boundaries. It must understand the actual
module's livepatch relocation metadata; do not assume plain objdump labels
identify unresolved calls. Require one matching site and validate the callee,
instruction boundary, argument meaning and hold/stack requirements. Bind the
selected site to the captured module digest and log the evidence. Missing or
ambiguous sites fail before installing a probe. This is a bounded selector for
specific calls, not a general disassembly/DWARF service. Its feasibility with
the current candidate is not established by this source-only analysis.

For the fragment witness, the narrow selector is its timer-arm `mod_timer`
call in `inet_frag_find` or an emitted `inet_frag_create`, not a fixed offset
into an assumed inlining layout. Alternatively, a named `mod_timer` entry probe
filtered to that candidate caller range observes the same timer argument
without an instruction offset. It needs precise caller filtering and ABI-valid
queue-member access; unrelated timer calls cannot supply evidence. Preserve
native unlocked/unhashed versus candidate locked/hashed observations and
profile accounting. Packet delivery alone does not prove timer/hash ordering.

Named-callee filtering also fits SUNRPC `cancel_delayed_work_sync` and
`klp_shadow_free`, whose ABI arguments already carry the matched worker and
transport. Scope the former to the drain caller and the latter to callback
release plus the SUNRPC shadow ID. The existing `klp_shadow_alloc` injection
counter is already layout independent, but currently global
(`livepatch_test_probe_main.c:120-160`); constrain its identity if using it to
replace the `xs_connect` call witness. A raw counter increase alone could come
from another subsystem. Preserve the held-worker race and exactly-once
matching-transport release assertions, not merely eventual mount failure.

For TCP there is no comparable named arithmetic site. The smallest explicit
behavioral replacement keeps the preexisting wrapped socket, forced MTU probing,
8 MiB send, bounded completion and kernel-health assertions; use a validated
current replacement entry to prove that implementation ran. Existing
`release_legacy_tcp_socket` checks the sender's 8388608-byte result
(`:1792-1843`), while the receiver discards data. If this becomes the ordinary
behavioral witness, receive and verify the known payload too. This proves the
declared traffic behavior, not that one particular inlined arithmetic
instruction executed. Retain that old exact-instruction witness in an
explicitly historical suite unless a narrowly validated current site can be
selected. The difference must be visible in names/docs/results.

If a call-site adaptation is not small or reliable, explicitly separate the
exact-layout witness into historical coverage bound to its original artifact
and preserve the ordinary current-build behavioral cases. Do not retain old
offsets with a dynamic checksum, silently skip on lookup failure, or claim
behavioral tests prove the removed internal ordering/race property. Separating
the fragment/race witness leaves a specific coverage gap unless an equivalent
current observation replaces it; architect/lead must name that decision.

## Concrete acceptance and remaining decisions

- Quick checks: declared hooks/formatters; inspect the digest flow and all
  `correctedSha256` references; ensure fixture stays linked to normal producer
  and no historical v7 allowlist remains in ordinary preparation. Validate
  absent/malformed current digest rejection and preserve predecessor/boot
  guards. No hidden build during metadata evaluation.
- Identity cases: a changed current producer digest is accepted after capture;
  replacing a guest/module after capture fails; a different producer path or
  source identity cannot be reported as the captured build; every matrix row
  uses the same selected artifact. Corrupt v5/v6 fixtures and mismatched boot
  image/notes still fail. Check every actual import CRC, not an assumed count.
- Selector cases, if implemented: altered prefix/function placement still
  selects the same required operation; missing/duplicate call or wrong digest
  fails; no probe is installed at an unvalidated site. Preserve exact callback
  counts and zero misses. Tests should use representative ELF snippets/files
  for the narrow selectors, not a new compiler-analysis framework.
- Runtime: existing AMD/Intel rows, both predecessor variants, main/perf/TUN/
  SCTP/NFS/fragment behavior, ordinary lifecycle and boot-identity cases. Keep
  failed-transition diagnostics/recovery and native .110 continuity. Verify
  any rewritten witness actually triggers its precondition and rejects its
  negative control. Long checks remain future authorized work.

Open decisions are the finite selector feasibility, whether TCP gets the
explicit behavioral/historical split, and whether each internal race/order
witness can retain its property without expanding scope. Candidate callback
symbols/counts stay tied to current source semantics; if future source changes
those semantics, adjust their independent expectations in the same change.
No proof of current import CRCs, symbol availability, selector correctness or
runtime safety is claimed here.

The proposal changes test acceptance/provenance, not runtime APIs, persistent
formats or normal producer inputs. Historical deployment qualification is a
separate claim; current-build green results do not retroactively qualify old
artifacts or remove quarantine. Existing boot and recovery boundaries remain.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
