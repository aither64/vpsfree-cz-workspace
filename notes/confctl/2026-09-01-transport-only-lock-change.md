# Confctl Does Not Commit Transport-Only Input Changes

Related initiative:
`work/2026-09-01-vpsadmin-flake-notifications`.

## Symptom

After changing a flake input from a Git SSH URL to `github:`, this command
rewrote `flake.lock` correctly but printed `No changes` and made no commit:

```sh
nix develop --no-write-lock-file -c confctl inputs update INPUT
```

## Cause

Confctl's input diff currently treats an input as changed only when its locked
revision changes. A fetcher type, owner/repository, or transport change at the
same revision is therefore not considered commit-worthy even though Nix
rewrites the lock node.

## Workaround and verification

Run the input update through confctl as required, then commit the resulting
transport-only `flake.lock` delta with the associated `flake.nix` URL change.
Verify that the locked revision and NAR hash are unchanged and that
`nix flake metadata --no-write-lock-file --json` resolves the intended fetcher.

This was verified when converting `vpsfreeNotificationTemplates` from SSH Git
to the GitHub fetcher without changing its revision or NAR hash.
