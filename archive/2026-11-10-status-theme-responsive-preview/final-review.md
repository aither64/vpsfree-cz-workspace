# Final independent review

Reviewed repository `vpsfreecz/vpsf-status`, full range
`e560b43b01b7b387f1cd7a40a635d27f3b7fba2b` →
`1b39ba205bebc2f8d5a0754c1cfd08f94711e9fc`, ordered commits
`63d34fe341f759455d81e262ffc38fccad8c3cb5` (preview) and
`1b39ba205bebc2f8d5a0754c1cfd08f94711e9fc` (themes/responsiveness),
complete diff, adjacent implementation, tests and permanent docs. Original
committed head reviewed, not an in-progress remediation. Saved by lead from
reviewer0's complete returned report, preserving reviewer's read-only constraint.

Reviewer: retained `reviewer0`, review purpose/index0, thread
`01a1c544-e3f5-7751-ae63-5942b898172c`; saved `gpt-6.1-sol` / `xhigh` /
`read_only` verified live and unchanged. Independent, no authorship/fallback or
nested agents. Exact trusted binding verified; both environment markers absent.
Workspace/repository instructions, procedures, review skill and all four lane
references read. Medium bounded UI/preview risk; all four lanes applied.

## Findings

**Important R1: stale focusout callback closes the newly focused history day.**
`public/theme.js:81–84`, introduced by `1b39ba2`. Moving keyboard focus A→B
schedules A's focusout frame, then B's focusin opens B. A's callback observes A
neither focused nor hovered and globally closes B. The enhanced mode disables
CSS focus fallback, so sequential Tab loses B details and can prevent reaching
its incident link. Read-only in-memory Node VM evaluation of the committed
script reproduced B open immediately after focusin and closed after A's frame.
Restrict deferred close to the wrap still owning active; equivalent discipline
for delayed pointer dismissal. Browser acceptance must cover consecutive days,
incident links, Escape and outside tap. Assigned to P1; unresolved at this exact
review snapshot.

**Blocking: none. Advisory: none.** No other concrete correctness/security finding
inside supported scope.

## Scope and architecture

The user requests system/manual themes, readable navy/orange styling, responsive
phone/tablet layouts and lighter standalone preview; later approval authorizes
implementation and sample data. The 21-file 1093+/300− diff matches. Available
timing/evidence shows delivered milestones, not scope churn or stalled subsystem.
The tagged preview reuses routes/templates/localization/view builders/existing
SQLite store with fixed fixtures, not a parallel monitoring engine or framework.
Shared header removes duplication; semantic CSS owns surfaces and preference
remains browser-local. No disproportionate subsystem or hardening needs removal.

## Whole-branch history and compatibility

Both commits have coherent independently reviewable purposes with tests/docs.
README's short forward appearance link resolves in the following UI commit and
does not invalidate split. **No obsolete approaches, transitional compatibility
paths or redundant follow-up commits remain in the reviewed series. No repeated
dependency/channel/input/generated-artifact update streams exist.** Translation
generation belongs with UI source; dependencies/locks unchanged.

**No migrations.** No history schema/format, production state, API/client, JSON,
metric, protocol or Nix option/pin changes. Normal entry changes only its
`!preview` constraint. Preview never initializes monitoring, uses fresh temporary
state, reserved endpoints and loopback default. Old code ignores preference;
no conversion/coordinated update. Matching templates/assets/catalogs must ship
together. Review grants no integration or production-deployment approval.

## Documentation placement and preservation

README remains reachable basic start; links project-owned
`docs/how-to/sample-preview.md` for startup/scenarios/dependencies/state cleanup
and `docs/reference/appearance.md` for preference/fallback/cache/responsive and
compatibility behavior. Lasting explanations do not need session records;
individual receipts stay with session. Commands/defaults/frozen time/temporary
SQLite/CDN dependency/nonloopback unauthenticated exposure/forced-exit residue
match source. No moves, anchor loss, supported-upgrade retirement or recovery
removal. No extra upgrade/runbook bundle warranted. Keyboard claim conditional
on R1 correction and browser acceptance; no other placement/preservation gap.

## Verification and remaining limits

Inspected v2 passing normal/tagged Go suites, i18n and both build receipts.
Reviewer independently reconstructed all 98 committed file hashes: zero
mismatches versus input digest
`db934b29c5ad544bd3c2138f01d80cb86b6e4f35bdd86ee6d36c5e9ec17b7032`.
Diff whitespace passed. New route tests cover localized controls/labels; tagged
tests cover fixture scenarios/routes/gzip banner/pagination/history isolation.
These tests cannot execute the browser interactions that exposed R1.

No builds, Go suites, browser matrix, preview or long checks run by reviewer;
only source/evidence inspection and subsecond read-only callback reproduction.
B2 must establish computed contrast/overflow/zoom/themes/storage and keyboard/
touch popovers. CDN remains disclosed dependency, not new offline requirement.
Review complete with one Important finding: fix or explicitly dispose before
continuing. Lead may directly inspect/test the narrow ownership fix under the
skill's remediation rule; no automatic full rereview unless scope/behavior expands.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-10-status-theme-responsive-preview/)
