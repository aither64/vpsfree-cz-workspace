# 2026-08-09-kb-nixos-rebuild-switch

## Goal

Audit the complete Czech and English production KB page inventories for
`nixos-rebuild` commands that omit an action such as `switch`, correct every
confirmed instance, and prepare the exact reviewed candidates on the staging
KB sites without writing to production.

## Affected repositories

- vpsFree.cz coordination workspace: guarded production page inventory,
  replacement plan, bilingual candidates, release manifests, and tracking.
- No application repository or runtime code change is expected.

## Approach

1. Fetch all accessible Czech and English production pages with
   `bin/kb-contract-fetch`.
2. Search every fetched page for `nixos-rebuild`, inspect each occurrence in
   context, and classify whether a required action is missing.
3. Build complete candidates from an exact guarded content-replacement plan.
4. Generate localized checksummed release manifests.
5. Claim and reset the KB staging instance, stage both language manifests, and
   verify the staged content and language links.
6. Leave production untouched pending explicit user approval.

## Compatibility and deployment

This is a documentation-only correction. It changes no persisted state,
database schema, API, generated client, protocol, or NixOS configuration.
Existing and new systems are unaffected. Staging mirrors production and release
manifests guard every page by production revision and content checksum, so a
later production promotion will stop if the source pages have changed. Each
language can be promoted independently; rollback would be a normal DokuWiki
page revision restore.

## Testing plan

- Verify production API identity and access for both wikis.
- Confirm the all-page source inventory is complete and search all occurrences.
- Build candidates with exact occurrence counts and review only intended diffs.
- Generate and inspect Czech and English release manifests.
- Stage and run `bin/kb-release verify` for each language.
- Read back affected staging pages and confirm corrected commands and
  Czech/English counterpart links.
