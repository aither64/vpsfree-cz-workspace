# Visibility quick3 packet

Quick2 Ruby syntax and scoped lint passed. Core API bootstrap stopped before
any examples because the tracking TMPDIR made MariaDB's mysql.sock path exceed
its 107-byte limit; full mode did not run. Root supplied that diagnosis.

The only harness change is export TMPDIR=/tmp, with no tracking temporary-directory
creation. The existing automatic test helper owns its unique atomic temporary
directory, free port, startup and normal-exit shutdown/prune. Product code,
resource specs, docs, tools/test_db.rb and all quick1/quick2 artifacts are unchanged.
Logs and native RSpec JSON remain under this session's tracking directory.

After root inspection, run:

```bash
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/visibility-quick3.sh
```

The wrapper checks the same source guard and source hashes before and after,
requires quick2's passing lint receipt, and runs only the five complete resource
specs in core mode (seed 36954) then full mode (seed 9346). It retains explicit
Nix shell routing, per-step logs/status, aggregate logs/status, native JSON and
stop-on-first-failure behavior. No old scratch or artifact cleanup is requested.
The implementer has not launched this packet or claimed API results.
