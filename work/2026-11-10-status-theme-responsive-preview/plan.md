# 2026-11-10-status-theme-responsive-preview

## Goal

I'd like to extend vpsf-status, so that:

- contains light/dark themes (auto detection + manual switch).. not sure how to handle this, it could be near language switch, but perhaps in a drop down menu? leaving that up to you
- the current theme is light, so you have to introduce the dark theme. use colors/inspiration from vpsfree.cz and the new dark theme from vpsadmin-webui (although this one is not perfect, it has insufficient contrast and is thus hard to read).
- make the design responsive to support smaller screens (tablets and phones)
- I'll need to see it in a preview server... we do have it integrated into vpsadmin dev cluster, but it is rather heavy, so maybe it'd be worth to run it standalone

Look it over and suggest a solution.

## Affected repositories

- `vpsf-status`: intended implementation, styling and standalone preview.
- `web` and `vpsadmin-webui`: read-only visual references from canonical bare repositories.
- Coordination workspace: this session's plan, state and proposed design only.

## Approach

Current request is investigation and a proposed solution. Architect `architect0`
owns bounded source investigation and `design.md`; no application implementation,
preview launch, deployment or default-branch integration is assigned in this pass.
Inspect current rendering, localization, styles, reference palettes and standalone
runtime dependencies. Propose a small implementation with clear acceptance checks.

## Decisions

- Preserve the existing light appearance while introducing an accessible dark palette.
- Recommend explicit System/Light/Dark choices and responsive header/content layout.
- Prefer a standalone preview if existing architecture permits representative data
  without the vpsAdmin development cluster; distinguish verified feasibility from
  an untested launch recipe.
- Retain the saved Full-team roster and settings. Only the design package is
  executing; implementers and reviewer are not assigned speculative work.

## Compatibility and deployment

Aim for frontend-only behavior and a browser-local preference, with no API,
database, protocol or deployment-configuration changes. Confirm this in source.
No production deployment, integration or session lifecycle action is authorized.
Future temporary previews must use `dev-session service run`.

## Documentation

Readers: user evaluating the proposed UX and implementers taking a subsequent
implementation package. Keep proposal/evidence in this session's `design.md` and
current phase/results in `state.md`. Lasting feature/preview documentation belongs
in vpsf-status if implementation proceeds.

## Testing plan

This pass uses source inspection only; no builds or tests are necessary to state
the proposal. Design will identify quick checks and browser acceptance for both
themes, system/manual preference, localization, contrast, narrow screens and
representative status data. Implementation requires committed changes, passing
quick checks and mandatory independent final review before longer checks.
