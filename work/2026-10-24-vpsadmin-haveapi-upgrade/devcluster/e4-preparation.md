# E4 reset/redeploy preparation — 2026-10-27

## Latest released read-only preflight, from 22:57 UTC

**Read-only facts complete; reset/start remain unreleased.** Selected runtime is
`/nix/store/pq2jwjcv4hbyiwzcam50x6j9fv008qiq-dev-workspace-0.2.0`, provider
`/nix/store/vh650zaiazv3n8z12yf12pfbc951xwb9-vpsfree-dev-workspace-tools-0.1.0`.
Contract stays `9c8e9e5c…`, schema1/policy3. Actual installed proof source still
has SSH reading stdin and full-boot enumeration using a here-string: F is not
installed. Historical generation facts below are not today's command binding.

One public `nix flake metadata` run passed in 21.347 seconds, no-write-lock-file,
IFD=false/max-jobs0. It explicitly overrides the **proposed** 0311 aliases and
both native OS inputs, not the old live canonical paths. Complete 20-node graph
SHA-256: `d6f76d362cbfe695550a19674150ebab6c9d3d5bcfd44728fddf2faaba562f84`.
Native OS `origin/staging` advanced to
`f4e55a13d7d2f5c1b61737f0300ec8a535ef02f1`, NAR
`sha256-HRAKzl1PywAm/AVo64V1PXOg5xD2i+Z1oMdrC/aG9Mk=`.
Effective stable nixpkgs is `718f670e845328e9c2cecdd832835712b2cbd065`, unstable
`3ec636362e1816bc2f0888fa0fa2c69f1bc9e504`; vpsfStatus advanced to
`e4881a932ad20bab141e3203afb985e96a51b1da`. Seven node keys differ from the
old accepted graph; exact [delta](e4-preflight-0311/proposed-graph-delta.json)
is retained. This changed graph requires lead acceptance. C's standalone graph
uses nixpkgs `5e2305d…`/OS `97045e5…`; no artifact equality/reuse is claimed.

Aliases are clean exact A `9697bf28c3171d4ee3e0980160be60764ae2c4aa` and C
`e468ca48406bde1bd99cc42a05e1832fb42162f4`; before/after dependency locks match,
including API full lock `0051b738…`. Proposed path NARs are
API `sha256-4H/TYNh45ocmhugc6p/7fgDh1o3ljGuoZgNAwBcXWAw=` and
React `sha256-htG58D3bJKNw0/veLRSxYqORIjTXdKeOD495SbKFWBA=`.
A reports stable API lock/no source writer, but later normal ignored PHP setup
may write; raw-path identity stays provisional until final writer handoff and
canonical mapping. C's final publication/no-writer handoff is accepted.

Current canonical live source remains old70a/f10, native running/ready,
single/bridge, pending=null. Runner2882335 matches all four native flags/socket;
its four QEMUs remain in the original scope. All four fixed-IP neighbor MACs
match those own old QEMUs. One other QEMU431390 is not on br0, consistent with
the ongoing A services check. This passive attribution does not prove free
addresses after reset. No guest commands were issued.

Host snapshot: MemAvailable56,915,280KiB (54.28GiB), 64 allowed CPUs, load
6.36/6.90/6.92, disk free97.79GB. Global Nix daemon current5.15GB/historical
peak42.71GB is separate and not E-attributed. A overlap remains a gate; this
snapshot is not a capacity reservation. Bridge/KVM/helper access passes.

Kernel-only public evaluation with builds/IFD disabled confirms node6.12.113
`/nix/store/4k5kg0x1msvl4kffpr2g7cidpnwbnkhk-linux-6.12.113` exists locally and
in cache.vpsadminos.org; native test-base `linuxPackages_6_12` selects
`/nix/store/6sn4mxbn21zap3dc6nln6zbzzqb7as0x-linux-6.12.113`, local and
cache.nixos.org. Exact paths/derivations/NARs are retained. The preliminary
`pkgs.linux`6.18 probe is explicitly not the native test-base selection.
Final guest overrides/full payloads are not evaluated; no build/substitution
occurred. Known module/initrd assembly is distinct from real kernel compilation.

Evidence: [inputs/generation](e4-preflight-0311/generation-inputs.json),
[proposed full graph](e4-preflight-0311/proposed-metadata.json),
[command/lock guards](e4-preflight-0311/proposed-metadata-result.json),
[sanitized host/native](e4-preflight-0311/native-host-sanitized.json),
[passive address attribution](e4-preflight-0311/address-attribution.json),
[node cache](e4-preflight-0311/kernel-cache-proof.json),
[NixOS test kernel](e4-preflight-0311/nixos-test-kernel-cache.json).
All exact command handles completed. No private helper, guest query, config
preservation/write, reset/move, driver edit, source/ref mutation or observer was
used. A services/effects handoff, changed-graph acceptance and fresh
post-mapping/immediate pre-start checks remain gates; no further polls assigned.

## Earlier preparation and ordered execution draft

**PREPARED ONLY. No cluster reset, move, config copy/write, guest probe or startup was
executed.** This implements the operational proposal in `design.md:2021`;
lead retains native reset/start ownership. Current targets are A `9697bf28…`
(`vpsadmin-0311`) and C `e468ca48406bde1bd99cc42a05e1832fb42162f4`
(`vpsadmin-webui-0311`), committed/quick-pass per lead. C review is accepted and
postchecks released; A review and required A/C postchecks remain gates. Existing
LIVE cluster/source/state remain unchanged. KB 0.31.1 staging is separately
accepted, owned/up and retained for user review.

`dev-session current` from this exact tracking directory matches the trusted
session/workspace binding; ambient environment values are both absent. Current
Git/lifecycle/deployment/verification procedures, selected coordination guide,
native README/contract and public source-selection/SSH/reset paths were read.
The earlier preparation observed public commands resolving to runtime
`/nix/store/46rpb1jcjaclc01vrj0r9m8v0xvp8341-dev-workspace-0.2.0`;
provider is
`/nix/store/cscrk1qkydsvzlkxjv272nq7xq25bg30-vpsfree-dev-workspace-tools-0.1.0`.
Contract SHA-256 is
`9c8e9e5c371eda46ccb49eaf275ee4996d2ddce3930c9047da39ccd195f67183`,
schema 1/policy 3. F was not installed; the old stdin/full-boot proof defect was
present. These historical identities must be freshly checked after execution-prep
release; they were not queried for this draft update. No private helper is part
of the plan.

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
git --git-dir=/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git worktree move /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-0311 /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin
git --git-dir=/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-webui.git worktree move /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-live030
git --git-dir=/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-webui.git worktree move /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui-0311 /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui
```

Lead then changes only the corresponding four registration `name` values,
carrying each whole ordinary entry (including comparison/base data) intact:

| Old name | New name | Branch retained |
| --- | --- | --- |
| `vpsadmin` | `vpsadmin-live030` | `2026-10-24-vpsadmin-haveapi-upgrade` |
| `vpsadmin-0311` | `vpsadmin` | `2026-10-24-vpsadmin-haveapi-upgrade-0311` |
| `vpsadmin-webui` | `vpsadmin-webui-live030` | `dev/vpsadmin-haveapi-upgrade` |
| `vpsadmin-webui-0311` | `vpsadmin-webui` | `dev/vpsadmin-haveapi-0311` |

Lead runs public `dev-session sync 2026-10-24-vpsadmin-haveapi-upgrade --as-is`.
Both `vpsadmin-031` and `vpsadmin-webui-031` checkouts/registrations stay in place;
published C4 `baf00acc31d34ab37720643c5833b4476a341f3b` is preserved. Refresh/F
and every other registration remain unchanged. Post-move inventory
must prove canonical paths hold accepted final0311 heads and retained paths hold
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

## Bounded acceptance and separate completed staging

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
React; verify actual packaged HaveAPI/generators0.31.1, PHP new canonical source,
matching frontend/BFF final build-info and generated TypeScript docs alongside
Go/Rust. No new VPS/member mutations, broad SDK/browser campaign, screenshots,
tokens/cookies/password logs or host trust change. Report actual URLs/CA/private
credential access and leave cluster running/session open.

The former foreign staging blocker was resolved by its owner. KB 0.31.1 staging
is accepted under our ownership, container up, with current EN pending manifest;
see [staging receipt](../package-0.31.1/staging/receipt.md), SHA-256
`11bdb447e13e90e2ec81ff3180ecbb85a5fea60970d8e644dc30b7f64cb36784`.
No further KB checks, reset, stop/release or production promotion are assigned.
This completed staging work supplies no E4 cluster execution clearance.

Session portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/>.

## Historical C4 0.31.0 prepared artifact facts received from lead

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
