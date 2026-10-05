---
lifecycle: active
---

# Repeated VPS deletion investigation

## Current phase

Investigation and proposal; application code unchanged.

## Phase checklist

- [x] Verify bound session identity and retained same-session roster/access.
- [x] Assign nontrivial diagnosis/design to architect0.
- [x] Decode all three emails without copying raw inputs into Git.
- [ ] Reconcile deployed and current behavior and finalize recommendation.
- [ ] Record design/verification brief and hand off findings.
- [ ] Implementation, local runtime checks, final review and deployment: not requested.

## Evidence so far

All three reports are DELETE requests to the v7.0 VPS endpoint. All fail with
`environment=1/2/5,class_name=Vps,direction=leave,state=soft_delete`.
The May reports name deployed revision 8cd6889929f90199d4edd166d8ffcf8eb1e9868f;
October names f9beb46e5206864bca9d37672e1419cf03661467. Both revisions exist in
the canonical bare repository. Current inspected baseline:
9fc0648accd414246d6422e67106ae7217486020.

Lifetimes classifies equality as leave and resolves required expiration before
acquiring the wrapper's resource lock. May DELETE lacks a VPS state guard;
October/current code rejects inactive VPS for non-admins but bypasses it for
admins. The emails alone do not establish actor role or success of the preceding
request. October raw request parameters are not proof of effective normalized
input or role.

## Repositories and verification

Read-only canonical repos/vpsadmin.git; no branch, worktree or source edits.
Read repository AGENTS.md, README.md and transaction/overview documentation.
Verification so far is static source/stack inspection only; no runtime tests,
production database reads, CI or deployment.

## Next action and risks

Complete architect findings, validate retry/locking and blocking response
semantics, then present a concrete recommendation. Production first-request
outcome remains unknown without transaction/state logs. Preserve account and
ownership restrictions; do not acknowledge unrelated operation locks as deletion.

## Inputs and cleanup

Three raw .eml inputs remain in portal upload storage outside Git. Session stays
open. No cleanup, archival or lifecycle terminal transition is requested.
