# M6 documentation identity and OAuth token seam: source ready

Base head `266dcb1852c8bac8735af684ce48380d2851a658` above35c. Owner4's
nine-path hashes are in `milestone6-oauth-source-ready-hashes.json`; the patch
includes tracked deltas and explicit new-file additions. All are unstaged.
Other owners' concurrent paths were preserved; no Git mutation/hooks ran.

Agreed before auth writes: owner0's C core owns the public
`documentation_authenticated?(version)` orchestration and private
`documentation_authenticate(version)` defaultnil, plus nil controls. Core resets
`@current_user`, calls the private hook, then post-authenticated/locale once.
Owner4's optional D helper overrides only the private identity hook and controls.
It never calls ordinary API authentication, injects/restores Authorization or
mutates request headers/params. GET and HEAD on the configured origin validate
only the purpose-bound, unexpired docs cookie and its requested-version token.
Missing/invalid/revoked/unsupported sessions remain anonymous with no fallback.

`Chain#authenticate_oauth2_token(version,request,token)` selects only requested
version providers named oauth2 with the explicit public token-validator method,
in registration order with existing deny semantics. Unsupported custom providers
fail closed without calling their ordinary authenticator. Standard OAuth2
`authenticate_access_token(request,token)` factors existing config lookup and
AuthenticationError-to-nil; ordinary extraction/conflict/API behavior remains.
Logout and Switch user now ignore API credentials and still require the existing
cookie/origin/CSRF/strict switch capability. Revoke/clear/303 fresh state+PKCE,
502 failure, cancellation and R1 pending-only callback failure behavior remain.
No cookie/config/lifetime/provider wire or refresh redesign.

Reusable test-only helper:
`servers/ruby/test_support/documentation_oauth_fixture.rb` has no RSpec/spec_helper
dependency. `DocumentationOAuthFixture.configure(server,users:{version=>{token=>user}},
origin:'https://example.org',mount_path:'/')` registers an actual OAuth provider
and optional docs client beforemount. `fixture.header_for(server,version:,token:)`
aftermount uses that client's actual encrypted cookie writer. Lifetime is fixed
once perfixture at3600s; CSRF is deterministic per fixture token and stable across
repeated source samples. Header issuance belongs outside measurement.
`fixture.lookups` records actual [version,token] provider callbacks; `fixture.origin`
provides matching synthetic HTTPS URLs. Rack::MockRequest also needs HTTP_HOST.
No real TLS/server is started. Every network page still decrypts/validates and
looks up its token; the helper proof verifies three real reads/lookups, admin/member
filtering and identical repeated HTML. Owners0/1 consume this exact helper.

Final known-quick batch (prepared Nix/root tools, existing server bundle):

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --no-write-lock-file --command bash -euc '
  cd servers/ruby
  export BUNDLE_GEMFILE="$PWD/Gemfile"
  bundle exec rspec spec/documentation/oauth_spec.rb \
    spec/documentation/oauth_fixture_spec.rb \
    spec/documentation/oauth_transport_spec.rb \
    spec/authentication/oauth2_chain_spec.rb \
    spec/authentication/oauth2_token_validation_spec.rb \
    spec/authentication/oauth2_spec.rb spec/authentication/token_spec.rb \
    spec/authentication/token_version_routes_spec.rb \
    spec/authentication/basic_spec.rb --seed 16029 --format progress
'
```

**120 examples,0 failures**,6.34s plus1.38s
load. **8 owned Ruby files linted, no offenses**; diff whitespace check passes.
`make doc` ran before the focused batch; final main-only guide prose was read
for factual agreement without repeating tests or rewriting it. Logs:
`milestone6-oauth-source-ready.log/.exit`. Initial raw Rack helper proof lacked
HTTP_HOST; it was a test environment correction, with prior log retained. Earlier
format-only lint corrections are also retained. No dependency install/change.

Coverage includes valid cookieB crossed with valid Basic/Bearer/custom/queryA and
malformed/conflicting credentials; absent/tampered/expired/revoked cookie does
not fall back, challenge or use A. Provider sees original credentials unchanged.
Tests cover HEAD, perversion root map/posthooks/oncedescribe, explicit API and
OPTIONS identity/conflict behavior, OAuth chain order/deny/custom-capability,
keyed200/304 token revalidation, permissions409, Set-Cookie no-store, Basic-present
ordinary logout/switch, bad-origin/CSRF and preserved R1 regressions.
Owner0 owns only the two legacy Basic route expectation changes; its five
ordinary Basic API examples are unchanged and included in this120-case run.

Read final main guide in full: OAuth-only identity, original-request directtoken
callback/custom-provider requirement, API separation, compatibility303 routes,
operator assertion/switch failure and rollback facts agree. No added live-client,
provider-selection, cookie-schema or release claim. New C/D history must retain
core anonymous default independent of optional module; D owns the hook override,
optional config/control wiring and direct token seams together. The new support
and optional OAuth specs belong with D, never borrowed into an earlier C smoke.

No active command/check/watcher or uncertain effect remains. Owner4 is source/Git
quiet awaiting collective commit and affected review. Existing HTTP preview,
local TLS/private fixture, peer environment, releases/merges and session lifecycle
were not touched. Real provider, browser and performance acceptance remain pending.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
