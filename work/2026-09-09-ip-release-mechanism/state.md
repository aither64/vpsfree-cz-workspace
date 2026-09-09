---
lifecycle: active
---

# IP release mechanism

## Status

- 2026-09-09: implementation proposal ready in `plan.md`. The user requested
  suggestions; no project code/templates or production data were changed.
- Keep the initiative active for discussion. Implementation follows if asked.
- Verified dev-session current matches VPSFREE_DEV_SESSION_SLUG exactly:
  `2026-09-09-ip-release-mechanism`.

## Repositories and branches

- Shared workspace: master; preserve unrelated modified/untracked records.
- vpsadmin: read fetched origin/master at
  `19971f039771500d5d0304610f91fe6f4af5fed3` from canonical bare repository.
- vpsfree-notification-templates: read fetched origin/master at
  `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676` from canonical bare repository.
- vpsfree-kb-contracts: read canonical WebUI documentation workflow.
- No project branch/worktree created. Future implementation should use this
  initiative slug if it continues before archival.

## Commands and findings

- Read workspace/repository AGENTS.md and notification README.
- Used git fetch/show/grep/ls-tree for IP ownership, assignment, resource locks,
  quota and DNS cleanup, mail tracking, scheduler, and notification templates.
- Proposed campaign, per-user request, and per-allocation outcome records.
- Default seven-day grace and immediate per-IP reason-based retention.
- Force disables reasons only; assigned addresses remain protected.
- Reuse Ip::Update accounting/cleanup with locked eligibility rechecks.
- Verify individual mail transaction success, with late/failed notices blocked.
- Additive deployment; enable expiry only after compatible API rollout.

## Verification and review

- Source inspection/design only; no runtime tests or builds performed.
- Plan describes required concurrency/accounting/mail/WebUI tests.
- Read mandatory-change-review skill: perform implementation review after
  committed project changes and quick checks. No project implementation or
  project documentation changes exist to review in this proposal turn.
- Shared workspace declares no tracked hook framework in .overcommit.yml,
  .pre-commit-config.yaml, lefthook.yml, .husky, or package.json.
- Plan/state whitespace, active lifecycle, and portal artifact YAML checks
  passed using Ruby/Psych. Ambient Python lacks PyYAML; used installed Ruby.
- Portal TLS check passed with its public CA and returned HTTP 401 as expected.
  Reused notes/cross-project/2026-09-07-portal-curl-private-ca.md after ambient
  curl could not verify the private CA.
- Prepared the initial coordination commit for plan/state/portal only. No
  project-code commit or external mutation is planned.

## Next action

- Discuss defaults with user; implement if requested.
- Before coding, create feature worktrees and read current repository rules.
  Fetch again because upstream and concurrent IP-accounting work may advance.
- Implementation must apply user-facing writing, mandatory change review,
  notification checks, and the WebUI documentation workflow.

## Portal and cleanup

- Applied skills/dev-session-handoff/SKILL.md; plan is in portal manifest.
- Stable URL:
  https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-ip-release-mechanism/
- No project worktrees, background jobs, credentials, or bulk captures created.
- Session remains active for design discussion.
