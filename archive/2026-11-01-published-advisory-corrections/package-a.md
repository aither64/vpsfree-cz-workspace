# vpsAdmin packages A and B: implementation receipt

Status: implemented, quick checks passed, committed and published; final
independent review and longer application verification remain pending. No
integration, production correction, deployment or lifecycle action occurred.

## Exact branch and history

Repository: `git@github.com:vpsfreecz/vpsadmin.git`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-published-advisory-corrections/vpsadmin`.
Branch: `2026-11-01-published-advisory-corrections`.

Base: `610a96f8ce523afbcd3e4374a70047dbe3264b0d`.

1. A: `892b68b4e9218143d3750b21e3cdbcce990620af`
   `api: allow silent corrections of published advisories`
2. B: `d80ac520c66a9d4a318df517a06f13ac717f2399`
   `webui: enable guarded published advisory corrections`

A is implementer0's package; B is implementer1's frozen deliverable, accepted by
the lead and committed separately by implementer0, the sole repository Git/index
owner. Only the assigned application paths were staged; no tracking was staged.

Fresh SSH fetch after both commits and push, plus `git ls-remote`, prove remote
master remains the base above and the remote feature head is exactly B. No
rebase or patch-equivalence migration was needed. The worktree and index are
clean. `dev-session worktree capture-comparison` recorded this exact range.

Implementation history inventory: two logical commits, no superseded approaches,
pin streams or temporary compatibility implementation commits. No schema,
migration, seed, notification-template or separate advisory-update changes.
There is no migration lineage to consolidate or externally consumed migration.
The independent reviewer must assess the complete range and give its own history
and no-migration conclusion; this receipt is not review approval or readiness to
merge.

## Package A behavior and coverage

Separate locked content methods allow draft/published original text and existing
node corrections while leaving membership mutation draft-only. Both PUTs expose
optional String `expected_state` with `draft`/`published` include values; it is
checked with the required revision under the parent lock. Publication's unchanged
revision contract remains intact. Conventional HaveAPI choice maps provide the
approved display labels without changing machine values.

Published time changes/clearing are rejected; equal normalized instants are
accepted. Published edited node rows must be resolved, with normal mitigation
time and active-node validation. Node corrections rebuild projections inside the
same transaction; text and draft node edits do not rebuild. Manual rebuilds use
the same parent lock. Locking reads avoid stale child, note, VPS, owner and derived
user data inside repeatable-read outer transactions.

Owned coverage was added to existing model/API specs and a focused
`api/spec/models/security_advisory_concurrency_spec.rb`: immutable publication
identity/history, silent corrections, authorization, timestamp equivalence,
revision/state refusal, draft behavior, resolved node validation, projection
transitions/filter visibility, rollback after partial translation/projection
writes, one winner at a revision, manual rebuild ordering, current data after an
older snapshot, and publication crossing a guarded draft edit. These application
specs have not yet run; final review precedes the longer suites.

Behavior documentation is in `docs/security-advisories.md` and its docs-index
link. The lead directly applied the required writing workflow to the page and
approved new API descriptions/errors and exact English/Czech locale text before
commit. Locale changes are limited to `expected_state` (8 English lines and 9
Czech lines after generated YAML wrapping).

## Completed quick checks

- Ruby syntax passed for both changed models, the resource and all three focused
  spec files.
- API-shell RuboCop passed on all six Ruby files. An initial four test-style
  offenses were corrected; the final affected-file check passed.
- `git diff --check` passed for the final range.
- API locale generation and `vpsadmin:i18n:health` passed; resource RuboCop also
  passed after declaring source choice labels.
- Both A and B commits passed all mandatory pre-commit hooks, including API and
  WebUI i18n health, MigrationSpecs and applicable RuboCop/Nixfmt/PhpCsFixer.
  Commit-message hooks passed with advisory warnings for body lines above 72
  columns; all lines meet the workspace's 80-column rule.
- B's PHP syntax/format, JS syntax, Nixfmt and diff checks were reported by
  implementer1 and accepted by the lead before staging.

The first commit attempt failed only locale normalization after manual text
edits; no commit was created. Regeneration uses source defaults for English, so
the approved human choice labels were declared in the ordinary source metadata,
then normalization/health passed. No obsolete failed-attempt commit remains.

## Tooling evidence and remaining checks

The initial observation watcher completed normally and reported that hook
failure. Two fresh locale-repair utilities returned incomplete without running
the repair: one misread identity variables as files, the next verified identity
but misresolved a procedure path. These are verification-tooling failures, not
application test failures. Parent freshly verified identity and, under the
monitor skill's visible fallback and lead instruction, completed the prescribed
repair and mandatory hooks with bounded output. No utility operation remains.

Complete disposable logs are under:

- `/tmp/2026-11-01-published-advisory-corrections-locale-repair/repair.log`
- `/tmp/2026-11-01-published-advisory-corrections-commits/retry-commit.log`
- `/tmp/2026-11-01-published-advisory-corrections-commits/commit-status.json`

The successful A/B hook batch exited 0 in 131.8 seconds. Initial failure and
utility reports remain in those directories for diagnosis.

Automatic branch CI runs observed at final SHA, without waiting or manual
dispatch:

| Workflow | Run |
| --- | --- |
| i18n health | [41331586018](https://github.com/vpsfreecz/vpsadmin/actions/runs/41331586018) |
| RuboCop | [41331585930](https://github.com/vpsfreecz/vpsadmin/actions/runs/41331585930) |
| Webui PHPUnit | [41331585937](https://github.com/vpsfreecz/vpsadmin/actions/runs/41331585937) |
| API Specs (topic parallel) | [41331585935](https://github.com/vpsfreecz/vpsadmin/actions/runs/41331585935) |
| CI | [41331585931](https://github.com/vpsfreecz/vpsadmin/actions/runs/41331585931) |

They were queued/in progress when inspected; no CI success is claimed. Next:
lead coordinates D's exact-final-head pin and mandatory independent final review,
then the accepted bounded full/core advisory/concurrency specs and advisory
browser scenario. Implementer0 retains responsibility for A follow-up fixes and
repository Git operations until released.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/>
