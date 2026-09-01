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

Configure every external package through
`vpsadmin.api.notificationTemplates` in `replace` mode. The upstream
`vpsadmin-notification-templates.service` builds the effective package and
uses the public transactional reconciler before the API or supervisor starts.
The development cluster no longer duplicates that work in its seed.

External installation requires authoritative notification-template mode,
introduced by vpsAdmin commit `cbd0fa16`, and the declarative `templates/`
package layout. Nix evaluation checks both requirements before building the
cluster. Set
`mail.templates.install` to `false` in the cluster config when running an older
vpsAdmin and template pair; the cluster then uses bundled defaults instead of
reconciling the external worktree.

## Verification

Nix parsing and `git diff --check` passed. Re-running the bridge-cluster
services update reconciled the external package through the upstream one-shot
service, completed the seed with status 0, and started both the API and
password-recovery worker. Database inspection confirmed both languages and
expected variants from the effective replacement package.

Related initiative: `work/2026-08-18-vpsadmin-password-reset/`.
