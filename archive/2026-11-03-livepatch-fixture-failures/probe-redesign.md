# Current-build probe redesign plan

Implementer3, retained Sol/xhigh. Exact session/environment binding and live
roster reverified. Source worktree remains clean at
`dd188397abe37d0bc33f4c5dfb3605206ce5e326`. This is a source-only plan: no
application edits, tests, builds, copies, Git/pin or runtime mutations.

This plan supersedes the historical-witness separation proposed in
[ordinary-ci-checks.md](ordinary-ci-checks.md). Default CI tests the current
normal producer, with no new historical lane or input freeze. All existing
semantic witnesses remain in its default coverage. Source references below
are relative to the assigned vpsAdminOS worktree.

## Inputs and finite scope

Capture one normal producer module/digest for the run; verify it before resolving
sites and in every guest. Retain exact v5/v6 predecessor bytes, frozen boot
image/notes and all actual import-CRC checks. Provenance/digest work is a
separate package below; a digest authenticates the selected test artifact, not
historical qualification.

Implementer1 owns actual ELF inspection. The lead relayed these scoped findings:
old/current `.text` is byte-identical, all nine queried function address/size
pairs agree, and current SUNRPC allocation/drain and fragment timer calls have
unique relevant relocations. This is not whole-module equivalence or proof for
future builds. FUSE has **two** `fuse_copy_finish` calls: the intended one is in
the `fuse_ref_page` inline context, not `fuse_try_move_page`; its livepatch
relocation namespace is `.klp.sym.fuse`, which ordinary objdump labels omit.
TCP has an observable completed-value comparison in the current artifact.
Reconcile these facts against implementer1's final ELF report during design
acceptance; they were not measured again by implementer3.

Use the architect-selected pyelftools/Capstone host tool for a closed set of
semantic site identifiers. Do not add a generic decoder, instrumentation
framework, execution mode or fallback that omits a witness. Unknown, missing,
ambiguous or incompatible metadata produces a clear failure before probing.

## Per-witness contract and selected replacement

| Witness | Required semantic point | Smallest current-build replacement and evidence |
| --- | --- | --- |
| Nested SVM repair | Current `svm_vcpu_run` before its body changes the vCPU; ABI arg0 is the vCPU. Legacy state must be repaired both after activation and on later entries. | Resolve the actual function symbol and validate its fentry/prologue boundary. Select the first safe preprologue instruction after fentry, preserving arg0 and entry stack shape. Retain bitmap injection, repaired-state checks and hit requirements. A symbol start or arbitrary `+5` is insufficient. |
| NFT batch removal | A batch is inside current `nft_pipapo_insert` before its body proceeds; removal must wait for the held batch, then preserve element state. | Same validated post-fentry/preprologue entry selector. Keep the frozen-boot activation half separate. Preserve exact held-batch completion, transition wait and element assertions. |
| SUNRPC worker ownership race | Hold current `xs_tcp_tls_setup_socket` at a safe entry boundary with ABI arg0 equal to its `work_struct`, before it claims ownership. | Validate current post-fentry/preprologue state. Retain held worker capture, matched callback claim, disable pending while held, release and exactly-once transport cleanup. Named body entry and interior established-frame points are not interchangeable. |
| FUSE finish/abort | In the `fuse_ref_page` path, after `unlock_request` cleared `FR_LOCKED`, before `fuse_copy_finish` changes copy state or publishes a pipe buffer. Preserve the original caller frame for transition/abort observation. | Resolve intended call using inline identity + callee relocation + instruction boundary. Hold at the resolved **original fuse callee's safe entry**, filtered by the exact selected caller return PC. The call has only pushed a return address; its callee body has not run, arg0 is still the copy-state passed from caller R14. Detailed frame contract below. |
| SUNRPC allocation failure | The current connection producer attempts the SUNRPC shadow allocation; injected failure reaches no TLS worker, then ordinary no-agent TLS reaches its expected path. | Keep named `klp_shadow_alloc` injection; use its current call site in the resolved connection producer as the narrow path witness. Retain injected-failure increment and zero worker hits. An unfiltered global allocation count cannot replace the producer witness. A future source change that moves allocation out of the expected inline/caller context requires an explicit selector update. |
| SUNRPC callback claim | At `cancel_delayed_work_sync(&state->transport->connect_worker)`, after `take_work` assigned callback ownership, before waiting for the held worker. | Resolve the unique current call within the drain context. Existing non-holding probe2 observes ABI arg0 = work pointer and matches the held worker. Named `take_work`/drain entry would precede the needed state; a global cancellation probe without caller+worker filtering would accept unrelated activity. |
| SUNRPC callback release | At `klp_shadow_free(transport, SUNRPC_SHADOW_ID, NULL)` in callback release, with that exact transport in ABI arg0. | Resolve the current call in callback-release context; reuse probe3's matching-transport count. Preserve exactly one matching release and zero missed hits. Named `klp_shadow_free` with caller/ID filtering is semantically valid, but resolving the already available unique call is smaller than adding global filter state to this counter. |
| Fragment timer ordering | At timer registration, native queue is unlocked/unhashed; current queue is hash-linked and locked. Nonzero observations, no lost hits. | Resolve current `mod_timer` call in the fragment allocation inline/function context (`inet_frag_find`, or its emitted `inet_frag_create`), with timer in ABI arg0. Existing tracefs observation can remain at this non-holding call boundary. A named `mod_timer` probe is equivalent only with precise candidate-caller filtering; the verified unique call avoids global noise/filter changes. Preserve native frozen offset separately. |
| TCP MTU arithmetic | Execute current `tcp_mtu_probe` size calculation with legacy `reordering == UINT_MAX`; addition must widen before increment and the completed size must exceed UINT_MAX for positive MSS. | Resolve the inline context and completed `size_needed` comparison, not function entry or old count-only `+0x7e0`. Use tracefs fetchargs for validated live GPR values; capture needed as u64, reordering/MSS at their validated widths. Require selected sender context, nonzero/miss-free samples and the independent bound below. Preserve traffic and add actual receiver integrity. |

The finite current entry selectors are SVM, NFT and TLS worker; interior
observation selectors are the FUSE call, SUNRPC allocation/claim/release,
fragment timer and TCP size comparison. No other site expansion is proposed.

## FUSE: eliminate the unsafe interior-to-entry assumption

The current FUSE test uses schedulable `probe_hold`, **not** `probe_spin_hold`.
The latter is used by a different SUNRPC test around main-suite line 4171.
Implementer1 reports an established FUSE frame at the intended call: entry RSP
delta `0x68`, changed modulo-16 state, RBP established, copy-state passed R14 to
RDI. A unique call address does not certify a safe redirection through an
entry-oriented save/call sequence. Do not reuse that interior redirect merely
because old/current text is equal.

Instead, resolve the callee from the actual `.klp.sym.fuse` relocation,
including symbol position/namespace; do not look for an assumed candidate
`livepatch_7:fuse_copy_finish`. Select its validated safe entry or post-fentry
**preprologue** point. If fentry is present, choose after it and verify the
original entry stack/arg0 state still holds. Verify no ftrace redirection
conflict. Filter before counting, capturing or holding by the exact caller
return address: runtime caller symbol address + selected call offset + decoded
instruction length. This also disambiguates the other finish call.

Extend the existing probe helper with one optional expected-caller-return
predicate, read safely from the validated entry stack. Unrelated callers must
not count, capture arguments, claim the one hold slot or sleep. Keep the current
resume-task guard and restore/reset handling. The normal entry trampoline saves
and restores all registers/flags, resumes the original instruction and publishes
its ORC synthetic target marker; preserve those properties. The original
`fuse_copy_page` frame remains below the callee frame and must be visible to
the reliable unwinder during the hold. At this entry-equivalent point RDI is
the same copy-state and finish has performed no body side effects.

This is a narrow alternative to a second interior-alignment trampoline path.
No `.S` change is planned. If the selected build lacks a safe, nonconflicting
callee entry or cannot retain the required caller frame/state, fail the FUSE
descriptor. Do not substitute an interior redirect, a spin hold, a generic
function-entry hit, or a skipped case. Runtime acceptance below must prove the
entry-based hold preserves the original semantic witness; this source plan
does not claim that runtime proof has already passed.

## TCP: concrete regression and content proof

The production patch changes `size_needed` from int to u64 and casts
`tp->reordering` before adding one. In the original function, queue-size/window
comparisons consume that value before allocating an MTU probe. Existing traffic
creates a socket before activation with `tcp_reordering=-1`, enables MTU probing,
then sends 8 MiB, but the old internal probe asserts only a hit and the receiver
writes to `/dev/null` (`main:1792-1843,3505-3538`).

Use the current-ELF comparison selector with finite register enums. Lead-relayed
current evidence has the completed u64 in RAX at a comparison currently at
`+0x7f9`: zero-extension of reordering, 64-bit add-one/multiply and addition of
the sign-extended probe size precede it. This is evidence to validate, not a
new RAX/offset constant. Match inline `tcp_mtu_probe` plus operation/dataflow
and operand widths, requiring a unique comparison site. DWARF/source line
alone is insufficient. If necessary source variables are unavailable or the
pattern is unsupported, report that exact unsupported condition and fail.

Use existing tracefs register fetchargs rather than a general C register
reader. Filter to the known single sender PID/socket workload; capture
`size_needed:u64`, `reordering:u32` and `mss:u32` from validated live locations.
Prefer live GPR operands over introducing socket field offsets. If a socket
pointer is needed for disambiguation, its location and field reads must also be
validated, never guessed from a prior build. Assert at least one matching sample
with reordering equal to UINT_MAX, MSS greater than zero, and size_needed greater
than UINT_MAX. That bound is independent of the implementation formula and
catches the legacy wrap-before-multiply case. Missing samples fail the
precondition; a normal `tcp_write_xmit` entry hit is not a substitute.

Change the controlled receiver to store the stream and publish EOF/completion
status. Verify its exit, exact 8 MiB length and byte-for-byte contents against
the known sender payload, in addition to the existing sender result/deadline.
The present all-zero payload is sufficient when checked completely; no new
network protocol or receiver framework is necessary. Wait for receiver
completion, not merely for client `send()` success. Wrong, truncated or
duplicated bytes must fail even if the sender reports 8388608 bytes.

The traffic assertion and arithmetic observation prove different things; keep
both. This plan does not replace arithmetic/race proof with behavioral success.

## Minimal resolver output contract

Inputs: selected module file, independently captured run digest, source/input
identity reference, and required fixed SDK/boot metadata. Verify digest before
decoding. Emit one JSON object with schema version, exact module digest,
module/ELF identity, source reference and the finite semantic site map above.
Each site records symbol/module namespace and position, inline/caller context,
decoded offset/length or safe named-entry selector, callee identity where
relevant, required GPR enums/widths and frame-kind predicates. FUSE additionally
records exact caller-return construction and resolved original callee identity.
Include compact selection evidence for diagnostics. No addresses from one
loaded guest belong in this host descriptor.

The consumer verifies digest/site completeness and resolves runtime bases by
module-qualified symbols; duplicate/absent symbols or contradictory contexts
fail. Allow only known read-only observation and validated entry-hold shapes.
Decoder output must never authorize a new arbitrary hold or register program.
Data offsets (`inet_frag_queue` timer/node/lock; `sock_xprt.connect_worker`) are
separate ABI records validated against matching SDK/candidate types, not text
offsets. Keep immutable boot call/gate offsets and their identity contract
separate; do not retarget production gates or rebuild the boot kernel.

## Actionable packages and file ownership

| Package | Files and boundary | Dependencies / quick acceptance |
| --- | --- | --- |
| A — current producer identity | `tests/fixtures/livepatch/default.nix`, `.github/workflows/ci.yml`, `livepatch-nfs-transition.nix`, `livepatch-sctp-common.nix` | Remove only historical v7 allowlist; capture current normal module digest once; pass producer/source identity and digest to all rows. Preserve predecessor pins, existing env interface and fixture-to-normal linkage. Quick checks cover missing/malformed digest, mismatch and unchanged predecessor/boot policy. Workflow invokes B after realization; C owns fragment/common changes. |
| B — finite host resolver | New `tests/fixtures/livepatch/probe-sites.py`, `probe-sites.nix`; narrow export from fixture default serialized with A; focused resolver test file beside helper | Architect-selected pyelftools/Capstone packaged in the declared Nix environment. Implementer1 ELF report supplies evidence, not hardcoded results. Parser/selection tests cover real livepatch relocations, inline ambiguity, entry frames, widths and failure diagnostics. No OS producer or root lock changes. |
| C — runtime witnesses and technical docs | `livepatch-6.12.95-common.nix`, `livepatch-inet-frag.nix`, `livepatch-6.12.95/livepatch_test_probe_main.c`, `docs/os/testing.md`; focused existing runner-spec extensions where useful | Consume A/B; replace literals and stale grep offsets, implement FUSE exact-return filter, keep simple counters, add TCP tracefs value/content assertions. Existing `.S`/header contract is inspected and retained. No generic register-reader API or historical discovery mode. Validate helper filters/descriptor failures and Ruby/Nix syntax; compile the small SDK-backed helper as an appropriate quick check if bounded. Long operations use watchers. |

These are responsibility boundaries, not authorization to assign new members.
Lead serializes shared fixture/workflow edits and Git operations; parallel work
can develop B's new files while A/C consume its settled contract. Assemble and
check the complete branch before final independent review. Technical docs state
current-build acceptance and actual witness properties, with lead-owned final
user-facing wording as applicable.

## Positive and negative acceptance

- Resolver: changed function placement/prefix without semantic change selects
  the intended site; wrong module digest, missing inline context, wrong callee,
  duplicate valid call, unsupported widths or unsafe frame fails clearly.
  FUSE's other finish call must not be accepted for `fuse_ref_page`. Mutating
  the TCP cast/type in a disposable current-source candidate must fail semantic
  selection or the observed wide-value property, after normal digest capture;
  this cannot be rejected solely by a historical checksum.
- FUSE: hold only the selected caller, observe correct copy-state and unlocked
  request before finish, show original caller in reliable stack evidence, and
  pass existing transition/abort/close expectations. Wrong return PC/namespace
  or unrelated finish traffic cannot satisfy the hold precondition. Zero hits,
  missed hits or lost caller visibility fail. No interior redirect is tested
  under an assumed entry contract.
- SVM/NFT/TLS entry holds: validate site, args and stack shape, observe the
  existing repair/batch/ownership assertions, and release/resume exactly once.
  A prologue-shifted or ftrace-conflicted entry descriptor is rejected before
  installing the hold; a wrong-worker match cannot count as callback claim.
- SUNRPC: preserve failed-allocation/no-worker then no-agent path, callback
  ownership before waiting, pending disable while worker held and exactly one
  matching transport release. Wrong caller/transport/shadow context and dropped
  events cannot satisfy these checks. Keep independent callback counts.
- Fragment: retain native unlocked/unhashed and current locked/hashed samples
  at actual timer registration, nonzero hits and zero misses. A wrong call site
  or deliberately invalid member-layout descriptor fails rather than reading
  unrelated memory; a sample showing unlocked/unhashed current state fails.
- TCP: require wrapped legacy precondition, actual comparison samples and wide
  bound; an event with wrapped needed value fails. Verify receiver EOF, length
  and content; corruption/truncation and a sender-only success report fail.
- Identity/recovery: current digest movement is allowed after capture; wrong
  copy after capture fails. Exact predecessor and boot mismatches remain fatal.
  Preserve failure evidence, no forced transition reversal and native .110
  continuity.

Run each package's relevant quick checks and consolidate all intended changes
into commits. Then mandatory independent final review of the complete branch,
including history/migration conclusion, precedes long checks. Long acceptance
is the existing current-build AMD/Intel matrix with both predecessor variants,
ordinary lifecycle/kernel-identity and all main/perf/TUN/SCTP/NFS/fragment
coverage. Run focused positive/negative witness controls before repeating the
full matrix. No test run is authorized or claimed by this planning report.

No normal-package implementation, persisted format, API or fleet-wide update
changes are planned. Remaining implementation gates are exact resolver/frame
validation against implementer1 evidence and the required runtime acceptance,
especially FUSE reliable-stack preservation and TCP sample reachability. An
unsupported build fails with the named witness/constraint; it does not change
the plan into historical coverage or silently discard proof.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/>
