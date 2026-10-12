---
lifecycle: active
---

# Portal Codex provider selection

## Current status

Investigation/design in progress. The user requested provider selection and a
provider label in the Codex limits area. Proposed scope is the whole workspace;
the optional scope clarification is pending. No application code or live provider
settings have changed for this initiative.

The affected projects are dev-workspace and codex-web. This tracking-only session
has no native lead or roster, so the lead performs ordinary investigation/design
and implementation. Mandatory final review will use the installed fallback review
policy. No specialists or team members are being added.

## Phase checklist

- [x] Read workspace routing, source instructions and documentation entry points.
- [x] Create and verify an isolated initiative; identify repository scope.
- [ ] Finalize provider/UI/transition design and verification brief.
- [ ] Implement on owned feature worktrees and run quick checks.
- [ ] Commit, publish and complete independent final review.
- [ ] Complete longer verification and prepare a reviewable handoff.
- [ ] Integrate/deploy only under explicit direction for those actions.

## Findings and next action

GET /api/codex-limits is session-independent and cached for 30 seconds. Its current
sidebar does not expose the provider. The installed 0.160.0 provider change was
previously verified through cold native thread/resume; loaded threads ignore the
override. Merely restarting retains the old saved provider unless resumption
explicitly chooses the new one. Native member access must be rebound from the
saved application roster. Codex cgroups can own VMs, and the portal cgroup owns
tmux; a provider operation must preserve both boundaries.

Next: inspect runtime/client construction and existing operation recovery before
final design. Initial branch/worktree registrations and implementation are pending.

## Documentation and cleanup

Maintain plan/state and the design brief here, and lasting contracts in the owning
project docs. Keep the existing portal.yml free of secrets and transient outputs.
No archive, delete, session stop, cluster mutation or live deployment is authorized.
