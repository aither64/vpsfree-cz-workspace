# Automatic archival must preserve the retirement deadline

Related initiative: work/2026-09-16-archive-retirement-timeout/.

Automatic archival of 2026-09-15-abuse-uceprotect reached tracking_committed,
then hourly retries failed with exit 124 from workspace-portal thread retire.
The worker wrapped every subprocess in a 60-second GNU timeout, overriding the
retirement command's existing 180-second internal deadline. A read-only probe
of the exact directory-filtered thread/list took 70.453 seconds and returned the
expected idle conversation; direct thread/read and latest-turn reads took 7 ms.

Keep ordinary automatic commands bounded at 60 seconds, but scope a 210-second
subprocess deadline around retirement so the 180-second client deadline can
return an explanatory error. Test both timeout restoration and replay from
tracking_committed. Do not replace authoritative discovery with an index-only
lookup merely to avoid its cost.

The portal's pending phase is the last completed journal step, not the latest
failed worker attempt. Worker blockers and checked_at belong to a separate
private sidecar and must be matched to the same operation and conversation.

Recovery uses the installed dev-session archive command for the same slug/mode,
which resumes the journal and has no automatic worker wrapper. Complete pending
journals before package activation; never remove them to bypass that guard.
The installed manual retry completed the exact operation on 2026-09-16 without
another tracking commit. The journal and authority were removed, history moved
to archived_sessions, and both feature refs remained unchanged. Focused
subprocess/retry and Chromium/Firefox tests passed. Exact deployment results
are recorded in the initiative state.
