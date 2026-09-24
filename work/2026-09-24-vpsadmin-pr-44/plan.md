# 2026-09-24-vpsadmin-pr-44

## Goal

review this vpsadmin pr: https://github.com/vpsfreecz/vpsadmin/pull/44

I'm interested if the changes are justified, the commits coherent or suitable for squashing. do we need to update webui accordingly? apply our mandatory review skill.

## Affected repositories

- `vpsadmin`: review PR #44 against its `master` base, including API resources,
  specs, locale catalogs, commit history, and the in-repository PHP WebUI.
- Inspect related clients and KB contracts only where the changed pagination
  behavior reaches them. This is a review; no project-source change is planned.

## Approach

- Inspect the exact PR base/head and each commit, then trace the pagination
  contract through resource code, tests, and WebUI callers.
- Run quick read-only verification where useful, then use the mandatory change
  review's general, architecture, scope, and risk lanes with an independent
  reviewer. Reconcile findings against code and the reported CI evidence.
- Report whether the fix is justified, whether commits should stay separate or
  be squashed, and concrete API/WebUI/client follow-up before integration.

## Decisions

- Review-only scope: do not edit or merge the PR, post a GitHub review, or
  modify WebUI source without a further user request.
- The saved session roster is solo, so the mandatory review uses its catalog
  fallback reviewer after the review packet is prepared.

## Compatibility and deployment

- Check cursor ordering and tie-breaking, rejected anchors, filtered and
  authorization scopes, and mixed old/new API-client behavior.
- No persisted schema or on-disk format change is claimed in the PR. Verify
  whether rollback preserves valid client behavior and whether the changed
  HTTP 400 contract requires coordinated client handling or deployment order.
- Check visible WebUI order, "next page" behavior, and KB screenshot/text impact.

## Documentation

- Keep review findings, evidence, and next actions in this session's state.
  Recommend any missing lasting API contract documentation; do not change
  project docs in a review-only request.

## Testing plan

- Inspect the author's focused RSpec/RuboCop and current CI results.
- Run only focused quick checks needed to validate specific claims; avoid long
  integration work unless a concrete unresolved risk warrants it.
