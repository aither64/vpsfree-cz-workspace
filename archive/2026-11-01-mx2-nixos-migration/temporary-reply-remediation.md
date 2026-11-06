# Native temporary-reply decoration

Batch 5 at `795134a48cdee269bdccabb68168de2d190c6830` stopped after 190.39 seconds;
`verification-5-vm.log` and `verification-5-status.json` preserve the failure.
The same-disk guest reboot, queue/Postgrey persistence, recovery, delivery and
drain subtest passed. Native cleanup killed all guests in 0.78 seconds and no
commands 2–6 ran.

Queue `7F7FCF8`, recipient `temporary@vpsfree.cz`, recorded the intended native
reply over the controlled primary transport:

```text
450 4.2.0 <temporary@vpsfree.cz>: Recipient address rejected: fixture temporary rejection
```

The assertion incorrectly required the SMTP code and configured reason to be
adjacent. It now requires `450 4.2.0 ` and `fixture temporary rejection` separately
in the same recipient's delay reason. Queue ID, sender, content, exact recipient,
SMTP code and controlled reason remain required. A DNS/connect failure or merely
deferred item cannot pass. This is the reviewer's original equivalent queue-bound
SMTP evidence; no policy, fixture or scope change.

Current head `8d4e03d53699d80f46030b0ee6eb213151b8ae30`, tree
`afbe660182a79891c035cdfca47ae7e47808d9e7`. Only `tests/mx2.py` differs, with two
additions and one deletion; [source/range delta](temporary-reply-diff.md).
The tests commit is amended; host `36ae6529`, DNS `91595bef`, original source and
reviewed-import refs remain unchanged. Native ty/Ruff, Python compilation,
whitespace and normal hooks pass. Exact-head evaluations pass:

| Item | Derivation | Expected output |
| --- | --- | --- |
| VM check | `/nix/store/8pan3ddqairw3js87iaysvjqwzalxgls-vm-test-run-mx2.drv` | `/nix/store/jgq1lk68xjj40j2h4wnw403pc3nylni4-vm-test-run-mx2` |
| Production MX | `/nix/store/3i0j3mdsxka3aylji983m8midp1322l6-nixos-system-mx2-26.05.20261026.718f670.drv` | `/nix/store/cpd6wpk8rmpn144hn3r49swgalrfz3f5-nixos-system-mx2-26.05.20261026.718f670` |

Fresh base is unchanged `c040c14cdbacc07998700b524996a89306188d7f`. The complete
input graph is recoverable from the current head's unchanged `flake.lock`, blob
`ec3d5aea9a7e55e69778e3ae4136cf2b3bb84e86`, SHA-256
`505f6c89e18972827beecc29a0c7c85e1df2576ed4074205501167a3dd6f326a`.
Source is frozen for lead's next accepted parent-monitoring batch. No long retry,
production operation, integration or lifecycle action is launched by implementer0.

Publication succeeded with the exact `795134a4` predecessor lease. Fresh remote
proof shows current feature `8d4e03d53699d80f46030b0ee6eb213151b8ae30` and unchanged
master/base above; native comparison is current. CI returned no branch runs, so
none needed cancellation. Worktree is clean, the source delta outside the driver
is empty and original source/reviewed-import refs remain exact. No implementer
command remains running; lead owns subsequent runtime work.
