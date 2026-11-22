# `confctl inputs channel set` uses channel and role names

## Symptom

Running `confctl inputs channel set` with the flake input name in either the
channel or role position reports `no channels matched`.

## Cause

The command arguments are `<channels> <role> <rev>`. These are the first two
columns from `confctl inputs channel ls`, not the flake input in its third
column. For `vpsadminServices`, the channel and role are both `vpsadmin`.

## Fix

Inspect the mapping before setting an exact revision:

```shell
confctl inputs channel ls
confctl inputs channel set --commit vpsadmin vpsadmin REVISION
```

Run the command and the resulting push from the repository's Nix development
shell so its commit and push hooks can find the pinned Ruby gems.

## Verification

The corrected command generated the expected `vpsadminServices` lock update,
ran the Nixfmt hook, and committed it. The pushed configuration branch then
built all seven password-recovery rollout hosts successfully.

Related initiative:
`work/2026-08-18-vpsadmin-password-reset/`.
