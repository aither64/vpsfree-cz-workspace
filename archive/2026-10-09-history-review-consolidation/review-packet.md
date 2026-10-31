# Final review: dependency history consolidation instructions

User outcome: strengthen enforcement after four successive configuration channel
pins passed review and entered master. User authorizes instruction edits only and
explicitly requires approval before merging. Separate initiative created by this
conversation: 2026-10-09-history-review-consolidation, no Codex/team roster.
Lead owns the bounded design/edits; plan.md contains the direct design brief.

Read root AGENTS.md and applicable procedures in docs/agent-instructions/
(projects, sessions, git, lifecycle, documentation, verification, commits), plus
local AGENTS.md in each worktree. Read the installed mandatory-change-review
SKILL.md and the general, scope and risk lane references in full. Perform your
own final review of the committed instruction changes; no nested agents or edits.

## Complete series and final diffs

inventory.json contains exact bases, heads, one-commit series and worktrees.
workspace: b1658d80a8c8cce3b832764fc57b459d9d4d2a1c ->
08b3c6f3ee2713004b8f9d22125ebbb15cb0db33.
vpsfree-dev-workspace: 0ff827df13e82dfab4b536ff29979280f264e8f5 ->
3e5dc4681b0343ec236c3f3dfc0d6f725577c376.
Full diffs alongside this packet: workspace-final.diff and
vpsfree-dev-workspace-final.diff. Independently inspect each Git series and diff.
No migrations or dependency-input updates exist in this instruction change.
Workspace remote comparison starts at07b393609417e921d5b1c2cfec7b3d89abc473ab
and also includes tracking-plan ancestorb1658d80; inventory.json lists the full
two-commit remote series. workspace-remote-final.diff includes those initial
plan/state records as well as the instruction edit. Inspect that full series.
There are no iterative feature commits to consolidate yet. Explicitly assess
whole-branch history, repeated-update streams and migration lineage.

Workspace commit changes AGENTS readiness summary and the canonical Git procedure.
Extension commit changes the canonical review skill and its general-lane reference.
These splits follow source ownership. Existing README links already discover the
skill; no new standalone guide is needed. Installed skills originate in the
extension source; generic runtime packaging consumes those skill files unchanged.
Workspace orchestration reads its AGENTS/procedure; there are no API or state
formats, runtime code, Nix pins, catalog/member settings or live deployment changes.

## Acceptance and scope

Require consolidation per logical dependency/channel/input stream; generated
content and development deployments cannot exempt redundant pins from history
assessment. Evidence must justify retaining separate updates when a supported
release/consumer/state boundary actually needs them. Preserve required migrations,
behavior and exact source refs; protect merged history. Review packet/report
must identify repeated streams and commit dispositions. Lead checks the current
full series immediately before an approved merge without requiring redundant
full reviews for unchanged patches or narrow fixes.

Independently assess ambiguity and proportionality, particularly the distinction
between deployed compatibility and Git commit retention. Consider the prior
four-pin failure (configuration commits081ac7cc,04ee1fe6,557c97a7,1f356990,
all superseding the same devWorkspace channel selection) and a supported consumer
or persisted-schema boundary whose required behavior/ref must remain available.
These cases are acceptance scenarios, not new implementation-mirroring tests.
Do not change previous published portal history, install the feature skill bundle,
update deployment pins, or expand this into automated history-rewrite tooling.

## Verification and review policy

Quick checks passed: existing skill-policy Ruby suite5 runs/72 assertions;
YAML front matter parses;17 local Markdown links resolve; whitespace clean.
One focused commit per repository; worktrees clean. Neither repo declares a
hook framework or has active hooks; no bypass. Workspace branch descends from
current shared master. No application/VM tests needed for prose-only edits.

Overall risk high for instructions governing history rewrites and preservation
of supported deployed state. General, scope/proportionality, risk/compatibility
lanes selected; no hand-written application/config logic changed, so architecture
lane omitted. Reviewer fallback from installed default lead_reviewed review role:
gpt-6-astra/xhigh/read_only, catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd.
No retained member exists; prior portal reviewer belongs to the completed delivery
and is not this new initiative's retained reviewer. Verify/report your identity
and configured model/effort; parent will verify native metadata as well.

Start with findings by severity and file/commit reference, then independent
history/repeated-update/migration conclusions and residual gaps. Remain read-only;
no builds, CI waits, deployment, merge, ref mutations, live accounts or reset RPCs.
