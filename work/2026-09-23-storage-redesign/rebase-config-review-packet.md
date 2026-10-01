# Final rebased configuration review

## Requested outcome and exact scope

Review the complete unmerged site configuration branch after the user-requested
current-default rebase. The disposable React cluster uses the installed
provider independently; this branch is a guide plus a generated service pin,
with no host deployment or default-branch integration authorized.

Verified session: `2026-09-23-storage-redesign` in
`/home/aither/workspace/ai/vpsfree.cz`. Current scope and acceptance criteria:
[design.md](design.md), [plan.md](plan.md), [state.md](state.md), and the
individual [rollout record](rebase-devcluster-20261001.md).

Repository/worktree: `vpsfree-cz-configuration` at
`worktrees/2026-09-23-storage-redesign/vpsfree-cz-configuration`.
Base: `029c616ed906de80b8813cc20391e294c3e9f4c2` (`origin/master`).
Head: `5eff558c493b2d8ee2e2fff120fd68f3d30fbdc8`.

Complete series:

1. `603da36eb4179647abd898d68cb868e591422df5` — rollout guide and navigation.
2. `5eff558c493b2d8ee2e2fff120fd68f3d30fbdc8` — confctl-generated service pin.

The obsolete earlier service pin was removed during rebase; its refs are
preserved. Exactly one generated pin remains. No migrations or schema changes
exist in this repository/range. The two externally consumed Admin migrations
retain their versions/blobs/schema and were independently cleared in Admin's
complete nineteen-commit review; reset does not erase that provenance.

## Cross-project graph and non-goals

Published/reviewed Admin:
`e65a5a6b0f227f78cdcd40afa6a8de1f5b497b36`, based on `90184b374`.
Published/reviewed provider:
`8d05dc3ae1fb71c1385609990acdf093af49ceec`, based on staging `26f28c691`.
Both complete branches passed HIGH-risk four-lane independent review.

The generated lock changes only `vpsadminServices.locked` revision, NAR hash and
timestamp. Follows mappings and all other lock nodes are unchanged, including
site OS staging/production, Admin staging/production and React. The services
input follows the site's independent `vpsadminosStaging`; the Admin internal
provider pin alone does not upgrade a shared storage host's osctld. The new
upstream React input/channel follows `vpsadminServices` and remains intact.
No staging provider pin, shared-host switch, production rollout or merge.

Guide acceptance: truthful API-only global freeze/DB-drain, schema/provider/Node
ordering, actor/CAS controls, rollout/recovery boundaries, and no physical quiet
or repair authority. Child coverage and historical terminal proof remain unknown;
strict production, identity publication, repair readiness and APPLY stay off.
The published provider is a current-staging descendant; do not regress the site
OS lineage to the original old `dcad` provider base.

## Verification and review request

Generated update used the required normal Nix environment and
`confctl inputs channel set --commit vpsadmin vpsadmin <published Admin SHA>`.
Generated commit message is preserved, including its expected TextWidth warning.
Commit hooks passed; tracked tree clean; complete-range diff check clean.
Lead structural assertion confirms only the one service lock node changes.
Normal full hooks and channel evaluation are the separate quick check gate;
their results are supplied with assignment after completion.

Risk: HIGH because the guide describes authorization/deployment ordering and the
pin changes a live service package graph, despite no actual shared-host deployment.
Reviewer: retained independent reviewer0, saved GPT-6.1 Sol/xhigh/read-only,
without overrides. Cover general, architecture/repetition, scope/proportionality,
and risk/compatibility using the canonical skill and all four references.

Inspect the complete two-commit series, final diff, generated message and
consumers; explicitly conclude history/no-migrations status. Read-only review,
no builds/deployment/private credentials. Earlier slice reviews are context,
not a substitute for this final rebased range.
