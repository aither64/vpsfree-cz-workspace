# Dedicated DNSBL client address correction

Batch 3 tested `9738dfbc66bd06b75670d8efd93c684a174acbee` and stopped on the first
runtime failure after 102.34 seconds: SMTP could not bind `192.168.1.11`
(`OSError: 99`). See `verification-3-vm.log` and `verification-3-status.json`.
Native cleanup killed all three QEMU guests; the command exited 1 and no system
build commands 2–6 ran. Batch 2 was an incomplete utility readiness refusal, not
a runtime attempt. These distinct failures remain preserved.

Root cause: the network helper uses `mkOverride 20`, stronger than the sender's
`mkForce` (priority 50). Evaluation and the actual sender network-start log both
show only `.10`, excluding the intended `.11` before SMTP runs. The fix gives
the existing sender two-address list priority 10 and adds an address preflight
before the unchanged DNSBL rejection case. Lead accepted this direct narrow
remediation within the reviewed topology, without a new review lane.

Current head `1bea06a507cf6d3c738740a778cb8328d1f49e92`, tree
`59ca419b073321de81dcfb08be4ffec588af2788`. Only `tests/mx2.nix` and
`tests/mx2.py` differ: three additions and one deletion. The owning test commit
is amended; host `36ae652962d0217dd5b22965cd44fd711790d77a` and DNS
`91595bef8847063d76246b292293a687362af420` remain unchanged. Full
[source/range delta](fixture-address-diff.md). Original source and reviewed-import
refs remain preserved. No production, trust, DNSBL policy or public address change.

Focused native ty 0.0.38, Ruff 0.15.14, Python compilation, Nixfmt, Nix parsing,
whitespace and normal hooks passed. The native checker command and exact pinned
header/import paths remain in [type-check remediation](typecheck-remediation.md).
Owned `/tmp/mx2-native-typecheck`, `/tmp/mx2-python-check` and the earlier
`/tmp/mx2-test-script-with-types.py` are retained scratch artifacts for this session
until the final pass; no process runs from them and no fixture guest is retained
by this implementer. No new watcher scaffolding or runtime rerun was launched.

Exact-head evaluation confirms sender IPv4 `192.168.1.10/24` and
`192.168.1.11/24`, IPv6 `fd42:6d78:32::10/64`. MX and primary addresses are
unchanged; all guests retain `restrictNetwork = true` and both default gateways
null. No loopback or trusted client substitutes for the listed source.

| Item | Evaluated derivation | Expected output |
| --- | --- | --- |
| VM check | `/nix/store/zd6ql5prppfbzm6mln4g5jndja0p9c9a-vm-test-run-mx2.drv` | `/nix/store/a78704chhhsxz338abdv6hhy0438sgiz-vm-test-run-mx2` |
| Production MX | `/nix/store/zwggslvdc6gdjxb9aq4z5ighy8181vlk-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/7x283zwklcp4kwg43vfvygi15r408d8s-nixos-system-mx2-26.05.20261026.718f670` |

Source/input graph is bound by that final head and unchanged lock blob
`ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
The full graph is recoverable from the exact head's `flake.lock`.

Lead directly accepted the source delta and started batch 4 at this exact head
under parent-monitoring fallback. Source is frozen while that batch is active.
Implementer0 owns only publication/comparison/evidence completion now; any new
correction goes through lead to reconcile the current run first. Evaluation here
does not claim a runtime pass. No production operation, integration or lifecycle
action has been performed.

Publication used an exact `9738dfbc` predecessor lease. Fresh remote proof reports
feature `1bea06a507cf6d3c738740a778cb8328d1f49e92` and unchanged master
`c040c14cdbacc07998700b524996a89306188d7f`; native comparison binds that base/head.
The worktree is clean, only the two declared test paths differ, and original
`40411d67` / reviewed-import `e4c1ac0c` refs remain exact. CI returned no branch
runs, so no superseded run needed cancellation. No implementer-owned command is
left running; lead owns the active batch 4 operation.
