# Bounded implementation assignment

Exact session: 2026-10-03-newadmin-http-check. Workspace:
/home/aither/workspace/ai/vpsfree.cz. Verify dev-session current against this
identity and saved member access before doing anything session-owned.

Read in full before acting: workspace AGENTS.md; workspace procedures
projects.md, sessions.md, git.md, lifecycle.md, documentation.md, verification.md,
deployment.md and commits.md under docs/agent-instructions; your worktree
AGENTS.md; session plan.md and state.md. Read relevant repository README and
docs/operations/newadmin-webui.md. Honor saved GPT-6.1 Sol/xhigh settings.

Use only the registered vpsfree-cz-configuration feature worktree for this
session. Application ownership is yours. Preserve all unrelated work.

Implement plan.md exactly: whitespace-tolerant schema and SHA patterns; three
dedicated missing-metrics severity changes; one per-site severity value for the
two exact newadmin HTTP keys applied to both generated ExporterDown and WebDown
rules; all nine Newadmin alerts warning; existing expressions/durations/frequency
unchanged. All non-newadmin site and shared VPS infrastructure severity stays
unchanged. Update existing newadmin rule tests with warning expectations, both
ExporterDown scenarios, all-nine warning invariant, and API/console/legacy
critical controls. Update the existing newadmin operations guide's warning
policy. Do not add options, Alertmanager overrides, dependency/pin changes, UI
changes or generalized infrastructure.

Intended two commits: (1) probe regex fix in monitor/http.nix; (2) dedicated
warning policy plus supporting rule tests and operations documentation. This
keeps independently reversible behavior independently reviewable. Apply the
repository's commit-message, temporary message file and declared-hook rules.
No hook bypass. No merge, default-branch push or production deployment.

Run bounded quick checks only. Before uncertain-duration Nix environment setup,
check builds, integration tests or host builds, report exact required commands
to the lead so a fresh utility watcher launches them. No long checks yourself.
If dependencies/hooks are not ready, finish the edits and report the required
environment preparation rather than taking ownership of an uncertain build.
Do not launch integration tests before mandatory independent review.

Quick verification should parse configured regexes and exercise compact,
formatted and whitespace metadata, schema 10 and invalid full commit hashes;
use the same regex semantics as the exporter if available. Export generated
rules for quick promtool checks when tooling is ready. Do not add committed
regex test scaffolding for this small correction.

Report edits, commands/results, pending commands, final commit heads and any
deviations in implementation-result.md under this session tracking directory.
Keep lead-owned plan/state/portal unchanged. Return a compact report to the lead.
