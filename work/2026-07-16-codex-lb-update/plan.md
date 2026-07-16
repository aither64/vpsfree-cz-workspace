# 2026-07-16-codex-lb-update

## Goal

Update the codex-lb container deployed on aitherdev to the latest upstream
release, determine why the daily llm-agents input update no longer advances
when Codex changes, repair the automation, and allow operators to launch the
same workflow on demand.

## Affected repositories

- `vpsfree-cz-configuration`

## Approach

1. Verify the latest codex-lb release and refresh its pinned container image.
2. Inspect the current llm-agents lock, upstream Codex version, workflow logic,
   recent workflow runs, and relevant repository history.
3. Fix the updater while preserving `confctl inputs` as the only mechanism for
   changing flake inputs.
4. Keep the generated llm-agents input update separate from functional changes.
5. Preserve the workflow's atomic final push: if a later update fails, discard
   all updates from that run rather than pushing partial results.
6. Add Bundix to the repository's flake dev shell and run the package refresh
   through `nix develop`; do not introduce legacy `nix-shell` invocations.
7. Add a manual workflow trigger without changing the scheduled job behavior.
8. Run quick workflow/configuration checks, commit the changes, obtain the
   mandatory standalone change review, then run the relevant aitherdev build.

## Compatibility and deployment

- The codex-lb data volume is persistent and `1.21.0` applies Alembic schema
  migrations at startup. Its container entrypoint calls
  `python -m app.db.migrate upgrade` and then disables the application-level
  startup migration path. The CLI path does **not** create the automatic SQLite
  backup or emit the migration-complete/drift-check logs implemented by
  `app/db/session.py`; deployment must not rely on those safeguards.
- The llm-agents change only updates a flake input consumed by aitherdev. Mixed
  versions are not a protocol concern, but the resulting aitherdev evaluation
  and build must succeed before deployment.
- The workflow fix affects only future repository automation. It must remain
  compatible with GitHub-hosted runners, repository permissions, and the
  repository's `confctl` commit/push flow. Scheduled and manual runs share the
  same job and its final push remains atomic.
- Deployment order: merge the configuration/input commits, but before deploying
  aitherdev use the currently running container's Python `sqlite3` backup API to
  copy `/var/lib/codex-lb/store.db` to a unique
  `/var/lib/codex-lb/store.pre-1.21.0-<UTC timestamp>.db` inside
  `codex-lb-data`. Run `PRAGMA quick_check` on the new backup and verify that it
  returns `ok` and the backup is non-empty. Abort deployment if creation or
  verification fails. This online backup is an explicit operator step; no
  deployment is part of this initiative.
- After activation, require `podman-codex-lb.service` to remain active, inspect
  its entrypoint output for the resulting `current_revision`, and run
  `podman exec codex-lb python -m app.db.migrate check`. Accept the deployment
  only when it prints `migration_policy=ok` and `schema_drift=none`, and the
  codex-lb endpoints respond normally.
- Reverting only the image is not a reliable codex-lb rollback because the old
  version can reject a schema revision created by `1.21.0`. To roll back, stop
  the service, use `podman volume inspect codex-lb-data` to locate the volume,
  preserve the failed upgraded `store.db` and sidecars, restore the selected
  verified `store.pre-1.21.0-*.db` as `store.db` with matching ownership/mode,
  remove stale `store.db-wal` and `store.db-shm` while the service is stopped,
  activate the reverted image configuration, and start the service. This is
  deliberate operator action, not an automatic configuration rollback.

## Testing plan

- Validate workflow YAML and exercise its version-detection logic locally.
- Reproduce the failing nested Bundix update with the flake dev shell and a
  writable runner-style Bundler configuration.
- Run repository hooks for all committed changes.
- Evaluate/build the aitherdev configuration with `confctl`.
- Inspect GitHub Actions after pushing if a branch push is requested or needed
  for CI feedback.
