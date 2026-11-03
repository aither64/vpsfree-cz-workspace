# Candidate deployment admission prerequisite

The user authorized deployment of VPS27627 at172.19.9.22. SSH trust/root access
work, and the private staging candidate is committed/reviewed at08448817. The
existing original system remains installed; no new activation has occurred.

The selected workspace package is
/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0.
Its immutable coordination catalog lists only aitherdev. It contains no mx2,
VPS27627, private172.19.9.22 or verified physical-node alias. The selected guide
requires configured-machine ownership for deployment and documents no dynamic
machine-registration command or guest-only exception. Reserving aitherdev as a
surrogate would not reserve this candidate.

Relevant [installed coordination guide](/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0/share/dev-workspace/coordination.md):

> Machines still require configured names, IDs or aliases.

> Run the shared mutation only while the exact claim is held.

## Proposed separate workspace change

Add one ordinary configured-machine entry in the workspace's
config/coordination.nix, retaining all existing mappings:

```nix
machines.mx2 = {
  id = "vpsfree:ct:27627";
  aliases = [
    "172.19.9.22"
    "cz.vpsfree/containers/mx2"
  ];
  adapter = "confctl";
  configurationRepository = "vpsfree-cz-configuration";
  selector = "cz.vpsfree/containers/mx2";
};
```

This is a proposal, not an active registration or a source edit. It identifies
only the confirmed guest, without claiming unverified physical placement.
Prepare/check/review the workspace feature in its own worktree, build the user
package and activate it through the supported workspace package workflow. That
would update the shared workspace user package on aitherdev; it does not require
a NixOS host configuration deployment, public DNS or CentOS changes.

That additional workspace package activation is outside the user's exact mx2
deployment authorization and needs explicit direction. Default integration of
either repository remains separately unapproved. Once the candidate mapping is
active, acquire/verify exact candidate ownership near activation, dry-activate
then switch the reviewed built mx2 generation and verify its effects. Machine
holds follow the normal deployment/integrated-lineage retention rules.

The alternative is operator deployment of the exact prepared candidate through
their own workflow. The agent must not bypass its machine-ownership rule.
