# Recovery review reconciliation

All four mandatory lanes reviewed vpsAdmin `268f7d09b9e3ca59d2b8f286e6666f72f9f7a9ff`
and maintenance `c77ff3742f623afd23c0be26c0f6ddbc026f1ba4`. Each reviewer used a
fresh standalone GPT-6 Astra agent at xhigh, as explicitly selected by the user.
Risk is high because the change stores comparison evidence and changes inferred
history bounds. Scope and compatibility reported no additional findings.

- General G1, Blocking: the synthetic recovery software revision was not a full
  Git SHA, so the actual parser rejected it. Replaced it with 40 lowercase hex
  characters. The exact base and recovery construction snippets extracted from
  the Nix integration scenario now pass PayloadParser in the API environment.
- Architecture A1, Blocking: the installed API interpreter loads scripts without
  changing `$0`; the old executable guard silently skipped the command. The
  dated task now has a small executable that unconditionally invokes its
  importable runner. Subprocess tests use the installed interpreter's `load`
  semantics and verify help, all-node preview, subset apply, all-node apply and
  an idempotent rerun on disposable MariaDB data. All 29 maintenance examples pass.
- Architecture A2, Advisory: the existing HistoryBackfill default is 10,000,
  despite the plan and help promising 1,000. Kept the approved follow-up's 1,000
  as an explicit task-owned constant shared by Runner, NodeRepair and help.
  Removed the incorrect claim that it matched HistoryBackfill. The execution
  test asserts the effective default, and all six task Ruby files pass lint.

These are direct, bounded remediations of reviewed behavior. They introduce no
new public contract or repair scope and require no review rerun under the skill.
The changes are folded into their owning feature commits. Final heads and
subsequent integration, exact pin reviews, builds and CI are recorded in state.md.

Persistent reviewer instructions are unchanged; the user owns that update in
another session. Production and session lifecycle remain untouched.

Final downstream reviews bind V42984def6/Cc8b7a499/K610cb7bf/M2fdc9f28. General
found an Important operator issue: NixOS /etc units outrank runtime masks. Both
lanes reviewed the replacement start-condition drop-in+marker and both-host
checks around activations, exact generation selection, and scoped restoration.
An isolated live systemd fixture and pinned activation source inspection support
it. All 14 prepared shell blocks parse. M's final amendment changes README only.
No unresolved findings remain. Full VM activation rehearsal is not claimed.
