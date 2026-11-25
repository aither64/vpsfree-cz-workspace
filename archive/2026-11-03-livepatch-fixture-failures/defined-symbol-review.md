# Defined-symbol correction: independent committed review

Reviewer: reviewer0, retained gpt-6.1-sol/xhigh, review-purpose/read_only.
Final range: vpsfreecz/vpsadminos 742eb30cb1a8b6766c85e915d26b0400e38244b1 -> 65d43eececbd0d13a3863c554e86e22680fbff84.
Affected delta: tested 48f2983e3cf6b5b72a21c254f744ad8e7d62a123 -> 65d43eececbd0d13a3863c554e86e22680fbff84.
Lanes: general, architecture/repetition, scope/proportionality and risk/compatibility.

## Findings

### Blocking DS1 — The predicate filters the pre-format ELF type, but /proc/kallsyms lowercases this import

Commit 65d43eececbd0d13a3863c554e86e22680fbff84:
- tests/suite/kernel/livepatch-6.12.95-common.nix:953-956.
- tests/suite/kernel/livepatch-inet-frag.nix:89-90.
- test-runner/spec/test_runner/livepatch_runtime_sites_spec.rb:90-96,160-163,173-177.

Both new queries exclude only uppercase U. The primary-source excerpt in the packet stops too early to establish the actual /proc/kallsyms presentation contract. Although kernel/module/kallsyms.c:elf_type() initially returns U for this strong SHN_UNDEF import, the same pinned kernel's kernel/kallsyms.c:s_show() changes the type before printing a module row:

    type = iter->exported ? toupper(iter->type) : tolower(iter->type);

This is at a2384967b90f24d2470c9eb15f0e66d938df7e08:kernel/kallsyms.c:742-752. The module reader obtains iter->exported from is_exported(name, value, mod), which searches that module's export table (kernel/module/kallsyms.c:24-35,378-399). kernel/module/main.c:2129-2138 initializes that table from __ksymtab. Actual readelf inspection of the exact qi47 normal module shows no __ksymtab symbols or sections. Therefore its retained non-exported inet_frag_find import is rendered as lowercase u, and $2 != "U" keeps it.

I independently rehashed the module to 7c4da9d643d45ad9c07bde72b0180175519c5e7a15a6f2aec9e54831aee8455f and confirmed the same two ELF entries: local FUNC definition at .text+0x44e50, size 1928; global NOTYPE UND import. The pinned source also explicitly retains all symbols for a livepatch module (kernel/module/kallsyms.c:203-221), explaining why the import remains visible. This is a source/ELF-derived conclusion; the uploaded failing query prints addresses only, so I do not claim that its raw log directly captured the type character.

Read-only reproduction extracted both actual committed Ruby lookup methods and executed their rendered AWK commands over stdin with the source-derived lowercase presentation:
- Uppercase U import plus t definition: both return the expected replacement address.
- Lowercase u import plus t definition: common raises "ambiguous kernel symbol ... (2 matches)"; fragment raises the same two-address ambiguity as the original runtime failure.
- Lowercase u import only: both incorrectly accept the original-kernel address as the selected module's symbol.

Thus the demonstrated runtime failure remains possible for the exact pinned kernel/module, and an import-only row can still supply the wrong base address. The green fixture suite currently encodes the mistake: it supplies uppercase U for imports and explicitly calls lowercase u a defined symbol. The pinned Linux formatter does not justify that interpretation of u; GNU nm-style expectations cannot substitute for the actual proc renderer.

Smallest correction: align the two predicates and comments with the pinned proc presentation, excluding the current strong undefined-import marker in both cases (for example U/u), while keeping genuine text/data definitions eligible. Change the lowercase-u positive controls into source-grounded import rejection controls, including import+definition, import-only and the FUSE position paths. Retain exact names, module/NF scope, unique-definition validation, defined-data coverage and rejection of equal-address duplicate definitions. Reconcile the clipped source claim and lowercase-u acceptance decision in the existing design/evidence records. No new schema, descriptor field, generic symbol framework, address-prefix heuristic, first-match selection or kernel change is needed.

Fix DS1 before replacement long CI. This correction is needed inside the accepted pinned-kernel lookup boundary; an architect-approved plan cannot establish a kernel fact contradicted by the owning source.

## Evidence and review scope

I read the mandatory skill and all four lane references, reverified identity/settings and reused unchanged applicable workspace/repository guidance already read in this context. The current guidance commit remains 674a723ef and those instruction paths are clean. The review directly covers the complete new three-path committed delta and necessary kernel/runtime context. It reuses final-review.md, review-reconciliation.md and retention-review.md for unaffected implementation; no unrelated sixteen-file audit was repeated.

The saved raw job log binds run 41740116653, attempt 1, Intel job 126293359412 to tested head 48f2983e3cf6b5b72a21c254f744ad8e7d62a123. It reports ten successful scripts and only kernel/livepatch-inet-frag failed. I independently verified artifact ZIP size 366187 bytes and SHA256 0547b8aca3557008b5e1de4037c56099b86548d3ac8955fa3776a091035ff7d5. Raw job output identifies artifact 13294011506; ZIP contents supply the exact normal producer/module digest/sites/source/input identities and descriptor.

The actual machine-shell query returned ffffffffc1c91f50 and ffffffff92f7fd20. Its native baseline recorded one timer observation with next=0x0 and lock=0. Candidate activation completed, then lookup failed before target probe installation. No candidate locked/hashed observation is present, so this is evidence of lookup failure rather than a target timer regression or target pass.

I inspected the nineteen added controls and saved 53-example red/final outputs. They meaningfully execute actual AWK rather than mocking filtering, retain duplicate-definition and data/position behavior, and show six regressions before the source correction. Their remaining limitation is the incorrectly modeled import case described in DS1. The final 53-example pass and hook/lint results cannot prove a kernel presentation contract that their input fixtures misstate. No full suite rerun was needed to demonstrate this; my in-memory reproduction uses the same actual methods and real AWK without source/session writes.

Primary kernel source was inspected from the canonical local Linux object at exact a2384967b90f24d2470c9eb15f0e66d938df7e08, not a newer upstream version. The existing boot source pin names that revision. Relevant paths are kernel/module/kallsyms.c, kernel/kallsyms.c and kernel/module/main.c. No live kernel probe, guest, build, fetch or network observation was launched.

## Scope, architecture, compatibility and documentation

The accepted task is unchanged: current normal producer qualification with finite meaningful witnesses and exact boot/predecessor/recovery contracts. The new delta is three paths, +117/-7, principally nineteen focused regression cases. A small eligibility predicate in the two existing consumers is proportionate to this concrete failure; no new subsystem is warranted. The roughly ninety-minute old Intel job and its diagnostic artifact are delivered verification evidence, not grounds to widen the feature or repeat expensive checks before fixing the source-level defect.

Adding NF == 4 for module rows agrees with the pinned proc output format; native NF == 3 remains appropriate. Exact module/name selection, cardinality, address validation, FUSE positions 0/1 and data-symbol support remain correctly bounded. Neither consumer deduplicates true definitions. DS1 concerns the one import/definition classification rule, not these preserved checks.

The behavior belongs in these existing test consumers. The two small predicates and parallel controls are sufficient; extracting a new framework would add scope without resolving DS1. No helper C/assembly, host resolver/schema, ABI, candidate input, predecessor, fixed boot, production state/protocol/API or deployment contract changes. No coordinated fleet update is required.

Existing project documentation already states the unique-definition contract; corrected nearby source comments are an adequate durable explanation. Keep the individual failed attempt and exact evidence in package-c-runtime-symbol-failure.md. Its initial "uncommitted" wording is an earlier checkpoint; the review packet and current state correctly identify committed 65d. The important factual reconciliation is the proc case conversion and unsupported lowercase-u acceptance claim.

## Final history and provenance

Independently verified:
- Exact final object 65d43eececbd0d13a3863c554e86e22680fbff84 has parent and merge base 742eb30cb1a8b6766c85e915d26b0400e38244b1.
- Complete final range has one feature commit, "tests/livepatch: qualify current module probe sites", sixteen paths +2270/-183.
- 48f2983e -> 65d changes exactly the two lookup consumers and their runtime-site spec, +117/-7.
- All thirteen other feature blobs and the original commit message are identical to reviewed/tested 48f2983e, including retention workflow, resolver/schema, helper C, predecessor/boot material and docs.
- No rebase or target change occurs in this delta. Local tested-48f2983e backup retains 48f2983e3cf6b5b72a21c254f744ad8e7d62a123.
- git diff --check passes; HEAD and final clean index/worktree/nonignored-untracked status still matched 65d at completion of inspection.

The branch continues to have one coherent internal qualification feature. Prior narrow fixes and retention support are folded into their owner; no obsolete approaches, fixup/tidy commits or transitional source iterations remain. DS1 is a correctness defect in the new predicate, not obsolete history.

No repeated dependency/channel/input/pin/lockfile/generated-update streams exist in the final series. No consolidation or intermediate-consumer exception is needed.

No migrations. There is no database/schema or production persisted-format/protocol migration, deployed intermediate or externally consumed intermediate schema; migration lineage is empty. Prior review and retained local backup refs remain provenance outside the final feature history.

## Readiness, identity and handoff

Disposition: one Blocking finding, DS1. Current 65d is not ready for replacement long CI until it is corrected and the source-grounded focused controls pass. Afterwards, actual new-head fragment hash-linked/lock-held/nonzero-hit/zero-miss proof, FUSE safe caller-filtered hold/unwind/recovery behavior, TCP arithmetic/receiver proof, the remaining semantic witnesses, native suite and all nine lifecycle rows remain required. Old-head partial row successes do not satisfy the user's complete final-head CI condition for vpsadminos/staging merge.

Session binding is exact: dev-session current printed 2026-11-03-livepatch-fixture-failures; both environment identity markers are absent, and trusted thread-bound developer instructions name this slug and /home/aither/workspace/ai/vpsfree.cz. Fresh roster confirms reviewer0/thread 01a1a24e-920c-7b82-9fff-7754d1f947ab, gpt-6.1-sol/xhigh, review/read_only, ready. No settings override or nested reviewer.

I remained read-only: no source/session writes, builds, VMs, retry/cancel/fetch/push, merge, deploy or lifecycle action. Report delivered through report_to_lead for root to save as defined-symbol-review.md. Implementers own correction; the session remains open.
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-livepatch-fixture-failures/
