# Final review packet — pending final heads

Do not begin review until lead assigns the completed packet with exact heads.

## Request and acceptance

Implement hourly summary notifications in vpsfree-irc-bot and update the bot's
package revision/hash and settings in vpsfree-cz-configuration. User explicitly
excluded deployment. No service restart, activation, default-branch integration
or PR is authorized. Per-poll summaries were rejected because gradual advisory
creation still spams IRC. Accepted design is design.md; plan/state in this folder.

Modes individual/summary/off, omitted individual; positive integer interval in
seconds, default and site value 3600. Keep minute API polling, silent bootstrap
and existing state format. Summary counts distinct new and updated advisory IDs
across polls, with new winning across the whole interval. Link existing WebUI
advisory list. No immediate/size-triggered/empty/catch-up digests, and arrivals do
not postpone deadlines. Monotonic deadline at least full interval after due
handling. Off consumes without accumulating; memory-only pending counts lost on
restart, no durable notification guarantee. Existing eligibility/API unchanged.

## Repositories and owners

- Bot: worktrees/2026-10-19-security-advisory-notifications/vpsfree-irc-bot,
  implementer0. Owns modes/aggregation, specs/integration coverage and docs.
- Configuration: worktrees/2026-10-19-security-advisory-notifications/vpsfree-cz-configuration,
  implementer1. Owns site summary/3600 and fetchFromGitHub source revision/hash.
- API/HaveAPI only investigated as reference; unchanged dependencies.

## Risk and review lanes

Overall high per risk taxonomy because configuration and cross-project version
compatibility/rollback are involved; no security authorization/schema changes.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Read mandatory-change-review/SKILL.md and all four lane references. Lead read all.
Retained reviewer0: gpt-6.1-sol, xhigh, read_only; no overrides/fallback. Reviewer
must independently assess complete commit series, final diff, tests, contracts,
consumer pins and documentation. Require explicit whole-branch history and
migration conclusions and repeated pin-stream disposition, not only tree review.

## Boundaries and residual behavior

No persisted digest queue, delivery repair, new API, WebUI redesign, generalized
scheduler, severity policy or unrelated dependency updates. Startup/downtime
notifications remain best effort; restart deliberately discards pending counts.
An old bot ignores the mode and resumes individual output. Configuration must
select the compatible bot head together with the new settings; old state remains
readable on rollback. No database migrations expected; final inventory follows.

## Evidence to complete before assignment

- Exact bases/heads, complete commits, final diff artifacts and clean worktrees.
- Migration inventory/provenance and obsolete history conclusions.
- Pin update streams, final selected revision/hash, consolidation disposition.
- Commit split and rationale, docs paths and lead writing inspection.
- Quick commands/results including hooks; long integration/build remain unrun.

## Bot final inventory

Base `e9c60b0b95d3cc0dad6f012d8127c2bc078cfa7d`, feature head
`2756ee653fb844a611a9f2083ca8890a1f70f72d`, published over SSH. Complete series
has one commit: `security_advisories: add interval summaries and silent mode`.
See `bot-series.txt` and `bot-final.diff`. Worktree clean. No obsolete history,
follow-up commits, dependency update streams or migrations. No migrations have
been merged/released/deployed/externally consumed because none were introduced.
One logical behavior commit bundles its own documentation, unit and integration
coverage; no separate unrelated behavior. Changes: README/sample config,
security_advisories implementation, 34 focused examples, targeted VM scenario
retaining individual coverage and adding gradual summary arrivals.

Quick batch exit 0: `nix develop -c bash -c 'bundle exec rspec && bundle exec
rubocop && nixfmt --check tests/suite/vpsadmin-events.nix'`: 146 examples, zero
failures; 63 files no lint offenses; Nixfmt clean. Nix expression parse and
extracted Ruby testScript syntax checks pass. Commit hooks pass; push hooks pass
under the same Nix environment. Ambient-shell push had a signature mismatch;
Nix-environment retry succeeded without bypass or source changes. Lead directly
applied required writing skill to README/sample and message/validation prose.
No changes requested. Long local integration has not run.

## Configuration final inventory

Base `91639dec2c78721b3d8765de10dc65e0c66d59db`, head
`aa933ecf78325326c1ccc097944f2ce53b8423f8`, published over SSH. Complete series:

1. `fcdb2e7c58ed1d9f665b800d691f060c08312b8d`
   `cluster: use hourly security advisory summaries on Libera` — site policy.
2. `aa933ecf78325326c1ccc097944f2ce53b8423f8`
   `packages: pin bot with hourly advisory summaries` — final source pin/hash.

See `config-series.txt`, `config-final.diff`, `config-package-report.md`.
Worktree clean. Final diff is two files, +4/-2. No obsolete history, follow-up
fixes or migrations; no migration versions have external use. Exactly one bot
package update stream, one final pin; no consolidation needed. There are no
flake channel/lock/gemset updates or other dependencies. Separate policy and
package commits follow repository conventions and keep a mechanical pin apart
from functional site settings. No deployment or supported interim state exists.

Selected bot rev `2756ee653fb844a611a9f2083ca8890a1f70f72d`, unpacked hash
`sha256-hQl4jf4oLNgU5XlBV10W6v+/bNTPzV2hUouMo6ulMmQ=`. Source prefetch passed.
Package and settings syntax/nixfmt/whitespace checks and mandatory hooks passed.
No applicable push CI exists in this configuration repository. No configuration
prose added: bot README/sample own supported behavior; site changes need only
two settings and a pin. Operational/session evidence stays in session records.

Owning provider is bot SecurityAdvisories plugin; the site's Libera instance is
the discovered consumer, wired through the existing arbitrary-settings Nix
module. Optional private settings load afterward and may override configuration;
no private contents inspected or altered. The config-eval.nix harness mirrors
pinned confctl module assembly for only int.vpsfbot, asserting generated JSON
advisory settings/channel and ExecStart config reference, and outputs exact
package/source identity. Fresh Luna/low watcher is running this scoped evaluation
before final review; result follows. No full container build or local VM test
has started.

## Final quick-check gate complete

Corrected scoped configuration evaluation passed exit 0 in ~31 seconds at exact
configuration head aa933ecf, clean worktree. See config-eval.json/log/exit.
Asserts and output verify summary/3600/#vpsfree, generated JSON and ExecStart
config path, selected package and exact source pin/hash. First harness attempt
failed because lib.hasInfix fed derivation string context into regex; the owning
implementer fixed only the comparison needle with unsafeDiscardStringContext.
No application changes or new contracts. Prior failure retained in
config-eval-first-failure.log/exit. This was a harness error, not hidden by retry.

Both intended deliverables are now committed, published, clean and quick checked.
All complete series and final diffs captured. No local long tests/builds started.
Final review is authorized now. Require explicit history/no-migrations and pin
stream conclusions for BOTH repositories. Reviewer report should be a session
artifact and report_to_lead; read-only source, no nested review agents.

## Narrow remediation update

Original final review completed, persisted final-review.md. One Important local
bootstrap retry defect and one Advisory YAML off-quoting note were accepted.
Reviewer explicitly permits direct step9 narrow-fix inspection without a full
rerun. Lead inspected actual old-to-new diff and 38-focused/150-full passing
spec/lint/format evidence, plus selected Ruby YAML parse. Corrected bot head
`49a8ff8086b7b325f9f1a8f4825619f8e03245ce` is published, clean; complete history
still sole feature commit above e9c60b0. Final five-file diff +757/-25. No new
public boundary, migrations or dependencies. Superseded commit consolidated.
See bot-review-remediation.diff and bot-bootstrap-recovery.md for exact evidence.
Configuration owner is refreshing the same sole package commit and will inspect
new origin advancement before final patch-equivalent rebase/inventory/evaluation.

Current exact-head automatic CI: RSpec 39317498639; Integration 39317498503.
Old-head queued Integration 39315420422 cancelled and confirmed; old RSpec
39315420448 completed success and retained. No current-head runs cancelled,
manual dispatch or local long checks started.
