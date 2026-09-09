---
lifecycle: active
---

# IP accounting audit

## Status

Implementation is complete, committed and locally verified. All required review lanes are complete and findings are reconciled.
No production execution, reconciliation, push, merge or deployment was requested
or performed. Keep the initiative active and worktrees available for user review.

## Repositories

- vpsfree-maintenance-tasks: branch `2026-09-09-ip-accounting-review`, worktree
  `worktrees/2026-09-09-ip-accounting-review/vpsfree-maintenance-tasks`.
  Base: `6eea682ede8d8e2634b2d41e5b11cf0f02231bc6`.
  Final head: `0e4531b2a9839152c74a970c472bf65a3cc3c0c9`.
- vpsadmin: unchanged reference branch `2026-09-09-ip-accounting-review`,
  worktree `worktrees/2026-09-09-ip-accounting-review/vpsadmin`,
  head `19971f039771500d5d0304610f91fe6f4af5fed3`.
- Both project worktrees have ordinary clean status. The maintenance repository
  and workspace declare no hook framework. No vpsAdmin commit was made.

## Implementation

New task `2026-09-09-check-ip-accounting/` contains executable Ruby script,
README and focused database-backed specs. It reports IP inventory, authoritative
resource usage, stored limits and assigned package totals per user/environment/
IP resource. It includes evidence rows and unresolved charging environments.
It reads a MariaDB-enforced read-only repeatable-read transaction and publishes
one private JSON file after success, refusing overwrite. Amounts are decimal
strings preserving the decimal(40,0) schema. Exit codes: 0 clean, 2 findings,
1 failure. No resource allocation or repair methods are called.

## Verification

- Read current repository instructions, workspace writing/handoff/review skills,
  existing IP repair tasks, and relevant vpsAdmin models. Both project origins
  fetched before creating isolated worktrees through dev-session.
- Initial plan/state/portal committed to shared workspace master as `fd85b9d`.
- Seeded ignored API Gemfile.lock from packages/api/Gemfile.lock before the Nix
  API shell. Used packaged JSON 2.21.2; no tracked dependency files changed.
- From reference vpsAdmin root, command:
  `VPSADMIN_API_SPEC_HELPER="$PWD/api/spec/spec_helper.rb" nix develop .#api -c bundle exec rspec <absolute-task-path>/check_ip_accounting_spec.rb`.
  Initial 16 examples passed (seed 35709); after remediation, all 16 passed
  again (seed 65333, 13.9 seconds excluding startup).
- `verify_runtime.rb` passed against the disposable API test database: clean,
  findings and failure statuses; JSON parsing; overwrite rejection; actual
  snapshot method rejected an injected database write and rolled back cleanly.
- `benchmark.rb`: 1,000 synthetic users with 6 resource limits, 1 package,
  1 confirmed usage and 1 owned IPv6 allocation each. Scan of 1,004 total users
  returned no findings in 43.259 seconds, with 14,046 non-schema SQL statements.
  This measures the corrected provider-used implementation, not production load.
- Script syntax, help, git diff --check and script RuboCop with the reference
  root .rubocop.yml passed. No long VM/integration tests required. Maintenance
  repository has no GitHub workflows; no push/CI run was needed.

## Review

Medium risk: bounded operational reporting with a new JSON output contract.
Required lanes: general, architecture, scope, risk. Every reviewer uses fresh
context, gpt-5.6-sol, xhigh, with no nested delegation. Reviewed original commit
`9ec505df9b67bc19f7983c1bb5c34ad160eddd05`; direct fixes folded into final head.

General and scope: no findings. Architecture: three Important findings recorded
and reconciled in review-resolution.md. Provider-use duplication fixed;
orphan discovery explicitly excluded from this user-account audit; per-user
query cost accepted after the synthetic benchmark. No schema or input-scope
expansion, so no reviewer rerun required for these direct fixes/clarifications.
Risk review corroborated the accepted query-cost finding. The runbook now
specifies a quiet period and Ctrl+C to release the snapshot if database load
becomes excessive. Its Advisory finding about post-publication errors was
resolved by documenting that summary/cleanup failure can return 1 while the
complete file remains. No new runtime behavior was introduced. All four lane
reports and the reconciliation are retained with the review packet.

## Setup lessons and cleanup

- vpsAdmin post-checkout hook rejected a changed Overcommit configuration
  signature after worktree creation. The worktree was present/clean, and
  repeating dev-session add registered it. Existing lesson:
  notes/cross-project/2026-06-07-overcommit-worktree-add.md.
- API dev shell changes into api/ when started from the repository root; use
  absolute external spec paths. Referring to the API flake from the workspace
  root instead looked for a workspace Gemfile. Both corrected runs passed.
  Durable lesson: notes/vpsadmin/2026-09-09-maintenance-spec-path.md.
- Optional lint config is the reference root .rubocop.yml. Autocorrect fixed
  help-block layout; remaining style choices were fixed manually. IP size is a
  numeric column, not a collection length.
- Removed the workspace-root Bundler cache from the failed wrong-directory
  invocation with non-force removal. Reference API dependencies remain ignored
  in its worktree. Test DB auto-start cleanup stops and prunes each disposable
  database at process exit. All task-owned test/lint processes have exited.

## Handoff

Committed local branch is ready for user review and later integration.
Production timing is unmeasured; follow the quiet-period/interrupt guidance.
Snapshots can include mid-chain state, so admins must review and rerun findings
before reconciliation.
Do not archive while user review/integration remains pending.

Portal is deployed and responds with its expected authentication challenge:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-09-ip-accounting-review/
