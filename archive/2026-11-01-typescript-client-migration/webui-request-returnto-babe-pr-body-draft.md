## English

Run broad smoke on pull requests, pushes to every branch and manual dispatch.
The existing Chromium/mobile Chrome selections, job limits, permissions,
artifacts and per-ref concurrency remain. Branch-protection settings are unchanged.

Correct the fixtures behind the 33 failed project cases: canonical response
frames and relations, complete lookup rows, supported filters, role-shaped
transactions and the existing request-review queue policy. The node-filter
fixture also supplies typed public status data and waits for filtering before
checking retained rows. Rejection, identity, count and uncertain-write/no-replay
assertions remain. Ten repaired leaves join strict E2E coverage; larger test
diffs include whole-file formatting.

State-only bulk advisory updates previously cleared stored localized notes.
Each language now requires an explicit choice: unchecked preserves its note;
checked text sets a trimmed value; checked blank clears it. Localized help and
disabled fields explain the choice. The single-node editor, revision/state
guards, captured batch values and partial-progress/recovery behavior remain.
REQ055 and the owning workflow and CI documentation describe these rules.

An asynchronous request ID lookup could restore legacy `q` in its return path
after the list URL had been normalized. Return paths now remove `q` when they
are captured, preserving other filters and pagination. The existing browser
assertion stays unchanged; model regressions cover stale and duplicate `q`,
parameter order and input immutability.

Verification for `babe51421bd1df61a548e7b2f047053df14ff3eb`:

- Nine request-model tests, application type checking, required project lint,
  formatting and documentation checks passed on exact inputs later committed.
  An extra direct lint of RequestsPage retains three unchanged baseline hook
  diagnostics; the comparison and scope limit are recorded for review.
- Strict E2E evidence remains 153 checked / 130 deferred, with unchanged
  dependency inputs. Earlier affected-browser evidence retains 79 passes and
  one viewport skip, plus the corrected node-filter case. The 31 advisory tests
  and eight implemented EN/CS desktop/mobile images retain their actual scope
  for unchanged advisory components; captures submitted no API mutations.
- Independent affected review and current-head focused browser, five Nix targets and
  automatic required/full broad CI remain pending. These are merge gates.

[Screenshots and detailed evidence](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
are in session Files, including `webui-bulk-notes-implemented-captures.md`.
Original failed attempts and their diagnoses remain available.

The compatible workflow-action refresh is a separate commit. Application
client/runtime dependencies, npm locks, flake inputs and Nix dependency hashes
are unchanged. There are no database or persisted-format migrations. Guarded
writes still require API `8225229a` or equivalent capabilities. Fixture checks
do not certify a live API.

## Česky

Rozšířené smoke testy se spouštějí u pull requestů, při pushi do každé větve
i ručně. Dosavadní výběr pro Chromium a mobilní Chrome, limity úloh, oprávnění,
artefakty i souběh podle refu zůstávají. Ochrana větví se nemění.

Opravená testovací data řeší příčiny 33 neúspěšných případů: obálky odpovědí
a vztahy podle kontraktu, úplné řádky pro výběr, podporované filtry, transakce
podle role a dosavadní chování fronty žádostí. Test filtru nodů navíc používá
typované údaje o veřejném stavu a před kontrolou zbývajících řádků čeká na
filtrování. Kontroly odmítnutí, identity, počtů a zákazu opakování nejistých
zápisů zůstávají. Deset opravených souborů nově prochází přísnou typovou
kontrolou E2E; větší rozdíly v testech zahrnují formátování celých souborů.

Hromadná změna stavu dříve mazala uložené jazykové poznámky k bezpečnostním
upozorněním. Každý jazyk nyní vyžaduje výslovnou volbu: nezaškrtnutý poznámku
ponechá, zaškrtnutý nastaví text bez okolních mezer a zaškrtnutý s prázdným
polem poznámku smaže. Volbu vysvětluje přeložená nápověda a neaktivní pole.
Editor jednoho nodu, kontroly revize a stavu, zachycené hodnoty dávky i chování
při částečném průběhu a obnově zůstávají. Pravidla popisuje REQ055 a příslušná
dokumentace workflow a CI.

Asynchronní vyhledání žádosti podle ID mohlo v návratové adrese obnovit
nepodporovaný `q`, přestože URL seznamu už byla upravená. Návratové adresy nyní
vynechají `q` hned při sestavení a zachovají ostatní filtry i stránkování.
Původní kontrola v prohlížeči se nemění; testy modelu ověřují starý i opakovaný
`q`, pořadí parametrů a neměnnost vstupu.

Ověření pro `babe51421bd1df61a548e7b2f047053df14ff3eb`:

- Devět testů modelu žádostí, typová kontrola aplikace, povinný lint projektu,
  formátování a kontroly dokumentace prošly na přesně shodných vstupech, které
  byly následně zahrnuty do commitu. Dodatečný přímý lint RequestsPage nadále hlásí tři
  původní chyby závislostí hooků; porovnání a rozsah tohoto omezení jsou doložené.
- Přísná kontrola E2E zůstává na 153 kontrolovaných a 130 odložených souborech se
  shodnými závislostmi. Dřívější cílené běhy zahrnují 79 úspěšných případů a jedno
  přeskočení podle viewportu, navíc opravený test filtru nodů. Pro nezměněné
  komponenty upozornění zůstává zachován skutečný rozsah 31 testů a osmi snímků
  implementace v češtině a angličtině pro desktop a mobil; při pořízení snímků
  se neodesílaly změny do API.
- Nezávislá kontrola opravy a cílený běh v prohlížeči, všech pět cílů Nix i povinné a celé
  rozšířené CI z aktuálního commitu zatím čekají. Zůstávají podmínkou začlenění.

[Snímky a podklady k ověření](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
jsou v souborech relace, včetně `webui-bulk-notes-implemented-captures.md`.
Původní neúspěšné pokusy a jejich diagnózy zůstávají dostupné.

Kompatibilní aktualizace akcí workflow je samostatný commit. Závislosti klienta
a běhového prostředí aplikace, npm lock soubory, vstupy flake a hashe závislostí
Nix se nemění. Nevzniká databázová migrace ani změna uloženého formátu. Chráněné
zápisy nadále vyžadují API `8225229a` nebo odpovídající schopnosti. Testovací
data neprokazují funkčnost živého API.
