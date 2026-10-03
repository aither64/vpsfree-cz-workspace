---
lifecycle: active
---

# API exception from newadmin

## Current status

Investigation in progress. Session identity matches the thread binding and both
environment markers. No application edits or production operations.

## Phase checklist

- [x] Verify session identity and retained roster.
- [x] Extract sanitized exception and identify the exact deployed API revision.
- [ ] Trace API session/token cleanup and WebUI authentication behavior.
- [ ] Reconcile independent architect findings and verification evidence.
- [ ] Deliver root cause, uncertainty and proposed correction to the user.

## Evidence

Email dated 2026-10-03 16:47:13 +0200 reports `NoMethodError` on
`GET /v7.0/users/current`, with Origin `https://newadmin.vpsfree.cz`.
The API is `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`; the exception is at
`api/lib/vpsadmin/api/operations/user_session/resume_oauth2.rb:40`:
`oauth.single_sign_on.token.valid_to < user_session.token.valid_to`.
The raw email remains in the uploaded private input location outside Git.

## Team and repositories

- `architect0` (design, Astra/xhigh, workspace write): independent API trace and
  proposed fix/verification brief in `design.md`.
- Lead: report extraction, WebUI trace, reconciliation and coordination records.
- Implementer and reviewer are retained but have no application assignment.
- Canonical bare repositories: `repos/vpsadmin.git`, `repos/vpsadmin-webui.git`,
  `repos/haveapi.git`. No project feature branches or worktrees created.

## Next action and limitations

Trace why an existing SSO row can lack its token while an OAuth access session
remains valid. No production database or correlated cleanup logs have been
inspected. The report alone may not distinguish expiration from revocation or
a concurrent cleanup race.

## Documentation

[Investigation plan](plan.md); architect brief pending. No project documentation
change is needed until a correction is implemented.
