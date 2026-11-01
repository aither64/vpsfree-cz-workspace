# Competing native conversation writers

At 2026-10-28 22:10–22:16 UTC, two App Servers share the same Codex home:

| Owner | PID | Native version | Socket |
| --- | --- | --- | --- |
| Managed Codex app daemon | 42858 | 0.165.0 | `/tmp/codex-daemon-1000/f22c2c5f700ab6c394dd5a6118426738ca3d4058a59872811943fbe02146e259` |
| Workspace App Server | 156049 | 0.164.0 | `/run/user/1000/dev-workspaces/vpsfree-cz/app-server.sock` |

The workspace socket resolves to another native socket, ending in
`bced879de15a05f23836072b53ea2860aa13a982415f07bf83ab93a6ee8c9ea6`.
The portal connects to this workspace authority, as its runtime records require.

The managed daemon holds the writer-lock descriptors and rollout descriptors for
both reported threads. A metadata-only `thread/read` returns `idle` for confctl
and `active` for autostart from the managed daemon. The workspace App Server
returns `notLoaded` for both. Its journal repeatedly reports:

```
failed to initialize thread persistence: thread-store conflict:
thread <id> already has an active writer
```

Autostart thread: `01a163b4-e2c6-7081-b9cb-e7a0e78eab4b`.
Confctl thread: `01a14bb2-e3ad-7922-a5c9-bc1d07d5cbb8`.

Historical activity can still be read through the portal: current local activity
requests return HTTP 200 with partial history statistics. These snapshots report
autostart as idle/interrupted even while its actual owner reports active. They do
not establish live timing or control. The browser displays `Timing unavailable`
when its activity request fails before it has any successful snapshot.

The failed original message was identified by SHA-256 of `yes go ahead`:
`998751648973f83f8ed6d0105f584a259060597f4b212c3e1f92941e65acbc90`.
Its durable portal send ID is `2a2656f4-3d35-4bee-9a71-14e20bc35669`, state
`prepared`. It has not passed the portal's native-send stage. Preserve that ID
for retry; do not invent a second send. This is distinct from unrelated uncertain
historical submissions in the ledger, which were not changed.

The native protocol has no general per-thread unload command. `thread/unsubscribe`
is connection-scoped: a guarded attempt on the idle confctl thread returned
`notSubscribed`, and did not release the owning app's writer. No thread was
interrupted, archived, deleted, copied, or rebound; no daemon was restarted.

## Pending recovery decision

Asked the user whether both interfaces are intended to remain usable. If the
portal alone should own these sessions, the app must release them after their
active work ends; then ordinary portal resume can reacquire them. If simultaneous
use is required, it needs an explicit shared-authority design rather than a blind
host redeploy or an unverified socket substitution. A version bump by itself does
not let two processes own one thread.

After the chosen repair, check native ownership and live portal timing, then POST
the original message through `/codex/conversations/2026-10-17-confctl-rust-rewrite-plan/message`
with `message: "yes go ahead"`, its original `clientUserMessageId`, and `retry: true`.
Verify acceptance and one matching transcript item. Do not use a separate native
send while the original browser receipt remains unresolved.

Schema inspection is retained in the untracked `native-schema/` directory; it is
disposable. This diagnosis is investigation evidence, not a completed substantive
implementation deliverable, so independent change review is not yet triggered.
