# OAuth session resume exception: investigation and correction brief

## Scope and evidence boundary

Architect investigation and accepted correction brief for the lead, implementer
and reviewer. The initial request covered root-cause investigation. The user
subsequently accepted the plan and requested the bounded API fix, persisted
regressions and the `vpsadmin` channel update in `vpsfree-cz-configuration`.
Initially, default-branch integration and deployment were outside the accepted
scope. The user later directed: "you can merge it into the default branches
when API specs workflow passes. we will not wait for CI." This authorizes the
lead to fast-forward `vpsadmin:master` and `vpsfree-cz-configuration:master`
after the exact-head API Specs workflow passes, leaving integration CI running
unawaited. The subsequent 60-minute workflow follow-up moves that gate to API
head `f9beb46e5206864bca9d37672e1419cf03661467`; success or a retry on the earlier
`af8a9767` head does not satisfy it. Deployment remains user-owned; no lifecycle
cleanup is authorized.
See [authorization](plan.md#authorization) and [current status](state.md).
The exact-head gate has now passed and both remote master branches were
fast-forwarded to the reviewed heads; see [integration proof](integration-result.json).
Production deployment and acceptance remain pending and user-owned. The
architect's assignment remains limited to this design record,
with no application edits or commits. Implementation and verification results
belong in the lead's session state. The private report
stays outside version control; this brief contains no authentication material
or personal data.

Session identity was verified before using its records: `dev-session current`
from the bound session directory printed `2026-10-03-newadmin-exception`.
Both environment identity markers were absent; the trusted developer binding
supplies the matching absolute workspace and slug. Running `current` from the
shared workspace root initially found no session; rerunning from the intended
session directory resolved that before any session records were accessed.

Initial investigation source inspected through canonical bare repositories,
without other sessions' branches or worktrees:

- API incident revision: `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`.
- Local API `origin/master`: `148ef0eaed0459c825f1ba94b8dad2b9f3311b2f`.
  `ResumeOAuth2`, `SingleSignOn`, the session cleanup task and OAuth2 configuration
  have no differences against the incident revision at this reference.
- Local WebUI `origin/main`: `aa2f60b89df65d2f987be48784ed42bab7010833`.
  This is a source reference, not a verified deployment revision.

Later evidence resolves and checks the configuration's exact WebUI pin
`f123a7fb825437034a764a8a5654032a481a8476`; see the
[pinned WebUI trace](pinned-webui-trace.md). That later source evidence confirms
the refresh/bootstrap path without establishing which revision was running
when the incident occurred. The initial reference-source chronology above is
retained.

Read workspace procedures and the documentation skill, repository instructions,
API documentation index/overview/object lifetimes and testing/development
procedures, plus the WebUI design index, API contracts, OAuth refresh contract,
BFF README and token-renewal documentation. There is no dedicated API OAuth/SSO
lifetime document in the inspected documentation index; model and operation
source establish the relevant contract.

## Root cause

`ResumeOAuth2` assumes that an existing SSO record necessarily has a token. That
assumption contradicts the supported persisted state: closing an SSO deletes
its token but retains its record and its OAuth authorization links. An OAuth
access session can remain valid, or become valid through refresh, after this
closure. Its next `renewable_auto` request attempts `nil.valid_to` while trying
to extend the SSO.

This is an API authentication failure before the requested `/users/current`
action runs. It is not specific to that resource or browser origin. The new
WebUI exercises the OAuth refresh and resume path that exposes it.

All API file/line references below use the exact incident revision above:

| Evidence | Source |
| --- | --- |
| Access token lookup requires an open OAuth session with a valid token; account state, lockout and forced reset are checked. | `api/lib/vpsadmin/api/operations/user_session/resume_oauth2.rb:8-23` |
| Request count, access-token auto-renewal and last-request timestamps update before SSO extension. | Same file, lines 25-32 |
| SSO existence is checked but its token is not, immediately before `.valid_to`. | Same file, lines 34-42; failing expression at line 40 |
| SSO usability already treats a missing token as unusable. Closing deletes the token and writes `token: nil`, without deleting the SSO or nullifying authorization links. | `api/models/single_sign_on.rb:3-8,26-31` |
| A nullable SSO token is part of the schema contract. | `api/db/migrate/20231216155818_add_single_sign_ons.rb:3-5` |
| Cleanup deletes expired access tokens but leaves sessions open when their OAuth authorization is refreshable. | `api/lib/vpsadmin/api/tasks/user_session.rb:8-32` |
| The same task closes unusable SSO records regardless of whether a refreshable OAuth session still exists. | Same file, lines 46-51 |
| Refresh validates the refresh token and account/session restrictions, replaces the access token, and rotates the refresh token. It neither requires nor renews the SSO token. | `api/lib/vpsadmin/api/authentication/oauth2_config.rb:257-294` |
| New SSO validity is based on authorization-code expiry plus the client's access-token duration, not its refresh-token duration. | Same file, lines 938-963 |
| OAuth access authentication calls this resume operation. | Same file, lines 412-414 |

The valid access-token association is loaded by `renew_token!` before the failing
comparison (`api/models/user_session.rb:32-34`). With the reported failure at
line 40, the unguarded SSO-token association is the direct source explanation.
The lead independently confirmed this trace against the deployed source.

## Likely trigger and alternative paths

The following sequential scenario follows from the source; it does not require
a race or corrupted database:

1. An OAuth client uses `renewable_auto`, has SSO enabled, and issues refresh
   tokens which remain valid beyond an idle period.
2. The browser stops making API requests long enough for access and SSO tokens
   to expire while the refresh token remains valid.
3. Cleanup removes the expired access token while preserving the open session,
   then closes the SSO by removing its token. The authorization retains its SSO
   reference. The NixOS module enables this task on a five-minute timer
   (`nixos/modules/vpsadmin/api/rake-tasks.nix:137-145`); actual production timer
   execution at the relevant time has not been established.
4. The client refreshes successfully, obtaining a new access token for the
   existing session. The SSO remains tokenless.
5. A request using the fresh token reaches SSO extension and raises the reported
   `NoMethodError`.

Cleanup need not be scheduled: closing any user session also sweeps expired
SSOs (`api/lib/vpsadmin/api/operations/user_session/close.rb:19-21`). Explicit
SSO closure on OAuth revocation is another route: `close_sso` can close a shared
SSO while another authorization remains active
(`authentication/oauth2_config.rb:300,347-351` and
`api/models/single_sign_on.rb:13-14`). The latter can leave another access token
usable immediately, without refresh being necessary.

Neither the production database's exact state nor its cleanup/revocation
timeline was queried. Therefore, idle expiry followed by refresh is the leading
source-supported trigger, not a proven history of this particular request.
The user additionally reports that multiple users are affected and suspects
ordinary inactivity is sufficient. This corroborates the ordinary idle path
above rather than requiring a rare concurrent event, but no per-request cleanup
logs were inspected to establish those individual timelines.
The request proves entry to the `renewable_auto` branch but does not establish
all current client settings or the deployment's token durations. No duration
values or actor are inferred from the report.

Repeated failing requests can still extend the API access token and update
timestamps because those writes precede the exception; this operation has no
enclosing transaction of its own. A page reload or another token refresh does
not by itself repair the retained tokenless SSO association.

## Why the new WebUI exposes it

At the WebUI source reference above:

- `bff/server.js:154-183` refreshes a stored OAuth access token near or after
  its recorded expiry using the stored refresh token. `/session.json` invokes
  this at lines 256-273 and returns the resulting access token.
- `src/app/auth.tsx:124-130` loads the current user when authentication is
  enabled. `src/lib/api/users.ts:19-24` makes `GET /users/current`.
- The BFF README specifies that the browser calls the API directly with the
  OAuth token; the BFF handles exchange and refresh rather than proxying these
  resource requests. This explains the report's WebUI Origin.
- `src/components/layout/SessionTokenKeepalive.tsx:55-60` enables its periodic
  keepalive only for HaveAPI `token` authentication, not OAuth2. Do not attribute
  this request to that component merely because it uses the same endpoint.

The legacy token authentication operation, `ResumeToken`, has no SSO-extension
block (`api/lib/vpsadmin/api/operations/user_session/resume_token.rb:25-33`).
The defective OAuth branch can therefore remain hidden in ordinary token-auth
usage. Any OAuth client producing the supported state can expose the bug.
These initial WebUI references corroborated the route without establishing the
revision deployed for the report. The later [pinned WebUI trace](pinned-webui-trace.md)
confirms the route at the configuration's actual consumer pin; the incident's
running revision remains unproven.

## Accepted correction and invariants

In `ResumeOAuth2`, obtain the associated SSO token once and extend
it only when it exists and expires before the renewed access token. An absent
SSO token should skip this optional extension and allow the otherwise-valid
OAuth session to resume normally.

The correction must preserve these invariants:

- API access authority comes from the existing access-session/account checks.
  A closed SSO is not itself a revocation of every linked OAuth authorization.
- Keep SSO closure effective. Do not create a replacement SSO token, revive a
  revoked SSO, delete historical SSO records, detach authorizations or require
  reauthentication solely to avoid this exception.
- Existing SSO tokens may be extended as before; later expirations must not be
  shortened. Missing authorization and missing SSO remain valid no-op cases.
- Invalid/expired access tokens, closed sessions, locked accounts and forced
  password reset retain their current denial semantics.
- Do not replace the presence check with `sso.usable?` without an explicit
  policy decision. Existing code can extend an expired but still-present SSO
  token; refusing that changes behavior beyond the reported nil dereference.

A local variable plus token-presence guard handles a token removed before it
is loaded. It is not a general concurrency redesign: access-token refresh,
SSO cleanup and renewal remain subject to their existing transaction/locking
boundaries. A concurrent deletion after the token has been loaded must not lead
to creating a new token. Broader serialization or a change to SSO expiry policy
would need a separate design decision through the lead.

Refreshing OAuth tokens without extending SSO is a proven part of the trigger
chain, but changing refresh to renew/recreate SSO is not the minimal correction.
The existing independent SSO and refresh lifetimes can remain supported.

## Files, interfaces and implementation boundaries

The approved API application change is bounded to:

- `api/lib/vpsadmin/api/operations/user_session/resume_oauth2.rb`.
- Regression examples in
  `api/spec/models/operations/user_session/resume_oauth2_spec.rb`, plus a
  persisted cleanup/refresh/resume example in the existing auth/session specs
  if needed to cover the lifecycle across components.
- A short explanation of the tokenless-SSO invariant near the extension code
  or in the owning API documentation. This session brief is investigation
  evidence, not a substitute for lasting feature documentation after a fix.

No WebUI change, API resource/response contract, client regeneration, CLI or
Terraform adjustment, schema migration, seed change, daemon protocol change,
Nix option or vpsAdminOS change is required for the guard.

Implementers use dedicated same-session feature worktrees under
`worktrees/2026-10-03-newadmin-exception/vpsadmin` and
`worktrees/2026-10-03-newadmin-exception/vpsfree-cz-configuration`, following
the registered session branches. The original instruction to keep both changes
off `master` is superseded by the conditional integration authorization above.
The lead owns that short coordination step after exact-head API Specs success;
retain both feature branches after integration.

## Requested workflow timeout follow-up

The user superseded the earlier retry with: "well don't just rerun it... let's
extend the timeout then... to 60 minutes." Implementer-authored commit
`f9beb46e5206864bca9d37672e1419cf03661467` follows the unchanged authentication
fix and persisted specs at `af8a97670293f4aa9a57e3196ac263c9c9530644`.
Its only changes are the full/core topic job timeouts in
`.github/workflows/api-specs.yml`, from 45 to 60 minutes. The 10-minute coverage
job, topic selection and action references are preserved. This does not change
the source invariants, expiry policy or compatibility conclusions in this brief.

Structural checks and all mandatory hooks passed. Independent affected-lane
and complete final-series review passed without findings.
See [current state](state.md), [timeout decision](api-specs-timeout.md) and
[verification evidence](verification.md) for the evidence. API Specs run
`37151153953` succeeded at exact head
`f9beb46e5206864bca9d37672e1419cf03661467`: all 27 jobs passed, including topic
coverage. Full-platform RSpec took 32m56s; the full/core limits remain 60 minutes
as requested. [Completion result](api-specs-60m-completion-result.json).
The refreshed configuration review/build also passed, and both repositories
were integrated after the Specs gate. Integration/default-branch CI was not
awaited. No production activation is implied by these results.

## Accepted configuration channel update

Configuration source `657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`
(`origin/master` when inspected) maps channel `vpsadmin`, role `vpsadmin`, to
flake input `vpsadminServices` in `flake.nix:106-108`. Its input declaration is
at lines 69-73. This is distinct from the `vpsadminProduction` and
`vpsadminStaging` inputs owned by the node channels.

After the API feature revision has passed the required verification/review and
is published, pin that exact reviewed SHA from the configuration feature
worktree's `nix develop` environment:

```sh
confctl inputs channel set --commit vpsadmin vpsadmin <reviewed-published-api-sha>
```

Use the generated channel-owned lock update and preserve confctl's generated
commit message and useful changelog. Do not edit `flake.lock` manually. Verify
that the resulting `vpsadminServices` revision is exactly the reviewed and
published API feature SHA, and account for any necessary transitive lock
changes. No unrelated channel/input or configuration changes belong in this
update. Review the complete API revision delta from the previous configuration
pin as well as the bounded fix, since an updated base can include other changes.
Record the previous and new pins and the configuration feature head in session
state for the user's deployment handoff. The command above records the selected
workflow. Its earlier completed pin update and rebased configuration head are
historical checkpoints documented in [verification evidence](verification.md)
and summarized below. Final configuration
`074b62fe4ca99bcb6e0b2cd186e43f039c666b36` contains one consolidated generated
update from the original
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff` pin to the reviewed, published
`f9beb46e5206864bca9d37672e1419cf03661467` head. It passed final validation and
the independent general/risk checkpoint without findings, preserving prior
unaffected review conclusions. Both API1/API2 builds passed at generation
`2026-10-03--22-46-01` with source `f9beb46e`; see the
[build result](configuration-updated-build-result.json) and
[actual outputs](configuration-updated-outputs.json).
The feature was published using the exact historical `dd5e0b5d` lease and then
fast-forwarded into remote `master` after the API Specs gate. Follow
[state](state.md), [integration proof](integration-result.json) and
[rollout](rollout.md) for exact delivery and user-owned deployment details.

## Compatibility, deployment and recovery implications

The correction accepts a state already produced by deployed code. Existing
database rows and token formats remain readable in both directions; no data
conversion or cleanup is required. Rolling API deployment is possible, but
old API workers can continue raising this exception until replaced. There is
no coordinated WebUI, node or fleet upgrade requirement. Existing clients
receive a normal successful response where a valid session currently fails.

Software rollback has no schema prerequisite and can load all resulting state;
it restores the nil-dereference failure for affected sessions. Recreating
deleted SSO tokens is not a recovery action. A fresh interactive OAuth login
can obtain a new authorization/SSO when applicable, but that is a temporary
client recovery path rather than correction of the underlying API defect.
No recovery, production deployment or dry activation was performed in this
session.
The accepted configuration update prepares the exact source selection for the
user's later deployment and does not activate services. Default-branch
integration completed under the separate conditional user authorization above.
Retain the previous configuration pin for recovery;
rollback of the guard itself requires no data conversion, while any other
changes in the full old-to-new API pin delta need their own compatibility check.

## Acceptance and verification brief

Source inspection completed: the exact failing code, closure semantics,
nullable schema, cleanup/refresh sequence, WebUI bootstrap route, current
default-ref equivalence and existing tests were checked. No runtime
reproduction or tests were run during that initial investigation. Subsequent
implementation and verification were performed by the assigned team. The
following historical checkpoint comes from the lead's [state](state.md),
[verification evidence](verification.md) and [independent review](review.md):

- Historical reviewed and published API feature head:
  `af8a97670293f4aa9a57e3196ac263c9c9530644`. Three persisted regressions failed
  on the original source; the corrected focused suites passed 72 examples with
  zero failures. Independent review passed all four lanes without findings.
- Historical reviewed and published configuration head:
  `dd5e0b5d1d8a2487d608909676c828934966abdc`, based on
  `7e32833aca1cb65902b50f61eb76dd1022691591`. The rebase after a monitoring-only
  master advance preserved the feature patch and message. Final validation and
  the independent review checkpoint passed, preserving prior review conclusions.
  Its earlier initial pin commit was
  `e96fbde0c622e3807593e3e59daae0f668045540`; both are superseded by final
  configuration `074b62fe`.
- Both API1/API2 builds at that historical configuration head passed,
  generation `2026-10-03--21-30-00`. These results do not certify the replacement
  pin to the timeout-follow-up head; the replacement has its own successful
  review/build evidence at generation `2026-10-03--22-46-01` above.

Final delivery is recorded in [integration-result.json](integration-result.json):
after exact `f9beb46e` API Specs success, fresh fetches confirmed API remote
master/feature equality at `f9beb46e5206864bca9d37672e1419cf03661467` and
configuration remote master/feature equality at
`074b62fe4ca99bcb6e0b2cd186e43f039c666b36`, with fast-forward ancestry from both
prior master heads. Integration/default-branch CI was not awaited. See
[verification](verification.md) for completed checks and
[manual handoff](rollout.md) for the pending user-owned rollout and production
acceptance. These source, test and build results do not establish a deployed fix.

At the originally investigated source, resume coverage tested successful SSO
extension but not an SSO row whose token was deleted. Cleanup coverage separately
checked tokenless SSO closure and preservation of refreshable sessions, without
completing the cleanup-to-refresh-to-resume sequence. The recorded persisted
regressions now cover that sequence.

Acceptance cases for the approved implementation are:

1. A valid renewable OAuth session linked to an SSO explicitly closed with
   `SingleSignOn#close` resumes, sets current user/session and renews its access
   token. Its SSO remains tokenless and no new SSO token appears.
2. The same holds after real expiry cleanup and OAuth refresh. Assert the open
   session and retained authorization/SSO relationship in the database, not
   only a stubbed nil association.
3. An existing earlier SSO expiry extends to match access expiry; a later one
   is preserved. Missing authorization and missing SSO still succeed.
4. Nonrenewable OAuth sessions retain their behavior. Expired/invalid access
   tokens and account/session denial states remain rejected.
5. Closing a shared SSO while another authorization remains valid does not
   crash the other authorization's subsequent resume or recreate the SSO.

Quick checks, in the same-session API worktree and its `nix develop .#api`
environment: run the touched-file RuboCop checks and the existing resume,
cleanup and OAuth2-config RSpec files using the repository's isolated test DB
support. Keep every API spec covered exactly once in CI if any new spec file
is added. Do not capture task output containing real token values; the current
cleanup task prints token strings at `tasks/user_session.rb:12`, so reproductions
must use synthetic credentials and retain only sanitized results.

For the configuration update, check the generated lock diff and exact API SHA,
preserve repository hooks, and verify channel resolution/evaluation using the
repository's declared tools. Include the configuration diff and old-to-new pin
inventory in the required review. Any long build or uncertain-duration check
uses the required watcher; deployment, including dry activation, remains with
the user.

Longer acceptance, after the required independent change review: use an
isolated API and synthetic OAuth client to exercise login, idle expiry,
cleanup, refresh, then `GET /v7.0/users/current`. Expect success and a still-null
SSO token with the correction; expect the reported exception before it. A real
WebUI/BFF pass can verify the same bootstrap path if needed. Delegate any long
or uncertain-duration verification to the required watcher. This retains the
original longer-check plan: the persisted cleanup/refresh/access-authentication
sequence has since passed locally, while full HTTP/browser acceptance and
production activation have not been performed. See the linked verification
record for the distinction; integration CI is not an additional waiting gate.

## Handoff

The lead owns integration of this finding into session state and the portal
manifest; this assignment restricts the architect to `design.md`. The precise
production closure trigger remains the only material incident uncertainty.
The session remains active and open; feature and integration worktrees and refs
are retained. No session cleanup occurred. Deployment, any operational rollback,
and production acceptance remain with the user under [rollout](rollout.md).

Stable session URL:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-newadmin-exception/>
