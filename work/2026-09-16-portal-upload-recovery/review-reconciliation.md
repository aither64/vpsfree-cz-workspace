# Review reconciliation

Initial packet: review-packet.md. All reviews use gpt-6-astra xhigh.
General, architecture and risk finished; scope reviews the final consolidated set.

| Finding | Lanes | Severity | Resolution and focused evidence |
| --- | --- | --- | --- |
| DELETE 404 may mean temporarily unavailable scope | General G1, risk R1 | Important | Read the authorized listing after DELETE 404. Only absence/deleted permits clearing. Retain errors when present or listing fails. Two browser regressions cover both refusals. Risk reviewer assessed this correction within the current contract. |
| Successful DELETE followed by transient storage failure can re-enable deleted ID | General G2, architecture A1, risk R2 | Important | Mark remote deletion before local persistence. Retained deleted cards cannot be ready. Require error-free entries for readiness so an uncertain deletion response also blocks sending until reconciled. Tests cover one-shot/persistent write failures and lost DELETE responses. |
| Pre-request storage failure marks a never-started upload uncertain | General G3 | Important | Restore the previous creation outcome when persisting uncertainty fails before the network call. A regression proves Remove sends neither POST nor DELETE. |
| New C1 rejection prevents recovery of older accepted identity | Architecture A2 | Important | Resolve exact scoped client identity before applying admission validation for new files. Test an old-format C1 record, recover its original ID, delete its bytes, and reject new C1 creation. |

All four fixes preserve the planned interfaces and storage layout. Provider README
now spells out idempotency before tightened admission and authorized confirmation
of missing files. These are direct fixes inside the reviewed design; no review
rerun is needed under the mandatory skill. Scope lane remains required.

Focused checks: 26 upload browser tests pass; runtime upload-store tests pass.
Logs: review-browser-fixes.log and review-store-fixes.log. Provider CI for final
7429ff29 passed (35065045039). All final pins are committed and pushed; revisions.json records exact heads.

Scope review completed against the final series with no findings. All required
lanes are complete; long acceptance tests started after reconciliation.
