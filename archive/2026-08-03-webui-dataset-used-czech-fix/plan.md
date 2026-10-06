# 2026-08-03-webui-dataset-used-czech-fix

## Goal

Correct dataset size details in the vpsAdmin WebUI so Czech output separates
the translated label from the compression ratio value and uses the adverb
"nekomprimovaně" in this context. Audit other uses of the same formatter or
translation to prevent the defect from remaining elsewhere.

## Affected repositories

- `vpsadmin`: WebUI formatting, translations, and focused tests.
- `vpsadmin-kb-captures`: pin the exact vpsAdmin revision and run the canonical
  WebUI documentation contract. Dataset screenshot captures exist, so review
  and regenerate the reported Czech/English concepts as required.
- `vpsfree-cz-configuration`: after vpsAdmin integration, update the production
  `vpsadmin` channel through `confctl`, verify the resulting pin, and push it.

## Approach

1. Locate the dataset used/referenced rendering and trace its translation and
   whitespace handling.
2. Search for all consumers of the affected formatter and translation keys.
3. Remove leading/trailing whitespace from short gettext messages, put
   separators in PHP rendering code, and correct the Czech wording.
4. Add focused regression coverage for Czech and English output.
5. Review the KB documentation contract impact, run quick verification,
   commit, perform mandatory standalone change review, then run relevant tests.
6. Leave reviewed KB candidates staged without production promotion, integrate
   vpsAdmin by fast-forwarding `master`, and update/push the configuration
   `vpsadmin` channel through `confctl`.

## Compatibility and deployment

This is expected to be a presentation-only WebUI localization change. It must
not change API contracts, persisted state, database schemas, generated clients,
protocols, NixOS/vpsAdminOS configuration, or deployment ordering. Old and new
WebUI processes may run concurrently because each response is independently
rendered; rollback restores the previous wording without affecting stored
state. No coordinated node or machine update is expected.

The catalog audit found the same whitespace-sensitive construction in several
other WebUI labels. Those call sites will be corrected in the same change. The
rendered English output remains unchanged; Czech output gains separators that
were previously lost where translations omitted source whitespace. One dynamic
gettext expression for the route-via default will also be split so the static
text can actually be translated.

The deployment configuration update will only move the vpsAdmin source pin to
the integrated commit. It does not change schema or protocol ordering. Existing
and updated WebUI instances remain compatible during rollout, and rolling back
the configuration pin restores the previous wording without state conversion.

## Testing plan

- Run focused tests for the formatter/view component in Czech and English.
- Search all locale files and WebUI consumers for equivalent broken patterns.
- Run repository hook checks required by the local `AGENTS.md`.
- Run the mandatory standalone change review after committing and before any
  longer integration suite.
- Run the capture contract, regenerate and visually inspect affected bilingual
  screenshots, validate the exact candidate release, and leave it staged only.
- Run the configuration repository's local checks and inspect the generated
  `confctl` channel-update commit before pushing.
