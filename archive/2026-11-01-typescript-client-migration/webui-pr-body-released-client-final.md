## English

WebUI uses the generated TypeScript client for vpsAdmin API operations and descriptions. HaveAPI still encodes requests and decodes replies. The shared WebUI policy retains authentication, language, anonymous-client isolation and recovery for reads. Writes preserve their receipts and cannot be replayed when the outcome is uncertain.

Domain callers validate generated responses and expose supported controls. For example, an advisory draft retains its accepted parent and original CVE intent when a child sequence stops, so review can preserve unresolved work without creating another parent. The migration also corrects resource associations, asynchronous receipts and fixtures that described unsupported response shapes.

The committed dependency is published `vpsadmin-typescript-client@0.3.0`, selected by exact version, registry URL and integrity. All 1,352 shipped JavaScript and declaration files match the tested `99ee0665` candidate byte for byte. The released source and generator provenance are distinct and documented; the consumer runtime peer remains `haveapi-client@0.32.0`.

Frontend Nix packaging uses ordinary registry dependency fetching. The temporary tracked archive, archive provenance and cache adapter are removed; HaveAPI/XHR provenance and source-security guards remain. The optional local workflow still supports `npm pack` and a no-save installation, with `npm ci` restoring the committed graph. No database or persisted-format migrations are introduced.

## Česky

WebUI používá generovaného TypeScript klienta pro operace API vpsAdminu a jejich popisy. HaveAPI dál sestavuje požadavky a zpracovává odpovědi. Společná vrstva WebUI zachovává přihlašování, jazyk, oddělené anonymní klienty a obnovu požadavků pro čtení. U zápisů uchovává potvrzení akce a při nejistém výsledku brání opakovanému odeslání.

Volající ověřují odpovědi podle generovaného kontraktu a zobrazují podporované ovládací prvky. Když se například zastaví přidávání CVE do konceptu upozornění, zůstane zachovaný přijatý koncept i původní záměr. Následná kontrola tak zachová nedořešené změny a nevytvoří další koncept. Migrace také opravuje vazby na zdroje, potvrzení asynchronních akcí a testovací odpovědi, které neodpovídaly API.

Závislost v repozitáři používá vydaný `vpsadmin-typescript-client@0.3.0` s přesnou verzí, adresou registru a integritou archivu. Všech 1 352 vydaných souborů JavaScriptu a deklarací se bajt po bajtu shoduje s testovaným kandidátem `99ee0665`. Zdrojová revize vydání a původ generátoru jsou odlišné a zaznamenané v dokumentaci. Přesná závislost na běhové knihovně zůstává `haveapi-client@0.32.0`.

Nix při sestavení frontendu používá běžné stahování závislostí z registru. Dočasný archiv v repozitáři, jeho záznam původu a úprava cache jsou odstraněné; kontroly původu HaveAPI/XHR a bezpečnosti zdrojů zůstávají zachované. Volitelný vývojový postup dál umožňuje použít `npm pack` a dočasnou instalaci bez změny manifestu a lockfile. Příkaz `npm ci` obnoví závislosti podle repozitáře. Změna neobsahuje databázové migrace ani změny formátu uložených dat.

## Verification / Ověření

Released-client transition at `4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e`:

- All 1,360 installed package files match the verified release archive. Only the root client selector and client lock record changed; 484 other lock records are preserved. Public exports and the resolved HaveAPI peer were verified.
- Six source-checker tests and 100 policy/wire tests across six files passed against the installed release. Application, tooling and E2E strict checks passed, including 141 checked E2E files with 141 deferred. Scoped lint, formatting, Nix syntax and the design-documentation audit passed.
- Independent final affected review completed all four lanes with no findings, including the complete 37-commit history, the external release boundary and migration inventory. All 36 earlier published commits are preserved.
- Nix frontend, BFF, provenance, source-content and package-content checks passed on the exact commit, native exit 0 in 54.957 seconds. Both installed build-info files identify the full clean commit.

The preceding candidate `b5c12bcd` passed [core CI](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41548300724) and the [browser matrix](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41548300683): 2,227 application tests in 343 files; Chromium 632 passed, mobile Chrome 574 passed, and mobile WebKit 274 passed with 2 skipped, without failures or retries. Its focused support-account scenario preserves the foreign owner, positive and negative permission assertions across all tabs, and the final no-mutations assertion. The released-client transition changes no application or browser-fixture code; that full matrix was not repeated solely for identical distributed programs.

Earlier isolated API evidence covers 23 generated-client calls against API `610a96f8` and HaveAPI `0.32.0` using candidate `99ee0665`, with native cleanup verified. Earlier browser, packaging, optional local-client and desktop/mobile visual evidence retain their recorded revisions and input scopes in the migration work log. They are not relabeled as executions on the registry-transition head. npm still reports 12 moderate advisories; no unrelated dependency repair is included.

These checks distinguish synthetic fixtures, isolated HTTP contracts and package output. They do not certify live authorization, OAuth deployment or asynchronous worker completion. The visual samples do not cover every changed control or unvisited language/reset state.

The candidate remains based on `63d484fc`; `main` has advanced to `1c8478bc`. Reconciling that upstream change is a separate integration step. Merge and production deployment remain maintainer decisions; this PR does not claim readiness to merge the current `main`.

Requirements: REQ-005, REQ-007, REQ-011, REQ-012, REQ-054, REQ-056, REQ-060, REQ-061 and REQ-068. Current contracts, packaging instructions and the detailed migration record are included in this branch.

[Review records and actual desktop/mobile images](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
