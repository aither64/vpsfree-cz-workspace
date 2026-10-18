# Final independent review packet

Final no-build evaluation PASSED on exact committed OS head, exit0 in88seconds (os-evaluation-final.log/result). Intended deliverable is complete and committed in both repositories. Review exact ranges below independently; source-owner/architect reports are evidence to check, not conclusions to repeat.

## Outcome and user decisions

Remove the whole proactive-swap experiment only from Linux6.12.113; keep upstream DAMON/native memory.reclaim and unrelated product/safety behavior. Retire custom scope/free-memory quota options and experiment QEMU/tests/build/flake/selection entry points. User selected retirement (no legacy support), explicitly requested no new normal-reclaim tests, and confirms never deployed/no backward compatibility/rollback requirement. Older kernel/ZFS pins, frozen outputs, .6.18, ordinary memory-view tests and generic DAMON configuration stay unchanged.

User explicitly directed vpsAdminOS staging merge after QUICK checks so they can subsequently boot it on staging nodes, then instructed implementation. Do not require or launch kernel builds/boots/runtime/fullsuite/fullCI before merge. No tests added. Compilation/runtime are acknowledged pending user staging validation, not claimed proved. No deployment or Linux release/default-ref rewrite authorized.

## Exact deliverables and history inventory

| Repository | Base / original | Final committed published head | Target |
| --- | --- | --- | --- |
| linux | task base108d4158fae3c0d0affb58491ee67b9f573b550e; full upstream7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e; original product11058eb4fe1cba30653e8e643546c13bc8bcd792 | 86d54e7adff82e632299b41a2d1397ccbec1cb9e | New feature publication only; no merge to existing release/default ref |
| vpsadminos | 60f9ed1c153a734880e002b63d6ab7ed5fe87d0e | bf9bcb5e83f21d17561aad9416eeef2853d90956 | refs/heads/staging |

Both session-owned worktrees are under worktrees/2026-10-16-proactive-swap-patch-removal/. Both published feature refs are refs/heads/2026-10-16-proactive-swap-patch-removal; no pull requests or existing refs force-moved.

Read linux-source-inventory.md IN FULL: complete61-original-owner disposition, exact50-commit inherited consumed prefix and full55-final upstream-to-head sequence, five task-owned final owners, final28-file diff disposition and migration provenance. Independent full-history conclusion required. The prefix through108d4158 is commit-identical to existing published/current OS-consumed source (source consumption is not deployment); legacy Common-functions, CPU visibility/loadavg stages/messages are explicitly inherited baseline, not falsely normalized here. Assess that boundary, full source series and task-owned suffix directly under Git/patch-series policy. No automatic unrelated prefix rewrite is requested. Task suffix has no experiment/revert/fixup/WIP trail; CSS lifetime+early guards are folded into one coherent v2 owner.

Linux final task sequence:
1. 83a59ebf6d041c57d445fefd69e9ec6cd019314f — generic iterator safety.
2. def4b8a2613fd958daf882cfd4a9ff7a7e7ac1f0 — combined CSS lifetime/early guards v2.
3. b7609ccb76dabcb146356ea4c318715d1e9332bf — downstream affinity intersection.
4. 7ab40a1fe08da2c7cc2f6b369d10938c6579de81 — NFS cold-NLM safety.
5. 86d54e7adff82e632299b41a2d1397ccbec1cb9e — minimal ordinary unlimited-swap sysinfo v2.

All six experimental commits omitted. Important scoped design adjustment: mixed accounting owner a2425d1734ae also corrected ordinary unlimited-swap sysinfo. Architect/lead approved minimal kernel/sys.c-only standalone extraction for BOTH cgroup-v1/v2 to avoid known regression in unchanged memory-view expectations. It keeps host swap capacity, derives v1 swap-only usage from combined memsw-memory charges, uses v2 swap-only usage, bounds only new unlimited-branch subtraction. No finite/zero/general saturation rewrite or proactive fields. Independently check correctness and provenance; no new normal-reclaim tests/runtime gate.

OS complete base-to-head series is ONE coherent commit bf9bcb5e83f21d17561aad9416eeef2853d90956 (`os: retire proactive swap experiment from Linux 6.12.113`). Cleanup and pin are bundled because kernel/service interface removal must agree; no intermediate placeholder pin or repeated dependency stream. Final OS diff:10paths,4insertions/649deletions (Makefile,flake,os/Makefile,DAMON module,.113pin,test selector; delete QEMU+3dedicated tests). Source original-product-to-new diff:28paths,150insertions/819deletions, every path within experimental owners' file union.

Read actual full diffs with git diff for exact ranges (OS base..head; Linux oldproduct..newhead plus taskbase..newhead). No migrations in either deliverable: no schema/data/on-disk/container format/API/client/Terraform/protocol migration version merged,released,deployed or externally consumed. State explicit migration conclusion and repeated-stream/history conclusion.

## Final pin and consumer boundaries

OS ONLY .113 rev becomes86d54e7adff82e632299b41a2d1397ccbec1cb9e; sourceURL=https://github.com/vpsfreecz/linux/archive/86d54e7adff82e632299b41a2d1397ccbec1cb9e.tar.gz; flat archive SRI=sha256-qOskH2ecF3n0yzNE2F9vo7voFS1flXZo8Dc9h8MzxPM=. Archive246077587bytes, independently hashed Nix+Python and root exact head; linux-archive-hash.log/result. Verify actual committed linkage, no NAR-vs-flat confusion, every other kernel/ZFS value unchanged.

Owner of custom interfaces is Linux; consumer is shared DAMON Nix module plus retired experiment profile/tests. No actual external feature callers found in prior vpsadmin/site-config searches; ordinary libosctl/cgroup readers unchanged. Shared module becomes upstream-only for all kernels by explicit choice: removes public scope/quota.freeMemRate/quota.freeMemBytes/assertions/writers outright, no aliases/capability/runtime branches. Disabled service also writes parameters if available, so inspect both disabled/enabled generated forms.

## Checks and documentation

Linux source owner passed old/new and task diff --check; native checkpatch0errors/0warnings182lines; all6 omitted IDs absent ancestry; native DAMON subtree/header/admin docs byte-identical upstream; nonadapted experiment files exact prefix; CSS-helper/affinity/NFS blobs exact oldproduct and generic iterator/affinity/NFS stable patch-ID equality. Exact Linux tree declares no AGENTS,hook framework or Nix shell; native patch checks used without bypass.

OS passed nixfmt on all4changed Nix files, required Overcommit precommit+commit-msg hooks in declared Nix shell, diff --check, stale option/path/env/fixture scans, other-pins equality, ordinary test/frozen-output preservation. Ambient Overcommit0.71 disagrees with declared0.73 signature; config reviewed/signed and commit/push succeeded normally IN Nix environment, no bypass. Integration hooks must use prepared declared environment.

No-build evaluation: four default/selected .113 disabled/enabled configs, failedAssertions=[], generated upstream-only service/removed-option checks, kernel+toplevel+QEMU-script drv paths,25surviving outputs/186tests, no removed output names and memory-view v1/v2 discovery. First path-flake fixture failed from missing Git revision; diagnosed and corrected check-only input to git+file flake, no product workaround. Intermediate corrected evaluation passed. FINAL committed-pin evaluation PASS exit0 in88seconds at bf9bcb5e, os-evaluation-final.log/result; exact final URL/SRI checked in all4cases. No builds/IFD/runtime/CI.

Project explanations: Linux experimental ABI/admin docs removed/restored with owners, native upstream docs now authoritative. OS kept existing supported option descriptions and .6.18-specific update wording; no new page useful for deletion of never-deployed unused experiment. User-facing new prose not authored. design.md records final contract and accepted ordinary-view adjustment; plan/state hold coordination, source inventory holds ownership/provenance.

## Requested reviewer and lanes

Risk HIGH: kernel host/tenant memory behavior and removal of cross-project/Nix interfaces. Select saved reviewer0 (gpt-6.1-sol/xhigh, review-purpose/read_only), independent of all authors. Cover ALL four mandatory lanes: general; architecture/repetition; scope/proportionality; risk/compatibility. Read mandatory-change-review SKILL and every applicable lane reference, repository AGENTS and routed policy before reviewing.

Report severity-ranked concrete findings and exact refs/lines. Explicit conclusions required for whole branch history/inherited boundary, new suffix logical ownership, no obsolete task approaches, no repeated pin stream, no migrations, final source-to-pin link and residual compilation/runtime gap. Do not run a nested reviewer, source edits or long checks. Narrow requested fixes return to implementers; do not demand new tests/fullCI contrary to accepted scope merely to duplicate native upstream behavior. Actual correctness defects within scope remain findings.
