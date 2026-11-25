# Backend/API delivery

Current corrected source is backend `dbfd2bbf060237189797aafa7db359ea0edbd797`
and final head `5a59ead40a283f74d211c7afde4d4d69aab28785`; see
[remediation.md](remediation.md) for fixes, the retained original range, focused
45/2 verification and the required architecture/risk follow-up. The receipt
below preserves the original delivery and its evidence before those findings.

Owner: implementer0. Worktree:
`worktrees/2026-10-30-oomd-abuse-policy/vpsadmin`, branch
`2026-10-30-oomd-abuse-policy`. Base and freshly fetched `origin/master`:
`ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`.

Backend source, schema, focused tests, technical documentation and shared
browser/CI registration are committed. Independent final review remains pending;
no merge, deployment, push or long integration test has run. Implementer0 retains
exclusive vpsAdmin Git ownership. The exact final series is:

- `a9e5fe4ff1c7071672c76e7627ff870008eb99a4`: backend/API/support, 38 paths.
- `51297de1a05fee60aaba8a31e443abf95675396c`: accepted legacy UI, nine paths.

The final branch has no obsolete or fixup commits and one final-schema migration.
Independent review must confirm the whole-branch and migration conclusion.
Tracked worktree/index are clean; only the excluded `webui/.phpunit.cache/`
remains untracked. No source is uncommitted.

## Shape and documentation

One additive migration and action model; a conventional evaluator and batched
summary; existing supervisor, incident task, VPS Update/Stop and mail chains.
No node protocol or transport change. Default mode is observe. Existing VPS
read/update routes expose the fixed flat contract. Stop and mail have separate
durable progress; physical uncertainty is never automatically replayed.
Ownership success uses Chown completion, rollback preserves accounting, and
cooldown survives transfer. Both API metadata languages and fallback English
mail follow lead-approved prose. Current mail settings govern future claims;
counts retain the decision snapshot. The stopped mail describes autostart as
an effect of that stop, since normal Start re-enables it.

The owning project explains behavior and compatibility in
`docs/oom-abuse-policy.md`, linked from `docs/README.md`. Individual rollout
state remains here. Raw logs are disposable local evidence.

## Verification

- API Nix shell: Ruby 3.4.9 and dependencies satisfied; root hooks installed and
  signatures verified. No bypass.
- API i18n health: exit 0. Template checker: 58 templates/186 files, exit 0.
- CI selection unit checks: 16 runs/55 assertions, exit 0. Nix parse/format and
  whitespace checks passed. New specs fit existing foundation/vps topic globs;
  no API spec partition change is needed.
- Ruby lint: no offenses. Final staged backend covers 38 paths. A final lint
  invocation with an empty unstaged list scanned the repository's 2,202 Ruby
  files rather than only owned files; it reported no offenses and changed no
  paths. The temporary launcher was corrected to use the HEAD diff and reject
  an empty list.
- Stopped-mail rendering after a manual start/exemption/limit change:
  `spec/models/transaction_chains/vps/oom_policy_mail_spec.rb`: 1 example,
  0 failures (7.87 seconds, 14.84 seconds load), exit 0.
- Full app/related batch: 205 examples, 201 passed and four new fixture
  failures, 17 minutes 22 seconds plus 13.4 seconds load, exit 1. Exact failure
  traces were retained; the successful existing groups were reused. The four
  failures came from two base chain fixtures missing required STI type, an
  association cached across raw fixture deletion, and cleanup hitting the
  pre-existing obsolete VpsMount association. Only fixture code changed.
- Affected policy/concurrency rerun: 16 examples, 0 failures (22.92 seconds plus
  12.96 seconds load). Separate migration process: 2 examples, 0 failures
  (5.31 seconds plus 0.92 seconds load). Overall command exit 0.
- Scoped final Ruby check: 24 files, no offenses, exit 0.
- Both commits passed all ordinary pre-commit and commit-message hooks.
  Commit-message hooks emitted their advisory 72-column warnings; every line
  complies with the repository/workspace 80-column requirement.

The broad command was `/tmp/oom-final-checks.sh` under
`VPSADMIN_PLUGINS=none nix develop .#api`. It covered new policy/concurrency,
summary and API specs, existing VpsEvents, incident task/resource and VPS
read/write groups. The final command `/tmp/oom-affected-checks.sh` reran the
corrected model/concurrency groups and the migration in a separate process.
Evidence is in `backend-regressions.log`, `backend-affected-checks.log`,
`backend-render-check.log`, `backend-rubocop-affected.log`, the i18n/selector logs,
and both commit logs. Legacy evidence belongs in `legacy-ui-delivery.md`.

Earlier failures were diagnosed before reruns. Migration specs switch to a
minimal schema/database, so they must not share a process with app specs.
Transaction status fixtures must use the daemon's direct updates because the
model's save callback resets status. Required associations cannot be cleared
with association `delete_all`. A genuine SQL bug compared COALESCE fallback
thresholds as strings; explicit numeric casts fix it and mode-switch coverage
exercises it. The original watcher launcher returned exit 127 before testing because its
timing wrapper was unavailable; the fresh run uses the exact command. The watcher later failed
to collect its result, so minimal parent monitoring resumed the same running
process and logs. No duplicate run was launched. The first backend commit attempt passed every
hook except WebUI locale health: Overcommit hid unstaged tracked UI source and
catalogs but left the new untracked form visible. Temporarily moving only that
owned untracked form out allowed the backend snapshot to be checked normally.
An EXIT trap restored it and verified matching SHA256 before UI staging. The
second backend attempt and the complete UI commit passed without bypassing hooks.

## Migration lineage and prepared long checks

Migration `20261030180000_add_vps_oom_policy` directly describes the final
additive schema. It was created in this session and has not been merged,
released, deployed or consumed by an external persistent environment. Only
isolated disposable local test databases were used. There are no transitional
or superseded migrations. Normal source migration guards were not added.

After complete committed source review, run through a fresh watcher:

```sh
./test-runner.sh test alerts-oom-abuse-policy
./test-runner.sh test 'webui#oom-policy'
```

The first authored scenario publishes daemon-format messages through RabbitMQ,
checks deduplication, a real node stop and autostart effect, SMTP failure and
independent retry, then manual start, retained data and a new cooldown incident.
It does not induce actual resource abuse. The second is implementer1's
administrator/member browser scenario. Stop on the first failed scenario and
diagnose its concrete evidence; stop an unexpected local kernel build under the
workspace verification rule. Silence or elapsed time alone is not failure.
Physical ownership transfer with this feature is a remaining long-check gap;
local epoch-success/rollback and existing transfer preparation tests do not
prove its data integrity on a real node. Do not claim deployment or usability
from these local checks.

Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/>.
