# MkDocs is not in the configuration development shell

Related initiative: `work/2026-08-06-node-kernel-history/`

## Symptom

`nix develop -c mkdocs build --strict` enters the documented configuration
development shell but fails with `mkdocs: not found`.

## Cause

The configuration development shell provides `confctl` and repository hook
tools, but does not currently include MkDocs even though the repository owns an
`mkdocs.yml` documentation site.

## Workaround

Run the documentation build with the package explicitly supplied:

```shell
site_dir=$(mktemp -d)
nix shell nixpkgs#mkdocs -c mkdocs build --strict --site-dir "$site_dir"
```

## Verification

The strict build passed for the livepatch-history deployment runbook on
2026-08-07.
