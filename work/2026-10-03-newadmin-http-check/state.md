---
lifecycle: active
---

# 2026-10-03-newadmin-http-check

## Status

- Phase: implementation setup; approved probe fix and dedicated warning-only policy.
- Cause confirmed: both public frontend body patterns require compact JSON,
  while the live endpoint serves formatted JSON with a space after each colon.
- Implementation authorized by the user; no merge, production deployment or lifecycle action authorized.

## Phase checklist

- [x] Verify exact session identity and inspect retained roster (`solo`).
- [x] Inspect live metadata, HTTP probe configuration and exporter semantics.
- [x] Reproduce both pattern failures and check proposed replacements.
- [x] Separate BFF health and status-site redirect from the frontend failure.
- [ ] Set up the approved implementation team and dedicated feature worktree.
- [ ] Implement probe fix, warning-only rules, coverage and policy documentation.
- [ ] Complete quick checks and required hooks; commit intended changes.
- [ ] Complete independent whole-branch review.
- [ ] Build both monitoring hosts and prepare rollout.
- [ ] Merge/deploy only after later explicit direction; verify production probes.

## Next actions

Correct both `bodyMatches` entries for `newadmin_vpsfree_cz` in
`modules/clusterconf/monitor/http.nix`, then deploy monitoring to mon1 and check
the production probe. Proposed Nix values:

```nix
bodyMatches = [
  ''"schemaVersion"[[:space:]]*:[[:space:]]*1[[:space:]]*[,}]''
  ''"commit"[[:space:]]*:[[:space:]]*"[0-9a-f]{40}"''
];
```

Both are required. Fixing the first alone exposes the second mismatch because
the exporter stops at the first missing required pattern.

## Documentation

- Read configuration `README.md`, `AGENTS.md` and
  `docs/operations/newadmin-webui.md` from canonical cached `origin/master`.
- The operations guide's schema/full-SHA contract is correct; no project
  documentation update is useful for this read-only diagnosis.
- Upstream implementation checked:
  <https://github.com/prometheus/blackbox_exporter/blob/v0.28.0/prober/http.go>
  (`matchRegularExpressions`, lines 46–64: raw body matching, all required
  patterns, early failure).

## Repositories

- Configuration canonical cached `origin/master`:
  `657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`.
- Probe definition: `modules/clusterconf/monitor/http.nix:52–63`.
- Configuration plumbing:
  `modules/clusterconf/monitor/default.nix:489` passes `bodyMatches` directly
  to `fail_if_body_not_matches_regexp`.
- Probe introduction: `4f1dfd72`,
  `monitor: check newadmin frontend, BFF and certificate`.
- WebUI pinned and publicly served commit:
  `f123a7fb825437034a764a8a5654032a481a8476`.
- Cached WebUI `origin/main:build/buildInfo.ts:103` emits
  `JSON.stringify(buildInfo, null, 2)`, consistent with the observed formatting.
  The pinned WebUI revision is absent from this local bare clone; its exact
  source was not inspected, and no fetch was needed for the diagnosis.
- No registered feature branches or owned project worktrees.

## Commands run

- `dev-session current`: matches exact thread binding and both environment
  markers. `dev-session team list 2026-10-03-newadmin-http-check --as-is`:
  solo roster, no members. Stable URL obtained with `dev-session url`.
- Public `curl` GETs for `/build-info.json`, `/healthz` and the status site
  (including IPv4 and following the status redirect).
- Read-only canonical Git inspection (`show`, `grep`, `log`, `rev-parse`).
- Ruby raw-body regex evaluation and JSON parsing using Nix-profile Ruby.
- Read upstream blackbox exporter 0.28.0 source and configuration documentation.

## Results

Live checks on 2026-10-03 at approximately 18:00–18:03 UTC:

- `/build-info.json`: HTTP 200, `application/json`, 159-byte formatted body.
  `schemaVersion = 1`, full lowercase 40-character SHA, `dirty = false`.
- Configured schema pattern `"schemaVersion":1`: false.
- Configured commit pattern `"commit":"[0-9a-f]{40}"`: false.
- Both proposed whitespace-tolerant patterns: true against the live body.
- Proposed schema pattern rejects `{"schemaVersion":10}`.
- `/healthz`: HTTP 200 with `ok`.
- `status.vpsf.cz/`: HTTP 302 to `/?lang=en`; following the redirect returns
  the configured `vpsFree.cz Status` body match. Exporter defaults to following
  redirects; the warning is separate from the logged frontend regex failure.
- `tests/prometheus/newadmin-rules.nix` exercises alert rules with promtool;
  it does not validate body regexes against actual endpoint JSON.

## Open questions

- No blocker to diagnosis. The running exporter on mon1 was not queried
  directly; its failure reason comes from the supplied logs, corroborated by
  the matching source configuration and observed public response.
- These checks do not certify interactive login or all WebUI behavior.

## Cleanup

No temporary artifacts or development resources were created. Session remains
open and active. Unrelated shared-workspace changes were preserved.

## Approved implementation scope

The user requested warning-only Newadmin alerts and selected the dedicated-alert
scope. Shared VPS infrastructure severities remain unchanged. Implementation
was authorized with "Implement the plan" after the proposed plan. No merge or
production deployment approval was given. The bounded design is recorded in
`plan.md`; the implementer owns application edits and the lead owns tracking.

Initial coordination commit will precede team setup and project-code commits.
