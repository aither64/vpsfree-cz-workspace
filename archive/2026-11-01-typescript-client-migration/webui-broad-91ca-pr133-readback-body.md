## English

Broad smoke now runs on pull requests, pushes to every branch and manual dispatch.
The existing Chromium/mobile Chrome suites, permissions, job limits, artifacts
and per-ref concurrency are preserved. Branch-protection settings are unchanged.

Fix the API fixtures behind the 33 failed project cases: canonical response
frames and relations, complete lookup rows, supported filters, role-shaped
transactions and the existing request-review queue behavior. Keep the rejection,
identity, count and uncertain-write/no-replay assertions. Nine repaired leaves
join strict E2E coverage; whole-file formatting accounts for much of the test diff.

State-only bulk advisory updates previously cleared existing localized notes.
Each language now requires an explicit choice: unchecked preserves its note;
checked text sets a trimmed value; checked blank clears it. Localized help and
disabled fields explain the choice. The single-node editor, revision/state guards,
captured batch values and partial-progress/recovery behavior are preserved.
REQ055 and the owning workflow and CI documentation describe these rules.

Local verification for `91ca5ab44d07d62a8226f5a2b774747a44ff2c0d`:

- Affected browsers: 79 passed, one explicit viewport skip, automatic retries disabled. A
  request-test modal-order failure was diagnosed and corrected before continuation.
- 31 focused product tests and quick checks passed for their exact retained
  inputs; fresh E2E strict passed with 152 checked / 131 deferred. Independent
  four-lane final review is complete, with its sole Important finding fixed.
- Five Nix build targets passed. Four EN/CS desktop/mobile capture cases passed,
  producing eight implemented screenshots with no submitted API mutations.

[Screenshots and verification evidence](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
are in the session Files, including `webui-bulk-notes-implemented-captures.md`.
Full broad and required CI run for this PR and remain merge gates.

The compatible workflow-action refresh is a separate commit. Application
client/runtime dependencies, npm locks, flake inputs and package hashes are
unchanged. There are no database or persisted-format migrations. Guarded writes
still require API `8225229a` or equivalent capabilities. Fixtures do not certify
a live API; the existing preview and production are unchanged.

## Česky

Rozšířené smoke testy se nově spouštějí u pull requestů, při pushi do každé větve
i ručně. Dosavadní sady pro Chromium a mobilní Chrome, oprávnění, limity úloh,
artefakty i souběh podle refu zůstávají zachovány. Ochrana větví se nemění.

Oprava testovacích dat řeší příčiny 33 neúspěšných případů: obálky odpovědí
a vztahy podle kontraktu, úplné řádky pro výběr, podporované filtry, transakce
podle role uživatele a dosavadní chování fronty žádostí. Kontroly odmítnutí,
identity, počtů a zákazu opakování nejistých zápisů zůstávají. Devět opravených
souborů nově prochází přísnou typovou kontrolou E2E; velkou část rozdílů
v testech tvoří formátování celých souborů.

Hromadná změna stavu dříve mazala uložené jazykové poznámky k bezpečnostním
upozorněním. Každý jazyk nyní vyžaduje výslovnou volbu: nezaškrtnutý poznámku
ponechá, zaškrtnutý nastaví text bez okolních mezer a zaškrtnutý s prázdným
polem poznámku smaže. Volbu vysvětluje přeložená nápověda a neaktivní pole.
Editor jednoho uzlu, kontroly revize a stavu, zachycené hodnoty dávky i chování
při částečném průběhu a obnově zůstávají zachovány. Pravidla popisuje REQ055
a příslušná dokumentace workflow a CI.

Místní ověření pro `91ca5ab44d07d62a8226f5a2b774747a44ff2c0d`:

- V prohlížečích prošlo 79 případů, jeden byl výslovně přeskočen podle velikosti
  viewportu, s vypnutým automatickým opakováním. Chyba pořadí ovládání dialogu
  v testu žádosti
  byla před pokračováním diagnostikována a opravena.
- Prošlo 31 cílených testů produktu a rychlé kontroly na shodných uložených
  vstupech. Nový běh přísné kontroly E2E prošel se 152 kontrolovanými a 131
  odloženými soubory. Závěrečná nezávislá kontrola ve čtyřech oblastech je hotová;
  její jediný závažný nález byl opraven.
- Prošlo všech pět cílů sestavení Nix. Čtyři případy pro češtinu a angličtinu
  na desktopu a mobilu vytvořily osm snímků implementace bez odeslání změn do API.

[Snímky a podklady k ověření](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
jsou v souborech relace, včetně `webui-bulk-notes-implemented-captures.md`.
Celé rozšířené sady a povinné CI se spouštějí pro tento PR a zůstávají podmínkou
začlenění.

Kompatibilní aktualizace akcí workflow je samostatný commit. Závislosti klienta
a běhového prostředí aplikace, npm lock soubory, vstupy flake a hashe balíčků se
nemění. Nevzniká databázová migrace ani změna uloženého formátu. Chráněné zápisy
nadále vyžadují API `8225229a` nebo odpovídající schopnosti. Testovací data
neprokazují funkčnost živého API; dosavadní náhled ani produkce se nemění.
