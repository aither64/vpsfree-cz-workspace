# 2026-11-27-monitor-native-command-launch-failure

## Goal

# Diagnose and fix native monitor command launch failures

Investigate the workspace's native `monitor_operation` path. Registered local
monitor operations are accepted with `executionOwner=native` and a live utility
thread, but intermittently never spawn their declared source command. Status
then remains `launch.state=running` with no command output or terminal event.
After cancellation, the utility can retain an active-native fence even though a
bounded process check proves that no registered command, builder, output, or
other native effect exists.

Reproduction observed on both a small exact Nix dependency build and a larger
livepatch producer build. Active-parent execution of the same command works,
so the failure is in monitor launch/utility orchestration rather than the Nix
build itself.

Deliverables:

- reproduce and isolate why the utility polls its operation status instead of
  launching the registered source command;
- fix launch, cancellation, terminal reporting, and external-effects fencing
  without weakening duplicate-run protection;
- add focused regression coverage for accepted-but-unlaunched commands and
  cancellation of such operations;
- document verification and recovery behavior;
- use the normal independent review and integration workflow; do not modify or
  interfere with the livepatch session's worktree, runtime operations, or
  private evidence.

## Affected repositories

- `dev-workspace`: native monitor registration, utility bootstrap, reporting,
  cancellation and external-effects reconciliation. Inspect `codex-web` only if
  the adapter boundary requires a change.

## Approach

1. Trace the registered source through utility instructions and launch receipts;
   reproduce with isolated fixtures and session-owned harmless commands.
2. Record the design and verification brief, then implement the smallest fix
   covering launch, cancellation and terminal/effect accounting.
3. Add focused regressions, update the owning documentation, run quick checks,
   commit and obtain mandatory independent final review.
4. Run applicable longer checks, publish the feature branch and prepare explicit
   repository/target integration approval. No live package switch is implied.

## Decisions

- Verified thread-bound session and matching environment on 2026-11-27.
- Live same-session roster is absent; the lead owns design and implementation.
- Do not access or change the livepatch session's worktree, operations or private
  evidence. Use only isolated/session-owned reproduction inputs.
- Preserve duplicate-run protection and uncertainty fences; absent output alone
  cannot prove that an accepted command did not run.

## Compatibility and deployment

Assess retained native operation snapshots, launch/submission receipts, restart
recovery and rollback. Preserve old operations' recovery contracts. Any schema
or cross-repository interface change needs explicit rationale and mixed-state
coverage. Keep the installed package unchanged during development and review.

## Documentation

Runtime maintainers and operators need a launch-state explanation and bounded
recovery steps. Update existing monitor/runtime documentation and skill guidance
where behavior changes. Keep reproduction and check evidence in this session.

## Testing plan

Focused tests must distinguish utility acceptance from command start; cover an
accepted utility that never launches, cancellation before launch and during
launch uncertainty, terminal event delivery, source/effect reconciliation and
unchanged-ID retries without duplicate execution. Use repository Nix tooling.
Select full packaged checks after diagnosis and independent review.
