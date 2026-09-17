# Automatic Luna monitoring

## Goal
Reduce routine monitoring usage by automatically delegating long tests, CI checks,
and builds to fresh gpt-5.6-luna/low subagents. Keep planning, implementation,
diagnosis and review on gpt-6-astra/xhigh in the original parent conversation.

## Components and approach
- dev-workspace owns the built-in dev-session-monitor skill, catalog packaging,
  tests and generic user/developer documentation.
- vpsfree-dev-workspace consumes the reviewed generic revision without owning
  the generic skill.
- workspace owns its automatic-use/model policy and downstream extension pin.
- vpsfree-cz-configuration aligns its devWorkspace host input using confctl and
  deploys aitherdev from this initiative branch. The latest user instruction
  explicitly authorizes configuration integration into master.

Use native delegation, fresh context and explicit model/effort. Delegate expected
waits over one minute and uncertain integration tests/builds before starting them.
Watchers own new commands or observe external logs/status, return compact evidence,
and cannot edit, diagnose, retry, accept verification, deploy or spawn agents.
Parents avoid duplicate polling and continue on completion/escalation. Missing
Luna/capacity falls back visibly to minimal-output parent monitoring. Caller
cancellation/escalation rules remain authoritative, including unexpected kernel
builds in this workspace. No persistent supervisor, portal scheduler, default
model downgrade, broad AGENTS rewrite or usage dashboard.

## Compatibility and deployment
No API, database, protocol, manifest, persisted-state or catalog-schema change.
Reuse existing schema-1 skill catalog and managed links. Old packages lack the
skill and use the visible parent fallback; rolling back removes only its managed
link. Preserve runtime/Codex compatibility and avoid unrelated dependency updates.
Align extension/workspace/host generic revisions and validate the existing site
contract. Deploy application with workspace-host switch; keep application out of
system configuration. Respect active-turn/cluster guards and report deferred
reconciliation separately. No coordinated infrastructure/node upgrade is needed.
User authorizes deployment to aitherdev and explicitly waives waiting for CI.

## Verification
Validate skill front matter/UI metadata, meaningful core/extended catalog and
collision checks, focused local checks, committed mandatory Astra/xhigh review,
then package checks and live delegation scenarios. Verify real model metadata,
fresh watcher context, automatic parent continuation, success/failure evidence,
quick-check exclusion, fallback and caller-directed escalation behavior. Review
the CI monitoring contract without waiting for CI, as requested by the user.
Do not claim a fixed weekly saving. Keep recorded logs bounded and secrets absent.

## Documentation and decisions
Readers are workspace users/operators and future skill maintainers. Generic
behavior belongs in dev-workspace skill/session guide/README. The consuming
workspace holds its concise policy. Exact heads, review, deployment and recovery
evidence belong in this initiative. Native Luna delegation for tests, CI and
builds was explicitly selected by the user; generic ownership was explicitly
corrected and accepted. Keep sessions and branches for follow-up.

User now explicitly authorizes merging both Luna monitoring and instruction
routing into all default branches, including configuration. Complete reviews
and verification first; do not wait for CI or close the sessions.
