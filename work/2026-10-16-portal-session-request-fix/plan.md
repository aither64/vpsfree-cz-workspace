# 2026-10-16-portal-session-request-fix

## Goal

Fix portal session creation failing with `unknown session request field` and
replace the saved request's poorly spaced text copy button with the established
copy icon. Deploy the reviewed result to aitherdev using its configuration.

## Affected repositories

- `dev-workspace`: creation form validation, recovery layout, regression coverage.
- `workspace`: select the exact fixed runtime in the nested flake input.
- `vpsfree-cz-configuration`: matching `dev-workspace` channel pin and aitherdev
  system artifact. Application selection remains in the workspace user profile.

## Approach

Compare the actual browser form with the strict preparation parser. Preserve
strict validation, admitting only the already supported notification preference.
Reuse the portal copy control and its feedback, with space around the saved text.
Publish isolated feature branches, run focused checks, commit and independently
review the full series before longer packaged/browser verification and deployment.

## Decisions

- The user authorized aitherdev deployment, not default-branch integration.
- Keep all feature refs and the initiative active pending merge direction.
- This conversation created the initiative after `dev-session current` found no
  current session and neither DEV_SESSION identity variable was present.
- A bounded form allowlist and recovery control fix is lead-owned; no separate
  application implementer is needed. Consult the installed policy for review
  and verification utilities; do not invent a team.

## Compatibility and deployment

The parser already contains validation and persistence for
`browserNotificationsEnabled`, but its allowlist omits that field. Admitting the
existing exact boolean field preserves request/state formats, notification
defaults, idempotent retries, old clients, and strict rejection of other fields.
No database, schema, journal, API client, daemon protocol or cluster changes are
intended. The copy control changes only browser markup/styles and reuses the
existing clipboard handler. No coordinated node upgrade is needed.

Select the published runtime through the workspace's direct nested override and
configuration's confctl channel. Verify matching locks, build outside claims,
and activate system then user profile through the coordinator's exact owned
reservation. Preserve live identity/recovery receipts; profile selection is
forward-only. Recover through the same operation or a compatible successor.

## Documentation

Readers are portal maintainers and the deploying operator. Update the owning
session-preparation documentation if the control wording changes. Keep exact
rollout revisions, logs and review evidence in this initiative. No KB publication
or vpsAdmin WebUI change is involved.

## Testing plan

- Regression for notification preference true, false, omitted, malformed and
  duplicate values, retaining unknown-field rejection.
- Focused Go web checks, syntax/format checks and existing recovery browser
  coverage, using the repository's Nix environment.
- Independent committed full-branch review including migration/history inventory.
- Packaged checks and browser recovery verification after review, with fresh
  verification watchers for long/uncertain checks.
- Matching deployment locks, built aitherdev artifact, coordinated activation,
  and live portal checks for request acceptance and accessible copy layout.
