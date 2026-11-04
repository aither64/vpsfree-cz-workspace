## English

WebUI uses the generated TypeScript client for vpsAdmin API operations and live action descriptions. HaveAPI retains request encoding and response decoding. The shared WebUI policy preserves authentication, language, anonymous-client isolation and read recovery. Mutations retain complete receipts and stop without replay when their outcome is uncertain.

The branch now uses the published `vpsadmin-typescript-client@0.4.0` and is rebased onto main `1c8478bc`. The runtime remains `haveapi-client@0.32.0`. Advisory corrections and lifecycle actions introduced on main use generated operations and descriptions, including callers in new files that arrived without Git conflicts. Revision and state guards, parent/child snapshots, partial progress and unresolved edits remain part of the workflow. Capability checks cover the effective actions before a sequence starts writing.

Frontend Nix packaging uses ordinary registry dependencies. The client manifest, lock record and frontend dependency hash form one final update in the 36-commit series. The series never introduces the obsolete tracked archive, archive provenance or cache adapter. The documented local workflow still supports packed snapshots and temporary no-save installation, with `npm ci` restoring committed dependencies. The change introduces no database or persisted-format migrations.

Guarded advisory writes require a backend that advertises the supported actions, guard parameters and allowed states. An API version number alone does not establish compatibility. Missing capabilities cause a visible refusal before writing. This PR does not certify production authorization, OAuth deployment or asynchronous worker completion.

An inherited limitation remains: CVE ordering by `cve_id` differs from the numeric ID cursor, so multi-page collection can omit CVEs. The contract records a separate producer/cursor follow-up.

## Česky

WebUI používá generovaného klienta v TypeScriptu pro operace API vpsAdminu a aktuální popisy akcí. HaveAPI dál sestavuje požadavky a zpracovává odpovědi. Společná vrstva WebUI zachovává přihlašování, jazyk, oddělené anonymní klienty a obnovu požadavků pro čtení. U zápisů uchovává úplná potvrzení akcí a při nejistém výsledku brání opakovanému odeslání.

Větev používá vydaný `vpsadmin-typescript-client@0.4.0` a vychází z větve main `1c8478bc`. Běhová knihovna zůstává `haveapi-client@0.32.0`. Opravy bezpečnostních upozornění a změny jejich životního cyklu přidané do main používají generované operace a popisy akcí. To zahrnuje i volání v nových souborech bez konfliktu v Gitu. Zůstávají zachované kontroly revize a stavu, snímky nadřazeného záznamu a jeho vazeb, částečný postup i nedořešené úpravy. Před prvním zápisem se ověřují všechny akce potřebné pro daný postup.

Nix při sestavení frontendu používá běžné závislosti z registru. Manifest klienta, jeho záznam v lockfile a hash závislostí frontendu tvoří jedinou aktualizaci v řadě 36 commitů. Dočasný archiv, jeho záznam původu ani úprava cache se v této řadě nevyskytují. Dokumentovaný místní vývoj dál umožňuje použít zabalený klient a dočasnou instalaci bez změny manifestu a lockfile. Příkaz `npm ci` obnoví závislosti podle repozitáře. Změna neobsahuje databázové migrace ani změny formátu uložených dat.

Zápisy do bezpečnostních upozornění vyžadují backend, který nabízí podporované akce, kontrolní parametry a povolené stavy. Samotné číslo verze API kompatibilitu nepotvrzuje. Pokud potřebná schopnost chybí, WebUI zápis viditelně odmítne před odesláním. Tento PR nepotvrzuje oprávnění v produkci, nasazení OAuth ani dokončení asynchronních úloh.

Přetrvává známé omezení: řazení CVE podle `cve_id` se liší od kurzoru podle číselného ID, takže výpis přes více stránek může některé CVE vynechat. Sjednocení řazení a kurzoru zůstává samostatným úkolem.

## Verification / Ověření

Candidate: `670cf286daf9bddb65594035507ca112a9e6d397`, tree `51c71ab123c4f10266fafb9b2e895c78d0915053`, based on `1c8478bceb3943645ec06ccde895ee4b0985873f`.

- All 1,364 installed client files match the verified 0.4.0 archive. Public exports, generated descriptions and the resolved HaveAPI peer were inspected. The 484 unrelated root lock records remain unchanged from main.
- Application strict typing passed with zero diagnostics in 57.974 seconds. Tooling and E2E strict checks passed with 143 checked files and 140 deferred. These results are bound to the retained source and compiler inputs; they are not literal final-head executions.
- Six source-checker tests passed. Affected Vitest continuations passed after the recorded initial failures, including the final node-panel checks across three files and 12 tests, the editor test, and the API state/revision negatives. No single aggregate Vitest pass count is claimed.
- The accepted-parent recovery regression passed across four focused files and nine tests, including null/contradictory revision responses, zero child writes and intent/block persistence after reopening and attempted resubmission.
- Scoped lint, formatting, documentation, catalogs, structural checks, API-barrel checks, Nix syntax and whitespace checks passed. The final work-log appendix received its own documentation and formatting checks.

The complete 36-commit series was independently reviewed in all four lanes at `db90da33`. Its Important accepted-parent recovery finding is fixed and verified in this candidate under the review policy’s narrow-fix rule. The inherited CVE paging limitation remains documented.

Standalone Nix frontend, BFF, provenance, source-content and package-content checks passed on literal `670cf286` in 66.96 seconds. Both installed metadata records identify clean `670cf286`; the full input graph and protected source/lock bindings were inspected. Transient dependency caches were unavailable for later archive rereads; those limits are recorded without a new cache-byte certificate.

[Core CI](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41691007867) and the [browser matrix](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41691007905) passed all six jobs on attempt 1: 2,252 unit tests in 348 files; Chromium 632 passed, mobile Chrome 574 passed, and mobile WebKit 274 passed with 2 skipped. No failures or flaky retries were observed. The ordinary PR checkout was merge commit `75c58bf57f10d6017d8e75bbeed6021e0558bc78`, whose tree exactly matches `670cf286` and whose parents are `1c8478bc` and `670cf286`. This distinguishes the tested merge checkout from the feature commit. Production build and Chromium script regressions also passed.

The earlier `b5c12bcd` candidate passed [core CI](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41548300724) and the [browser matrix](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41548300683): 2,227 application tests in 343 files; Chromium 632 passed, mobile Chrome 574 passed, and mobile WebKit 274 passed with 2 skipped, without failures or retries. Those results retain their original source scope. Earlier isolated API evidence covers 23 calls against API `610a96f8` using the earlier client candidate; it does not verify the new advisory guards.

The running preview remains on the preserved `4ed519b6` revision and its original backend. That commit is not an ancestor of this successor. The preview has not been updated, and its running API is not a compatible validation backend for the new advisory guards. The rebase includes substantive current-main behavior; no patch-equivalence or deployed-successor claim is made.

Integrated into WebUI `main` at `670cf286` by an ordinary fast-forward and non-force SSH push after review and all required checks passed. The configuration channel update targets this revision on its separate feature branch; configuration-default integration and production deployment remain separate. Review records, exact input receipts and prior desktop/mobile images are available in the [session record](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-typescript-client-migration/).

Requirements: REQ-005, REQ-007, REQ-011, REQ-012, REQ-054, REQ-055, REQ-056, REQ-060, REQ-061 and REQ-068.
