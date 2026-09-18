# Archive unchanged local feature branches

## Goal

Allow `dev-session archive` to complete when a registered feature branch has no
commits beyond its recorded `initial_base_sha` and therefore has never been
pushed. The archive must still prove that the unchanged head is an ancestor of
the current remote default branch.

## Affected repositories

- `dev-workspace`: archive merge proof, retry proof, lifecycle documentation,
  and focused tests.
- `vpsfree-cz-configuration`: deploy the exact runtime commit to
  `cz.vpsfree/machines/aitherdev` through a feature branch; do not integrate
  configuration master.
- Workspace coordination: retain this plan and state, deployment evidence, and
  the requested archive result.

## Implementation decisions

- “Unchanged” means local feature head equals the manifest's valid
  `initial_base_sha`; equal trees are insufficient because history matters.
- Always fetch and verify the configured remote default branch.
- If the feature ref exists, fetch it and require exact equality with the local
  feature head. If it is absent and the branch is unchanged, use the local head
  for the ancestry proof. Missing refs for changed branches, missing base
  markers, and transport or authentication errors remain failures.
- Apply the same rule to initial archive proof and interrupted-archive retry
  proof. Keep journals, manifests, final-head recording, worktree checks, and
  retained branch refs unchanged.

## Compatibility and rollout

There is no schema, journal format, API, database, or protocol change. Older
runtimes continue to fail safely when an unpushed feature ref is absent. The
new runtime is backward compatible with existing manifests and only accepts an
absent feature ref when the recorded base proves there were no feature commits.
Deploy the exact runtime commit through the aitherdev configuration feature
branch, dry-activate first, then activate and switch the user profile. Keep the
previous profile and configuration generation available for rollback.

## Verification and completion

Run focused archive tests, repository hooks, mandatory change review, and the
required flake/build checks. After aitherdev health checks pass, archive
`2026-09-14-kernel-history-fix` and verify its journal, manifest, retained refs,
and unrelated worktrees. Do not archive if deployment or runtime checks fail.
