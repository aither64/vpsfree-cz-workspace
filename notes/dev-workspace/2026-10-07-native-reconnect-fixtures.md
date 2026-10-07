# Isolated native App Server reconnect fixtures

When testing the pinned native Codex binary with a loopback Responses provider,
return HTTP 426 to a WebSocket upgrade probe when the fixture only implements
HTTP streaming. Returning 404 causes repeated transport retries; an accepted
report can then appear stuck. The existing native naming fixture uses 426.

Pass explicit empty environment maps to StartThreadWithSettings and ResumeThread.
A nil map encodes the shell environment setting incorrectly. Seed a fresh thread
with an initial native turn/start before using client.Send, whose resume path
expects a saved rollout. These setup corrections enabled active-turn, queue and
report retry checks with native 0.160.0.

The native command approval request can precede its command item in
thread/items/list. The browser client correctly refuses to approve without that
authority. Reconnect coverage must distinguish request replay and the terminal
response path from browser approval coverage; do not weaken the browser guard
to make a synthetic test pass.

Go vendoring includes imports behind integration build tags. Adding wsjson to
the fixture changed the generated vendor tree even though default package tests
did not compile that fixture. A cached Nix fixed-output dependency masked the
mismatch locally; clean CI detected it. The fixture could use its existing
WebSocket and encoding/json dependencies instead, preserving the vendor hash.
Check freshly generated vendor contents when adding tagged imports.

Related initiative: work/2026-10-07-workspace-live-switch.
