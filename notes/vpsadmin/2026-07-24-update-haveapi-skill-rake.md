# vpsadmin-update-haveapi uses a removed bundix script

Initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix/`

## Symptom

Running the repository skill command

```sh
nix develop -c skills/vpsadmin-update-haveapi/scripts/update_haveapi.py 0.29.5
```

fails with `error: could not find vpsAdmin repository root`.

## Cause

The skill identifies the repository by requiring
`tools/bundix_all.sh` and later invokes that script. Commit `8db0f9a54`
removed the script when gem metadata updates moved to Rake, but the skill was
not updated.

## Workaround

Apply the five source dependency updates listed in the skill, then use the
current repository workflow:

```sh
nix develop . --command rake vpsadmin:gems
```

Review the generated diff and rerun the command to verify it is idempotent.
This produced clean RubyGems-backed HaveAPI 0.29.5 metadata in the related
initiative.
