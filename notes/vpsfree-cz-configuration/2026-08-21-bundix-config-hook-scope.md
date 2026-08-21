# Scope Bundix's application config away from Git hooks

## Symptom

The daily update workflow generated a package lockfile and gemset successfully,
then failed when committing them. Overcommit could not find the repository's
root development and lint gems. Runs without a changed package lockfile passed
or failed elsewhere, so the package commit path could remain broken unnoticed.

## Cause

Bundix needs a writable Bundler path because it removes `BUNDLE_PATH` before
invoking Bundler. The workflow provided that path through a temporary
`BUNDLE_APP_CONFIG`, but exported the variable to the parent shell. The Nix
development shell normally points the same variable at the repository's root
`.bundle` config and `.gems` path. Later `git commit` hooks therefore inherited
the package-only config and could not load Overcommit or the root lint bundle.

## Fix

Keep the temporary config, but pass `BUNDLE_APP_CONFIG` only to
`bundle config set` and `bundix -l`. Do not export it across later Git commands.
This preserves Bundix's writable package cache while repository hooks continue
to use the root development bundle.

## Verification

Generate a representative package lockfile and gemset in a temporary directory
under the scoped config, then run root `bundle check` and Overcommit in the same
parent shell. The hosted workflow should also create at least one package
dependency commit, pass its hooks, push the result, and save the cache.

This was verified by GitHub Actions run `32521846985`, which committed updates
for geminabox, ssh-exporter, and syslog-exporter and passed every hook.

Related initiative: `work/2026-08-10-vpsfconf-daily-update/`.
