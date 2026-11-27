# Independent final review packet

Requested outcome: minimal mail/DNS nodectld must not require osctld; restore the
existing watchdog everywhere the common NixOS/systemd service runs. The user
explicitly included DNS. No deployment or default-branch integration authorized.

Repository: vpsadmin, worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-27-nodectld-minimal-watchdog/vpsadmin`.
Base: `99207a8dcd92f5907c52dbc99af52b30aa7ecac1` (freshly fetched origin/master).
Final commits/head will be recorded below before review starts.

Read [design](design.md), [plan](plan.md), [state](state.md), repository AGENTS and
applicable routed procedures. Review the full base-to-head series and final diff.

## Scope and implementation

The minimal-mode override disables ExportMounts and VpsOsRelease, retaining the
existing override precedence on load/reload. Their constructors and refresh
methods already gate on enable flags. Standard-mode defaults remain enabled.

The common NixOS unit runs the existing wrapper. Restart=always handles the
wrapper's successful watchdog exit. KillMode=mixed gives the wrapper initial
TERM ownership; TimeoutStopSec=90 provides margin over its 60-second child kill
escalation. Existing restart delay/rate limits and production watchdog timings
remain unchanged. No runit changes. A disposable integration fixture accelerates
timers and blocks polling without adding production test knobs.

Acceptance: no osctld calls from minimal facilities; queued mail and DNS work
succeeds; a responsive status thread does not hide stale transaction polling;
unresponsive child recovery is bounded; one wrapper/child after recovery;
manual systemd stop stays stopped; nodectl restart/stop retain supervised
semantics. Inspect all new scenario assertions, including real mail capture and
BIND reload chains. The scenario is evaluated/syntax checked but deliberately
not executed until final review.

Non-goals: prove the original native hang's exact cause, change database timeouts,
change transaction semantics, add a new watchdog, deploy/pin production configs,
or guarantee exactly-once SMTP delivery. Logs established the two defects;
there was no pre-kill backtrace proving the blocked native call.

## History and compatibility

Two logical commits: minimal policy + focused specs; systemd integration +
packaged regression + operator guidance. The second scenario exercises the two
fixes together because the common mail/DNS fixture must stay healthy to test
watchdog recovery. No obsolete approaches, migrations, schema/API/protocol
changes, dependency/pin streams, generated artifacts, or externally consumed
branch iterations. No migrations were merged, released, deployed or consumed.
No coordinated node update is needed. Deploy the generated NixOS unit with the
matching package; an executable-only update leaves an old unit bypassing the
wrapper. Rollback remains data compatible but restores old reliability defects.

Owners/consumers: AppConfig owns minimal-mode policy; ExportMounts/VpsOsRelease
consume its enable flags. nodectld Cli owns wrapper and watchdog recovery.
NixOS common nodectld module owns systemd lifecycle and is consumed by mailer
and DNS modules/test guests. vpsAdminOS runit already runs the wrapper and is
unchanged. Representative runtime integration covers both NixOS roles; existing
node-control smoke tests cover standard/runit behavior.

## Documentation routing and evidence

| Topic | Reader/class | Authoritative home | Evidence |
| --- | --- | --- | --- |
| Minimal mode, watchdog, service control and diagnostics | Operator, reusable operations with concise config facts | `docs/operations/nodectld.md` | AppConfig, Cli, TransactionWatchdog, NixOS/runit modules and command handlers |
| Chain failure semantics | Developer/operator, reference | Existing `docs/transactions.md`; new runbook link | Existing transaction execution/confirmation code; no semantic change |
| Entry point | Developer/operator, navigation | `docs/README.md` | New runbook link and all changed local links resolve |
| Individual incident and planned rollout | Session evidence | plan/state/design | Central log timeline and user-confirmed kill; no deployment claimed |

No content was moved or removed. Writing skill applied by the context-owning
lead. Require an explicit documentation placement/preservation conclusion.

## Quick checks

- Focused RSpec config, export mounts, transaction watchdog, CLI socket watchdog,
  remote status/debug: 18 examples, zero failures, `final-specs.log`.
- RuboCop changed Ruby files: clean. CI selector: 16 cases / 55 assertions clean,
  `lint-selection.log`.
- Nixfmt, Nix parse/full scenario evaluation and evaluated Ruby script syntax:
  passed (`test-config.json`, `evaluated-test.rb`, `commit-setup.log`).
- `test-runner.sh ls --filter 'tag=ci && (tag=admin || tag=dns)'` includes the new
  test, `test-selection.log`. Existing runtime mappings select node/dns, and
  NixOS/all-tests changes select full CI; no selector rule needed.
- `git diff --check` and changed doc links: clean. Declared commit hooks must
  pass; final commit receipts recorded below.

## Review policy

High risk because daemon/process lifecycle affects host/service operations.
Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Use mandatory-change-review and all four lane references. Require explicit
whole-branch history, repeated-update-stream and no-migrations conclusions.

Tracking-only session has no valid native lead/retained roster (verified with
`dev-session team list`). Installed default development team's first
review-purpose role: reviewer, gpt-6.1-sol, xhigh, read-only. Fresh standalone
fallback, no nested agents. Catalog digest
`1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c` from
`/nix/store/4d0iy6lkl1jq9nngi9mkf3mb2ydj6vxi-dev-workspace-0.2.0`.

Return findings with severity, lane and file/line evidence. Do not edit source,
run long integration tests, merge, deploy or approve on the user's behalf.

## Final committed range

Complete series, oldest first:

1. `e9a52767538537798d0c60db38f96d843ad84a05` — minimal-mode policy and specs.
2. `84cc09332fc09e3178405df34539cbd4c1d20a46` — systemd supervision, regression and docs.

Final head: `84cc09332fc09e3178405df34539cbd4c1d20a46`.
Worktree clean; full range diff check passes. Both commits ran all declared
Overcommit hooks successfully (Nixfmt, MigrationSpecs, WebUI/API i18n, RuboCop;
commit-message checks passed with advisory 60/72-column width warnings; all
messages comply with repository/workspace 80-column requirement).

## Follow-up: main-thread progress correction

The first review's Important finding is corrected using the design addendum.
New `last_transaction_progress_monotonic` advances only after a successful poll
or when the transaction loop reaches an intentional skip (full queues or
pause/draining). Existing real-poll fields remain unchanged. Watchdog status and
debug add the new field; wrapper prefers it and falls back to the existing poll
field. The runbook documents the diagnostic interface and in-memory pause scope.
No persisted state, schema, API, configuration options or thresholds change.

The full focused suite, now including Daemon, passes 37 examples
(`progress-specs.log`). After a style-only local fixture rename, the affected CLI
suite passes all six examples (`progress-cli-final.log`). Nine touched Ruby files
pass RuboCop (`progress-lint-final.log`), Nixfmt passes, and the revised packaged
scenario evaluates and its generated script passes Ruby syntax checking. New
packaged pause/resume examples wait past the test watchdog restart deadline,
assert unchanged processes and queued chains, then resume and verify real work.

Review the correction under general, architecture and risk/compatibility;
recheck proportionality/history for the final consolidated range. The correction
is folded into the systemd commit: the rejected polling-only integration is not
retained as a transient branch commit. The first reviewed SHA remains recorded
here and in review.md solely as evidence, and was never published or deployed.
Final amended SHA/clean status will be recorded before reassignment.

Corrected final head: `258a62e4ac7234639aecebf6cdce726ef9c5fcd7`.
Series: unchanged `e9a52767538537798d0c60db38f96d843ad84a05`, then amended
`258a62e4ac7234639aecebf6cdce726ef9c5fcd7`, against the unchanged recorded base.
Worktree clean, range whitespace clean, all declared commit hooks passed.
No migrations or repeated update streams. Review old-head-to-new-head correction
and final base-to-head history/compatibility conclusion.

## Runtime-discovered stop parser correction

Final candidate head: `a8ef7163832f3c246bb3927f00d68dd5a001818b`.
Complete series against the same base:
1. `e9a52767538537798d0c60db38f96d843ad84a05` minimal policy/specs.
2. `f3a74127a30fffc9d14a26100636ce2cfed91110` supervision/progress/tests/docs.
3. `a8ef7163832f3c246bb3927f00d68dd5a001818b` pre-existing stop parser typo.

The r2 runtime run passed 12/14 examples, including all actual watchdog and
pause recovery for both mailer and DNS. Both `nodectl stop` examples failed
before sending a request: `Stop#options(_parse, _args)` uses `parser` in the
body. The third commit changes only that parameter to `parser`. This existing
bug is independently revertible and not an obsolete iteration of the supervision
change. The second commit differs from the prior full reviewed head only by
replacing unsupported test DSL `let` with an ordinary role-local binding.
No migrations, repeated updates, dependency changes, production deployments or
external consumers of intermediate revisions.

Focused check through the real CLI dispatch/parser (remote execution intercepted)
passes default stop, --force, -f and --help. Targeted RuboCop and full-range
whitespace pass. All declared hooks passed; worktree clean. Evidence:
`stop-parser-check.log`, `check-stop-parser.rb`, `commit-stop.log`.

Retain the previous architecture/scope conclusions; review only affected general
and CLI risk/compatibility behavior, and confirm the complete three-commit history
conclusion. No new interface, stop semantics or documentation change is intended.
