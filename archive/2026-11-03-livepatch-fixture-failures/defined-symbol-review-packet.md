# Defined runtime symbol correction: committed review packet

Session2026-11-03-livepatch-fixture-failures; vpsfreecz/vpsadminos worktree
worktrees/2026-11-03-livepatch-fixture-failures/vpsadminos. Retained reviewer0
Sol/xhigh/read_only remains independent. Assess the affected lookup behavior
under general/architecture/scope/risk lanes and verify final whole-branch
inventory. Reuse unaffected prior substantive source reviews, not another full
sixteen-file audit: final-review.md + review-reconciliation.md + retention-review.md.

Exact final range:742eb30cb1a8b6766c85e915d26b0400e38244b1 ->
65d43eececbd0d13a3863c554e86e22680fbff84. Parent unchanged; no rebase needed.
One feature commit with original valid message,16paths+2270/-183. No migrations,
repeated dependency/input/pin/generated streams or obsolete fixups. Canonical
staging freshly verified742; published/tested feature remains48f2983e3cf6b5b72a21c254f744ad8e7d62a123.
Local backup tested-48f2983e preserves that exact head;4fc/efc/06d backups retained.
Current65d is committed/clean, not published/CI-verified. Complete final
comparison captured. No default-branch or deployment change.

New behavior delta48->65d is EXACT3paths+117/-7:
- tests/suite/kernel/livepatch-6.12.95-common.nix
- tests/suite/kernel/livepatch-inet-frag.nix
- test-runner/spec/test_runner/livepatch_runtime_sites_spec.rb
All13 other feature blobs and commit message unchanged, including cache-retention
workflow, resolver/schema, fixed predecessors/boot, test helper C and docs.

Read package-c-runtime-symbol-failure.md and linked raw verified evidence.
Old exact48/run41740116653 attempt1 Intel126293359412 failed after1h30m50s,
only kernel/livepatch-inet-frag failed; ten other scripts passed. Its artifact
ZIP13294011506/366187B matches reportedSHA0547b8aca3557008b5e1de4037c56099b86548d3ac8955fa3776a091035ff7d5.
Native timer baseline passed; after candidate activation, exactmodule-filtered
kallsyms query returned two same-name addresses before candidate probe install.
Real module ELF has defined LOCAL FUNC inet_frag_find .text/0x44e50/1928 and
GLOBAL NOTYPE UND same name. Pinned kernela2384967 module/kallsyms.c elf_type()
classifies SHN_UNDEF as uppercaseU. Exact source URL/excerpt is retained in C note.
These observations establish the lookup fault; no candidate hash/lock observation
was reached, so no timer regression or target runtime pass was inferred.

Architect-owned bounded decision recorded in design.md/implementation-plan.md:
exclude uppercaseU imports BEFORE existing exactly-one checks in BOTH lookups;
retain exactname/module, NF4 for modules/NF3 for native, legitimate defineddata
(x2avic_enabled), lowercaseu and supported positions0/1 including originalFUSE1.
Do not deduplicate even equal-address defined rows; no first/address-prefix
match. No descriptor/staticsectionfield/schema/resolver/Nix-input/ABI/producer/pin or
production change, generic framework, weaker witness or historical lane.
Fragment locked+hashed/nonzerohit/zero-miss checks and FUSE/TCP behavior remain.
Existing definition-identity contract and nearby comments explain the invariant;
no further product-doc mechanism needed. Failure/rollout evidence belongs here.

C added19 meaningful controls executing ACTUALrendered AWK queries against
fixture files (machine transport stubbed, filtering uses real awk). Inputs cover
native/target/import/unrelated/wrongscope; import-only/absent definitions;
duplicate defined rows incl equal addresses; defineddata/lowercaseu; FUSE0/1,
unsupportedpos and truepos1 ambiguity. Six regressions reproduced beforefix;
final53examples0failures/body1.86s, declared cached test-runner/native environment.
RuboCop, Nixfmt, Nix/Rubyparse and whitespace pass. Ordinary mandatory commit
hooks pass with exact cached declared tools, no tracked unstaged/stash/reset.
No builds/VM/kernel/oldNix repeat. Unchanged helperC SHA d9226b31152ce994b16e5733f8e801329ff8e8ca1b22074e2b0bee36373b3977
binds prior compile+49/19importCRC proof. Unchanged B module/schema/source binds
prior24resolver controls and real all9 selectors; prior53host specs are not
runtime qualification. Verify check scope and actual source, not just counts.

Risk: overall livepatch-test instrumentation remains high; this delta narrows
eligible runtime symbols to definitions inside the accepted contract. No
production persisted state/protocol/migration/fleet update. User authorizes
implementation/publication and conditional vpsadminos/staging merge ONLY after
complete final-head CI passes. That condition is currently UNSATISFIED. Current
old48 run continues under solewatcher with four rows passed, Intel main failed,
others/native pending/running; no retry/cancel/newCI until reviewed publication.
Required next proof: real fragment target hash-linked+lock-held/zero-missed
observation, required FUSE/TCP/other semantic witnesses, native and all9rows on
new exacthead. Do not silently weaken assertions or treat host fixtures as VMproof.

Read applicable workspace/repo guidance and mandatory skill+fourlane refs.
Stay read-only; no source/session writes, builds/VM/retries/fetch/push/CI mutation,
merge/deploy/lifecycle. Return complete report through report_to_lead for root
to save as defined-symbol-review.md. Include explicit finalhistory, no repeated
streams, no migrations and remaining proof limits; no rubberstamp requested.
