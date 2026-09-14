# Bounded CI remediation review

Read the existing packet.md and state.md for initiative context. Review only
runtime 63cbc32173f73da313e4f11c9c2214884f6161d5 -> cdcaafa0333cd7aa1f48e6eedc3424ca5d447b13, two focused commits,
and the mechanically updated runtime/organization pins in sibling worktrees.
The UI changes already completed four review lanes and browser validation.
Worktrees: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-portal-review-fixes/dev-workspace, vpsfree-dev-workspace and workspace.

Organization CI 34886053176 failed the unchanged pagination fixture at count 101
with Git exit 128; the other package's suite passed. The runner discarded stderr.
After adding bounded stderr to the same exec.ExitError, 1 of 50 local runs failed
with "Could not read <object> / revision walk setup failed", again at count 101.
Git trace shows automatic commit-graph write at the 100-commit boundary. Another
100-run diagnostic series passed, so it is intermittent. The evidence is
consistent with a background maintenance race, not proof of an upstream cause.

The final change retains bounded stderr on exec.ExitError, preserving Error(),
context/limit handling and HTTP responses. A unit test verifies the diagnostic
and unchanged public error text. The history-count fixture prints the diagnostic
and revision pair, and disables maintenance only in its own disposable repo,
as the existing bulk-rename fixture does. Production Git config is unchanged.
No new retry, fallback, provider/API/state/archival or security behavior is added.
No user-visible text is added. Trust/consumers/deployment remain as packet.md.

Quick checks: diagnostic regression passed (0.166s), complete repository suite
passed (11.536s), 50 pagination runs with fixture maintenance disabled passed
(68.786s). Final code is committed and pushed. Downstream pins simply select it.

This is a Low-risk diagnostic/test addition within the Medium-risk initiative.
Rerun General and Architecture directly with gpt-6-astra/xhigh; no nested agents.
Scope/Risk had no findings and their accepted boundaries are unchanged. Write
ci-general.md or ci-architecture.md alongside this packet. Do not run long tests.

vpsfree-dev-workspace: 3f602aef0662b23eef9f7aa2f4c5a76e20e943bd -> 6f59c3017b6da91bd5745a35a934be265b8330f1.

workspace: c986868b94ef67c9ecf9a65b814f1f18793dadee -> 5bd3d8b409dfa466438777a2e31aad6202a62c6a.
