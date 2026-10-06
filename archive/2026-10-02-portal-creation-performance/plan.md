# Portal session creation performance

Implement the accepted optimization plan for new sessions, approved-plan
sessions, forks and retries. The preceding investigation is
`work/2026-10-02-portal-creation-latency/analysis.md`: the observed 103.55-second
creation spent about 98 seconds in filesystem-backed Codex thread discovery.
Database-only discovery took 4–7 milliseconds. Normal thread reads were cheap.

## Scope and ownership

Use a new Full team initiative. The retained design member owns `design.md`;
the retained implementation member owns application changes; an independent
review-purpose member reviews committed changes. The coordinating conversation
owns tracking, dependency sequencing, verification decisions and deployment.

Affected repositories: codex-web (optional database-only listing), dev-workspace
(freshness/recovery and streamed progress), vpsfree-dev-workspace and workspace
(dependency pins), and vpsfree-cz-configuration (matching host input).
All feature work uses isolated worktrees under this slug and SSH remotes.

## Implementation

Determine freshness under existing locks before writing a creation journal.
Proven fresh attempts start or fork directly; retries preserve recovery.
Add an optional `UseStateDBOnly` list option, omitted when false. Recovery checks
loaded and indexed threads, preserving cwd, source, ownership, history and fork
validation. Exclude only exact validated retained team member IDs. Empty,
failed or inconsistent fast discovery must perform the existing complete scan
before creating a replacement. Confirmed ambiguity or mismatch remains a
refusal. Preserve the initial-goal attempt marker and exact root identity.

Design refinement: Codex's index has no completeness proof even for nonempty
pages. Preserve the complete scan before every recovery adoption or replacement;
fast discovery can reject positively proven ambiguity early. This keeps the
existing uniqueness guarantee. Fresh starts and forks remove normal latency,
and rare recovery is allowed to retain the measured scan cost with progress.

Accepted recovery refinement: a proven loaded root without persisted history
retains its original start-time frozen policy and is adopted without resume.
Codex cannot resume that root until its first request materializes history.
Materialized roots still use the existing resume path. Missing rollout and
thread-not-loaded errors remain uncertainty, so they cannot authorize replacement.
The original unavailable fault root stays untouched; fresh exact real fault
cases supply corrected recovery acceptance without repeating the timing cohort.

Stream opt-in framed JSON progress over stderr through nested Ruby and Go
helpers. Preserve existing JSON stdout and diagnostic stderr. Update only the
active receipt attempt, using its existing phase field. Cover conversation,
recovery, team, prompt, terminal and final evidence stages with elapsed timing.
Progress cannot itself mark a session ready. Team bootstrap remains sequential.

Document supported behavior and recovery in the owning projects, with concise
source comments for freshness and fallback invariants. Readers are runtime
maintainers and operators; individual deployment evidence stays in this session.

## Compatibility and recovery

No persisted schema, database migration, protocol-breaking change, Codex patch,
Codex upgrade, or archive/delete/revive change is planned. Existing helpers and
SDK callers retain default behavior. Verify the optional list field against
the installed Codex 0.160 protocol. Every recovery adoption or replacement keeps
complete filesystem discovery, even after indexed hits; it may retain the old
scan cost, with visible progress. Fresh paths avoid that scan under existing locks.

Deploy SDK and runtime revisions, then extension/workspace pins and the matching
configuration input. Mixed old/new callers must remain valid. Configuration
and application deployment are separate: aitherdev through confctl, application
through the user profile. Package recovery is a new forward generation reverting
the faulty change, never a previous profile generation. Retain canary sessions,
branches and tracking. Deployment does not authorize default-branch integration.

## Verification and acceptance

Protocol fixtures must reject filesystem discovery on fresh new, approved-plan
and fork paths. Exercise lost responses and interrupted journal/thread/manifest,
team, prompt and evidence steps, proving stable IDs and exactly-once prompts.
Cover loaded-only recovery, restart, missing/stale/failed DB, ambiguity, wrong
fork and exact team-member exclusion. Test progress before command completion,
malformed and oversized frames, failures, stale attempts and old helpers.

Run focused quick checks, commit intended changes, inventory whole-branch history
and migration provenance, and run mandatory independent review before long
integration checks. Fresh catalog Luna/low utilities own long checks and waits.
Run five sequential isolated warm Full-team creations with representative
history: median under 10 seconds, maximum under 15 seconds. After deployment,
retain one actual-history portal canary; measure acceptance to ready separately
from the first model response.

## Deployment

Publish reviewed feature branches over SSH and advance the dependency chain:
codex-web → dev-workspace → vpsfree-dev-workspace → workspace. Set the confctl
`dev-workspace` channel's `devWorkspace` input to the exact generic runtime
revision. Run `bin/check-dev-workspace-deployment` against the owned workspace
and configuration worktrees. Build `cz.vpsfree/machines/aitherdev`, dry-activate,
then activate the host configuration. Switch the workspace user profile through
the supported host command. Verify health, revisions, retained conversations,
progress and canary timings. Keep all feature branches unmerged until explicit
repository/target integration direction.
