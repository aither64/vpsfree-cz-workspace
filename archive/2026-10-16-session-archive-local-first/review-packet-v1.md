# Final archive reliability review

Requested outcome: archive closes locally after durable preservation, independent
of Git fetch/hooks/shared master failure. Tracking retries separately and pending
archive/revive transitions coalesce to latest state. Reduce proportional cost of
large clean checkout preservation; portal/browser interruption must not kill the
worker. Deployment is authorized, default-branch integration is not.

Read plan.md, design.md and state.md here. review-heads.json gives exact complete
ranges and ordered series; *-review.diff are complete final diffs. All source
changes are committed and quick checks pass. Review ALL three branches, including
the inherited already-deployed Codex baseline and final composition. No database
migrations. Versioned on-disk formats ARE changed: inventory2, archive journal4,
cleanup sidecar3, revive journal5, tracking receipt1, portal operations2. Inspect
old readers, generation guards, old-journal retry and rollback refusal.

Overall risk HIGH: destructive checkout removal, recovery integrity, persistent
journals, worker authorization and package/deployment ordering. Assign general,
architecture/repetition, scope/proportionality and risk/compatibility lanes.
Follow ~/.codex/skills/mandatory-change-review/SKILL.md and all four references.
Root AGENTS.md and applicable docs/agent-instructions procedures govern this task;
read affected repository AGENTS.md before review. Keep read-only.

This initiative was created threadless, null roster. Installed catalog digest
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd selects
lead_reviewed/reviewer: gpt-6-astra, xhigh, read_only. Standalone fallback is used
because no retained review member exists. Review directly; no nested agents.

History inventory and inherited baseline:
- Runtime 1b2a0e7/3c57e2e are the exact already-deployed Codex0.163 baseline from
  initiative 2026-10-16-update-codex. Our two logical commits introduce Git-backed
  recovery, then local completion/deferred sync/supervised execution. Narrow
  fixes are folded into owners. The second commit keeps CLI, persisted receipt,
  portal worker and host retry service together because local closure must never
  be enabled without a durable retry/status/compatibility mechanism.
- Workspace 65acdda7 reproduces deployed f5da0f7e skills composition on current
  shared master. Pin0fcf9d9c is the ONLY runtime pin in our series, including all
  transitive Codex0.163 input updates. Lifecycle instructions078e8c88 own local
  closure semantics. Current base5a9cb6b6 contains tracking-only shared changes.
- Configuration inherits exact deployed skill8f9b857d and llm-agents81ab9fad,
  followed by ONE final generated devWorkspace update0ced1926. The superseded
  deployed devWorkspace pin107255f8 is not copied into this branch. Its source
  remains retained by the other owner's branch and coordination artifacts.

No superseded archive formats from unmerged iterations remain intentionally;
predecessor archive/revive journals and schema1 full snapshots are existing
supported persisted boundaries. No application DB migration or fleet update.
Please explicitly conclude whole-branch history, repeated pin consolidation,
format/migration lineage and supported deployed compatibility.

Contracts/consumers: generic dev-workspace owns recovery, lifecycle, tracking
receipts, host service and portal execution. Site workspace consumes through
nested vpsfree-dev-workspace/dev-workspace, extension stays767dfd587e346168e1443e65ccdb67ce748f3fe3.
Configuration consumes devWorkspace through its dev-workspace/devWorkspace channel.
Both select2d7e8efe. Installed codex-web a0561fad remains unchanged. Inspect actual
imports, wrappers, packaging, locks and generated contracts. Local operator is
trusted per runtime AGENTS; remote portal clients are untrusted. Preserve exact
session/workspace/generation locks, cluster/coordinator ownership and snapshots.

Quick evidence: final-focused-ruby.log:7 runs122 assertions (coalescing, clean
Git recovery, filter fallback, conflict stages/binary bytes, worker authorization,
metadata cache and coordination completion). Earlier host2 runs6 assertions pass.
rebased-quick-go.log passes selected worker/store/timeout/browser contract checks;
internal/session regex matched no cases in that rerun, prior focused session
checks passed (focused-go.log). Workspace instructions8 runs144 assertions pass.
Composition checker passed2d7e8efe; diff --check clean. CI prebaseline failure was
synthetic fixture missing its schema; fixed in owning commit, exact test passes.
Long acceptance/package/scale tests await this review; identify meaningful gaps.

Docs: runtime docs/dev-sessions.md and docs/session-archive-recovery.md own
behavior/recovery/compatibility. Workspace lifecycle procedure changed. Rollout
status and exact deployed provenance belong in state.md, separate from feature
docs. Deployment must activate matching system host contract before user profile.
Aitherdev remains reserved by update-codex; never bypass it. No activation done.

Non-goals: artifact deletion/curation, changing archive eligibility/merge policy,
removing hooks or integrity checks, default-branch integration, global task
framework, recovery garbage collector. Retained supervised units are currently
not collected; assess that concrete operational cost proportionally.

Report findings by severity with file/line and commits. Include all distinct lane
conclusions, whole-branch history and migration/format conclusions. Save the full
report only to this initiative's review-report.md (that report is the sole allowed
write); send a concise result to parent. Do not implement fixes or launch long tests.

Additional parent evidence: rebased-session-go.log now passes the complete
internal/session suite and the exact deadline/error-format regression at the
packet runtime head. No source heads changed. Acceptance scripts and fixtures
are prepared here, unexecuted until findings are resolved. They include a real
user-manager worker/cancel/new-observer test and scale archive/revive test.
Parent follow-up tool messages appear to arrive encoded; ignore unreadable
messages. The original packet remains authoritative.
