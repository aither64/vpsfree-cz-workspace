# Committed upgrade-test cleanup and lifecycle policy review

Requested outcome: implement the user's minimal cleanup after the configured
production baseline superseded September's rollout scenarios, and introduce
mandatory naming/header/removal conditions for userspace upgrade tests.

Scope: vpsadminos only, worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-ci-failure-analysis/vpsadminos`.
Cleanup base `f74629fa4046089e2c53d0cb0e3ba7ef5b178e82`; committed head
`8fb5782ff630deee79d0cdbb7eee55abc459464f`.
Design: design.md:4977. Current plan/state start with the minimal selected task.

Acceptance: exactly 33 exclusive old upgrade/diagnostic/support/spec deletions;
retained production-impermanence renamed to impermanence-from-2abbe3cc1c10,
native-name metadata/header updated, behavioral template and script exact;
two catalog opt-ins removed, sole retained template renamed; focused docs kept,
obsolete sections replaced by policy, AGENTS points to it. No new framework.
The old persisted-state repair remains supported; retirement evidence for that
retained fixture is explicitly not established. Configuration pin evidence is
not a live production inventory.

One logical commit bundles retirement, catalog/doc cleanup and the lifecycle
policy applied to its retained case. No implementation, input, lock, generated
metadata, runtime format, migration or deployment change. No migrations. No
dependency update stream exists in this package.

Quick evidence: repair/upgrade-cleanup-1/static-checks.json establishes the exact
deletion/rename boundary, catalog equality and 16,955-byte unchanged testScript
SHA256 b949f3fc408e31daa78fcf15d46016fe424ccceafb33096c9e821579be9e78e4.
Commit/amend logs and statuses in the same directory retain mandatory hooks.
Lead inspected exact prose and all three requested wording edits. Native catalog
discovery/VM execution remain unrun, not PASS; restoring missing inputs or
restarting the prior verification campaign is explicitly excluded.

Review risk: medium (test selection/coverage and contributor policy changed,
bounded/reversible with no production-code change). Reviewer: ready retained
reviewer0, gpt-6.1-sol/xhigh/read_only, no overrides. Lanes: general, architecture
and repetition, scope and proportionality, risk and compatibility (retired
transition coverage and intentional test-name changes). Read mandatory review
skill and every lane reference. Review directly; no nested reviewer.

Complete earlier branch context from initial base
846bb469505789ba0b2a405fa5905ba6d8253006, oldest first:

1. ae33b06b0264b2aabcb5af21bb47c029a6a3f091 persist impermanent selection
2. be4ec430d49395513a0c7188bffcd78f17cd4ae9 authenticated legacy recovery
3. 50a796f2824424252be177aedafb277b6f149073 DHCP diagnostic
4. 247c091e6a48083099395e5e1f4847ef5a585be6 first-switch diagnostic
5. a1c4dc932b953cc21fde47a2fc2e6f85bb03e8f8 historical opt-in
6. a2e4c097103eeeba8ae016571ffbe25316ceb10f focused impermanence transition
7. 39b6f68f245d6ebddf40a5ffc8e2e9485a9a8a17 hotplug health checks
8. f74629fa4046089e2c53d0cb0e3ba7ef5b178e82 experimental recorder
9. 8fb5782ff630deee79d0cdbb7eee55abc459464f this cleanup/policy

The current task intentionally does not declare the entire earlier feature
branch merge-ready. Commits 3–5 are superseded by the cleanup and need history
consolidation before whole-branch readiness; do not hide that in the conclusion.
Earlier runtime/recorder/production validation limits remain. Do not expand this
review into repairing those unrelated features or authorizing their execution.
Earlier series has no database migrations or repeated dependency-pin stream;
retained legacy run-state behavior is compatibility with production, not a
transitional database schema. Independently check relevant history/context and
state the bounds of this completed-deliverable review.

No merge/deploy/lifecycle/cleanup authority. Return concrete findings and limits;
write only a concise review record under this session and report to lead.
