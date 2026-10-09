# Test-shell boot readiness does not establish SSH readiness

In the ordinary-host campaign, the pinned OSVM `wait_for_boot` accepted the
virtio test-shell marker. It does not wait for sshd. The subsequent single
`ssh-keyscan -T 5` failed at K7dc4d708, leaving phase `verifying`; its generic
35-byte error omitted the machine, exit status and diagnostic stderr.

The source-supported correction is SSH-specific discovery under the existing
absolute readiness deadline, with per-machine private native evidence and
complete candidate trust before any write. Invalid keys, identity loss and
retained-key mismatch remain immediate refusals. Guest authentication and
source/closure attestation are separate requirements.

The actual failing endpoint and reason are unknown. Guest logs show startup,
not a conclusive transport diagnosis. The runner continued publishing briefly
and later its recorded tuples were absent without a complete receipt. Neither
absence nor a guessed executor teardown authorizes cleanup. POSIX session
separation does not escape cgroup termination; real verification needs a durable
operator-owned execution context, including for the unchanged predecessor.

Source acceptance and forthcoming hosted/real results remain separate. See
`work/2026-10-05-network-ipv4-left-counter/design.md` and the linked SSH/lifecycle
failure summaries in that session’s state. Both failed states remain retained.
