The first fresh utility check exited before running the helper fixture because
the workspace-write sandbox denied writes to Nix fetcher-cache-v4.sqlite under
/home/aither/.cache/nix. This is an execution-environment refusal, with the exact
SQLite error retained. No helper/worker assertion ran and no test retry is
accepted without that diagnosis. The next fresh same-policy utility has only
that existing Nix cache added as a writable directory, with declared network
access for Nix/user-bus APIs. Tested source and command remain identical.

The second fresh utility reached the fixture but could not communicate with
the real user bus (No data available); the private worker unit was not started.
Its exact error/stack and status remain retained. This command requires host
user-service execution, unavailable in the fallback CLI sandbox. The native
delegation interface is already unavailable; parent now uses the skill's
visible minimal-output monitoring fallback with the same source/command.
No source fix, protocol bypass, assertion change or generic green retry.
