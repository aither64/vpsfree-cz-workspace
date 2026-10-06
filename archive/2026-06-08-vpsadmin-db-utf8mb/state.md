---
lifecycle: abandoned
---
# 2026-06-08-vpsadmin-db-utf8mb

## Repositories

- `vpsadmin`
  - Bare repo: `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-08-vpsadmin-db-utf8mb/vpsadmin`
  - Branch: `2026-06-08-vpsadmin-db-utf8mb`
  - Base: `origin/master` at `bb38a42cd`

## Status

- Worktree prepared for review planning.
- No repository code changes made yet.
- Plan written for the utf8mb3-to-utf8mb4 migration tasks.

## Commands Run

- `bin/dev-session current`
  - Reused active slug `2026-06-08-vpsadmin-db-utf8mb`.
- `git --git-dir=repos/vpsadmin.git fetch origin`
  - Updated the bare vpsAdmin clone.
- `bin/dev-session worktree add 2026-06-08-vpsadmin-db-utf8mb vpsadmin --as-is --base origin/master`
  - Created the vpsAdmin worktree and feature branch.
  - The command exited non-zero because an Overcommit hook wrapper ran but the
    ambient shell did not have the `overcommit` gem. The worktree itself was
    created successfully and is clean. Hook setup must be fixed before any
    commit.
- `sed -n '1,260p' worktrees/.../vpsadmin/AGENTS.md`
  - Read repository-local instructions.
- `rg -n "utf8|utf8mb|charset|collation|encoding|mysql2|DATABASE_URL|Sequel|database.yml" ...`
  - Found current utf8mb3 production/test config and schema usage.
- Read relevant files:
  - `api/Rakefile`
  - `api/lib/vpsadmin/api/tasks/db.rake`
  - `api/lib/vpsadmin/api/tasks/db.rb`
  - `api/spec/support/db_setup.rb`
  - `nixos/modules/vpsadmin/api-app.nix`
  - `tests/configs/nixos/vpsadmin-services.nix`
  - `nixos/modules/vpsadmin/database.nix`
  - `nixos/modules/vpsadmin/database-setup.nix`
  - `nixos/modules/vpsadmin/api/rake-tasks.nix`
- `nix shell nixpkgs#mariadb nixpkgs#ruby --command ... tools/test-db start`
  - Started a scratch MariaDB 11.4.9 database on port `13317`.
  - The helper-started server exited after command completion, so a foreground
    `mariadbd` session was started for the SQL probes.
- SQL probes against scratch MariaDB 11.4.9:
  - Converted a test table from `utf8mb3_czech_ci` to `utf8mb4_czech_ci`.
  - Queried the converted table over a `utf8mb3_unicode_ci` connection.
  - Tested current runtime explicit collations:
    `COLLATE utf8_bin` and `COLLATE utf8_unicode_ci`.
  - Tested mixed old/new column comparisons.
  - Tested selecting a stored supplementary character over an `utf8mb3`
    connection.
  - Tested `ALGORITHM=NOCOPY, LOCK=NONE` for a simple conversion.
- User decision on 2026-06-14:
  - Do not consider a shadow-table/online-schema-change fallback.
  - Native MariaDB online DDL only.
- `mariadb-admin --host 127.0.0.1 --port 13317 --user root shutdown`
  - Stopped the scratch MariaDB server.
- Browsed MariaDB documentation:
  - `SET NAMES`
  - `Unicode`
  - `ALTER TABLE`
  - `InnoDB Online DDL Operations with the INPLACE Alter Algorithm`
- `nix eval --raw github:NixOS/nixpkgs/nixos-26.05#mariadb.version`
  - Reported `11.4.9`.

## Results

- Current production database config explicitly uses `utf8mb3` and
  `utf8mb3_unicode_ci`.
- Current local test database setup uses the same defaults.
- Core schema dump uses `utf8mb3_czech_ci`; plugin tables must be handled from
  live metadata.
- Runtime explicit `utf8` collations are limited to:
  - password login lookup,
  - user search filters.
- Local MariaDB 11.4.9 accepted a converted `utf8mb4` table with the old
  `utf8mb3` connection and the runtime explicit-collation query shapes.
- A four-byte character stored in `utf8mb4` was returned as `?` over an
  `utf8mb3` connection. This confirms the final connection switch must happen
  before allowing/expecting supplementary characters.
- A simple conversion accepted
  `ALGORITHM=NOCOPY, LOCK=NONE` on MariaDB 11.4.9.
- Revised DDL default after review: use explicit `LOCK=NONE`, but leave
  `ALGORITHM` at MariaDB's default so MariaDB 11.4 can choose online copy when
  needed. Stop if `LOCK=NONE` is not supported.
- Review answer on 2026-07-04:
  - Preserve current production collation families is the lowest-risk DB
    migration:
    `utf8mb3_czech_ci` -> `utf8mb4_czech_ci` and
    `utf8mb3_unicode_ci` -> `utf8mb4_unicode_ci`.
  - However, `utf8mb4_czech_ci` is deployment-specific and strange as a neutral
    upstream `schema.rb` default. Split this from the charset migration
    decision.
  - For neutral project defaults, prefer `utf8mb4_unicode_ci` unless a separate
    review intentionally chooses a newer UCA collation. Do not choose
    `utf8mb4_general_ci` as the new neutral default.
  - `utf8mb3` connections can access `utf8mb4` tables for existing/BMP data,
    because the connection repertoire is a subset of `utf8mb4`.
  - Emoji/user-data support needs both `utf8mb4` storage and an `utf8mb4`
    application connection.

## Open Questions

- None currently.

## Cleanup

- Scratch MariaDB foreground session was stopped.
- Worktree should be removed after merge or abandonment.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
