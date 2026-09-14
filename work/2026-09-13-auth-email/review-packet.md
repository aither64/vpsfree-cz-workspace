# Email login implementation review

Read this packet, plan.md and state.md in the same directory. Review the
committed API/WebUI implementation and production mail templates directly.
Do not launch further agents or change code. Record findings in the assigned
review file. Review all commits, not only the final tree.

## Scope and acceptance

User requested implementation of optional email verification after a correct
password for accounts without effective TOTP/passkey MFA on unknown devices.
Preference defaults off and is editable in WebUI profile settings. Historical
successful device login is required; retained revoked/expired known records
still count. Current trust requires a usable known-device cookie for that user.

Fixed 30-minute challenges (the user requested at least 15 minutes for mail
delays), six digits, five wrong guesses, three sends with 60-second spacing,
three pending challenges/account. Shared fixed UTC bucket limits: account
5 sends/15m, 20/day, 10 wrong guesses/15m; IP 60 sends and 100 wrong guesses/15m.
Resend replaces code without extending challenge expiry or resetting attempts.
Forced password changes receive a fresh five-minute continuation after email.

Explicit user decisions: password-token issuance must enforce email too; Basic
rejects without sending mail. No email on enrollment, just current password.
Self-admin requires password; administrator override for another user is
allowed and audited. Full normal administrator-only mail history and queued
rendered payloads are intentional. Do not demand redacted/sensitive mail
transport or new secrets. Active MFA has precedence while preference persists.
Existing sessions, supplied tokens, refresh and valid SSO retain existing flow.

OAuth email challenges bind the browser cookie and original OAuth client,
redirect URI, scope, state and PKCE context. Recheck authority under the user
lock at completion and OAuth code exchange, including first-device bootstrap
and revocation races. Security changes invalidate pending authentication.
Enrollment gate defaults off and controls new opt-ins, not enforcement.

## Owning repositories

Workspace root: /home/aither/workspace/ai/vpsfree.cz
Initiative: work/2026-09-13-auth-email
Worktree group: worktrees/2026-09-13-auth-email
Branch in each repository: 2026-09-13-auth-email

- vpsadmin: API, database, OAuth page, PHP WebUI, built-in templates and tests.
  Base: 791ab3aa89e2f613979da6090b89785c78245db5
  Head: 3c24a6aadacb054732a2a22214c98e3edb03ef5c
  Commit split: API enforcement/schema/built-ins/unit tests/rollout guidance;
  then profile UI/translations/browser regression. Supporting migrations,
  authentication protocol, and unit tests remain with the API behavior.
- vpsfree-notification-templates: production bilingual template contract.
  Base: f944ba03eba5d0d6b58b7eb856f251d1c96f2c11
  Head: 06f03bad4294b6f28ca9478e907f43967ebeb7d0

Downstream KB publication preparation is a separate phase because its workflow
requires an exact pushed API revision. Its current local account-page
candidates may inform this review; contract pinning and the downstream commit
will receive separate review before completion. No production writes are part
of this request. Four pre-existing all-page annotation mismatches are recorded
in kb-impact.md; do not require unrelated page changes as part of this feature.

## Dependencies and compatibility

No new dependency, secret service, or node protocol. Existing bcrypt and mail
queue; new AuthToken enum value appended. Additive default-off users column,
nullable authorization proof JSON text, new shared rate bucket table.
Deploy schema/templates, update all API workers and WebUI, then open enrollment.
Old workers ignore enforcement and are unsafe for opted-in accounts. Rollback
keeps additive schema but explicitly loses enforcement; drain challenges and
accept that loss or keep the enforcing version. No vpsAdminOS/node updates.

HaveAPI client entry points inspected in installed client and fetched
HaveAPI a52769871096e45bf443767bb1a79546857784ae. CLI prompts for arbitrary
continuation input; Ruby/PHP clients support generic next_action callbacks.
PHP fetched 0f5f9dad0ff445bdd36c776390ce4c8e8415444e. Terraform provider
8e205a3b4b87160a42e69de63c28653d226e65c2 requires a supplied auth_token and
never issues it using a password. No client changes/pin updates are necessary.

## Quick verification

- 105 auth/mail/concurrency examples passed (including actual mail queue,
  browser binding/context, token/Basic, concurrent single-use consumption).
- 34 shared password/MFA/email-policy examples passed after consolidating
  active MFA in User.effective_multi_factor_auth?.
- 15 new email-flow/profile-setting examples passed.
- 2 migration/up-down/default/unique-bucket examples passed.
- Late OAuth forced-reset/browser lifetime regression: 1 example passed;
  affected Ruby files lint clean.
- Ruby lint clean; PHP syntax/gettext health/compilation, JS syntax, Nix parse.
- CI selector 16 tests/55 assertions pass; 405 non-migration specs each covered
  exactly once (migrations use their own workflow).
- Built-in template checker: 55 templates /177 files. Production flake check
  passed on staged contents.
- Integration/browser tests have not started, per mandatory review ordering.

Overall risk HIGH: authentication, persisted state, public continuation actions,
concurrency and rolling-deployment enforcement. Required lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. Every lane
uses gpt-5.6-sol with xhigh effort and fresh context as required by the skill.

Use Blocking/Important/Advisory severities, with concrete file/line/commit
references and failure scenarios. Report serious issues from other lanes if
you encounter them. State no findings clearly and note residual test gaps.
