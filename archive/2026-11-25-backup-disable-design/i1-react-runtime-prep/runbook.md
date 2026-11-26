# React review runtime preparation and recovery

## Refresh3 — ordinary app refresh, final actual binding complete

Root owns every driver. This is the authorized ordinary development refresh for
corrected React defaults; no peer switch or additional user-approval step is part
of this package. Current refresh2 previews remain running. I1 has prepared local
controls/binding only, with no live health assertion or runtime action. Root
accepted the controls and I4's actual reviewed/built output handoff. The existing
binder passed once with clean reviewed `39a1f17ce859600d10276da0fe29bfb1593c8132`,
matching full metadata, output layout and built inline CSP. Its only code change
was the expected-head literal. Final inputs/env/nginx now exist; ordinary runtime
admission remains absent. Exact final hashes are in `refresh3-preparation.json`;
unbound binder/manifest copies are retained separately. Source/artifact dependency
is satisfied. Root owns final binding acceptance and actual driver release.

Executed once, recorded in `refresh3-binding.log`:

```sh
/home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/bind-refresh3.py /nix/store/59ynv5gwz6b3s0ddnpzdggzg718d2vfb-vpsadmin-webui-frontend-1.0.0 /nix/store/jxscjby6p1dh2jyv6nr9b7yvrmprbcdg-vpsadmin-webui-bff-0.1.0
```

Exact current stop targets and fresh attempts:

| Component | Current registration / InvocationID | Fresh registration / guest unit |
| --- | --- | --- |
| Edge | `d9e230fb-a0c2-429e-9798-5ec83134709f` / `45586e7a6b00493fa73744195b238d3f` | `383bd08d-ec47-4e94-ac15-3eaa07837154` / `vpsadmin-review-edge-ac1f7e2d-refresh3.service` |
| BFF | `be2b20b5-4704-42a6-ba03-fc69fc2f263c` / `56075bd161e841218a0bb0922b69f061` | `203cb011-868e-401f-a28b-3ec4ad386e40` / `vpsadmin-review-bff-ac1f7e2d-refresh3.service` |

After actual binding/root freeze and root's driver release, normally stop only
current edge then BFF. Root captures private command/terminal receipts:

```sh
/home/aither/bin/dev-session service stop 2026-11-25-backup-disable-design --as-is --id d9e230fb-a0c2-429e-9798-5ec83134709f --json
/home/aither/bin/dev-session service stop 2026-11-25-backup-disable-design --as-is --id be2b20b5-4704-42a6-ba03-fc69fc2f263c --json
```

Prove both exact refresh2 remote InvocationIDs terminal/MainPID0/cgroups gone.
Then record ordinary fresh actual-generation/input-hash admission; this takes no
peer reference, switch outcome or external-clearance arguments:

```sh
/home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/reconcile-refresh3-old.py
/home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/record-refresh3-admission.py
/run/current-system/sw/bin/bash /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/stage-apps-refresh3.sh
```

The existing full staging protocol runs **after stop/reconciliation/admission**.
It validates and roots the bound host outputs, exports their complete closure,
binds inventory/payload/runtime hashes, and uses the known ignored backend mount
for ordinary guest-daemon NAR import. Full validity, closure equality, separately
bound metadata hashes and fresh persistent roots precede config/owner staging.
No new early-copy transport/cache, signature bypass, guest build or remount is
introduced. The actual I4 build/metadata binding is ready before interruption;
closure export/import remains inside the accepted stage protocol. Receipts and
host roots use `app-stage-refresh3`; guest roots use
`vpsadmin-review-ac1f7e2d-refresh3-{frontend,bff}`. Existing roots remain intact.

Root registers BFF once, then releases bounded exact-unit/InvocationID/cgroup,
nonroot actual bound-package argv, typed3credentials and loopback health proof:

```sh
/home/aither/bin/dev-session service run 2026-11-25-backup-disable-design --as-is --id 203cb011-868e-401f-a28b-3ec4ad386e40 --name 'React review BFF refresh3 ac1f7e2d' --cwd /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design -- /home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/host-owner-refresh3.py bff
```

Only after BFF readiness does root register edge and release its bounded
identity/typed2credentials/nginx-prestart/strict-TLS metadata/config/session proof:

```sh
/home/aither/bin/dev-session service run 2026-11-25-backup-disable-design --as-is --id 383bd08d-ec47-4e94-ac15-3eaa07837154 --name 'React review HTTPS edge refresh3 ac1f7e2d' --cwd /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design -- /home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/host-owner-refresh3.py edge
```

`refresh3-preparation.json` contains frozen control hashes, local syntax/critical
argv checks and final actual-binding status; `refresh3-controls.diff` is the
complete comparison. New host receipts use `host-{bff,edge}-refresh3`; remote
attempts use `{bff,edge}-refresh3.*`. Private OAuth/signing/TLS inputs, BFF
StateDirectory/session store, origin/ports/firewall and foreground owner semantics
remain unchanged, including separate3BFF/2edge LoadCredential properties.

Preserve all five guests and the user's current backend data. PHP cleanup has
been submitted; historical plan/snapshot rows below are not current assertions.
No backend probe, fixture recreation or business operation is part of this refresh.
On first failure/UNKNOWN preserve the exact attempt and stop progression. Local
exit/15s grace/lock release never substitutes for matching remote terminal proof.
No blind replay, broad kill, reset, private unlock or lifecycle action is allowed.
Root owns recovery/activation; I1 retains technical fixes. No preservation blocker
or source/artifact dependency remains. No root driver has been executed by I1.

## Refresh2 — command-ready, preparation only

Lead owns every execution step. Current refresh1 previews remain running.
Explicit user approval for the preview interruption, peer READY and lead's own
inspected activation release are prerequisites for stopping anything. Preparation
is accepted/frozen and PARKED awaiting those conditions; peer READY alone causes
no action. No command below is scheduled or has been executed by I1.

The unchanged clean source is `1d895a5746561d15413f42afd83678b898de3b45`, tree
`1e52746fdf08f561e70efdbee6e7bbd22a57aebd`. Frontend is
`/nix/store/8zryvl94jahgq206bg2jf5wn6zymzrwp-vpsadmin-webui-frontend-1.0.0`;
BFF is `/nix/store/wdgyn07nr7mch8i5l3113h06injclnj3-vpsadmin-webui-bff-0.1.0`.
The binder passed matching clean metadata and inline CSP. Inputs and output env
are byte-identical to refresh1. Nginx changes only attempt paths and TLS unit
references. Exact hashes and local checks are in
[refresh2-preparation.json](refresh2-preparation.json); the complete control diff
is [refresh2-controls.diff](refresh2-controls.diff).

| Component | Stop only this current registration | Exact old unit / InvocationID | New registration / unit |
| --- | --- | --- | --- |
| Edge | `8636db4f-65a6-4e1f-b95b-afc45e842350` | `vpsadmin-review-edge-ac1f7e2d-refresh1.service` / `5939ce88915749079709484121cc07a6` | `d9e230fb-a0c2-429e-9798-5ec83134709f` / `vpsadmin-review-edge-ac1f7e2d-refresh2.service` |
| BFF | `01f924c6-7e76-4c06-9833-15993e028f8e` | `vpsadmin-review-bff-ac1f7e2d-refresh1.service` / `9a0195e943bc41b9baaabf5558bedd2d` | `be2b20b5-4704-42a6-ba03-fc69fc2f263c` / `vpsadmin-review-bff-ac1f7e2d-refresh2.service` |

Root retains private command/exit receipts through its existing driver. After
explicit user approval, peer READY and explicit root release, normally stop edge
then BFF:

```sh
/home/aither/bin/dev-session service stop 2026-11-25-backup-disable-design --as-is --id 8636db4f-65a6-4e1f-b95b-afc45e842350 --json
/home/aither/bin/dev-session service stop 2026-11-25-backup-disable-design --as-is --id 01f924c6-7e76-4c06-9833-15993e028f8e --json
```

Root announces the gap and holds replacements for the single original switch's
known terminal outcome plus explicit restart clearance. Do not add readers while
the peer is waiting. After that outcome, reconcile the two exact stopped remote
InvocationIDs, MainPID0 and empty/gone cgroups. Local exit, the15s grace and lock
release are insufficient. UNKNOWN blocks replacement. These commands do not stop
services; the second records root's clearance and the fresh actual generation.
Replace `ORIGINAL_SWITCH_REFERENCE` with the actual receipt reference and use the
proved outcome (`succeeded`, `failed`, or `compensated`):

```sh
/home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/reconcile-refresh2-old.py
/home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/record-refresh2-clearance.py ORIGINAL_SWITCH_REFERENCE succeeded reviewed-inline
```

After both proofs and fresh admission, root may run the reviewed staging command:

```sh
/run/current-system/sw/bin/bash /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/stage-apps-refresh2.sh
```

Staging validates the same60 resident closure paths against the retained plan,
their ordinary daemon-store validity, exact metadata and new persistent GC roots.
It copies only the public closure list/config/owner files through the known ignored
backend mount. It neither exports nor imports a NAR and never builds. Missing or
invalid resident content fails the attempt; it does not trigger a fallback copy.
Host receipts/roots use `app-stage-refresh2`; guest roots use
`vpsadmin-review-ac1f7e2d-refresh2-{frontend,bff}`. Old payloads/roots remain intact.
No service or firewall is activated by staging.

Root then registers BFF once, verifies its exact fresh unit/InvocationID,
nonroot wdgyn process, three typed credentials and canonical-Host health200:

```sh
/home/aither/bin/dev-session service run 2026-11-25-backup-disable-design --as-is --id be2b20b5-4704-42a6-ba03-fc69fc2f263c --name 'React review BFF refresh2 ac1f7e2d' --cwd /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design -- /home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/host-owner-refresh2.py bff
```

Only after BFF health does root register edge once:

```sh
/home/aither/bin/dev-session service run 2026-11-25-backup-disable-design --as-is --id d9e230fb-a0c2-429e-9798-5ec83134709f --name 'React review HTTPS edge refresh2 ac1f7e2d' --cwd /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design -- /home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/host-owner-refresh2.py edge
```

Verify exact edge ownership/nonroot nginx args, two typed credentials, successful
prestart config test, strict existing-CA/hostname TLS and actual full1d895 metadata,
public API config and same-origin anonymous session. The existing guest8443 rule
stays in place; no port action is needed. New host receipts are
`host-{bff,edge}-refresh2`; remote receipts use `{bff,edge}-refresh2.*` under the
same private base. The owner remains foreground and binds stop to its recorded
InvocationID/cgroup, with the corrected separate3BFF/2edge credential properties.

Preserve client2/private signing/TLS inputs, BFF user/StateDirectory/session store,
all old receipts/roots/refs, five guests, fixtures and Vite. On uncertain stop,
staging or registration, preserve that exact attempt and reconcile before any
continuation. Inspect only its bound remote unit with the corresponding owner
script's `inspect` mode. Do not replay a driver, create another instance, broadly
kill, unlock, reset, rotate credentials or clean anything. A new process's lost
SSH/local exit is never proof of remote termination. Root owns recovery decisions;
I1 retains technical fix ownership. Prevention/source and storage stay parked.

## Historical initial deployment and r2 preparation

Session: `2026-11-25-backup-disable-design`; operation `ac1f7e2d`.
Lead owns every guest write and service registration below. I1 prepared files
only. The original storage verification stays parked. Preserve all guests,
VPS1, dataset1, daily plan, three source snapshots, one backup and Vite5187.

## Current execution boundary

The original provisioning attempt ended at staging: no staged files, private
credentials or POST intent existed. Only the owned empty0700 guest directory
was created. Keep `oauth-driver/` unchanged. The stable public dispatcher uses
`Open3.capture3` without stdin data, so tar, scripts or NAR streams on its stdin
do not reach SSH. `resume-oauth-driver.py` resumes only those proven absent code
files using safely quoted base64 of secret-free source; it checks the frozen
hashes before the original single create. Credential values never enter argv.
Lead ran the corrected guard-complete driver `8bd1eb11…` exactly once:

```sh
/home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/resume-oauth-driver.py
```

Result: root tool39632 joined exit0; stage PID/PGID3551973 and create
PID/PGID3552398 both joined exit0. The safe receipt is `oauth-provisioned`,
mode `create`, nondefault, exact callback and private files true. Do not run
create, reconcile or the correction again. Private OAuth/signing credentials
now exist under `/var/lib/vpsadmin-react-review-ac1f7e2d/credentials`. No app or
firewall was activated. Original failed attempt receipts remain intact.

The intermediate frontend/BFF outputs were bound locally in
`intermediate-18597-inputs.json` and `intermediate-18597-outputs.env`:
full clean `18597f1df0e610a2d4177609626a27565581deeb`, matching
metadata and the built inline bootstrap CSP hash. This is package proof only.
18597 is not the final runtime candidate. Final reviewed checkbox-complete
`ff2cf8ae4b44781f90941611294a94fd6953763a` is now bound locally in `inputs.json`,
`outputs.env` and generated `nginx.conf`, using actual realized outputs:

- frontend `/nix/store/yd27wqhv0pwqkdd6f94w6nvmj3rs82b7-vpsadmin-webui-frontend-1.0.0`
- BFF `/nix/store/4f9ch790kw1i3hh8ypj1x6lsxpd9d5h8-vpsadmin-webui-bff-0.1.0`

The binder passed parsed clean metadata equality, public output layout and built
inline bootstrap CSP checks. Each differently formatted metadata file has its
own bound SHA256 in `outputs.env`. I4's final build/postproof receipt is
`i4-logs/acknowledgement-nix-output-receipt.json`; I1 did not duplicate those
checks. Local binding does not release import, app or firewall activation.

Earlier candidate outputs were absent/invalid in the services guest; `/nix/store`
is ext4 mounted read-only in the client namespace. Root then authorized one ordinary
`NIX_REMOTE=daemon` hash query against the known running system. It passed and
normally socket-activated daemon PID37075; that daemon's exact mount namespace
has `/nix/store` ext4 `rw,relatime`, super options `rw`. No import or remount ran.
The architect recorded the conventional mounted-NAR/daemon route.
`stage-apps.sh` requires final `inputs.json`/`outputs.env`, now present. Its
execution remains held for lead acceptance/release; no import has run.

The public staging path is the existing ignored backend `.rubocop_cache/`
namespace, in its unique `vpsadmin-react-review-ac1f7e2d/` child. Git check-ignore
confirmed the existing `.gitignore:5` rule and Git ls-files returned no tracked
entries. A secret-free mount-proof file hashed identically on host and at
`/mnt/vpsadmin/.rubocop_cache/vpsadmin-react-review-ac1f7e2d/mount-proof`:
`1aa1cfa285c4fb9f8427ed627524e74a8b6ded7e1e27e6795be2d18fd1940dfe`.
No ignore configuration or application file changed.

After final output binding and lead release, the exact staging command is:

```sh
/run/current-system/sw/bin/bash /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/stage-apps.sh
```

It roots the already-valid host outputs, exports their complete explicitly listed
closure, records byte count/path inventory/digest, and invokes public SSH with
argv only. The guest verifies manifest/payload hashes and imports through
`NIX_REMOTE=daemon` with redirection from its mounted file. It checks the complete
imported closure, matching metadata and ordinary persistent per-output daemon
GC roots, then stages only the public runtime config/owner script. No signature
bypass, guest build, alternate store, mount change, service or firewall activation
is included. A failed/uncertain phase preserves the exact attempt; reconcile
before any continuation instead of replaying the driver.

## Prepared runtime contract

Origin `https://newadmin.aitherdev.int.vpsfree.cz:8443`; services VM
`172.16.106.53`; BFF loopback `127.0.0.1:3001`. No CORS rewrite is needed.
The separate nginx config/prefix never reloads the main nginx. Static content
comes from the exact built frontend; OAuth/metadata routes go to BFF. Headers
replace all forwarded scheme/host/IP values; OAuth access/error logs are off.
Metadata retains BFF cache/CORP/Vary. Existing TLS references are supplied through
private `LoadCredential`, without copying a key into source or output.

`remote-owner.sh` prepares one ordinary transient unit per component, each with
its unique session/operation description, InvocationID/PID/cgroup receipt and
foreground `systemd-run --wait --pipe`. Both run as dedicated DynamicUser users.
BFF uses the module's `LoadCredential` raw files, private StateDirectory/session
store, absent retired secret variables and strict CA trust. Edge has its own
StateDirectory/PID/log/temp files and credential-loaded certificate/key. Its
ExecStartPre validates nginx before listening. No restart policy, runtime lease
or end-of-turn cleanup is added.

Staging rechecks only selected ports and exact owned state before first
activation. After successful final import/staging and lead release, register the
local foreground commands (these are NOT released before final binding/import):

```sh
/home/aither/bin/dev-session service run 2026-11-25-backup-disable-design --as-is --id fe58b25f-b98f-4f9a-b491-c211fc513c7e --name 'React review BFF r2 ac1f7e2d' --cwd /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design -- /home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/host-owner-r2.py bff
/home/aither/bin/dev-session service run 2026-11-25-backup-disable-design --as-is --id c346723f-3467-4ed3-910c-24033cd45bd9 --name 'React review HTTPS ac1f7e2d' --cwd /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design -- /home/aither/.nix-profile/bin/python3 /home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/host-owner-r2.py edge
```

### Corrected BFF attempt r2 — prepared, not staged or started by I1

The first registration `2b7078f3-699f-4a37-bb94-08599b82fdb9` and guest unit
`vpsadmin-review-bff-ac1f7e2d.service` failed before Node executed. Its recorded
InvocationID is `45c15fae092a4513b6998d6d2979287f`. The unit's D-Bus credential
array had one entry whose source contained three space-joined paths; the executor
reported `Failed to deserialize: Invalid argument`. The original host/SSH PIDs
are absent, unit MainPID0/cgroup absent and port3001 has no listener. Old scripts,
registration, identity, receipts and logs stay unchanged.

`remote-owner-r2.sh` supplies one `--property=LoadCredential=ID:PATH` per
credential: three BFF entries and two edge TLS entries. The
[systemd credential contract](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html#LoadCredential=ID:PATH)
says the option may be used multiple times, each defining an additional
credential. Other unit settings stay unchanged. The new BFF unit is
`vpsadmin-review-bff-ac1f7e2d-r2.service`, description ends `/bff-r2`, and private
identity/terminal/stop receipts use `bff-r2.*`. `host-owner-r2.py bff` uses the new
`host-bff-r2/` directory and new registry UUID above. Existing OAuth/client2,
credentials, StateDirectory and final package inputs are reused. Edge has never
launched; the corrected owner keeps its original unit name, description and
credential mount paths. Its registration/firewall remain held for BFF health.

Lead may stage ONLY this secret-free corrected owner with the following exact
public-SSH command, before the corrected registration. This does not execute the
owner or change credentials, units, services or firewall:

```sh
/home/aither/.nix-profile/bin/python3 - <<'PY'
from pathlib import Path
import base64
import hashlib
import shlex
import subprocess
source = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/remote-owner-r2.sh')
digest = '8acdc34ea1119a2993ab50c23b3c9227f3ba88c745988a0f6a97bb222834f6e6'
data = source.read_bytes()
assert hashlib.sha256(data).hexdigest() == digest
target = '/var/lib/vpsadmin-react-review-ac1f7e2d/remote-owner-r2.sh'
encoded = base64.b64encode(data).decode()
script = (
    'set -euo pipefail; umask 077; '
    f'test ! -e {target}; test ! -L {target}; '
    f'(set -o noclobber; printf %s {shlex.quote(encoded)} | base64 -d > {target}); '
    f'test "$(sha256sum {target})" = "{digest}  {target}"'
)
subprocess.run([
    '/home/aither/bin/vpsadmin-devcluster', 'ssh',
    '2026-11-25-backup-disable-design', 'services', '--',
    '/run/current-system/sw/bin/bash -c ' + shlex.quote(script),
], stdin=subprocess.DEVNULL, check=True)
PY
```

Before opening ingress, prove both exact remote unit identities, nonroot UID,
actual process/package command and loopback health. `open-edge-port.sh` prepares
only the exact commented TCP8443 rule in `nixos-fw`; it does not reset rules.
It is not copied by app staging. Lead invokes it from the host through public
SSH using this exact command, after the unit/health proof. The script travels as
quoted secret-free argv; no caller stdin or host-side iptables is used:

```sh
/home/aither/.nix-profile/bin/python3 - <<'PY'
from pathlib import Path
import shlex
import subprocess
script = Path('/home/aither/workspace/ai/vpsfree.cz/work/2026-11-25-backup-disable-design/i1-react-runtime-prep/open-edge-port.sh').read_text()
subprocess.run([
    '/home/aither/bin/vpsadmin-devcluster', 'ssh',
    '2026-11-25-backup-disable-design', 'services', '--',
    '/run/current-system/sw/bin/bash -c ' + shlex.quote(script),
], stdin=subprocess.DEVNULL, check=True)
PY
```

Then verify strict trusted TLS, actual build-info, runtime config API/origin,
same-origin anonymous session and I4's real admin/member OAuth/UI acceptance.
No backup cleanup or plan removal is submitted. Preserve private credentials and
sessions for human review.

## Ownership and uncertainty

Local registration stays attached to public SSH for the remote unit's lifetime.
Authorized local termination requests only the exact identity-bound remote unit
to stop; PTY HUP/TERM also reaches its owner trap. Keep both source and remote
start/terminal receipts. A lost link, killed local supervisor or local registry
terminal state alone never proves remote exit. The local registry's15s stop
grace may end before remote proof. Reconcile via the same public SSH command
`bash /var/lib/vpsadmin-react-review-ac1f7e2d/remote-owner-r2.sh COMPONENT inspect`;
require matching InvocationID, terminal unit/MainPID0 and empty/gone owned
cgroup. Do not start another component instance after UNKNOWN. Any later stop
needs its own authorization and uses only the matching component/unit. No guest,
main service, session or fixture cleanup is part of this preparation.

Quick checks so far: bash syntax, Ruby syntax and Python AST pass. First BFF
attempt failed before ExecStart; r2 and nginx/ingress remain unexecuted runtime
proof. No fixture or OAuth mutation accompanied that failed startup.
