## English

WebUI now uses the generated TypeScript client for vpsAdmin API operations and
descriptions.
HaveAPI still encodes requests and decodes replies. WebUI retains authentication,
language, anonymous-client isolation and read-only recovery; it preserves write
receipts and blocks replay when the outcome is uncertain.

Domain callers validate the generated contract and expose supported controls.
For example, an advisory draft keeps its accepted parent and original CVE intent
when a child sequence stops, so review does not create another parent or lose
unresolved work. The migration also corrects resource associations, asynchronous
receipts and fixtures that described unsupported response shapes.

The committed dependency is the published `vpsadmin-typescript-client@0.3.0`,
with its canonical registry URL and integrity in the npm lockfile. Its 1,352 shipped
JavaScript and declaration files match the tested candidate byte for byte. Release
source and generator provenance are recorded separately; the exact runtime peer
remains `haveapi-client@0.32.0`.

Frontend Nix packaging uses ordinary registry dependency fetching. The temporary
tracked archive, archive provenance and cache adapter are removed. The optional
local development workflow still supports `npm pack` and a no-save installation;
`npm ci` restores the committed graph. This branch has no database migrations.
Merge and production deployment remain separate maintainer decisions.

## Česky

WebUI používá generovaného TypeScript klienta API vpsAdminu pro operace i jejich
popisy.
HaveAPI dál sestavuje požadavky a zpracovává odpovědi. WebUI zachovává přihlašování,
jazyk, oddělené anonymní klienty a obnovu požadavků pouze pro čtení. U zápisů
uchovává potvrzení akce a při nejistém výsledku brání opakovanému odeslání.

Volající ověřují data podle generovaného kontraktu a zobrazují podporované
ovládací prvky. Když se například zastaví přidávání CVE do konceptu upozornění,
zůstane zachovaný přijatý koncept i původní záměr. Následná kontrola tak nevytvoří
další koncept ani neztratí nedořešené změny. Migrace také opravuje vazby na zdroje,
potvrzení asynchronních akcí a testovací odpovědi, které neodpovídaly API.

Závislost v repozitáři používá vydaný `vpsadmin-typescript-client@0.3.0`.
Lockfile obsahuje adresu npm registru a integritu archivu. Všech 1 352 vydaných
souborů JavaScriptu a deklarací se bajt po bajtu shoduje s testovaným kandidátem.
Zdrojová revize vydání a původ generátoru jsou zaznamenané samostatně. Přesná
závislost na běhové knihovně zůstává `haveapi-client@0.32.0`.

Nix při sestavení frontendu používá běžné stahování závislostí z registru.
Dočasný archiv v repozitáři, jeho záznam původu a úprava cache jsou odstraněné.
Volitelný vývojový postup dál umožňuje použít `npm pack` a dočasnou instalaci bez
změny manifestu a lockfile. Příkaz `npm ci` obnoví závislosti podle repozitáře.
Větev neobsahuje databázové migrace. Sloučení a produkční nasazení vyžadují
samostatné rozhodnutí správce.

## Verification / Ověření

- Recorded application checks: 2,227 tests in 343 files; BFF: 58 tests; affected
  script, compiler, lint and documentation checks pass.
- Synthetic browser workflows: 124 desktop/mobile cases and 8 Czech/English
  capture cases at `1bfad6ce`, with locale, viewport and trace provenance.
- The first 30-spec CI repair passed its news5 and remaining98 local gates at
  `4279c238`. The second 27-spec repair covers all 220 selected local identities:
  164 passed at `3ca34e34`, with 56 individually proven passes retained from
  unchanged files. All 12 advisory cases passed on that source.
- The third repair passed all 118 local Chromium/mobile Chrome cases across
  11 further specs at `2ad8f717`: 59 per project, retry 0, no errors or reused
  passes. The initial three-project attempt stopped during local WebKit page
  setup before the failed test body. The later native WebKit CI on `20aa0e9e`
  passed 274 cases with 2 skipped; all 8 touched WebKit identities have individual
  pass evidence on that source. Recorded owned process/listener effects are reconciled.
  This checkpoint adopted 136 files with 146 deferred.
- The fourth repair covers 136 Chrome identities across six further specs:
  114 passed at `451dfe1d` (46 Chromium and 68 mobile Chrome, retry 0), with
  22 individually proven passes retained from unchanged files and inputs.
  All 90 lifecycle identities ran on the corrected source. This is combined
  coverage across recorded heads, rather than 136 executions on one head.
  The corrections complete canonical response and template-Show fixtures and
  exact Start request expectations; production guards and runtime are unchanged.
  At that checkpoint, strict E2E coverage was 140 checked/142 deferred; the
  original baseline, sourceRevision, compiler options and surviving deferral
  records remained unchanged.
- The residual support-account scenario now uses the declared nullable DNS
  resolver relation. Its complete Chromium scenario passed at `b5c12bcd`,
  retry 0, with support identity, foreign owner, all tab permission checks and
  the final no-mutations assertion preserved. The entire spec is now strictly
  checked, bringing E2E coverage to 141 checked/141 deferred without changing
  compiler options, the baseline or surviving deferral records.
- Independent source/history and affected fixture reviews leave no findings
  unresolved. The direct semantic payload-assertion remedy and final factual
  work-log append were inspected separately. One generated-client input stream
  remains, with no database or persisted-format migrations.
- The isolated local-client build/pack/override/restore cycle passed on WebUI
  `8d0bb48a` / client `e16663a9`: typecheck, 23 binding tests, both forced Vite
  resolutions and full installed-client restoration. The packed README matches
  corrected source; this was verified before the registry transition.
- Isolated API: 23 calls through the generated client against API `610a96f8` and
  HaveAPI `0.32.0`, with native cleanup verified. This used candidate `99ee0665`;
  the released package has the same distributed program and declarations.
- Nix frontend/BFF/provenance/source/package-content checks pass on exact
  `b5c12bcd`, exit 0 after 53.299 seconds. Both installed metadata files identify
  that full clean commit. The complete 1,801-derivation input graph and locked
  source identities are recorded; all 25 protected inputs match the committed,
  literal and filtered sources. Archive, generator and dependency pins are unchanged.

Required CI passed on `b5c12bcd`:

- [Core CI](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41548300724):
  all three jobs passed, including 2,227 application tests in 343 files and
  strict E2E coverage of 141 checked files with 141 deferred.
- [Browser matrix](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41548300683):
  Chromium 632 passed, mobile Chrome 574 passed, and mobile WebKit 274 passed
  with 2 skipped. No test retries or failures were reported.

Independent affected review, the focused support scenario and exact-head Nix
packages/provenance checks also passed at that checkpoint. Earlier browser and
isolated API results retain their recorded revisions and input scopes.

The released-client transition is committed at `4ed519b6`. All 1,360 installed
package files match the verified release, including the 1,352 distributed program
and declaration files. The bounded lock delta preserves 484 other records.
Six source-checker tests and 100 policy/wire tests passed against the installed
release. Application, tooling and E2E strict checks passed (141 checked files,
141 deferred), as did scoped lint, formatting, Nix syntax and the docs audit.

Independent final affected review at `4ed519b6` found no unresolved findings.
Exact-head Nix package verification is pending.

The candidate remains based on `63d484fc`; `main` has since advanced to
`1c8478bc`. Reconciling that upstream change remains a separate integration step.

These checks distinguish fixtures, isolated HTTP contracts and package output;
OAuth deployment and asynchronous worker acceptance remain separate. The visual
sample does not cover every changed control or unvisited language/reset state.

Requirements: REQ-005, REQ-007, REQ-011, REQ-012, REQ-054, REQ-056, REQ-060,
REQ-061 and REQ-068. Details are in the migration work log, API contracts and
workflow documentation in this branch.

[Review records and actual desktop/mobile images](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
