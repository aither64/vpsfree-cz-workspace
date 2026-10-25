# Approved API-documentation acceptance checklist

Implementation authorized by user "Implement the plan" after final four-owner
proposed plan. Preserve release baseline 08345b2 evidence; new exact final head
must be independently reviewed and checked. No integration/publication authority.

| Capability | Owner | Required acceptance |
| --- | --- | --- |
| File system removal | implementer0 | No renderer/overview/init/auth/action tab; other legacy formats preserved; separate client project untouched |
| Shared context | implementer0 | Selected API version, mounted URL, per-user filtered help/sample; no cross-user privilege cache |
| SDK profile config | implementer0 | Per-version actual published Go/Rust SDK; no profile hides overview/all tabs; malformed configured profile fails startup |
| JS callback/async | implementer1 | Actual setup/auth/action/error/result APIs; coherent runnable composition; omission and exact names preserved |
| TS callback/async | implementer1 | Strict installed-package typing; no any/private fallback; static safe callback action lookup |
| Python sync/async | implementer1 | Actual context manager/call/response/exception interfaces; complete asyncio ownership |
| Go | implementer2 | Canonical generator mapping, correct path/setter/null/selection; unsupported list input/Custom explicit; compile/run fixture |
| Rust async/blocking | implementer3 | Snapshot+TOML mapping, actual inputs/setters/path/null/list interfaces; blocking lifecycle; compile/run/MSRV |
| HTML/assets | implementer0 | All requested labels/ordering/highlight languages, keyboard/narrow/no-JS readable; no unsafe literal/HTML paths |
| Profiles/authorization | shared | Full SDK schema kept internal; no extra privileged names/defaults/sample values/path leak; stale sample explicit limitation |
| Metadata/state | language owners | Advertised and real APIs only; no new example wire shape/invented helper/drop |
| Release | implementer0+lead | Logical source commits before exact last Version 0.30.0; hooks+quick checks, full final independent review, long acceptance/build/CI afterward |

Frozen contract recorded by architect in design.md and api-doc-client-examples-plan.md.
Language owners must route registry/dependency/test runner/shared fixture requests
to implementer0, who serializes all Git/index/hooks. Existing renderer extension
calls, Ruby/PHP/CLI/curl/HTTP examples and protocol remain supported. No DB schema
or persistent state migration. No production credentials or registry calls in tests.
