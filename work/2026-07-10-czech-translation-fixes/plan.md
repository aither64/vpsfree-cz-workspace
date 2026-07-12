# 2026-07-10-czech-translation-fixes

## Goal

Correct reported Czech localization issues in the vpsAdmin WebUI and API
metadata, including terminology, an untranslated version label, and clearer
ZFS property names in the dataset form. The follow-up also corrects the IP
address assignment-history headings and audits network `Prefix` terminology
across the Czech catalogs. A further follow-up audits mount-state wording,
localizes the user-namespace restart notice, and makes node scrub/resilver and
performance values consistently lower-case. The current follow-up replaces the
generic WebUI submit label `Go >>` with context-specific actions and fully
localizes the VPS swap preview. A subsequent follow-up localizes descriptions
of configured web services on the Czech vpsf-status page while preserving the
existing English JSON API contract. The latest follow-up localizes the VPS
root-password warning and network-interface type labels, and capitalizes only
the entity probe-log message column in vpsf-status. Merge each result to its
default branch and update the corresponding production deployment channel.

## Affected repositories

- `vpsadmin`: owns the WebUI gettext catalog/templates and the Czech API
  locale used for transaction-chain and dataset-property metadata.
- `vpsfree-cz-configuration`: pins the merged vpsAdmin revision for the
  `vpsadmin` channel, configures monitored vpsf-status web services, and pins
  the deployed vpsf-status revision.
- `vpsf-status`: parses configured web-service descriptions, renders the
  locale-specific status page, and exports the stable JSON status contract.

HaveAPI itself is not changed: it provides the localization mechanism, but the
reported application strings are defined by vpsAdmin.

## Approach

- Correct the Czech OOM, payment-chain, node navigation, transaction-chain,
  SSH-key, and dataset-property translations.
- Translate the IP address assignment-history headings as `Od`, `Do`,
  `Přidělení`, `Odebrání`, and `Přiděleno`.
- Audit every Czech catalog use of `Prefix` and keep the established networking
  term `prefix` instead of the literal `předpona`; document the distinction in
  the Czech terminology guide.
- Replace the unnatural unmounted-state wording with `Nepřipojeno` and audit
  the complete Czech mount-state set in context.
- Localize the VPS-details notice shown when changing the user namespace map.
- Audit all Czech scrub/resilver and node-performance values and keep status
  values lower-case when they are rendered as table-cell data.
- Localize the index-page cgroups help URL so Czech users are sent to the Czech
  KB page instead of the English manual.
- Change route and host-IP add/remove transaction labels from infinitives to
  consistent Czech verbal nouns.
- Correct export-for-mount wording and localize the create-export advanced
  options toggle.
- Standardize Czech `subdataset` terminology as `vnořený dataset` and retain
  `potomci` when wording explicitly describes all recursive descendants.
- Replace all 22 `Go >>` submit buttons with labels describing the submitted
  action. In particular, use `Set resources` / `Nastavit prostředky` and
  `Set features` / `Nastavit funkce`; remove the decorative arrows everywhere.
- Fully localize the VPS swap preview. Use complete numbered-placeholder
  strings for the dynamic title and migration descriptions, translate every
  hard-coded table label and arrow alternative, change `Teď` to `Nyní`, and
  render the footer as `Změněné atributy jsou označeny zeleně.`
- Call the preview operation `Swap VPS` / `Prohodit VPS`, matching the actual
  `swap_with` action instead of describing it as a replacement.
- Make the WebUI version caption pass through gettext.
- Name the node storage-pool scan column after the ZFS operations it tracks
  (`Scrub / resilver`) and show an explicit inactive status when neither is
  running.
- Add the exact ZFS names to the five advanced dataset-property labels:
  `compression`, `recordsize`, `atime`, `relatime`, and `sync`.
- Localize the three administrator payment views. Keep English `Login` and
  translate it as `Přezdívka`; use `Částka`, `Platby uživatele`, and
  `Přehled plateb`; translate all payment-table headers; rename the incoming
  payment's contextual English `FROM` header to `PAYER` / `PLÁTCE`; and render
  incoming-payment state values through the API's localized choice metadata.
- Add an optional `descriptions` map to each configured vpsf-status web
  service. Select `descriptions.<page locale>` for HTML and fall back to the
  canonical English `description`; keep `/json` unchanged.
- Configure exact Czech descriptions for all six production web services:
  `Webové stránky v češtině`, `Webové stránky v angličtině`, `Znalostní báze
  v češtině`, `Znalostní báze v angličtině`, `Diskusní fórum`, and the agreed
  technical term `IRC bouncer`.
- Update the vpsf-status sample configuration to document the localized shape.
- Localize and polish the non-admin VPS root-password warning using exact
  English/Czech sentences while preserving its formatting and behavior.
- Render network-interface types through the API's localized choice metadata.
  Keep raw values unchanged and use exact English/Czech labels: lower-case
  `venet`, `Bridged veth` / `Veth připojený do bridge`, and `Routed veth` /
  `Routovaný veth`.
- Capitalize the first Unicode character of localized vpsf-status probe-log
  messages only when it is lower-case. Apply this at the shared probe-log view
  boundary for entity and group detail logs. Keep shared lower-case
  translations for history summaries, and preserve acronym, numeric, and
  already-capitalized prefixes.
- Use exact Czech payment headers `PŘIJATO`, `ZAÚČTOVAL`, `ČÁSTKA`, `OD`,
  `DO`, `PLATBA`, `DATUM`, `STAV`, `PLÁTCE`, `ZPRÁVA`, `VS`, `UŽIVATEL`, and
  `MĚSÍCE` according to each table's columns.
- Regenerate the WebUI POT/PO/MO catalogs with the repository scripts.
- Fast-forward the reviewed vpsAdmin feature commit into current upstream
  `master` and push it.
- Run `confctl inputs channel update --commit vpsadmin` in a dedicated
  configuration worktree, preserving the generated commit message, then
  integrate that input-only commit into the configuration default branch.

## Compatibility and deployment

- The changes affect display strings and template wiring only. There are no
  database, persisted-state, API schema, protocol, CLI, generated-client, Nix
  option, or on-disk format changes.
- Old and new API/WebUI versions remain mutually compatible. A rolling deploy
  can temporarily show the old or new wording depending on which WebUI/API
  instance serves a request.
- Rollback is safe and requires no operator action; it only restores the old
  labels.
- The `vpsadmin` configuration channel changes only the `vpsadminServices`
  source pin after the vpsAdmin commit is available on `master`. No coordinated
  vpsAdminOS, database, or all-node update is required.
- Deployment ordering is vpsAdmin merge/push first, then configuration input
  update. Rolling mixed-version operation and rollback to the prior pin are
  safe because all runtime changes are presentation-only.
- The vpsf-status configuration extension is additive. Old binaries ignore
  `descriptions`; new binaries render legacy configurations through the
  existing `description` fallback. The public JSON schema and English values,
  metrics, persisted probe history, and on-disk formats do not change.
- The vpsf-status application and configuration can be deployed in either
  order. Until both are present, the Czech page falls back to English; rollback
  is safe and requires no operator action.
- Network-interface enum values and API response data remain unchanged; only
  localized choice labels change. Old/new vpsAdmin API and WebUI versions are
  compatible, though both updated components are needed to display the labels.
- Probe history storage is unchanged. Capitalization occurs only in probe-log
  view models, so existing history summaries such as `Ping not responding` and
  `Ping neodpovídá` remain grammatically unchanged.

## Testing plan

- Run the WebUI locale update/check and locale health scripts.
- Run focused WebUI regression tests for template/localization behavior.
- Update Playwright selectors for the contextual submit labels and extend the
  existing swap preview coverage to assert both English and Czech rendering.
- Extend the existing administrator payment Playwright scenario with exact
  Czech payset, incoming-payment, detail, and payment-history assertions,
  including all four localized state choices and failure-safe restoration of
  English.
- Run focused API locale specs or the repository's equivalent localization
  checks.
- Run mandatory pre-commit hooks and the standalone mandatory change review
  before any long integration testing.
- Verify the generated configuration input diff and run the repository hook
  checks; evaluate a representative affected vpsAdmin service scope if the
  channel update selects one clearly.
- Add parser/model and HTTP rendering coverage for localized vpsf-status
  descriptions, English rendering, missing-translation fallback, and the
  unchanged `/json` contract.
- Run `go test ./...`, `make i18n-health`, the declared Lefthook checks, and
  `nix build .#vpsf-status`; evaluate/build the production vpsf-status machine
  after updating its input through `confctl`.
- Add exact WebUI catalog/API metadata assertions and English/Czech Playwright
  coverage for the password warning and `veth_routed` label.
- Add vpsf-status unit/HTTP coverage for English/Czech capitalization, raw
  messages, acronym/numeric preservation, and unchanged shared history text.
- Keep the password warning, interface labels, and probe-log capitalization as
  three focused functional commits. Run the mandatory standalone review before
  `webui#vps-user-core` and other long integration tests.
