# 2026-06-09-github-workflow-versions

## Goal

Audit GitHub workflow files across the vpsFree.cz development workspace and
upgrade stale `actions/*` imports to the latest upstream major versions. Update
the top-level workspace instructions so future workflow edits verify action
versions from upstream instead of relying on memory.

## Affected repositories

- Workspace root:
  - `AGENTS.md`
- Workflow updates:
  - `confctl`
  - `haveapi`
  - `terraform-provider-vpsadmin`
  - `vpsadmin`
  - `vpsadminos-org-configuration`
  - `vpsfree-cz-configuration`
- Scanned with no changes required:
  - `haveapi-client-php` (no workflows on default branch)
  - `ruby-lxc`
  - `ssh-exporter`
  - `syslog-exporter`
  - `vpsadmin-go-client`
  - `vpsadminos`
  - `vpsf-status`
  - `vpsfree-client`
  - `vpsfree-irc-bot`
  - `vpsfree-mail-templates`
  - `vpsfree-maintenance-tasks`
  - `web`
- Explicitly skipped by user request:
  - `zfs`
  - `linux`

## Approach

1. Fetch all canonical bare repositories.
2. Scan default-branch `.github/workflows` for `uses: actions/...@...`.
3. Verify latest action tags from official `actions/*` repositories.
4. Create per-repository worktrees on branch
   `2026-06-09-github-workflow-versions`.
5. Update only stale action refs:
   - `actions/checkout@v4` to `actions/checkout@v6`
   - `actions/setup-go@v5` or pinned v5.1.0 SHA to `actions/setup-go@v6`
   - `actions/setup-node@v4` to `actions/setup-node@v6`
   - `actions/cache/{restore,save}@v4` to `@v5`
   - `actions/upload-artifact@v4` to `@v7`
   - `actions/download-artifact@v4` to `@v8`
6. Leave non-`actions/*` workflow actions unchanged.

## Compatibility and deployment

This is CI-only workflow metadata plus workspace documentation. It does not
change runtime code, persisted state, database schemas, API contracts, NixOS or
vpsAdminOS module options, generated deployment configuration, or rollback
behavior.

The changes can be merged independently per repository. No coordinated update
of running machines or vpsAdminOS nodes is required.

## Testing plan

- Run a post-edit scan of all non-`zfs/linux` project workflows and confirm all
  `actions/*` refs are on the selected latest major aliases.
- Run `git diff --check` in every changed repository worktree and for the
  top-level `AGENTS.md` edit.
- Run `actionlint` through Nix for the changed workflow files. If full
  repository lint fails on pre-existing ShellCheck findings, record the
  unrelated findings in `state.md` and run scoped workflow-structure lint with
  ShellCheck disabled.
