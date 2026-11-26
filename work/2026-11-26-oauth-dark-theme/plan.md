# 2026-11-26-oauth-dark-theme

## Goal

I'd like you to add dark theme support to the oauth server in vpsadmin API.

- the login should have controls for light/dark/auto switch, use compact icons
- the login form shows vpsfree.cz logo in production. we'll need the logo in a dark variant. see if you can reuse it from vpsf-status. we can make the logos configured declaratively instead of a sysctl, so the logos would be provided through vpsfree-cz-configuration
- vpsadmin should have some default logo if it is unset
- dark color scheme should look similarly to vpsf-status, look there for inspiration
- it has to be interconnected with the react UI. so when the user is logging from the react UI, the auth server must use the same theme as the client. I imagine this will be passed as a query parameter. We also have to land back into the same theme when returning to the UI.
- php webui so far doesn't have a dark theme, so there will not be any interconnection
- it'd be nice if we could have scheme integration also from haveapi online documentation available at api.vpsfree.cz. It should work in the same way as the react UI, so the same theme is preserved.

Look it over, suggest a solution and create an implementation plan.

## Affected repositories

Expected: vpsadmin (OAuth server), the React WebUI repository, haveapi
(online documentation), and vpsfree-cz-configuration (site branding). Inspect
vpsf-status for existing dark colors and reusable logos; inspect packaging/module
owners as needed before fixing the final repository scope.

## Approach

This request authorizes investigation, a proposed solution and an implementation
plan. Product implementation, deployment and integration are later phases.

1. Inspect current OAuth forms, branding and authentication flow.
2. Inspect theme and OAuth flows in the React UI and HaveAPI documentation.
3. Reuse vpsf-status design conventions and existing logo assets where suitable.
4. Record a concrete cross-project contract, compatibility and verification brief
   in [design.md](design.md), then present the proposal to the user.

## Decisions

- Preserve the distinction between an explicit theme preference and the scheme
  resolved from the operating system. Determine exact transport from source.
- Keep existing OAuth state/redirect security and retry behavior.
- PHP WebUI theme integration is out of scope.
- No project worktrees or feature changes are needed for this planning phase.

## Compatibility and deployment

The design must cover clients without theme parameters, staggered client/server
updates, existing logo sysconfig, new declarative assets, deployment ordering and
rollback. No database or API-schema change is assumed until investigation proves
one necessary.

## Documentation

Current readers: the user, implementation owners and reviewers. Proposal and
temporary evidence belong in this session's plan/state/design. Future lasting
theme/configuration contracts belong with their owning project when implemented.

## Testing plan

Planning uses source inspection only. The final brief will identify quick checks,
independent final review and longer browser/auth verification for implementation.
No implementation or integration tests are being claimed during planning.
