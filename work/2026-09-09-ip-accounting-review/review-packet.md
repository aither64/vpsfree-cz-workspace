# IP accounting audit review packet

## Outcome and acceptance

User requests a vpsfree-maintenance-tasks script to identify users holding more
IP addresses than cluster resources/packages allow, and output a parseable file
for later admin reconciliation. Accept a read-only JSON report containing user
IDs/logins, per-environment/resource amounts, overages, supporting records and
unresolved charging environments. Script must not repair anything.

## Locations and commits

Workspace: /home/aither/workspace/ai/vpsfree.cz
Initiative: work/2026-09-09-ip-accounting-review/{plan,state}.md
Implementation: worktrees/2026-09-09-ip-accounting-review/vpsfree-maintenance-tasks
Original reviewed commit: 9ec505df9b67bc19f7983c1bb5c34ad160eddd05
against base 6eea682ede8d8e2634b2d41e5b11cf0f02231bc6. Final direct
remediations are recorded in state.md and review-resolution.md. Only new directory 2026-09-09-check-ip-accounting changes.
Reference: worktrees/2026-09-09-ip-accounting-review/vpsadmin at 19971f039,
unchanged. No companion API branch or dependency changes.

## Commit split

One functional commit containing the standalone audit, README and focused specs.
The docs and tests describe/validate exactly this one new behavior and are kept
with it. No shared framework, existing task edits or generated files changed.

## Scope decisions and ownership

- IP ownership takes precedence; userless assigned IPs belong to the VPS owner.
  Owned reservations count. IP size is allocation units, not row counts or IPv6
  host expansion. Charged environment is authoritative. Unresolved environment
  IPs appear separately and do not enter guessed environment totals.
- User default scope excludes hard-deleted accounts; includes suspended and
  soft-deleted accounts. VPS joins follow the existing model default scope.
- Packages determine UCR.value; compare independently, never add twice.
- Match UCR.used confirmed/enabled filtering. Show pending/disabled evidence.
- Report both overages and usage/limit drift, including evidence IDs. No repairs,
  quota adjustments, production runs, deployment, main-branch merge, credentials,
  email, API/UI changes, or broad inventory-integrity framework.
- This dated maintenance script owns a new schema_version 1 JSON report. Its
  consumer is a human admin / future reconciliation tooling; no existing parser
  or downstream pinned dependency exists. It consumes current vpsAdmin models.
  Older accounting references: 2022-01-21-fix-user-ip-address-allocation and
  2026-09-07-fix-ip-charged-environments; shared provider semantics are in
  api/models/{user,user_cluster_resource,ip_address,network}.rb.

## Verification

- 16 database-backed examples passed in the reference vpsAdmin API Nix shell
  with its disposable MariaDB. Command (from reference root):
  VPSADMIN_API_SPEC_HELPER="$PWD/api/spec/spec_helper.rb" nix develop .#api -c
  bundle exec rspec <absolute-task-path>/check_ip_accounting_spec.rb
- Syntax and git diff --check passed.
- Optional RuboCop with reference root .rubocop.yml passed (no maintenance
  repository hook framework declared; no hooks bypassed).
- work/.../verify_runtime.rb passed: CLI exit 0/2/1, complete JSON/no overwrite,
  actual snapshot rejects injected writes at MariaDB layer, rollback closes
  transaction. Initial spec path and Nix working-dir errors are explained in
  state and durable note; final correct runs passed.
- No long integration tests needed or started. No production credentials used.

## Risk and compatibility

Medium: bounded reversible read-only operational script; correctness matters to
later admin reconciliation and there is a new report format consuming vpsAdmin
models. No state/schema writes, breaking APIs, node changes or coordinated
upgrade. Selected review effort is xhigh for every lane, model gpt-5.6-sol.
Lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility (operational tool and new report contract).

Snapshot uses MariaDB read-only plus ActiveRecord repeatable-read transaction.
Active transaction chains can be captured midway: docs require reviewing and
rerunning findings before corrections. Missing/broken references encountered while auditing existing users either
produce explicit findings or fail before publishing a report. Orphan ownership
and assignment chains outside those users are not scanned (see review-resolution.md). No attempts to validate
every possible historic corruption. JSON decimal strings preserve decimal(40,0)
precision; output is atomically linked from a 0600 temporary file and refuses
overwrite. Supported execution is the API host's vpsadmin-api-ruby wrapper.

## Reviewer task

Read the mandatory-change-review skill and your lane reference. Review committed
changes directly, do not spawn subagents. Write findings with severity and exact
file/line references to work/2026-09-09-ip-accounting-review/review-LANE.md.
