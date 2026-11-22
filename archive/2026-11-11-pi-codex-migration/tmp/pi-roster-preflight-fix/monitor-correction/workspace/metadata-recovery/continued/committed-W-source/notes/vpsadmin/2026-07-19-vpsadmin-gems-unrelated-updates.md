# `vpsadmin:gems` can refresh unrelated unlocked dependencies

## Symptom

Running `nix develop -c rake vpsadmin:gems` before a development-cluster
rebuild changed `concurrent-ruby` from 1.3.7 to 1.3.8 in the API, client, and
download-mounter package lockfiles and generated gemsets, even though the
initiative changed only API source code.

## Cause

The task resolves the package bundles against the current RubyGems index. An
unconstrained transitive dependency can therefore advance while the task is
regenerating package inputs.

## Workaround

Inspect the worktree immediately after `vpsadmin:gems`. Preserve generated
changes required by the initiative, but restore unrelated dependency drift to
the committed versions before building the development cluster. Dependency
updates should remain separate reviewable commits.

## Verification

For `work/2026-07-13-security-advisory-automation`, restoring only the three
lockfile/gemset pairs left the vpsAdmin worktree clean and `git diff --check`
passed.
