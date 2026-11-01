# HaveAPI documentation Switch user and 0.32.1

Design owner: architect0. Scope and public interface accepted by the lead on
2026-11-01. Implementation can proceed against this brief. The lead owns
tracking, integration and publication; implementers own application changes.

## Scope and evidence

Provide an optional provider-neutral extension for additional revoke POST
parameters used only by documentation Switch user. Preserve ordinary Sign out
and the existing validation, cookie, redirect and failure behavior. Release a
compatible supported patch with the one applicable master fix.

Read-only live `git ls-remote origin` on 2026-11-01 confirmed:

| Reference | Commit / finding |
| --- | --- |
| `master` | `209a7ac0c2fe6cd1b78735f50b5e60d979309543`, VERSION `0.32.0` |
| newest release branch `haveapi-0.32` | `0e7166a0f8f15827bfac051666a53bf449e999ec`, VERSION `0.32.0` |
| annotated `v0.32.0` | tag object `e78e4b398819a82961cabb7c7ceea59c773c6a64`, peeled commit equals stable |
| `v0.32.1` | absent; suitable next patch subject to fresh release preflight |

`origin/haveapi-0.32..origin/master` contains only `209a7ac0`, which fixes
performance-CI false failures when a newly pushed branch already belongs to
captured default history. Include it with `git cherry-pick -x`: it changes only
`utils/performance_ci.rb`, its event-baseline specs and `doc/performance.md`.
It preserves performance guards outside that no-source-change case and has no
runtime, API or persisted-state effect. There is no additional backlog at these
refs. The local bare `refs/heads/master` was stale; use verified remote refs.

The existing `DocumentationOAuth#logout` revokes only the documentation access
token. The session plan records the consumer's diagnosis: with another active
authorization, vpsAdmin can retain shared SSO and silently select the old user
again. Its existing provider accepts `close_sso=1` on revoke. HaveAPI must carry
configured parameters without implementing that provider's SSO semantics.

## Public interface and invariants

The exact consumer configuration is:

```ruby
api.documentation_oauth(
  # Existing client, callback, session and scope options remain required.
  switch_user: true,
  switch_user_revoke_params: { 'close_sso' => '1' }
)
```

- Add `switch_user_revoke_params` to `DocumentationOAuth::FIELDS`. The existing
  `Server#documentation_oauth(**options)` forwards it without an API redesign.
- Accept a static `Hash<String, String>`, default `{}`. Reject other containers,
  symbol/non-string keys, non-string or nested values, and the reserved keys
  `client_id`, `client_secret`, `token`, `token_type_hint` with
  `DocumentationOAuth::Invalid`. Do not coerce values, add callbacks or invent
  count/name/value length limits. Errors must not echo configured values.
- Copy and freeze the hash and its string entries at initialization. Later
  caller mutation cannot change the configuration. Configuration is accepted
  with `switch_user: false` but remains inert and never enables switching.
- On a validated switch, append only this configured hash to the revoke form.
  Assemble the four required fields authoritatively from configured credentials,
  the documentation cookie token and literal `access_token`. Browser parameters
  never supply additional revoke fields or override these fields.
- Preserve ordering: configured HTTPS origin, accepted switch capability and
  scalar request field, exact `Origin`, valid session and session-bound CSRF all
  succeed before revocation or its new parameters have any external effect.
  Existing malformed/duplicate/array/multipart switch refusal stays intact.
- Ordinary Sign out sends exactly its previous revoke fields, even when extras
  are configured. Authorize and token requests never receive the new extras.
- Preserve cookie clearing before revoke; revoke failure returns the existing
  truthful 502 with no fresh-login redirect. Success returns the existing fixed
  303 login route; the next login creates fresh state and S256 PKCE. No new
  `prompt`, `select_account`, return-URL or cookie-renewal behavior is introduced.
- HaveAPI neither interprets `close_sso` nor promises whole-account logout.
  Provider-specific configured behavior can close SSO while unrelated access
  tokens remain valid. The operator still verifies the provider permits account
  selection before enabling `switch_user`.

## Implementation packages and dependencies

| Owner | Files / responsibility | Dependency and acceptance |
| --- | --- | --- |
| implementer0 | `servers/ruby/lib/haveapi/documentation_oauth.rb`; `servers/ruby/spec/documentation/oauth_spec.rb`; `doc/documentation-oauth.md` | Master-based source/spec/docs commit after worktree hook preparation. Implement and check the exact interface and acceptance cases below. No server DSL, templates, translations or browser JS changes needed. |
| implementer1 | Stable worktree: `-x` backports of `209a7ac0` and implementer0's final source fix; `VERSION`, component version/dependency files changed by `make version`, `CHANGELOG.md` | Source backport waits for implementer0's committed fix. Separate source/backport commits from stable `0.32.1` metadata. Bring applicable release notes to master while keeping master version/dependency metadata at `0.32.0`. Coordinate all Git writes with lead. |
| lead | Tracking, review packet, approved integration, annotated tag, protected publication and downstream report | Inspect final committed ranges and quick checks, obtain mandatory independent review, then required release checks/workflow. Verify published artifacts rather than reporting a tag alone as usable. |

The documentation guide is the authoritative extension contract. Replace its
blanket requirement for vpsAdmin `allow_single_sign_on=false` and blanket claim
that switching never affects SSO with the configurable provider behavior. Keep
ordinary logout's semantics clear, document the new option/default/reserved
fields, and explain removal of the option before rollback to older HaveAPI.
Site-specific setup and consumer wiring stay with the originating session.
Apply the required user-facing writing skill before committing project prose.

## Acceptance and verification

Use the repository Nix shells, declared Overcommit hooks and development/release
procedures. Run `make doc` before server specs. Keep local verification focused;
there is no separate production, browser-fleet or downstream runtime campaign.

| Check | Required evidence |
| --- | --- |
| Configuration regression | Default empty configuration preserves behavior; reject wrong hash/key/value types and each reserved key; caller mutation after initialization cannot alter sent fields. |
| Revoke payload regression | Valid switch sends exact configured extras plus the four correct required fields. Ordinary logout sends no extras. Browser-supplied fields cannot replace configured/required fields. Authorize/token traffic excludes extras. |
| Shared-SSO regression | A small in-spec fake provider holds documentation and second authorization sharing SSO. Without configured switch extras, docs revoke leaves SSO reusable while the second authorization exists. With configured switch extras, docs revoke closes SSO and the second authorization remains valid; fresh authorization therefore cannot silently reuse SSO. This models the provider boundary, not vpsAdmin implementation. |
| Existing validation/failure cases | Run `bundle exec rspec spec/documentation/oauth_spec.rb` from `servers/ruby`; exercise configured extras with invalid Origin/CSRF/disabled or malformed switch so no revoke occurs. Preserve 502, cookie clearing, fixed redirect and fresh state/PKCE cases. |
| CI backport | Run `bundle exec rspec spec/performance/event_baseline_spec.rb` from `servers/ruby`; confirm only the known CI-fix diff is backported. No extra performance campaign is needed for this inventory check. |
| Quick source/release checks | Root-bundle RuboCop on changed Ruby files; declared hooks; inspect doc examples/contract; top-level shell `make release-deps` before `make version VERSION=0.32.1`, then `make release-check` and metadata/diff inspection. No tracked library locks. |
| Final review and required release run | Give independent reviewer complete master/stable base-to-head series, final diff, `-x` lineage, metadata split and explicit no-migrations conclusion. After committed quick-green final review, the protected release workflow runs its existing component tests/build/package verification. Use the monitoring skill for long or uncertain checks; do not duplicate its broad release matrix locally without a failure-driven reason. |
| Publication | Validate exact release tag/source, original artifact manifest/checksums, five gems, npm, both Python artifacts, PHP mirror tag/source, Packagist availability and completed GitHub Release. Report actual versions/hashes and verification limits to downstream. |

## Release, compatibility and recovery

`doc/agent-instructions/releases.md` is identical on the two inspected lines.
Only the newest release branch is supported. Patch source fixes use
`cherry-pick -x`; patch metadata stays on `haveapi-0.32`; master retains `0.32.0`.
All maintained components publish together through the existing tag-triggered
protected `release` workflow. The lead resolves authorization from the user's
release request and observes protected-environment approval; preparing this
brief grants no publication or integration authority itself.

There are **no database migrations**, schema changes, seeds, persisted-state
changes, API-client protocol changes or generated system configuration changes.
Existing config on new HaveAPI behaves identically. Old HaveAPI rejects the new
keyword, so deploy the upgraded library before enabling consumer configuration,
and remove that keyword before reverting the library. Mixed workers can retain
the existing encrypted cookie format and shared session secret; an old worker
does not acquire the new provider behavior. Consumer rollout owns that ordering.

No production deployment is part of this session. No cookie sliding-expiry
redesign, refresh-token support or unrelated runtime work is included. The
documentation cookie retains its existing initial fixed expiry behavior.

Preserve published history, existing tags and recovery refs. A partial registry
publication is non-atomic: preserve the exact tag, original Actions artifacts,
manifest and draft Release; verify successful uploads against original hashes
before recovery through the original workflow. Never retag, replace accepted
artifacts, blindly reupload or overwrite a published version. A content defect
needs a new patch. Consumer rollback selects the prior package and removes the
new option; it requires no state migration. Keep this session open.
