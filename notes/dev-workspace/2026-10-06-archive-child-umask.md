# Keep the native archive child umask at 022

A private maintenance wrapper used umask 077 for its logs and backups, then
passed that umask to dev-session archive. The archive projected state.md and
portal.yml as mode 0644 but wrote them as 0600. Recovery refused the moved
tracking tree because its immutable hash includes file modes.

Keep the maintenance directory private, but invoke the ordinary archive child
under umask 022. When supplying confirmation through script's PTY, set the
umask in the child subshell before script.

For the five affected records, independently computing the exact native tree
hash with only those two mode corrections matched the saved journal projection.
Restoring only those modes made the actual hash match; ordinary native retries
then resumed. No contents or journal hashes were rewritten. A mismatch still
requires diagnosis and must not be cleared by editing the journal.

Related initiative: work/2026-10-04-session-archive-reliability.
