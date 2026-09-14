---
lifecycle: active
---

# 2026-09-13-auth-email

## Repositories

- Proposal only; no registered feature branches or project worktrees.
- Fetched `repos/vpsadmin.git` / `origin/master`:
  `791ab3aa89e2f613979da6090b89785c78245db5`.
- Inspected HaveAPI clients at local `haveapi HEAD`
  `1e475d2e39f0b33a009a5e17c9aac3439da0c546` and
  `haveapi-client-php HEAD` `a8b1b403a75a29287659ea983957c42d9a071214`.
  These client refs were not fetched; recheck them for implementation.
- Read `vpsfree-kb-contracts origin/master` documentation workflow.

## Status

- 2026-09-14: inspected login/device/profile/mail code and prepared the solution
  proposal in `plan.md`. The user requested a suggestion, not implementation.
- No project code, remote branch, deployment, or production wiki changes.
- Session remains active and open for design feedback or implementation.

## Commands run

- `dev-session current`, with matching `DEV_SESSION_SLUG` verified.
- Workspace Git status/index inspection; unrelated changes preserved.
- `git --git-dir=repos/vpsadmin.git fetch origin`.
- `git show`, `git grep`, and `git ls-tree` for the refs above; read vpsAdmin
  `AGENTS.md` and inspected password recovery compatibility.
- Applied dev-session-handoff and vpsfree-user-facing-writing skills, including
  English humanizer guidance for the proposed profile wording.
- Consulted official OWASP/NIST email authenticator guidance.
- `dev-session url 2026-09-13-auth-email --as-is`.
- Tracking whitespace check and initial coordination commit on shared `master`
  after fetching origin; local master was two commits ahead and zero behind.

## Results

- Device trust uses cookie tokens; successful-login history survives revocation
  and expiry. Current trust must also test `known`, not just an active row.
- Basic and password token issuance share password verification with OAuth2.
  A browser-only check would leave alternative password login routes available.
- Password recovery provides exclusive primary-email delivery and generation
  handling to reuse. Rendered mail persists in both mail logs and transaction
  payloads, so login codes need explicit handling in both paths.
- No runtime tests or mandatory implementation review: this is a coordination
  design proposal. Implementation verification/review is planned in `plan.md`.
- Portal returned HTTP 401 in a diagnostic curl check with certificate
  verification disabled. Ambient curl lacks the private CA. The existing
  lesson `notes/cross-project/2026-09-07-portal-curl-private-ca.md` identifies
  a public CA file on aitherdev, which is absent locally; a read-only SSH
  attempt to check there failed host-key verification. No trust configuration
  was changed. The listener is reachable, but TLS was not verified here.

## Open questions and next action

- User design feedback is next; implementation has not been requested.
- Recommended clarification: count retained successful known-device history.
  Requiring a currently valid known-device token would turn protection off
  after the last token expires or is revoked.
- Challenge limits are proposed initial values, not existing defaults.
- Implementation must verify CLI/Terraform authentication modes and choose the
  smallest transport change protecting mail logs and queued payloads.

## Cleanup

- No project worktrees, cluster, captures, or secret files created.
- `portal.yml` accurately lists no repositories/artifacts; proposal/status use
  the standard tracking files.
- Leave the session open; no lifecycle cleanup is authorized.
- Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-13-auth-email/
