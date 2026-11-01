---
lifecycle: active
---

# HaveAPI patch release: documentation Switch user

## Current status

Phase: investigation/design. Identity and environment match the thread-bound
2026-11-01-haveapi-0321-docs-switch-user in /home/aither/workspace/ai/vpsfree.cz.
Full team delegated preset is live: architect0 Astra/xhigh; implementer0 and
implementer1 Sol/xhigh; reviewer0 Sol/xhigh; observer0 read-only. Saved workspace
write access verified for architect and both implementers. Architect investigation
assigned; application edits await its brief and newly registered worktrees.

## Phase checklist

- [x] Verify identity, roster, scope and runtime communication grant.
- [ ] Commit substantive initial plan/state before project commits/publication.
- [ ] Inspect live master/stable/tags and release policy; accept design/backports.
- [ ] Implement fix/backports/release metadata; commit and pass quick checks.
- [ ] Independent final whole-history/migration review; resolve findings.
- [ ] Applicable longer/release checks and protected integration.
- [ ] Publish packages/tag and prove registry/install readiness.
- [ ] Notify originating lead with exact provenance and update handoff.

## Backlog and dependencies

- architect0: design.md, exact interface and compatible patch inventory; first
  milestone is public-interface recommendation plus stable/release findings.
- implementer0: OAuth complete package after accepted design.
- implementer1: independent backport/release package after boundaries settled.
- reviewer0: final review only after all intended changes committed/quick green.
- Lead: tracking, coordination, acceptance and protected release integration.

## Repositories and authorization

HaveAPI only; no worktrees registered yet. Canonical origin is SSH
 git@github.com:vpsfreecz/haveapi.git. User's current request explicitly approves
required HaveAPI integration/tag/package publication for this patch; exact target
branches will be recorded after policy inspection. No production deployment.

## Evidence and next action

`dev-session current` and both environment markers match. Live roster inspected.
`session_communication list` proves active exact-pair grant; do not create another.
Workspace has unrelated changes; stage only this session's records. Initial
workspace index was empty. No declared workspace hook framework found in HEAD.
Next: commit initial records, register fresh HaveAPI worktrees and receive design.

## Known limits

Expected version 0.32.1 is unconfirmed. Fixed initial docs-cookie expiry is outside
scope. Release readiness requires real published packages. Leave session open;
no archive, deletion, stop or cleanup is requested.
