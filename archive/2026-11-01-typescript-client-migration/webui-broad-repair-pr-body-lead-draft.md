## English

Broad smoke runs on pull requests, pushes to every branch, and manual dispatch.
The Chromium and mobile Chrome selections, 45-minute job limit, permissions,
per-ref concurrency and artifacts are preserved. This makes the broad results
available before merge; branch-protection settings are unchanged.

The 33 failures from the main-branch run exposed stale test fixtures and a real
bulk advisory-note bug. Fixtures now use the declared response frames, relations
and field types, complete lookup resources, supported filters and the existing
request-review queue policy. Transaction fixtures distinguish member and admin
responses; admin payloads use the declared JSON-string output. Existing rejection,
count, identity and no-replay assertions remain. Much of the larger test diff is
whole-file formatting. Nine repaired leaves also join strict E2E coverage.

Bulk advisory notes now require a separate selection for each language.
Unchecked languages preserve their stored note. Checked languages set trimmed
text, or explicitly clear the note when the field is blank. The disabled field
and adjacent help explain this choice. Closing and reopening resets the bulk
form. Revision/state guards, captured batch values, partial progress and refusal
to replay uncertain writes are preserved; the single-node editor is unchanged.

Verification at `c1ad3e253ee7953fde8c5734cfa8a4d971854614`:

- 31 focused product tests passed with unchanged final production/test inputs.
- Application strict checks, catalogs, documentation and structural checks passed
  on their retained exact inputs. E2E strict passed again after the review fix:
  152 checked / 131 deferred, with the original baseline, compiler options and
  surviving deferrals preserved. Scoped lint, formatting and workflow checks pass.
- Independent final review covered the complete seven-commit series in four
  lanes. Its one Important finding was fixed and verified by focused inspection.
- The first affected browser batch stopped at a request-test interaction failure:
  42 passed, one failed, one interrupted, one skipped and 25 did not run; mobile
  did not run. Diagnosis and correction precede another attempt. EN/CS desktop/
  mobile captures, full broad, required CI and exact-head Nix remain pending.

The compatible workflow-action refresh is a separate commit. Client 0.4.0,
HaveAPI 0.32.0, npm locks, flake inputs and package hashes are unchanged. There
are no database or persisted-format migrations. Guarded advisory writes still
require API `8225229a` or equivalent capabilities. Browser fixtures do not certify
a live API; the existing preview and production are unchanged. REQ055 and the
owning workflow/CI documentation describe the behavior.

## Česky

Rozšířené smoke testy se spouštějí u pull requestů, při pushi do každé větve
i ručně. Výběr testů pro Chromium a mobilní Chrome, 45minutový limit úloh,
oprávnění, souběh podle refu i artefakty zůstávají zachovány. Výsledky tak budou
k dispozici před začleněním změn. Nastavení ochrany větví se nemění.

33 neúspěšných případů z běhu na hlavní větvi odhalilo zastaralé testovací
odpovědi a chybu při hromadné úpravě poznámek k bezpečnostním upozorněním.
Testovací data nyní používají deklarované obálky odpovědí, vztahy a typy polí,
úplné podklady pro výběr, podporované filtry a dosavadní chování fronty žádostí.
Transakce mají odlišné odpovědi pro člena a administrátora; administrátorský
výstup obsahuje deklarovaný řetězec JSON. Kontroly odmítnutí, počtů, identity
a zákazu opakování zápisů zůstávají. Větší část rozdílů v testech tvoří
formátování celých souborů. Devět opravených souborů nově prochází přísnou
kontrolou typů E2E.

Při hromadné úpravě poznámek se každý jazyk volí zvlášť. Nezaškrtnutý jazyk
ponechá uloženou poznámku. Zaškrtnutý jazyk nastaví text bez okolních mezer,
nebo poznámku při prázdném vstupu výslovně smaže. Neaktivní textové pole
a sousední nápověda tuto volbu vysvětlují. Zavření a nové otevření hromadné
úpravy formulář resetuje. Kontroly revize a stavu, zachycené hodnoty dávky,
částečný průběh a zákaz opakování nejistých zápisů zůstávají; editor jednoho
uzlu se nemění.

Ověření pro `c1ad3e253ee7953fde8c5734cfa8a4d971854614`:

- Prošlo 31 cílených testů při zachování přesných vstupů finálního produktu a testů.
- Přísná kontrola typů aplikace, katalogů, dokumentace a strukturálních limitů
  prošla na uložených shodných vstupech. Po opravě z nezávislé kontroly znovu
  prošla přísná kontrola E2E: 152 kontrolovaných / 131 odložených souborů.
  Původní baseline, volby překladače a zbývající odklady zůstaly zachovány.
  Prošly také cílený lint, formátování a kontroly workflow.
- Nezávislá závěrečná kontrola posoudila všech sedm commitů ve čtyřech oblastech.
  Její jediný závažný nález byl opraven a ověřen cílenou kontrolou.
- První ověření v prohlížeči zastavila chyba v ovládání testu žádosti: 42 případů
  prošlo, jeden selhal, jeden byl přerušen, jeden přeskočen a 25 se nespustilo.
  Mobilní sada se nespustila. Před dalším během následuje diagnóza a oprava.
  Syntetické snímky pro oba jazyky a velikosti, celé rozšířené sady, povinné CI
  a Nix balíčky z přesného commitu zatím čekají.

Kompatibilní aktualizace akcí workflow je samostatný commit. Klient 0.4.0,
HaveAPI 0.32.0, npm lock soubory, vstupy flake a hashe balíčků se nemění.
Nevzniká databázová migrace ani změna uloženého formátu. Chráněné zápisy nadále
vyžadují API `8225229a` nebo odpovídající schopnosti. Testovací odpovědi
neprokazují funkčnost živého API; dosavadní náhled ani produkce se nemění.
Chování popisuje REQ055 a příslušná dokumentace workflow a CI.
