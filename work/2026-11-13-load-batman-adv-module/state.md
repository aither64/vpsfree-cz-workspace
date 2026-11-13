---
lifecycle: active
---

# Load batman_adv in vpsAdminOS

Phase: design. Session/environment identity verified as
`2026-11-13-load-batman-adv-module` in `/home/aither/workspace/ai/vpsfree.cz`.

- [x] Verify identity and retained team access.
- [ ] Settle design and dependency evidence.
- [ ] Implement, commit and pass quick checks.
- [ ] Independent final review.
- [ ] Finish applicable runtime checks / CI and publish branch.
- [ ] Integration (requires explicit approval); deployment not requested.

## Packages

| Package | Owner | Dependency / acceptance | Status / evidence |
| --- | --- | --- | --- |
| D: module loading design | architect0 | Existing loader/dependency path; sufficient brief | Assigned 2026-11-13, executing; [design](design.md) |
| I: narrow OS change | implementer0 | Accepted D; source, quick checks, commit, evidence | Blocked on D |
| R: final review | reviewer0 | Committed I + quick checks; history/dependency conclusion | Not assigned |

## Repositories and next action

Only `vpsadminos` is in scope. Feature branch/worktree setup follows initial
tracking commit. No machine reservation, deployment or merge approval exists.
Next: accept architect brief and release implementation.

## Documentation and verification

Workspace procedures and repository AGENTS.md read. Documentation decision:
short source rationale only if useful; keep temporary evidence here.
Shared workspace has unrelated dirty records; preserve them and stage only owned
paths. No session lifecycle cleanup is authorized.
