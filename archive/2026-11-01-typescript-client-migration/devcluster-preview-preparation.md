# Devcluster preview preparation — 2026-11-03

Prepared by implementer6 for lead/architect0. Session binding and environment
match `2026-11-01-typescript-client-migration` in
`/home/aither/workspace/ai/vpsfree.cz`; roster61 retains Sol/xhigh and
workspace_write. This records preparation, not a running preview.

## Current state and preparation deviation

The first standard text `status` reported stopped, without topology, network,
ready marker or result. Config existence was not measured before the next call.
The standard `urls` command unexpectedly ran `ensure_cluster_config`, which can
initialize this session's directory/socket identity and merges defaults into
config. It also printed development credentials; values are excluded here and
from reports. Lead accepted benign own metadata initialization under the user's
cluster-start request. No undo, reset or private repair was attempted.

After reconciliation, standard schema2 JSON status reports found/stopped,
ready=false, empty topology/network. The exact cluster directory contains only
`config.json` and `socket-dir`, both timestamped 2026-11-03 13:30:06 UTC. There is
no runner/PID, state/disks, applied selection, maintenance hold, ready marker,
result-config, SSH bundle or WebUI credential bundle in that directory. The
recorded workspace-scoped socket is `/tmp/vpsfree-devcluster-2390ddf185e2`, which
does not exist. Initialization is consistent with newly absent state, but the
pre-call config existence was not independently observed. No runner started;
the command only accessed the exact session/default-config/certificate-path
selection. No other-session state was inspected or changed.

Owned state/config path:
`.dev-clusters/vpsadmin/clusters/2026-11-01-typescript-client-migration/`.
Config enables `newWebui`, all API plugins, cluster DNS and mail templates.
Services address is 172.16.106.53; bridge is br0, gateway 172.16.106.1.
Host br0 is UP, /dev/kvm is readable/writable, the configured setuid
qemu-bridge-helper is executable, and bridge.conf allows br0. React WebUI
requires bridge; there is no observed reason for a local fallback. A later
standard start must still respect its occupied-services-address refusal and
must not use `--force` to bypass another running cluster.

## Sources and final candidate dependency

At inspection, clean session sources were WebUI
`b5c12bcd8afa67103ae05bd3fc993ad4fe14f256`, API
`610a96f8ce523afbcd3e4374a70047dbe3264b0d`, HaveAPI
`f29c1e4675bc1f79641faa619b8c68ecec923c71`. No same-session vpsadminos
worktree exists; the provider selects the canonical local origin/staging ref,
without fetching it. No source was changed or arbitrarily repinned here.

The installed provider automatically overrides `vpsadminWebui` with
`path:worktrees/<slug>/vpsadmin-webui`. Its frontend and BFF packages both come
from that input. It also selects the session API and optional HaveAPI worktrees.
There is no live Vite frontend mount. Wait for W's released npm client adoption,
committed quick checks, affected review and final five-package proof; do not
start the old vendor-archive WebUI candidate. Architect0 reports the released
package's complete dist/generated/schema equivalence to99ee and concludes no
backend repin is required. That compatibility disposition is separate from
guest build/boot success.

`result-config` and status record source revision/dirty/kind labels; those labels
do not prove activation. Package build-info derives separately from flake
self.rev/self.dirtyRev and otherwise reports unknown/dirty/unavailable. No
evaluation was run here: inspect actual final frontend/BFF metadata and store
paths rather than assuming path-input provenance is clean. Preserve honest
unknowns and report any packaging discrepancy before changing the provider.

## Shortest standard launch and access

After the final candidate is ready, parent launches under a fresh watcher:

```sh
vpsadmin-devcluster start 2026-11-01-typescript-client-migration \
  --topology single --network bridge
```

Single is services plus one node. Normal start creates credentials and builds
the selected cluster configuration, waits for readiness, refreshes seeded nodes
and proves the complete applied boot. It performs these mutations; this record
does not. This metadata-only state has no retained applied selection, so portal
`--existing` is not the initial-start path. For later changes on a running
cluster use ordinary `update <slug> services`; a retained cold start boots proved
applied payloads rather than replacing them with a new worktree candidate.

React URL: https://newadmin.aitherdev.int.vpsfree.cz/ . API/auth use the matching
api/auth hostnames. The user needs development network/DNS access and trust in
the workspace CA at `.dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt`.
Use the portal's exact-session service account fields privately for seeded
admin/member login; never copy passwords or OAuth/session secrets into reports.

The enabled build generates and retains its own WebUI credential bundle. Its
seed configures a separate nondefault OAuth client, callback
`https://newadmin.aitherdev.int.vpsfree.cz/oauth/callback`, 20-minute access and
30-day refresh tokens. Public TLS proxies to private nginx port18082; the BFF
listens at loopback3001 inside the newadmin container and trusts the cluster CA.
BFF sessions persist in `/var/lib/vpsadmin-webui/sessions`. No manual OAuth DB
bootstrap, credential rotation or production setting is needed.

Parent acceptance should retain the start's actual exit/runner/effect evidence,
standard ready status and exact applied system proof. Check TLS `/healthz`
(`ok`), public `/build-info.json`, safe `/config.json`, logged-out session and
login redirect/deep route. Match frontend/BFF package metadata, exact activated
services closure and selected final source. Status labels alone are insufficient.
No endpoint/SSH health probe was executed during this stopped preparation.

## Preserved uncertainty and authority

`sdk-real-api-2-result.md` retains its failed run and unconfirmed cleanup; this is
an unrelated isolated API/test-DB history, not evidence of a devcluster runner.
The later API3 run passed23 calls on API610/SDK99ee. Neither result authorizes
resetting, cleaning or killing old API2 resources, and no such action ran here.

Installed authority read in full:

- Selected coordination guide: `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0/share/dev-workspace/coordination.md`
  and `coordination-operations.md` in that directory.
- Provider README: `/nix/store/9019d7wm0c40q59vrnlf1clwp7q00xrd-vpsfree-dev-workspace-tools-0.1.0/share/vpsfree-dev-workspace/dev-clusters/vpsadmin/README.md`.
- Provider implementation: `bin/devcluster`, `lib/runtime.sh` (shared parent),
  and `nix/test.nix` under the same installed dev-clusters tree.
- API AGENTS, README/docs index, development/testing procedures; WebUI
  NIXOS_SERVICE and packaging provenance guidance.

No start/update/reset/stop, tests/builds/shells/install/download, API/DB/SSH
mutation, production deployment, default merge or session lifecycle action was
performed. The session stays open. Parent retains launch ownership.
