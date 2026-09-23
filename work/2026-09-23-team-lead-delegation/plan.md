# 2026-09-23-team-lead-delegation

## Goal

Make a session's root lead reliably discover and use its persistent direct team
for substantive separable work, while keeping short dependent steps with the
lead and preserving the existing review and verification workflows.

## Affected repositories

- `codex-web`: allow idle-thread instruction reconciliation with an explicit
  thread policy.
- `dev-workspace`: apply a root-only lead policy on creation/recovery and portal
  reconciliation; document and test it.
- This coordination workspace: reinforce the rule for CLI-attached leads in
  `AGENTS.md`.

## Approach

Use one concise, stable root policy. For each new substantive work item the lead
checks the live same-session roster using `dev-session team list`; it delegates
nontrivial design and separable implementation to ready retained members,
coordinates their results, and follows the mandatory review skill for review.
Do not start assignments merely because a session was created. Keep the current
global lifecycle policy and independent member policies intact. Reconcile
existing idle root threads with the new policy; retry active threads later.

## Decisions

- A full team means default delegation for substantive separable work, not
  automatic fan-out of every request.
- Roster data stays authoritative. Instructions must not embed addresses or
  model settings that can become stale after add/remove/configure.
- No new communication bus, roster schema, or UI control is needed.

## Compatibility and deployment

No persisted format or cross-service protocol change is intended. The new
`codex-web` API adds an explicit-policy reconciliation method while retaining
the old method. A compatible user-profile `dev-workspace` switch applies the
policy to idle existing root threads; active turns are left alone and retried.
Member threads and their saved model/effort remain unchanged. The portal and
terminal continue to share the root thread. Deploy through the site-composed
workspace package, with the feature `dev-workspace` and `codex-web` heads
pinned in a local deployment wrapper; the generic runtime package alone omits
the site team catalog and cluster providers. Deployment does not integrate any
feature branch to a default branch; that requires separate approval.

## Documentation

Update `dev-workspace/docs/dev-sessions.md` for generic behavior and this
workspace's `AGENTS.md` for local CLI/portal lead guidance. Keep rationale and
rollout evidence in this initiative.

## Testing plan

Focused Go tests for policy creation, recovery, reconciliation, global
lifecycle preservation, and member isolation; Ruby/session tests as affected;
quick checks before mandatory review, then packaged checks and a bounded
full-team canary. Exercise solo and dynamic add/remove behavior and verify
portal and CLI see the same retained thread. Long checks use the fresh Luna/low
watcher. Do not merge without explicit integration approval.
