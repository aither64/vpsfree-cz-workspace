# R1 callback-session preservation: source ready

Base HaveAPI head: `9f68dad5436799d82e9c9e1c69e73866a279e9a6`.
The lead resumed this bounded fix after implementer3 released the previous
browser/source hold. Existing HTTP preview remains untouched. No Git mutation,
hooks, dependency installation, provider network call, local TLS/private fixture,
peer access or session lifecycle operation ran.

Only two assigned files are changed and unstaged. Production change removes the
callback rescue's unconditional authenticated-session cookie deletion. A rejected
sign-in attempt consumes its pending cookie as before and returns the same 400
failure page; it no longer performs an unprotected logout. Success, token request
validation/counts, expiry and CSRF-protected logout/revocation paths are unchanged.
Existing owning guide remains accurate; no product documentation edit was needed.
The original review and R1 proof remain unchanged.

Regression coverage uses the existing Rack fake provider. It checks exact cookie
preservation, cleared pending value, visible admin identity and ordinary provider/
post-authentication identity after unsolicited, missing, mismatched, malformed,
cancelled, duplicate, expired and replayed callback state, missing code, token
exchange failure and invalid token response. Absent/tampered sessions do not gain
identity; successful same-origin CSRF logout still removes identity. No new state
store, provider protocol or refresh behavior was added.

With the regressions added before the production fix: **37 examples, 11 failures**,
all existing-session preservation failures at the old deletion. See
`R1-regression-before.log` and `.exit`. The first post-fix run exposed two test
assumptions: Rack's jar retains an empty expired pending entry, and anonymous
reference pages intentionally show declared schema. Assertions now test the
cleared pending value and real identity/CSRF/provider lookup rather than cookie
key absence or a resource 404. A subsequent lint finding about memoized-helper
count was resolved with a simple test helper. Those failed logs remain retained.

Final quick command in the prepared repository Nix shell (no installs):

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

`make doc` and bundle check ran before the initial regression execution. Final
result: **41 examples, 0 failures**, 2.95 seconds plus 1.02 seconds load;
**2 files linted, no offenses**, exit0. `git diff --check` passes. Only the module
and OAuth spec appear dirty; no command/watcher remains running. Evidence:
`R1-focused-ready.log`, `.exit`, and `R1-source-ready.patch`.
Patch SHA256: `a3380654cf2d2b69fce7a87555f2a2a9f71db275a0b215b5360a02b634292114`.
Await collective commit slot and affected independent review; this is not live
OAuth, browser acceptance, deployment or final R1 review acceptance.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
