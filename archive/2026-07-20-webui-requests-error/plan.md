# 2026-07-20-webui-requests-error

## Goal

Fix the production vpsAdmin WebUI failure when denied change requests belong
to hard-deleted users. Preserve the historical user ID using the same raw
foreign-key pattern already used by IP address assignments, keep request list
and detail rendering null-safe, and reject attempts to resolve a request whose
user no longer exists.

## Affected repositories

- `vpsadmin`: WebUI approval-request rendering, requests plugin API/model, API
  specs, and Playwright regression coverage.
- `vpsadmin-kb-captures`: pin the exact vpsAdmin feature revision and run the
  WebUI documentation contract because the rendered fallback is user-visible.
- `haveapi-client-php` and `haveapi`: read-only reference for association
  serialization and lazy resolution behavior. No changes are expected in
  either repository for this fix.

## Approach

1. Add `UserRequest#raw_user_id` and expose it as an additive integer API
   output, blacklisted from non-admin Index/Show responses like
   `IpAddressAssignment#raw_user_id`.
2. Render the live user when the typed association resolves and otherwise
   render the preserved raw ID without dereferencing the null association.
   Apply this to approval-request list and detail pages, and omit resolution
   controls for historical change requests with no live user.
3. Reject direct resolution of a change request whose user association is
   missing before any request state or mail processing can occur.
4. Add focused API specs and extend the existing admin approval-request
   Playwright scenario with a denied hard-deleted-user fixture.
5. Commit after quick verification, run the mandatory standalone change
   review, then run the targeted WebUI integration test.
6. Push the vpsAdmin feature revision, pin it in `vpsadmin-kb-captures`, and
   run the documentation contract to determine whether any KB pages or
   screenshots are affected.

## Compatibility and deployment

The API change is additive and requires no database migration or persisted
state change. Old WebUIs ignore `raw_user_id`; new WebUIs probe the returned
attribute map and therefore remain safe against an older API, falling back to
`-` until the API is upgraded. Deploying the API first gives the final numeric
fallback immediately. No generated client, node, vpsAdminOS, protocol, or
configuration coordination is required, and rollback can read all existing
state because no stored format changes.

The raw ID remains admin-only on Index/Show, matching the existing IP address
assignment authorization pattern. Hard-deleted `User` resources remain hidden;
the change does not relax the `User` default scope.

## Testing plan

- Run the focused change-request API spec, covering additive output,
  authorization, hard-deleted association serialization, and resolution guard.
- Run WebUI PHP syntax checks and the repository hook suite.
- Extend and run `webui#users-admin` after the mandatory change review.
- Run the WebUI documentation contract from the capture repository against the
  exact pushed vpsAdmin revision and record any reported page/capture impact.
