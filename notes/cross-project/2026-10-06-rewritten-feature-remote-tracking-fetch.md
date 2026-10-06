# Refreshing remote-tracking refs after an owned feature rewrite

Related initiative: work/2026-10-05-network-ipv4-left-counter.

The vpsadmin-webui canonical bare clone had no origin fetch refspec. After a
reviewed unmerged feature rewrite was pushed with an exact force-with-lease,
the remote branch held the new commit but local origin/dev/network-enabled
still held the old one. A later explicit fetch into that remote-tracking ref
failed non-fast-forward, stopping pin preparation before any pin mutation.

Parent verified the exact remote head, clean local feature head and untouched
configuration/KB worktrees, then fetched ONLY that remote-tracking ref using
an explicit +refs/heads/dev/network-enabled:refs/remotes/origin/dev/network-enabled
refspec. The guarded pin workflow could then resume unchanged. This updates
local remote-tracking evidence; it does not force-push a branch or authorize
rewriting any default or colleague-owned feature history.

When preparing a downstream pin after an authorized owned feature rewrite,
verify the remote SHA independently and account for this explicit tracking
refresh. Preserve clean/default ancestry/exact-head gates rather than weakening
them or adding a shared remote configuration change for one session.
