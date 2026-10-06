# 2026-07-16-codex-lb-update

## Follow-up: 2026-07-19 default-branch snapshot

### Goal

Update the codex-lb instance configured on aitherdev from release `1.21.0` to
the latest commit in upstream's default `main` branch.

### Approach

1. Resolve and pin the current `main` commit and source hash.
2. Keep the published `1.21.0` image as the runtime dependency base because
   upstream has not published a default-branch image and runtime Python
   dependencies have not changed since `1.21.0`.
3. Pin Bun2nix as a direct flake input and pin upstream's required Bun 1.3.14
   binary. Generate the frontend dependency closure from the exact upstream
   lock file, build the frontend, overlay the complete application,
   configuration, script, and generated frontend files on the base image, and
   produce a locally named OCI image through Nix.
4. Point aitherdev's declarative container at the Nix-built image. Do not
   publish an invented upstream tag or rely on a mutable/preloaded local
   image.
5. Format and build the image and complete aitherdev configuration, commit the
   focused change, and run mandatory standalone review before final
   integration validation.

### Compatibility and deployment

- The target source contains seven Alembic migrations after `1.21.0`, so the
  explicit verified SQLite backup, post-start migration check, and rollback
  procedure below remains mandatory before any deployment. Name the backup
  `store.pre-git-9b40f746-<UTC timestamp>.db`, record the exact created path,
  and use only that verified file for this deployment's rollback.
- Runtime Python dependencies are unchanged between `v1.21.0` and the target
  commit. Reusing the pinned release runtime image therefore preserves the
  exact Python environment while replacing all application, configuration,
  script, and frontend files from the target source.
- Bun2nix is a direct channel input rather than an implementation detail of
  `llm-agents`, so routine `llm-agents` input updates cannot silently change
  the image builder. Bun itself is pinned to the version required by the
  upstream frontend.
- No application/configuration/script files were deleted between `v1.21.0`
  and the target commit, so an OCI overlay cannot expose removed stale code
  from the base image.
- Upstream CI for the target commit passed its Docker build, packaging,
  frontend/backend tests, type checks, and migration checks. The aggregate run
  is red only because the architecture line-budget check reports 2,604 lines
  against a 2,600-line limit.
- The change remains configuration-only until explicitly deployed. Mixed
  versions do not communicate with one another, but rollback to the exact
  digest-pinned `1.21.0` image/configuration still requires restoring the
  recorded `store.pre-git-9b40f746-*` database because `1.21.0` cannot be
  assumed to load the target commit's schema.

### Testing plan

- Verify the source pin still matches upstream `main` immediately before the
  final commit.
- Build the reproducible frontend derivation and OCI image.
- Inspect the loaded image metadata and assert that target-only backend,
  migration, script/configuration, and frontend files are active beneath
  `/app`.
- Exercise the upgrade from a disposable database created by the pinned
  `1.21.0` image, including verified backup, target migration/check, and
  restore followed by the `1.21.0` migration check.
- Run Nix formatting, repository hooks, whitespace checks, and a full
  `confctl build -y cz.vpsfree/machines/aitherdev`.
- Run mandatory standalone review after the intended commit and quick checks.

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
- Deployment order: merge the configuration/input commits, but before
  deploying aitherdev use the currently running container's Python `sqlite3`
  backup API to copy `/var/lib/codex-lb/store.db` to a unique
  `/var/lib/codex-lb/store.pre-git-9b40f746-<UTC timestamp>.db` inside
  `codex-lb-data`. Record the exact created path. Run `PRAGMA quick_check` on
  that backup and verify that it returns `ok` and the file is non-empty. Abort
  deployment if creation or verification fails. This online backup is an
  explicit operator step; no deployment is part of this initiative.
- After activation, require `podman-codex-lb.service` to remain active, inspect
  its entrypoint output for the resulting `current_revision`, and run
  `podman exec codex-lb python -m app.db.migrate check`. Accept the deployment
  only when it prints `migration_policy=ok` and `schema_drift=none`, and the
  codex-lb endpoints respond normally.
- Reverting only the image is not a reliable codex-lb rollback because
  `1.21.0` cannot be assumed to load schema revisions created by commit
  `9b40f746`. To roll back, stop the service, use
  `podman volume inspect codex-lb-data` to locate the volume, preserve the
  failed upgraded `store.db` and sidecars, restore the exact recorded and
  verified `store.pre-git-9b40f746-*.db` as `store.db` with matching
  ownership/mode, remove stale `store.db-wal` and `store.db-shm` while the
  service is stopped, activate the exact prior digest-pinned `1.21.0`
  configuration, and start the service. This is deliberate operator action,
  not an automatic configuration rollback.

## Testing plan

- Validate workflow YAML and exercise its version-detection logic locally.
- Reproduce the failing nested Bundix update with the flake dev shell and a
  writable runner-style Bundler configuration.
- Run repository hooks for all committed changes.
- Evaluate/build the aitherdev configuration with `confctl`.
- Inspect GitHub Actions after pushing if a branch push is requested or needed
  for CI feedback.
