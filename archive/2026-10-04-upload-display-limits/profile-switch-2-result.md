Terminal summary: successful activation at 03:27:57 CEST on October 5; atomic
exit 0, phase activated, inactive/dead, systemd result success. Historical
observations below describe earlier busy waits and the final terminal proof.

# Profile switch attempt 2 observation

- Result: incomplete; the existing user service remains active, so no exit status has been produced.
- Run: `upload-profile-switch-20261004-2.service`.
- Workspace revision: `88c0b957a1e870e4ce36a1743f72b529ba4825e1`.
- Selected package candidate: `/nix/store/jq982nq0jxfhmr4jxyvkglnyy77n1kxf-dev-workspace-0.2.0`.
- Observed elapsed time: about 15 minutes 57 seconds from the log's `2026-10-04T23:04:02+02:00` start timestamp to the scheduled check at 23:19:59 +0200.
- Current service properties: `ActiveState=active`, `SubState=running`, `Result=success`, `ExecMainStatus=0`.
- Phase: `waiting for busy Codex; next check in900seconds`.
- Terminal file `profile-switch-2.exit`: absent.
- Blocker evidence: log reports thread `01a0d230-6068-71d2-9768-4928682cdccf` is not idle; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` has status `inProgress`, during `quiesce 2026-09-23-storage-redesign`.
- The phase file was updated at 23:19:59 +0200; next scheduled busy check is approximately 23:34:59 +0200.
- Observation continues. No retry, deployment, interruption, or approval action was taken.

## Scheduled recheck at 23:35:01 +0200

- The phase has advanced to `switching` after the scheduled busy check.
- Service still reports `ActiveState=active`, `SubState=running`, `Result=success`, `ExecMainStatus=0`; `profile-switch-2.exit` remains absent.
- Log still contains the prior `not idle` evidence; no newer terminal status is present.
- Phase mtime 23:35:01 +0200 sets the next scheduled busy check at approximately 23:50:01 +0200. Observation continues.
- Correction: because the phase is `switching`, the 23:50:01 estimate is not a scheduled retry time. A next busy-check time can be derived only if a later phase again reports `waiting` with a current busy refusal.

## Fresh busy refusal at 23:35:25 +0200

- Phase returned to `waiting for busy Codex; next check in900seconds` after another refusal for thread `01a0d230-6068-71d2-9768-4928682cdccf`, latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` still `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 23:50:25 +0200, based on the waiting phase mtime 23:35:25 +0200.

## Fresh busy refusal at 23:50:50 +0200

- Scheduled check again returned `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`, latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` still `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 00:05:50 +0200, based on the waiting phase mtime 23:50:50 +0200.

## Fresh busy refusal at 00:06:16 +0200 on 2026-10-05

- Scheduled check returned to `waiting for busy Codex; next check in900seconds` for the same thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` remains `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 00:21:16 +0200, based on the waiting phase mtime 00:06:16 +0200.

## Fresh busy refusal at 00:21:41 +0200 on 2026-10-05

- Scheduled check returned to `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` remains `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 00:36:41 +0200, based on the waiting phase mtime 00:21:41 +0200.

## Fresh busy refusal at 00:37:07 +0200 on 2026-10-05

- Scheduled check returned to `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` remains `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 00:52:07 +0200, based on the waiting phase mtime 00:37:07 +0200.

## Fresh busy refusal at 00:52:32 +0200 on 2026-10-05

- Scheduled check returned to `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` remains `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 01:07:32 +0200, based on the waiting phase mtime 00:52:32 +0200.

## Fresh busy refusal at 01:07:59 +0200 on 2026-10-05

- Scheduled check returned to `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` remains `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 01:22:59 +0200, based on the waiting phase mtime 01:07:59 +0200.

## Fresh busy refusal at 01:23:26 +0200 on 2026-10-05

- Scheduled check remains a busy refusal: phase is `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` is still `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 01:38:26 +0200, based on the waiting phase mtime 01:23:26 +0200.

## Active switch phase at 01:38:27 +0200 on 2026-10-05

- The scheduled attempt advanced to `switching` (phase mtime 01:38:27 +0200), after the preceding busy refusal.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Observation continues for terminal completion or a fresh busy refusal.

## Fresh busy refusal at 01:38:51 +0200 on 2026-10-05

- The active attempt returned to `waiting for busy Codex; next check in900seconds` for the same thread `01a0d230-6068-71d2-9768-4928682cdccf`, latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` still `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 01:53:51 +0200, based on the waiting phase mtime 01:38:51 +0200.

## Fresh busy refusal at 01:54:17 +0200 on 2026-10-05

- Scheduled check returned to `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` remains `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 02:09:17 +0200, based on the waiting phase mtime 01:54:17 +0200.

## Fresh busy refusal at 02:09:45 +0200 on 2026-10-05

- Scheduled check returned to `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` remains `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 02:24:45 +0200, based on the waiting phase mtime 02:09:45 +0200.

## Active switch phase at 02:24:46 +0200 on 2026-10-05

- The scheduled attempt advanced to `switching` (phase mtime 02:24:46 +0200), after the preceding busy refusal.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Observation continues for terminal completion or a fresh busy refusal.

## Fresh busy refusal at 02:25:13 +0200 on 2026-10-05

- The active attempt returned to `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`, latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` still `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 02:40:13 +0200, based on the waiting phase mtime 02:25:13 +0200.

## Fresh busy refusal at 02:56:08 +0200 on 2026-10-05

- Scheduled check returned to `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` remains `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 03:11:08 +0200, based on the waiting phase mtime 02:56:08 +0200.

## Fresh busy refusal at 03:11:35 +0200 on 2026-10-05

- Scheduled check returned to `waiting for busy Codex; next check in900seconds` for thread `01a0d230-6068-71d2-9768-4928682cdccf`; latest turn `01a10855-8b8a-7fa1-a7a7-30d87a0c72a1` remains `inProgress`.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Next scheduled busy check is approximately 03:26:35 +0200, based on the waiting phase mtime 03:11:35 +0200.

## Active switch phase at 03:26:37 +0200 on 2026-10-05

- The scheduled attempt advanced to `switching` (phase mtime 03:26:37 +0200), after the preceding busy refusal.
- Service remains active/running with `Result=success`, `ExecMainStatus=0`; terminal `.exit` absent.
- Observation continues for terminal completion or a fresh busy refusal.

## Terminal result at 03:27:57 +0200 on 2026-10-05

- Result: completed successfully; atomic `profile-switch-2.exit` contains `0`.
- Service properties: `ActiveState=inactive`, `SubState=dead`, `Result=success`, `ExecMainStatus=0`.
- Phase: `activated`.
- Elapsed time from log start `2026-10-04T23:04:02+02:00`: approximately 4 hours 23 minutes 55 seconds.
- Workspace revision: `88c0b957a1e870e4ce36a1743f72b529ba4825e1`.
- Selected package candidate: `/nix/store/jq982nq0jxfhmr4jxyvkglnyy77n1kxf-dev-workspace-0.2.0`.
