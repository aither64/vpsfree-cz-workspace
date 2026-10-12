# vpsAdmin Markdown documentation review

## Request and acceptance

The user accepted a proposal to replace ikiwiki under docs/ with ordinary
Markdown, retain useful current documentation, and remove obsolete pages.
There is no requirement to build or publish a site. The collection must be
readable from the checkout/GitHub, indexed, and free of ikiwiki dependencies.
Retained technical explanations must describe the current implementation.

## Scope and revisions

- Initiative: `2026-09-15-vpsadmin-docs`.
- Plan/state: this directory's `plan.md` and `state.md`.
- Repository/worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-vpsadmin-docs/vpsadmin`.
- Base: `f8fb5b3af225f20b40ad16df49d4f4ceca68fcf7`.
- Head: `48a456ceba8bb7c462321ac28429790f50efe969`.
- Branch: `2026-09-15-vpsadmin-docs`.

Two commits:
1. `b3e7118ed`: remove obsolete v2/v3 release and upgrade material, scripts,
   OpenVZ VPS layout/console/shaping guides, and corresponding index entries.
2. `48a456ceb`: convert and update retained docs, consolidate storage stubs,
   remove the ikiwiki recipe/CSS/editorconfig, and update README/AGENTS pointers.
   Format conversion and factual corrections stay together so the Markdown
   collection is introduced as documentation of supported behavior.

## Decisions and non-goals

Use plain Markdown now. No MkDocs configuration, renderer, publication,
external wiki change, runtime code change, dependency pin, or deployment.
Keep `docs/LICENSE` and `docs/i18n-cs.md` byte-identical. Git history preserves
removed documents. No separate historical archive or empty topic scaffolding.
Do not require a comprehensive rewrite of undocumented subsystems.

## Documentation and evidence

New index: `docs/README.md`. Retained topics: `overview.md`, `transactions.md`,
`object-lifetimes.md`, `plugins.md`, `storage/README.md`, `storage/branching.md`,
and `storage/download.md`. Source links in each page identify implementation
checks. The context-owning agent applied the user-facing writing workflow and
English humanizer after technical verification.

Quick verification:
- `python3 ../.../check-docs.py` from the worktree: 92 local links in 11
  Markdown files pass, including anchors, index coverage, code fences, page
  titles, preserved license/terminology files, and obsolete-markup checks.
  The exact script is in this tracking directory.
- `git diff --check` and staged whitespace checks: pass.
- Both commits passed mandatory Overcommit hooks in `nix develop .#vpsadmin`,
  including API/WebUI translation health and migration-spec coverage.
- Commit 1 has nonfatal 72-column message warnings; all lines meet the
  repository's 80-column requirement. Commit 2 has no hook warnings.
- No VM integration tests for documentation-only changes.

## Risk and compatibility

Low risk: source documentation changes only, reversible in Git, without
runtime/API/schema/security/protocol behavior changes. The removed Makefile
was exclusively the obsolete docs build/deploy recipe. Existing hosted sites
are not altered. External links to removed repository paths can break;
in-repository entry points are updated. No rollout ordering or data rollback
is needed. API specs CI may run because it includes AGENTS.md in its paths.

Selected lane: general (documentation-only; no new build/framework/runtime
logic). Model gpt-6-astra, reasoning xhigh. Inspect the committed series,
retained claims against source, link/navigation quality, and removal scope.
Report actionable findings without editing project files. Write the review
into `review-general.md` in this directory.
