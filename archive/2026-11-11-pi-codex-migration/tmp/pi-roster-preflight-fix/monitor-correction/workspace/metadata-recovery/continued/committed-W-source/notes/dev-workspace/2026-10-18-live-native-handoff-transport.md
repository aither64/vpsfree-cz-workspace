# Use the workspace daemon for a retained-lead handoff

An externally initiating Codex app can read a retained workspace thread from
disk yet report stale interrupted/notLoaded status while the live workspace
daemon reports an active turn. Its direct send can also refuse another active
writer. A v2 utility refuses direct app-server input. These errors do not prove
the managed thread is idle or that a message was delivered.

Use the registered session portal's ordinary message endpoint for an explicitly
authorized handoff to that initiative's retained root. Preserve the stable
client message UUID and returned turn ID, then verify the receiving lead's actual
pickup and scope. Read the live session transcript or a receiving-lead pickup
artifact. For package cutover, use the selected runtime's require-idle probe on
the registered workspace daemon; do not infer idle from an external app's disk
read or change another session's identity.

During original profile recovery the managed lead must also become idle. Launch
its admitted recovery from a retained independent service under the actual
native-owner environment, then end that lead turn. Do not keep an active lead
turn awaiting an operation that must quiesce it. Retain the original job/attempt,
claim, source and approval; use the installed recovery procedure.

Evidence: work/2026-10-18-portal-untracked-files/rollout.md and
native-profile-recovery-pickup.json. This records transport and handoff behavior;
the profile rollout's final acceptance is tracked separately.
