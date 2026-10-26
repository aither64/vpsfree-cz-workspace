# Hook preparation

Owner: implementer0. Scope: repair the existing HaveAPI checkout's hook setup
without bypassing hooks or changing source. Source backports wait for the
architect's accepted design.

## Identity and existing effects

- `dev-session current` returned `2026-10-25-haveapi-backport-release`.
- `DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE` both match the exact thread
  binding, including `/home/aither/workspace/ai/vpsfree.cz`.
- Existing checkout:
  `worktrees/2026-10-25-haveapi-backport-release/haveapi`.
- Branch: `2026-10-25-haveapi-backport-release`.
- HEAD: `1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`.
- Checkout and index were clean after the failed checkout hook.
- The portal already recorded this branch and exact `initial_base_sha`.
  No branch or checkout recreation is needed.

## Reviewed setup

Read the workspace and repository instructions, routed setup/release procedures,
`.overcommit.yml`, both custom pre-commit hooks and the repository's Nix shell.
The configured custom checks invoke i18n health and Python formatting/linting;
RuboCop and PHP CS Fixer are also enabled. Existing common Git hooks are the
normal executable Overcommit entrypoints; no `core.hooksPath` override was set.

The existing [worktree signature lesson](../../notes/haveapi/2026-10-12-worktree-hook-signature.md)
documents installation and signing inside the Nix shell followed by the normal
registration retry. No source or hook configuration edit is planned.

## Environment preparation

The fresh `hook_environment_setup` verification utility owns one Nix shell
dependency-preparation command. Its pinned catalog digest is
`840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa`;
the utility uses `gpt-6-luna` / `low` and the installed full-access policy.
The corresponding native utility is
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`.
Its complete log is `hook-environment-setup.log` in this tracking directory.

`nix develop -c true` passed (exit 0, approximately 42 seconds), installing
Bundler 4.0.23 and the 33 declared gems. The watcher observed no kernel build.
Its compact receipt is `hook-environment-setup-result.json`.

## Repair and verification

With dependencies prepared, ran these commands successfully in the top-level
Nix environment with `HAVEAPI_RELEASE_TOOLS_ONLY=1` to reuse prepared inputs:

```sh
bundle exec overcommit --install
bundle exec overcommit --sign
bundle exec overcommit --list
git hook run post-checkout -- \
  1c3c98f0d77e0b23c8da1a8937f25c5799864a3b \
  1c3c98f0d77e0b23c8da1a8937f25c5799864a3b 1
```

The ordinary retry also passed:

```sh
dev-session worktree add 2026-10-25-haveapi-backport-release haveapi \
  --as-is --branch 2026-10-25-haveapi-backport-release \
  --base origin/haveapi-0.30 --no-fetch
```

The resulting manifest records `haveapi-0.30` as the target and preserves the
exact initial base. Final HEAD remains
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`; checkout and index remain clean.
Overcommit signature verification remains enabled (`1`) and the configuration
and both custom-hook signatures are present. No hooks were bypassed, no source
files changed and no project commit, push, integration or publication occurred.

Preparation is complete. Next: accepted architect design and lead assignment
for the serialized source backports. This evidence follows the existing setup
lesson, so no new reusable project documentation is needed for this repair.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/>
