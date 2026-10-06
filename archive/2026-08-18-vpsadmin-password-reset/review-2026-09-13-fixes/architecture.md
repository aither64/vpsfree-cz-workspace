# Architecture and repetition review rerun

Reviewer: fresh `gpt-5.6-sol` / `xhigh`, architecture-and-repetition lane. I
reviewed the remediation commits and their affected consumers at the exact
heads in `packet.md`, including repository rules, prior findings, surrounding
implementation and tests, and relevant history. I did not launch nested agents
or modify a repository.

## Findings

### Blocking

1. **The strict AuthToken contract left a second test-token constructor
   unstamped and now breaks the regular WebAuthn API suite.** Commit
   `d0dd1f551b25ddd99c0f878d00328fe60cea9de1` correctly changed
   `vpsadmin/api/models/auth_token.rb:20-26` so only an explicit integer
   generation can satisfy `authentication_current?`. The shared fixture helper
   already owns this contract and stamps new tokens at
   `vpsadmin/api/spec/support/auth_operation_helpers.rb:39-56`, but the older
   local helper at `vpsadmin/api/spec/api/resources/webauthn_spec.rb:62-65`
   independently calls `AuthToken.create!` without `opts`. Every positive
   regular WebAuthn authentication example built through that helper is now
   rejected at `vpsadmin/api/lib/vpsadmin/api/resources/webauthn.rb:169-177`
   before a challenge is created.

   This is reproduced on exact head
   `41d590aa86b05439633db68e607405d6132da7f0` with:

   ```text
   nix develop .#api -c bundle exec rspec \
     spec/api/resources/webauthn_spec.rb:322 --format documentation
   ```

   RSpec selected the example at line 305 and failed one of one: the endpoint
   returned `status:false` where the example expects a challenge and
   `status:true` at lines 305-318. This file is assigned to the API resource
   topic in `.github/workflows/api-specs.yml:109`, so the final head does not
   have a passing relevant quick suite even though the narrower 235-example
   remediation selection passed. Remove the duplicate constructor and use the
   shared `create_auth_token!` helper, reserving explicitly unstamped records
   for the new negative compatibility examples. That localizes future pending
   token contract changes to one fixture owner.

### Important

1. **Recovery now owns a private WebAuthn metadata normalizer while the other
   writer of the same persisted contract remains unbounded.** Commit
   `d889044b3caf0137c8f9f1b8a012a05a6188d365` added
   `webauthn_client_version` at
   `vpsadmin/api/lib/vpsadmin/api/authentication/password_recovery.rb:507-511`.
   It repairs recovery by converting invalid UTF-8, replacing characters that
   utf8mb3 cannot store, and truncating to the database column limit. The
   ordinary registration and login implementation still creates the same
   `WebauthnChallenge` model through a separate factory at
   `vpsadmin/api/lib/vpsadmin/api/resources/webauthn.rb:13-33` and writes the
   raw request User-Agent to both `UserAgent` and `client_version`. The latter
   is the same utf8mb3, 255-character column declared at
   `vpsadmin/api/db/migrate/20250213133759_add_webauthn.rb:16-27`.

   A user with a valid, explicitly stamped MFA token and a 256-character ASCII
   User-Agent therefore still reaches `create_challenge!` and receives a
   persistence failure during ordinary passkey login; non-BMP or invalid input
   can fail earlier while inserting the raw `UserAgent`. The prior
   characterization already demonstrated `ActiveRecord::ValueTooLong` for 256
   ASCII characters on this exact challenge column. The recovery-only helper
   fixes one caller but creates two incompatible construction rules for one
   record type. Put database-compatible WebAuthn client metadata normalization
   in a shared challenge boundary or factory and use it from recovery,
   registration, and authentication. Cover the shared boundary plus a
   representative ordinary authentication request.

2. **The shared public password rule still omits the administrator-facing User
   Create action that advertises it.** Commit
   `41d590aa86b05439633db68e607405d6132da7f0` establishes
   `PasswordChanges::MINIMUM_LENGTH` and `valid_length?` at
   `vpsadmin/api/lib/vpsadmin/api/password_changes.rb:4-13`, and the four
   previously identified reset/update paths now use that owner. The same
   commit also derives the public `password` parameter description from that
   minimum at `vpsadmin/api/lib/vpsadmin/api/resources/user.rb:32-35`. User
   Create consumes that parameter at lines 122-129, but its execution path at
   lines 140-145 passes any non-empty value directly to `User#set_password`.
   The model has only a presence validation (`vpsadmin/api/models/user.rb:65`),
   and `set_password` intentionally has no public-policy validation.

   As a result, the public metadata says an initial password must have at least
   eight characters while an administrator can create a login-capable account
   with a one-character password. A future minimum change through the new
   owner updates Create's advertised contract but still does not update its
   behavior. Apply the shared predicate at User Create, or record an explicit
   initial-password exemption and give that parameter accurate action-specific
   metadata. Add a Create boundary example so the public consumer inventory
   cannot drift again. This mismatch predates the remediation, but the new
   shared-policy boundary and localized description make it an unresolved
   consumer of the contract under review.

### Advisory

No findings.

## Other assessed remediations

The Basic request propagation and MailLog nullability changes are localized to
their existing owners and representative consumers. The queue remediation
keeps admission, claiming, retention, completion, and retry under the existing
queue-lock boundary. Its near-identical `finish!` and `retry_or_finish!` bodies
have distinct terminal semantics and are small enough that extracting them
would not improve ownership. I found no additional architecture finding in the
history consolidation, exact downstream pins, or KB inventory refresh.

## Residual gaps

The queue tests supplied in the packet cover recent-claim retention and a row
that disappears before late completion/retry, but do not run retention and an
active worker concurrently. Static inspection shows both transitions serialize
on the same queue lock and that cleanup excludes a claim younger than
`CLAIM_TIMEOUT`. A process that runs longer than the five-minute claim timeout
can still be reclaimed or deleted, which is the accepted bounded retry behavior
from the prior reconciliation.

I ran only the focused regular-WebAuthn example described above; it failed in
18.56 seconds after the test environment loaded. I did not run the complete
WebAuthn file, the full API topic, or integration tests. The ordinary
WebAuthn long-header failure is established by the raw writer and shared schema
plus the prior same-column database characterization; it was not dynamically
reproduced again in this lane.

Reviewed heads: vpsadmin `41d590aa86b05439633db68e607405d6132da7f0`,
vpsfree-mail-templates `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`,
vpsfree-kb-contracts `497ad8e37e7478aa2fa8e86696829efcf755fd7b`,
and vpsfree-cz-configuration
`4a7ec36ea5a88b088cd77431fb12f4df0f57bd43`.
