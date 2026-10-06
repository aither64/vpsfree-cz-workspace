# 2026-08-31-vpsadmin-notifications

## Goal

Make notification templates a declarative, build-time input to vpsAdmin. A
custom deployment should provide only template data, while vpsAdmin owns the
parser, validation, packaging, reconciliation, Nix helpers and reusable CI.
Rename the vpsFree.cz data repository to
`vpsfree-notification-templates` and consume its flake from production
configuration. Do not integrate vpsAdmin events.

## Affected repositories

- `vpsadmin`
- `vpsfree-notification-templates`
- `vpsfree-cz-configuration`

All project repositories use branch `2026-08-31-vpsadmin-notifications` and
worktrees below `worktrees/2026-08-31-vpsadmin-notifications/`.

## Template contract

Template providers supply only this data structure:

```text
templates/<name>/meta.rb
templates/<name>/email/<language>.subject.erb
templates/<name>/email/<language>.text.erb
templates/<name>/email/<language>.html.erb
```

`meta.rb` declares the template identity, label, visibility and sender
addresses. A metadata subject may remain as a fallback. The localized subject,
plain-text body and HTML body otherwise live together below `email/`.

vpsAdmin provides:

- a strict parser and checker for the data contract;
- flake helpers that package a template tree and expose checks/apps;
- an effective package that combines bundled core templates, plugin templates
  and an optional deployment overlay;
- a reusable GitHub Actions workflow;
- a NixOS option and one-shot service that reconcile the effective package
  into the existing mail-template database tables.

The vpsFree.cz repository is a thin caller: template data, a flake invoking the
vpsAdmin helper, and a workflow invoking vpsAdmin's reusable workflow.

## Reconciliation behavior

- The effective package's immutable Nix store path is the source identity.
- The package is parsed and reconciled transactionally before the API and
  supervisor start.
- Templates present in the effective package are created or repaired even if
  database content drifted. An unchanged, undrifted source produces no
  database writes.
- Removing a deployment override while keeping the source configured exposes
  the bundled default again, so the next package identity restores it.
- Database rows that do not belong to the effective package are preserved.
- Setting the source option to `null` disables external reconciliation and
  leaves the last database values in place.
- The standalone uploader and its manual/API-based installation workflow are
  removed. Existing `/mail_templates` API resources remain unchanged.

## Compatibility and deployment

- No database migration, API schema, daemon protocol or event-system code is
  included. Existing mail-template tables and API resources are retained.
- The filesystem contract is intentionally incompatible with the old
  repository layout. Legacy `.plain.erb` paths and the standalone uploader are
  no longer supported; template repositories must adopt `email/` and the new
  suffixes.
- The renamed database-setup option retains a Nix renamed-option alias.
- Old and new API processes can read the same persisted rows. Only `int.api1`
  receives the external template source and reconciles the shared database;
  `int.api2` does not.
- A rollback to old vpsAdmin code can still read the database because the
  schema is unchanged, but old tooling cannot consume the new filesystem
  layout. Roll back configuration and package pins together if the template
  source must be reconciled by an older generation.
- No vpsAdminOS node or machine-wide coordinated update is required.
- Production deployment and branch integration are out of scope and remain
  operator-run after review.

## Verification plan

- Compare converted metadata, subjects, bodies and symlink targets with their
  legacy sources; permit only removal of semantically empty language blocks.
- Run parser/importer specs, RuboCop, CI-selection tests, all repository hooks,
  and focused Nix checker/effective-package builds.
- Run the external repository's flake checks and checker app against the exact
  pushed vpsAdmin revision.
- Generate configuration pins only through `confctl`, verify exact lock
  identities, and evaluate API1, API2 and vpsfbot system derivations.
- After commits and quick verification, run the mandatory standalone
  fresh-context review before long configuration builds.
- Build API1, API2 and vpsfbot, inspect generated units, and monitor all
  current-head GitHub Actions. Do not deploy or merge.
