# Scope and proportionality review

Reviewed with the mandatory-change-review scope lane at
`gpt-5.6-sol` / `xhigh`:

- `vpsadmin`
  `cf2c8734c9091327cbc9157d43915695e9750bc5..d6f51b6e8ad9d78c68e6d0f0ce5276ca610e7bf8`
  (`95a67e55e9695b5a7f56b491af186840c389f444` and
  `d6f51b6e8ad9d78c68e6d0f0ce5276ca610e7bf8`)
- `vpsfree-notification-templates`
  `06f03bad4294b6f28ca9478e907f43967ebeb7d0..97ac666a390fc028c5b610b48c9963adb9e0b4ef`

I inspected the review packet, initiative plan and state, repository guidance,
exact commit series and diffs, existing login-code and new-device mail paths,
template ownership and style, authentication evidence flow, focused specs,
browser fixture/assertions, rollout documentation, and synthetic preview
method.

## Findings

No Blocking, Important, or Advisory scope-and-proportionality findings.

## Proportionality assessment

The mail refinement is the smallest maintainable implementation of the accepted
presentation contract. `EmailLogin.start` snapshots only the display data needed
by the message, using existing `AuthToken` fields and options. Mail rendering
delegates reverse DNS to the existing DNS helper and device display to the
existing `UserAgent#to_user_friendly_s` formatter. The service-name argument has
one current OAuth consumer and a concrete token-login default. No new schema,
metadata model, formatter, resolver, registry, or public authentication action
was introduced.

The added template variables correspond exactly to the requested
service/time/device/IP/PTR layout. Retaining the earlier `user_agent` variable is
an explicit compatibility choice, while the rollout note records the only new
cross-repository ordering constraint. The four HTML templates are deliberate
copies in the two existing template owners and two supported languages; that
duplication is required by the current built-in/production packaging boundary.
The templates add no HTML variants to the separate new-device notification, in
line with the non-goal.

The notification change is one predicate on the already persisted, authority-
checked authentication method. It preserves the existing successful-session
device-known update and does not add a second trust marker or broaden the auth
protocol. Its normal, forced-reset, password/device and MFA assertions exercise
the stated boundary. The browser mail-count fixture changes are necessary to
prove that suppression is selective rather than an artifact of globally
disabled mail. The rendering tests and four synthetic previews cover owned
language, format, escaping and parity behavior without building a generalized
mail-rendering test framework.

The commit series is coherent: presentation, metadata and their documentation
are together; notice suppression and its focused assertions are separate; the
production template owner has one matching commit. No obsolete implementation
iterations, speculative fallback paths, or unrelated cleanup remain in the
reviewed diffs.

## Cross-lane issue and residual gaps

The exact reviewed vpsAdmin head performs reverse DNS at
`api/lib/vpsadmin/api/email_login.rb:85-86` while holding the user lock and
before the authoritative send-budget check. GENERAL and ARCHITECTURE already
reported this operational issue, so it is not duplicated as a scope finding
here. The coordinating agent's described remediation—an advisory availability
check using the same bucket definitions before DNS, with the existing locked
check remaining authoritative—does not broaden the product contract, but it is
outside the commit range reviewed above and still needs focused inspection and
verification.

The focused browser integration and exact rendered previews remain the relevant
post-review validation. Reverse rollback ordering requested by the risk lane is
also documentation work outside these reviewed heads. No further generalized
compatibility layer or mail framework is warranted for this follow-up.
