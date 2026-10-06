# Final review packet: Codex web portal update

Initiative: `2026-09-18-codex-web-portal-waiting`

## Requested outcome and acceptance criteria

- Relicense `codex-web` under Apache License 2.0 and make its README a practical
  user entry point while retaining the former technical reference in `docs/`.
- Display an amber dot inside the existing Codex rail icon, without increasing
  its horizontal space, while a current portal session needs user attention.
- Split `test/dev_session_test.rb` and `test/workspace_host_test.rb` into
  focused suites without changing their original loader commands or coverage.
- Deploy the reviewed feature configuration to aitherdev. Do not wait for CI.

The indicator must use the provider's existing `isBlocking` contract, clear
when activity is stale, unavailable, paused, nonblocking, or resumed, and
remain compatible with prior package and session state.

## Scope and final heads

| Repository | Base | Head | Role |
| --- | --- | --- | --- |
| codex-web | `7429ff29d3ae35c43b155a99b1bd34c6a33ae187` | `0a75d720171c52719679c7dd2e356d50f4b81f16` | Apache licensing, user/API docs, shared request policy |
| dev-workspace | `18817f4bf60f9918932d980d5c91b92852ba3cfa` | `b52a2363be8bb9985e4b9f254fb43e8cade4551d` | portal indicator, Ruby test split, direct source pin |
| vpsfree-dev-workspace | `e170ea0ead2babef823aa415e2d1b354d1648173` | `298a8a42282f193c82a24e87a95300548a4d5903` | generic runtime pin rebased onto the current default branch |
| workspace | `77afe04b318a82a8eea72b031bac2da856eb6abc` | `4bdc90b6601383ecee13fef4931227f09da89fda` | extension pin rebased onto the shared default branch |
| vpsfree-cz-configuration | `c7ed1210fc90434e50de2b1e4752a7ae38d9a491` | `5b500b2d0364e0def63d2ffdc13337c72a8413a7` | aitherdev `devWorkspace` channel pin |

All heads were committed, clean, and verified before integration. The source
path is exact and one-way:
`codex-web@0a75d72` → `dev-workspace@b52a236` →
`vpsfree-dev-workspace@298a8a4` → `workspace@4bdc90b`. The aitherdev
configuration selects `dev-workspace@b52a236` directly.

## Commit split and rationale

`codex-web` separates the user/documentation and licensing move from the
request-state behavior. The policy follow-ups (`b803905`, `7e65852`, and
`0a75d72`) correct review findings: one function now owns blocking defaults,
and unsupported MCP elicitation is automatically rejected, nonblocking, and
removed from activity recording. They are distinct behavior corrections with
focused regression tests.

`dev-workspace` separates the visible portal behavior, the Ruby structural
refactor, stale-state handling, and dependency update. The final input commit
contains the exact Go module, vendor hash, Nix lock, and source input needed to
build the corrected provider together. Each consumer history has one final pin
commit; superseded input commits were removed while the feature branches remain
unmerged. The pre-consolidation commit ranges are retained under local
`refs/rewritten/2026-09-18-codex-web-portal-waiting/` for recovery.

## Design, security, and compatibility

The browser owns presentation only. It reads the existing synchronized activity
and prompt data and overlays a CSS amber dot on the Codex icon. It adds neither
an endpoint nor persisted portal state. A provider-marked blocking command,
file-change, permission, or user-input prompt can signal waiting. The
`requestPolicyFor` function in `codex-web` owns the default classification used
by both prompt normalization and activity recording; an explicit user-input
`isBlocking` value remains authoritative.

Unsupported MCP elicitation is kept as an authorized diagnostic notice after
an immediate `-32601` response, but it is neither actionable nor blocking. Its
activity request is removed through the recorder's normal resolved transition,
so it cannot leave a stale waiting indicator. Pending conversation data remains
behind the existing capability checks; this change introduces no new endpoint
or broader visibility.

There are no schema, database, manifest, journal, protocol-shape, or migration
changes. Old profile generations keep reading current state; a rollback to the
prior user-profile generation removes the indicator and restores the earlier
provider behavior. No coordinated node update is required. Deployment order is
source pins first, then the aitherdev configuration input. The user later
explicitly directed fast-forward integration of the reviewed branches.

## Documentation and operational records

- `codex-web/README.md` documents purpose, features, quick use, browser API,
  trust boundary, and Apache 2.0 license.
- `codex-web/docs/reference.md` preserves the former README byte-for-byte.
- `dev-workspace/README.md` documents the visible indicator; its test README
  explains the retained Ruby test loaders.
- [plan.md](plan.md) and [state.md](state.md) hold compatibility, deployment,
  review, and recovery records for this initiative.
- [vendor-hash note](../../notes/dev-workspace/2026-09-18-vendor-hash-refresh.md)
  records the reusable fixed-output refresh procedure.

No member KB changes are needed: the visible behavior is documented in the
project README and does not change a vpsAdmin WebUI workflow.

## Quick verification already passed

- `git diff --check` passed for every committed implementation and final pin
  range.
- The original codex README and `docs/reference.md` were byte-identical after
  the move.
- Detached baseline and refactored Ruby loaders each passed: 316 runs and
  3,526 assertions for `dev_session_test.rb`; 77 runs and 490 assertions for
  `workspace_host_test.rb`.
- `nix develop -c bash -lc 'cd portal && go test -mod=readonly ./internal/web'`
  passed in 31 seconds, and Node syntax checks passed for the changed portal
  JavaScript and presentation browser contract. The final browser regression
  also passed with Nix-provided Playwright and browsers; it proves the amber
  dot clears immediately after an accepted response even when the next activity
  poll is stale, and makes its settings-cache expiry deterministic.
- The final focused provider test passed:
  `nix develop -c go test -mod=readonly ./codex -run
  'TestRequestPolicyKeepsPromptAndActivityBlockingMethodsAligned|TestRequestUserInputDefaultsMissingBlockingStateToBlocking|TestActivityBlockingUnionNonblockingTerminalAndPrivacy|TestActivityUnsupportedMCPRejectionDoesNotOpenWaiting|TestUnsupportedServerRequestIsRejectedAndSurfaced'`.
- `nix eval --raw .#workspace-portal.drvPath` passed at the final generic
  revision. The final vendor hash is
  `sha256-8Z6/cgM5VTFaHVGgGSqkPTIJre0KDyqV6sGPxpPnGIw=`.
- `nix flake show --json` passed for the final vpsFree extension and workspace
  profile. `confctl inputs channel set --commit` passed its Nixfmt and
  commit-message hooks for the final aitherdev pin.

## Review scope

Risk is **high** because the shared portal runtime will be deployed to a live
development host. The initial general, architecture/repetition,
scope/proportionality, and risk/compatibility Terra/xhigh lanes found the
accepted-response indicator defect and repeated input history. The remediation
adds an actionable-prompt projection and deterministic browser regression,
amends the Codex behavior commit body, and consolidates pins. The prior general
and architecture focused rechecks cleared the behavior and history changes.
Run a final focused risk/compatibility recheck on these exact heads with
`gpt-5.6-terra` at `xhigh`; reviewers make no edits and run no long checks.

## Review result

The initial Terra/xhigh general, architecture/repetition, scope/proportionality,
and risk/compatibility lanes identified the accepted-response indicator defect,
repeated input-pin history, and an obsolete module checksum. The defect is fixed
by the shared actionable-prompt projection and its stale-pending browser
regression; the input history was consolidated and the module data refreshed.
The focused general and architecture rechecks cleared those remediations. The
final Terra/xhigh risk/compatibility recheck also cleared these exact heads: it
found no security, mixed-version, deployment, or rollback incompatibility and
confirmed that all consumers resolve the final direct source pins. No reviewer
ran long checks or made edits.

The extension default branch advanced during integration with an independent
runtime pin. The extension feature was rebased onto it, preserving the reviewed
generic and Codex input revisions; its flake check passed. The workspace then
refreshed that exact extension pin, rebased onto its shared master, and passed
its flake check. These dependency-only integration updates leave the reviewed
behavior unchanged. All five final heads were fast-forwarded into their remote
default branches at the revisions listed above.
