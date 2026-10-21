# Configure RainerScript omfile creation permissions on the action

Pinned rsyslog8.2608.0 did not apply legacy FileGroup/DirGroup/DirCreateMode defaults
to action(type="omfile" dynaFile=...). A real VM created fresh directories0700
root:root and files0640 root:root, denying the intended reader despite the globals.

Set fileOwner, fileGroup, fileCreateMode, dirOwner, dirGroup and dirCreateMode
explicitly on that RainerScript action. Retain legacy defaults for a legacy local
messages selector. Syntax checks with all groups substituted to root cannot prove
actual ownership; mapped actual-reader-GID probes and VM checks are necessary.
Native probes verified fresh paths0750/GID100, files0640/GID100, messages0640/GID100,
and a distinct exporter pipe0640/GID200 unchanged. Existing metadata stays unchanged,
so historical permission reconciliation remains a separate operator action.

Evidence: work/2026-10-21-aitherdev-observability-access/logger-permission-diagnosis.md.
