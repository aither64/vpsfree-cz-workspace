# Child processes created by worker threads

The hosted shutdown tests at K3bb waited for a held late child to appear in the
runner receipt. Both failed at the same five-second barrier. The fixture spawned
that child on a worker thread, while ProcessIdentity read only
`/proc/PID/task/PID/children`.

Linux exposes the selected task's immediate children there. Enumerate every
numeric task under each recursively reached process, union child PIDs and retain
the existing process identity checks. Task IDs are not child-process records.
Do not move the fixture spawn to the main thread or extend the wait to hide this
ownership gap. The existing OSVM startup currently runs on the main thread; this
failure does not establish that earlier QEMU launches were missed.

A worker can exit and reparent its children to a task already visited in that
pass. A genuinely vanished task or changed task set therefore makes the pass
inconclusive. Preserve previously observed identities and observe again through
normal tracking. A live task with unavailable child data, permission failure or
malformed identifiers must refuse rather than report an empty tree.

Before K invokes machine cleanup, quiesce the tracker and repeat the full proof;
retain a fresh proof afterward before publishing completion. All-task traversal
remains non-atomic and cannot recover processes that escaped before observation
or repair old incomplete receipts.

K29b publishes this correction with the original worker-spawn tests and their
five-second guards unchanged. Its two source Checks succeed; independent affected
review and real guests remain pending at this note's boundary. No local test ran.
Evidence: `work/2026-10-05-network-ipv4-left-counter/`, accepted design5043 and
order reconciliation, `finish-k-task-children-commit1-proof.json`, and native
Checks37984641800/37984642157.
