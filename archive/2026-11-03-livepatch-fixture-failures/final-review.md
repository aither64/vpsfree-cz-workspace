# Final independent review

Reviewed range: vpsfreecz/vpsadminos dd188397abe37d0bc33f4c5dfb3605206ce5e326 -> 4fc0f375de34f92dd59aef94080e874b302c720c.
Reviewer: reviewer0, retained gpt-6.1-sol / xhigh, review purpose, read_only. General, architecture/repetition, scope/proportionality and risk/compatibility lanes.
Disposition: two Important findings; no Blocking findings. Reconcile both before proceeding under the mandatory-review gate.

## Findings, ordered by severity

### Important R1 — Partial-register zeroing is accepted as a NULL pointer
Commit 4fc0f375; tests/fixtures/livepatch/probe-sites.py:83-98 and :426-428.

The sunrpc_callback_release selector certifies that the klp_shadow_free destructor is NULL using zero(..., "rdx"). Both immediate() and zero() normalize subregister names without checking operand width. Consequently xor dl,dl, xor dx,dx, mov dl,0 and mov dx,0 all satisfy this predicate, although the upper RDX bits survive and the pointer need not be NULL. For example, RDX=0x10000 remains nonzero after xor dx,dx. The site is therefore certified under a semantic condition that was not established. This contradicts the declared rejection of unsupported register widths and can misqualify a changed callback-release sequence.

Read-only reproduction against the committed resolver, using its already-built Python/Capstone environment, returned:
- xor dl, dl: zero(rdx)=True, width=8
- xor dx, dx: zero(rdx)=True, width=16
- mov dl, 0: zero(rdx)=True, width=8
- mov dx, 0: zero(rdx)=True, width=16
The legitimate xor edx,edx and xor rdx,rdx also return True.

Smallest fix: accept only definitions that establish the complete pointer value, such as 32-bit zero-extending or 64-bit MOV/XOR zeroing. Add focused negative controls beside the existing call-site fixtures for 8/16-bit definitions, retaining positive 32/64-bit controls. No general register/dataflow framework is needed.

### Important R2 — Consumers reject a fragment symbol the resolver intentionally supports
Commit 4fc0f375; tests/fixtures/livepatch/probe-sites.py:434-459; tests/suite/kernel/livepatch-6.12.95-common.nix:820,833-839; tests/suite/kernel/livepatch-inet-frag.nix:70.

Resolver.fragment() searches both inet_frag_find and a separately emitted inet_frag_create, and emits the actual owning function as the record symbol. Both runtime validators insist on inet_frag_find. If the compiler emits the explicitly supported standalone inet_frag_create, host resolution succeeds but the main suite and fragment suite reject the resulting valid finite record before running. This is the allocation inline/function alternative described in probe-redesign.md and the implementation brief; it is not an arbitrary-function request.

Read-only reproduction extracted the actual committed consumer methods, loaded the actual B sites.json and changed only inet_frag_timer.symbol to the resolver's alternate supported name. Both validators accept the original record; common rejects the alternate with "invalid livepatch site contract: inet_frag_timer", and fragment rejects it with "invalid current fragment timer site or structure ABI".

Smallest fix: align both consumers with the two explicitly supported owning symbols and retain all existing namespace, kind, frame, ABI, callee and bounds validation. Add one positive out-of-line fixture and exercise its emitted record through both consumers. If the lead instead chooses to exclude this already documented alternative, remove the resolver's unused acceptance path and explicitly reconcile that supported-boundary decision; do not leave producer and consumers contradictory.

## Readiness and verification limits

The committed deliverable has received final independent review; this is not runtime qualification or merge readiness. Both Important findings require a fix or an explicit recorded decision under the skill before continuing. The narrow fixes described above remain within the reviewed design; focused lead inspection and checks can reconcile them under the skill's narrow-remediation rule.

The packet's quick-check evidence is useful within its declared scope: 21 resolver controls, 26 consumer examples, actual all-nine parsing/selection against the current module plus immutable SDK/original FUSE, helper compilation and import-CRC checks, and hooks. I inspected all 16 changed files, the complete final diff, the commit message/parentage, relevant surrounding helper/trampoline/runtime code, and the requested design/evidence records. I independently ran git diff --check, the in-memory zero-width reproduction and actual-consumer alternate-symbol reproduction. No source/session file was written and no long check, build, VM, retry, fetch, push, merge or deployment was launched.

candidateSites package realization remains unverified locally. The successful direct CLI run used verified immutable archive bytes restored with installed Nix; it does not establish the unchanged archive-helper derivation/old-Nix closure or the candidateSites wrapper's complete realization. Preserve this as a separate required packaging result, not a passing package claim. The approximately nine-minute first-generation DWARF cost is explicit and incurred once per candidate derivation; optimization is optional follow-up.

Focused live acceptance is still required for the original FUSE callee, exact caller filtering before count/capture/hold, safe stack/reliable-unwind behavior, correct unlocked copy-state and release/resume; also TCP comparison reachability for the intended sender with UINT_MAX reordering, a positive MSS, a wide completed result, loss-free tracing and receiver EOF/length/content. The existing callback, race, boot/predecessor identity, health, scale/profile, recovery and complete matrix requirements remain. Static ELF and stubbed host consumers do not replace them.

## Scope and architecture assessment

The actual outcome relayed by the packet is current normal-package qualification after the user rejected an input freeze and historical-offset lane, then authorized implementation. The final 16-file +2056/-180 diff is substantial for the original fixture failure, but the added mechanisms correspond to the nine retained semantic witnesses, one digest-bound internal record, a narrow existing-helper return-PC predicate, receiver proof and independent controls. I found no generic instrumentation/review-state framework, production input change or unrelated subsystem. Replacing these witnesses with entry hits or weakening them would not satisfy the accepted scope.

The records span investigation, withdrawn proposals, design and implementation; they do not provide an authoritative non-overlapping active-time total. Delivered milestones are concrete (current ELF evidence, finite contracts, committed resolver/consumers and quick checks). The smallest completion path is the two bounded corrections, existing packaging/focused runtime acceptance, then the established matrix. No extra framework or optional hardening is recommended.

The finite resolver appropriately delegates ELF/DWARF parsing and instruction decoding to pyelftools/Capstone. The internal record has actual consumers in the two tests and CI preparation. Independent fixture labels provide an oracle separate from selector offsets. The FUSE change keeps the existing trampoline and compares the caller return PC before injection/count/capture/hold; TCP preserves the arithmetic witness and adds complete receiver checks. No external test-runner public interface or production mixed-version contract changes.

## Whole-branch history, repeated streams and migrations

Independently verified HEAD=4fc0f375de34f92dd59aef94080e874b302c720c, HEAD^ and merge base with the supplied baseline both equal dd188397abe37d0bc33f4c5dfb3605206ce5e326. The complete range contains exactly one commit: "tests/livepatch: qualify current module probe sites". Worktree/index/nonignored-untracked status was clean at the end of review.

The resolver, identity transport, consumers, controls and documentation implement one bounded internal test contract; this single feature commit is coherent. There are no fixup/tidy commits, retained obsolete branch approaches or transitional compatibility implementations in the reviewed series. Withdrawn freeze/historical-lane proposals remain historical session context, not shipped source.

No repeated dependency, channel, input, pin, lockfile, Bundix or generated-update streams exist in the range. There are no superseded update commits requiring consolidation.

No migrations. No database schema or production persisted format/protocol change, transitional migration, deployed intermediate or externally consumed intermediate schema is introduced. Migration lineage has no steps to consolidate. Production producer/kernel inputs, fixed boot and released predecessor identities remain separate; no coordinated node update is required by this test-only change. No integration approval exists for vpsadminos/staging.

## Identity and handoff

Both DEV_SESSION_SLUG and DEV_SESSION_WORKSPACE were absent. The trusted thread-bound developer instruction explicitly binds this reviewer to session 2026-11-03-livepatch-fixture-failures and workspace /home/aither/workspace/ai/vpsfree.cz. dev-session current from the assigned tracking directory matched that exact slug. (An initial call from the workspace root returned no current session; the intended-directory call resolved it before any session files were read.) Fresh live roster confirmed reviewer0, thread 01a1a24e-920c-7b82-9fff-7754d1f947ab, gpt-6.1-sol/xhigh, review/read_only, ready. No nested reviewers or setting changes were used.

Report delivered read-only via report_to_lead for the lead to save as work/2026-11-03-livepatch-fixture-failures/final-review.md and link from state. Session remains open.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/

