# WITHDRAWN — modern visibility delta

The user explicitly corrected the ownership contract: visibility is handled
completely by the server; UIs show what it sends. The lead directed complete
withdrawal of the modern filtering/cache-defense delta. This supersedes the
accepted UI portion of the earlier design and every implementation/readiness
claim below. No further modern visibility implementation or acceptance applies.

The branch and draft PR122 were restored exactly to previously reviewed/running
`1c8478bceb3943645ec06ccde895ee4b0985873f`, tree
`7d3169bc4f80af199631e73cc4442b7985d8cf6d`. All fifteen source/test/docs/inventory
paths were restored with path-scoped Git restoration. No unrelated or untracked
data was present; no repository-wide reset, clean or stash was used.
The consumed/reviewed 1c847 source and its Nix/npm/toolchain inputs are exact;
no new full tests/build or preview update is needed or performed.

The withdrawn commit `f7c4eb282cd146d5b905c70db74f2aedb4ff4969` remains at
`refs/evidence/2026-11-01-published-advisory-corrections/superseded-modern-visibility-f7c4eb28`.
Its original quick evidence, binary delta and range-diff remain below and in
/tmp/2026-11-02-modern-visibility/. These are superseded investigation evidence,
not part of the current deliverable or a claim that client filtering is desired.
SSH force-with-exact-lease f7c4→1c847 succeeded. Fresh ls-remote proves restored
feature1c847 and unchanged main63d484fc070dbee633d32624de545e834d483701.
PR122 remains draft at exact1c847; its client-guard paragraph was removed and
the original advisory-management validation is scoped to the restored head.
Current preview already uses1c847; no cluster/process/source activation occurred.

CI withdrawal snapshot: old f7c4 CI41460012271 completed success, preserved as
superseded evidence. Cancellation of active f7c4 browser41460012379 was requested successfully
(exit0); the immediate status remained in_progress, so completion is not claimed. Restored1c847 prior successful CI41339759463/browser41339759427
are retained; automatic restored-head CI41462732480/browser41462732324 are
current and left untouched. Exact cancellation receipt is
/tmp/2026-11-02-modern-visibility/ci-cancellation.json; no run was relaunched,
retried or awaited. No production/default integration/lifecycle action.

Final bounded cancellation snapshot confirms browser41460012379 completed
with conclusion cancelled at f7c4; receipt
/tmp/2026-11-02-modern-visibility/ci-cancellation-final-snapshot.json.
No current1c847 or previous successful run was cancelled.

The API server owner continues the server-only scope correction independently.
Later modern verification, if released, is read-only server-denial acceptance,
not mocked client-side hiding.

---

# Modern published-only visibility — committed quick packet

Session binding verified: 2026-11-01-published-advisory-corrections,
/home/aither/workspace/ai/vpsfree.cz; implementer1 owns only modern source/Git.
Accepted contract: [visibility-design.md](visibility-design.md). Implementer0
owns API authority, legacy source/Git and KB pin. No source overlap.

## Exact history and provenance

- Repository: git@github.com:vpsfreecz/vpsadmin-webui.git
- Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-published-advisory-corrections/vpsadmin-webui
- Feature: dev/published-advisory-corrections; target main; draft PR122.
- Fresh default/base: `63d484fc070dbee633d32624de545e834d483701` (fetch + ls-remote immediately before publication).
- Previously reviewed and consumed preview head: `1c8478bceb3943645ec06ccde895ee4b0985873f`.
- Preserved ref: refs/evidence/2026-11-01-published-advisory-corrections/reviewed-running-preview-1c8478bc.
- Final successor: `f7c4eb282cd146d5b905c70db74f2aedb4ff4969`; tree `4f48268a8d04b9fae9eede32df65ebc502fdae0d`.
- Complete final base-to-head series: one commit, `f7c4eb282cd146d5b905c70db74f2aedb4ff4969`.
- This consolidates visibility changes into the existing E logical commit per lead.
  It preserves the original author and all prior baseline evidence. The old head
  is not an ancestor and is not literally merged; its exact source ref remains.
- Applying the exact old-to-new binary delta to a temporary index seeded from
  `1c8478bceb3943645ec06ccde895ee4b0985873f` reconstructs final tree `4f48268a8d04b9fae9eede32df65ebc502fdae0d` exactly.
- Full range-diff: /tmp/2026-11-02-modern-visibility/range-diff.txt; exact successor delta:
  /tmp/2026-11-02-modern-visibility/visibility-successor.patch.
- No migrations, persisted-state changes, dependency/pin streams or new transport,
  BFF, catalog, SDK or cache framework. No obsolete intermediate commits remain.
- Locked vpsAdmin terminology/input remains a65a4dfeb92a59df4a80a737a20bcbf8558793ff;
  main unchanged; root installed dependencies reused from the prior pinned setup.
- Git author/committer remain Jakub Skokan <jakub.skokan@havefun.cz>.
  No declared hook framework or active hooks; nothing bypassed.

## Final delta

Public list requests published rows only. A render-time filter protects cached
rows before pagination and CVE requests. Detail admits only a published parent
before body and all CVE/node/update/outage/affected-VPS child queries. Admin
all-state queries and corrections remain unchanged. Existing not-found copy reused.

Exact changed paths relative to the reviewed preview baseline:

- `WORK_LOG.md`
- `docs/design/ACTION_CONTRACTS.md`
- `docs/design/API_CONTRACTS.md`
- `docs/design/EVIDENCE_MATRIX.md`
- `docs/design/REQUIREMENTS.md`
- `docs/design/WORKFLOWS.md`
- `docs/work-log/2026-11-02-advisory-visibility.md`
- `e2e/specs/public/security_advisories_visibility.spec.ts`
- `scripts/fixtures/e2e-type-coverage.json`
- `src/pages/app/admin/security/AdminSecurityAdvisoryDetailPage.snapshot.test.tsx`
- `src/pages/public/SecurityAdvisoriesPage.test.tsx`
- `src/pages/public/SecurityAdvisoriesPage.tsx`
- `src/pages/public/SecurityAdvisoryDetailPage.test.tsx`
- `src/pages/public/SecurityAdvisoryDetailPage.tsx`
- `tsconfig.e2e.json`

The delta is 15 paths, +335/-96. The runtime change is confined to two public
pages. Test growth covers meaningful rendered cache/role regressions and the
new bounded public browser fixture with strict E2E type adoption. Main directly
reviewed the project docs and PR visibility paragraph before publication.

## Quick evidence

Pinned `nix develop`:

- `npm test -- SecurityAdvisoriesPage SecurityAdvisoryDetailPage SecurityAdvisoryAdminGate securityAdvisoryAdminModel`:
  41 tests / six files PASS, 10.14s, 2026-11-02 at 14:08 UTC.
- Affected six-file ESLint PASS; new browser fixture Prettier PASS.
- `npm run ci:quick` PASS, including docs, lint/format, catalog/architecture audits,
  frontend/tooling/BFF types and strict E2E (101 checked, 183 deferred).
  Log: /tmp/2026-11-02-modern-visibility/quick.log; completed 2026-11-02T14:12:29Z.
- Docs-only factual evidence update followed by `npm run audit:design-docs` PASS
  (257 routes,65 API modules,178 documents,76 unique requirements).
- `git diff --check` PASS; source clean after commit.
- No full suite, build, browser execution, new capture, package check or preview
  activation before affected committed-source review. The new browser fixture
  is compiled only; no browser PASS is claimed.

The old baseline's completed full suites/package/browser/OAuth evidence remains
scoped to that exact baseline in [modern-verification.md](modern-verification.md)
and [modern-preview.md](modern-preview.md), not final successor acceptance.

## Review and remaining work

Lead coordinates affected independent review of this delta and complete final
branch history. This is a high-risk read-visibility/public-contract correction;
review scope includes cache and child-query gates, admin preservation, browser
fixture assumptions, compatibility/docs and consolidated lineage. No migration.
The API is authoritative and must be updated first or with the UI. Software
rollback is data-compatible but must preserve the published-only server scope.
Existing delivered browser content/mail cannot be recalled.

After review/release: full unit/build and bounded public desktop/mobile fixture
execution, then released exact-source preview update and normal TLS/OAuth
read-only role/state acceptance against the preserved three live examples.
Running preview remains old1c847/API49f5; no activation or data mutation by this
package. No production/default integration/session lifecycle action.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/

## Publication snapshot

SSH lease push succeeded from old1c847 to f7c4eb28. Fresh `git ls-remote` proves
feature `f7c4eb282cd146d5b905c70db74f2aedb4ff4969` and unchanged default
`63d484fc070dbee633d32624de545e834d483701`. Draft PR122 reports that exact head.
One fresh current-head CI snapshot records CI41460012271 and Playwright
smoke41460012379 in_progress; no conclusion claimed and no run awaited/retried.
There were no superseded active own-branch runs to cancel. Snapshot saved at
/tmp/2026-11-02-modern-visibility/ci-snapshot.json.
