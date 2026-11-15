# Package D: monitor report invariant and compatibility

Accepted by lead at `3a0af7ad6b97ae4a3a7e38921beac8a2cdf9ff54`.
Implementation and focused checks are complete; final independent review and
long integration remain lead-owned. No push, deployment, live monitor resolution
or session lifecycle action was performed.

## Revisions and scope

- Repository: `git@github.com:aither64/dev-workspace.git`.
- Worktree: `worktrees/2026-11-11-session-archival-failures/dev-workspace`.
- Branch: `2026-11-11-session-archival-failures`.
- Base: `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
- D head: `3a0af7ad6b97ae4a3a7e38921beac8a2cdf9ff54`.
- One commit: `monitor: reject contradictory new terminal reports`.
- Exactly five files, 174 additions; no migrations, pins, generated files or
  superseded implementation history. No design deviations.

Owned files:

- `portal/internal/monitoroperation/service.go`: preserve the retained report
  validator; reject new terminal passed/failed with nonempty `stillRunning`
  after exact same-slot replay.
- `portal/internal/monitoroperation/launch.go`: explain reporting fields in
  newly frozen utility launch instructions.
- `portal/internal/monitoroperation/report_test.go`: focused admission and
  retained-record compatibility regressions.
- `skills/dev-session-monitor/SKILL.md`: watcher reporting instructions.
- `docs/dev-sessions.md`: monitor reporting section only.

Lead finalized the user-facing error and prose before commit. C's source,
browser tests and archive recovery documentation remained unstaged. The index
was empty when D released its exclusive commit window.

## Behavior and compatibility evidence

`TestOperationNewTerminalReportsRequireEmptyStillRunning` exercises both direct
`AddEvent` admission used by the cold observer and caller-bound `Service.Report`:
passed and canceled/failed reports accept omitted/empty fields; completed
evidence belongs in detail/evidence; `none`, historical none prose, whitespace
and actual running identities reject for new terminal passed/failed reports.
Incomplete outcomes retain their effects fence, including unknown identities.

`TestOperationHistoricalContradictoryReportRemainsImmutableAndFenced` writes a
disposable retained failed/cancelled record with the exact historical value:

```text
none; observation session 68962 exited 1; GitHub run 42816255766 attempt 1 is terminal completed/cancelled
```

It proves persisted reads and exact retries through both routes preserve the
event and accepted delivery receipt. Changed reports, foreign callers and changed
native epochs refuse. Lifecycle readiness remains fenced; ordinary evidence
resolution still requires native proof and preserves the original report and
receipt. Test fakes establish no new native launch, send or archival effects.

No persisted format changed. Older readers can read newly accepted reports;
new readers retain the original validation contract for historical reports.
Existing owner, epoch, source-result, external-effects and evidence-resolution
rules remain unchanged. The runtime does not parse English `none`, migrate
records or infer authority to resolve existing operations. Retained launch
instructions remain immutable; only new launch envelopes get the guidance.

## Checks and remaining boundary

- Nix formatting: `nix develop --command gofmt -w
  portal/internal/monitoroperation/service.go
  portal/internal/monitoroperation/report_test.go`, passed.
- A fresh native Luna/low watcher ran
  `nix develop --command go -C portal test -mod=readonly -count=1
  ./internal/monitoroperation`, exit 0, 20.253 seconds elapsed, Go package
  5.589 seconds. Log:
  `/tmp/2026-11-11-session-archival-failures-D-monitor-check.log`.
- Lead wording changed while that run was being prepared, so the now-known
  quick suite ran once more against the settled source using the same command:
  exit 0, 8.110 seconds elapsed, Go package 5.913 seconds. Log:
  `/tmp/2026-11-11-session-archival-failures-D-final-monitor-check.log`.
- Final source identity was unchanged before/after that check and after commit:
  `2821769456c86a3c195d58d3baf314e8348ccfc24d43391e4db80562481334be`.
  This SHA-256 covers, in order, `portal/go.mod`, `portal/go.sum`, then sorted
  `portal/internal/monitoroperation/*.go`, feeding each path, NUL, file bytes,
  NUL. It is scoped focused-check evidence, not a complete deployment input graph.
- `git diff --check`, staged diff check and base-to-D-head diff check passed.
  No declared hook framework, configured hook path or active repository hooks
  were present; no hook bypass was used.

The watcher used installed package
`/nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0`, catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`, schema 6,
verification utility
`dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`,
`gpt-6-luna`/`low`, danger-full-access and approval never. It reported no
remaining command or tool session. No watcher was reused.

Documentation placement: report behavior and compatibility live in the existing
session guide for operators/developers; agent execution guidance lives in the
existing monitoring skill and launch prompt. This record contains only package
status and verification evidence. README already links the monitoring section;
no new entry point was needed. Archive preparation/recovery documentation is C's
separate package.

Next dependency: lead assembles the complete C+D committed review packet and
invokes independent final review before long integration. Implementer1 remains
available for D review findings; no new package is assigned.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-session-archival-failures/).
