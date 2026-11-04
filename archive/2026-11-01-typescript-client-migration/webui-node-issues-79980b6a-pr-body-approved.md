## English

Run broad smoke on pull requests, pushes to every branch and manual dispatch,
with the existing Chromium/mobile Chrome selections, job limits, permissions,
artifacts and per-ref concurrency. Branch-protection settings are unchanged.

Correct the fixtures behind the 33 failed project cases: canonical response
frames and relations, complete lookup rows, supported filters, role-shaped
transactions and the existing request-review queue policy. A further node-filter
fixture now supplies typed public status data and waits for filtering to finish
before checking retained rows. This fixes the false-pass race seen in the PR
run. Existing rejection, identity, count and uncertain-write/no-replay assertions
remain. Ten repaired leaves join strict E2E coverage; larger test diffs include
whole-file formatting.

State-only bulk advisory updates previously cleared stored localized notes.
Each language now requires an explicit choice: unchecked preserves its note;
checked text sets a trimmed value; checked blank clears it. Localized help and
disabled fields explain the choice. The single-node editor, revision/state
guards, captured batch values and partial-progress/recovery behavior remain.
REQ055 and the owning workflow and CI documentation describe these rules.

Verification for `79980b6a6607d08cccd252439ced328a250bd5b0`:

- The corrected node-filter browser case passed with automatic retries disabled.
  Earlier affected-browser evidence retains 79 passes and one explicit viewport
  skip for unchanged inputs. Failed attempts and their diagnoses are preserved.
- Strict E2E checks pass with 153 checked / 130 deferred. Leaf lint/format,
  documentation checks and the retained application checks and 31 focused product
  tests pass for their exact inputs. Independent four-lane review is complete;
  the additional correction has no findings and the earlier finding is fixed.
- All five Nix targets built for this exact commit. Eight implemented EN/CS
  desktop/mobile screenshots are retained for unchanged UI inputs, with no
  submitted API mutations.

[Screenshots and detailed evidence](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
are in session Files, including `webui-bulk-notes-implemented-captures.md`.
Full current-head broad and required CI remain merge gates.

The compatible workflow-action refresh is a separate commit. Application
client/runtime dependencies, npm locks, flake inputs and Nix dependency hashes
are unchanged. There are no database or persisted-format migrations. Guarded
writes still require API `8225229a` or equivalent capabilities. Fixture checks
do not certify a live API.

## Česky

Rozšířené smoke testy se spouštějí u pull requestů, při pushi do každé větve
i ručně. Dosavadní výběr pro Chromium a mobilní Chrome, limity úloh, oprávnění,
artefakty i souběh podle refu zůstávají zachovány. Ochrana větví se nemění.

Opravená testovací data řeší příčiny 33 neúspěšných případů: obálky odpovědí
a vztahy podle kontraktu, úplné řádky pro výběr, podporované filtry, transakce
podle role a dosavadní chování fronty žádostí. Další test filtru nodů nyní
používá typované údaje o veřejném stavu a před kontrolou zbývajících řádků čeká
na dokončení filtrování. Oprava brání falešnému úspěchu, který se projevil
v běhu pro PR. Kontroly odmítnutí, identity, počtů a zákazu opakování nejistých
zápisů zůstávají. Deset opravených souborů nově prochází přísnou typovou
kontrolou E2E; větší rozdíly v testech zahrnují formátování celých souborů.

Hromadná změna stavu dříve mazala uložené jazykové poznámky k bezpečnostním
upozorněním. Každý jazyk nyní vyžaduje výslovnou volbu: nezaškrtnutý poznámku
ponechá, zaškrtnutý nastaví text bez okolních mezer a zaškrtnutý s prázdným
polem poznámku smaže. Volbu vysvětluje přeložená nápověda a neaktivní pole.
Editor jednoho nodu, kontroly revize a stavu, zachycené hodnoty dávky i chování
při částečném průběhu a obnově zůstávají. Pravidla popisuje REQ055 a příslušná
dokumentace workflow a CI.

Ověření pro `79980b6a6607d08cccd252439ced328a250bd5b0`:

- Opravený test filtru nodů prošel s vypnutým automatickým opakováním. Pro
  shodné vstupy zůstává platných dřívějších 79 úspěšných případů a jedno výslovné
  přeskočení podle velikosti viewportu. Neúspěšné pokusy a jejich diagnózy jsou
  zachovány.
- Přísná kontrola E2E prošla se 153 kontrolovanými a 130 odloženými soubory.
  Cílený lint, formátování, dokumentace, dřívější kontroly aplikace a 31 testů
  produktu prošly na přesně uvedených vstupech. Nezávislá kontrola ve čtyřech
  oblastech je hotová; další oprava je bez nálezů a původní nález je opraven.
- Prošlo všech pět cílů sestavení Nix z tohoto commitu. Osm snímků implementace
  v češtině a angličtině pro desktop a mobil platí pro shodné vstupy rozhraní;
  při jejich pořízení se neodesílaly změny do API.

[Snímky a podklady k ověření](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/)
jsou v souborech relace, včetně `webui-bulk-notes-implemented-captures.md`.
Celé rozšířené sady a povinné CI z aktuálního commitu zůstávají podmínkou začlenění.

Kompatibilní aktualizace akcí workflow je samostatný commit. Závislosti klienta
a běhového prostředí aplikace, npm lock soubory, vstupy flake a hashe závislostí
Nix se nemění. Nevzniká databázová migrace ani změna uloženého formátu. Chráněné
zápisy nadále vyžadují API `8225229a` nebo odpovídající schopnosti. Testovací
data neprokazují funkčnost živého API.
