# PR #43 review packet

User request: review https://github.com/vpsfreecz/vpsadmin/pull/43.
Review only: do not edit project code, post GitHub comments, push, or merge.
Report concrete introduced defects, exact locations, reproducible triggers,
and consequences. Explicitly distinguish residual test gaps from findings.

## Scope and acceptance

The PR adds inclusive created_from/created_to datetime filters for global
payment history, preserves normal-user scoping, aligns from_id pagination
with created_at DESC/id DESC even for out-of-order IDs, adds a reversible
created_at index, and exposes localized API OPTIONS metadata.

Workspace: /home/aither/workspace/ai/vpsfree.cz
Initiative: work/2026-09-09-vpsadmin-pr-43
Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-vpsadmin-pr-43/vpsadmin
Branch: 2026-09-09-vpsadmin-pr-43
Base: 3a64784708faef5e9f4f093255954b14e396904c
Head: 44cfb4357751d9c925e1a74e7bf6a3842ebd3cd1

Read initiative plan.md/state.md and repository AGENTS.md. One commit:
api: filter user payments by creation period. Six files contain API query,
localized descriptions, focused specs, and index migration. Index, tests,
and documentation support the same accounting-history behavior; no generated
or dependency changes are bundled. No implementation changes will be made
in this review session. No long integration tests planned.

## Verification completed

- git diff HEAD^ HEAD --check passed.
- Ruby syntax passed on all four changed Ruby files.
- API-shell RuboCop: four files inspected, no offenses.
- GitHub PR checks: 63 successful, none unsuccessful at inspection time.
- Focused payment and migration RSpec runs will be run by the coordinator.
  Do not concurrently start Nix/Bundler/database jobs in this worktree.

## Risk and compatibility

High risk classification because of API pagination semantics, tenant-scoped
records and database schema change; all lanes use gpt-5.6-sol/xhigh.
Lanes: general, architecture, scope, risk.
New inputs are optional. An index should not change stored payment data and
can be rolled back independently. Old API code can use indexed/unindexed
schema. PR calls for usual migration window, API before dependent WebUI Next
finance feature; no companion frontend revision was supplied. No node,
protocol, file format or Nix configuration changes.

## Owner and observed consumers

Owning API: plugins/payments/api/resources/user_payment.rb.
Core framework: HaveAPI 0.29.8 in packages/api/gemset.nix and local installed
api/.gems/ruby/3.4.0/gems/haveapi-0.29.8. Pagination adapter under
lib/haveapi/model_adapters/active_record.rb, datetime parsing in framework.
Existing WebUI consumers: webui/forms/users.forms.php (payment log and
user_payment_history) with user/accounted_by filters, from_id and limit.
WebUI pins haveapi/client 0.29.6 in composer.json/composer.lock.
Additional generated clients can be inspected from canonical bare repositories
if relevant; do not change other initiatives or their worktrees.

Use the assigned lane reference and produce the review directly. Do not spawn
nested agents. Report with skill severities Blocking/Important/Advisory,
plus P1/P2 equivalents for concrete bugs if useful. Do not manufacture style
findings or require unrelated refactors. Write your lane result in the
initiative directory as review-<lane>.md and send a concise result to parent.
