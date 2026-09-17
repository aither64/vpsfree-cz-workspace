# Verification

## Focused checks

- Ruby automatic/retirement suite: 24 runs, 371 assertions, no failures/errors.
  Exercises a real subprocess that outlives the ordinary deadline, bounded timeout,
  restoration on success and failure, and journal retry without another commit.
- Go workspacecodex, web and workspace-portal suites passed. Retirement RPC errors
  preserve stage context; browser contract assertions cover stale operation and
  conversation identities, failure timestamp and safe diagnostic rendering.
- Chromium and Firefox: archive browser fixture passed in 12.10 seconds. Covered
  read-only markup, separate journal/worker timestamps, coalescing and throttling,
  hidden pages, retained data during failed refresh, running retry and completion.
- Fixture initially lacked VerifyThread, causing the intended normalization to
  strip its thread ID. Added exact fixture identity verification and an assertion;
  no product change. Repeated real-browser checks passed.

## Packaged checks

- Runtime flake evaluation and all normal feature-branch checks passed on a5f8715
  (same application code as final 0bd68ef; final differs only in browser fixtures).
  Host module idempotency VM is excluded by the normal feature-branch CI policy;
  this change does not alter host modules, activation or persistent contracts.
- Extension full flake checks passed on 0bbb053, including package/compatibility,
  extension catalog, source boundaries and Ruby extension/migration tests.
- Workspace package and deployment-contract passed on fba9c39.
- Final package and current-head CI results are recorded below when complete.

## Reviews

All four fresh gpt-6-astra/xhigh lanes completed: general, architecture, risk,
scope. No Blocking/Important findings. General documentation advisory corrected.
Architecture advisory retained: automated tests do not detect future drift in the
Go timeout; inspected production hierarchy is 60/180/210 seconds. Runtime docs
explain maintaining the outer limit above the inner limit. See review-*.md and
state.md for original reviewed heads and final narrow remediations.

## Live recovery

Installed manual archive resumed operation
9a6219fda3a306872793abfdffc34eae4cb99815d5b32c11ba7313523d21b5ff and completed at
2026-09-16T20:47:21Z. Source journal and runtime authority are absent. Exact thread
01a0a4da-4f2b-7ad1-ab6d-27b3262dc671 moved from sessions into archived_sessions.
Both feature refs remain b6e650ad902482b4c4e66b5a89a4275bed92419e. Portal operation
returns archive/complete; page has complete lifecycle, empty pending lifecycle,
verified retained thread ID, interactive=false and no message form.

Current runtime head 0bd68ef passed
[CI 35148407354](https://github.com/aither64/dev-workspace/actions/runs/35148407354)
at 20:47:47 UTC, including package and all normal feature-branch checks.

Final workspace c60bac9 built successfully as
/nix/store/bspd81hp98awq942lnr7p93k38i8d8di-dev-workspace-0.2.0.
Its packaged Go suite and Ruby suites passed (313/3326, 8/33 and 77/475
runs/assertions; zero failures/errors, existing environment-dependent skips).
Deployment-contract check passed 3 runs/14 assertions. Profile 48 activation and
live asset/health/identity checks passed; exact evidence is in rollout.md.

Current extension head 90ce0cf passed [CI 35148442339](https://github.com/vpsfreecz/dev-workspace/actions/runs/35148442339) at 20:53:58 UTC, including full flake checks and cluster-packaging smoke tests. All required checks are complete.

## Default-branch integration, 2026-09-17

Runtime and extension heads are unchanged from the reviewed, tested deployment.
Workspace rebased over coordination-only changes; range-diff proves its pin patch
unchanged. Final integration inspection confirmed the same dependency revisions.
Runtime generic-source, extension organization-source and workspace deployment-
contract checks passed. All three merges were fast-forward-only.

Runtime master CI: [35193656065](https://github.com/aither64/dev-workspace/actions/runs/35193656065).
Extension master CI: [35193746897](https://github.com/vpsfreecz/dev-workspace/actions/runs/35193746897).
Runtime host activation, renewal and rollback VM smoke test passed. Runtime package/focused checks also passed. Extension flake checks passed; its
cluster-packaging smoke test was still running when the user requested no further
waiting. The GitHub workflow was left running, and no result is claimed for that
last step. Workspace has no GitHub workflow; its local contract check passed.

Runtime master CI completed successfully: both package/focused and host VM jobs
passed. Remote ls-remote verification after integration reports matching default
and retained feature heads in all three repositories:
- dev-workspace: 0bd68efa9cadb0589148fac40de7645a06b03468.
- vpsfree-dev-workspace: 90ce0cfe7c39c944aca0c7b27fe1e53a719075a3.
- workspace: eca34d047621ba42de3bd48e23e26b88d5f4d3fb.
All three canonical feature paths and both temporary integration paths are absent.
