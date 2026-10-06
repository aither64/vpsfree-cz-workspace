# gh-runner3

## Goal

Create the `gh-runner3` machine in `vpsadminos-org-configuration` using the
existing GitHub runner machines as the pattern. Add the matching internal DNS
entry in `vpsfree-cz-configuration`.

## Affected repositories

- `vpsadminos-org-configuration`
  - Branch: `2026-06-01-gh-runner3`
  - Worktree: `worktrees/2026-06-01-gh-runner3/vpsadminos-org-configuration`
- `vpsfree-cz-configuration`
  - Branch: `2026-06-01-gh-runner3`
  - Worktree: `worktrees/2026-06-01-gh-runner3/vpsfree-cz-configuration`

## Inputs

- Machine name: `gh-runner3`
- VPS ID: `29654`
- Internal IP: `172.16.4.25`

## Approach

1. Inspect the existing GitHub runner definitions in
   `vpsadminos-org-configuration`.
2. Add `gh-runner3` by following the nearest existing runner pattern and only
   changing identity-specific values.
3. Find the internal DNS zone in `vpsfree-cz-configuration` and add
   `gh-runner3` with IP `172.16.4.25`.
4. Run targeted evaluation or syntax checks supported by each repository.
5. Commit the two repository changes separately if validation succeeds.

## Decisions

- `vpsadminos-org-configuration` does not store VPS/container IDs in the
  existing GitHub runner machine modules, so `29654` is not represented there.
- `vpsfree-cz-configuration` was changed only in the internal DNS zone requested
  by the task. Its older `cluster/org.vpsadminos/cluster.nix` mirror was left
  untouched because adding a container ID there without regenerated vpsAdmin
  container placement data could break monitor/alerter evaluation.

## Compatibility and deployment

This should be an additive machine and DNS configuration change. It should not
alter existing persisted state, database schemas, APIs, protocols, generated
clients, or module option semantics. Mixed-version operation is expected to be
safe because existing hosts and records remain unchanged. Rollback consists of
removing the new machine definition and DNS record; no new on-disk format or
state migration is introduced by the configuration itself.

Deployment ordering is flexible for existing services. Creating DNS before the
machine is active may briefly resolve a not-yet-running host, while deploying
the machine before DNS may require direct-IP access; neither affects existing
machines.
