# Nix path inputs cannot traverse workspace symlinks

## Symptom

Starting the vpsAdmin development cluster from a clean temporary workspace
checkout failed while resolving the local `vpsadmin` flake input:

```text
error: path '//tmp/.../worktrees' is a symlink
```

## Cause

The temporary checkout linked its `worktrees/` directory to the main
coordination workspace. Nix rejects path flake inputs when an ancestor of the
input is a symlink.

## Workaround

Create detached clean project worktrees below the temporary checkout at the
exact revisions required by the cluster. This preserves clean-source isolation
without putting a symlink in the flake input path.

## Verification

Related initiative: `work/2026-07-13-security-advisory-automation/`.
The subsequent cluster evaluations accepted real detached worktrees below the
temporary checkout. The final compatible build used detached `vpsadmin`,
`vpsadminos`, and `vpsfree-cz-configuration` inputs.
