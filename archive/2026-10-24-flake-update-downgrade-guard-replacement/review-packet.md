# Final review packet

All intended provider and seven consumer changes are committed, worktrees clean,
and quick checks/hooks passed. Review the exact complete eight-repository ranges
in [review/inventory.json](review/inventory.json); each repository's complete
commit list and final diff are saved alongside as `<project>.commits.txt` and
`<project>.diff`. No long local integration/package check has been launched.

## Request and acceptance

User authorized implementation of the proposed solution: automated flake writers
must preserve advanced manual pins instead of replacing them with lagging channel
tips. Shared confctl `--forward-only` mode validates a separate candidate lock
before installation/commit. Apply it across all seven publishing workflows.

Accept equality or proven old-to-new ancestry in the same supported source.
Check the full reachable graph, including chained follows and transitive inputs.
Unknown evidence fails; non-forward candidates reject without publication. Keep
intentional unguarded manual/set behavior. Ordinary non-force pushes must reject
target movement; retries regenerate from a fresh baseline. Preserve existing
metadata freshness warnings, commit conventions, hooks and repository checks.

## Scope and ownership

- Provider: confctl, public update/check CLI, semantic lock resolver and GitHub
  ancestry evidence. Documentation belongs in its input guide/manual.
- Additive `inputs ls --json [pattern]` exposes existing metadata rows with full
  resolved revisions/null for status/IRC subjects; no consumer graph parser.
- Consumers: haveapi, terraform-provider-vpsadmin, vpsadminos, vpsf-status,
  vpsfree-irc-bot, vpsfree-cz-configuration, vpsadminos-org-configuration.
- All seven use the same pinned CI tool without introducing a flake dependency
  cycle. Configuration deployment-tool pins remain unchanged; this avoids
  unrelated historical confctl runtime changes and supersedes the initial
  bootstrap proposal.
- Architect: architect0. Implementers: implementer0 (policy/provider, then
  ordinary consumers), implementer1 (transaction/CLI/docs, then configurations).
- Lead owns plan/state, acceptance and context-dependent user-facing prose.

See [design.md](design.md), [plan.md](plan.md) and [state.md](state.md). Exact
workflow paths and inspected input graphs are in the design. Refresh evidence is
in [inventory-refresh.json](inventory-refresh.json); rollout/source compatibility
and selector fixtures are in [rollout-prerequisites.md](rollout-prerequisites.md).

## Review policy

Risk: high, because this changes a cross-project CLI/input-safety contract and
automated branch publication. No live machine or daemon protocol change.

Select retained reviewer0 after rechecking live same-session roster. Saved
settings: gpt-6.1-sol / xhigh / read_only. Reviewer must remain independent and
read mandatory-change-review plus all four lane references: general,
architecture/repetition, scope/proportionality, risk/compatibility. Do not nest
reviewers and do not override retained settings.

Evaluate whole branch history and final diffs, not only the last commits. Give
explicit conclusions about obsolete history, repeated pin streams and migration
lineage. No database migrations are intended; verify against final inventories.

## Boundaries and residual limits

- Guarantee is ancestry preservation, not detection of an upstream revert commit
  or proof of software compatibility.
- No automatic patch-equivalence, cherry-pick or branch-migration exception.
- No speculative fallback clone on GitHub API errors, no partial graph splicing,
  no PR machinery or new shared action project.
- Atomicity is per updater invocation; prior independent local commits in one
  workflow are not rolled back when a later invocation fails. Final push stops.
- User approved implementation; default-branch integration/deployment are not
  authorized. Feature branches are published for review.

## Attachment checklist

- Exact target/base/head for each repository and complete base-to-head series.
- Final diffs and disposition of superseded/fixup commits.
- Pin-stream inventory: exact selected confctl revision, consolidated updates,
  any supported exact-source consumer boundary and its evidence.
- Migration inventory and merge/release/deployment/external-use provenance.
- Changed project docs and final behavior reconciliation.
- Quick checks, required hooks and relevant failure/remediation evidence.
- Exact worktree paths and published remote heads.

Long verification starts after review and finding reconciliation. Use fresh
Luna/low operation watchers under dev-session-monitor for uncertain checks.

## Exact deliverable and quick-check evidence

The inventory is now complete for all eight repositories. Provider final head:
`7ba361d22a4aac044cb02abf8397800bcf5726bf`; all seven workflows select this exact
external CI tool and retain their runtime inputs. Each final range contains one
commit. The single provider commit bundles policy, transaction and CLI with
supporting tests/docs because these implement one public guarded-update feature;
there is no separately useful deployed policy-only interface. Consumer adoption
commits remain separate per owning repository.

- Provider: [package-a-report.md](package-a-report.md),
  [package-b-report.md](package-b-report.md), [package-b-quick.log](package-b-quick.log).
  143 focused examples plus existing unguarded workflow regression passed;
  RuboCop 25 files clean, man generation and ordinary hooks passed. Provider
  docs-only amendment from d58181a to 7ba361d changed guide/manual publishing
  examples to export `HEAD:flake.lock`; code/tests/inputs are unchanged.
- Five ordinary consumers: [package-c-report.md](package-c-report.md),
  [package-c-branches.json](package-c-branches.json),
  [package-c-provider-refresh.json](package-c-provider-refresh.json),
  [package-c-actions.json](package-c-actions.json). Forty declared-shell
  fixture cases passed, actual locks passed graph equality, Bash syntax,
  Actionlint/ShellCheck and required hooks passed. All final remote heads
  independently observed by owner. Exact initial published ranges and
  substantive committed-blob correction are preserved as provenance, not
  claimed patch equivalence; see package-c-branches-initial.json and range-diff.
- Both configurations: final heads f5bf3f026210d30c0b9b219aac47ff6490e4cddc and
  30ea016491f78d88037508e3a7e9c9a20d50511b, bases in inventory. Twenty dynamic
  workflow cases passed including hook failure and committed/worktree lock
  drift; YAML/Bash syntax and ordinary hooks passed. Only daily-update.yml
  changes in each. [package-d-workflow-check.py](package-d-workflow-check.py)
  contains the evidence harness; [package-d-report.md](package-d-report.md),
  [package-d-branches.json](package-d-branches.json) and
  [package-d-quick.log](package-d-quick.log) contain final source publication
  proof, clean-state/hook receipts and complete history conclusions.

The final workflows validate the committed `HEAD:flake.lock` blob against their
original baseline immediately before ordinary non-force push. Configuration
steps preserve their old tools-shell hook environment while explicitly invoking
the newly pinned tool inside it. The full old-shell/IRC packaged-runtime proof
is deliberately post-review; inherited Ruby/Bundler settings caused a C harness
subprocess issue, not a demonstrated package failure. Provider wrapper overrides
Ruby paths; supported invocation still needs artifact verification.

No migrations, schema/format transitions, deployments, releases or integrated
consumer boundaries exist in these ranges. No obsolete implementation, repeated
provider-pin update or transitional migration commit is intentionally retained.
Independently verify these history and migration conclusions. Preserve supported
manual/set behavior and source/error limits; do not require speculative provider
fallbacks or semantic patch-equivalence exceptions.

Long checks prepared only: [package-c-live-checks.md](package-c-live-checks.md)
and [package-d-live-checks.md](package-d-live-checks.md). Automatic push CI is
separate evidence; do not interpret its success as final-review substitution.
