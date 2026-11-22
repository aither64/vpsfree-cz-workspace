# Candidate annotation import scope

Related initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

Running `tools/import-kb-annotation-plan.rb` with a focused candidate index
rewrote `contract/kb-annotations.yml` with only four bindings and no
exceptions. The normal contract contains bindings for all KB pages.

## Cause

The helper imports the candidate index's `annotations` array. That array
describes planned replacements in existing pages; it is not an inventory of
every `<vpsadmin-nav>` tag in generated candidate pages.

## Safe workflow

Use the helper only when the candidate index is intentionally the complete
source of the annotation contract. For an all-page KB contract, preserve the
existing explicit exceptions and derive semantic tag counts from every
candidate page using `KbNavigationDiscovery.semantic_content`, which excludes
examples inside code blocks. Review the resulting diff before validation.

Regenerate independent navigation discoveries separately. When discovery IDs
are unchanged, preserve their existing `paths` or `reason` classification;
classify every new ID explicitly.

## Verification

For the related initiative, `nix develop -c bin/check` and the candidate-aware
`tools/check-kb-annotations.rb` check both passed after rebuilding 131 semantic
bindings, preserving 9 exceptions, and classifying all 252 discoveries.
