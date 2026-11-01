# Expanded packages A, B and D

Implemented, quick-checked, consolidated and published. Expanded final independent
review and longer acceptance remain pending. No default integration, deployment,
production correction, cluster operation or session lifecycle action occurred.
This supersedes the readiness description in `package-a.md`; its original heads
and evidence remain historical records of the narrower deliverable.

## Exact final ranges

| Repository | Base | Final head |
| --- | --- | --- |
| vpsadmin | `610a96f8ce523afbcd3e4374a70047dbe3264b0d` | `fb53edcb2326cd6c7d7bc638b3a0d86f4323deb4` |
| vpsfree-kb-contracts | `ce2c8cd9358c3636e5d39343e595df813a0b197f` | `938942f5235098faa0fa39a61fd4be42c488a969` |

Both feature branches are `2026-11-01-published-advisory-corrections`, in their
registered same-session worktrees. Fresh SSH fetch/ls-remote proves each final
feature head and unchanged remote master base. Worktrees/indexes are clean.
Both comparison captures use these exact ranges.

Final vpsAdmin series:

1. `da9ceeed36769f456afa834196d727c6c1cafbce` — API/model/spec/docs/locales A.
2. `fb53edcb2326cd6c7d7bc638b3a0d86f4323deb4` — legacy PHP/browser/locale B.

Final KB series contains one mechanical five-pin commit,
`938942f5235098faa0fa39a61fd4be42c488a969`. It selects final vpsAdmin above.
There are no schema migrations, seeds, transitive pin streams or obsolete
restriction/fixup commits in these final histories. Independent review must
assess complete ranges and explicitly conclude history/migration suitability.

Original ranges were `610a96f8..d80ac520` (A `892b68b4`) and
`ce2c8cd9..0a12d7d9`. These remain reachable via each repository's local
`2026-11-01-published-advisory-corrections-initial` branch and original receipts.
The expanded implementation is a substantive successor, not a patch-equivalent
rebase of the narrower scope. Neither original nor final source was deployed or
merged. No default history was rewritten.

Separate binary A/B patches, hashes and original refs were saved before scoped
restoration and two interactive-rebase edit stops. Amendments used ordinary
hooks. Final vpsAdmin tree `1e6709dcbf7e92372ae911bc359d6b95235318f6` equals
the captured intended expanded tree after one recorded test-layout-only change.
The prior expected tree was `c626b39e6f3b2fd7f1135db04c5247f91e21a4ee`;
root/component RuboCop disagreed on multiline call alignment, resolved with a
local relation variable. No semantic change was hidden by this proof.

## Expanded implementation and checks

Original report/time, CVE and node corrections support all three states. Every
affected mutation accepts optional expected state with required revision under
the parent lock; normal HaveAPI labeled choice maps expose machine values as
their keys. Node CRUD outside draft rebuilds the existing projections atomically.
Direct guarded retract/delete are silent, while separate update posts retain
their state/time/mail behavior. Publish now requires draft. Parent locking also
covers update creation, translation/delete and outage-link creation.

Tests cover expanded mutations, JSON DELETE input, new scopes, lifecycle retries,
draft publication behavior, resolved node validation and membership projections.
Core/full deletion coverage checks original/update translations, CVEs, node rows
and notes, VPS/user projections and outage links while preserving referenced
infrastructure, outages, transaction concerns and mail history. Rollback and real
concurrency cases cover correction/delete, update creation/translation/delete,
manual rebuild ordering and outage-link creation. No generic framework added.

Quick evidence:

- Runtime Ruby syntax passed; focused RuboCop passed all 11 touched Ruby paths.
- Final API locale generation/health and 11-file lint passed in 124 seconds,
  operated by fresh Luna/low watcher `01a19849-4d41-7881-9d67-7de6542b42c4`.
- Lead directly applied/approved writing guidance to final behavior docs,
  English descriptions/errors and exact Czech locale changes.
- Both final A/B amendments passed all mandatory hooks, including root RuboCop,
  API/WebUI locale health, MigrationSpecs and applicable PHP/Nix formatting.
- Final A/B resume batch exited 0 in 137.5 seconds. Final diff checks passed.
- B's seven frozen files and quick checks were accepted by the lead before
  implementer0 staged them. No unfinished or tracking files were staged.

## Concrete original-head CI failures and fixes

Automatic API CI `41331585935` tested exact original head
`d80ac520c66a9d4a318df517a06f13ac717f2399`. Failed logs were read before fixes.
Core foundation job `124922653647` had two failures:

- `rolls back changed notes, projection inserts and deletions and derived users
  after a rebuild failure`;
- `rolls back original fields, translations and timestamp when translation
  persistence fails`.

The parent lock's transaction joined the existing RSpec outer transaction;
catching the exception inside it retained partial writes. Public mutation,
delete, publish/rebuild and announcement/child-write paths now use conventional
`with_lock(requires_new: true)` savepoints. Parent serialization and one revision
increment remain. Named regressions additionally cover manual rebuild rollback,
announcement state/time rollback after mail failure, late dependent cascade
failure and earlier translations after a later child-translation failure.

Full/core platform-operations jobs `124922653434`/`124922654297` failed only the
expected-state metadata assertion: HaveAPI returns a labeled Hash, whereas the
spec assumed an Array. Final API specs check keys. Client owner was informed to
retain the real labeled-map capability contract. This is a test-contract fix;
no API downgrade or retry without preconditions was introduced.

These application regressions have not yet been run locally; no success is
claimed from quick checks or a blind CI rerun. Final review must inspect the
savepoint semantics, named coverage and actual metadata shape explicitly.

## KB five-pin disposition

D changes only `flake.nix`, generated `flake.lock`, `captures.json`,
`contract/navigation.yml` and `contract/pages.yml`: eight insertions/deletions.
All select final vpsAdmin. The explicit vpsAdminOS revision
`6bdf458fd9105379860234ff33d352e55844f08f`, every other lock node, root follows,
capture/page provenance, assets and source content are unchanged. Final vpsAdmin
input narHash is `sha256-spYZf0EgTF+SjhBqxb5MhhK8j8rhITgd9+zYzJaEjeM=`.

`nix flake update vpsadmin` passed, followed by pinned-shell JSON/YAML parsing,
Nix syntax, full before/after lock-graph equality outside the selected node,
exact-source pin/provenance checks and diff check. No hook framework or active
non-sample hook is declared/present. Advisory-control/page/capture binding search
remains empty. No strict `bin/check`, capture, staging or production operation
was launched; strict pinned-source acceptance follows expanded final review.

## Evidence and next step

Disposable exact logs/receipts:

- `/tmp/2026-11-01-published-advisory-corrections-expanded-a/`: original CI
  failures, final locale/lint logs, binary delta patches, consolidation inputs,
  initial hook-layout failure and successful resume/status.
- `/tmp/2026-11-01-published-advisory-corrections-kb-refresh/`: original five pin
  files, lock update, pinned-shell quick check and complete final lock graph.

Current vpsAdmin CI: API Specs `41335693055`, CI `41335692937`, i18n
`41335692911`, Webui PHPUnit `41335693071`, RuboCop `41335693151`. KB CI:
Check `41336064140`, Managed page runtime `41336064109`. Runs were only listed,
not awaited. Old-head vpsAdmin CI `41331585931` is confirmed cancelled; old KB
Managed page runtime `41331810954` is also confirmed cancelled after its head was
proven superseded. Current-head runs are retained.

Next: combine final A/B/D ranges with C/E, conduct expanded mandatory whole-branch
review, then run bounded full/core advisory/concurrency/plugin suites, legacy
browser acceptance and strict pinned KB `nix develop -c bin/check` as assigned.
The earlier paused narrower review is not final approval.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/>
