# Targeted risk and compatibility review rerun

Reviewed the committed remediation snapshot from `packet.md` at these exact
heads:

| Repository | Reviewed head |
| --- | --- |
| vpsadmin | `41d590aa86b05439633db68e607405d6132da7f0` |
| vpsfree-mail-templates | `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11` |
| vpsfree-kb-contracts | `497ad8e37e7478aa2fa8e86696829efcf755fd7b` |
| vpsfree-cz-configuration | `4a7ec36ea5a88b088cd77431fb12f4df0f57bd43` |

The coordinator began a further uncommitted correction while this lane was
finishing. All source references below were therefore read from the explicit
vpsadmin commit with `git show`, and those later worktree changes are outside
this snapshot.

## Findings

### Blocking

None.

### Important

1. **The browser-metadata repair covers recovery WebAuthn but leaves both
   ordinary WebAuthn challenge paths on the same unsafe storage boundary.**
   Commit `d889044b3` normalizes the recovery challenge's `client_version` at
   `api/lib/vpsadmin/api/authentication/password_recovery.rb:491-511`, but the
   shared ordinary registration/authentication factory still passes
   `request.user_agent` unchanged to both
   `UserAgent.find_or_create!` and `WebauthnChallenge.client_version` at
   `api/lib/vpsadmin/api/resources/webauthn.rb:13-33`. The latter is a
   255-character `utf8mb3` string
   (`api/db/migrate/20250213133759_add_webauthn.rb:16-27`), and the permanent
   user-agent table is also `utf8mb3`
   (`api/db/schema.rb:1843-1847`). A member can therefore complete password
   authentication and then make ordinary passkey authentication fail with a
   256-character header; a supplementary Unicode character can also make
   either raw insert fail character-set validation. Registration has the same
   writer and failure. This is the same public input class and challenge model
   that the remediation now promises to bound, so keeping separate writer-side
   normalization leaves inconsistent behavior and a continuing persistence
   error path. Put the field-specific normalization at a shared model/factory
   boundary, use it for both challenge writers, and do not insert the raw
   ordinary header into `UserAgent`.

2. **User Create advertises the shared eight-character minimum but does not
   enforce it for an explicitly supplied initial password.** The shared
   parameter now publishes
   `PasswordChanges.minimum_length_description` at
   `api/lib/vpsadmin/api/resources/user.rb:32-35`, and Create imports that
   parameter at lines 122-130. Its execution path nevertheless sends any
   non-nil value directly to `User#set_password` at lines 140-145. The model
   validates only password presence (`api/models/user.rb:65`) and its setter
   encrypts the plaintext without a length check
   (`api/models/user.rb:206-228`). An administrator can consequently create a
   login with a one-character password even though the action metadata says
   at least eight and every other public password-change path rejects it. Apply
   the shared predicate when Create receives an explicit password while
   retaining the established omitted-password behavior, and cover both cases.

3. **The ordinary WebAuthn resource spec still manufactures a legacy
   generation-less login token, so the positive path fails and two negative
   examples can pass for the wrong reason.** The local helper at
   `api/spec/api/resources/webauthn_spec.rb:62-65` creates `AuthToken` without
   `opts`, whereas the canonical helper stamps the current generation at
   `api/spec/support/auth_operation_helpers.rb:39-57`. The remediation at
   `api/models/auth_token.rb:20-29` correctly treats the local fixture as stale.
   At the exact reviewed head, the focused command
   `nix develop .#api -c bundle exec rspec
   spec/api/resources/webauthn_spec.rb:305 --format documentation` failed its
   sole example at line 311 because the response status was false instead of
   true (one example, one failure). The expired-token and destructive-lifecycle
   examples at lines 278-303 also construct the same invalid token, so their
   expected rejection no longer proves the intended expiry or lifecycle
   checks. Use the canonical stamped helper, then retain explicit legacy-token
   coverage only where rejection of missing generation is the behavior under
   test.

### Advisory

None.

## Confirmed remediation behavior

- `AuthToken#authentication_generation` accepts only an explicit Ruby integer;
  nil, a missing key, null and strings cannot authorize, while integer zero is
  preserved. MFA, ordinary WebAuthn and reset continuations check it under the
  user lock. The deployment guide records that predecessor pending MFA/reset
  continuations must restart, preserves established sessions, and enforces the
  no-overlap writer barrier.
- Basic authentication now forwards the request to the transparent password
  rehash, so the sessionless audit record gets the client snapshot. MailLog
  Index and Show metadata now declare the account reference nullable.
- Queue admission, claim, retention and finalization use the same global lock.
  Retention excludes current claims, missing-row completion/retry is
  idempotent, and unrelated query/update errors still propagate through the
  worker's error path. I found no remaining static race that loses authority or
  silently suppresses another database failure.
- The recovery-only implementation correctly converts invalid and
  supplementary Unicode before truncating to the existing utf8mb3/255 limit,
  and its narrow `WebAuthn::Error` rescue no longer disguises storage errors.
- Configuration and KB pins match the packet heads. The five migrations remain
  additive and occur once in the rewritten history; no node protocol or
  coordinated vpsAdminOS upgrade was introduced.

## Residual gaps

- The new queue tests retain a current claim and synthesize disappearance, but
  they do not run retention and live worker completion concurrently on separate
  connections. Existing threaded queue tests establish serialization on the
  global lock, and the reviewed lock ordering is internally consistent, so this
  remains a test-evidence gap rather than a finding.
- Rollback intentionally restores predecessor authentication semantics while
  leaving additive data in place. In particular, the preceding MailLog
  description again says `user` is non-null even though account-neutral
  recovery mail rows can remain. The inspected generated Go representation is
  already nullable and tolerates those rows, but other schema-derived consumers
  were not dynamically exercised against that rollback state.
- I ran only the isolated ordinary-WebAuthn example described above. I did not
  run a long integration suite, deployment, migration lifecycle, or a live
  cleanup-versus-worker race. Generated cache/tool directories documented in
  the packet were excluded from review, and no project repository was modified
  by this lane.
