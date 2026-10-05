# Fix newadmin probes and warning-only dedicated alerts

## Goal and authorization

Implement the plan accepted by the user's "Implement the plan" instruction.
Correct the public frontend metadata probe and retain all dedicated Newadmin
alerts as warnings. The user selected "Newadmin alerts only": shared
infrastructure alerts for the VPS retain their existing severities.
Implementation and verification were authorized initially. The user later
explicitly directed integration of `vpsfree-cz-configuration` into default branch
master and retained production deployment ownership. That fast-forward
integration is recorded in state.md. No agent deployment or session lifecycle
action is assigned.

## Scope and implementation

Only `vpsfree-cz-configuration` changes. Keep the WebUI application, dependency
pins, Alertmanager routing and shared infrastructure rules outside scope.

- Correct both frontend body patterns in
  `modules/clusterconf/monitor/http.nix` to allow JSON whitespace around colons.
  Retain schema version 1, require a comma or closing brace after it, and retain
  the full lowercase 40-character hexadecimal commit hash.
- In `modules/clusterconf/monitor/rules/vpsadmin.nix`, change the three dedicated
  missing-metrics alerts to warning. Compute HTTP severity once for each site:
  warning for the exact newadmin frontend and BFF keys, critical for other
  sites. Use that value in both generated ExporterDown and WebDown alerts.
- Preserve alert names, PromQL, durations and notification frequencies. All
  nine dedicated Newadmin alerts must be warnings; API, console and legacy UI
  checks remain critical.
- Update existing rule test expectations and coverage for both exporter-down
  alerts, all-nine warning severity and critical control cases for other sites.
- Document the warning-only policy in `docs/operations/newadmin-webui.md`.
  Promotion to critical requires a later explicit policy decision.

## Team and execution

The runtime retained the solo preset and refused a different preset. Add the
installed development implementer and reviewer roles with supported team-add
commands, preserving the saved lead and each member policy.
The lead owns session tracking, coordination and acceptance. Assign this small,
bounded unit directly to the retained implementation-purpose member; a separate
architect design document is unnecessary because the approved plan resolves the
regex and alert-generation design without an interface change. Preserve saved
access, model and effort. Use the retained independent review-purpose member
under the mandatory-change-review skill.

Use the exact session branch and dedicated worktree. Fetch upstream before
creating it. Commit with declared hooks active, and retain a coherent reviewed
branch. Long or uncertain verification is launched and monitored by a fresh
catalog-resolved Luna/low watcher under dev-session-monitor.

## Compatibility and deployment

This is monitoring configuration only. Compact and formatted schema-1 JSON are
both supported. No persisted-state, schema, API/client, protocol, Nix option or
WebUI deployment changes are required. Mixed monitoring versions continue to
operate, but the old monitor can still emit false failures and critical alerts.

Prepare rollout instructions for both `cz.vpsfree/containers/prg/int.mon1` and
`cz.vpsfree/containers/prg/int.mon2`; do not activate them without explicit
production deployment direction. Confirm the frontend and BFF probes report
`probe_success = 1` and all dedicated Newadmin rule severities are warning.
A whole-change rollback restores the faulty compact-body checks and critical
severities; prefer a targeted correction retaining the warning-only policy.

## Verification and acceptance

Before independent review, use the Nix environment for quick rule checks,
formatting/hooks and regex fixture checks. Compact, formatted and additional
whitespace metadata must match; schema 10 and invalid commit hashes must fail.
Run the existing newadmin promtool check, extending it to verify all nine
warnings, both exporter failures and API/console/legacy critical controls.

Commit intended changes and inventory the complete base-to-head series and
final diff, including an explicit no-migrations conclusion. Conduct mandatory
independent review before long integration verification. Resolve material
findings, then build both monitoring hosts via the fresh verification watcher.
Record tested exact heads and build results. No production activation is part
of implementation acceptance.

## Documentation and handoff

Operators need the warning policy in the existing configuration operations
guide. Session tracking retains investigation evidence, exact revisions,
verification, review and prepared rollout/rollback steps. Update the portal
with useful durable artifacts and include its stable URL. Keep lifecycle active
and the session open for the operator-owned rollout and follow-up results.
