# Deployment baseline refresh review

Perform independent final review of the refreshed complete branches. The original
reviewer thread 01a15493-6331-7333-a36a-21e171b191e2 is unreachable: CLI resume
refused an unloaded multi-agent v2 child and required its external parent first.
Do not resume that parent. This fresh standalone fallback uses the installed
catalog default lead_reviewed review-purpose role: gpt-6-astra/xhigh, read-only
review under full_access/never execution. Retain the original reports as context.
No nested agents or source edits.

Read applicable workspace AGENTS.md and repository AGENTS.md; session, git,
lifecycle, deployment, documentation and verification procedures apply. Read
~/.codex/skills/mandatory-change-review/SKILL.md and all four lane references:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Risk remains high due persisted lifecycle, cleanup and deployed-state compatibility.
Use the documented trusted-local-operator boundary; remote clients are untrusted.

Scope remains archive tracking prerequisites and stable index text selection.
The archived failed target is already finished and must not be mutated again.
User handed remaining approved deployment continuation to managed lead. No merge,
reboot, release, closure or checkpoint commit is authorized. Existing system and
dependent profile jobs must be refreshed rather than duplicated.

The prior system job stopped before activation: installed coordination adapter
catalog changed while waiting, and current defaults had advanced. Preserve all
integrated session-creation fixes. The two reviewed runtime commits rebased
cleanly onto ea650c34. Their range-diff reports both patches equal. Consumer old
pins were dropped and each regenerated once on its current default. No handwritten
logic or new contract was introduced in this refresh. Inspect this independently,
especially overlapping upstream lifecycle/portal changes and deployment safety.

Exact complete series, base/head pairs and migration inventory are in
baseline-refresh-inventory.json. Final diffs are baseline-refresh-dev-workspace.diff,
baseline-refresh-vpsfree-cz-configuration.diff, baseline-refresh-workspace.diff.
Original range and reports remain in branch-inventory-reviewed.json,
final-review.md and final-review-followup.md. See baseline-refresh-runtime-range-diff.txt.
Review every refreshed full base-to-head series and final diff; explicitly conclude
history consolidation, repeated pin streams, migration lineage and compatibility
with the currently deployed ea650c34 baseline. No migrations or format changes
are intended; no original feature revision from this initiative has activated.
Each consumer should contain one final pin, with extension/sibling graph preserved.

Documentation: runtime docs/session-archive-recovery.md still owns supported
behavior and invariants. The continuation brief is appended to design.md;
rollout.md/state.md own deployment evidence. Source explanation needs no new
prose for an unchanged rebased patch. No production KB content changes.

Quick verification: focused explicit/automatic lifecycle regression passes:
2 tests, 193 assertions, zero failures/errors/skips (50.44s). Ruby/JS syntax passes.
Go index status and shipped-browser/API harness checks pass. I initially invoked
the browser-contract .cjs fixture directly, which correctly refused missing server
URL; corrected to TestShippedBrowserClientMatchesSessionAPI, its owning Go harness.
Composition-contract check passes exact runtime 09a40795 with unchanged extension
and sibling inputs. Configuration generated commit passed mandatory Overcommit.
All worktrees clean and diff checks pass. Full refreshed package/VM/real-browser
verification waits for this review; original-head checks remain retained evidence.

Runtime owns the behavior; workspace consumes it through direct nested override
and configuration through dev-workspace/devWorkspace channel. Activation must use
fresh selected-generation/catalog/live-baseline preparations under the held
reservation, system before application profile, forward recovery, no reboot.
No public interfaces, schema, journals or mixed-version guarantees should change.
No fleet update. Keep original uncertain attempts for recovery if effects occur.

Return findings ordered by severity, lane and file/line/commit, or explicit no
findings with residual gaps. Assess complete history and migrations explicitly.
Do not run long tests or deployment. Write only your final report through the
CLI output path; do not edit application source or initiative tracking yourself.
