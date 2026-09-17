# Knowledge-base and user-facing writing

Required workspace procedure, selected by the routing table in `AGENTS.md`.
Its rules retain workspace scope and precedence. Paths and commands are relative
to the coordination workspace unless the text specifies another repository.

DokuWiki user documentation is hosted at `kb.vpsfree.cz` and
`kb.vpsfree.org`. Their review instances are
`kb-cs.aitherdev.int.vpsfree.cz` and `kb-en.aitherdev.int.vpsfree.cz`. API
access to production uses one token per wiki:

When authoring or translating Czech KB pages, address the reader using
informal singular forms (`tykání`), for example `můžeš`, `potřebuješ`,
`nainstaluj`, and `použij`. Do not use formal `vy` or plural imperatives as a
polite form; use plural only when genuinely addressing multiple people.

The invisible DokuWiki `<page>` tag connects Czech and English translations.
Use the same tag value in every language variant, and always derive it from the
English KB page ID. The real DokuWiki page IDs remain language-specific.

For all user-facing prose, use the workspace skill in
`~/.codex/skills/vpsfree-user-facing-writing/SKILL.md`. This applies to KB pages,
vpsAdmin documentation and interface copy, user-visible errors and help, mail
templates, website copy, and member-facing release or operational messages.
The agent that owns the task context must apply the skill directly after the
technical content is settled and before committing. Do not delegate the main
rewrite to a context-poor subagent; a fresh agent may review the finished text.
Human-readable comments in bilingual scripts and configuration examples must
use the language of the surrounding page while commands and machine-significant
content remain equivalent.

Write KB pages as documentation of the current supported state. Do not
mention obsolete distributions, former defaults, superseded commands, or
historical workarounds unless readers of a still-supported installation need
that history to migrate or recover. Record removal rationale in commit
messages, DokuWiki revision summaries, or initiative notes instead of page
prose.

For vpsAdmin changes that can affect visible WebUI documentation, follow the
canonical workflow in `vpsfree-kb-contracts/docs/webui-change-workflow.md`.
Use `kb-contract-fetch`, `kb-contract-build`, and
`kb-contract-manifest` for durable all-page candidate preparation; keep
capture generation and the documentation contract in the independent capture
repository.

Do not merge a `vpsfree-kb-contracts` feature branch merely to make managed-page
links work in staging. Managed release manifests pin the committed and pushed
feature revision, and staging resolves `<kb-managed>` links at that exact
commit. Before production promotion, integrate the contract changes into
`master`; the release tool verifies the recorded page and test files against
remote `master` before it writes production pages.

- `kb.vpsfree.cz`:
  `/home/aither/.codex/codex-kb-vpsfree-cz-aither-key`
- `kb.vpsfree.org`:
  `/home/aither/.codex/codex-kb-vpsfree-org-aither-key`

Never copy credentials into notes, commits, command output, URLs, or prompts.
Always prepare wiki changes as local candidate files first. Use `kb-page`
for individual DokuWiki operations and `kb-release` for a review bundle
instead of hand-crafting API calls.

The declarative `kb-staging` NixOS container on aitherdev is global and
on-demand. Its data and ownership survive `kb-stage stop`; only
`kb-stage reset --yes` discards staging content and mirrors the current
production pages and shared media. A development session must claim staging
with `kb-stage start` before it can write. Staging ownership is serialized
by the active `DEV_SESSION_SLUG`; do not manipulate another session's
staging data or ownership. `kb-stage release --yes` stops the container and
releases ownership while retaining the data. It refuses a pending review
bundle unless `--discard-pending` is explicit.

Stage complete pages at their real page IDs so links and language mappings are
reviewed exactly as they will appear in production. For every new release,
prepare one bilingual `release-changes.yml` with an informative localized
summary for each page write or deletion, then generate checksummed schema-5
manifests with `kb-contract-manifest --changes FILE`. Stage them with
`kb-release stage --manifest FILE --yes` and verify them with
`kb-release verify --manifest FILE`. The verification output must expose
each exact summary and its clickable staging revision-history URL so the user
can review revision metadata before publication. Do not use the production
`drafts:` namespace for routine review. The release tool verifies that
production still matches the recorded source revision and content before
staging or promotion.

Production writes always require direct user approval. After approval, promote
the exact staged manifest with `kb-release promote --manifest FILE --yes`
and `--approved-production`. Individual production writes with `kb-page`
also require `--approved-production`, including writes in `drafts:`. Read-only
production checks do not require approval. Before every write, verify
authentication and page permission against the exact target wiki.

Every production page edit must have an informative, single-line change
summary that describes the actual content change. Do not use generic summaries
such as "Publish reviewed KB release" for new edits. Write summaries for
`kb.vpsfree.cz` in Czech and summaries for `kb.vpsfree.org` in English.
Because each summary already belongs to one page, do not repeat that page's
title or subject. Describe only the resulting content changes.
Write Czech summaries as noun phrases that name the resulting changes, not as
infinitive instructions. For example, use `Doplnění síťové konfigurace a
vysvětlení správy obsahu v repozitáři`, not `Doplnit síťovou konfiguraci a
vysvětlit správu obsahu v repozitáři`. Do not rewrite existing DokuWiki
revision summaries merely to adopt this convention.

Page deletions belong in the same guarded schema-5 release manifest as page
writes. Stage and review their localized summaries and revision histories, then
promote the exact manifest after approval. Do not delete release pages with
separate `kb-page` calls. New `kb-cleanup` manifests must use schema 2 and give
every page deletion its own summary; media deletions do not have summaries.

Common KB tool examples:

```sh
kb-page whoami --wiki cz
kb-stage start
kb-stage reset --yes
kb-release stage --manifest work/example/kb-release.yml --yes
kb-release verify --manifest work/example/kb-release.yml
kb-page save --wiki cz information:published-page preview.txt \
  --summary "Aktualizace dokumentace" --update --approved-production
kb-release promote --manifest work/example/kb-release.yml --yes \
  --approved-production
kb-stage release --yes
```
