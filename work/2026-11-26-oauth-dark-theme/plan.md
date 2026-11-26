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

Implementation scope: vpsadmin (OAuth server), vpsadmin-webui (React/BFF),
haveapi (provider response extension and online documentation), and
vpsfree-cz-configuration (site branding). vpsf-status is the visual/asset reference;
web confirms dark-logo provenance. No vpsadminos changes are needed.

## Approach

The user accepted implementation on 2026-11-26, with the explicit amendment:
"we don't need to keep core.logo_url sysctl fallback. aside from that, implement
it". Deployment and default-branch integration remain separate actions.

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
- Implement the accepted brief in session-owned project worktrees.
- Use the existing semantic palette and both transparent vpsf-status logos;
  copy site assets into configuration rather than depend on the status package.
- Exchange `theme=light|dark|auto`; React maps system to auto. Keep the effective
  scheme separate. New clients request success-response theme with
  `theme_return=1`, preserving compatibility with strict older docs callbacks.
- The choice on the OAuth page wins on successful return. Consume it only after
  existing authentication validation; errors retain the initiating preference.
- Keep OAuth state, PKCE and registered redirect URI semantics unchanged.
- Reuse deploymentConfig JSON for branding; remove core.logo_url registration
  and consumers. Scheme override → declarative common logo → bundled vpsAdmin
  wordmark. No migration solely to delete dormant settings rows.

## Compatibility and deployment

The accepted design covers clients without theme parameters, staggered client/server
updates, dormant logo sysconfig rows, declarative assets, deployment ordering and
rollback. No migration or API-schema/SDK change was introduced. Configuration
retains its reviewed scoped0b base while current master1e43 has four unrelated
commits; later integration requires separate approval and fresh reconciliation.

## Documentation

Current readers: the user, implementation owners and reviewers. Proposal and
temporary evidence belong in this session's plan/state/design. Future lasting
theme/configuration contracts belong with their owning project when implemented.

## Testing plan

Implementation and final independent source/history reviews are complete across
all four repositories. Quick gates, installed package proofs, four configuration
system builds and composed consumer verification are accepted. C default/site and
all six D docs native cases are accepted within their recorded input scopes.

All planned native provider and paired-client acceptance is now complete within
its recorded scope. The final B recovery/SSO continuation passed with original
C/D records unchanged after exact auth_url/TLS restoration. Earlier successful
leaves and failed fixture attempts remain separately identified; three canonical
recovery submissions stayed private and queued without SMTP. No product change
followed fixture corrections.

The remaining check is broad B integration CI45836501978 at exact913. All27
API full/core jobs and final4 C CI runs have passed. Keep the initiative active
while this external result and unmerged delivery remain outstanding. Exact
commands, outcomes, source/input boundaries and limitations are in [state.md](state.md)
and linked owner evidence. No merge, deployment or lifecycle action follows
verification acceptance.
