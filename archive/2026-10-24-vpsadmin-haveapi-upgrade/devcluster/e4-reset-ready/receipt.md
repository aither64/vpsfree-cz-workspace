# E4 reset-ready handoff — 2026-10-28

**RESET-READY for parent public reset only. No reset/move/config initialization
or startup has been run by E3.** Lead accepted A9697/Ce468 final source, review,
checks/publication/effects/no-writer handoffs and the changed native input graph.

Private preservation contains only documented editable config:
`/home/aither/workspace/ai/vpsfree.cz/.dev-clusters/vpsadmin-preserved/2026-10-24-vpsadmin-haveapi-upgrade/e4-20261028/config.json`.
SHA-256 `10819c2d393795f4909695f04e4caf3d4035a94e84e25c871ecfc1ab19a16332`;
directory0700/file0600, UID1000/GID100. Original bytes are unchanged. No applied
envelope, disks, journals, sockets, credentials or other runtime tree was copied.
See [preservation facts](preserved-config-receipt.json).

All four actual moving worktrees are clean, common Git directories match their
canonical bare repositories, and no index lock is present:

| Path basename | Branch | Exact head |
| --- | --- | --- |
| `vpsadmin` | `2026-10-24-vpsadmin-haveapi-upgrade` | `70a2ed54b98d0c2f359a9cc4484452a257a9807b` |
| `vpsadmin-0311` | `2026-10-24-vpsadmin-haveapi-upgrade-0311` | `9697bf28c3171d4ee3e0980160be60764ae2c4aa` |
| `vpsadmin-webui` | `dev/vpsadmin-haveapi-upgrade` | `f10d3d48c4f21cc39187c3667ffffd9952404c11` |
| `vpsadmin-webui-0311` | `dev/vpsadmin-haveapi-0311` | `e468ca48406bde1bd99cc42a05e1832fb42162f4` |

[Before-move inventory](before-move-inventory.json) records absolute paths,
branches/heads/common and worktree Git directories, directory device/inodes,
logical index/tracked-diff digests, selected private/ignored lock/vendor hashes,
modes/symlinks and ignored top-directory identities. A/C final receipt values
match. The first local inventory adapter expected objects where the protected
receipt uses plain hashes; it stopped before config preservation or mutations,
then was corrected once. Both `*-live030` destinations are absent. Existing031
checkouts/publishedbaf remain untouched. No Git moves or refs were changed.

Fresh sanitized native/host facts at 23:21:05 UTC:

- Runtime `pq2jwjcv4hbyiwzcam50x6j9fv008qiq`, provider
  `vh650zaiazv3n8z12yf12pfbc951xwb9`, exact contract `9c8e9e5c…`, schema1/policy3;
  accepted OS `f4e55a13d7d2f5c1b61737f0300ec8a535ef02f1` remains unchanged.
- Current old canonical cluster running/ready/single/bridge, pending=null.
  Runner **2882335**, start ticks **1233732770**, has all four exact native
  tuple flags; socket `/tmp/vpsfree-devcluster-02da06564216` matches recorded
  ownership. Exact state/PID/ready paths are in the facts file.
- Own four QEMU PIDs **2891713, 2896888, 2898197, 2898599** remain children of
  that runner in `vpsadmin-haveapi-upgrade-e-20261026T153200Z.scope`.
  Extra PID431390 is non-br0/outside our runner and is explicitly untouched;
  its ownership is not inferred from A's separate effects proof.
- All expected fixed-IP neighbor MACs match our four old VMs. These addresses
  remain occupied until reset; this is not a free-address reservation.
- MemAvailable57,871,500KiB, 64 allowed CPUs, load4.70/4.95/6.17, disk95.44GB
  free; global Nix daemon8.45GB current is separate, not E-attributed. Startup
  still needs fresh capacity/address proof after mapping.

See [exact reset-ready facts](reset-ready-facts.json). No guest commands or
full metadata repeat occurred. The earlier proposed graph/cache evidence is
unchanged; no standalone artifact reuse/equality is claimed.

## One fresh reset observer

Actual attached observer: retained catalog840de475, native utility
`dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12`, **Luna/low**,
explicit **danger-full-access/never**, fresh thread
`01a17fac-31c8-7252-b33b-8511011e88e0`, launcher handle43824, actual PID1416872.
The selected installed execution policy was resolved separately. It observes
only parent-created sanitized `parent-reset-result.json` and
`parent-reset-events.jsonl` in this directory. Missing files mean wait, not
failure/completion. No transferred parent handle or native query is used.

[Setup](reset-observer-setup.json), [launch](reset-observer-launch.json),
[actual identity/policy](reset-observer-actual-policy.json) and the independent
`reset-observer-events.jsonl`/`reset-observer-final.txt` retain evidence.
This utility must not reset/start/retry/signal/stop/release/edit/diagnose or
query guests. On actual mismatch/early finish, reconcile once and use visible
parent fallback; no repeated watcher repair. Reset and later startup need
separate fresh observers. No optional CI wait is involved.

Parent's literal mutation remains:

```sh
vpsadmin-devcluster reset 2026-10-24-vpsadmin-haveapi-upgrade
```

Only after parent proves reset completion/effects and releases moves may E3
execute the four ordinary worktree moves. Lead then remaps whole ordinary
registrations/public sync. Config initialization/restore, final mapped graph and
minimal driver constant/Nix1job2cores updates wait for their later release.
No production KB, provider installation, host/profile, default branch or session
lifecycle action is authorized. KB0311 staging remains owned/up for user review.
