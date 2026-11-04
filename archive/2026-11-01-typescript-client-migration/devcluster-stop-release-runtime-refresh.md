# Stop/Release authority refresh — 2026-11-04

The prior [preparation](devcluster-stop-release-preparation.md) remains intact
at SHA256 `e8ac6275a994f5f3da508d868b2b2539b11461a5551a92c58754ccab9feaa0c9`.
This supplement rebinds its authority and current ownership. No cluster or
session lifecycle mutation was performed. WebUI merge and released merge claim
remain parent prerequisites for actual execution.

Selected runtime is `/nix/store/hyjxg06wbz3z7jm62338a3s3s18hn66w-dev-workspace-0.2.0`,
coordination catalog `775fe9cf6ad9c2d99088359ffd37d0cbdbc23fc9d3fb38524e2f06238541ea81`.
The public selected extension catalog points to provider
`/nix/store/hya6sqxjdzpjnp9c41yxksdvrpjbhpv5-vpsfree-dev-workspace-tools-0.1.0`.
Its README at `share/vpsfree-dev-workspace/dev-clusters/vpsadmin/README.md`,
CLI implementation, shared ownership runtime and shutdown budgets are byte-identical
to the prior provider. Existing full README reading therefore remains applicable.

Current immutable runtime source is
`/nix/store/ipd26pw75apgx5l303xnpr32k5369d6i-source` (selected catalog skill source).
Its complete Development cluster controls and Cluster provider status/shutdown
sections, cluster Control/runProvider functions, public controlCluster handler
and Origin validator are byte-identical to the prior source. Full runtime files
and runtime-contract bytes did change; whole-file equivalence is not claimed.
The provider sub-contract remains busy75/release180seconds and shutdown
120+10+20seconds. Both current coordination/recovery guides were read completely.
New physical-machine schema2 does not apply to this virtual-cluster operation.
No claim was created or released.

At 00:12:34Z, safe public status returned0: running/ready, single/bridge,
actions stop+release, no maintenance object. Applied version1 remains pending=null,
SHA256 `91842caad08e21eb6aabe31a889c9c8e75f4dbb3264b7fc12fb28c80d1ba180b`.
Runner3399167/start31781317/uid1000/PGID=SID3399167 and recorded socket
`/tmp/vpsfree-devcluster-2390ddf185e2` match the prior proof; four exact argument
pairs and root identity revalidation passed. All four direct QEMU guest
PID/start identities match; only38 positively owned descendants were traversed,
with no snapshot race. The preview source remains old4ed; no update is needed.
No disk contents, guest SSH/API or other-session resources were inspected.

Public operations are unchanged. From `/home/aither/workspace/ai/vpsfree.cz`:

```sh
vpsadmin-devcluster stop 2026-11-01-typescript-client-migration
```

Then use the normal public Release (or portal Release, which includes stop):
`POST https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/api/sessions/2026-11-01-typescript-client-migration/release-cluster`,
body `{"kind":"vpsadmin"}`, Content-Type `application/json`,
Origin `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz`.
No separate CLI release or coordination-machine release is introduced. Public
Release retains its documented deletion of this cluster's disks/config/socket/state
through its provider implementation; no direct reset/private helper is proposed.
All prior refusal, uncertainty and postcondition guidance remains applicable.

[Sanitized snapshot and exact authority hashes](devcluster-stop-release-runtime-refresh.json).
Raw status stayed only in memory; credential fields were never printed or copied.
Only this tracking supplement and sanitized JSON were written, with no Git commit.
The session remains open.
