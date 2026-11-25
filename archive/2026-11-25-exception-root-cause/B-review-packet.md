# Package B review evidence

Status: implementation/export accepted by lead; independent final review found
no findings and the reviewed feature head is published. Client assessment and
push-triggered CI evidence remain separate obligations. This packet does not
declare final readiness.

## Scope and source

Fix the reported incident-report list exception through the narrow implementation
and verification brief in [design.md](design.md). Preserve filters, ownership and
owner-epoch visibility, notice output, includes and pagination. No audit, query
loading redesign or cursor change is included.

- Repository: `vpsfreecz/vpsadmin`, remote `git@github.com:vpsfreecz/vpsadmin.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-exception-root-cause/vpsadmin`.
- Branch: `2026-11-25-exception-root-cause`; target: `master`.
- Base: `81e930b25fa3252d7e849aff4819e663cec37b07`.
- Head: `da7724abdc080e59820cc4f0812ce1a41b3fc5df`.
- Owned files: `api/lib/vpsadmin/api/resources/incident_report.rb` and
  `api/spec/api/resources/incident_report_spec.rb`.

The correction qualifies descending `detected_at` ordering through ActiveRecord's
hash syntax. The request regression uses the real MariaDB-backed endpoint with
an IP filter, explicit `user,vps,ip_address_assignment` includes and limit 25.
Notice timestamps are ordered opposite to the nested trigger timestamps. Existing
member filtering coverage now also exercises includes and asserts exact order,
including an empty response for another owner's IP.
The local minimal VPS-row factory was replaced by the existing `create_vps!`
helper, which supplies the dataset/pool/DNS associations required by an included
VPS. This fixture correction introduces no production behavior.

## Setup and checks

The initial worktree existed and was clean at the base. Reviewed `.overcommit.yml`,
all five `.git-hooks/pre_commit` plugins and the root Gemfile. In the repository
Nix shell, installed Overcommit and signed the reviewed configuration/plugins:

```sh
nix develop .#vpsadmin --command bash -c 'bundle exec overcommit --install && bundle exec overcommit --sign && bundle exec overcommit --sign pre-commit'
dev-session worktree add 2026-11-25-exception-root-cause vpsadmin --as-is --branch 2026-11-25-exception-root-cause --base origin/master
```

Both exited 0. The ordinary worktree retry returned the intended existing path.
No branch/worktree reset or hook bypass occurred. Fresh fetch retained the base.

Before-fix regression:

```sh
VPSADMIN_PLUGINS=all nix develop .#api --command bash -c 'bundle exec rspec spec/api/resources/incident_report_spec.rb --example "orders IP-filtered reports with includes"'
```

Failed as intended: 1 example, 1 failure, HTTP 500. The local synthetic fixture
log contains `Mysql2::Error: Column 'detected_at' in ORDER BY is ambiguous`.
Log: `/tmp/exception-root-cause-before.log`; elapsed 109.9 seconds including
first API bundle setup. Runtime: Ruby 3.4.12, ActiveRecord 8.1.4.1, mysql2 0.5.7,
HaveAPI 0.32.2; MariaDB 11.4.13 with REPEATABLE-READ and
`innodb_snapshot_isolation=0`.

Before input identities at base HEAD:

- Resource SHA-256: `d3c0b60e66d96c1fb7608df996965597ba55082c01bc4575ac6463ffe3b3a38c`.
- Regression spec SHA-256: `6dcc89a4f1439d759a947b5ed6077a4b802b586d4442c0414cca7ea47c688956`.

Changed-file lint before the resource edit passed using the root Nix shell:
`nix develop .#vpsadmin --command bundle exec rubocop api/lib/vpsadmin/api/resources/incident_report.rb api/spec/api/resources/incident_report_spec.rb`
(2 files, no offenses; root RuboCop 1.85.1).

After-fix full/core focused file, component lint, hooks and final source schema
export results will be recorded below before delivery. Longer integration
coverage is reserved until independent final review. Native verification uses
fresh GPT-6 Luna/low utilities selected from installed package
`/nix/store/1zn1a51qrsin83fszrprdjp45208vsj4-dev-workspace-0.2.0`, catalog
`1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c`,
`execution_access=full_access`. Its matching verification utility configuration
sets danger-full-access and approval never; no saved team settings changed.

The first full-mode after-fix file run completed 27 examples with two failures
in the changed includes examples: the query succeeded, then VPS serialization
encountered the pre-existing minimal fixture's missing dataset (`Vps#pool`).
Log: `/tmp/exception-root-cause-full.log`; test duration 7m03s, with 13.48s load.
The following core run was interrupted under lead authorization after the same
fixture defect was established. Its partial summary was 11 examples, 0 failures;
exit 1 means incomplete coverage. The enclosing script exited 1 in 12m29.8s;
component lint was short-circuited by the full-mode RSpec failure and did not run.

Interruption reconciliation: one SIGINT to the verified RSpec PID 3292837 caused
normal RSpec shutdown. `tools/test_db.rb` registers database stop/prune in
`at_exit`. The test runner, parent script PID 3214019 and owned MariaDB PID
3294919 exited; its exact disposable database directory under
`/tmp/nix-shell.DPsmbW/vpsadmin-test-db-auto-20261125-3292837-rx44rs` was absent.
Watcher command session 80874 completed with no owned cells/sessions remaining.
Only then was the fixture edited. The next batch runs the two changed examples
in both modes and required component lint; seven-minute full-file reruns are
reserved until final independent review per lead direction.

The next focused batch exposed a missing explicit `CoreResourceSpecHelpers`
include (full/core each 2 examples, 2 failures, before endpoint execution).
Both processes ended normally; no interruption or source edit overlapped them.
After adding the group-level include, a database-free Ruby/RSpec diagnostic
confirmed `create_vps!` resolves to that module with the expected keywords.
The diagnostic used the API bundle; a first root-bundle invocation lacked RSpec
and was corrected before any further database check.

The corrected full-mode ordering example passed: 1 example, 0 failures, about
43 seconds including setup, log `/tmp/exception-root-cause-one-full.log`.
Its source SHA-256 values are:

- Resource: `60df1134acd89a5c7f301596270187f218332306614055ef192df1ca6aafe35e`.
- Final spec: `8a99a06fc82f8b0c6223cf1347fce31696d9aa411d3147ae18d4fcf419abc37e`.

API-bundle changed-file RuboCop 1.93.0 passed both changed files after the fixture
and include corrections. Full component lint ran once: 1588 files, 25 offenses
in 10 unrelated files. [Baseline blob proof](B-lint-baseline.md) records every
offending file's identical base/current Git blob. No lint configuration, pin or
unrelated file is changed. Lead accepted preservation of this baseline gap for
disclosure to review; hooks still must pass normally.

Final focused completion reuses the passing full-mode ordering example and runs
only the full-mode member IP example plus both changed examples in core mode,
fail-fast. This passed in about 105 seconds:

- Full member example: 1 example, 0 failures; 38.35s plus 13.94s load;
  `/tmp/exception-root-cause-member-full.log`, seed 36293.
- Core changed examples: 2 examples, 0 failures; 38.59s plus 12.51s load;
  `/tmp/exception-root-cause-final-core.log`, seed 31217.
- Native source session 98867 and enclosing watcher invocation completed;
  no operation-owned work remained running.

Together with the separate full-mode ordering example, both changed examples
passed in both modes on the exact final source/spec hashes above. Final fresh
fetch retained `origin/master` at the exact base. Ordinary pre-commit hooks
passed: Nixfmt, MigrationSpecs, VpsadminWebuiI18n, RuboCop and VpsadminApiI18n.
Commit-message hooks passed with TextWidth warnings for three body lines over
72 characters; every line remains within the workspace's 80-character limit.
No bypass occurred. Worktree is clean and committed file hashes equal the tested
hashes above. No long full-file rerun, integration test or feature push preceded
independent final review.

## History, migrations and compatibility

Complete base-to-head series is one logical fix commit bundling its regression:
`da7724abdc080e59820cc4f0812ce1a41b3fc5df` (`api: qualify incident report
detection-time ordering`). Final diff: 2 files, 36 insertions, 25 deletions.
There are no
superseded approaches, follow-up implementation commits or repeated dependency,
channel, pin or generated-artifact streams to retain. No migrations, schema changes,
dependency changes, generated output or state conversions are introduced. No
feature head has been integrated, released or deployed; no changed or externally
consumed migration version exists.

This corrects read-query construction within the existing API contract. Existing
client/server request and response formats and node protocols remain compatible.
Old API processes may still return the exception. Software rollback restores the
bug without state repair. No integration, deployment or lifecycle action is part
of this package.

## Documentation and client assessment

| Topic | Reader / class | Authoritative home | Evidence |
| --- | --- | --- | --- |
| Reproduction and source lineage | Implementer/reviewer, individual execution | `design.md` and this packet | Before/after endpoint evidence |
| Report-order invariant | Maintainer, regression contract | `api/spec/api/resources/incident_report_spec.rb` | Opposite notice/trigger timestamps and exact ID order |
| Incident policy behavior | Maintainer/operator, reference | `docs/incident-escalation.md` | Checked; query correction leaves documented policy behavior unchanged |
| Generated-client freshness | Contributor, compatibility evidence | `docs/api-schema-export.md`; [B-export-receipt.md](B-export-receipt.md) | Final clean-head safety/snapshot 14/0; two fresh exports byte-identical; implementer1 owns three client comparisons |

No product or KB prose change is useful: the fix restores the existing listing
contract, introduces no configuration or operational sequence, and requires no
special upgrade or recovery procedure. Session-specific failure lineage belongs
here; the lasting sort invariant is expressed in the resource request spec.

## Review and publication

[Independent final review](review.md) by retained reviewer0 (gpt-6.1-sol/xhigh),
general and architecture/repetition lanes, found no findings at the exact range
above. It explicitly accepted the whole-branch history and no-migration inventory.
Lead accepted B implementation/export and released ordinary feature publication.

Fresh `git fetch origin` retained master at the exact reviewed base; worktree was
clean and no rebase occurred. `dev-session worktree capture-comparison` recorded
that base and final head. Ordinary SSH feature push through `nix develop
.#vpsadmin --command git push --set-upstream origin
2026-11-25-exception-root-cause` exited 0. A subsequent fresh `git ls-remote
origin refs/heads/2026-11-25-exception-root-cause` returned exactly
`da7724abdc080e59820cc4f0812ce1a41b3fc5df`, equal to local HEAD; worktree remained
clean. No default branch, integration, deployment or lifecycle operation occurred.

One bounded GitHub API discovery returned these push-triggered runs. Every run
has attempt 1, branch `2026-11-25-exception-root-cause` and head
`da7724abdc080e59820cc4f0812ce1a41b3fc5df`:

| Workflow | Workflow ID | Run ID / link | Status at discovery |
| --- | --- | --- | --- |
| API Specs (topic parallel) | 234996228 | [45641819759](https://github.com/vpsfreecz/vpsadmin/actions/runs/45641819759) | queued |
| CI | 228803702 | [45641819704](https://github.com/vpsfreecz/vpsadmin/actions/runs/45641819704) | queued |
| RuboCop | 229534945 | [45641819843](https://github.com/vpsfreecz/vpsadmin/actions/runs/45641819843) | in_progress |
| i18n health | 307073542 | [45641819724](https://github.com/vpsfreecz/vpsadmin/actions/runs/45641819724) | in_progress |

Raw discovery: `/tmp/exception-root-cause-push-runs.json`. Lead owns exact
runtime-ci observation; B does not poll these runs or launch another observer.
B retains completed-failure diagnosis and artifact assembly after outcomes arrive.
Required API evidence includes platform-operations full/core manifests and native
results proving this entire incident-report file and both changed cases ran,
plus topic coverage and other selected workflow outcomes. Local full-file reruns
are unnecessary when exact-head CI supplies the required modes.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-exception-root-cause/>.
