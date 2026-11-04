## English

WebUI now uses generated vpsAdmin SDK actions for API operations and descriptions.
HaveAPI still encodes requests and decodes replies. WebUI retains authentication,
language, anonymous-client isolation and read-only recovery; it preserves write
receipts and blocks replay when the outcome is uncertain.

Domain callers validate the generated contract and expose supported controls.
For example, an advisory draft keeps its accepted parent and original CVE intent
when a child sequence stops, so review does not create another parent or lose
unresolved work. The migration also corrects resource associations, asynchronous
receipts and fixtures that described unsupported response shapes.

The SDK stays unpublished. A tracked, revision-qualified SDK archive uses an
ordinary npm file dependency, checked provenance and integrity. Frontend Nix
packaging adds the verified local archive to the transient cache map and retains
the upstream lock fixer and offline npm installation. This branch has no database
migrations. Merge and deployment remain separate maintainer decisions.

## Česky

WebUI používá generované akce SDK vpsAdminu pro operace API i jejich popisy.
HaveAPI dál sestavuje požadavky a zpracovává odpovědi. WebUI zachovává přihlašování,
jazyk, oddělené anonymní klienty a obnovu požadavků pouze pro čtení. U zápisů
uchovává potvrzení akce a při nejistém výsledku brání opakovanému odeslání.

Volající ověřují data podle generovaného kontraktu a zobrazují podporované
ovládací prvky. Když se například zastaví přidávání CVE do konceptu upozornění,
zůstane zachovaný přijatý koncept i původní záměr. Následná kontrola tak nevytvoří
další koncept ani neztratí nedořešené změny. Migrace také opravuje vazby na zdroje,
potvrzení asynchronních akcí a testovací odpovědi, které neodpovídaly API.

SDK zůstává nevydané. Verzovaný archiv s konkrétní revizí je v repozitáři jako
běžná závislost npm ze souboru s kontrolou původu a integrity. Nix při sestavení
frontendu doplní ověřený lokální archiv do dočasné mapy cache; původní úprava
lockfile a instalace npm bez přístupu k síti zůstávají zachované. Větev neobsahuje
databázové migrace. Sloučení a nasazení vyžadují samostatné rozhodnutí správce.

## Verification / Ověření

- Application: 2,227 tests in 343 files; BFF: 58 tests; affected script, compiler,
  lint and documentation checks pass.
- Synthetic browser workflows: 124 desktop/mobile cases, plus 8 selected Czech/
  English capture cases. Actual images retain locale, viewport and trace provenance.
- Isolated API: 23 SDK calls against API610a96f8 and HaveAPI0.32.0; native cleanup
  verified. SDK candidate99ee0665 remains unpublished.
- Nix frontend/BFF/provenance/source/package-content graph passes on exact final
  `14cfdcb6`; realized frontend/BFF metadata identifies that clean commit. PR CI
  is pending.

These checks distinguish fixtures, isolated HTTP contracts and package output;
OAuth deployment and asynchronous worker acceptance remain separate. The visual
sample does not cover every changed control or unvisited language/reset state.

Requirements: REQ-005, REQ-007, REQ-011, REQ-012, REQ-054, REQ-056, REQ-060,
REQ-061 and REQ-068. Details are in the migration work log, API contracts and
workflow documentation in this branch.

[Review records and actual desktop/mobile images](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
