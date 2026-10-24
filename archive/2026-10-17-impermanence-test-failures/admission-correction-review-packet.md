# Oversized-test fallback final review packet

Session: 2026-10-17-impermanence-test-failures; workspace /home/aither/workspace/ai/vpsfree.cz.
Owner: implementer0; independent reviewer requested: retained reviewer0, gpt-6.1-sol/xhigh/read_only, no overrides. Risk high (host memory behavior); all four lanes apply. Read mandatory-change-review SKILL and all four reference files, applicable workspace procedures, repository AGENTS and patch-series policy.

## Requested outcome and user boundary

User: "we should try to run such tests. if they crash on oom, well, then they have to be fixed." Restore baseline scheduler fallback: normal RAM/shm/CPU concurrency budgets remain; if none fit and no test runs, attempt first pending oversized test alone, with full unchanged resource request and generic warning. No new refusal option, skip/retry/OOM framework. Prebuild/cache/sizing/canonical validation/root lifetime unchanged. Actual host OOM remains explicitly accepted residual. No deliberate OOM validation.

## Committed final range and history

Review worktree worktrees/2026-10-17-impermanence-test-failures/vpsadminos-admission (branch suffix -admission).
Base 0081fc01f13236a098380094ddbd00539a9c8dae.
Head e32d5382910501b0c8fe80bc6b9e6044e56ead8e; tree a57b700797c2396e148da18b6729cb49b2fc0d21.
Complete series:
1.5acb08db650a0c72d3b00ab66cbdd9da6b50eb46 cache option, unchanged.
2.e32d5382910501b0c8fe80bc6b9e6044e56ead8e prebuild + inseparable canonical resolver/validation/root/docs/specs/CI support.
Old 09fb4131d strict refusal removed entirely, no reject/revert residue; old a2 prebuild reconstructed into final owner. Old a2 stays preserved as benchmark295b814 ancestry and dated backup ref (externally measured revision must remain exact, not shipping history).
No migrations, transitional persisted-state/protocol formats, dependencies/pins or repeated generated update streams; no migration merge/release/deploy/external provenance exists. All inherited relevant prior reviews in review.md / benchmark-review.md; read as context, independently assess full final series and delta. Current staging advanced to f4bac6b49; merge-base remains0081. This review is against stated original base; premerge refresh remains needed and no merge authorized.

## Evidence and scope

Reconstruction from unchanged5ac first proved exact olda2 tree98fab688 before intentional correction. Final a2..e32 correction exactly7paths: executor/resource_pool/executor_spec, CLIapp/app_spec, docs/os/testing.md/man. ResourceError and overflow helpers removed; baseline generic fallback and worker loop restored; prebuild worker-join root cleanup retained. Full series/finaldiff must be inventoried; no obsolete alternatives/fixups.
Diff receipts in session directory:
admission-correction-final.diff SHA256662bea01d9e736991ab4af1013352e2f37332f87808071c9e6a7b0f506e10595.
product-final-after-admission-correction.diff SHA256e0dc3e1793f0d88dfaf2d939c1b961e200bcde10e16196644f5e96b81cca33f7.
155examples0failures1.48s focused executor/pool/prebuild/config/evaluator/CLI specs, admission-correction-focused.log; enabled whole-owner scoped hooks and commit hooks pass (admission-correction-hooks.log/admission-correction-commit.log). Tree/diff match tested precommit receipt, worktree clean. New CV regressions wait while another reservation active then admit oversized RAM/shm/both/CPU unchanged; existing prep/retry/no-Nix/cleanup tests pass.
Lead reviewed final visible docs/man/help/warning wording with vpsfree writing skill. Architect reconciled design.md to user decision; plan/state track new current phase. Canonical provider is vpsAdminOS test-runner; representative consumer vpsAdmin exports tests/testsMeta only, no lib.testFramework. Existing final review inspected pinned consumer b4ef8535.../vpsadminos8e44a512..., fixtures retained. This delta restores baseline scheduling and changes no export/JSON/CLI option contract.

## Reporting

Write admission-correction-review.md with findings by severity and applicable lane; explicit complete-history/consolidation/migration conclusions. Do not edit product, launch long tests, push, merge, deploy or invoke lifecycle actions. Scope correction is small, but this is final independent review of completed committed deliverable, all four lanes. Remain read-only. Report exact identity/settings/head/tree and residuals; no nested reviewer.
