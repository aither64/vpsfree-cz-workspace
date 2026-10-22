---
lifecycle: active
---

# Automatic retries for failed Codex turns

## Status

Implementation authorized; architect recording design before application edits.
No application changes, review, tests or deployment yet. No merge approval.

## Phase checklist

- [x] Session identity/roster/access verified; planning and source investigation.
- [x] User preferences: capacity indefinite, cyber30/5min, default-on, new failures only.
- [ ] Architect-owned durable design and initial tracking commit.
- [ ] codex-web implementation and quick checks (implementer0).
- [ ] dev-workspace implementation and quick checks (implementer1).
- [ ] Dependency/configuration pins, final commits and whole-branch inventory.
- [ ] Independent final review; long package/native verification.
- [ ] aitherdev build/deployment/live verification and user acceptance.
- [ ] Explicitly approved integration; machine release only if directed afterward.

## Backlog

| Owner | Expected result / acceptance | Dependency / checks |
| --- | --- | --- |
| architect0 | design.md: fixed interfaces, boundaries, invariants and checks | Plan/source findings; before application edits |
| implementer0 | library primitive, projection and generic API/browser capability | Design; ledger/race/protocol and UI quick checks |
| implementer1 | runtime scheduler/store/admission/recovery and docs | Design; dispatch depends library; focused quick checks |
| Lead | Tracking, copy/acceptance, review packet and rollout coordination | Committed deliverable plus quick checks before review |
| reviewer0 | Independent final review and history/migration conclusions | Entire intended committed deliverable and quick checks |

## Evidence and current constraints

- dev-session current and both environment markers match exact thread binding.
- Retained ready architect0 workspace_write Astra/xhigh; implementer0 and1
  workspace_write Sol/xhigh; reviewer0 read_only Sol/xhigh; execution full_access.
- Earlier creation error resolved: current creation state ready. Architect verified
  identity from owned tracking CWD and completed read-only source investigation.
- Installed runtime483d4e7e source matches all535 files; libraryea64ef57. Existing
  workspace pins older: preserve current installed lineage while preparing update.
- Official App Server docs: https://developers.openai.com/codex/app-server/.
- CyberPolicy binary token is evidence but generated-schema check remains required.
- No supported native turn/retry; use existing visible recovery continuation.

## Repositories and heads

No feature worktrees registered yet. Intended: codex-web, dev-workspace,
workspace, vpsfree-cz-configuration. Register exact bases/heads during setup.

## Documentation

[Plan](plan.md); architect design.md pending. Session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/

## Next actions

Commit initial plan/state, obtain architect brief, delegate two execution packages.

## Authorization and ownership

User “Implement the plan” authorizes implementation and its planned aitherdev
rollout. No integration approval, reboot, machine release or session lifecycle
cleanup direction. No resources reserved; session stays active/open.
