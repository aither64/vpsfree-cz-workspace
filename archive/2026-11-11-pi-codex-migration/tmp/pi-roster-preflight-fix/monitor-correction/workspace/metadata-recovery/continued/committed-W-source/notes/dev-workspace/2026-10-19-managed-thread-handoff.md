# Handing work to a managed session from an external conversation

The external task-message connector and a registered workspace App Server may
share persisted history while having different live thread writers. During the
archive repair, read_thread showed the managed lead idle, but send_message_to_thread
failed with thread/resume already has an active writer. No message was accepted.

Use the ordinary registered portal session message API to submit the same-session
handoff through the App Server that owns the lead. Retain one stable client
message UUID, the returned send receipt and the actual pickup acknowledgment.
Never infer acceptance merely from readable history or successful native delivery.
The portal response and transcript confirmed a new turn with retained Sol/xhigh
settings. Do not change a roster, launch a second CLI writer or forge environment
identity to work around the refusal.

Related initiative: work/2026-10-19-session-archive-refresh-fix/.
