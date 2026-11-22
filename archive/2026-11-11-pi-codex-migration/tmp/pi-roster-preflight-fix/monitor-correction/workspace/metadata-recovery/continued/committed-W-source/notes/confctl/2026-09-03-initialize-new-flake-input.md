# Initialize a new confctl flake input before setting a revision

## Symptom

`confctl inputs channel set --commit CHANNEL ROLE REV` failed with `unknown
input` when the input and channel mapping had just been added to `flake.nix` but
the input was not present in `flake.lock`.

## Cause

`channel set` expects the mapped flake input to exist in the lock file. The new
input definition alone is not enough.

## Workaround

Commit the input and channel definition, then initialize the lock entry with:

```sh
confctl inputs channel update --commit CHANNEL ROLE
```

After that generated commit, `channel set --commit` can pin an exact revision.
Both commands must run in the repository's Nix development shell so Overcommit
can run Nixfmt.

## Verification

The update added `vpsfreeWorkspace` to `flake.lock` and committed revision
`108bd5f1`. A following `channel set` changed it to exact revision `d45b5e91`.

Related initiative: `work/2026-09-03-dev-session-portal/`
