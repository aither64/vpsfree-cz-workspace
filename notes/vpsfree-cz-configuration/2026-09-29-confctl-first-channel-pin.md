# First pin for a new confctl flake channel

When `vpsadminWebui` was added to `vpsfree-cz-configuration`, its URL initially
pointed at `vpsfreecz/vpsadmin-webui` main. Main did not yet contain `flake.nix`.
`confctl inputs channel set` failed during its own Nix evaluation even when an
outer `nix develop` used `--override-input`; that override did not reach the
confctl subprocess. The existing `flake.lock` also had no node for the new
input, which `channel set` requires before it can construct a revision override.

The published feature branch already contained the flake. Declaring its branch
URL in `flake.nix` fixed source resolution without changing either default
branch. On the installed Nix 2.34.8, this read-only check succeeded before the
lock node existed:

```sh
nix eval --json --no-write-lock-file --no-update-lock-file .#confctl.channels
```

It warned that the missing input was resolved in memory and did not write the
lock. From the configuration worktree's declared `nix develop` environment,
`confctl inputs channel update --commit vpsadmin-webui vpsadmin-webui` then
created the first node through its owning channel. After inspecting the whole
lock diff, `confctl inputs channel set --commit vpsadmin-webui vpsadmin-webui
FULL_PUBLISHED_SHA` confirmed the exact revision. The set command made no
second commit because update had selected that SHA already. The generated lock
commit added only the root edge and WebUI node; its two input edges followed
the existing Nixpkgs and vpsAdmin inputs.

For another new channel, verify the published source contains a flake, use the
owning channel for the persistent lock update, and check the complete locked
revision and transitive graph. Do not edit `flake.lock` manually or assume an
outer Nix override applies inside confctl. If a hook or update fails after a
lock write, inspect the tracked diff and status before retrying or restoring
the task-owned change.

Related rollout: `work/2026-09-27-newadmin-integration/design.md`, section
"Initial WebUI channel lock bootstrap".
