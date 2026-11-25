# React OOM escalation package

Phase: independently reviewed, corrected, verified and published as
[PR 115](https://github.com/vpsfreecz/vpsadmin-webui/pull/115). All six exact-head hosted checks pass; ready, awaiting merge approval.
No merge or deployment authorization. Earlier milestones below
retain their original tested ranges; current final series and provenance follow.

Repository: `vpsadmin-webui`, worktree
`worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-webui`, branch
`dev/oomd-abuse-policy`, SSH origin `git@github.com:vpsfreecz/vpsadmin-webui.git`.
Fresh target/base: `40653dffed4561dd6086716fd506a7223d3631d7` (`origin/main`).
Original reviewed head: `6fcbbc172277677785b59ec2ee66724c3b1c1bb6`.
Final local head after approved clarification: `5d262808311831334086584d5914552426788fbf`.

Complete base-to-head series:

- `5d262808311831334086584d5914552426788fbf` — vps: show memory incident limits and stop status

Final diff: 28 files, 840 insertions, 18 deletions. This is one coherent UI/API
consumer change, including tests, locales and its required documentation. No
migrations, obsolete intermediate approaches, repeated dependency/input streams,
lockfile/pin changes or deployed/external state boundaries exist in this branch.
The current SSH fetch/rebase is a no-op and the worktree is clean.

The released implementation contract is used exactly: flat VPS Index/Show fields,
existing filters and three nullable/admin settings via the existing Update route.
Backend owner confirmed settings-only updates are synchronous without a receipt;
only those validated keys bypass asynchronous receipt requirements, and a fresh
VPS read verifies the saved values. Mixed writes retain existing validation.
No alternative endpoint or BFF change. Older APIs hide the feature on absent
`oom_incidents_7d`. No frontend incident counting or enforcement timer.

## Quick evidence

Pinned `nix develop` works; root `npm ci --no-audit --no-fund` completed without
lock changes. Terminology was resolved at locked vpsAdmin
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff`. Lead completed the main English/Czech
writing pass over all 38 keys; exact requested replacements were applied.
No hook framework or `core.hooksPath` is declared; Git identities were verified
in the actual worktree before the normal commit.

Passed:

- `npm run typecheck`.
- `npm run typecheck:e2e:core`: 88 checked files, 190 unchanged deferred files.
- `npm test -- src/lib/api/vps.oom.test.ts src/lib/api/vps.blocking.test.ts src/pages/app/vps/vpsOom.test.ts src/pages/app/vps/VpsOom.test.tsx src/pages/app/vps/useVpsListSmartFilters.test.tsx`: 57 tests, 5 files.
- Focused `VpsOom.test.tsx` rerun after final immutable-save/readback guard:
  all 16 cases passed.
- `npm run lint`, `npm run format:check`, `npm run audit:mutations:check`
  (225 calls, zero warnings), `npm run audit:ui-strings:check`.
- `npm run docs:inventory` and `npm run audit:design-docs` (153 docs,
  76 requirements, 257 routes, 64 API modules; generated inventory unchanged).
- `npm run audit:i18n` (8403 keys in each language),
  `npm run audit:i18n-structure`, `npm run audit:component-contracts`,
  `npm run audit:pages`, `npm run audit:structural` (zero unaccepted findings).
- `git diff --check` and clean Git status after commit/rebase.

The filter-clear test found a URL/state race during implementation; the final
clear action uses existing URL hydration and the test passes. Audit failures
were fixed without changing baselines, exception ledgers or gates.

## Documentation and remaining verification

Project record: `docs/work-log/2026-10-30-oom-incidents.md`; REQ-051,
`WORKFLOWS.md`, `API_CONTRACTS.md` and `EVIDENCE_MATRIX.md` updated. The canonical
external KB workflow was read. Current contracts/captures cover legacy PHP,
not React. Member incident guidance and VPS management/list captures are the
impact concepts; this package makes no KB or production write and does not
claim the PHP contract certifies React.

Lead should assign the retained independent reviewer the complete range above
under mandatory-change-review (general, architecture, scope and risk lanes).
Risk is high at initiative level: cross-project additive API and administrator
settings govern destructive backend behavior; this UI itself performs no stops.
No migration lineage exists in this repository.

After final review: run required full check/test/build batch and the prepared
`e2e/specs/app/vps_oom_summary.spec.ts` in desktop/mobile projects through fresh
verification watchers. Browser cases use synthetic HaveAPI fixtures, not a real
backend. Capture and show actual implemented cs/en member/admin detail and list
screens. Fetch/rebase again if upstream changes, preserve review equivalence,
then push the feature branch, create its required PR and monitor exact-head CI.
No default-branch integration or deployment is authorized.

Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/>.

## Approved review clarification fold

After the original independent report completed, lead authorized folding exactly
three files into the owning unmerged commit: API contract and work-log text now
state that the backend rejects mixed OOM/other writes before effects, while the
client test title describes its defensive rejection of malformed/mixed success
responses. Runtime behavior and test assertions are unchanged.

Old reviewed range:
`40653dffed4561dd6086716fd506a7223d3631d7..6fcbbc172277677785b59ec2ee66724c3b1c1bb6`.
New range:
`40653dffed4561dd6086716fd506a7223d3631d7..5d262808311831334086584d5914552426788fbf`.
Fresh SSH fetch left origin/main unchanged; rebase was a no-op. Range-diff
contains only those two documentation changes and one test-title replacement.
An exact byte comparison verifies all remaining runtime source and test
assertions are unchanged. Original reviewed Git object remains readable.

Approved focused verification for the clarification passed: six adapter tests,
design-doc audit and diff whitespace check. No broad checks were repeated.
Publication, browser checks and builds remain held pending backend source
clearance. No migrations or lineage change exists in this React fold.

## Publication checkpoint

Final branch `dev/oomd-abuse-policy` is clean and published at
`b67c7917e8758e707e0b88512f055eab9fbd8529`; SSH remote exact-head verified.
Fresh main/base remains `40653dffed4561dd6086716fd506a7223d3631d7`; rebase no-op.
Complete current series:

1. `626c6cf6e896b57212e9381d54969cddbc4698fb` — consolidated application, tests,
   locales and feature docs, including approved rapid-filter correction.
2. `b67c7917e8758e707e0b88512f055eab9fbd8529` — routine verification/capture
   receipt and four synthetic PNGs only.

Original independent review examined `6fcbbc17`; lead preserved its report and
accepted the three-file clarification and bounded filter correction directly.
There are no migrations, obsolete intermediate commits, repeated input streams,
dependency changes or deployed state boundaries in the final series.

Full local required batch passed at `5d2628083118`: Node24.21.0/npm11.19.0,
ci:pr,226script/57BFF/1935unit tests(308files), build21.74s,0vulnerabilities in
both audits. Exact log/result under `react-verification/required-checks.*`.
Initial scoped browser batch at that source passed10/12; its two failed combined
filter cases exposed a real rapid-navigation stale-params race. Negative test
failed before the bounded correction. Lead accepted7runtime lines using existing
latest-search-ref convention; rendered rapid/external-navigation tests, focused
adjacent tests/type/lint/structural/UI-string checks pass. Only the affected
browser pair repeated, passing2/2 at committed `3fdbecf526c4` without retries.
The corrected browser source and folded626c complete trees are exactly identical:
`7b2a2a2caac4601abf6bcebf669ad2219dc1335a`. Finalb67 runtime/test/toolchain paths
are unchanged; only evidence Markdown/PNGs differ. Preserve original failed run
as failed and original successful unaffected scope without relabelling it as
an exact-final-head full suite.

Evidence: browser.log/results/report (original), browser-filter.log/results/report
(corrected pair), filter-fix.patch and filter-fold-range-diff.txt. Corrected list
screenshots were visually inspected and shown, then copied unchanged into
`docs/work-log/screenshots/2026-10-30-oom-incidents`. Both layouts show retained
status+exemption and bounded count badge. Detail English desktop/Czech mobile
captures remain explicitly pinned to5d; their components/styles were unchanged.
All images use synthetic API/identities; none certifies backend enforcement.

Automatic PR runs at exact finalb67:

- CI41117892033: <https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41117892033>
- Playwright41117892171: <https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41117892171>

A fresh standalone Luna/low CI watcher operation observes both and retains
logs under `react-verification/hosted-ci*`; native/CLI settings are recorded in
watcher logs. No duplicate workflow dispatch or successful full local rerun.
No feature content entered main and no deployment occurred.

## Final package receipt

PR115: <https://github.com/vpsfreecz/vpsadmin-webui/pull/115>.
Final local, PR and SSH-remote head:
`b67c7917e8758e707e0b88512f055eab9fbd8529`.
Fresh SSH main remains `40653dffed4561dd6086716fd506a7223d3631d7`.
The registered comparison was captured with these exact base/head revisions.
Worktree clean; branch retained; session active/open.

Both hosted workflows are terminal success at that final head:
CI41117892033 and Playwright41117892171. All six commit check runs pass.
Browser totals: Chromium613, mobileChrome555, mobileWebKit249 =1417passed,
plus2intentional WebKit skips. Terminal job logs contain no flaky/retry/failed
summary. No hosted workflow was rerun or cancelled. The smoke aggregate briefly
lagged after all jobs/check runs were terminal success; it reconciled to
completed/success with updated_at2026-10-30T20:18:16Z. Preserve that observation
rather than claiming success from intermediate green steps alone.

Final hosted logs/results are retained under `react-verification/hosted-*`.
Fresh Luna/low CI watcher01a18e59-4fac-7670-85bf-16a3e42b8735 completed and
reported no running operations. Its full-access/never launch policy is in its
log. All verification commands launched for this package have ended.

Source/review lineage: original review40653dff..6fcbbc17; approved clarification
5d262808; narrow browser-filter correction3fdbecf5 folded into626c6cf6 with
identical full tree7b2a2a2c; b67c7917 adds only evidence Markdown/PNGs. Final
runtime/test/toolchain paths equal3fdb, with final hosted checks providing direct
exact-head proof. Detail captures are explicitly pinned to5d; corrected list
captures to3fdb/626c. No migration or deployed lineage exists in this repository.
The complete final two-commit history contains no obsolete intermediate work
or repeated dependency/input update streams.

Lead accepted independent-review scope, clarification,7-line correction,
negative/positive/external-navigation tests and representative implemented
synthetic images. The final PR body records outcomes and source/capture limits.
No UI fixture certifies backend enforcement/accounting/mail. External KB
contracts remain legacy PHP evidence. No default-branch integration,
deployment, machine reservation, repository merge claim or lifecycle action
occurred. The frontend package has no remaining implementation/check/publication
work; integration and deployment require separate explicit direction.

Final structured PR check proof: `react-verification/hosted-final-checks.json`
asserts the exact final head and six COMPLETED/SUCCESS checks. A later optional
attempt to download the complete aggregate CI text log hit an HTTP/2 stream
CANCEL transport error; this does not alter the successful structured run/check
proof, watcher record or completed browser job logs. No tests or workflows were
repeated for that incidental log-download failure.

## Reproducible-data cleanup

After explicit user cleanup direction and lead acceptance of package-process
reference scope, removed own ignored dependency/build data and duplicate browser
reports. Preserved committed PNG/docs, all logs/receipts and compact original
failure traces; source/committed tree and clean status unchanged. No tests,
installs/builds/GC/lifecycle action. See [exact byte accounting and df proof](react-cleanup.md)
and [machine-readable receipt](react-verification/cleanup-receipt.json).
