# Rebase after changing Overcommit configuration

Related initiative: `work/2026-06-15-vpsadmin-events`.

## Symptom

Rebasing a configuration feature branch failed first because the ambient
shell could not load the bundle for the pre-rebase hook. After installing the
bundle, replay stopped again when a historical commit changed
`.overcommit.yml`: the `prepare-commit-msg` hook rejected the now-stale
signature.

`git commit --no-verify` does not bypass `prepare-commit-msg`.

## Workaround

Install and sign hooks in the repository development shell:

```sh
nix develop -c bundle install
nix develop -c bundle exec overcommit --sign
```

For an explicitly authorized history reconstruction, replay the affected
historical commit with hooks disabled through Git's hook path, then continue
the rebase the same way. Do not use this for new or final commits.

After the rewritten branch reaches its final tree, sign the current
configuration again and run the complete hook suite normally:

```sh
nix develop -c bundle exec overcommit --sign
nix develop -c bundle exec overcommit --run
```

The event-system configuration rewrite passed its final Nixfmt, RakeTarget,
and RuboCop hooks after this sequence.
