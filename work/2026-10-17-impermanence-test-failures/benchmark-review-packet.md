# Benchmark final review packet

User asks for execution-time comparison with and without prebuild, including
whole-command wall time, rather than correctness/capacity evidence alone.

Scope: temporary benchmark-only vpsadminos ref/worktree
2026-10-17-impermanence-test-failures-benchmark / vpsadminos-benchmark.
Product revision for BOTH timed CLI children is exactly
`a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`; the product branch remains unchanged.
Accepted brief: performance-plan.md, linked by design.md. State/plan retain the
performance acceptance gap. One self-hosted job keeps builder assignment;
warm-root API blocks surround independent full CLI children A(no-prebuild),
B(prebuild), with identical native ci configuration, selection, automatic jobs,
production reserves/factors and unrestricted cores. No prepared-config shortcut.

Acceptance: real monotonic total, phase markers with honest attribution,
selection/result/resource receipts, logs and owned cleanup; unequal failures,
pressure/capacity drift or incomplete work qualify the result. One warm A/B pair
is exploratory. No claim about cold build overlap, old compressor policy,
arbitrary-build OOM prevention or statistical equivalence. Do not invent a
performance pass threshold. No unrelated fixture fixes or weakened assertions.

Overall risk: high because this runs full native workloads and cleanup on shared
self-hosted infrastructure. Review all four mandatory lanes using retained
reviewer0 (gpt-6.1-sol/xhigh/read_only), no overrides. Read all lane references.
Check proportionality: this is a temporary measurement job, not a general disk,
benchmark or resource framework. No new product knobs/APIs. Existing runner
operational checks plus concrete resource observations; Nix build temporary and
sparse-disk peaks are unknown, not a formal admission guarantee.

Complete inherited product series from base0081fc01: cache5acb08db6,
strict-memory09fb4131d, prebuilda2ccd72d0. All inherited product code independently
reviewed under review.md, including direct R1 repair. Inventory new benchmark
owner and full final diff after commit below; benchmark ref is not intended for
product integration. No migrations, persisted-state changes, dependency/pin
updates or repeated generated streams; no migration provenance to preserve.
Representative external consumer/provider contracts are unchanged from product
review; only temporary CI orchestration consumes existing APIs.

Official actions checked19October via upstream release APIs: checkoutv7.0.1,
upload-artifactv7.0.2; compatiblev7 refs remain. No merge/deployment permission.
No long benchmark may start until completed intended changes are committed,
quick checks pass and this independent review resolves Important/Blocking items.

## Committed final receipts

Base/product: a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1.
Benchmark head: 4a3e43347ffe9913b330a97fd297d7e64db51d50.
Tree: b153c396a52f1bd7e9e72317de7dc67e8eeda2fa.
One new owner: ci: compare warm native suite prebuild timing.
Complete series from original0081fc01: 5acb08db6,09fb4131d,a2ccd72d0,4a3e43347.
The inherited product head is a required exact checkout boundary, not obsolete
benchmark history. Product ref stays a2; temporary benchmark CI must not merge
into staging. All caused benchmark refinements are folded into its sole owner.

Final three-file delta is benchmark-final.diff, SHA256
2c3e4b414687448f339121773617c6db6e4b420e8aad1d52ad26254686b8fee9.
Workflow temporary replacement,442-line Ruby helper and173-line focused spec;
676 insertions/482 deletions. No Python cleanup/retention helper remains.
No superseded pin streams, generated updates, migrations or transitional formats.
No merge/release/deployment/external migration provenance exists.

11 focused examples/0 failures in2.60s (benchmark-focused.log), YAML parsing and
all shell blocks bash -n passed, scoped Nixfmt/RuboCop plus enabled commit hooks
passed (benchmark-hooks.log/benchmark-commit.log). Source/index clean and diff
--check passes. Lead directly completed final prose pass before commit; two
clarifying strings folded in. Actual initial logged Executor memory/shm/CPU
ceilings are retained and compared, not only assigned host limits.

Review execution and measurement validity, bounded cancellation/owned cleanup,
root lifetime, selection/config fidelity, telemetry limitations, secrets and
scope proportionality. No long execution has started, and no push/dispatch yet.
Finite dry-run kernel check cannot rule out a later failed substitution; watcher
must observe actual warmup build logs and escalate/cancel unexpected kernel
compilation under workspace procedure. Never match arbitrary systemd unit names
containing kernel as if they were Linux compilation.

## Narrow repair verification and final execution head

Lead directly verified R1/R2 repairs under mandatory-review steps9–10:
explicit host log paths exclude guest shell/console builds while retaining CLI,
runner and preparation logs; passive runtime capacity-update receipts prevent a
clean comparability claim while retaining totals. Meaningful filesystem/external
CLI and reduction/recovery regressions passed. No new design/public boundary,
so no unaffected-lane reviewer rerun. Main-context prose pass remains applicable.

Final benchmark head06915925a7a63a2fac7135a752101228b5b699e0, tree
771895324cfc498413a8eb801ac0b0b9bac5fb4b; source/index clean. The range from
producta2 remains one owner, all caused repairs folded in.13 focused examples/
0 failures in2.40s, standalone RuboCop and enabled amend hooks passed. YAML/bash
workflow unchanged since successful checks. No migrations, pin streams or
product edits. Original reviewed diff preserved as benchmark-reviewed-original.diff;
repair-only diff benchmark-review-fixes.diff SHA256
 a9fdd6061906dc5ac8fb79cd9a26b70205779d389f086d7ddf28cfc8a57d462b.
Complete final benchmark-final.diff SHA256
39dc48fa19955eb3bc48917c82b60c820a78abd64fedc524464050b34017ced3.
Long verification gate is satisfied for this exact benchmark head. Publication
and dispatch are authorized by the user's measurement request; no merge/deploy.
