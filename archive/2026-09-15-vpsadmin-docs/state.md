---
lifecycle: complete
---

# vpsAdmin Markdown documentation

## Current status

Implemented and fast-forwarded into remote `vpsadmin/master` at
`564cc80ea5d4420d0f2441c996fb0df2f82bb39c`. The remote default and feature
branches both point to that exact commit. Documentation checks, independent
review, API specs, migration specs, i18n, RuboCop, and WebUI PHPUnit passed.
The temporary merge checkout was removed. The feature worktree, branches, and
session remain open.

## Next actions

- No implementation, integration, deployment, or user action remains for the
  requested documentation migration.
- The push to master triggered duplicate checks on the same tested commit.
  An additional full integration workflow remains queued due solely to the
  inherited upstream dependency delta; see the scope assessment below and
  [CI snapshot](ci.json). No current-head run was canceled.

## Repository and commits

- Repository: `vpsfreecz/vpsadmin`, SSH origin `git@github.com:vpsfreecz/vpsadmin.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-15-vpsadmin-docs/vpsadmin`.
- Branch: `2026-09-15-vpsadmin-docs`, clean and tracking its remote branch.
- Base: `ff5d5e5914bf5746e649f3a986659e4193717044` (fetched upstream master).
- `40c1a384f40357251c91672b0dd174b03888cbd6`: remove obsolete release/upgrade
  instructions, migration scripts, OpenVZ VPS/console/shaping guides, and links.
- `564cc80ea5d4420d0f2441c996fb0df2f82bb39c`: introduce the maintained Markdown collection and entry points.
- Before integration, upstream advanced with `ff5d5e591` (WebUI PHPUnit
  dependency metadata only). Rebased cleanly; `git range-diff` confirms both
  documentation patches are identical to the reviewed series. Repeated
  Markdown/whitespace checks pass. No review rerun is needed for the unchanged
  patches. Pushed with an explicit lease on the previous feature head.
- Saved the comparison with `dev-session worktree capture-comparison
  2026-09-15-vpsadmin-docs vpsadmin --as-is` at the final head.

## Documentation

Start at `docs/README.md`. Topics are `overview.md`, `transactions.md`,
`object-lifetimes.md`, `plugins.md`, `storage/README.md`,
`storage/branching.md`, `storage/download.md`, and the existing `i18n-cs.md`.
The root README and AGENTS link to the index. There is no generator or
publication configuration. License and Czech terminology guide are unchanged.

Checked retained explanations against transaction construction/scheduling,
confirmations, lock handling, lifetimes, plugin loading and migrations,
storage transfer/rollback/branching/retention, and download/CLI implementations.
Each topic links its source. The context-owning agent applied the user-facing
writing skill and English humanizer after establishing technical facts.

The accepted design, removal rationale, compatibility, and commit split are in
[plan.md](plan.md). Current project knowledge lives in the project docs.

## Verification

- `python3 .../check-docs.py` from the worktree: 92 local links in 11 Markdown
  files pass. Checks include anchors, index coverage, code fences, page titles,
  absence of ikiwiki syntax, and byte-identical license/terminology files.
- `git diff --check` and staged whitespace checks pass.
- Both commits and the final narrow amendment passed all mandatory Overcommit
  hooks in `nix develop .#vpsadmin`: API/WebUI translation health, migration
  coverage, and applicable formatting checks. The removal commit's message
  produced nonfatal 72-column warnings; all lines meet the 80-column rule.
- Repository source searches found no remaining consumers of removed pages or
  one-off scripts. Generic `.mdwn` CI-ignore patterns are harmless and retained.
- No local VM tests: only documentation and retired docs-build helpers changed.
- Original-head RuboCop, migration specs, and both i18n jobs passed. The API
  run had 20 successful jobs and six running without failures when superseded.
  Canceled only that old-head run (`34963241869`) after the rebase push.
- New-head CI includes the upstream dependency delta in the push comparison,
  so WebUI PHPUnit and integration selection also run. No current-head
  workflow has been canceled. Results are retained in [ci.json](ci.json).
- All 27 API workflow jobs passed on final head `564cc80ea`, including topic
  coverage: run `34965422973`. Final-head RuboCop (`34965422977`), migration
  specs (`34965422938`), i18n (`34965422939`), and WebUI PHPUnit (`34965422981`)
  also passed. No failed runs were rerun or accepted without investigation.

## Mandatory review

Low risk: docs-only changes with no runtime, schema, API, protocol, or deployment
behavior changes. General lane, `gpt-6-astra`, `xhigh`, fresh context.
[Review packet](review-packet.md) and [general review](review-general.md).

Reviewed `f8fb5b3af..48a456ceb`: no Blocking or Important findings. One Advisory
requested an initialized-database prerequisite for plugin rake commands. The
agent independently found the same issue, and the reviewer inspected the
prepared correction. It was folded into `dab3317d7`, then rebased unchanged
as final head `564cc80ea`; focused checks and hooks pass. No rerun is required
for this narrow correction or the subsequent unchanged-patch rebase.

## Command verification and setup lessons

`nix develop .#api -c bundle exec rake -T vpsadmin:plugins` fails in a fresh
checkout with `ActiveRecord::ConnectionNotDefined` while loading SysConfig.
Ordinary rake task discovery requires an initialized API database. The guide
now states that prerequisite and the database configuration mechanisms.
The i18n tasks have a separate automatic test-database path. No production
database was accessed, and no plugin migration was executed.
See [reusable lesson](../../notes/vpsadmin/2026-09-15-plugin-rake-database.md).

Initial worktree creation returned nonzero because the post-checkout Overcommit
configuration was unsigned, although the branch and checkout existed. Inspected
`.overcommit.yml` and all custom hooks, installed/signed them in the root Nix
shell, and retried registration successfully. Prepared both root and API shell
dependencies for the translation health hooks.

An ambient-shell push was refused by the configuration-signature check before
remote mutation. `nix develop .#vpsadmin -c bash -c
'bundle exec overcommit --sign && git push -u origin 2026-09-15-vpsadmin-docs'`
succeeded. All hooks remained enabled.

## Session and cleanup

`dev-session current` matched `DEV_SESSION_SLUG`. Session remains active and
open; no lifecycle actions or delayed cleanup were invoked. Worktree and
branches are retained. Unrelated shared-workspace changes were preserved.
Tracking follows the initial commit plus in-working-tree update cadence.

Stable portal:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-15-vpsadmin-docs/>.

The user explicitly authorized default-branch integration after completion.

## Integration result

A fresh detached target worktree was created from `origin/master` at
`worktrees/2026-09-15-vpsadmin-docs/merge/vpsadmin`. Ran
`git merge --ff-only 2026-09-15-vpsadmin-docs`, verified its clean status and
documentation checks, then pushed `HEAD:master` from that checkout through
the repository Nix/Bundler shell. The last fetch before push showed no further
upstream advance. Remote master advanced from `ff5d5e591` to `564cc80ea`.

`git ls-remote` verified both `refs/heads/master` and the retained feature
branch at `564cc80ea5d4420d0f2441c996fb0df2f82bb39c`. Removed only the fresh
temporary target checkout with non-force `git worktree remove`. The clean
feature worktree stays open. Saved pre-merge comparison remains
`ff5d5e591..564cc80ea`.

Before merge, the repository CI selector returned `mode=skip` for
`origin/master..HEAD`.
The force-push comparison `dab3317d7..564cc80ea` contains only the already
upstream `webui/composer.lock` and `webui/php-packages.nix`; those unmapped
metadata paths select the full integration suite. That queued run is retained
but is not a gate for the docs-only merge. API specs, i18n, migration specs,
RuboCop, review, and local documentation checks all passed before integration.
The default-branch push triggered duplicate API/i18n/lint/migration checks on
the same commit; no second API run is needed to validate the unchanged tree.
See the [CI selection lesson](../../notes/vpsadmin/2026-09-15-rebase-ci-selection.md)
for the evidence behind this scope decision and typical platform-job duration.
