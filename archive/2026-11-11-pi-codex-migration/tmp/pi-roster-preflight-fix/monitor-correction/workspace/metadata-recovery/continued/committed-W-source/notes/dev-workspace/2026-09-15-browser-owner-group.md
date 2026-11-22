# Refresh the portal-owner group for authenticated browser probes

A browser probe could verify the portal TLS certificate but failed reading
`/var/lib/dev-workspaces/password/password` with EACCES. The long-running Codex
process had only users/wheel in `id`, although `getent group
workspace-portal-owner` already listed aither. Existing processes had not acquired
the newly configured supplementary group.

Run the short authenticated probe with `sg workspace-portal-owner -c '<command>'`.
This uses the configured membership without changing file permissions or copying
credentials to a temporary file. Keep password reads inside the probe and never
print them. `sg ... -c id` confirmed the expected group; the browser retry could
then read the credential and reach the authenticated portal.

Related: `work/2026-09-15-portal-diff-highlighting/`.
