# Milestone 5 documentation account switch: source ready

Base: HaveAPI `898df315add307ce5d3013ab62ae12834b64a13f`, including the
accepted R1 callback fix. Owned changes are unstaged in
`servers/ruby/lib/haveapi/documentation_oauth.rb`,
`servers/ruby/spec/documentation/oauth_spec.rb` and
`doc/documentation-oauth.md`. Owner0's server/helpers/templates are independent;
the interface was agreed before these writes and its source-stable notification
preceded the combined focused run. No Git/hooks, live preview/provider, local TLS,
private fixture, peer record/cluster or dependency setup was performed.

The backend validates strict Boolean `switch_user` (default false). Public
`signed_in` controls reflect only ordinary authentication that successfully used
the documentation cookie on this request; the request-local CSRF marker resets
before any explicit-credential early return. `switch_user:true` is exposed only
for that mode plus the configured capability. Owner0 consumes the unchanged
`signed_in` flag in its memoized presentation-only account context.

Switch POST validation precedes cookie reading/clearing and token revocation.
One decoded scalar `switch_user=1` is required, with capability on, no explicit
credentials, same-origin and the existing session CSRF. Duplicate/array/invalid
values and multipart switches fail without effects. The existing revoke/local
clear sequence redirects303 to the fixed default-version login only on success.
Following it creates new state/PKCE, preserving configured scopes. Arbitrary
request return/scopes do not change the login destination. Cancellation leaves
the old account signed out; revoke failure remains502/local sign-out and never
continues to login. Ordinary logout, cookie schema, provider protocols and
API/OPTIONS/mutation authentication remain unchanged; R1 deletion stays intact.

Compatibility: declared Sinatra `~>4.0` permits Rack3.0.0, whose official
`https://raw.githubusercontent.com/rack/rack/3.0.0/lib/rack/request.rb` lacks
`form_pairs`. The implementation therefore uses ordinary `handler.params` plus
Rack's existing cached `rack.request.form_vars` and decoded query pairs solely
to retain duplicate detection. That cache exists in both3.0.0 and installed3.2.7.
No method capability probing, body reader/parser, dependency pin or framework.
The generated native form is URL-encoded; multipart switching is refused.

Final known-quick check in the prepared Nix environment:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop --no-write-lock-file --command bash -euc '
  cd servers/ruby
  export BUNDLE_GEMFILE="$PWD/Gemfile"
  bundle exec rspec spec/documentation/oauth_spec.rb \
    spec/documentation/oauth_transport_spec.rb --seed 16028 --format documentation
  bundle exec rubocop lib/haveapi/documentation_oauth.rb \
    spec/documentation/oauth_spec.rb
'
```

Result: **59 examples,0 failures**,
4.46 seconds plus1.16 seconds load; **2 Ruby files, no lint offenses**; exit0.
`make doc` and diff whitespace checks pass. Logs are
`milestone5-switch-ready.log/.exit`; original focused log and lint correction
remain retained. R1's existing41-case coverage is included. New18 cases cover
Boolean defaults/validation, actual-mode controls, fresh authorization and
cancellation, malformed/duplicate/array/disabled/bad-origin/bad-CSRF refusal,
revoke failure, single-version root cookie identity, and real Basic A with
OAuth-cookie B identity/filter/menu priority. Mixed explicit/malformed/conflicting
credentials do not look up B or offer its controls. Direct switch with explicit
Basic also fails before effects. Native root/templates use owner0's current seam.

The guide's additions are technical facts for the lead's final prose pass:
strict false default and SSO-off client precondition; actual-auth presentation
and Basic browser limitation; R1 preservation; switch input/revocation/new-login/
cancellation/failure behavior. No provider account chooser or active client is
claimed. New visible module error strings are
`Invalid documentation OAuth switch-user capability` and
`Invalid documentation switch request`; main may review this wording.

Exact owned patch/hashes: `milestone5-switch-source-ready.patch` and `.json`.
No command remains running after final doc sync. Owner4 is source-quiet and
awaits collective commit/review, not live OAuth acceptance. The existing HTTP
unit remains unchanged. Capability must stay off until operator/partner proof.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
