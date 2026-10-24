The WebUI uses the packaged HaveAPI `AsyncClient` for normal authenticated requests, public reads and API-description discovery. This removes its custom fetch transport and duplicate wire encoding/decoding while preserving WebUI session renewal, live credentials, cancellation, result shapes and mutation safeguards. Writes are never automatically replayed after renewal.

The unreleased client is a normal dependency from a committed npm archive of HaveAPI `f94e65e`, with lock integrity and source provenance. Nix uses its pinned `importNpmLock` support for that archive. No npm release is required to build or test this PR. The former standalone pilot is removed; its dated evidence remains historical.

Quick verification: 39 changed API test files / 289 cases, app/tooling/E2E type checks, scoped lint/format, documentation and structural audits, plus six source-package checks passed. Independent final review, full application tests/build, Nix package checks and ordinary browser workflows are pending. No deployment or live OAuth certification is claimed. REQ-007, REQ-011, REQ-012, REQ-059 and REQ-068.

---

WebUI používá balíček HaveAPI `AsyncClient` pro běžné autentizované požadavky, veřejná data i načítání popisu API. Vlastní transport přes fetch a duplicitní kódování a dekódování protokolu se odstraňují. Obnova relace, aktuální přihlašovací údaje, rušení požadavků, návratové hodnoty a ochrana změnových operací zůstávají ve WebUI. Po obnově relace se změnový požadavek nikdy automaticky neopakuje.

Dosud nevydaný klient je běžnou závislostí z npm archivu uloženého v repozitáři, vytvořeného z HaveAPI `f94e65e`. Lockfile a záznam původu vážou závislost na přesný obsah. Nix používá podporu `importNpmLock` ze své připnuté verze. Sestavení ani testování PR nevyžaduje vydání na npm. Samostatný pilot se odstraňuje, jeho datované výsledky zůstávají historickým záznamem.

Rychlé kontroly prošly: 39 změněných souborů s testy API / 289 případů, typové kontroly aplikace, nástrojů a E2E, lint a formátování změn, kontroly dokumentace a struktury i šest kontrol zdrojového balíčku. Nezávislá závěrečná revize, úplné testy a sestavení aplikace, kontroly balíčků Nix a běžné prohlížečové scénáře ještě čekají. Změna není nasazená a nepotvrzuje funkčnost skutečné výměny OAuth tokenů. REQ-007, REQ-011, REQ-012, REQ-059 a REQ-068.
