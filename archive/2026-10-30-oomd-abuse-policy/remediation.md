# Review remediation and consolidated source

Owner: implementer0. The original independent report remains in [review.md](review.md).
The lead owns the required focused architecture/risk follow-up; this record does
not claim independent clearance. No source changes, publication, deployment or
long integration runs follow the final heads below.

## Exact ranges and history

Repository: `git@github.com:vpsfreecz/vpsadmin.git`, worktree
`worktrees/2026-10-30-oomd-abuse-policy/vpsadmin`, branch
`2026-10-30-oomd-abuse-policy`.

- Original reviewed base: `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`.
- Original backend: `a9e5fe4ff1c7071672c76e7627ff870008eb99a4`.
- Original reviewed UI/head: `51297de1a05fee60aaba8a31e443abf95675396c`.
- Tested remediation before consolidation: `a916b2a8193236850d4704eef254ae1fe9526502`.
- Final backend: `dbfd2bbf060237189797aafa7db359ea0edbd797`.
- Final UI/head: `5a59ead40a283f74d211c7afde4d4d69aab28785`.

Original heads remain reachable through
`refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-original`; the pre-consolidation
remediation is retained by the corresponding
`vpsadmin-remediation-before-consolidation` ref. No branch/ref was deleted.

The final tree equals the tested pre-consolidation remediation exactly:
`git diff --exit-code a916b2a8193236850d4704eef254ae1fe9526502 HEAD` passed.
The complete old/new base-to-head range comparison is
[remediation-range-diff.txt](remediation-range-diff.txt). Backend fixes and their
regressions are folded into the owning backend commit; the legacy patch remains
unchanged in its rebased child. No fixup, obsolete approach, transitional
migration or repeated dependency/input stream remains in the final series.
The portal comparison was refreshed for the final exact head.

Tracked worktree and index are clean. Only the existing disposable
`webui/.phpunit.cache/` is untracked. Rebase, all commits, hook commands and test
commands have exited; no uncertain operation is left running.

## R1: ordinary notifications cannot bypass enforcement

`VpsOomPolicy.process!` prepares stop actions before ordinary notification work.
Each ordinary preparation and acknowledgment runs in its own savepoint. A real
preparation error rolls back only that notification, logs the error and leaves
it pending for retry, while the stop decision and actual stop chain remain.

`IncidentReport::New` permits a legitimate empty chain: ordinary mail disabled
by a member or suppressed for an inactive recipient need not create a mail
transaction. Its only runtime callers are the OOM policy and IncidentReport API
Create. Create now follows the existing synchronous-success convention with a
nullable chain ID; no new endpoint, parameter or response field was added.

The nullable internal `incident_reports.oom_report_processed_at` acknowledges a
prepared-or-intentionally-suppressed notification. It is not SMTP delivery
proof. Null remains pending, including after actual preparation failure. A
successful queue retains its real chain ID; intentional suppression has an
acknowledgment and no chain. No sentinel identity is used. Acknowledgment and
chain linkage share the savepoint, preventing partial preparation from escaping
and preventing an acknowledged event from being replayed later.

Tests use the real member preference row and real rendering/chain preparation.
They prove a qualifying stop still queues with ordinary mail disabled; enabling
mail later does not replay that acknowledged event. Another test invokes real
New preparation, raises after its chain is created, verifies its mail/chain are
rolled back while the stop remains, then verifies one stable ordinary chain on
retry. The actual API Create path succeeds without an action-state receipt when
ordinary mail is disabled. Existing New chain tests cover its normal actions.

## R2: pending transfer summaries

An unconfirmed Chown is nil, rather than false. Real queued, rollbacking, failed,
fatal and resolved chain rows produce valid summaries. A successful done chain
uses the Chown transaction finish as a virtual epoch before scheduler
persistence; an unsuccessful transaction does not reset the epoch. No transfer
mechanism was redesigned.

## R3: settings changes remain synchronous and audited

VPS Update rejects a supplied OOM settings field mixed with any other mutation
before API effects. The direct Update chain applies the same boundary before
locks or changes. OOM-only writes keep the existing synchronous acknowledgment,
VPS PaperTrail update and serialized final-pair validation. No deferred
confirmation framework was added. Both existing UIs already send isolated
settings requests. The exact lead-approved English and Czech validation help is
included; the owning feature document describes the constraint.

Actual API regressions cover mixed hostname, CPU and lifetime mutations with
unchanged VPS state, no prepared chains/transactions and no audit changes.
An isolated update creates its audit record; a later conflicting global default
is rejected. Direct-chain mixed writes are rejected, and an ordinary hostname
update retains its existing asynchronous behavior.

## Final schema and verification

Migration `20261030180000_add_vps_oom_policy` remains the single direct additive
migration from its immediate predecessor. Its final version adds the nullable
ordinary-notification acknowledgment; legacy incident rows retain null, and
rollback removes that feature column. It was never merged, released, deployed
or consumed by an external persistent environment. Only isolated disposable
local databases have loaded the earlier or final draft. No guards or separate
transitional migration were added. The committed core schema was dumped from a
core-only disposable database.

Focused command, from the repository's API Nix shell:

```sh
VPSADMIN_PLUGINS=none nix develop .#api -c /tmp/oom-review-checks.sh
```

The script ran these exact commands in that shell, using separate RSpec
processes for application and migration checks:

```sh
bundle exec rspec spec/models/vps_oom_policy_spec.rb \
  spec/models/vps_oom_summary_spec.rb spec/api/resources/vps_oom_policy_spec.rb \
  spec/models/transaction_chains/incident_report/new_spec.rb \
  spec/api/resources/incident_report_spec.rb:407
bundle exec rspec --options /dev/null --require ./spec/migration_helper.rb \
  spec/migrations/20261030180000_add_vps_oom_policy_spec.rb
```

These are the policy, summary, OOM VPS API, IncidentReport::New and actual
IncidentReport API Create groups, followed by the final migration. Result: **45 application examples, 0 failures**, 3 minutes 33.1 seconds
plus 13.63 seconds load; **2 migration examples, 0 failures**, 5.04 seconds plus
0.85 seconds load; overall exit 0. See [remediation-checks.log](remediation-checks.log).
The previously successful unrelated examples from the 205-example batch remain
valid; that broad batch was not repeated.

Final scoped lint: 12 Ruby files, no offenses. Nix formatting and parsing passed,
and the exact added transfer assertion fragment passed Ruby syntax checking.
See `remediation-final-lint.log` and `remediation-transfer-syntax.log`.
The fixup commit and both final commit groups passed normal pre-commit and
commit-message hooks, including API/WebUI locale health, migration checks,
RuboCop and Nix formatting. A first ambient-shell pre-rebase invocation was
refused before changes by Overcommit signature verification; running it in the
declared Nix shell resolved the environment difference without bypassing hooks.
See `remediation-commit.log` and `remediation-rebase-nix.log`.

## Prepared physical verification

The existing `alerts-oom-abuse-policy` scenario now adds successful ownership
transfer of the same disposable VPS after stop, mail retry and manual start.
It uses the existing fixture-user, update and chain-wait helpers. It checks the
actual successful Chown finish against the new epoch, reset counts and warning,
retained stop cooldown, new-member incident-history scope, preserved admin audit
and the exact data sentinel after transfer. No topology, transport, helper
framework, induced resource abuse or physical rollback campaign was added.

The scenario and `webui#oom-policy` remain **unrun** pending corrected-source
clearance. Physical behavior and transfer data integrity are not yet proven.
No UI/template source beyond the accepted packages changed in this remediation.

Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/>.
