# Final review packet

User request: update all Red Hat-family image releases in vpsadminos; merge when
verified. Scope is four RELEASE line replacements, no production deployment.
Acceptance: exact latest upstream release RPMs, four image-specific commits,
quick checks/hooks, final whole-branch review and four image integration tests.

Repository/worktree: worktrees/2026-11-03-redhat-image-releases/vpsadminos.
Feature: 2026-11-03-redhat-image-releases. Target: origin/staging (live default).
Base: dd188397abe37d0bc33f4c5dfb3605206ce5e326.
Head: 3307df52ea5bf875e1d8a23318a64f569d8b3ebc.
Fresh fetch retains the base as origin/staging. Working tree and index clean.

Complete series:

- 09f209688616b60155e9ac99fa8431a11b9e20a0 CentOS Stream 9, 36 -> 38
- a3c7c77459762d1a45f323de0f3f8dd5d8447323 CentOS Stream 10, 21 -> 23
- 6ede3bd22b2ed28fb28a5a912f3a7daf7743fb6a Rocky 9, 1.1 -> 1.2
- 3307df52ea5bf875e1d8a23318a64f569d8b3ebc Rocky 10, 1.1 -> 1.2

Inspect complete diff and history directly. Four files, four insertions/deletions.
Each stream has one final update; no superseded approaches or follow-up fixes.
Separate commits are required by the image release skill and allow independent
image rollback. No migrations, schema changes, release/deployment or external
consumption of feature commits. No repeated updates requiring consolidation.

Read plan.md, state.md, design.md, centos-result.md and rocky-result.md in this
tracking directory. Design records live discovery of all twelve images; eight
are current. Existing repository release skill and image-scripts/README.md own
reusable workflow; no product documentation edit is useful for RPM-only bumps.
Do not expand to builders, helpers, CI, kernel, tests or unrelated image versions.

Quick verification: four bash -n invocations and full committed git diff --check
pass; both implementers report successful required hooks in nix develop shell,
signatures enabled, no bypass. Lead repeated quick checks and inspected clean
status, complete series and diff. osvm/test-runner and all interfaces unchanged.
Long image tests deliberately pending this review.

Risk: low, reversible release-input metadata replacements with no host state or
contract change. General lane covers content and mandatory history/migration
conclusions; standalone mechanical-content exemption does not skip history.
Reviewer: retained independent reviewer0, gpt-6.1-sol/xhigh, saved read_only.
No model/effort override or fallback. Read mandatory-change-review SKILL.md and
references/general-review.md in full. Review directly, no nested agents or edits.
Return findings by severity or explicitly none; include whole-branch history,
repeated-update and no-migrations conclusions, residual risk and test gaps.
