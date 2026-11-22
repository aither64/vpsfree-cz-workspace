# Node builds require the external initrd SSH key

Initiative: `work/2026-07-13-security-advisory-automation`

`confctl build -y "cz.vpsfree/nodes/stg/*"` can evaluate the node configurations
successfully and then fail while forcing the top-level derivation with:

```text
error: path '/secrets/nodes/initrd/ssh_host_ed25519_key' does not exist
```

The initrd host key is an external deployment secret and is not present in a
normal feature worktree. Nix formatting and module evaluation before the
top-level build can still be used as local validation; a complete node build
requires the deployment secrets environment. No secret value belongs in the
worktree or logs.
