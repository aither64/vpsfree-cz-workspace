# Candidate deployment admission: schema 2 supported

Updated 2026-11-04. **The previous static-catalog blocker is superseded.**
The user already authorized agent deployment of VPS27627/private172.19.9.22.
Current workspace docs and `workspace-host coordination guide` select package
`/nix/store/myjy32qh6bd4avgym1awx180y29nvwz9-dev-workspace-0.2.0`, which supports
schema-2 claims resolved from exact registered configuration machines. No static
catalog edit, workspace source project or additional deployment approval is needed.

Lead owns claim acquisition and activation. Use a fresh requestId with schema=2,
repositories=[] and this one machines entry:

```json
{
  "repository": "vpsfree-cz-configuration",
  "selector": "cz.vpsfree/containers/mx2",
  "adapter": "confctl"
}
```

The selector is exact configured Machine.name, not `mx2`, an IP or a physical-node
assumption. The canonical repository is
`git@github.com:vpsfreecz/vpsfree-cz-configuration.git`. Absent a configured shared
lock-id, its logical identity displays as
`machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/containers/mx2`.
The runtime resolves the registered feature branch's committed revision with local
locked inputs, without target probes, builds, fetches or lockfile writes. A claim
request cannot override its source path/revision/label. Do not use aitherdev or a
legacy catalog alias as a surrogate.

After preparation, lead acquires near activation, checks authoritative held status,
and runs the supported `workspace-host coordination verify-machine` for this
session, owned claim ID, repository and selector once before the intended committed
batch. Owner0 refreshes the already built084488 candidate/output4pc5 and native
generation/SSH/recovery receipts; this documentation update neither claims those
checks ran again nor creates new implementation/review/build work. Ordinary
single-target copy/dry-activate/switch and exact installed-system verification
follow under the original deployment authorization.

The rollout remains restricted to candidate27627/private172.19.9.22 and at most
two marked podpora normal/temporary-queue messages. Preserve old98n9 rollback,
trusted SSH, queue safety and complete source/input/generation evidence. Old
CentOS, primary configuration, public IP/DNS changes, default integration and
session lifecycle remain excluded. Retain ownership for uncertain effects or
missing integrated-lineage proof; release follows the installed policy.

Architect only read current guidance and updated these session records. No claim,
candidate probe, build, source/Git mutation, runtime change or activation occurred
in this documentation task. The earlier same-session-lock assignment failure had
no task effects according to lead; this update is the successful documentation retry.

## Historical admission assessment (superseded; do not execute its proposal)

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
