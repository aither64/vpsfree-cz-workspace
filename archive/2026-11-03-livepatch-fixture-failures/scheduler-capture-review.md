# Scheduler counter capture and one-case execution: combined committed review

## Findings and disposition

**No new Blocking, Important or Advisory findings.**

Exact **13b658f67c37418d6bbf91316ea7b3c6db99fe17** passes this combined affected committed review for the separately released **one-case diagnostic execution** in the packet. This does not establish successful probe registration, valid guest fetches, incident cause, corrected scheduler behavior, full qualification, staging readiness or production kernel approval.

Complete evidence range: **2951a632c4254a44747a8da326e3dde897eaa0e2..13b658f67c37418d6bbf91316ea7b3c6db99fe17**. New affected range: **bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf..13b658f67c37418d6bbf91316ea7b3c6db99fe17**. All four lanes: general, architecture/repetition, scope/proportionality, risk/compatibility. Overall **HIGH** risk because kernel observation, host behavior and CI coverage selection are involved.

## Scope and proportionality

The actual new diff is exactly two paths, **+136/-34**:
- qualification.rb: **+134/-1**, finite observation around the existing failing pre-transition hotplug.
- ci.yml: **+2/-33**, temporary native-job suppression and retention of one existing lifecycle matrix entry.

The user authorized current-normal-module qualification and shorter aging during diagnosis. The accepted package investigates the new, recorded CPU127 predecessor warning while preserving its failure. It does not authorize a scheduler fix, lower workload, changed frozen kernel/predecessor, warning exemption or broad instrumentation system.

The implementation fits that boundary. A single caller-site kprobe with one owned trace instance is proportionate to the missing runqueue evidence. It avoids a globally hot dl_server_stop handler and stack-based caller inference. A finite field declaration is authoritative for this exact notes-bound layout, rather than a new resolver/schema. The workflow change uses the existing build and lifecycle job; it adds no workflow, dispatch input, native-tag escape hatch or campaign machinery.

Existing dispatch cannot select lifecycle alone: a nonempty native pattern skips capture/lifecycle; empty pattern ordinarily schedules native plus nine. Narrowing the existing workflow on diagnostic ancestry is a bounded execution dependency, separate from observation.

## Capture site, frozen identity and field safety

**qualification.rb:12-23,302-309** binds the capture to frozen notes and predecessor release before deriving the native base plus0xc3. I traced the reused symbol_address implementation (**common.nix:939-968**): validated name, native NF3 only, U/u imports excluded, exactly one result and a nonzero hexadecimal address. No module/import ambiguity or new resolver path was introduced.

I directly inspected pinned Linux source a2384967b90f24d2470c9eb15f0e66d938df7e08 and the retained immutable ELF/BTF, rather than relying only on the packet:
- Source sched_cpu_dying takes rq_lock_irqsave, checks nr_running/pinned state, dumps tasks on warning, calls dl_server_stop and then unlocks. Pinned deadline.c dequeues the entity in dl_server_stop.
- Frozen disassembly confirms RBX is rq; the LEA at **+0xbc** loads **RDI=rq+0x968**; the five-byte CALL at **+0xc3**, address **ffffffff810ed123**, targets dl_server_stop. The warning cold path rejoins at+0xbc; unlock follows the call. The observation is before the CALL executes, under the same locked pre-dequeue boundary.
- I checked the retained493-byte caller extent, all182 static blacklist pointers for an entry inside that caller, and the selected point against entry/noinstr/kprobes excluded ranges. The selected instruction is within the function and outside those ranges. C's completed symbol/blacklist receipt also covers caller/callee uniqueness and the whole caller range. Static eligibility is not a claim that runtime registration has succeeded.
- I rehashed frozen vmlinux **6e63a63c8fd2fbaa92a51fd5bbcbd002909b33e0fa70ba77163075ab2014c5ab** and bzImage **3265b29d00581f09f9f171342c24cc8c6872ac679aca01f5e3fdb33d7850c541**. Direct ELF section reading confirms the84-byte notes equal the retained notes.bin and hash **1e4432629c0f1a1e9c6b175495217859279f98ded2beca091834ec059e42108a**, matching the guest guard.
- Direct BTF inspection confirms all declared offsets and widths: rq/entity sizes3520/240, embedded fair_server2408, entity.rq216, raw parent/color0, counts and CPU/online fields. The unsigned32 bitfield container at84 matches server4/active5/defer6/armed7/running8/throttled0.

The feasibility proof.json's callee-site field is historical. The later caller receipt and direct disassembly establish current+0xc3; no $stack0/return-PC filter remains.

**qualification.rb:263-293** requires the exact caller+offset, CPU127 header, positive timestamp, complete unique field set, nonzero entity/runqueue pointers, entity_rq==rq, server==rq+2408, matching rq_cpu, valid online value and server flag. Raw parent/color is retained and queue membership is decoded using the pinned RB_EMPTY_NODE contract at entity offset0; active alone is not presented as membership. Class and pinned counters remain observations, not a synthetic sum or userspace scheduler model.

The displayed /0x... span is checked only as well-formed hexadecimal presentation. It does not select, authorize or bound the address/reads. This is correct for kallsyms' next-nonalias span rather than ELF st_size. Rounded0x1f0 and alternative0x200 are positive host fixtures, not measured guest results. Static bounds, notes, instruction, native-base, CPU and entity guards remain independent of presentation.

## Trace ownership, failure semantics and capture completeness

**qualification.rb:296-375** refuses an existing named global event and creates a new owned instance. It uses:
- 64KiB **per CPU**, not a claim of64KiB total allocation;
- monotonic clock, overwrite disabled and the mask selecting CPU127;
- the exact caller instruction and rq_cpu==127 filter;
- ten-second bounds on each diagnostic guest operation.

Tracefs writes install the temporary observation. Fetches do not redirect execution, dequeue entities or write scheduler fields.

The wrapper is selected only for **AMD/v5/128CPU/16384MiB/100000tasks pre-transition** (**qualification.rb:627-633**). The original hotplug body remains unchanged (**245-260**): offline and verify, online and verify128, workload progress, then cumulative health using the original example baseline. Post-transition and other profiles retain their original call. No health reset, warning exception, watchdog change or workload reduction accompanies the capture.

Capture runs in ensure on success or failure. It first stops tracing, prints the raw trace, requires complete bound records, prints CPU127 stats and requires all three loss counters present/zero. It then prints probe hits/misses, requiring a present profile, hits sufficient for retained rows and zero misses. Missing record/fields, malformed identity, loss, misses or unsupported setup are explicit diagnostic incompleteness.

Cleanup attempts only resources whose creation succeeded: stop owned tracing, disable/delete the owned event, remove the owned instance. Each cleanup attempt is bounded and failures are retained. If the hotplug/health operation already raised, capture/cleanup StandardErrors are logged as INCOMPLETE and do not replace its original exception. If the operation otherwise succeeded, incomplete capture/cleanup raises, preventing apparent diagnostic success.

I traced machine.succeeds through OsVm::Shell and its StandardError-derived command/timeout/kernel errors. Existing assert_kernel_healthy remains outside the capture-error rescue and is not converted to success. Its RSpec expectation failure is retained through the ensure path. The wrapper does not alter normal group/workload teardown. A fatally unresponsive guest can still prevent fetch/cleanup; that is incomplete evidence and the existing runtime/teardown contract remains necessary.

A valid trace may accompany a RED qualification. Conversely, a probe hit or green nonrecurrence is insufficient to explain the old warning. A record showing a queued synthetic server and class/pinned counts supports the corresponding snapshot interpretation; it does not alone establish the initiating historical cause or justify ignoring the warning.

## Workflow selection, identity and resource contracts

**ci.yml:215-217** adds the explicitly temporary native test-job if:false. The lifecycle job still depends on **build only**, so skipping native does not remove its prerequisite or source/producer capture. **ci.yml:406-416** retains exactly the original entry:
vendoramd, runneramd-livepatch, labelamd-scale-aged-v5, taglivepatch-qualification-amd-scale-aged-v5, largetrue.

I reviewed A's full Psych/AST checks and independently reconstructed the pre-change workflow bytes by removing the two inserted lines and restoring the old matrix. The result is byte-for-byte equal to03aee's workflow. Thus build/capture/cache outputs, conditions, lifecycle body, env/opt-in, timeouts, uploads, result evaluation and cleanup are unchanged outside the two intended changes.

The empty-pattern ci route still enables normal capture and lifecycle. The build captures source/lock/producer/module/SHA/sites once; the row checks CAPTURED_* identities against its checkout, actual module and sites, and transfers the same artifact to its guest. VPSADMINOS_ENABLE_LIVEPATCH_TEST remains1 and overriding single-series/example filters remain unset.

The retained row still uses one test job, --fresh/--jobs1, --max-cpus128 and the existing ceiling CPU-overcommit calculation. Memory admission is unchanged. The selected profile stays128vCPU/16384MiB/100000tasks/300s. This is guest CPU oversubscription, not a claim of128 physical CPUs. Actual next-run selection must still prove exactly the expected one instance/default script; static selection is not an executed selection receipt.

Existing *.log/*.txt/sites artifact handling retains trace/stats/profile and console/shell/results. Evaluation propagates body failure; upload success does not make qualification pass. Cleanup/result handling is unchanged.

A's dated official receipts bind unchanged checkout@v7/latestv7.0.1 and upload-artifact@v7/latestv7.0.2 refs, including transitive upload. I read those receipts/local source without network checks. actionlint is unavailable; Psych/structural checks, exact byte preservation and normal hooks adequately cover this narrow change.

## Quick evidence and its limits

C's final source hash is **b3a3b1e8d41b36f9380ef5697c54423eadd0f0bd9385cbfef255ab992716f608**. Workflow hash is **8b53efb017ec324f8dc363d31ccef3eaaa9e28a4725989190066585ff9137782**. I independently matched both files to committed blobs.

The actual-method inspector records **20 passing controls** covering complete/invalid records, queue-versus-active, spans, identity/fields, ownership, original errors and miss/loss refusal. It stubs guest I/O; it does not model rq accounting or prove registration/guest cleanup. I inspected source/results without rerunning it.

Old f412 fails the legitimate rounded-span regression as intended; the caused+3/-1 correction is folded into03aee. Earlier17-green output and old source hash remain historical. Final Ruby parse/declared RuboCop/whitespace and corrected ordinary hooks pass; A's normal workflow hooks also pass. No bypass or new environment installation is claimed. The absolute primary Gemfile/ignored-lock/bundle binding remains explicit; no diagnostic lock or gem tree was copied.

These quick checks are adequate to proceed to the separately released first runtime observation. They do **not** prove first registration, accepted fetch syntax/values, actual hit, complete guest records, zero loss/misses or actual kernel cleanup. Those remain exact runtime conditions. Prior source/unit/ELF/module/runner receipts retain their actual component/input scope; no old whole-guest closure identity or new-head runtime pass is inferred. The full osctld unit suite remains unavailable before examples as previously recorded.

## Complete evidence history, provenance and migrations

I independently verified the six-commit chain and complete inventory:

1. 8169b8189c29f471b2ecf27a33b6f71dbde5e70e — current-module qualification.
2. e1751c917f216897292ab0b893727a6e5553a540 — bounded OSVM boot evidence.
3. 645927e22809a29c67ffd59c072e553e05e2a72b — coalesced production shutdown.
4. bda1f5d0d5dc302ff9b3002b9e9b20ee801553cf — temporary300s age.
5. 03aee94936c6693371b08e61a904d66a4be9e4da — finite dying-runqueue observation.
6. 13b658f67c37418d6bbf91316ea7b3c6db99fe17 — one-case diagnostic execution.

Exact parents are13b->03aee->bda1; merge base is2951. Complete range: **26 paths, +3775/-272**. Of the parent's25 feature paths, **24 unaffected modes/blobs are exact**; the already-feature-owned workflow is the affected parent path, and qualification.rb is the new26th path. Prior four objects/messages and patch IDs remain unchanged.

Independent new patch IDs: **3a75602ca12dec390ae632a4021fbb5900cc652c** (observation), **6387060d6947849d323842ae543dabb6443aba62** (execution). Message hashes match receipts; messages explain final behavior/boundary within80 columns.

The old unpublished **f41262be6759876709c35677b847da1f6ba53eec** is retained at the named local provenance ref and is **not an ancestor of13b**. Its formatter repair is in the owning03aee, not a fixup commit. The abandoned global callee/stack-filter design is feasibility history only, not committed current behavior. **No obsolete implementation, fixup/WIP, intentional-red prototype or transitional compatibility path remains in the reviewed six-purpose evidence series.**

**No repeated dependency/channel/input/pin/generated-update streams exist.** Canonical rake-compiler baseline2951 is not a feature update stream. Observation and execution are distinct active diagnostic purposes, not redundant repins.

**No migrations.** No new schema/database/on-disk/protocol transition, unapplied intermediate migration, or migration merge/release/deployment/external-consumption provenance exists.

Primary delivery remains exact **645927**, clean, with original14400 profile SHA **367dd4ce864b36c4807cb974857d7b58e22b18bb51343ad2724757132da12f2f**. Diagnostic profile remains SHA **2fb34cb01efc54b9ec0fa96af20805bbe49bb986c977e5ad86e0b374244411d3**. Both checkouts/indexes/nonignored-untracked states are clean. Complete-range whitespace passes. Registration still names only the primary delivery feature.

The three temporary age/observation/execution commits are outside primary delivery ancestry and **must remain outside final shipping ancestry**. Do not merge/cherry-pick them and add reverts. Retain diagnostic refs/results separately. This is a coherent six-purpose evidence history, not a staging-ready six-purpose shipping history. I reuse diagnostic-300s-review.md and shutdown/prefix reviews for the unaffected implementation, without a full unrelated source re-audit.

## Runtime conditions, remaining gates and completion

The retained old-bda1 case failed before candidate activation: CPU127 sched_cpu_dying warning/nr_running2, with only the stopper task printed; offline/online/progress returned. That is a kernel-health failure, distinct from old5235 loader/CSD evidence. Fair-server queue accounting is a source-backed hypothesis, not an observed incident state or proven cause. No helper misuse, harmless-warning, resource/flakiness or production-kernel correction claim follows.

After root reconciliation of the existing old run/sole utility slot, the next separately released execution must bind exact13b and prove:
- the expected build plus **one AMD aged-v5 lifecycle job**, native skipped, actual[1/1] qualification instance/default;
- normal captured source/module/sites/guest inputs, frozen kernel notes, v5 predecessor, declared resources and300s profile;
- successful actual registration, bound CPU127 pre-CALL records with every required field, zero ring losses/probe misses and retained raw trace/stats/profile;
- original hotplug/health result and normal teardown/recovery, including a RED result if the warning recurs.

Publication itself may launch CI. Bind an actual eligible exact-head push run, otherwise one existing empty-pattern dispatch only after exact-ref/no-duplicate reconciliation. No automatic retry, full-matrix or14400 escalation, health waiver or inferred permission to cancel the old run follows from this review.

A clean run narrows neither the earlier initiating cause nor four-hour stability. A useful complete RED capture is diagnostic progress, not qualification. The current failed case and other old failures remain unwaived.

Final shipping preparation must return to retained production lineage, excluding **all three** diagnostic commits, with original14400/comment absent and full original workflow. Preserve tested645927; remove only its isolated skip directive through the separately released normal-hooked message-only path; prove final tree/patch/message/history equivalence. Then qualify the actual final head with **full native plus all nine rows at14400**, complete semantic/identity/health/recovery proof and ordinary integration checks under applicable conditional user approval. Old, focused, short or one-case results cannot substitute. No coordinated fleet update, deployment, merge claim or lifecycle action is approved here.

Comments/tests explain layout, presentation and cleanup; temporary execution stays in session records. No public API/protocol/manual change or fleet coordination is needed. Rollback returns to retained source/evidence, without writing scheduler state or relabeling failure.

Identity reverified: exact dev-session current; both env markers absent; trusted developer binding names this exact workspace/session/reviewer. Live roster retains reviewer0/thread01a1a24e-920c-7b82-9fff-7754d1f947ab, ready/review-purpose **gpt-6.1-sol/xhigh/read_only**, no overrides/fallback. Current mandatory skill/all four lane references and applicable workspace/repository guidance were read or reused unchanged in this context; latest applicable package procedure is2b5944e8.

Read-only review only: source/history/receipt inspection, local Git/hash checks and bounded local frozen ELF/BTF/source inspection. **No source/session writes, suite/test/eval/build/VM/network/CI operation, Git mutation, nested reviewer, service or lifecycle action.**

**Combined review package complete.** No source fix requested. Root owns saving this full report as scheduler-capture-review.md, reconciliation and any later publication/one-case execution. Session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
