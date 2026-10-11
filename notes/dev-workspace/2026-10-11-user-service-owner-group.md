# Owner group in existing user services

After a host activation adds an owner group, an already running systemd user
manager retains its previous supplementary groups. Its transient units can
therefore fail to read a root-owned group-readable password even when a fresh
shell has the declared owner group.

In this rollout, the manager had groups 1 and 100, while the owner account also
belonged to workspace-portal-owner (989). The password stayed
root:workspace-portal-owner mode 0640. An authenticated check passed from the
current shell. Launching the owned verification unit through
`sg workspace-portal-owner -c 'COMMAND'` applies the existing group membership
without changing file permissions or restarting the user manager. The password
is read into shell memory and curl stdin, never into command arguments or logs.

Related initiative: work/2026-10-11-cluster-controls/rollout.md.
