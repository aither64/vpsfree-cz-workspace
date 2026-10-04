# API specs workflow optimization

## Goal and authorization

Reduce vpsAdmin API-spec workflow execution from its usual 40+ minutes while
preserving every existing test and both plugin modes. Historical investigation
and proposal review are complete. User requested an implementation plan, rejected
weighted sharding because test placement should remain simple, then authorized
“Implement the plan” on 2026-10-04. Implementation and controlled CI verification
are authorized; vpsadmin/master integration, production deployment and session
closure are not.

## Affected repositories and scope

vpsAdmin workflow plus AGENTS.md and testing procedure placement guidance.
Coordination workspace retains design, review and benchmark evidence. No API,
plugin, spec, schema, package or dependency change. Worktree/branch ownership and
exact heads are in state.md; do not borrow another session's worktree.

## Chosen approach

Maintain thirteen static domain topics in each full/core mode, 26 independent
jobs. Combine smoke/coverage/routes/models/supervisor into foundation and spend
the four released slots on platform3, users/auth2 and network/IP2. Other domains
stay unchanged. Use explicit patterns and the shared matrix; no test moves,
catch-all assignment, selector framework or duration-based placement.

Two functional commits: diagnostics and stronger both-mode aggregate using the
original topics, then static rebalancing with lasting developer guidance.
Native RSpec JSON supplements readable output; mode-qualified seven-day artifacts
retain manifests, outcomes, seeds and effective dependency fingerprints.
The aggregate checks exact-once file coverage per mode and successful matrices.
[Implementation plan](implementation-plan.md) and [focused design](design.md)
define the precise partition, interfaces, recovery and verification contract.

## Compatibility and recovery

Each job retains its isolated process/database and normal filters, pending
behavior and randomized order. Stable aggregate check name retained; renamed
topic contexts/artifacts are the only compatibility surface. Classic protection
inventory is permission-limited; document context mapping before adoption and
resolve required-check settings before integration. No production persisted
state, API/client/protocol, schema/migration or deployment ordering changes.
Rollback restores old topic patterns/expected names; diagnostics can remain.

## Verification

Quick checks/hooks and independent whole-branch history/final-diff review first.
Only after review push instrumented old-topic baseline, wait for its full run,
then candidate and a second candidate run. Keep source and dependency inputs
identical, compare effective Ruby/Bundler/RSpec/lock fingerprints by mode, and
require exact example IDs/status/pending parity. The native comparator is
session-only evidence tooling, never an application selector.

Seek <=25-minute slowest candidate test job in both runs. Separate execution,
queueing, setup, full workflow wall time and runner minutes. Investigate failed
attempts before reruns; missing evidence is not acceptance. Monitoring follows
the pinned utility policy with documented visible parent fallback when native
utility selection is unavailable. No VM/production verification is needed for
this workflow-only scope. Leave the feature unmerged pending explicit approval.

## Documentation and evidence

Maintainers and feature authors use vpsAdmin AGENTS.md and
`docs/agent-instructions/testing.md` for static topic placement, aggregate/artifact
semantics and local reproduction. Session records own exact revisions, temporary
benchmark/review tools and adoption evidence. Historical evidence remains in
[investigation.md](investigation.md) and [timing-summary.json](timing-summary.json).
Prior alternative estimates are historical, with weighted sharding rejected.
