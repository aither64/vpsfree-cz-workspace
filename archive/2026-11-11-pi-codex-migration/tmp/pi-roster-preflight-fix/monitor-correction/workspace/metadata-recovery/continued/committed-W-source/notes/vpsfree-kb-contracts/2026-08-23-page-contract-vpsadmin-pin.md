# vpsAdmin pin in the KB page contract

## Symptom

After updating the vpsAdmin revision in `flake.nix`, `flake.lock`,
`captures.json`, and `contract/navigation.yml`, `nix develop -c bin/check`
failed with `vpsadmin revision differs`.

## Cause

`tools/check-page-contract.rb` also requires `revisions.vpsadmin` in
`contract/pages.yml` to match the locked vpsAdmin input and capture metadata.
The canonical WebUI change workflow did not list this pin.

## Fix and verification

Update `contract/pages.yml` whenever the exact vpsAdmin contract revision is
changed. Initiative `work/2026-08-23-vpsadmin-outage-summary` also corrects
`docs/webui-change-workflow.md` to list the field. Rerun
`nix develop -c bin/check` after all revision metadata is aligned.
