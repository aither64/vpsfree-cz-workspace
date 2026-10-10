# Retain review reports without granting tracking writes

Related initiative: `work/2026-10-05-network-ipv4-left-counter`.

A retained reviewer with `read_only` access should return its complete report
in the final response when the native lead-report relay is unavailable. Do not
ask it to create a fallback tracking file. The lead owns that record.

For this handoff, the lead collected only the assigned turn's final report from
the exact retained native thread. Validate the thread UUID and CWD, retain the
assignment's turn ID and preceding file offset, and require the matching native
completion event. A partial response or an older completed report cannot clear
the gate. Keep tool transcripts and unrelated thread content out of the record.

The App Server's Unix socket uses WebSocket framing. Sending newline-delimited
JSON directly closed the connection before an RPC response; it is not a
supported read recipe. Use the installed client for live requests. The owning
transport is `codex/client.go` in codex-web.

`dev-session team list --as-is` includes the installed catalog as well as the
retained roster. Parse and inspect the roster field for identity/settings rather
than printing the whole response and losing its end to output truncation.
