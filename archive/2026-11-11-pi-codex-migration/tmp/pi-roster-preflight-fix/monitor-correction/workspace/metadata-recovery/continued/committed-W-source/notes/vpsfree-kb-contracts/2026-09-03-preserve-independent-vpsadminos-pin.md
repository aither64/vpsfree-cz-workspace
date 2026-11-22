# Preserve the contract-owned vpsAdminOS input when updating vpsAdmin

## Symptom

Running `nix flake update vpsadmin` changed the contract's independently
advanced `vpsadminos` input from `6bdf458f` to the older `8e44a512` revision
followed by vpsAdmin. Static contract checks could be made consistent with the
downgraded lock, but managed-page runtime tests then lacked retry APIs provided
by the intended vpsAdminOS test framework.

## Cause

The contract flake follows vpsAdmin's transitive vpsAdminOS input. A focused
flake update can therefore rewrite the followed lock node even when
vpsAdminOS was deliberately advanced independently for contract test support.

## Workaround

Before updating vpsAdmin, compare the vpsAdminOS lock closure and page-runtime
action references with the base revision. Preserve or reapply the exact
contract-owned vpsAdminOS revision and its related nixpkgs nodes, then update
only the vpsAdmin pin. Run runtime-aware contract checks; matching lock and
workflow references alone does not prove that the required test APIs exist.

## Verification

The related initiative restored vpsAdminOS `6bdf458f` and its original lock
closure, retained only the new vpsAdmin revision, and rebuilt the screenshot
cluster against that combination before recapturing affected checkpoints.

Related initiative: `work/2026-09-03-webui-vps-ipv6/`.
