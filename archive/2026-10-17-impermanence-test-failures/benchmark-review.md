# Benchmark independent final review

Reviewer: retained reviewer0, gpt-6.1-sol/xhigh/read_only, exact bound thread and
roster17 verified; no overrides, fallback, nested reviewers or source edits.
All four mandatory lanes completed on committed quick-checked benchmark head
4a3e43347ffe9913b330a97fd297d7e64db51d50, tree
b153c396a52f1bd7e9e72317de7dc67e8eeda2fa. Full diff matched
benchmark-final.diff SHA2562c3e4b414687448f339121773617c6db6e4b420e8aad1d52ad26254686b8fee9.
11 focused examples/0 failures, YAML/bash syntax, hooks and clean receipts read.
No long execution, push or dispatch before review.

## Findings and lead decisions

Two Important findings; no Blocking findings. Lead accepts both; implementer0
owns narrow repair, focused regressions/hooks and amendment into the sole owner.
Long execution remains held until direct verification under skill steps9–10.

R1 (general/scope): prebuild_benchmark.rb357–358 scans all leg logs for Nix builds.
Normal guest builds in existing system/install[-zfs] shell logs match, falsely
marking missing host images and preventing B. Restrict to runner-owned host
logs: CLI, per-test test-runner.log and preparation build.log; exclude guest
shell/console/VM logs. Keep actual host builds qualifying the result. Regression
must distinguish guest and host build messages. No tracing/classification layer.

R2 (general/risk/measurement): parser/compare25–39,69–76 and351–352 ignore runtime
Resource limits updated: messages. A temporary assigned-capacity reduction can
permanently shrink the pool while before/after host readings match, producing
false clean comparability. Record existing updates and conservatively qualify
such a pair, with a mid-run reduction regression. No sampler or product change.
Raw total times remain available; a recovered change alone need not skip B if
A completed its whole workload and native cleanup.

## Whole-branch conclusions

Complete inherited series: cache5acb08db6, strict-memory09fb4131d,
prebuilda2ccd72d0 including canonical parser R1 repair, benchmark4a3e43347.
Reviewer explicitly concluded coherent owners, no obsolete/fixup alternatives.
Producta2 is the required exact checkout boundary for BOTH CLI children, not
redundant benchmark history. Temporary workflow must remain off staging.
No migrations, transitional formats or migration merge/release/deploy/external
provenance. No repeated dependency/channel/input/pin/generated update streams.

Architecture/risk otherwise accepted: existing source/prebuild root blocks span
two normal CLI children; exact product, config/tag/system, auto jobs/default
reserves/factors/cores, native disk teardown and monotonic whole-command timers.
One manual self-hosted job, read-only contents permissions and no persisted
checkout credentials. No shared-store deletion or public contract change.
Temporary harness otherwise proportionate; do not generalize disk/resource or
tracing machinery. Inherited product review and direct canonical repair checked.

Residuals: one warm randomized A/B pair is exploratory, with neighbors/cache/
thermal effects and possible predecessor guest/cleanup failures. Buffered phase
receipts are approximate. Before/after sampling is not complete transient
pressure observation; cancellation ownership checks are best effort, not kernel
containment. Uninterruptible owned work requires escalation. Dry-run cannot
prove later substitution/peak disk/RSS; watcher must stop unexpected actual
Linux compilation. No cold/cache-policy/statistical/OOM-safety conclusion.

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

## Failed attempt1 contract repair,19October

Original published benchmark06915925a failed during preflight: pinned CI Nix
2.34.8 returns a version4 envelope with derivations keyed by store basenames.
The helper treated the top-level version Integer4 as a derivation and called
fetch. Original artifact12201105726 has legs=[]; no aggregate warmup/timed run.
Original logs/artifacts preserved in benchmark-ci-failed-* and utility's
benchmark-ci-39276852536 directory; published receipt retained in backup ref
refs/backup/2026-10-19-prebuild-benchmark-failed-39276852536 and diff.

Implementer0 repaired only envelope/map decoding and added exact requested-entry
and env-Hash validation, preserving pname=linux rejection. Actual Nix2.34.8 query
fixtures instantiate builder=/bin/false derivations without realization.15
focused examples0failures2.80s, exact Nix path/version in benchmark-ci-fix-specs.log;
RuboCop and enabled amend hooks pass. Lead directly inspected fix and tests,
completed main-context wording pass, and reused review under narrow-fix policy:
no expanded design/public boundary, no migration, no product modification.

Final benchmarkd3474e5fc634a387c7c2f2ecb28efefe476c434b, tree
7ccf6b85573a7ce631809dfd5b26f9d8a7f05e2b, clean. Fix-only diff SHA256
6984dbdcf854495b831031165220274dc31fbc05b78ddf2e5e5ee7a2955d7029;
final diff SHA256e2389b7043e520560004faf24ce7dd7193cbade2b467f2f521b5821cf2ef1763.
Still one benchmark owner above exact producta2; force-with-lease published only
that ref after fetch. Native comparison recaptured. No active superseded runs.
New manual benchmark39296042103 is in progress; no timing conclusion yet.

## Attempt2 child environment repair and attempt3

Attempt2 image warmup completed3174.64s, but actual A CLI exited0.544s on
Bundler::GemNotFound(geminabox); no VM/test or B leg. Inherited BUNDLER_SETUP
survived manual BUNDLE_/RUBY/GEM cleanup and Ruby3.4.9 loaded the dev Bundler,
which resolved product root Gemfile after BUNDLE_GEMFILE removal. Original
attempt2 artifacts/stack and published d347 receipt preserved.

Implementer0 replaced manual environment logic with Bundler.unbundled_env and
unsetenv_others, shared by both measured children and a new exact wrapper --help
smoke before expensive selection/warmup. No product/resource settings changed.
Exactproducta2 package was built/rooted by a fresh Luna package-only watcher
(exit0,39s,noimages/kernels). Actual contaminated Ruby3.4.9/Bundler4.0.23 parent
reproduced old CLI exit1/geminabox and new CLI exit0/normalhelp. Receipts under
benchmark-child-env-smoke;16focused examples0failures2.65s and enabled hooks pass.
Lead inspected source/realreceipt and main-context wording; direct narrow-fix
verification under review steps9–10, no new public boundary or design.

Finalbenchmark295b814ad3aadca80ee10c043327c4676d71913c/tree
626b58c3fe84ecc53db322a7853b9e6240220266 clean; soleowneraboveexacta2.
Fixdiffb7533b9a946153182c6efe820839b13c3ae18794e77f848169fdfd2b7855458e;
fulldiff3896b3081c4e7f2cca5f845a1ca9eb26dcf27d5c08ab0942f1d4c966fd4c0902.
Published SSH with exact d347 force-with-lease afterfetch; comparisoncaptured.
No active superseded run to cancel. New manualbenchmark39305352549 is active:
https://github.com/vpsfreecz/vpsadminos/actions/runs/39305352549
SameheadRSpec39305340692/RuboCop39305340491. Fresh Luna/low standalone watcher
owns only this observationbatch, explicitfullaccess/never and boundenvpair;
parent keeps turn open until result/failure handling. Producta2 unchanged.
No valid timing result yet; user's explicit instruction is persist until results.
