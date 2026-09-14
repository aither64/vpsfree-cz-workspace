---
lifecycle: active
---

# User metrics documentation

## Status and scope

- Completed a source-based solution proposal in `plan.md`.
- The user requested suggestions, not implementation. No project code,
  production pages, staging content, or deployments changed.
- Recommended shared API metric definitions, a collapsible WebUI reference,
  and managed bilingual KB examples checked against metadata and real exports.
- No code tests or mandatory code review run: this is coordination/design
  work only. Implementation verification is specified in the plan.

## Repositories and ownership

- Verified `dev-session current` and `DEV_SESSION_SLUG` both equal
  `2026-09-14-user-metrics-docs`.
- Workspace: `/home/aither/workspace/ai/vpsfree.cz`, shared branch `master`.
- Tracking: `work/2026-09-14-user-metrics-docs/`.
- No feature branches or worktrees created or registered.
- Proposed repositories: `vpsadmin` and `vpsfree-kb-contracts`.
- Fetched upstream heads inspected:
  - vpsadmin: `791ab3aa89e2f613979da6090b89785c78245db5`.
  - vpsfree-kb-contracts: `919577d0c770e47b623c591f8bf0cce4e8d30666`.
- Local bare master refs were older; final findings use fetched origin/master,
  including metrics version 1.1 and account security data.

## Commands and evidence

- `dev-session current`, `printenv DEV_SESSION_SLUG`, `dev-session url`.
- Inspected shared status and index; preserve all unrelated session changes.
- Fetched origin master in both canonical bare repositories.
- Read project rules, user/core/plugin exporter sources, token model/resource,
  WebUI token views, enums, localization, metrics route specs, managed page
  registry, sample runtime test, and WebUI documentation workflow.
- Read production with `kb-page get --wiki org manuals:vps:metrics` and
  `kb-page get --wiki cz navody:vps:metriky`. A guessed Czech ID ending in
  `metrics` was absent; navigation contracts supplied the correct `metriky` ID.
- Consulted official Prometheus exposition, functions, promtool, and rule-test
  documentation.
- Applied dev-session-handoff and vpsfree-user-facing-writing with its pinned
  English Humanizer in embedded mode to the finished proposal.

## Findings

- Scope is the user exporter, not the separate infrastructure Prometheus task.
- Explain monthly accounting gauges and conditional absence explicitly.
- Derive pool scan values from the model; HELP is currently incorrect.
- DNS priority HELP incorrectly specifies seconds.
- Include plugins and configured language-dependent outage labels.
- KB metrics pages have navigation contracts but are not managed page sources.
- Synthetic rules and catalogue checks need actual exporter behavior tests.

## Next action and open decisions

- Present alternatives and recommendation for the user's design choice.
- If implementation is requested, reuse this session, create feature worktrees
  from current upstream, and complete the metric semantics inventory first.
- Suggested default: normal API authentication for the catalogue; public
  documentation is an optional policy choice.
- Final grouping and example selection can be refined during implementation.
- Production approval is a later action on exact staged candidates.

## Cleanup and handoff

- No clusters, temporary worktrees, credentials, or bulk captures created.
- Keep the session open for follow-up; no lifecycle cleanup is authorized.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-user-metrics-docs/
