# Dev-cluster notification-template reconciliation

## Symptom

Updating a vpsAdmin development cluster after the declarative notification
template migration failed in the seed service with
`undefined method 'params' for DirectoryTemplate`. The API and recovery worker
then failed because both depend on a successful seed.

## Cause

`dev-clusters/vpsadmin/nix/test.nix` duplicated the former loader internals and
expected template-level `params` and `translations` objects. The current loader
parses channel variants and exposes reconciliation through a public API, so the
legacy seed no longer matched its data model.

## Fix

Seed every configured external package with
`VpsAdmin::API::MailTemplates.reconcile!(path: path, source_id: path)`. This is
the same transactional reconciliation path used by deployed systems and keeps
the development fixture aligned with future loader changes.

External installation requires the reconciler introduced by vpsAdmin commit
`ea956e5e` and the declarative `templates/` package layout. Nix evaluation
checks both requirements before building the cluster. Set
`mail.templates.install` to `false` in the cluster config when running an older
vpsAdmin and template pair; the seed then leaves existing database templates
unchanged.

## Verification

Nix parsing and `git diff --check` passed. Re-running the bridge-cluster
services update reconciled the external package, completed the seed with status
0, and started both the API and password-recovery worker. Database inspection
confirmed both languages and expected variants from the external store path.

Related initiative: `work/2026-08-18-vpsadmin-password-reset/`.
