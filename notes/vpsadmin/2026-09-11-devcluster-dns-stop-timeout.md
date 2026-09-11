# Development-cluster DNS shutdown delay

Related initiative: `work/2026-09-11-devcluster-packaging-investigation/`.

`vpsadmin-devcluster stop <slug>` can take several minutes because the DNS
VMs wait for the vpsAdmin node-control daemon's 90-second systemd stop timeout.
Observed on the retained-data acceptance cluster before the final runner switch.
The runner stopped services, node1, dns-secondary and dns-primary in order;
shutdown completed successfully and retained disks. Whether stopping the services
VM first causes the daemon delay is unconfirmed. Wait for the normal stop command
instead of assuming a stuck helper or resetting the cluster. This is separate
from package evaluation and startup readiness.

The provider's total stop window is120 seconds, shorter than two sequential
90-second DNS service stops. It then terminates the runner and owned socket
processes and reports `killed after timeout`, returning0. That path can retain
stale PID/readiness files even though status reports stopped. Repeat the stable
stop command to clear stale markers; it retains disks. The final retained-data
restart passed after a preceding timeout stop. A separate shutdown fix should
coordinate guest service ordering/timeouts and the provider's total deadline.
