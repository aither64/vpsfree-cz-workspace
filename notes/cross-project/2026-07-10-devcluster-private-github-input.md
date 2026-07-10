# Dev cluster private GitHub input

## Symptom

Starting a vpsAdmin dev cluster failed while evaluating
`dev-clusters/vpsadmin/flake.nix`:

```text
unable to download .../vpsfree-sms-gateway/commits/2026-06-15-vpsadmin-events
HTTP error 404
```

## Cause

The `vpsfreeSmsGateway` flake input uses a `github:` URL for a private
repository. Nix resolves that input through the unauthenticated GitHub API,
which reports the private branch as not found even though the canonical bare
repository can fetch it over SSH.

## Workaround

Add a `vpsfree-sms-gateway` worktree to the same initiative. The dev-cluster
helper detects the worktree and overrides `vpsfreeSmsGateway` with the local
path, avoiding GitHub API resolution:

```sh
bin/dev-session worktree add <slug> vpsfree-sms-gateway --as-is \
  --base origin/2026-06-15-vpsadmin-events
```

## Verification

Related initiative: `work/2026-07-10-kb-czech-fixes/`. Verification is
recorded in that initiative's `state.md` after the cluster start retry.
