---
lifecycle: active
---
# Token-auth compatibility

Phase: investigation/design. Session identity verified against thread binding
and both shell markers. User authorizes HaveAPI master integration, backport
to 0.31 and a new patch release. No deployment requested.

## Phase checklist

- [x] Scope, session and retained team verified
- [ ] Architect design and release-target assessment
- [ ] Fix and regression specs committed; quick checks pass
- [ ] Independent final review, whole-history and migration conclusions
- [ ] Relevant longer verification
- [ ] Approved master fast-forward integration
- [ ] 0.31 backport, patch metadata and independent review
- [ ] Release build, protected publication and registry verification

## Backlog

| Owner | Result | Acceptance/dependencies/checks |
| --- | --- | --- |
| architect0 | design.md and diagnosis | Minimal supported name normalization; real mounted JSON-copy boundary; release branch/version convention |
| implementer0 | Fix/specs, then backport/metadata | Depends on design; source regression red/green, quick lint/specs and hooks; full report and clean commits |
| reviewer0 | Independent final review | After committed quick-checked deliverable; explicit complete history/no-migration conclusion |
| lead | Integration/release coordination | Review/check evidence; fresh target and ownership; exact remote heads; publication receipts |

No blockers so far. Shared workspace contains unrelated changes; preserve them.
Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-token-auth-compatibility/
