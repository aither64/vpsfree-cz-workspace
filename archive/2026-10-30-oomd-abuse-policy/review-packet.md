# Final application review packet

Original committed application review completed with R1 Blocking and R2/R3
Important findings; see [original report](review.md). Backend fixes passed
45 focused application examples and2 separate migration examples and are being
consolidated; final corrected architecture/risk clearance is pending. Original
ranges below remain the review receipt, not clearance of later changes.
Dependent KB source awaits exact publication after corrected source review.

## Requested outcome and accepted boundary

Implement oomd incident escalation in vpsAdmin, both legacy and React WebUIs,
and localized site email templates. User authorized implementation; merge and
deployment remain separate. Keep original defaults: warning at 5 incidents in
rolling 7 days, stop at 10 in rolling 30 days. Repeat stops need a new incident
and at least 24h after the previous confirmed stop; cooldown expiry never stops
a VPS. Recovery is count expiry below the monthly threshold. The proposed 3/8
alternative was explicitly declined; VPS28376's known sample is intentionally
below the selected monthly limit. No burst rule or quiet-period latch.

Admins get inherited/default limits, nullable per-VPS overrides and a stop-only
exemption. Counts/warnings/host protection remain. Backend owns batch summaries,
permissions, source deduplication, durable action identity and stop/mail progress.
Successful ownership change resets the accounting epoch but preserves the
physical stop cooldown/audit. Events >24h old may count but cannot dispatch.
Observe is the deployment default; no historical mass action or live activation.

User emails gently explain shared-node disruption, worker concurrency vs memory
needs, and link language-specific membership expansion guidance. Say users can
increase memory, not request it. Do not say "policy" in member mail. Stop promises
must reflect current effective enforcement/limits at send time. Counts may remain
decision snapshots. Send stopped email only after a confirmed successful stop.

Sources: [plan](plan.md), [design](design.md),
[implementation contract](implementation-contract.md), [copy brief](mail-copy.md),
[log evidence](evidence.md), [state](state.md).

## Scope, sources and history

All worktrees are under
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/`.

| Repository / branch | Base | Final head | Whole-series disposition |
| --- | --- | --- | --- |
| vpsadmin / 2026-10-30-oomd-abuse-policy | ac10a62f1cb0fc890378ae83cdf18dd0e29f049a | 51297de1a05fee60aaba8a31e443abf95675396c | Two focused commits listed below; no obsolete branch iterations/repeated pins |
| vpsadmin-webui / dev/oomd-abuse-policy | 40653dffed4561dd6086716fd506a7223d3631d7 | 6fcbbc172277677785b59ec2ee66724c3b1c1bb6 | One commit: vps: show memory incident limits and stop status; no obsolete history or repeated dependency streams |
| vpsfree-notification-templates / 2026-10-30-oomd-abuse-policy | 2cfd218d9152888feea4109f064459078ea9f76e | e8c2c3df4ae57015ff4fba3647b13aa219d0c216 | One commit: vps_oom: add repeated-incident warning and stopped mail; final past-effect autostart correction folded, no obsolete history or repeated dependency streams |

Inspect complete `git log BASE..HEAD` and `git diff BASE HEAD` in each worktree,
not only the latest commit. Template source is already published; application
branches are held locally until source review because pushes automatically
launch long hosted checks. No feature has been merged or deployed. Require
explicit independent whole-branch history and migration conclusions.

Full vpsadmin series:

- `a9e5fe4ff1c7071672c76e7627ff870008eb99a4` api: handle repeated OOM daemon incidents
- `51297de1a05fee60aaba8a31e443abf95675396c` webui: show repeated OOM incident limits and controls

Final vpsadmin diff47files+2522/-123. The backend commit includes schema,
API/evaluator/source ingestion, related tests, owning docs, generated locale
metadata and CI/test registration; the legacy commit includes9approved UI,
locale and focused/browser test paths. Their split follows repository ownership.
No intended source remains uncommitted; only disposable untracked PHPUnit cache.
Normal hooks passed, including migration/API locale/RuboCop/Nix/legacy locale
checks. Initial backend hook snapshot conflict was reconciled by isolating and
trap-restoring the exact untracked legacy form; no hook bypass or broad stash.

Migration inventory: vpsadmin adds `20261030180000_add_vps_oom_policy.rb`, intended
as one direct additive schema migration from the preceding existing schema.
Unmerged/unreleased/undeployed and not externally consumed; migration and core
schema are committed together. New migration focused tests passed separately.
  Backend owner's [final detailed packet](backend-delivery.md) records exact
  hooks, commands, migration provenance and completed-operation evidence. React and
templates have **no migrations**. No dependency/pin update stream belongs to
these three application packages. Supported old nodes/protocol remain; no
coordinated node update or generated-client prerequisite. UI hides the feature
when an older API omits summary fields.

## Evidence and documentation

- Backend: commits complete as above. Initial DB-switching migration/app
  batch was invalid; migration and application groups now separated. A numeric
  SQL default-comparison defect was found and corrected, with regression coverage.
  Broad related batch205examples/4failures,201passed; all4failures traced to
  fixtures/cleanup and fixed without runtime source changes. Corrected affected
  policy/concurrency batch16examples/0failures, separate migration2examples/
  0failures; reuse existing successful201examples. All24touched Ruby files lint
  clean; i18n health, checker58templates/186files, CIselector16tests/55assertions,
  Nix parse/format and whitespace pass. Final real mail-render case1/0 passed.
  Owning docs `docs/oom-abuse-policy.md` and index link explain behavior,
  compatibility, deployment modes, failure handling and rollback.
- Legacy: [delivery](legacy-ui-delivery.md), full PHP116tests/803assertions,
  final focused9tests/65assertions, PHP lint/gettext check/scoped formatter/browser
  source syntax. One known unrelated pagination nullable deprecation recorded.
  Lead checked final EN/CS copy. Commit hooks performed by backend Git owner.
- React: [packet](react-package.md), typechecks including prepared E2E source,
  57focused/adjacent tests plus16final rendered cases, lint/format/mutation/UIstring/
  i18n8403/design/inventory/structural checks. REQ-051 and owning docs updated;
  main-agent prose pass completed with locked terminology revision in packet.
- Templates: [packet](template-package.md), checker75templates/373files,
  flake check,16render permutations+8first/repeat equivalences with actual pinned
  renderer/Prague time helper. Final past-effect autostart wording corrected
  because manual start can re-enable it before mail is delivered. Only those
  two language sentences changed from initialc8cb569; old/new range evidence in
  template packet. Final exact-head hosted CI41107732433 succeeded.

Long application integration/browser checks have not run. After review, package
owners run bounded real isolated backend/legacy integration and synthetic React
browser flows/screenshots; distinguish fixture from real API evidence. Failures
remain owner implementation/fix work and may need affected-lane review if material.

Required external KB workflow is a dependent verification package, prepared by
implementer3. [KB packet](kb-package.md). Two existing bilingual list concepts,
four PNGs, are affected. It needs the final published combined vpsadmin head;
contract source pin/check/commit and a separate mandatory source review precede
long capture builds. Existing details crop excludes the appended OOM section.
No invented React capture certification, production KB write or broad baseline
refresh. Disk capacity admission is unverified; no capture runtime launched.

## Reviewer assignment

### Corrected-range follow-up

Original findings/report are preserved in [review.md](review.md). Corrected
vpsadmin backend is `dbfd2bbf060237189797aafa7db359ea0edbd797`, legacy/head
`5a59ead40a283f74d211c7afde4d4d69aab28785`, sameac10a62f1base. Two focused commits,
unchangedUIpatch, nofixups; final tree equals testeda916b2a8193236850d4704eef254ae1fe9526502.
[Remediation receipt](remediation.md) and old/newrange-diff bind exact evidence.
45focusedapp/0failures +2separatemigration/0failures, scopedlint, core schema,
normalhooks and parsed/linted actualtransfer extension. GenericNewallowempty/
nullableCreate, ordinarymailprepared-or-suppressedack/savepoint, stop-first,
mixed-write rejection/audit and summarynilguard address R1-R3. Original migration
is amended directly; no consumer/release/deployment boundary intervened.

React final `5d262808311831334086584d5914552426788fbf` differs from original
reviewed6fcbbc17 only approveddocs/worklog/testtitle; runtime/assertions byteequal,
6focusedtests+docsaudit passed. Templates unchanged e8c2c3d. Follow-up assigned
same verified reviewer0 /savedSolxhigh, architecture/risk lanes only plus final
history/migration conclusions; originalgeneral/scope review retained. No runtime
clearance yet. Physical transfer proof now included in prepared scenario but
remains unrun until corrected source clearance.

Overall risk **High**: persisted schema/action state, automated VPS stops,
authorization, rolling counters, chown and mixed-version behavior.

Use retained independent reviewer0, saved `gpt-6.1-sol` / `xhigh`, read-only;
Live roster verified same session before assignment. All four mandatory-change-review
lanes apply: general, architecture/repetition, scope/proportionality, risk/
compatibility. Read the skill and every lane reference. No early/advisory review
is being requested; complete application sources are committed and quick checks passed.
Review directly without nested reviewers. Report concrete findings and residual
test/deployment limits, including explicit commit-history and migration lineage
conclusions. Fixes remain with package owners; no review permission to merge.
