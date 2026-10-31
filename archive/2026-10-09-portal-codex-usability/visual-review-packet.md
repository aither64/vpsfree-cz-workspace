# Final review: compact portal presentation

Initiative 2026-10-09-portal-codex-usability, created by this conversation,
threadless with no retained roster. Parent owns design/application edits.
Read plan.md, design.md, state.md, and final-inventory.md in this directory.
Canonical worktrees: ../../worktrees/2026-10-09-portal-codex-usability/.
The inventory contains full base-to-head series and exact final diffs for all
four repositories. Prior deployment identities and results are in rollout.md.

## Requested result

Whole-credit rounding with locale separators in sidebar and account dialog.
Muted account text in two lines, with 12px spacing after the allowance. One
information icon beside the limits heading. Centered model/reasoning text and
a pencil icon. Plan/Default belongs with attachment/Send controls on the left;
model information and Interrupt belong on the right. Preserve wrapping,
keyboard access, dialogs, and all existing settings/reset safeguards.

The visual correction is dev-workspace commit 577d5b72. Workspace and config
pins select that exact published runtime, preserving the extension and provider
versions. Codex-web has no further changes. No account API/state/schema changes.
No migrations, including no earlier unapplied migration versions.

## History and split

The initial eight-commit delivery passed independent review, tests and live
deployment. Those consumed source/pin commits remain as provenance for that
delivery; this is a new approved visual revision. Workspace's earlier pin was
rebased patch-equivalently onto c31fd962, then a separate final runtime pin was
added. No intermediate unpublished correction or redundant compatibility path.
The visual commit includes its direct browser assertions, cache query versions
and feature documentation. Workspace/config pins are separate commits.
Assess the complete branch series and explicitly conclude on history and
migration lineage. Also inspect the visual increment against deployed sources.

## Verification and documentation

Quick checks pass: Node syntax for app and two browser fixtures; git diff
--check; focused Go limits, reset-controller and auto-archive tests. The
composition checker passes at 577d5b72. Config hooks (Nixfmt and message hooks)
pass, retaining generated confctl message. Workspace rebase range-diff is equal.
README Codex limits and docs/workspace-portal.md composer guidance are updated.
No new deployment procedure is needed; this rollout uses the existing host
configuration then separate stable profile switch, with native Codex retained.
Browser and package checks follow this committed review. Account writes are
mocked; no live reset use is authorized for testing. All three currently remain.

## Selection, risk and boundaries

All four lanes: general, architecture, scope, risk/compatibility. Overall high
because deployment/composition is included; UI increment itself is bounded and
reversible. Installed catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd selects
lead_reviewed reviewer gpt-6-astra/xhigh/read_only. Prefer the prior verified
standalone reviewer for this coherent follow-up if its identity remains
addressable; otherwise use a fresh catalog fallback and record that reason.

No merge approval. No new abstraction, refresh change, clipboard change or reset
logic change. Trusted local operator boundary from repository AGENTS applies.
Portal owns these presentation controls; provider contracts remain unchanged.
Workspace nested runtime input and config channel are actual consumers.
Keep reviews read-only and perform all assigned lanes yourself.
