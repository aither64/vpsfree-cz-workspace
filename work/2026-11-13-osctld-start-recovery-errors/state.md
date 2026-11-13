---
lifecycle: active
---

# Status
Phase: setup and bounded investigation. Session/environment binding verified as 2026-11-13-osctld-start-recovery-errors in /home/aither/workspace/ai/vpsfree.cz. Retained delegated_4 roster confirmed; architect/implementers have workspace_write, reviewer read_only, execution full_access. No merge or deployment authorized.

## Phase checklist
- [x] Verify identity and retained roster
- [ ] Initial plan/state committed; independent worktree registered
- [ ] Architect design and bounded investigation accepted
- [ ] Diagnostics implemented and quick checks passed
- [ ] Independent final code/history review passed
- [ ] Required longer checks and exact-head CI passed; feature published
- [ ] Handoff ready, awaiting merge approval

## Packages
| Package | Owner | Deliverable / boundary | Dependencies and acceptance | Status / evidence |
| --- | --- | --- | --- | --- |
| D design | architect0 | design.md, settled diagnostic brief and race proposal | Current gate/race/July evidence; compatibility and safe recovery | Ready to assign |
| A diagnostics | implementer0 | osctld start gates, focused tests, relevant recovery docs | Architect brief; lead writing pass before commit; gates/contracts/force safety | Blocked on design |
| B July comparison | implementer1 | july-comparison.md; read-only old records and committed refs | Concrete guest shutdown/reboot/import/hook/link/admission functions/tests, explicit gaps | Ready to assign |
| C current race | implementer2 | race-evidence.md; read-only current callback/import/recovery source | Bounded incident proof/hypotheses, minimal alternatives and regression cases | Ready to assign |
| E contracts/checks | implementer3 | contracts-checks.md; read-only CLI/API/start/restart/boot/test inventory | Gate/consumer coverage and proportional established quick/long commands | Ready to assign |

## Repositories and commands
vpsadminos worktree/branch pending. dev-session current matched full environment and thread binding. Workspace stays on master; large unrelated dirty state preserved. No staged changes at inspection. Current upstream instructions read from canonical origin/staging; fetch/base verification pending.

## Next action / risks
Commit initial records, create isolated worktree and dispatch investigation. Exact early callback response and guest initiator intent are unconfirmed; avoid overstating source-backed hypotheses. No production log access needed yet. No cleanup/lifecycle actions requested.
