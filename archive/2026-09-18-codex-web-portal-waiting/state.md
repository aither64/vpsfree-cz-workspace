---
lifecycle: complete
---

# 2026-09-18-codex-web-portal-waiting

## Status

All five reviewed feature heads have been fast-forwarded into their remote
default branches. The mandatory Terra/xhigh review and focused rechecks are
clear. Aitherdev runs the built generation `2026-09-18--15-07-57`, which is
now also represented by the integrated configuration input. All final
repository flake checks passed.

The stable portal URL is
`https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-18-codex-web-portal-waiting/`.

## Implemented result

- `codex-web` is Apache 2.0 licensed. `README.md` is a user entry point with
  purpose, features, quick use, embedding/API, trust boundary, and license.
  The former technical README is byte-for-byte `docs/reference.md`.
- The Codex sidebar icon gains an amber overlay dot without increasing the
  rail's width. The dot appears only for a fresh successful activity read of
  an idle interactive session or a provider-marked blocking request, and clears
  for paused, stale, unavailable, nonblocking, or resumed activity.
- The large Ruby entry-point suites now load focused lifecycle test files and
  shared support while retaining their original commands and scenarios.
- `codex-web` owns request blocking classification. Command, file-change,
  permission, and default user-input requests are blocking. An explicit
  user-input `isBlocking` value remains authoritative. Unsupported MCP
  elicitation receives an immediate local rejection, stays nonblocking, and is
  removed from activity recording, so it cannot leave a false waiting signal.

## Repositories and source order

| Repository | Base | Head |
| --- | --- | --- |
| codex-web | `7429ff29` | `0a75d720` |
| dev-workspace | `18817f4b` | `b52a2363` |
| vpsfree-dev-workspace | `e170ea0` | `298a8a4` |
| workspace | `77afe04b` | `4bdc90b6` |
| vpsfree-cz-configuration | `c7ed1210` | `5b500b2d` |

The source order is `codex-web@0a75d720` → `dev-workspace@b52a2363` →
`vpsfree-dev-workspace@298a8a4` → `workspace@4bdc90b6`. Aitherdev's
`devWorkspace` channel directly selects `b52a2363`; there is no schema,
persisted-state, manifest, journal, API-shape, or migration change.

## Verification and review

- Detached baseline and refactored Ruby loaders both passed: 316 runs and
  3,526 assertions for `dev_session_test.rb`; 77 runs and 490 assertions for
  `workspace_host_test.rb`. Evidence is under
  `/home/aither/.local/state/dev-workspace-evidence/2026-09-18-codex-web-portal-waiting/`.
- Portal Go web tests, browser JavaScript syntax checks, exact README move,
  final focused Codex policy/activity tests, Nix flake evaluations, and
  `confctl` input-update hooks passed. The generic package's final fixed-output
  vendor hash is `sha256-8Z6/cgM5VTFaHVGgGSqkPTIJre0KDyqV6sGPxpPnGIw=`.
- The final mandatory review packet is [review-packet.md](review-packet.md).
  Its initial Terra/xhigh review found an accepted-response indicator defect
  and repeated dependency-pin history. The implementation now shares the
  actionable prompt projection, covers a stale pending read, amends the Codex
  commit body, and consolidates pins. The accepted browser regression now
  passes with a deterministic cache-expiry advance; the final source and its
  direct consumer pins were then refreshed. General and architecture focused
  rechecks were clear; the final Terra/xhigh risk recheck was also clear on
  the exact final heads. It confirmed accepted responses, stale/failed/paused
  activity, nonblocking prompts, resumed work, privacy, and direct pin
  topology without a compatibility or rollback finding.
- No GitHub Actions run is awaited, as the user directed.
- `confctl build --yes` built aitherdev successfully, and dry activation then
  switch both passed for generation `2026-09-18--15-07-57`. The switch health
  checks reported `systemd` running and the firewall active (two passed, zero
  failed). The endpoint is reachable and returns its expected `401` without a
  browser login; this host's private development CA is not installed in the
  local curl trust store.
- `nix flake check --print-build-logs` passed at `codex-web@0a75d720`,
  `dev-workspace@b52a2363`, `vpsfree-dev-workspace@7099f382`, and
  `workspace@578288ad`, with no unexpected local kernel build. The combined
  log is `/tmp/codex-web-portal-final-flake-checks.log`.
- During integration, the extension default branch had advanced with an
  independent Codex runtime pin. The feature was rebased onto `e170ea0`, its
  lock conflict resolved by retaining the reviewed generic and Codex sources,
  and `nix flake check --print-build-logs` passed at `298a8a4`. The workspace
  input was refreshed to that head, rebased onto its current shared master, and
  its flake checks passed at `4bdc90b6`. These dependency-only rebase updates
  did not alter the reviewed portal or provider behavior.
- Remote default-branch heads were verified after fast-forward integration:
  `codex-web@0a75d720`, `dev-workspace@b52a2363`,
  `vpsfree-dev-workspace@298a8a4`, `workspace@4bdc90b6`, and
  `vpsfree-cz-configuration@5b500b2d`. No CI run was inspected or awaited.

## Deployment and recovery

The user explicitly authorized this development deployment and subsequently
directed configuration integration. Retain the feature branches and the prior
user-profile generation. Roll back the profile with
`workspace-host rollback` if the portal runtime needs to return to the prior
generation; no data conversion is involved.

## Next action

No implementation, verification, deployment, or integration work remains.
The feature branches are retained for recovery. Do not archive or delete this
completed initiative unless the user explicitly requests that lifecycle action.

## Documentation

`codex-web/README.md` and `codex-web/docs/reference.md` are the reusable user
and technical documentation. `dev-workspace/README.md` describes the indicator,
and its test README describes the retained loader structure. The plan, this
state, [review packet](review-packet.md), and
`notes/dev-workspace/2026-09-18-vendor-hash-refresh.md` retain the temporary
review, deployment, compatibility, and vendor-refresh rationale.
