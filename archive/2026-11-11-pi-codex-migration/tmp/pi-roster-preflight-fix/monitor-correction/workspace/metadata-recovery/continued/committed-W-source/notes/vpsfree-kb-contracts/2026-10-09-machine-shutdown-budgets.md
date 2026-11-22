# Machine and controller shutdown budgets

The retained real isolation3 stop requested ordinary poweroff successfully, but
the services console still showed a console-router stop job after two minutes.
Its compiled guest unit allowed300 seconds. The old runner allowed120 seconds
per machine, while the controller independently allowed120 seconds for the
entire sequential shutdown. Node exit0 did not prove services exit.

Increasing only the controller timeout cannot extend the machine's wait or repair
a runner that already exited with incomplete child evidence. The guest service's
failure to stop promptly remains unexplained. Retain the failed receipts and
live-child ownership limits; no later source correction supplies missing exit
proof or cleanup permission.

The prospective runner uses its configured machine budget, latches one graceful
stop and keeps the same owner, tracker, listener and reapers while children remain.
A public join return is not enough: the pinned OSVM implementation discards its
wait timeout result. Require machine `!running?` plus all retained children gone.
Caller expiry is an observation failure, not authority to repeat poweroff, signal
a group, release claims or publish incomplete exit as terminal.

Withdraw readiness when shutdown starts and use one canonical readiness predicate
in status, capture and the selected workspace SDK consumer. Retained process
liveness and capture readiness have different meanings.

This behavior is published at K29b/E2ec; exact source checks and independent
review are separate from real shutdown proof. The retained old isolation3 run
cannot receive the correction retroactively. Evidence:
`work/2026-10-05-network-ipv4-left-counter/design.md` shutdown diagnosis and
4710/4866 proposal, `finish-direct-isolation3-retirement-failure1.json`, and
`finish-k-shutdown-owner-source1.*`.
