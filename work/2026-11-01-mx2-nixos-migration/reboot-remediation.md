# Native guest reboot handling

Batch 4 at `1bea06a507cf6d3c738740a778cb8328d1f49e92` failed after 164.36 seconds.
`verification-4-vm.log` / `verification-4-status.json` preserve the full traceback.
Address/DNSBL, normal delivery/content/IPv4/IPv6/TLS, missing-milter and policy
failure checks passed. The accepted outage queue survived the Postfix restart.
The guest then completed a normal system reboot, but QEMU exited on reset; the
following service check failed in native `connect()` with `Shell disconnected`.
Native cleanup finished in 0.46 seconds and no commands 2–6 ran.

The pinned owning driver explains this behavior:

- `Driver.start_all()` invokes each machine's `start()` without arguments.
- `QemuMachine.start(allow_reboot=False)` passes that default to `StartCommand`,
  which adds `-no-reboot` unless reboot is allowed.
- `QemuMachine.reboot()` sends Ctrl+Alt+Delete, marks the shell disconnected and
  documents use with a machine started using `allow_reboot=True`.
- A subsequent native `connect()` waits for the guest's new root-shell banner;
  EOF raises the observed exception. It cannot reconnect after QEMU has exited.

Source: pinned nixpkgs `nixos/lib/test-driver/src/test_driver/{driver.py,
machine/__init__.py}`; start/start-all/command/reboot/connect methods were read
directly, together with the complete failure traceback. The earlier Perl warning
is not the established cause and no dependency change is made.

The two-line correction starts MX with `mx.start(allow_reboot=True)` before
`start_all()`, with a comment explaining the native default. The latter start is
then an owning-API no-op for already-started MX. The existing `mx.reboot()` and
all queue-ID, queued sender/recipient/content, Postgrey, service and recovery
assertions remain unchanged. QEMU retains the same guest and disk. There is no
sleep, generic exception handling, retry fallback, disk replacement or queue
deletion. Lead accepted this documented API correction under focused review step 9.

Head `795134a48cdee269bdccabb68168de2d190c6830`, tree
`80b3bbccee5cd7ecb437c238244835d487d2ea37`. Only `tests/mx2.py` differs from the
predecessor, with two additions; [complete source/range delta](reboot-remediation-diff.md).
The owning tests commit is amended; host `36ae6529` and DNS `91595bef` remain
unchanged, as do production/fixture policies and complete input graph. Original
source `40411d67` and reviewed-import `e4c1ac0c` refs remain retained.

Native ty 0.0.38 and Ruff 0.15.14 on the exact generated driver/header/hints,
Python compilation, whitespace and normal repository hooks passed. Native
checker paths and retained scratch directories are recorded in the preceding
type-check/address receipts. Exact-head test and production Nix evaluation pass:

| Item | Derivation | Expected output |
| --- | --- | --- |
| VM check | `/nix/store/1vkwizcssfi0dmw3q1m88lq7i2h1jjp6-vm-test-run-mx2.drv` | `/nix/store/zjf8zcff3d525qf920zxsbv7a1dgpmmm-vm-test-run-mx2` |
| Production MX | `/nix/store/zb7lwwvhx2psykvia79zz3j1rifwa063-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/44kln46bw9awy3xi0ysm3hfr3jvjyzz1-nixos-system-mx2-26.05.20261026.718f670` |

Base remains freshly fetched `c040c14cdbacc07998700b524996a89306188d7f`.
Full transitive input graph is available from this exact head's unchanged
`flake.lock`, blob `ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
These new identities are evaluation evidence, not a runtime pass. Lead owns
direct acceptance and the next parent-monitoring fallback batch. Source is
frozen while that batch runs; implementer0 performs only publication/evidence
completion, with no runtime rerun, production operation, integration or lifecycle
action.

Publication succeeded with the exact `1bea06a5` predecessor lease. Fresh remote
proof shows feature `795134a48cdee269bdccabb68168de2d190c6830` and unchanged master
`c040c14cdbacc07998700b524996a89306188d7f`; the native comparison binds that pair.
CI has no branch runs, so none needed cancellation. Worktree is clean, the source
delta outside the driver is empty, and both preserved original refs remain exact.
No implementer-owned command remains running; lead owns subsequent runtime work.
