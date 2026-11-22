# Browser route changes need a real interface fixture

The networking browser fixtures were designed for form inspection and create
VPS/interface rows without node runtime. Submitting a real assignment in the
IP release scenario reached RouteAdd, which failed because nodectld's VPS config
had no interface; rollback failed for the same reason. SQL diagnostics linked
the browser attempt to the failed node transaction.

Reuse prepare_webui_storage_runtime to create the one stopped test container,
then create its interface through VethRouted::Create so both nodectld config and
osctld agree. Update the browser fixture ID and wait for the setup chain. Assert
the assignment notification and wait for its transaction to settle before
checking server-rendered protection. Do not replace real node work with a direct
assignment SQL update.

The test runner removes guest disks during normal shutdown, even after failure.
A trace path printed only inside the guest may therefore be lost; consult the
embedded error context and node/SQL diagnostics in retained shell logs.
Related initiative: work/2026-09-09-ip-release-mechanism.

Verification: all5 networking/DNS Playwright tests passed on1e2d2d7c9, including
node-confirmed assignment and subsequent forced campaign release protection.
