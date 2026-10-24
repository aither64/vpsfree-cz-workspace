---
lifecycle: active
---

# 2026-10-24-workspace-session-ui

## Status

- Phase: implementation preparation. User approved implementation and added
  silent queue-refresh behavior; architect is amending the design.
- Session identity verified against `dev-session current`, both environment
  markers, and the trusted thread binding.
- Live roster inspected; `architect0` is ready with saved `workspace_write`
  access and owns investigation/design. Implementers and reviewer are unassigned.

## Phase checklist

- [x] Verify session identity, scope, procedures, and saved roster.
- [x] Inspect causes and prepare architect-owned design.
- [x] Assess findings and present solution proposal.
- [ ] Amend design for silent routine queue checking/shared refresh policy.
- [ ] Implement all four fixes and pass quick checks; commit deliverable.
- [ ] Independently review final branch history, behavior and compatibility.
- [ ] Longer verification and feature publication/CI.
- [ ] Integration and deployment (separate direction; not authorized).

## Backlog

| Owner | Expected result | Acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| architect0 | Amend design for queue-refresh notice | Source-backed reuse of shared refresh policy; preserve actionable errors and confirmed queue | Existing design; no application edits |
| implementer0 (planned) | Settings switches | Existing style, keyboard/save semantics; focused checks and commit | Initial tracking commit/worktree setup |
| implementer1 (planned) | Filtered unread then composer and queue-refresh fixes | Four-issue behavior complete; original delivery identity/intent preserved | Design amendment; serialized app.js edits/Git |
| reviewer0 (later) | Independent final review | Explicit history, migration and risk conclusions | All intended code committed, quick checks pass |
| lead | Tracking, prose, acceptance, verification coordination | Evidence assessed, branch published, no unauthorized integration | Member reports and required checks |

## Next actions

- Commit substantive initial tracking, register a dedicated `dev-workspace`
  worktree from refreshed origin/master, and assign implementation packages.

## Documentation

- [Plan](plan.md); [architect-owned design and verification brief](design.md).
- Lead assessed the design against all three reported behaviors. This is routine
  investigation/planning, so no automatic independent review was assigned.
- Stable session URL:
  <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>.

## Repositories

- Candidate scope: `dev-workspace` and `codex-web`; no feature worktrees/branches
  registered or created.

## Commands run

- `dev-session current`; checked both identity environment markers.
- `dev-session team list 2026-10-24-workspace-session-ui --as-is`.
- Assigned proposal investigation to `architect0`, message
  `d121ca08-2bd5-460d-b605-c42c5a9e3682` (submission accepted).

## Results

- No application edits, tests, builds, independent review, or deployment.
- Architect inspected cached `origin/master` revisions without fetching:
  `dev-workspace` `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734` and `codex-web`
  `11ec57d2203fc735696fe75a837d47da55a5c6af` (matching the runtime's Go pin).
  Canonical bare HEAD refs were older; final evidence uses these cached remote
  refs and does not claim fresh upstream or deployed-source proof.
- `dev-workspace` `portal/internal/web/static/app.js`: unread badge uses any
  transcript change, separately from rendering filters (line 4707). Ordinary
  Send detaches/persists the draft and permits typing (5548–5557), but both
  submit buttons are disabled while `messageDispatchInFlight` (4315–4316), and
  another submission returns early (5488). Queue next additionally disables
  all inputs for the submission lifetime (5500–5501, 5581).
- Existing `.retry-policy-switch` controls in `session.html` provide the settings
  pattern. Existing prompt persistence/IDs and per-thread serialization should
  be preserved; concurrent native steer ordering is not established.

## Open questions

- No blocker to the proposal. Implementation must verify native multiple-steer
  consumption/order and browser-buffer recovery across reload. Ordered dispatch
  and original-ID reconciliation are required; native concurrent steer ordering
  has not been established.

## Cleanup

- No resources acquired. Leave the session open.
