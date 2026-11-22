# Native verification sandbox observations

The portal performance rollout used native CLI verification watchers on
2026-10-15. A sandbox without networking denied Unix socket connections with
EPERM. A second workspace-write sandbox with networking and an extra
/run/user/1000 writable root could reach portal.sock, but systemctl --user
failed with "Failed to connect to user scope bus ... No data available".
The parent could query the same unit. Neither attempt produced live acceptance
measurements.

A fresh native collaboration watcher inherited ordinary local service access.
Its MainPID preflight succeeded and the unchanged ten-minute probe passed.
In this case, enabling sandbox networking alone did not establish access to
all local IPC required by a verification command. The observed correction
changed the instrument context and required no redeployment.

The rollout also found that coordination finish evidence is a nonempty string;
a structured kind/path/sha256 object was rejected before mutation. The corrected
string retained the exact acceptance path and SHA256. This differs from the
structured evidence used by preparation requests.

Evidence: work/2026-10-15-portal-performance-fix/rollout.md,
live-watch-final.md, live-bus-denied.log and the retained native finish receipt.
