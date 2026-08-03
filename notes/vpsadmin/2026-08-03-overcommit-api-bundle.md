# Prepare the API bundle before running vpsAdmin's root hooks

## Symptom

`nix develop -c bundle exec overcommit --run` failed in
`VpsadminApiI18n` with `Bundler::GemNotFound` for Active Record, while the
other root hooks passed.

## Cause

The custom hook changes into `api/` and selects `api/.gems`, but a fresh
worktree has not populated that component bundle. Invoking Overcommit through
`bundle exec` also restores `RUBYOPT=-rbundler/setup` for hook children, which
can make them retain the root bundle before the hook's environment overrides
take effect.

## Workaround

Populate the API component bundle, then invoke the executable with `RUBYOPT`
unset:

```sh
nix develop .#api -c bundle check
nix develop -c env -u RUBYOPT overcommit --run
```

The API shell automatically runs `bundle install` when it starts. For the
actual commit, retain the same environment isolation:

```sh
nix develop -c env -u RUBYOPT git commit -F MESSAGE_FILE
```

## Verification

After `api/.gems` was populated, all six declared pre-commit hooks passed,
including `VpsadminApiI18n`.

Related initiative:
`work/2026-08-03-webui-dataset-used-czech-fix/`.
