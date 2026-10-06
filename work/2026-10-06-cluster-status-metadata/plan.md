# Restore development-cluster status decoding

Restore the existing portal card for the storage-redesign cluster. Its helper
returns a valid schema-2 response containing `webuiSource` and `maintenance`,
but the strict portal decoder does not recognize either field. The live helper
reports running/ready with a released maintenance receipt and ten services.

## Scope and decisions

- Generic `dev-workspace`: accept optional typed metadata in the helper wire
  response, validate it, and retain the existing public Status/card interface.
- Coordination workspace: select the repaired nested runtime without changing
  the selected extension or unrelated inputs.
- `vpsfree-cz-configuration`: align its `dev-workspace` channel/devWorkspace
  role, build/deploy only `cz.vpsfree/machines/aitherdev`.
- No edits, reset, rebuild, or record changes in the storage-redesign session.
  Use its helper and portal only for read-only reproduction and acceptance.
- Readers: runtime/provider developers and deployment operators. Lasting
  contract documentation belongs in the runtime portal guide; exact rollout
  revisions and evidence belong in this initiative.

## Design and compatibility

The wire response gains optional schema-2 metadata structs. WebUI source has a
lowercase 40-hex revision, explicit dirty boolean, and pinned/worktree kind.
Maintenance supports versions 1 and 2, maintenance mode, the six existing
phases, and explicit pending/copied/active booleans. Pending/active flags must
agree with phase. Pending maintenance requires false readiness and no services.
Unknown fields and trailing output remain rejected; schema-1 and older schema-2
responses with no metadata remain supported. Metadata is not displayed or added
to public Status. No persisted formats, databases, API clients, guest protocols,
Nix module options, or cluster transition policies change.

No cluster-state migration, guest rollout, coordinated node update, or retained
disk reset is required. Old portal readers reject these helper fields; deploy
the repaired reader using the supported forward-only user-profile switch.
Keep the existing policy-3-capable extension unchanged. Recover a failed switch
through its normal journal and the same/newer compatible package.

## Verification and rollout

Add regression cases for the current combined payload, individual metadata,
versions 1/2, absent metadata, malformed metadata, strict rejection, and cache
replacement during pending maintenance. Run focused Go/portal checks in Nix.
Commit and independently review the complete runtime branch and documentation
before long checks; explicitly conclude no migrations and no obsolete history.
Use fresh catalog-policy watchers for long checks/builds/CI waits.

Publish the reviewed runtime feature revision, generate the workspace nested
lock and configuration channel pins, inspect semantic lock identities, and run
the deployment-contract checker. Build/deploy the aitherdev host configuration
from its feature worktree and activate the composed application through the
user profile. Verify the real portal card and unchanged retained cluster.
Integrate all exact final feature heads fast-forward-only after verification.
Retain branches and leave the session open.

## Authorization

The user selected restoring the existing card without displaying metadata.
They authorized deploying aitherdev using vpsfree-cz-configuration and merging
the verified fix into the affected default branches. The accepted plan names
`aither64/dev-workspace:master`, `aither64/vpsfree-cz-workspace:master`, and
`vpsfreecz/vpsfree-cz-configuration:master`. The user then requested implementation.
