# Hotplug helper fixture: final review packet

Final committed head: `cb4dcaaa397cad1f18c8f3c067b95bb8036072dd`.
Tree: `362519204191c47275b0690ccfaa4a35787a4c66`.
Exact parent/base75836892; clean index/worktree/nonignored untracked list.
Normal precommit Nixfmt/RuboCop and commit-message hooks passed without warnings
(repair/hotplug-helper-commit.log). All intended changes committed and quick
checks passed. Changed spec SHA256:
`d6559cb097df24b2520ea4710e11308971a38adbcbd79b8b5bd611cb87bf7615`.

User selected “fix the helper spec and investigate the failures”. This packet
covers the helper-spec correction only. Investigation findings/design records
are not substantive deliverables requiring another automatic source review.

Repository: vpsadminos; primary checkout
`worktrees/2026-10-22-ci-failure-analysis/vpsadminos`.
Base: merged `75836892e5d446d7c1f76411654a4c1809ceb3a0` on remote staging.
Expected range: one NEW focused commit, no rewrite of already-merged history.
Author/commit message and final file delta are in the implementation report.

## Acceptance and scope

Fix the CPU-identity example in
`test-runner/spec/test_runner/livepatch_qualification_cleanup_spec.rb`.
The real qualification_hotplug helper requires phase and now invokes a cumulative
kernel-health assertion. Its synthetic fixture lacked both pieces of context.
Supply `phase: 'pre-transition'`, explicit dmesg baseline42 and a verifying
Proc spy forwarded by the fixture's health-check method. Assert the exact guest
and baseline were forwarded. Preserve existing CPU commands,60-second progress
wait, wrong-CPU rejection and subsequent genuine-progress acceptance.

One file, +6/-1. No production helper/runner change, assertion weakening, new
framework, pin/gemfile/lock update or broader compatibility layer. No migrations,
persisted-state/API/protocol/schema changes or deployment implication. No repeated
dependency/channel/input/kernel/generated update streams. Existing merged owners
remain unchanged, so the correction is appended rather than folded into them.

No lasting product documentation change is useful for this test-fixture repair:
the production contract is unchanged. Existing plan/state and design.md:5288
record the incident and separate findings; no operational rollout is implied.

## Verification

Actual direct focused RSpec, checkout Ruby libraries first and the existing
realized runner's dependency/native paths:36 examples,0 failures, seed56457,
4.57s examples plus0.76279s load. Log repair/hotplug-helper-spec-2.log.
The actual helper's pre-transition path reached its health assertion. Changed
spec passed Ruby syntax/RuboCop1file/no offenses (style-2.log) and diff whitespace
checks. Normal commit-hook results and exact tested/committed identity follow in
the final implementation report.

Earlier direct bootstrap failed0examples because pry was absent from the chosen
gem path. Two selected pry installs attempted an unwanted native io-console
dependency and failed; a bounded pure-gem retrieval attempt stopped at its55s
deadline. Those failures/partials are retained honestly. The successful check
used already-realized deps without a Nix/runner operation, build, install or
network request in that invocation. No dependency stubs were used. No VM/hotplug
runtime or full-suite result is claimed by36 focused examples.

## Separate investigation findings and limits

Main CI prebuild failed on two pinned Linux archive HTTP429 responses, before
VM tests. Aged-v5 failed on unchanged published wakeups during initial aging,
before hotplug/target activation. Producer publication ordering permits that
sample; eventual progress/kernel cause is unproved. Reusing the existing bounded
all-counter wait at the aging boundary is a proposal, not implemented here.
References: repair/ci-followup-prebuild-1/findings.md and
repair/ci-followup-aged-1/findings.md; design.md:5389.
Do not broaden this fixture review into a source/cache/VM/kernel campaign.

## Review selection

Risk Low: local reversible test-fixture context, no production/public/persisted
contract change. General and architecture/repetition lanes apply because test
logic changes. Read mandatory-change-review SKILL.md and both lane references;
review directly without nested agents. Retained reviewer0 remains independent,
gpt-6.1-sol/xhigh/read_only; saved settings govern. Verify exact complete one-commit
range/final diff and explicitly conclude obsolete history/migrations/update
streams, including no migrations. Return findings or no findings with limits.
No source mutations/tests/Nix/builds/push/merge/runtime/cleanup selected by review.
