---
lifecycle: active
---

# Workspace session naming

## Current status

Phase: implementation preparation. User approved the final 30-second naming plan
and its aitherdev deployment route. No default-branch merge approval exists.
Session identity and retained ready workspace-write design/implementation members
verified. Shared workspace has extensive unrelated changes; preserve them and stage
only this session's owned paths.

## Phase checklist

- [x] Diagnose generic fallback and aborted native retry.
- [x] Agree final behavior: shared30s, automatic retry, ultimate manual entry.
- [ ] Save final architect design and initial tracking commit.
- [ ] Implement A client and B runtime packages; integrate exact pins.
- [ ] Pass quick checks and commit/publish intended changes.
- [ ] Independent final whole-branch review.
- [ ] Long native/packaged checks and deployment builds.
- [ ] Deploy host then application profile; verify real naming and continuity.
- [ ] Obtain any later merge/acceptance/release directions separately.

## Owners and next actions

architect0 updates design.md. implementer0 owns codex-web; implementer1 owns
dev-workspace. Both are preparing own registered worktrees and must await the saved
design before substantive edits and initial tracking confirmation before project
commits/publication. Lead owns plan/state, acceptance, review and rollout.

## Branches and documentation

- dev-workspace: worktrees/2026-10-20-workspace-session-naming/dev-workspace,
  branch 2026-10-20-workspace-session-naming, initial fetched base bf6d4b0.
- codex-web: registration/setup pending report.
- Design/evidence: design.md. Initial incident: utility_error fallback from
  dev-workspace fdb13f838194; native retry warning interrupted by client.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/

## Verification and risks

No application implementation or tests completed yet. Prior investigation confirmed
the pinned native ErrorNotification contract. Provider preferred-account availability
cause remains external/unknown; require real selected-provider smoke verification.
Before activation inspect current machine ownership and selected runtime policy;
never borrow another session's reservation or recovery record.

## Cleanup

No lifecycle action requested. Preserve this session, feature branches and unrelated
workspace changes. No resource claim held by this session yet.
