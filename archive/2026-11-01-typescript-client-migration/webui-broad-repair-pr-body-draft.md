## English

Broad smoke now runs on pull requests, pushes to every branch, and manual
dispatch. It retains the existing Chromium and mobile Chrome selections,
45-minute job bound, per-ref concurrency and artifacts, so these failures can
be found before changes reach main.

The retained traces from all 33 failed project cases identified stale fixture
framing, field types, lookup resources and expectations, plus a bulk advisory
note bug. The fixtures now follow the generated wire contracts and current
filter and review-queue behavior. Existing rejection, malformed-response,
identity, count and no-replay assertions remain. Whole-file formatter changes
are mechanical; the request/WebAuthn functional patch is retained separately
for review.

Bulk advisory notes require an explicit selection for each language. Unchecked
languages keep their stored note. A checked language sets trimmed text, or
clears the note with null when blank. The textarea stays disabled until its language is selected; adjacent help
explains the choice. Cancel/reopen resets the bulk draft. State/revision checks, captured
batch intent, partial progress and refusal to replay uncertain writes remain.

Verification completed on the frozen source bytes, now bound to
`ebfdc1e320a80a1a08380ce0fd80b75b25c4baf1`:

- 31 focused helper/rendered/snapshot tests passed.
- Nine combined quick commands passed in 78.326 seconds: application strict,
  E2E strict and coverage (152 checked / 131 deferred), documentation,
  EN/CS catalogs and catalog structure, structural budgets, active docs,
  scoped formatting and whitespace. The original baseline, compiler options
  and surviving deferral records are preserved.
- Leaf lint/format and workflow YAML/structure checks passed for their retained
  exact inputs.

Independent final review, native affected browser verification, EN/CS desktop
and mobile synthetic captures, both full broad projects and exact-head Nix
packaging remain pending. No new captures or browser pass are claimed here.
Fixture checks do not establish live API or production acceptance.

The compatible setup-node/upload-artifact refresh is a separate first commit.
Generated client 0.4.0, HaveAPI 0.32.0, npm locks, flake inputs and package hashes
are unchanged; there are no database or persisted-format migrations. Guarded
advisory operations still require API `8225229a` or proven equivalent live
capabilities. The existing `4ed519b6` / API610 preview is unchanged.

## Česky

Rozšířená sada smoke testů se nově spouští u pull requestů, při pushi do každé
větve i ručně. Zachovává dosavadní výběr testů pro Chromium a mobilní Chrome,
45minutový limit úloh, souběh podle refu a artefakty. Chyby se tak mohou projevit
ještě před začleněním změn do hlavní větve.

U všech 33 neúspěšných případů v jednotlivých projektech ukázaly uložené trace
na zastaralé testovací odpovědi, typy polí, chybějící podklady pro výběr nebo
neplatná očekávání. Jeden případ odhalil chybu při hromadné změně poznámek
k bezpečnostním upozorněním. Testovací data nyní odpovídají generovanému
kontraktu a současnému filtrování i frontě žádostí. Kontroly odmítnutí,
neplatných odpovědí, identity, počtů a zákazu opakování zápisů zůstávají.
Formátování celých souborů je mechanické; funkční změny testů žádostí a WebAuthn
jsou pro kontrolu uložené i samostatně.

Při hromadné úpravě poznámek je nutné zvolit každý jazyk zvlášť. Nezaškrtnutý
jazyk ponechá uloženou poznámku. Zaškrtnutý jazyk nastaví zadaný text bez
okolních mezer, nebo poznámku při prázdném vstupu výslovně smaže hodnotou null.
Textové pole je pro nezaškrtnutý jazyk neaktivní a sousední nápověda vysvětluje
volbu. Zavření a nové otevření hromadné úpravy návrh resetuje. Kontroly stavu a revize, zachycený záměr dávky,
částečný průběh a zákaz opakování nejistých zápisů zůstávají.

Na neměnných zdrojových datech svázaných s commitem
`ebfdc1e320a80a1a08380ce0fd80b75b25c4baf1` prošlo 31 cílených testů a všech
9 rychlých kontrol za 78,326 sekundy. Prošla přísná typová kontrola aplikace
a E2E (152 kontrolovaných / 131 odložených souborů), dokumentace, české a
anglické katalogy a jejich struktura, strukturální limity, aktivní dokumentace,
cílené formátování a kontrola bílých znaků. Původní baseline, nastavení
překladače a zbývající záznamy odložených souborů zůstaly zachovány. Cílený lint,
formátování a kontrola YAML workflow prošly pro uvedené shodné vstupy.

Závěrečná nezávislá kontrola, ověření dotčených scénářů v prohlížeči, syntetické
snímky v češtině a angličtině pro desktop a mobil, obě celé rozšířené sady a
Nix balíčky z přesného finálního commitu zatím čekají. Nové snímky ani úspěšný
běh prohlížečových testů zde netvrdíme. Testovací odpovědi neprokazují funkčnost
živého API ani připravenost produkce.

Kompatibilní aktualizace setup-node a upload-artifact tvoří samostatný první
commit. Generovaný klient 0.4.0, HaveAPI 0.32.0, npm lock soubory, vstupy flake
a hashe balíčků se nemění; nevzniká databázová migrace ani změna uloženého
formátu. Chráněné operace bezpečnostních upozornění nadále vyžadují API
`8225229a` nebo prokázaně odpovídající schopnosti živého API. Dosavadní náhled
`4ed519b6` / API610 se nemění.
