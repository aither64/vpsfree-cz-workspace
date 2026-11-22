# Preflight complete standalone synthetic status payloads

The supervisor integration example timed out waiting for a status watermark.
Its services log showed ActiveRecord::ValueTooLong: synthetic vpsadmin_version
was 26 characters, but status columns allow 25. Replaying the exact payload in a
disposable database reproduced the error; a 19-character value passed.

A later run failed before publication because the fixture copied current kernel
evidence after a legacy report. Waiting for the reporter process does not prove
its first evidence-bearing status has arrived. SnapshotReader(nil).to_h returned
{}, so fetching kernel failed. Define a complete standalone synthetic report,
including all required software identities, and preflight the exact literal
through PayloadParser and real persistence before a long VM run.

Related initiative: work/2026-09-14-kernel-history-fix. Its state and verification
artifacts record the successful preflight and final VM result.
