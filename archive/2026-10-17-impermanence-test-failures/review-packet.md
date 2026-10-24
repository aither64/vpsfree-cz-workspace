# Final review packet

Session: 2026-10-17-impermanence-test-failures.
Repository: vpsadminos. Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-17-impermanence-test-failures/vpsadminos`.
Target: origin/staging. Initial/final base currently `0081fc01f13236a098380094ddbd00539a9c8dae`; upstream fetch unchanged during implementation.
Final head: `fac4fe226c2fe82fc907bded100bf24f73cfba1b`. Final tree: `ac4c01b3deff321373735e70d0d4087505f184be`. Worktree/index clean. Complete base-to-head series (oldest first):

1. `5acb08db650a0c72d3b00ab66cbdd9da6b50eb46` os: bound squashfs cache memory in test images.
2. `09fb4131d65926e7490829d5a278b3d162fac44d` test-runner: reject tests exceeding memory capacity.
3. `fac4fe226c2fe82fc907bded100bf24f73cfba1b` test-runner: prepare selected images before starting VMs.

Full final diff in `review-final.diff` (28 files, 1264 insertions / 168 deletions). It is byte-identical to tested precommit `quick-ready-input.diff` by cmp. All commits ran enabled scoped hooks; full Overcommit scan passed before split. No obsolete approach or follow-up repair commit is retained; caused fixes folded into owners. No pin/lockfile changes. Independently verify whole history and final diff; do not review only last commit.

## Outcome and limits

The user confirmed original impermanence shared-image preparation was OOM killed. Add opt-in staged preparation so all selected configs/images finish before any VM; CLI defaults off, native CI opts in with a dispatch off switch. Keep runtime jobs auto, CPU1.5, kernel/build CPU parallelism. Scale preparation max-jobs from local memory and inherited Nix max-jobs; cores unchanged. Add deterministic 2048MiB test-only compressor cache and strict RAM/shm oversized refusal, preserving CPU-only run-alone exception.

The 8192MiB per-preparation-job allowance is an overridable heuristic; cache is not RSS cap. No arbitrary-build OOM guarantee. One heavy job/invocation per runner is the operational assumption. Remote memory and unrelated Nix clients are outside sizing. No broker, daemon integration, sampler, profiling database, new VM-overhead schema, host-specific fixed job cap, production cache default change, NixOS guest assertions or data migration. No deployment or merge authorized.

## Review policy and scope

High risk: host resource behavior and reusable CLI/Nix module/public framework interface. General, architecture/repetition, scope/proportionality, risk/compatibility lanes all apply. Independent retained reviewer0, gpt-6.1-sol/xhigh, read_only, saved settings unchanged. Read mandatory-change-review SKILL.md and all four lane references. Read workspace and repo AGENTS/procedure routes. No nested review delegation.

Review COMPLETE series from base and final diff; assess logical ownership/bisectability, no obsolete approach/fixup residue. No migrations, schemas, persistent guest formats or repeated dependency/channel/input update streams. None merged/released/deployed/externally consumed on this branch. Source/root and prepared manifest are invocation-local; retain supported old source and test metadata paths. All running node coordination is unnecessary.

## Accepted design / implementation

Design: [design.md](design.md). State: [state.md](state.md). Incident/source evidence: [source-investigation.md](source-investigation.md).

Three planned logical owners: optional squashfs cache+test default; strict memory/shm admission; opt-in prebuild and supporting resolver/root/exact-config lifecycle+CI/docs/tests. Root helper extraction is inseparable support for shared existing ownership-aware root convention, not a separate feature.

Key invariants: selection/context resolved once inside immutable repo source; one aggregate derivation retains Nix string references to exact selected JSONs and shared closures; no VM/evaluator before batch success. Same ResourcePool captured before preparation injected afterward, assigned limits refreshed. Exact configs passed through retries without Nix. GC root through all owned child/VM cleanup. Preparation failure/cancel produces infrastructure error, starts no VM, retains exit/signal/log. max-jobs0 remains0; numeric value not CPU-clamped; no cores edit. RAM/shm overflow terminates finitely, independent of prebuild, cannot become expected failure. Production-null squashfs command preserves previous behavior.

## Consumer/compatibility evidence

Owning provider vpsadminos test framework/runner. External vpsadmin canonical HEAD `b4ef8535a629ee8c9cd753afecdb05e0895d0eea` pins vpsadminos `8e44a5124439b1f3048ffc56b1717614a5360358`; exports tests/testsMeta and runs nix run .#test-runner, without reexporting lib.testFramework/local helper. No consumer code/pin update planned. Verify representative exports-only fixture, native arguments/config/env/template paths. --test-config retains existing framework-export requirement. Existing no-prebuild/debug remain supported. --no-prebuild disables staging, but not separate test cache default/strict admission fix. Null/overrides supported. No fleet rollout or guest state conversion.

Product explanation: docs/os/testing.md and test-runner/man/man1/test-runner.1.md; help/module descriptions. Lead applied user-facing writing skill after technical pass. Official action latest compatible majors verified (checkout7.0.1/upload-artifact7.0.2); existing @v7 retained.

## Verification

Quick verification on frozen staged snapshot (receipt quick-ready-input.diff):

- `nix develop .#test-runner --command bundle exec rspec -I test-runner/spec test-runner/spec`: 367 examples, 0 failures, 37 seconds, ready-specs.log/.status.
- `nix develop .#test-runner --command nix eval --impure --raw --file tests/squashfs-memory-eval.nix`: passed, 6 seconds, ready-cache.log/.status.
- `overcommit --run` using exported declared generic Nix environment, sandbox-writable RuboCop cache: exit0, Nixfmt and RuboCop passed. Hooks also enabled during each commit.
- Initial harness/setup failures resolved using existing CI native extension recipe; fixture context inspection now discards context only for test-side JSON parsing, while independent selected-only getContext assertions remain. No product resolver context stripping.
- No long VM/image integration before final review. Final-tree comparison proved exact tested patch; see series above.

After review: original 12-script impermanence fixture plus defaults as one prepared selection, repeat warm with a different configured memory ceiling and unchanged CPUs. No shared cache deletion/intentional kernel rebuild. Report actual substitution/coldness, memory measurement scope, time/jobs/cache settings and environment limitations.

## Final narrow remediation (after completed review)

R1 in review.md fixed inside accepted canonical-validation boundary. Complete final series keeps5acb08db6(cache) and09fb4131d(memory) unchanged; prebuild owner amended to `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`. Final tree98fab6887104cc1aa6f05941825047b031c7c662 equals tested repair tree. Full final patch final-amended.diff, original reviewed patch retained in review-final.diff. No extra repair commit, migration, pin stream or consumer change.

Lead direct verification per mandatory narrow-fix policy: remove copied partial validator; canonical MachineConfig constructors/renderers run with only host MAC/port allocation disabled; same defaults for normal runtime. Valid-first/invalid-second fresh+expectFailure regressions assert no Executor/machine/disk/global allocation. Full runner373/0 in88s and OSVM184/0 in62s, scoped hooks/amend hooks pass. Receipt r1-input.diff and logs/status linked from review.md. Review history/no-migrations/no-stream conclusions retained; no new broader public/default contract or schema added. Branch published; native integration verification ongoing, no merge/deployment.
