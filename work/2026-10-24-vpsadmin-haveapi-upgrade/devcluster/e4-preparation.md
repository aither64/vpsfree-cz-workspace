# E4 reset/redeploy preparation — 2026-10-27

**PREPARED ONLY. No reset, move, config copy/write, guest probe or startup was
executed.** This implements the operational proposal in `design.md:2021`;
lead retains native reset/start ownership. Final A/C heads, review and affected
postchecks are pending. Existing LIVE cluster/source/state remain unchanged.
Staging remains foreign-owned with a pending release and is a separate blocker.

`dev-session current` from this exact tracking directory matches the trusted
session/workspace binding; ambient environment values are both absent. Current
Git/lifecycle/deployment/verification procedures, selected coordination guide,
native README/contract and public source-selection/SSH/reset paths were read.
Public commands resolve to runtime
`/nix/store/46rpb1jcjaclc01vrj0r9m8v0xvp8341-dev-workspace-0.2.0`;
provider is
`/nix/store/cscrk1qkydsvzlkxjv272nq7xq25bg30-vpsfree-dev-workspace-tools-0.1.0`.
Contract SHA-256 is
`9c8e9e5c371eda46ccb49eaf275ee4996d2ddce3930c9047da39ccd195f67183`,
schema 1/policy 3. F is not installed; the old stdin/full-boot proof defect
remains. No private helper is part of the plan.

## Preconditions and private editable config

Before disruption, lead accepts exact final A/C commits and dependency locks,
completed quick checks, independent history/source review and required affected
package/postchecks. Source owners confirm no active writer/check still uses the
four moving checkouts. Final heads are recorded explicitly, not inferred from
branch names. Preserve original 70a/f10 refs and all old receipts.

After source gates and before lead reset, preserve **only the documented editable
config** outside the reset tree. Proposed commands, not executed:

```bash
e4_root=/home/aither/workspace/ai/vpsfree.cz
e4_slug=2026-10-24-vpsadmin-haveapi-upgrade
e4_cluster="$e4_root/.dev-clusters/vpsadmin/clusters/$e4_slug"
e4_private="$e4_root/.dev-clusters/vpsadmin-preserved/$e4_slug/e4-20261027"
test -f "$e4_cluster/config.json" && test ! -L "$e4_cluster/config.json"
test ! -e "$e4_private"
install -d -m 0700 "$e4_private"
install -m 0600 "$e4_cluster/config.json" "$e4_private/config.json"
cmp -s "$e4_cluster/config.json" "$e4_private/config.json"
```

Record digest/mode/owner only, never config contents. This preserved file stays
outside Git and portal tracking. Do not copy disks, applied envelopes, journals,
socket state or credentials into the replacement cluster. Workspace CA and SSH
state remain intact. Native start generates fresh disposable BFF credentials.

Lead rechecks exact native ownership/pending/runner tuple, selected generation,
native OS ref, bridge/KVM, host capacity and separate daemon headroom at the
execution boundary. Public reset must actually complete and the exact owned
runner/QEMU/socket process effects must be reconciled before moves. No reset
or move release is implied by this preparation document.

## Four ordinary Git moves, only after reset-complete release

Before/after inventory covers each own checkout's absolute path, branch, full
HEAD, common Git directory, Git worktree identity, tracked index/diff state,
directory inode and relevant ignored lock/private-file digests/modes/symlinks.
Do not print private bytes. A directory rename preserves contents; the expected
Git administration path-pointer update is not a source change. Preserve source
owners' exact accepted ignored-byte inventory rather than assuming clean Git
proves ignored equivalence. Destinations must not already exist or be symlinks.

Run each command separately, stop at the first failure, and reconcile actual
paths before retry. No `--force`, symlink, branch checkout/reset or ref rewrite:

```bash
git --git-dir=/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git worktree move /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-live030
git --git-dir=/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git worktree move /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-031 /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin
git --git-dir=/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-webui.git worktree move /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-live030
git --git-dir=/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-webui.git worktree move /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-031 /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui
```

Lead then changes only the corresponding four registration `name` values,
carrying each whole ordinary entry (including comparison/base data) intact:

| Old name | New name | Branch retained |
| --- | --- | --- |
| `vpsadmin` | `vpsadmin-live030` | `2026-10-24-vpsadmin-haveapi-upgrade` |
| `vpsadmin-031` | `vpsadmin` | `2026-10-24-vpsadmin-haveapi-upgrade-031` |
| `vpsadmin-webui` | `vpsadmin-webui-live030` | `dev/vpsadmin-haveapi-upgrade` |
| `vpsadmin-webui-031` | `vpsadmin-webui` | `dev/vpsadmin-haveapi-031` |

Lead runs public `dev-session sync 2026-10-24-vpsadmin-haveapi-upgrade --as-is`.
Refresh/F and every other registration remain unchanged. Post-move inventory
must prove canonical paths hold accepted final031 heads and retained paths hold
old70a/f10, with unchanged branches/content/ignored locks/private bytes. The
native provider selects literal canonical paths; aliases/environment overrides
cannot replace these moves. No moves while old virtiofs/QEMU is alive.

## Initialization, graph and parent launch

After successful moves/public sync and a separate execution release, initialize
the same owned location with public
`vpsadmin-devcluster config 2026-10-24-vpsadmin-haveapi-upgrade`, discarding stdout
and withholding arbitrary diagnostics. Restore only preserved editable config
via mode-0600 copy, verify its digest, and require normal owned stub/socket
validation. Do not restore old applied state or bypass generation/refusals.

Bind complete effective source graph and canonical source/NARs with public
no-write metadata, IFD disabled/max-jobs0 where evaluation permits. Native
overrides both OS inputs to canonical `origin/staging`; its nixpkgs also supplies
the frontend graph. Report exact differences from standalone check graphs.
Check actual selected kernel outputs/cache and immediate capacity/address/
native conflicts before startup. There is no public build-only prepare command;
do not invoke private `build_config` or add an optional prebuild framework.

Existing `activation-driver.py`/command documents are **historical and cannot
launch E4 unchanged**: they pin w6/q19, old70a/f10, config/OS facts and Nix2/4.
Lead accepts later minimal rebinding only after final heads/input facts are
accepted. First preserve original driver/docs/check receipts with hashes; update
only exact selected constants/input facts and requested Nix jobs1/cores2 (including
the driver's existing matching guard). Refresh AST/shell/filter checks and small
synthetic initial/final/status-gating assembly checks; no mechanism expansion or
execution flag invocation by E3. Any substantive behavior change returns to lead.

Parent launches one fresh ordinary public start, single/bridge, through the
accepted containment/sanitization approach: resident 32GiB/12CPU/zero swap,
Nix max-jobs1/cores2 requests, separate daemon headroom accounting, retained
detached runner/QEMU limits. Native stdout is discarded; only allowlisted
diagnostics are emitted. A permitted fresh observer observes independent files
or parent uses visible fallback; no competing utility, implicit retry or teardown.

## Bounded acceptance and remaining staging blocker

After native completion, strict canonical readiness/selection and all four
QEMU scope membership must agree. Record exact result/toplevel/source graph and
normal host roots. Then run **four independent public SSH commands**, each using
`vpsadmin-devcluster ssh <slug> MACHINE -n -- ...`, for dns-primary,
dns-secondary, node1 and services. Validate exact current/booted system, whole
closure validity and existing standard/profile/provider roots. Do not feed SSH
from a names loop; do not create roots or repair the old applied certificate.
Missing extra provider roots remain an explicit cold-recovery/certificate gap;
independent valid current closures/system roots can support qualified testing.

Use existing bounded TLS/seeded-member login/read/logout checks once per PHP and
React; verify actual packaged HaveAPI/generators0.31, PHP new canonical source,
matching frontend/BFF final build-info and generated TypeScript docs alongside
Go/Rust. No new VPS/member mutations, broad SDK/browser campaign, screenshots,
tokens/cookies/password logs or host trust change. Report actual URLs/CA/private
credential access and leave cluster running/session open.

Staging is blocked by `2026-09-13-auth-email` and its pending EN bundle. Do not
poll, queue, contact the foreign owner or transfer/release/reset it. Once lead
confirms legitimate availability, final reviewed KB manifests can follow public
start/stage/verify after fresh production guards, showing both real page/history
URLs. No production promotion or post-handoff staging release is authorized.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/>.

## C4 prepared artifact facts received from lead

Read from existing Package C receipts only; no Nix/store/runtime query, probe or
rebuild was performed. C4 head is
`baf00acc31d34ab37720643c5833b4476a341f3b`, schema-1 build-info dirty=false.
Lead reports unit/script/BFF/build and five Nix outputs passed. The C4 browser
gate subsequently failed 3/6 cases: desktop dashboard navigation and session
expiry redirect on desktop/mobile. C1 is diagnosing the original traces;
publication/C readiness and E4 release are blocked. Earlier successful checks
retain only their recorded scope. These paths remain prepared inputs; no
artifact reuse or final C4/E4 acceptance is claimed.

| Output | Prepared store path |
| --- | --- |
| Frontend | `/nix/store/729jjifw96nb2hvh902563jfh7mjma00-vpsadmin-webui-frontend-1.0.0` |
| BFF | `/nix/store/l93gg2jcx91ir8qrrbv8x1zl5f4q7izh-vpsadmin-webui-bff-0.1.0` |
| Provenance | `/nix/store/p3vlsh9drr8mjjvahb4h4sy3r915n6sn-vpsadmin-webui-provenance` |
| Source contents | `/nix/store/l4b6yz1js8kjfb9cxgj1xdm2d8k0y5nh-vpsadmin-webui-source-contents` |
| Package contents | `/nix/store/58vfga3i9z61fgwmxwjypxavwwp7agf7-vpsadmin-webui-package-contents` |

Saved evidence under `package-c/0.31.0/`: `nix-output-identities.json`,
`nix-build-info.json`, `nix-root-map.json`, `batch2-nix-results.json` and full
`nix-recursive-input-graph.json`. Ordinary roots are recorded by that package;
they were not re-queried here. Its standalone graph is distinct from the later
native OS/nixpkgs/follows composition. No artifact reuse/equality with a future
native build is asserted. A4/B4 are not final; E4 preflight remains unreleased.

Later lead update: the bounded C4 gate is accepted. Exact cold, isolated f10 and
baf desktop-expiry comparisons both actually passed with the same unchanged
root-URL/Overview/notice assertions, runtime and caps. The earlier actual 5/6
run covers the other cases. Original 3/6 and 5/6 failures remain separate
evidence; this does not fabricate a single 6/6 run or establish a preexisting
cause. Unit/build/Nix provenance/root evidence retains its original scope.
C1 has release for ordinary publication of its own new ref and final receipt;
publication and writer reconciliation will be reported by C1, not assumed here.
E4 still has no execution/preflight release pending A31-R1 measurement/finding
and required A postchecks. No polling, probes or artifact reuse followed this
update; the later native graph may still differ from C's standalone graph.
