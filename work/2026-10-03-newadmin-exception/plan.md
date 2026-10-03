# Fix OAuth resume after SSO expiration

## Goal and scope

Implement the accepted plan: fix the API exception triggered by inactivity,
add persisted regression coverage, and pin the reviewed API feature revision in
the `vpsadmin` channel of `vpsfree-cz-configuration`. The user will deploy it.
Keep the raw email outside Git and record only sanitized evidence. Production
operation and session closure are not authorized. User subsequently authorized
both default-branch integrations after the API Specs workflow passes and
explicitly excluded waiting for integration CI.

## Affected repositories

- `vpsadmin`: deployed API revision
  `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`, OAuth authentication and SSO
  session/token lifetime management.
- `vpsfree-cz-configuration`: `vpsadmin` channel, role `vpsadmin`, maps to
  `vpsadminServices`; originally pinned the incident API revision above.
- `vpsadmin-webui` and `haveapi`: investigation references only; no edits.

## Approach and responsibilities

1. Root-cause investigation and architect brief are complete. Architect updates
   the brief for the accepted implementation and channel handoff.
2. Retained `implementer0` edits the API in its dedicated feature worktree:
   capture the optional SSO token once, guard its presence before extending it,
   and explain the deliberately retained tokenless SSO state in a code comment.
3. Add regressions to the existing resume and OAuth2 configuration specs:
   closed SSO plus valid access; actual expiry cleanup, refresh and access
   authentication; preserved live SSO renewal and missing-association behavior.
   Show the new regressions fail on the original implementation.
4. Run focused RuboCop and resume, cleanup and OAuth2 configuration suites in
   the API Nix environment. Commit with active hooks, inventory the entire
   branch, and assign mandatory independent review to retained `reviewer0`.
5. Publish the reviewed feature revision. Implementer pins its exact SHA using
   `confctl inputs channel set --commit vpsadmin vpsadmin <reviewed-api-sha>`
   in the dedicated configuration feature worktree. Keep generated changelog.
6. Review the final configuration diff and complete history; verify only the
   intended channel/input and required transitive locks changed. Build API1 and
   API2 without activation. Push the configuration feature branch and hand off
   exact commits, verification, deploy targets and rollback pin to the user.
7. Lead maintains records and integrates reports. Fresh Luna/low watchers own
   every long or uncertain check/build/CI operation. Wait only for exact-head
   API Specs; then fast-forward API and configuration into their remote default
   `master` branches. Leave integration CI running without waiting for it.

## Compatibility and deployment

No schema migrations, state conversion, token-format or public-interface
changes. A closed SSO token stays absent; independently valid OAuth sessions
resume normally. Preserve existing expiry policy for present SSO tokens rather
than introducing `sso.usable?` or changing refresh behavior. Mixed old/new API
workers are compatible, though old workers can still raise until replaced.
Rollback reads unchanged state and restores the original defect. No WebUI,
daemon or fleet upgrade is needed. Record any dependency updates inherited
between the old channel pin and freshly fetched API master. Never infer a
specific production cleanup event from the report alone.

## Documentation and verification

Readers are the user, implementer and reviewer. The concise invariant comment
belongs with API source; exact revisions, review packets, build evidence and
manual deployment/rollback steps belong in this session. Use actual persisted
fixtures and synthetic credentials with deterministic expiry timestamps, and
sanitize cleanup output. Both branches need complete history/diff inventories
and explicit no-migration review conclusions before readiness. Builds cover
`cz.vpsfree/vpsadmin/int.api1` and `int.api2` without activation.

## Authorization

User accepted the presented plan with "Implement the plan." User explicitly
requested the vpsadmin channel update and said "I will deploy it myself."
Later user direction in this conversation: "you can merge it into the default
branches when API specs workflow passes. we will not wait for CI."
This covers `vpsfreecz/vpsadmin:master` and
`vpsfreecz/vpsfree-cz-configuration:master`, conditional on API Specs success.
Retain both feature branches after integration. Deployment remains user-owned;
no session lifecycle cleanup is requested or authorized.

## Requested workflow timeout follow-up

User superseded the one-job retry with: "well don't just rerun it... let's
extend the timeout then... to 60 minutes." Retained implementer0 owns the
bounded two-field workflow edit: full/core topic jobs become 60 minutes;
coverage stays 10. Preserve the original authentication commit and make a
separate CI-policy commit. Official upstream action releases/rolling refs
were checked and existing major refs remain current; no action change is needed.
The old-head retry observer returned incomplete and stopped watching. Publish
the reviewed updated API head, cancel superseded same-branch runs, and regenerate
one consolidated channel update to that exact head. Fresh API Specs success at
the new head remains the merge condition. Refresh configuration review/build
evidence after repinning. Integration CI remains unawaited, user owns deployment.

## Result and operator ownership

Requested implementation and timeout follow-up are complete. Both master
branches contain reviewed/tested heads after exact f9 API Specs success:
API f9beb46e5206864bca9d37672e1419cf03661467 and configuration
074b62fe4ca99bcb6e0b2cd186e43f039c666b36. Both API server builds passed.
[Final status](state.md), [integration proof](integration-result.json),
[user deployment/rollback handoff](rollout.md). User owns production rollout;
session remains open and no lifecycle cleanup is requested.
