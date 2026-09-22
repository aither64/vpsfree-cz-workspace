# Phase 2C.0 mandatory review packet

## Outcome and scope

Review generic `dev-workspace` from
`6aa9be1969b428f67c63e04d0c60171305f70d83` through final generic head
`bb3de38`.

The final C0 amendment introduces the durable session-provenance classifier
used by the creation reader, helper and legacy lifecycle guard.

It classifies only `legacy_unmanaged`, `managed`, `managed_recovery` and
corrupt. The intentional recovery states are the valid schema-2
pre-publication record; the post-publication/pre-authority-record window; the
ordered finalization prefix journal `creating`, manifest `ready`, runtime
authority `creating` before its ready write; and the next prefix journal
`creating`, manifest `ready`, runtime authority `ready` before the journal
ready write. Each finalization prefix requires full state, binding, tmux and
runtime identity agreement. Inconsistent current state, binding, catalog or
runtime identity, including arbitrary mixed phases and all-creating phases, is
corrupt and fails closed. Existing schema-1 sessions, including `--no-codex`
journals, and unmanaged-source legacy forks are preserved without a migration.
Managed lifecycle operations remain unavailable.

## Finalization

- Final generic head: `bb3de38`
- Final fresh Luna/low watcher outputs: Go packages passed; creation suite
  passed with 12 runs and 148 assertions; host suite passed with 92 runs and
  524 assertions.

## Contract and compatibility

The authoritative design is `design-phase2c-runtime-dispatch.md`. The owning
documentation is `dev-workspace/docs/workspace-portal.md` and
`dev-workspace/docs/dev-sessions.md`. This has persistent-state, CLI/helper,
host transition and lifecycle-routing consequences, hence high risk. It adds no
daemon, package pin, database migration, deployment, rollback requirement or
new cross-project dependency.

The commit intentionally bundles the classifier, callers, strict reader,
candidate-registration invariant, documentation and tests: partial adoption
would recreate the ambiguity where a missing managed state is incorrectly
treated as a legacy session. Review fixes were folded into this owning commit,
so the branch publishes no intermediate incompatible state meaning.

## Evidence before review

- `nix develop path:. -c go -C portal test -mod=mod
  ./internal/agentteams ./internal/web ./cmd/workspace-portal` passed.
- `nix develop path:. -c ruby -Itest test/dev_session/agent_team_creation_test.rb`
  passed: 10 runs, 129 assertions.
- `nix develop path:. -c ruby -Itest test/workspace_host_test.rb` passed:
  91 runs, 520 assertions.

The final focused run after review remediation passed the same Go packages and
Ruby suites (the creation suite: 12 runs, 148 assertions; the host suite:
92 runs, 524 assertions). The fresh Luna watcher logs are
`phase2c0-go-tests.log`, `phase2c0-agent-team-creation.log`, and
`phase2c0-workspace-host.log`.

Fresh Luna/low watchers owned the uncertain-duration commands. Logs are
preserved locally under the initiative `logs/` directory.

## Lanes

General, Architecture/repetition, Scope/proportionality and
Risk/compatibility review at Sol/xhigh because the user explicitly prohibited
Astra. Reviewers reuse their retained initiative context while independently
reviewing this committed range.
