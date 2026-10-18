# Remove the proactive-swap experiment from 6.12.113

## Goal and authorization

Implement the approved plan and merge vpsAdminOS into staging after quick verification and independent final review. User explicitly selected staging as the merge target, then instructed "Implement the plan". Linux reconstruction is published on a new feature ref; existing Linux release/default refs are not rewritten. No deployment or reboot is authorized.

Only 6.12.113 changes. Leave older kernel sources/pins/frozen outputs, 6.18, and ZFS pins unchanged. User says the experiment is never deployed: no backward compatibility, rollback, transition shims or migrations. User selected removal of the whole experiment, retirement of its tooling, no new normal-reclaim tests, and no full CI wait. Kernel compilation/boot/runtime checks are subsequent user staging validation, not pre-merge gates.

## Execution and compact backlog

| Package | Owner | Result and acceptance | Dependencies/checks |
| --- | --- | --- | --- |
| Final technical brief | architect0 (Astra/xhigh, workspace_write) | Refresh design.md to all final decisions before source implementation | Exact .113 series established through read-only HTTP/API |
| Linux reconstruction | implementer0 (Sol/xhigh, workspace_write) | New .113 series drops all six experiment owners and preserves other behavior/safety fixes; publish final exact head | Architect brief, initial tracking commit; source/history checks, policy-compliant commits |
| OS consumers/tool retirement | implementer1 (Sol/xhigh, workspace_write) | Upstream-only DAMON module; remove experimental QEMU/tests/entry points, add no tests | Architect brief, initial tracking commit; hooks and quick Nix evaluation |
| Final kernel pin | implementer1 | Change only .113 Linux rev and archive-byte hash once | Final published Linux head; serialize OS Git operations |
| Independent final review | reviewer0 (Sol/xhigh, read_only), assigned when ready | Review exact committed Linux + OS deliverables, complete series/diffs/migrations and actual final pin/hash | All intended commits and quick checks passed |
| Acceptance and staging integration | lead | Coordinate FF-only vpsadminos staging merge, preserve feature refs; report runtime validation pending | Independent final review and authorized queued integration |

## Technical approach

Reconstruct Linux on upstream v6.12.113 base 7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e, preserving a dated backup of original product tip 11058eb4fe1cba30653e8e643546c13bc8bcd792. Omit owners a9dd8baca1c9, b1fe371e52aa, a2425d1734ae, 7b11a3286173, c89d7963a742, 5bbdd2635be1. Preserve native DAMON/memory.reclaim, ordinary product memory/swap views, CSS lifetime/early-access, iterator, affinity and NFS fixes. Fold dependency repairs into their retained logical owners under patch-series policy; publish new feature ref, not release ref rewriting.

Shared DAMON module removes scope, quota.freeMemRate and quota.freeMemBytes together with assertions/writers. Retire proactive-swap QEMU config, dedicated tests and all build/flake/test entry points. Preserve ordinary memory-view tests. Final Linux source must be published before computing the archive-byte hash and committing the one final .113 OS pin.

## Verification, documentation and operations

Quick gates: complete patch/tree/ownership inventory, absence of removed custom symbols and callers, repository formatting/hooks, Nix evaluation/instantiation disabled/enabled without kernel builds. Mandatory independent final review follows all intended commits and quick checks, including the exact final pin/hash. Merge via selected package coordinator, no machine reservation for merge-only work. Do not wait for full CI or launch kernel builds, VMs or integration tests.

Future user staging checks: exact kernel and matching modules/ZFS build, boot, DAMON disabled/enabled smoke, existing memory-view cgroup-v1/v2 cases. Identify changed kernel by store path/build identity, not uname alone. Report as merged with compilation/runtime pending, never as tested ready for use.

Readers are user, implementers and future kernel maintainers. Architect owns design.md; implementers own relevant kernel/OS technical documentation and patch provenance; lead owns session tracking/review/integration records. No configuration pin or deployment repository changes. Keep session open.
