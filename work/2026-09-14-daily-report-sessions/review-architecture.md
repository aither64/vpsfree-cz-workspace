# Architecture and repetition review

Reviewed the complete committed functional series for:

- `vpsadmin`
  `791ab3aa89e2f613979da6090b89785c78245db5..8769884ae69b03c22d8532fd09acf6de85542015`
- `vpsfree-notification-templates`
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..4dc2706df6332d235cad18c1202602004b75d63c`

The vpsAdmin API owns the aggregate payload and its built-in text consumer.
The notification-template repository is the external HTML consumer. The
configuration pin commits are deliberately deferred until after functional
review and are outside these reviewed heads.

No Blocking or Important findings.

## Advisory

### 1. The report adds another implementation of usable-session policy

Commit `8769884ae` implements the active-session snapshot as a standalone SQL
predicate in
`api/lib/vpsadmin/api/daily_report_authentication.rb:54-79`. It repeats the
account-state allowlist, lockout/password-reset checks, per-mechanism enable
flags, permanent-token representation, access-token expiry boundary, and
OAuth2 refresh-token fallback that are independently implemented by:

- `api/lib/vpsadmin/api/operations/user_session/resume_token.rb:8-23` and
  `resume_oauth2.rb:8-23`;
- `api/lib/vpsadmin/api/authentication/oauth2_config.rb:382-409`;
- `api/models/oauth2_authorization.rb:17-19`; and
- `api/lib/vpsadmin/api/tasks/user_session.rb:8-43`.

The new specs prove that today's copies agree for selected examples, but they
do not make that agreement structural. A later account-state rule, token
lifetime, OAuth2 relationship, or expiry-boundary change can update the login
or cleanup owner while the report continues to pass and silently calls an
unusable credential active (or omits a usable one). This is especially likely
because the new helper comments that it must match the resume operations while
having no shared interface with them.

There is no narrow extraction inside the accepted reporting-only boundary that
removes this duplication. Moving the SQL predicate into a model would only
relocate the report's copy; sharing it structurally requires changing the
authentication callers, while cleanup intentionally has narrower semantics
than account usability. Keep the bounded projection, its explicit parity
comment, and the existing fixed-time boundary fixtures in this change. Record
a dedicated follow-up to design a time-parameterized stored-credential
eligibility interface in the owning session/OAuth2 domain, with focused
provider tests, before a future authentication-policy change creates drift.

### 2. Recovery stage and deadline selection now has a third owner

Commit `8769884ae` derives the applicable recovery deadline and terminal state
inside the report helper
(`api/lib/vpsadmin/api/daily_report_authentication.rb:88-106`). The same state
machine is already expressed by `PasswordRecovery#email_token_usable?`,
`#session_usable?`, and `#active_state?`
(`api/models/password_recovery.rb:58-68`) and again by the expiry cleanup query
(`api/lib/vpsadmin/api/tasks/authentication.rb:58-68`). The report needs a
historical cutoff and completion precedence, but the choice between email and
session deadlines is the same domain rule.

If another recovery stage is added, a deadline changes, or stage selection is
refined, the interactive flow and cleanup can be updated without changing this
CASE expression. Daily reports would then classify pending, expired, and
invalidated attempts using obsolete semantics while their local aggregation
tests still pass.

The report deliberately needs fixed-cutoff and completed-plus-invalidated
semantics that the current live predicates do not expose. Moving only its CASE
expression into `PasswordRecovery` would not remove the parallel behavior;
making cleanup consume it would broaden this feature into a security-sensitive
runtime refactor. Keep the bounded projection and its boundary fixtures here,
and record a dedicated domain-refactor follow-up if recovery gains another
stage or changes deadline semantics. That follow-up should define the shared
time-parameterized relation and test its live and historical consumers.

### 3. Authentication types are catalogued independently in the resource and report

The new `AUTH_TYPES` constant and active-mechanism conditional live at
`api/lib/vpsadmin/api/daily_report_authentication.rb:4,37-38,61-64`, while the
public UserSession resource separately declares the same finite choices in
`api/lib/vpsadmin/api/resources/user_session.rb:10`. The text and HTML
consumers then carry their own label maps
(`api/notification_templates/templates/daily_report/email/en.text.erb:16-18`
and notification-templates commit `4dc2706df`,
`templates/daily_report/email/en.html.erb:286-290`).

For a new stored authentication mechanism, created counts automatically expose
a raw extra row, but active counts silently exclude that mechanism until the
SQL conditional is edited; the API choice list and both labels also require
separate updates. Give the finite machine-level type catalog one owner, reuse
it for the resource choices and report's zero-row/exhaustiveness checks, and
fail a provider-level test when a known type has no active-classification
strategy. Presentation labels should remain local to each language/template,
with their existing safe fallback for genuinely unknown stored values.

## Residual risks and validation gaps

- The aggregate payload is additive, the external template guards all four new
  top-level sections, and vpsAdmin's render spec exercises both the built-in
  text template and the external HTML template when supplied. No additional
  consumer or duplicate aggregate implementation was found.
- Repetition between text and HTML layout is appropriate for independent
  format and branding consumers. The duplicated machine-key label maps are
  covered by the narrower catalog finding above.
- The migration, selector entry, and delivery assertions stay in their owning
  vpsAdmin components. No abstraction or cross-project interface issue was
  found in those changes.
- Long integration tests and final configuration pin/build verification remain
  pending as recorded in the packet.
