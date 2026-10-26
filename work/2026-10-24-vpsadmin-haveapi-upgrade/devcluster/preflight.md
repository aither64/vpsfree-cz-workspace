# Package E preparation receipt

Prepared on 2026-10-26 for session `2026-10-24-vpsadmin-haveapi-upgrade`,
workspace `/home/aither/workspace/ai/vpsfree.cz`. `dev-session current` and both
environment bindings match. **Preparation complete; activation has not been
released by lead.** A/C verification and lead source/performance acceptance
remain separate gates. No cluster start, reset, reservation, deployment, private
helper, host configuration, project source/ref change or KB mutation occurred.
Main state/portal and commits remain lead-owned.

## Current installed generation and inputs

The selected package changed during preparation. Earlier JSON files remain
historical evidence; the additive `runtime-refresh/` evidence records the
currently selected generation:

| Item | Current identity |
| --- | --- |
| Runtime | `/nix/store/fa7zlb2z311w9p8y9wygaqxpmq086s9b-dev-workspace-0.2.0` |
| Provider | `/nix/store/7vrkd2yg349dsqq3hwmwpmcw86nrvq6s-vpsfree-dev-workspace-tools-0.1.0` |
| Coordination catalog SHA-256 | `34365aa1899ce1ff4e74c87aa76f3cf85410efefa5eb9317814269f88f69efd0` |
| Native runtime contract SHA-256 | `9c8e9e5c371eda46ccb49eaf275ee4996d2ddce3930c9047da39ccd195f67183` |
| Native state/transition policy | schema 1 / policy 3; status schema 2 |
| API worktree | clean `70a2ed54b98d0c2f359a9cc4484452a257a9807b` |
| React worktree | clean `f10d3d48c4f21cc39187c3667ffffd9952404c11` |
| Native OS `origin/staging` | `d9be8c4bada590c0405df85444600d40e6f3caa6` |

All 42 files of the installed provider's `dev-clusters/` tree are byte-identical
to the prior `wahwpzf7...` provider, including shared ownership code, launcher,
flake, README and runtime contract. The newly selected installed guides and
provider README/contract were reread. No package switch was performed by E.
See [contracts, sources and roots](runtime-refresh/contracts-sources-roots.json).

Public `nix flake metadata` with `allow-import-from-derivation=false`,
`max-jobs=0` and `--no-write-lock-file` succeeded in 22.12 seconds. The complete
20-node lock graph equals the prior graph. Its source remains
`/nix/store/kvr5zvhzdd03ps2lb9fbw8k5gvz9hk1d-source`, NAR
`sha256-SxA5jLINqum9hG3IpkFIwv5LivBi2Sck1ZRf72GOCwg=`. Fresh metadata SHA-256:
`d44231e219f322207829c96826fe6e7c434059a27f19be01e7595e7bdf40fc31`.
See [full graph](runtime-refresh/effective-flake-metadata.json) and
[comparison result](runtime-refresh/metadata-check.json).

Only our API and React worktrees are selected. There is no session OS or
HaveAPI worktree. Native selection overrides both OS input paths with the
canonical bare `origin/staging`; API's standalone OS lock is
`8e44a5124439b1f3048ffc56b1717614a5360358`. Effective stable nixpkgs is
`1f607aa79b6356ed45d3cd3c8079c196e79efa2c`, unstable nixpkgs
`3ec636362e1816bc2f0888fa0fa2c69f1bc9e504`, vpsfStatus
`0210b0556f6ec95fb8a9d01da867b58a298948af`. Lead provisionally accepted this
native graph and its distinction from standalone verification. This receipt
does not claim reuse of standalone build artifacts. Runtime/provider identity
changes and the unchanged graph were reported to lead for reconciliation.

## Owned stopped state and collision observations

At 09:58 UTC, public native status reports stopped, ready=false, empty topology
and network. Only `config.json` and `socket-dir` exist. Config SHA-256 remains
`10819c2d393795f4909695f04e4caf3d4035a94e84e25c871ecfc1ab19a16332`.
The recorded socket `/tmp/vpsfree-devcluster-02da06564216` matches the complete
workspace/slug digest and is absent. There is no runner PID, result, applied
selection, disk, WebUI credential bundle or maintenance/pending selection.
Config/URL commands were not invoked during this preparation phase: their
earlier initialization side effect is retained, not repeated or reset.

The refreshed host scan found no QEMU or VM-test runner, including no observed
legacy A guests. `br0` is up; KVM is readable/writable; the bridge helper is
executable and its policy allows `br0`. Available memory was 54.0 GiB, with
64 logical CPUs and approximately 131.8 GiB free filesystem space. Lead accepted
a 32 GiB / 12 CPU budget for 18 GiB guest memory / 10 guest vCPUs plus overhead.
That budget has not yet been applied to an activation operation.

Fixed IPs `172.16.106.53`, `.41`, `.61` and `.62` returned no ICMP reply and
accepted none of the tested TCP connections (services 443/22, other guests 22).
All four neighbor entries were INCOMPLETE. PHP and React names both resolve
to `.53`. These observations show no responding collision; they do not prove
exclusive address ownership or reserve addresses. The native launcher has
per-cluster tuple checks and a services-IP ping refusal, without an exclusive
global address registry. No foreign mutable cluster records were opened.
See [sanitized native/host/network evidence](runtime-refresh/preparation-recheck.json).

Public coordination status returns no own active claims or reservations and
one foreign held physical-host reservation, `vpsfree:aitherdev`. This was
reported to lead for coordination before activation; E requested no claim.
See [sanitized public control-plane summary](runtime-refresh/coordination-active-redacted.json).

## Evaluation, kernel availability and retained roots

The selected OS exposes `overlays.all`, per-disk preservation/rootDisk support
and `vpsadminosRubyGemConfig`; see [contract evidence](os-package-contract.json).
Complete cluster derivation evaluation deliberately stopped at IFD, exit 1,
after 107.19 seconds: the API source derivation needed realization. No build
was enabled. Exact full cluster derivations/payloads remain unproved until the
ordinary authorized native start. Lead accepted this limitation; the private
build helper and an IFD-enabled preparation run were not used.

Independent kernel-only evaluation with builds/IFD disabled succeeded:

| Default kernel | Derivation | Existing output and public cache |
| --- | --- | --- |
| Node/QEMU 6.12.113 | `/nix/store/s43jw77l0w9zb90ydxxhzhzqzswgmnmc-linux-6.12.113.drv` | `/nix/store/4k5kg0x1msvl4kffpr2g7cidpnwbnkhk-linux-6.12.113`; cache.vpsadminos.org |
| NixOS 6.18.57 | `/nix/store/dg0zwh8173fr4nk5rhmbzzv1ldghhz8a-linux-6.18.57.drv` | `/nix/store/ipabfanvi3crlh1zf18ss5fzh6lk1glg-linux-6.18.57`; cache.nixos.org |

These are OS defaults, not final whole-cluster payload proof. Cache responses
contained non-null path records and NAR hashes; see [kernel evidence](kernel-cache-preflight.json).
An unexpected local kernel compilation must stop the owned operation for
investigation under the verification procedure.

Seven prepared source/kernel paths retain their original normal indirect GC
roots under `devcluster/gcroots/`; all seven targets and own registered root
links were rechecked. They cover provider, OS, effective nixpkgs, API and React
sources plus both default kernels. No foreign roots or GC were touched. Native
result/payload roots will be established by native startup, not inferred from
the JSON receipts. Retain all prepared roots and external worktrees.

## Remaining activation and access gates

After explicit lead release, repeat exact session/generation, heads, native OS
ref, effective graph, native tuple/pending status, host capacity, process and
fixed-IP ownership checks. Any changed input needs lead disposition before
start. Reconcile the public foreign physical-host hold with lead. No duplicate
utility may be launched while A owns the sole watcher; use the documented
visible parent-monitor fallback or lead-assigned free slot.

The only planned initial operation is the public
`vpsadmin-devcluster start 2026-10-24-vpsadmin-haveapi-upgrade --topology single --network bridge`.
It builds and boots; no public build-only command exists. The activation
wrapper must retain the accepted resource limits around the detached runner
and QEMU descendants after the start command returns; resource containment is
not yet exercised. Daemon-backed Nix build load must also fit lead's allocation.
Do not use a wrapper whose ordinary successful exit stops its detached guests.

Capture and sanitize command output before any log or stdout emission: native
successful start invokes URL/account output. Do not persist raw status/config/
URLs, credentials, cookies, tokens, browser traces or screenshots of login.
Use the native private credential bundle and portal secret fields. CA-trusted
HTTPS and actual seeded member login/logout in both interfaces, API 7 reads,
locales, exact runtime/source and applied guest/root proof remain runtime gates.
No live-URL or login-readiness claim has been made.

Intended PHP: `https://webui.aitherdev.int.vpsfree.cz/`; intended React:
`https://newadmin.aitherdev.int.vpsfree.cz/`. Existing CA SHA-256 fingerprint:
`1C:60:3B:7C:2C:95:48:ED:32:DC:3B:49:33:5A:AF:89:C9:54:F0:7D:EE:04:77:07:03:1B:C6:7C:AD:FB:57:14`.
No trust-store import or actual OAuth verification occurred. Leave the session
open and retain its current native state; no lifecycle/cleanup action is implied.

Session portal: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/>.
