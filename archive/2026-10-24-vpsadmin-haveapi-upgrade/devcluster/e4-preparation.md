# E4 reset/redeploy preparation — 2026-10-27

## E5 released read-only preflight — 2026-10-28 09:57–10:00 UTC

**Read-only package complete; deployment remains gated.** Actual canonical
selection remains clean API9697/WebUIe468, public running/ready/single/bridge,
pending=null. Proposed aliases are exact A
`8102179cf7f7e9bb534965c8acb3e02ef723045f`
(`2026-10-24-vpsadmin-haveapi-upgrade-0312`) and C
`2e32c814d3af70ac39257f2542075bd580ee38d4`
(`dev/vpsadmin-haveapi-0312`), both Git-clean at this snapshot. Final review,
affected checks/publication/no-writer handoffs are still separate gates; raw
source NARs are provisional until ignored PHP/dependency writers finish.

Material generation change was reported immediately: selected runtime
`/nix/store/pjmi2cz75r9cwynh4lin706jdzlp4xb9-dev-workspace-0.2.0`, provider
`/nix/store/kbppyqvzbizqvdi7d8ws07j006mdz8q0-vpsfree-dev-workspace-tools-0.1.0`.
Architect reports lead accepted execution rebinding: runtime executable/contracts/
guides equal prior pq2 and provider native payload equal prior vh650; catalog
change is confctl wrapper path. E3 independently compared native script,
README, contract, flake and test definition byte-for-byte. Contract remains
`9c8e9e5c371eda46ccb49eaf275ee4996d2ddce3930c9047da39ccd195f67183`,
schema1/policy3, F proof-loop stdin/here-string defect unchanged. No package switch
or driver edit was performed. Current public wrapper realpaths require later
released constant rebinding; historical driver bindings are not launch-ready.

ONE public proposed-alias metadata run, no-write-lock-file/IFD=false/max-jobs0,
passed in12.498s:20nodes, SHA256
`439efd64f7deb8f7b868b308827e9a3e8ea7f7478788547d3d888479bf3faf15`.
Compared with accepted E4 final graph, only API path/NAR, WebUI path/NAR and
**vpsfStatus** change. OSf4e55a13 and effective stable nixpkgs718f670, every
other node and follows are unchanged. Proposed API NAR
`sha256-tgQXSKpg5eViCf7nJhLQ/sQ1DT9wNSt/yjKOogiQRv0=`, WebUI NAR
`sha256-Wz8/aQCPE4qOuhojcDTF6807XjFv+SLnqJAuJPsU2YQ=`. Material status
`e4881a932ad20bab141e3203afb985e96a51b1da` →
`5723f8a40d458a847d4efc4f6b30d98f22a6bca5`, NAR
`sha256-OP5Uztub5U+uyyR5nF4cf+uelPLhRur9y+cy7Oc1Q2M=`, was reported for
architect disposition; **not accepted here**. Lock digests match before/after.
This is a PROPOSED0312 graph, not current LIVE selection or standalone artifact
reuse/equality. No duplicate metadata, private build helper, build or IFD.

Owned runner1617073 has all four exact native flags, socket record
`/tmp/vpsfree-devcluster-02da06564216`, and four QEMUs
1621949/1624130/1624935/1625109 in exact prior233414Z scope. Socket entries
remain present. Resident memory.max34359738368/cpu.max1200000 100000, zero
OOM/kill; current20185604096/peak20901572608 bytes. Passive neighbor attribution
for172.16.106.53/.41/.61/.62 matches own guest MACs. Extra foreign resources are
untouched; this is not free-address clearance after reset. BridgeUP, KVM and
wrapper access pass. Host snapshot MemAvailable54473572KiB, CPUs0–63,
load19.72/15.83/13.40, diskfree90456014848 bytes; separate global Nix daemon
MemoryCurrent5878120448 bytes. No future capacity reservation or immediate
pre-start clearance follows while A/C checks overlap.

Kernel-only public evaluation confirms native node/QEMU6.12.113 output
`/nix/store/4k5kg0x1msvl4kffpr2g7cidpnwbnkhk-linux-6.12.113` and NixOS test-base
linuxPackages_6_12 output
`/nix/store/6sn4mxbn21zap3dc6nln6zbzzqb7as0x-linux-6.12.113`, both locally valid
and available from their ordinary vpsadminos/nixos caches with retained NARs.
This covers kernel selection defaults, not all future guest payload overrides.
Two kernel-only evals succeeded but a local consumer wrongly expected JSON
objects where Nix serialized outPath-bearing attributes as path strings; saved
successful raw output was consumed correctly, without further evaluation or any
metadata/build retry. The limitation is preserved in the kernel receipt.

Evidence: [generation/sources](e5-preflight-0312/generation-inputs.json),
[proposed full graph](e5-preflight-0312/proposed-metadata.json),
[exact graph delta](e5-preflight-0312/proposed-graph-delta.json),
[metadata/lock result](e5-preflight-0312/proposed-metadata-result.json),
[allowlisted native/host/address snapshot](e5-preflight-0312/native-host-sanitized.json),
[kernel local/cache proof](e5-preflight-0312/kernel-cache-proof.json).
All E3 handles complete20623/57358/53050/77560; kernel projection failures are
harness failures, not native/build failures. No watcher was launched or needed.
No guest SSH, config preservation/init, reset, move/sync, driver edit/start,
provider repair, KB query or registry campaign. Current cluster/scope/roots/KB
staging/session remain running/open. Next: lead accepts status delta and final
A/C gates, then separately releases fresh preparation/reset package. No polls.

## E5 / 0.31.2 current draft — records only

**Preparation draft only; source/review/affected-check/no-writer gates remain
pending. No preflight, reset, move, config preservation or driver edit released.**
This addendum supersedes the historical execution-draft source mapping below
for the next deployment. It uses existing accepted receipts only; no native,
generation, status, graph, capacity, guest or store query was performed.

The current canonical 0.31.1 predecessor is API
`9697bf28c3171d4ee3e0980160be60764ae2c4aa` and WebUI
`e468ca48406bde1bd99cc42a05e1832fb42162f4`, accepted for qualified current manual
use in [E4 receipt](e4-runtime/receipt.md). Intended new aliases are
`vpsadmin-0312` and `vpsadmin-webui-0312`; the released preflight above now binds
heads/branches, while final review/check/publication and writer handoffs remain
pending. No readiness is inferred from aliases. No 0.31.1 output/graph or
capacity snapshot establishes the future 0.31.2 selection.

Only after lead accepts final A/C gates, releases fresh preparation, and parent
public reset completes with owned runner/QEMU/socket effects reconciled, draft
these four ordinary worktree moves in the existing session group:

| Order | From | To |
| --- | --- | --- |
| 1 | `vpsadmin` | `vpsadmin-live0311` |
| 2 | `vpsadmin-0312` | `vpsadmin` |
| 3 | `vpsadmin-webui` | `vpsadmin-webui-live0311` |
| 4 | `vpsadmin-webui-0312` | `vpsadmin-webui` |

Use the existing ordinary Git move/inventory method, independently proving
before/after full heads, branches, common Git/registration identity, inodes,
tracked bytes and ignored locks/private file digests/modes. Destinations must be
absent. Preserve whole 0.31.1 predecessor checkouts/refs/private state, existing
`*-live030`, older 031 aliases, and all unrelated entries. Lead owns whole-entry
portal remapping/public sync. No moves while current virtiofs/QEMU remains live;
stop and reconcile any refusal without force or an automatic retry.

Later released config preservation/init/restore, final canonical no-write graph,
kernel-cache/capacity/address/ownership checks and minimal existing driver
constant rebinding follow E4's accepted method; no services-switch mechanism or
new framework. Resident32GiB/12CPU with Nixjobs1/cores2 and separate daemon
headroom are the prior adopted bounds, subject to fresh release-time checks.
Public reset/start remain parent-owned. F remains uninstalled in the last
accepted pq2/vh650 generation; generation and inputs must be checked freshly
when released. Keep the provider certificate/root limitation explicit and prove
four guests independently with public SSH -n, no root repair. Embedded path-input
unknown metadata requires independent complete source/input/output proof for
qualified dev use; it does not pass the clean-release packaging gate.

Postboot scope reuses E4 TLS/member login/read/logout and exact packaged/source
proof, plus the adopted Go token-panel acceptance for the 0.31.2 String/Symbol
transport-name remedy. Actual Go existing-token documentation proof belongs to
the newly selected deployment; archived package source parity alone does not
establish it. No broad client/browser campaign or guest mutation is implied.

KB0.31.2 is separately staged/verified and retained owned/up; see
[staging receipt](../package-0.31.2/staging/receipt.md). It supplies no deployment
clearance. No further KB checks/reset/release/promotion are assigned. Current
cluster/scope/roots/KB staging/session remain running/open. Lead will release the
complete fresh preflight/execution package after source gates; until then wait.

## Historical E4 released read-only preflight, from 22:57 UTC

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


## E5 followup: peer HaveAPI documentation deployment preparation

Preparation only, 2026-10-28. User authorization to deploy the other session's
version when ready persists; no second deployment confirmation is needed.
Peer35c1fb9 is only a source-contract reference: no peer source was fetched,
selected, pinned, built or deployed. Await its final test-only successor SHA/tree,
architect0's source/packaging/OAuth brief, and A0's final reviewed consumer,
affected checks and no-writer handoff. All five sibling gems must bind that one
revision with make-doc-generated assets. TSclient0.1.1/runtime0.30.2 stays separate.

Current public wrappers select runtime
`/nix/store/mw2fa43yyjar8hcl5h2zckrjg79rl915-dev-workspace-0.2.0` and provider
`/nix/store/n16b9dxgp5fx3g5xjfvpp00acaybsyzn-vpsfree-dev-workspace-tools-0.1.0`.
Read selected `share/dev-workspace/coordination.md` and provider
`share/vpsfree-dev-workspace/dev-clusters/vpsadmin/README.md`; catalog
`2dd2cf816ede4410b330c6181aef8b9b3001a6f80a00d7477a3261670c6f0c4a`.
These replace the guide paths for future preparation, not E5's historical
pjmi/kbppy execution proof. No payload equivalence or F-fix selection is inferred.

The minimal candidate is ordinary public `vpsadmin-devcluster update <slug>
services` after architect disposition proves state/schema compatibility and an
ordinary final-source binding preserves the canonical checkout inode and live
PHP bytes. The provider selects literal `worktrees/<slug>/vpsadmin`; a separate
alias alone is insufficient. Preserve E5 source refs/checkout/private ignored
locks, exact selected config/system/deriver/full graphs and normal roots in the
existing receipts. Future private preservation records only the documented
editable config and necessary application secret/config files, with 0700/0600
ownership and digest evidence, never contents in tracking/Git/Nix store.

If safe source binding or update compatibility cannot be established, use the
existing parent-owned reset/rebind/config-only restore/new single-bridge start
sequence after a concrete design disposition. Preserve unchanged WebUI sources;
do not repeat four moves merely because E5 used them. Never rename mounted live
checkouts, copy applied envelopes/disks into replacement state, or reset to evade
an uncertain/pending operation. Update failures keep the target pending and use
the original copy/activation/refresh recovery; selected labels are not live proof.
Immediate generation/ownership/pending/runner/kernel/cache/capacity/address
checks belong at execution time. Old driver guards require later reviewed
rebinding, not execution now; retain containment/redacted logging and Nix1job/2cores.

The selected provider has only the React-specific OAuth credential bundle/seed;
there is no documented dedicated docs-client provision/config selector.
Architect0/A0 must supply ordinary OAuth2Client Create/Update, the exact docs
HTTPS callback/scopes/lifetimes/ownership and repeatable private persistent
config/api.rb configure-before-mount secret delivery. Do not reuse BFF/PHP
credentials, write raw DB rows or add private-provider commands. No client was
created and no private config/credential was read during this preparation.

After parent activation/completion handoff, send actual native package paths,
derivers and one complete source/input graph to the independent provenance
owner; prove all five gems and generated assets, with separate unchanged SDKpair.
Reuse four independent public SSH-n current/booted/closure/root reads, then the
existing strict-CA curl and isolated-NSS Chromium member login/read/logout
mechanism in one bounded batch, extending only the architect's docs/OAuth flow.
Keep contexts separate and flows sequential; record only sanitized status/path
facts, never password/token/cookie/code/secret, callback query/fragment, HAR,
screenshot or trace. CA trust is isolated; never ignore HTTPS errors or change
host trust. Deliver the public CA path/fingerprint and private credential-file
access instructions, not credential values. E5 URLs/CA facts are historical
until the future activation verifies them again.

[E5 accepted runtime proof](e5-runtime/receipt.md), its full6749 graph and C1
native chain remain the baseline. Preserve the F retained-boot/root certificate
and unknown embedded WebUI metadata limitations; no reopening or repair claim.
No live native/status/guest/DB/HTTP/resource/CI query, preservation, source move,
config edit, client creation, driver/build/start or peer-resource action ran.
Only this preparation note changed; lead owns state/handoff. Await final source,
review and execution handoff. Existing HTTPS cluster, KB previews and session
remain running/open.


### cba62658 / DEV-R1 operational preparation update

Static preparation only. Source review/remediation is accepted at consumer
`cba626581a698256e873319983ac51312f40398c`, tree
`40375b83d5077e0fe16c0c47b8307ff467a82b4f`; all five HaveAPI gems remain on
the immutable d67 source. A0 still owns actual API outputs/docs/services checks,
publication and final no-writer handoff. No cluster/source activation is released.

Actual selected public runtime is now
`/nix/store/kdqm98kwk1mly4i1rfx58lnz6cscn6z6-dev-workspace-0.2.0`, provider
`/nix/store/ih7nwsm62rcvkv99p5m20kzi1q9fyfsa-vpsfree-dev-workspace-tools-0.1.0`,
catalog `89a06f899d10aaf911a6e51a960ea1f6fff5ca9f9c1a5a0f83a69247db73fbad`.
Their public coordination/native guide bytes match the previously read guides;
this establishes guide reuse only, not implementation equivalence or an F fix.
`update <slug> services` retains build/copy/activation/restart/refresh/target
proof and original pending-target recovery. Canonical-inode/live-PHP-byte
preservation plus normal source registration remains the gate for using it.

DEV-R1 sends the entire primary API virtual host directly nginx→HAProxy;
auth/PHP/React remain unchanged. The dev/test metrics60s Varnish cache is
intentionally lost. Native test.nix imports the consumer services module and
only overrides the primary api.test domain, supporting inheritance of the fix.
However, selected native test.nix:1541–1545 still explicitly sends the maintenance
API alias (tmpDomains.api) through Varnish. Lead/architect must disposition that
alias's docs credential/callback exposure before enabling OAuth; no all-alias
VSL-safety claim is made. Bind final actual nginx/HAProxy route/configuration to
the applied closure, including native overrides, rather than relying on source
or selected-result labels. Rollback must preserve the direct route while docs
OAuth is enabled, or first retire that exposure with matching old API config.

Later ordered operation, using existing mechanisms: after A0 handoff, preserve
the prior refs/private regular config and closure/input receipts, then perform
the approved inode/PHP-preserving Git binding and normal registration. Provision
only the exact owned documentation client through ordinary admin Oauth2Client
Create/Update: nondefault, confidential, fixed3600, no refresh, SSOoff, exact
`https://api.aitherdev.int.vpsfree.cz/_documentation/oauth/callback`. Deliver
protected persistent `config/api.rb`, adjacent `documentation-oauth.json`
(client_id/client_secret/redirect_uri, switch_user initiallyfalse) and stable
worker-shared `documentation-session.key` of at least64bytes by public services
SSH/protected stdin/atomic placement with restrictive API-readable permissions.
Load through the existing configure-before-mount hook; no values enter argv,
tracking, Git, Nixstore or raw logs. Scope remains all. Enable switch_user only
after fresh editable account entry is actually proved. Parent owns the public
services update, containment, original command handle and effects reconciliation;
reset/rebind remains the separately dispositioned fallback.

Use the existing bounded strictCA/isolated-NSS docs and both-UI acceptance batch.
Open a bounded, demonstrably working observation window for nginx, HAProxy
journal and VSL before login/callback/revoke. Check nonsensitive unique request
markers and response markers, and compare actual sensitive request query/header
and response Location/Set-Cookie values privately; retain only absence booleans,
counts, window bounds and route/closure identity. Missing reader/window coverage
is incomplete, never PASS; never save a raw credential-bearing VSL/log dump.
Final OAuth-only HTML/mixed-identity assertions follow settled d67 design,
not the superseded Basic-first brief. Bind native five-gem/generated assets,
actual services/roots/concurrency and private config ownership without repeating
peer matrices. Restore any bounded owned expiry fixture to3600. Existing F/
embedded-metadata limitations remain unchanged. Immediate freshness guards and
all runtime/client/config/log observations wait the released execution package.
Only this record was appended; no live probe, CI query, config/client creation,
preservation/rebind/build/native or cluster mutation occurred.


M8 fresh read-only preactivation guards and exact next boundaries are recorded
in [m8-preactivation/receipt.md](m8-preactivation/receipt.md). The2a4/e5ea
package/services lineage remains exact; reported FINAL511 awaits architect reuse
and A0 final pin/publication/no-writer handoff. No mutation is released by this
receipt or by passing the historical/live guards.


### Sign-out successor90e2/2f6: conditional activation preparation

Preparation only under the lead's standing deployment release. Exact target
consumer90e2a79092bad36ee1e444931f48178e6de8d7d3,
tree511b6fe3dc315bf4f178c3ddf951aea08cc719ea; HaveAPI
2f6c18a80f3a5f8ce46449ff81183b100b60f34c,
treee526e62753d6c18218074995761a944e6e61bdd5, common source hash
1j6nqkk18imxafy34xcxwkx81n4dr68ahhl3kzbxp6blliwla7hl,
full lockddb00294b01393e228e5aa20cd3173a8a909c61ae210a804194334db26c81f14.
Accepted source/quick/affected review is distinct from A0's still-required new
actual package/all34/effects/guarded SSH publication/no-writer handoff.
No binding writes until that actual handoff is verified, with A0 Git ownership
ended. Preserve original59d/511 and8102 refs/roots/private data and the original
[m8 runtime failure/partial passes](m8-runtime/receipt.md).

Reconfirmed retained E3 Sol/xhigh/workspace_write, bound slug and absent ambient
identity variables. Public coordination guide still selects runtime7wqvb8wdy58x94nh24k0kqnagqldfhvi,
catalog4fe07f1f834009f2ba2b82f125458879a1f44abab33af6c0885f2aaeaa77150e;
selected provider2flmy0zcmz59g1g35k0jm1czfvx3cdn1 native guide/recovery contract
is retained. This is guide/selection binding, not provider payload equivalence,
live freshness or F-fix proof. Fresh owner/pending/runner/source/inode/private
byte guards belong immediately before the released transfer/update.

The existing ordinary mechanism can transfer branches without mounted-path
moves: first public-register A0's existing isolated docs-signout branch under
vpsadmin-haveapi-dev (ordinary worktree add, existing ref, no guessed --base),
then isolated `git switch --detach 90e2a79092bad36ee1e444931f48178e6de8d7d3`,
canonical `git switch 2026-10-24-vpsadmin-haveapi-upgrade-docs-signout`, and isolated
`git switch 2026-10-24-vpsadmin-haveapi-upgrade-devdocs`. The latter retains an
ordinary59d/511 rollback checkout at the isolated inode, plus8102's existing
vpsadmin-live0312. Preserve the two complete registration entries by simultaneous
name mapping oldcanonical→vpsadmin-haveapi-dev and successor→vpsadmin, then public
sync. Old devdocs base/comparison fields remain intact; an unknown successor
historical base stays unknown. If A0's final handoff already supplies an exact
registration, reuse it rather than add another. No force, skip-worktree,
shared-master edit, checkout movement or hook bypass. A refusal stops dependent
operations; inspect actual effects before any correction.

Use the original private preservation/inventory mechanism for canonical inode
51940894,446 live PHP/template/static files/dependencies, private/ignored files,
mode/type/lock/ref/registration identities. Save old ignored effective lock
privately, install only A0's final exact new effective API lock at canonical
and retain old3f0f lock with rollback59d; tracked packaged lock follows checkout.
Client3 remains nondefault/confidential/fixed3600/no-refresh/SSOoff; callback,
reviewed protected hook/JSON, stable64-byte key and current switch setting remain
unchanged. No client recreation, new secret delivery or config/restart is needed
before the parent update. All new raw/private artifacts must be0700/0600 outside
tracking/portal, beneath the existing private preservation hierarchy; only
sanitized compact summaries belong here.

Update-ready command for the parent, after final source/input/ownership guards:
`DEV_SESSION_SLUG=2026-10-24-vpsadmin-haveapi-upgrade DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz vpsadmin-devcluster update 2026-10-24-vpsadmin-haveapi-upgrade services`.
Parent retains containment/Nix1job2cores/redacted original logs and pending-target
recovery; E3 does not invoke update. On copy/activation/refresh refusal, preserve
the original pending services target and effects, never reset to bypass it.
Rollback59d retains known signout defect;8102 rollback first retires optional
docs config so it cannot restore a Varnish credential path while OAuth is enabled.

After authoritative parent success, bind new actual applied package/paths via
A0's deployed-lineage handoff without duplicate graphs. Reuse mixedidentity/
OPTIONS/PHP/React/UI passes only at unchanged source/config scope. Run only
remaining affected acceptance: actual rendered document Referrer-Policy
strict-origin; sensitive login/callback/logout/error no-referrer; generated
normal forms with real exact Origin and matching policy/DOM facts, no injected
Origin. Prove ordinary Sign out and Switch user, successful token revocation,
local+pending cookie clearing, fresh editable account entry/callback, owned short
fixed expiry→anonymous→relogin, then restore client3600 and read back. Keep exact
worker/thread identity/cleanup attribution separate from cross-request HTTP
behavior; do not infer it from keep-alive or two-worker Puma scheduling. Use
existing protected logging window, strictcurl/isolated NSS, ordinary OpenSSH
protected stdin, no raw secret-bearing artifacts in tracking. Final owned docs
sessions must be reconciled/revoked through ordinary routes; no accountwide
cleanup. No provider/CA/source repair or new driver/test framework.

No live native/status/guest/HTTP/capacity probe, source/ref/registration mutation,
client/config/key change, build or watcher was launched for this preparation.
Lead owns state; cluster, KB and session remain running/open.


Resume identity rebind: accepted design.md “selected runtime d0wi/provider r2vd
update compatibility” supersedes only the explicit7wq/2flmy bindings above.
Current runtime `/nix/store/d0wikyzpr7qk1w2c2zbqgj97qz1m58qn-dev-workspace-0.2.0`,
provider `/nix/store/r2vdj3ib32pryx8n0cb1104adw5c4xn1-vpsfree-dev-workspace-tools-0.1.0`,
catalogaf53ccceb927a13cce1bed4ef27a6b236a2b24067b6ac481c4876a5d09d27c07.
Architect's accepted bounded equality preserves schema1/policy3/authority1 and
8MiB bound, public update/generation/pending/recovery and protected-stdin fallback.
Parent still runs the public `update <slug> services` command, never the old
start-only activation driver. Discard stdout; private0600 stderr with sanitized
allowlist only,32GiB/12CPU/zeroSwap/Nix1job2cores. Source/private/PHP/ownedcluster
fresh guards wait actual A0 all34/effects/publication/no-writer handoff. No
installed-source comparison, stdin fixture, live probe or mutation repeated.


Successor source binding executed2026-10-29; update-ready17:35:19UTC. Canonical
is exact90e2/tree511b6/full ddb002 at preserved inode51940894, isolated ordinary
rollback59d/devdocs at inode51976902;8102 remains at vpsadmin-live0312. Both branch
switches0, whole registration-entry name remap has exact inverse byte proof,
public sync0. All446PHP bytes and15780/13084 private-ignored entries preserved
except the intentionally transferred effective API locks. First detach performed
its branch effect then refused Overcommit trust; accepted config/customhook bytes
verified, normal bundle exec overcommit --sign under retained declared root env
and original post-checkout completion0, no checkout repeat/bypass/install. One
incomplete ambient gem environment attempt is retained as a local tooling error.
Fresh pendingnull/owned runner1531763/start1249236374/all4QEMU and currentxlwl,
config10819c plus protected API hook/JSON/stablekey hashes/0600 unchanged. Selected
d0wi/r2vd public bindings verified. Actual raw logs/inventories/heads/registration/
update-ready records are private0700/0600 under the existing preservation root's
signout-90e2 directory. One direct public-status tool stdout exposed seeded dev
account fields; no rawstatus/seed artifact was written to tracking/portal and no
OAuth secret/key was output. Subsequent status capture used a private-first
whitelist; tool history is not relabelled sanitized. No updater launched by E3;
all owned handles consumed, parent has literal public update-ready bindings and
original same-target recovery. Affected browser acceptance waits authoritative
parent update success. Source binding is not running90e2 proof.


Successor actual deployment and affected OAuth/same-thread/session-cleanup acceptance
completed: [sanitized final receipt](m8-runtime/signout-successor.md). Parent original
update2512/native1920050 completed0; actualxqd5/API0k8v/2f6 bound independently by
A0. Native form/policy/revoke/switch/expiry/relogin and controlled installed samePID/
thread/Fiber four-call invariant PASS; all seven owned verification sessions closed,
client3final3600/config/key unchanged. All owned operations/readers reconciled; no
cluster/session/KB lifecycle action or direct productionPuma-worker attribution.
Raw/private captures remain outside portal; prior failed evidence is preserved.


### Example-style1b successor: prepared bindings only

Read design.md “2026-10-29: example-style successor — bounded consumer adoption”.
Producer target1b264e25a73a0ab9bca5f847bd52254f74e0931c /
treedcdba06a92fe0d8a577f4cffe46ea69fc8d73a40; final consumer SHA/tree/full lock
and actual output paths remain pending A0 handoff, never guessed. Current working
90e2/2f6 deployment and [complete acceptance](m8-runtime/signout-successor.md)
remain intact. Retained E3 Sol/xhigh/workspace_write and exact session binding
confirmed. No live/runtime probe or source/ref/registration/client/config/key
mutation is released during this preparation; A0 owns isolated style worktree.

At the later lead-released boundary verify actual committed affected review,
new five-gem/API/frozen package proof, ONE34/native effects, exact ordinary SSH
feature publication and no-writer handoff. Reuse the existing immediate source/
private/PHP/owned runner/socket/pending guards once. Rebind concrete selected
runtime/provider at that boundary only; accepted d0wi/r2vd remains baseline.
Preserve canonical inode51940894/all446PHP/private files, root/API locks,
client3fixed3600/no-refresh/SSOoff/callback/stablekey/protected configuration.
No new OAuth session, TTL fixture, credential delivery or rotation is needed.

Use ordinary exact-final branch transfer without mounted path moves: detach
A0's final vpsadmin-haveapi-style/docs-style branch, switch canonical in place
to that exact branch, then attach the style worktree to old docs-signout90e2.
Preserve its own ignored effective lock with each selected revision. Retain old
vpsadmin-haveapi-dev59d/devdocs,8102/live0312 and all older recovery refs/roots.
Preserve whole registration entries through two-name mapping oldcanonical→
vpsadmin-haveapi-style and successor→vpsadmin, preserving every branch/base/
comparison field; reuse existing registration if A0 supplies it, then publicsync.
Do not infer historical initial bases. Ordinary refusal effects must be reconciled
before correction; no force/reset/bypass. Keep raw logs/inventories private0700/
0600 outside tracking; only sanitized facts/hash references belong in records.

Parent alone launches the unchanged supported public command:
`DEV_SESSION_SLUG=2026-10-24-vpsadmin-haveapi-upgrade DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz vpsadmin-devcluster update 2026-10-24-vpsadmin-haveapi-upgrade services`.
Retain Nix1job2cores/32GiB12CPU/zeroSwap, stdoutdiscard/private sanitized stderr,
original handle and same-target pending copy/activation/refresh recovery. No old
start-only driver, native reset or source repair. Working90e2/2f6 rollback keeps
matching direct route/private config;59d/511 retains known old signout failure,
and8102 retains optional-docs-config retirement requirement.

After authoritative parent0, share sanitized applied/status paths with A0 for
actual five/API/closure/source lineage reuse; no duplicate full graph. Confirm
unchanged relevant OAuth/helper/server/proxy/config/publicasset/guide/gemspec
identities before reusing prior actual OAuth/forms/revoke/expiry/relogin/
controlled-thread/privacy/PHPReact/UI results at their exact scope. Architect's
source equality establishes candidate reuse; actual deployed binding is still
required. No producer-style/full SDK/compiler/profile/OAuth/browser matrix.

Focused served-format batch uses the existing strictcurl--cacert panel mechanism
and synthetic public placeholders. Three existing routes suffice: overview/
initialization `/v7.0/`, auth `/v7.0/?page=authentication`, public action
`/v7.0/?resource=cluster`. Reuse panel IDs `init-2`, `auth-basic-2` and
`-thorough`, `example-cluster-public_stats-0-2` (plus its detail variant), Ruby0,
Python sync/async, Go and typescript-generated. Check representative PHP Simple
and With-error-handling single quotes, four-space indentation and blank lines;
Ruby authored single quotes/separators, Python import/top-level spacing, Go tabs/
import-group separation, and typedTS spaced imports/objects/double-quoted module/
auth literals. Concrete twoTS contracts: `import { createClient } from
"vpsadmin-typescript-client";` and `runtime.authenticate("token", { token:
"example-token" })`, plus unchanged public_stats call/values. Join existing HTML
highlight spans normally, preserve code whitespace for formatting assertions and
save first bounded outputs privately before assertions. Bind assets to actual
new installed outputs; identical public CSS/JS source is reused without a UI
sweep. No code execution or API action occurs when reading generated examples.

No producer/source/app/runtime/cluster/KB/default/release/lifecycle action ran.
Final artifact identities/review/native/publication/no-writer and lead execution
release remain pending; current cluster/session/KB and full90e2 acceptance stay
running/open. This note is preparation, not source-transfer or deployment proof.


Style source transfer executed2026-10-29; parent UPDATE-READY19:57:40UTC.
Canonical exactaae07e/tree37ba/full259403 on inode51940894; style checkout now
working90e2/docs-signout rollback on inode52078028.59d/511 and8102/older refs
unchanged. All3ordinary checkouts/hooks0; effective locks deliberately followed
selected source, whole-entry two-name registration remap/inverse byte proof and
publicsync0. All446PHP and15780canonical/12133style private-ignored files unchanged
apart from those effective locks. Fresh owned runner1531763/start1249236374/
all4QEMU/socket/config10819c/pendingnull/publicready/currentxqd5 and protected
hook/JSON/key0600 exacthashes proved; no client/config/key/OAuth operation.

Actual selected runtime at this boundary is g650vgjpzvyifjmb1j44pc5bby3522z4,
provider d50zvmwmvdj0j35pwcmaarcwyq3fqpqj, catalog410a01491f4e2f8a44686d3687923bd596bb544570112ae6dd535c981bd26193.
Selected coordination guide read and byteequal; schema contract and four public
cluster dispatch/generation checks match d0wi. Native command/README/runtime.sh/
maintenance/test/flake/runner/contracts match r2vd; provider wrapper exec path is
the only wrapper difference. This bounded interface/source proof rebinds the
existing public services update and original pending recovery, without a whole
package equivalence/F-fix claim. Raw guard/inventory/checkout/remap/update-ready
records are private0700/0600 under the session preservation tree style-1b.
No updater launched by E3; all handles consumed. Parent received literal public
command/env and32GiB12CPUzeroSwap/Nix1job2cores/protected-output bindings.
Current running90e2 OAuth acceptance stays unchanged; scoped served-style check
waits authoritative parent success and actual deployed-input binding.


Style successor parent update91432/native4105502 completed0 at20:13:57.878378UTC.
E3 actualapplied/current6dsi/API6qr8/bgwp/aae/1b/full259403/pendingnull and
unchanged private/auth/proxy input binding PASS; exact3strictCA served routes
and20format assertions PASS. [Scoped sanitized receipt](m8-runtime/style-successor.md).
PriorOAuth/privacy/PHPReact evidence reused only for unchanged relevant inputs;
no new login/session/TTL/action execution or broad campaign. All E3 handles
reconciled; A0 separately owns actual five-output/source/graph/closure lineage.
Cluster/session/KB and protected OAuth state remain running/open.

## 2026-10-30: released0.32 development update preparation (read-only)

KB overview is complete separately: [step05 receipt](../kb-restructure/overview/staging/receipt.md).
This preparation follows `design.md:4311`, especially its final E3 boundary.
Session/retained Sol/xhigh/workspace_write identity was reconfirmed. Selected
runtime is `/nix/store/d97nazmvhm2a2m3jn8ichid4ksannliq-dev-workspace-0.2.0`,
coordination catalog `f0188e28ef09cea1410c21f723a77ad2bc1e133d6f6e258af26eed0e058bfce7`;
its extensions bind provider
`/nix/store/4x0rwzn96xycjb8z4pjpg0z1kimc36d8-vpsfree-dev-workspace-tools-0.1.0`.
Selected coordination/deployment/lifecycle guidance and full native README read.
Bounded comparison to accepted g650/d50 found exact bytes for native
`dev-clusters/vpsadmin/bin/devcluster`, shared runtime.sh, README, test.nix,
flake, runner/maintenance files and runtime-contract.json. The coordination
body is unchanged. This proves the relevant public update/recovery contract,
not whole-package equivalence or a provider-F repair.

Static selected `test.nix:1731–1843` puts PHP in `containers.webui`, forces
`sourceCodeDir=/run/vpsadmin-live-webui`, and orders
`vpsadmin-webui-live-root` before PHP-FPM/nginx. It links authored entries from
`/mnt/vpsadmin/webui`, skips mounted vendor, and links vendor plus .git-revision
from `config.vpsadmin.webui.package`. The regular-vendor merge at1435–1495 is
instead the vpsFree website `/mnt/web` path. Thus this route needs A0's new
exact-lock noDev PHP package, not a canonical ignored-vendor refresh. At the
released boundary bind the actual selected/applied unit and resolve the actual
vendor package; installed source alone is not a live-unit claim. Preserve true
config/secrets and unrelated authored PHP, while allowing the reviewed Composer
metadata and intended dependency artifacts to change. Do not retain old
HaveAPI merely to satisfy the earlier blanket446-file equality check.

Last verified working recovery remains canonicalaae/1b/full259403 at inode51940894
([actual style receipt](m8-runtime/style-successor.md)); preserve it and its
private effective lock/refs/roots alongside90e2/2f6,59d/511 and8102. This note
makes no fresh live-status claim. Client3 remains nondefault/confidential,
fixed3600/no-refresh/SSOoff with existing callback, stable key and protected
hook/JSON; no client/key/config change is planned. Oldaae includes the reported
shell weaknesses and is recovery evidence, not security clearance.

Await A0's exact final0.32 commit/tree/effective+packaged locks, affected final
review, actual all-five/API/docs/frozen bundle plus CLI/download/PHP/console
package identities, ONE34/effects, ordinary SSH publication and no-writer
handoff, then lead release. Keep A0's Git/worktree exclusive until handoff.
At that boundary use the original private inventory, source/owner/pending/
runner/socket guards and inode-preserving branch transfer/whole-entry
registration remap/public sync. Preserve each rollback's own effective lock,
all private/ignored files and true configuration; do not guess historical bases.
Guard failures retain original effects, never authorize reset or bypass.

Parent alone launches:
`DEV_SESSION_SLUG=2026-10-24-vpsadmin-haveapi-upgrade DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz vpsadmin-devcluster update 2026-10-24-vpsadmin-haveapi-upgrade services`.
Retain Nix1job/2cores,32GiB/12CPU/zeroSwap, discarded stdout/private0600 stderr
and sanitized reporting. Public update records pending before copy/activation,
then API restart/Node refresh and exact-system/rooted-closure proof before
promotion; same-target original pending recovery remains parent's responsibility.
No old start driver, lifecycle/CA/provider action or new deployment framework.

After authoritative parent success, coordinate actual applied/system/source/
all-five/API/CLI/PHP/console/vendor0.32 binding with A0 without duplicate graphs.
Use existing strict dev-CA/NSS capture for representative served CLI/curl escaping
and inert response transcripts; any copied-command check is local argv-only,
never a real API action. Repeat bounded normal PHP login/read/logout because its
dependency changed. Reuse OAuth/thread/privacy and React only after exact actual
relevant source/config/dependency equality; consequential dependency differences
need targeted validation. No default TTL/mixed-identity/full-UI matrix. Preserve
main-origin/direct-route/noalias/log-window and private-evidence contracts.

No live cluster/status/guest/HTTP/resource query, source/ref/registration change,
client/config/private write, build, update, restart or production action ran.
Static preparation is ready; final identities/release remain the dependency.
Hold idle without a watcher or poll until the final handoff and lead release.

### Released0.32 source transfer — UPDATE-READY

Actual canonical is `33d6c7723b392c828de2165854d106d9528f9305`, tree
`ffab19170fee23226eced451ba18776c01273e84`, branch032, inode51940894.
Effective and packaged full API lock:
`ea0a24b176bd3526288fa217dbd43f38e715fe7c3b9f468a94682015559fa0a1`.
One public final metadata read (IFD=false/max-jobs0/no lock write) resolves
exactly A0's `/nix/store/qg5xmw0353wci8x6mp0ycris5m3lxizs-source`,
NAR `sha256-YbtMmXT2QSGt/TI2laas2KyNDkgEi4uZayliuUkwzeY=`, complete9-node
input graph retained with the private update-ready receipt. No whole-graph
rebuild or package relabel was performed.

All three ordinary checkouts completed. The first detached33d6 but its normal
post-checkout refused a changed Overcommit signature; exact reviewed project
configuration/hook equality was checked, ordinary `overcommit --sign` and the
original post-checkout verification passed in A0's prepared Nix shell. No
checkout was repeated or hook bypassed. Subsequent canonical/rollback hooks0.
Normal shell setup left existing ignored files and path inventory unchanged.
Both root/API effective locks now follow their own source. Rollbackaae/docs-style
is at vpsadmin-haveapi-032, inode52098765, API lock259403; existing90e2/59d/8102
and React2e32 heads/inodes/roots remain. Shared-master integration was not run.

Whole registration entries changed names only by exact two-name remap, with
inverse-byte proof and all base/comparison/unrelated fields preserved. First
public sync refused admission because another same-session command held the
lock; no sync effect occurred. Ordinary same-source retry0, final manifest
exactly equals the remapped whole entries. Canonical initial base remainsac10;
rollback's initial90e2 base is retained, with no invented historical base.

Fresh own runner1531763/start1249236374, five exact native flags, recorded
socket and four QEMU descendants passed. An initial name-only classifier
missed actual qemu-kvm processes; it was corrected before any source mutation.
Public status before/after is running/ready and authoritative applied pending
is null. Running system remains old6dsi; no deployed0.32 claim is made. All
three guest protected regular0600 UID992/GID990 hook/JSON/key hashes and types
match before/after. Client3/3600/key/config were not changed or reprovisioned.

Private inventories15780 canonical/23368 isolated are exact except the two
source-owned effective locks each. Of446 tracked PHP paths, only Composer's
three metadata files and webui/public/js/haveapi-client.js changed as intended;
442 unrelated paths and all ignored vendor files are exact. The console JS
change follows the reviewed33d6 tree. Actual new package/vendor selection is
a post-parent-success proof, not a canonical ignored-vendor refresh.

Parent received UPDATE-READY and exclusive writer handoff immediately. Literal
public command/environment and Nix1job2cores/32GiB12CPUzeroSwap, stdout-discard/
private0600 stderr and original same-target pending recovery stay unchanged.
All E3 handles are consumed, no active operation or source writer remains.
Private0700/0600 records live only under
`.dev-clusters/vpsadmin-preserved/2026-10-24-vpsadmin-haveapi-upgrade/released-032/`
(`update-ready.json`, final metadata, inventories, hook/checkout/sync effects).
No native update/restart/client/config flow or production/lifecycle action was
launched. Wait for authoritative parent success before affected live acceptance.
