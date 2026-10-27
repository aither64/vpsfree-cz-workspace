# 2026-10-27-codex-profile-generations

## Goal

dev-workspace codex profiles seem misdesigned to me. Look at this directory: /home/aither/.local/state/dev-workspaces/codex/generations/

it contains many generations and I don't see any way to remove the old generations. if it used standard nix-env profile, there would be an easy way to delete old generations. why was it done this way, is there any reason why it can't use normal nix-env? see if other profiles regarding the dev-workspace don't have a similar problem.

investigate and suggest a solution.

## Affected repositories

- `dev-workspace`: profile generation creation, switching, rollback and retention.
- Site workspace/configuration: read-only consumers and retention policy if relevant.
- No application edits, installed-profile changes, cleanup, deployment or integration requested.

## Approach

1. Architect `architect0` traces installed layout and source/history, inventories related profiles, and writes evidence and a recommendation in `design.md`.
2. Lead checks that the findings answer the user's questions and presents the smallest conventional solution with explicit limits.

Acceptance: explain documented versus inferred rationale; establish actual root/retention behavior; assess normal `nix-env` feasibility; cover other profile families; propose migration and cleanup semantics preserving running and recovery references.

## Decisions

- Investigation and proposal only. Inspect live state read-only; do not remove generations or invoke package transitions.
- The same-session retained architect has ready workspace-write access and owns substantive investigation/design. Implementers remain unassigned because implementation is outside this request.

## Compatibility and deployment

Assess immutable generation references, rollback, package-transition journals, mixed old/new helpers and GC reachability. No deployment is planned.

## Documentation

Readers: user and a future implementer. Findings/proposal belong in this session's `design.md`; plan/state hold scope and evidence. Owning project documentation can change with a later implementation, once behavior is decided.

## Testing plan

Read-only inventory and source/history inspection. No builds or integration tests are needed for this investigation. Distinguish verified runtime facts from an unimplemented/unverified proposal.
