# Independent final review

Reviewer0: retained gpt-6.1-sol/xhigh/read_only, roster17, verified session binding. Completed all four required lanes on base0081fc01f13236a098380094ddbd00539a9c8dae to headfac4fe226c2fe82fc907bded100bf24f73cfba1b / treeac4c01b3deff321373735e70d0d4087505f184be. No edits or long tests.

## R1 — Important (architecture/general/risk)

`TestConfig#validate_machine!` at test-runner/lib/test-runner/test_config.rb66–88 partially reimplements OSVM validation. It misses network requirements, shell count/transport/names, rootDisk/diskImage conflicts and shape/nil validation. Independent in-memory reproductions: testShells0 and bridge opts{} pass preparation but canonical MachineConfig.from_config raises. Native test networks are forwarded directly, so malformed definitions can trigger it.

False preparation success yields configs to Executor. Other tests may start; within one multi-machine evaluator, earlier valid machines can be constructed/reset under --fresh before a later invalid machine rejects. Late evaluator failure can synthesize missing script results or satisfy expectFailure. This violates invalid-config-before-runtime/mutation boundary.

Lead disposition: fix. Reuse authoritative side-effect-free canonical validation before Executor; avoid MAC/port reservation and disk actions. Regress valid first+invalid later with expectFailure. Architect0 owns bounded design refinement; implementer0 owns repair and focused checks. Long tests held. Fold into prebuild owner. Under skill narrow-fix policy, direct focused verification suffices if fix stays inside accepted boundary; new design/public contract requires affected-lane reassessment.

## Other conclusions

No Blocking findings or other Important issues. Complete series cache5acb08db6 / strict-memory09fb4131d / prebuildfac4fe226 has coherent ownership/order, no obsolete approach/fixup residue. No migrations or transitional lineage; none merged/released/deployed/externally consumed. No repeated dependency/channel/input/generated updates; no pins/lock changes.

Reviewer verified aggregate contexts/root lifetime, prepared retry reuse without Nix, cancellation ownership, cache production-null preservation/both branches, strict memory CPU-only exception, CI false switch, unchanged CPUs/cores, docs and representative vpsAdmin exports/pin compatibility. Provider owns reusable behavior; no coordinated fleet update required. Reviewed367/0 quick and cache/hook evidence/receipts; did not rerun full suite or integration.

Residual: original fixture+defaults long run, warm run and second configured memory ceiling outstanding.8192MiB/job and2048MiB cache remain heuristics; no arbitrary build/neighbor OOM guarantee or daemon RSS measurement. One-heavy-job/local scope and substitution/coldness to be reported.

## Accepted narrow repair route

Architect0 proposes canonical `MachineConfig.validate_config!` through existing spin dispatch/constructors with internal resource allocation disabled, then existing pure network option rendering. Normal runtime parsing retains allocation default. Suppress actual global MAC/port operations only; retain all canonical shape/type/field validation. TestConfig keeps test envelope/script and positive scheduler RAM/CPU sanity. Validation-only object discarded, no synthetic values enter runtime/JSON. Global MAC/host resource availability remains runtime-only. Lead accepted; implementer0 executing and amending prebuild owner. No broad parser refactor or new schema.

## R1 direct verification / resolution

Implemented only four repair files: canonical OSVM parser plus specs; TestConfig replaces its duplicate validator with canonical call; CLI regression covers full preparation barrier. Inspected diff: false allocation flag propagates through same spin/network constructors; actual global MAC/port calls alone suppressed; network renderer invoked; normal defaults remain true. No copied constraints, new product format or scheduler behavior. Regression valid-first/invalid-second with fresh+expectFailure confirms no Executor/machine/reset/allocator/result entry.

Focused runner41/0 and canonical35/0; scoped hooks pass. Fresh watcher full suites on exact staged tree98fab6887104cc1aa6f05941825047b031c7c662: runner373/0 in88s, OSVM184/0 in62s (r1-runner and r1-osvm log/status). Patch receipt r1-input.diff hash73ee5e2d498f4125a7f9bfbbe3f1ebe03077014db6ee085f0e5a1b684cb2a926. Cache source/eval unchanged. Lead accepts requested narrow repair as resolved under mandatory review steps9–10; no new design/public/default contract expansion requiring lane rerun. Original full branch review remains applicable; amended owner/tree/history will be re-inventoried directly. No long test started before resolution.

Final amended owner: `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`, tested tree98fab6887104cc1aa6f05941825047b031c7c662. Worktree/index clean; first cache/memory commits unchanged. Lead re-inventoried whole3commit history/final diff after amendment: no obsolete repair commits, no migrations/pin streams. Amendment scoped hooks passed. Native comparison captured base0081fc01 to final amended head.
