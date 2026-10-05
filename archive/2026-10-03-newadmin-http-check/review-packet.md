# Independent whole-branch review packet

## Outcome and boundaries

Session: 2026-10-03-newadmin-http-check in
/home/aither/workspace/ai/vpsfree.cz. User requested implementation of the
approved plan: whitespace-tolerant frontend metadata probe and warning severity
for every dedicated Newadmin alert. The user explicitly selected dedicated
alerts only, retaining shared VPS infrastructure severities. Preserve API,
console and legacy WebUI HTTP critical severity and all names, expressions,
thresholds and notification frequencies. No dependency/pin, app, schema, routing
or Nix interface changes. No merge or production activation is authorized.

## Instructions and reviewer

Use /home/aither/.codex/skills/mandatory-change-review/SKILL.md and read all four
references for general, architecture/repetition, scope/proportionality and
risk/compatibility lanes. Read workspace AGENTS.md and required procedure
routes, the affected repository AGENTS.md, plan.md/state.md and owning
operations documentation. Review independently and directly without nested
agents. Remain read-only; return findings and conclusions to the lead.

Retained eligible reviewer: reviewer0, GPT-6.1 Sol/xhigh, purpose review,
read-only. Reconfirm readiness/identity/settings before assignment. No model or
effort override. Overall risk is classified high conservatively for production
notification severity and two-monitor mixed-revision deployment consequences;
implementation is otherwise bounded, reversible and state-compatible.

## Repository and final inventory

Only vpsfree-cz-configuration changes. Worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-newadmin-http-check/vpsfree-cz-configuration
Branch: 2026-10-03-newadmin-http-check. Base:
657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da. Final head/series, diff and quick-check
evidence will be appended before assignment. The intended split is two logical
commits: probe matching correction; dedicated severity policy with supporting
rule coverage and operations documentation. These changes can be independently
reviewed and reverted.

No migrations: no database, persisted-state, release migration or on-disk
format change. Inventory superseded commits/follow-up fixes before final review
and require an explicit whole-history conclusion, not just the latest diff.

## Compatibility and documentation

Regex correction accepts both current formatted and compact schema-1 metadata.
Schema 10 and non-full/lowercase-hex commit hashes remain rejected. The HTTP
rule generator computes warning only for the two exact newadmin site keys and
critical for every other existing site. All nine dedicated Newadmin rules are
warning. Consumers are the generated blackbox and Prometheus configurations on
int.mon1 and int.mon2; existing Alertmanager routing consumes their labels.

The owning operations guide docs/operations/newadmin-webui.md records the
warning-only policy. No interactive UI or KB behavior changes. This session's
rollout.md is prepared operator guidance only. An old monitor can continue to
emit compact-body false failures and critical alerts until both are updated.
A whole-change rollback reintroduces those effects; no state rollback is needed.

## Required result

Return ordered Blocking/Important/Advisory findings with concrete file/commit
references, or explicitly state no findings and residual verification gaps.
Conclude whether the complete series retains obsolete approaches/fixups,
whether migration lineage is sound (explicitly no migrations), whether scope
matches the dedicated-warning choice, and whether documentation is correctly
placed. This final whole-branch assessment is required for branch readiness.

## Final committed inventory and completed quick checks

Upstream was fetched before final review and still matches the base. The
feature head descends from origin/master without rebase. Exact final head:
7e32833aca1cb65902b50f61eb76dd1022691591. Complete series:

1. fae43505f2b52f849627b571265b7d7906447dcf — monitor: allow whitespace in
   newadmin metadata probes. Only http.nix changes.
2. 7e32833aca1cb65902b50f61eb76dd1022691591 — monitor: keep dedicated newadmin
   alerts at warning. Rule generation, supporting tests and policy documentation.

Complete final diff: review.diff beside this packet. Five files, 221 insertions
and 51 deletions. The lead inspected the complete diff and messages; no obsolete
functional approach/fixup or migration remains in the reachable series. The
probe commit's earlier message-only versions were replaced to satisfy the
hook's stricter subject/body width warning; no unpublished behavior iteration
is retained. No migrations, prior deployments or externally consumed feature
versions exist for this branch. No pin or generated update commits.

Quick verification at final application content passed before assignment:
15 Go-regexp fixtures from evaluated source patterns; pinned promtool 3.12.0
check (36 rules) and tests (17 scenarios); the actual test Nix file's exact
nine-name/count/warning assertions; base/final generated-rule comparison
(exactly seven approved severity changes, all other fields/rules identical);
nixfmt and both final Overcommit commits; Git diff check. Worktree is clean.
See implementation-result.md for exact commands and fixture/tool details.
Full flake realization, host builds, live production exporter retest and
production deployment have not happened. They are not prerequisite evidence
being claimed for this review.
