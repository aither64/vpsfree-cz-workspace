# vpsadminos commit hooks need the Nix development shell

## Command and symptom

Running `git commit -F <message-file>` in the ambient shell invoked Overcommit,
but its Nixfmt hook failed with `nixfmt: command not found`.

## Cause

The hook framework was installed and active, but the formatter is supplied by
the repository's Nix development shell rather than the ambient user profile.
An earlier explicit `nix develop --command overcommit --run` passed because it
had the required tool environment.

## Fix and verification

Run the commit itself inside the development shell:

```sh
nix develop --command git commit -F <message-file>
```

Do not bypass the hook after a successful explicit run; the commit-time hook is
still mandatory. See `work/2026-07-21-system-install-failure/`.
