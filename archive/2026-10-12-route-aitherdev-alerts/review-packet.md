# Final review: selected machine recipients

Review the completed committed deliverable directly. Do not edit source or
spawn another reviewer. Return findings ordered Blocking/Important/Advisory,
with file/line and commit references, plus residual risks and explicit final
whole-branch history, migration and repeated-stream conclusions.

## Requested result and boundary

The user requested a generic per-system marker selecting exclusive recipients,
then authorized implementation. Add nullable `monitoring.alertRecipients`;
null keeps team behavior, nonempty registered IDs replace it, invalid/empty
selections fail. Enable only aither for aitherdev. Preserve severity=none
silence, default mail/SMS intervals, daytime/fatal policies and resolved
notifications. Exclude shared Telegram from selected systems. Use existing
FQDN identities and subject `node_fqdn` precedence, without modifying metric
labels/rules. Public/global alerts without machine identity retain team policy.
No production deployment, notifications, integration or input/secret changes.

## Scope and exact history

Session: `2026-10-12-route-aitherdev-alerts`, workspace
`/home/aither/workspace/ai/vpsfree.cz`.
Worktree: `worktrees/2026-10-12-route-aitherdev-alerts/vpsfree-cz-configuration`.
Base/default: `8e4da52c55f1d4396547630d1d4de518f8255619`.
Head: `a33c499f0117c189213a9cc70113f7906965f53f`.
Whole-branch inventory: [branch-inventory.md](branch-inventory.md).
Complete diff: [configuration-final.diff](configuration-final.diff).

Two commits: supporting contact/route/identity refactor
`c9dffde58bddc37736da2cea3c79dc4bd55ba7e3`, then selected-recipient behavior and
its tests/docs `a33c499f0117c189213a9cc70113f7906965f53f`. The first preserves
team behavior; the second changes only marked systems. No obsolete or fixup
iterations, no repeated dependency/input streams and no migrations. Nothing
has been merged, released, deployed or externally consumed.

## Review policy and settings

Use `/home/aither/.codex/skills/mandatory-change-review/SKILL.md` and read all
four references: general-review.md, architecture-review.md, scope-review.md,
risk-review.md. Risk is high because wrong routing can disclose notifications
to unselected people and mixed Alertmanager versions can still notify the
team. Review architecture, proportionality, compatibility and final history.

Selected retained member: reviewer0, thread
`01a13084-9461-7121-8f22-b3d5f06c2591`, purpose review, ready, independent,
read-only, saved model gpt-6-astra / xhigh. No overrides or fallback. Verify
session identity with `dev-session current` and the exact developer binding and
environment markers before session-owned records. Read workspace AGENTS.md and
applicable routed procedures, plus repository AGENTS.md before review.

## Evidence and documentation

- Lead [design.md](design.md), [plan.md](plan.md), [state.md](state.md).
- Project `docs/services/monitoring.md` describes policy, recipient registry,
  identity precedence, deployment and rollback; existing mkdocs navigation
  already links it. Main agent applied vpsfree-user-facing-writing directly.
- Nix format, shell syntax and `git diff --check` passed.
- Focused offline flake checks `alert-recipients` and `infra-monitoring-config`
  passed in 26 seconds: [quick.log](quick.log), [quick.status](quick.status).
  Exact final tree matches their evaluated derivations; no code changes were
  made after quick checks. Both commits passed active Overcommit Nixfmt and
  commit-message hooks. Only TextWidth advisory warnings (>72, <=80) occurred.
- Offline `amtool` uses inert receiver names. Nix assertions verify selection
  validation, email destinations and SMS interval configuration. These do not
  verify real delivery, runtime daytime activation, repeat timers or inhibition.
- No branch push-triggered CI exists; the only workflow is scheduled/manual
  Daily update. It is outside this feature's verification.

## Consumers and compatibility

Configuration repository owns the option, registry and routes. Both configured
Alertmanager containers import the shared alerter module. Cluster machine
`module.nix` files consume recipient metadata; monitor and alerter share the
management-FQDN helper. No cross-repository interfaces or pins change.

Only both Alertmanager replicas need a runtime update. Existing monitor,
exporter and machine identities/state stay unchanged. An old replica can keep
team delivery until both load the new routes. Reverting both restores prior
routing without migrations/state deletion. Longer validation after final
review will run monitoring rules checks and real builds of alerts1/alerts2.
