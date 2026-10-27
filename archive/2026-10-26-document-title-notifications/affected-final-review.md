# Affected final review — Firefox fixture follow-up

**PASS, no findings.** Received 2026-10-26 from same independent reviewer0,
thread01a179a6-9f40-7320-87f3-90d0e2fa3300, saved gpt-6.1-sol/xhigh/read_only,
identity/roster reverified, no overrides/fallback/subagents. Lead saves this
summary; original full report remains in reviewer-to-lead conversation. Reviewer
used read-only inspection, no checks/builds/edits/claims/deploy/lifecycle action.

Retain [original final review](final-review.md) for unchanged behavior/docs/assets/
browser runner. Affected general/architecture/scope/risk review is complete.

## Exact reviewed final ranges

| Repository | Base | Head |
| --- | --- | --- |
| dev-workspace | 7e6d7c9cdb3388ab7abc720c034c15c21afbd686 | d2099c62656bc2a36c306918a92832ba1e1a0cc0 |
| workspace | 978a2f280185f3ae114c2db13130f13e6976b159 | e3b44a8b59c656e0ecec0bd692ad7f72963f7e61 |
| vpsfree-cz-configuration | 880a6253f8d6cc1368e633f936b174792e86bff7 | 514e6a06ef72c3c2b4c50a592ff58b3d6fcd7cd2 |

All heads/parents/cached feature refs and clean trees matched. One final commit
per range. **No obsolete approaches, fixups, transitional migrations or superseded
unmerged iterations; no repeated update streams remain.** Runtime correction
folded into owner; each consumer directly selects final runtime from its accepted
base. Generated config history correctly says7e6d7c9c->d2099c62. Inherited shared
workspace tracking history/base rebase conclusions unchanged. Old ef85/6521/c6fa
heads were not deployed; no nonancestor deployed equivalence exception applies.
Fresh remote ancestry/actual activation remain lead-owned later evidence.

## Independent affected conclusions

- Original failed native log supports one DOM submit, two HTTP sends/mock
  dispatches/journals, accepted receipt and no manual unknown-retry control.
  Existing background-title/discard/read-budget assertions were already reached.
- Test fixture Send now serializes reconcile-before-dispatch, retains matching
  receipt, refuses mismatched text/action and fsyncs one journal record. Direct
  quick test exercises duplicate Send, not only ReconcileSend. This is scoped to
  the existing fixture, not new production persistent idempotency infrastructure.
- Shared loss helper sends502 headers plus one byte of a two-byte JSON body,
  flushes then closes HTTP/1 connection, only after real upstream/native handler
  acceptance. This models an uncertain gateway outcome and prevents zero-byte
  transparent replay before JavaScript can expose uncertainty.
- Reviewer independently inspected pinned codex-web8b60554 client: parse failures
  become empty objects, response.ok still makes truncated2xx accepted.502 with no
  notSent/retryable claim stays unknown; automatic retries admit only explicit
  transient non-delivery. Thus accepted fixture correction targets real boundary.
- New actual-handler regression uses same helper, requires upstream acceptance,
  502 plus io.ErrUnexpectedEOF, same-ID retry and exact two HTTP attempts/one
  dispatch/journal. Unchanged native runner still requires visible Retry original,
  cleared draft, explicit click and exact acceptance counts; no assertion weakened.
- Production JS/assets/templates/docs/native Firefox runner byte-identical to
  original review. Full runtime7 files+317/-65, delta test-only+99/-7; proportionate
  observed-failure fix. No production API/recovery/Codex/host/protocol changes.
- Independently compared lock node sets/edges/follows/siblings against original
  bases and reviewed old heads: only runtime nodes differ. Both select d2099c62 /
  sha256-kQkKnjQVSYZw3ZDNan8EakG7HS29wIbHGZ14B7Xq5vA=. Graph hashes match rollout;
  extension767dfd, codex-web8b6055, distinct system/profile Codex preserved.
- Original mixed-page/host-profile compatibility, trust and rollback conclusions
  stand. **No migrations:** no database/IndexedDB/event/read-state/protocol/
  lifecycle-journal formats or new schema versions/consumption history to retain.

## Limits

Reported quick3 Go tests/0.499s, formatting/whitespace/deployment contract/hooks
accepted; reviewer did not execute tests/builds. Unchanged Node-source focused
checks may be retained. Old complete package/config/CI results do not certify
refreshed derivations. New native Firefox, exact composed/config builds and CI
remain required. No finding asks for expansion or another source change.
This review is not deployment/integration/release proof; session stays open.
