# CI elapsed-time correction

Authoritative run start:2026-10-29T23:50:29Z.
Both the clock tool and host shell reported2026-10-30T00:02:15Z;
programmatic datetime subtraction gives707seconds, about11minutes47seconds.
The watcher overrun note at00:00:38Z should read609seconds/10minutes9seconds,
not20minutes9seconds. The20-minute reporting threshold is00:10:29Z.
Only the watcher elapsed estimate is incorrect; its recorded run ID/head/job
statuses remain the reported read-only metadata. Continue exact-head monitoring;
no failure, cancellation or retry follows from an elapsed estimate.
