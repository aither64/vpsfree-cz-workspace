# Product history reconstruction

Pending normal quick-stage completion. Never reset, clean, stash or bypass hooks.
Retain backup/2026-10-14-config-imports-pre-compatibility-review84d2fbe06 and an
exact backup of the complete verified staged implementation commit. Published
old product29e268350 and prior source backups remain exact provenance.

1. Hook-enabled commit of only the complete staged technical+guide inventory.
   Record head/tree and clean proof. This temporary independent technical commit
   will be folded before review/publication.
2. Populate history-rewrite-inputs.json with exact selector, oldFix, policy,
   technical heads, selectorTree, oldFixTree and final technicalTree.
3. Run interactive rebase onto1150e37b with the prepared sequence helper, inside
   the declared Nix environment. It rewords selector/oldFix with active hooks,
   proves their identical trees, folds technical into owning persistence change,
   amends final fix message with hooks, then applies the independent policy owner.
4. Final tree must equal verified technicalTree; complete range must be exactly
   selector + independent baseline correction + independent docs/policy owner.
   Inventory each path, complete series and no-migrations/repeated-stream facts.
5. Check final messages <=80, no development vN/history/check transcript/pending
   narration. Preserve actual releases, provenance and authorship. Run all4final
   committed templates/lock provenance before reviewer assignment.

Do not rewrite default/merged history. No integration or deployment authority.
