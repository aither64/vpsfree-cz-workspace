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

The selected client candidate stays unpublished. Its tracked, revision-qualified
archive uses an ordinary npm file dependency, checked provenance and integrity.
Frontend Nix packaging adds the verified local archive to the transient cache map and retains
the upstream lock fixer and offline npm installation. This branch has no database
migrations. Merge and deployment remain separate maintainer decisions.

Before merge, the committed dependency must use a compatible published release.
The optional development workflow installs a packed client checkout temporarily
without saving manifest or lockfile changes; `npm ci` restores the committed graph.
The registry transition will remove the archive-specific Nix adapter; the optional
development procedure remains available.

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

Vybraný klient zůstává nevydaný. Archiv s konkrétní revizí je v repozitáři jako
běžná závislost npm ze souboru s kontrolou původu a integrity. Nix při sestavení
frontendu doplní ověřený lokální archiv do dočasné mapy cache; původní úprava
lockfile a instalace npm bez přístupu k síti zůstávají zachované. Větev neobsahuje
databázové migrace. Sloučení a nasazení vyžadují samostatné rozhodnutí správce.

Před sloučením musí závislost v repozitáři používat kompatibilní vydanou verzi.
Při vývoji je možné dočasně nainstalovat archiv sestavený z lokálního checkoutu
klienta bez změny manifestu a lockfile. Příkaz `npm ci` obnoví závislosti podle
repozitáře. Při přechodu na vydanou verzi se odstraní část balení Nix určená pro
lokální archiv; volitelný vývojový postup zůstane dostupný.

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
  Strict E2E coverage is now 140 checked/142 deferred, with the original baseline,
  sourceRevision, compiler options and all surviving deferral records unchanged.
- Independent source/history and affected fixture reviews leave no findings
  unresolved. The direct semantic payload-assertion remedy and final factual
  work-log append were inspected separately. One generated-client input stream
  remains, with no database or persisted-format migrations.
- The isolated local-client build/pack/override/restore cycle passed on WebUI
  `8d0bb48a` / client `e16663a9`: typecheck, 23 binding tests, both forced Vite
  resolutions and full installed-client restoration. The packed README matches
  corrected source; the committed archive is unchanged.
- Isolated API: 23 calls through the generated client against API `610a96f8` and
  HaveAPI `0.32.0`, with native cleanup verified. Selected archive `99ee0665`
  remains an unpublished input.
- Nix frontend/BFF/provenance/source/package-content checks pass on exact
  `24ae8a8f`, exit 0 after 54.364 seconds. Both installed metadata files identify
  that full clean commit. The complete 1,801-derivation input graph and locked
  source identities are recorded; all 25 protected inputs match the committed,
  literal and filtered sources. Archive, generator and dependency pins are unchanged.

The published `20aa0e9e` [core CI](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41508552632)
passed all three jobs. Its [browser smoke run](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41508552554)
completed WebKit with 274 passed and 2 skipped; both Chrome jobs reached the
40-minute limit with partial assertion failures and retries, without final case summaries. The six-spec repair addresses those observed fixture
boundaries. Required full CI is pending for `24ae8a8f`; its exact-head Nix
packages and provenance checks have passed. Earlier browser and API checks retain
their actual revisions and input scopes.

These checks distinguish fixtures, isolated HTTP contracts and package output;
OAuth deployment and asynchronous worker acceptance remain separate. The visual
sample does not cover every changed control or unvisited language/reset state.

Requirements: REQ-005, REQ-007, REQ-011, REQ-012, REQ-054, REQ-056, REQ-060,
REQ-061 and REQ-068. Details are in the migration work log, API contracts and
workflow documentation in this branch.

[Review records and actual desktop/mobile images](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
