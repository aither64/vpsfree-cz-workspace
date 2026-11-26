Result: **failed**, wrapper exit status 1. No VM runner launched.

The source helper and cache preflight passed. Both fixtures mapped to the required node gem, and the exact selection command exited 0. The wrapper then stopped at the resource gate: **“insufficient current VM envelope.”** The test runner did not start.

Tested head/tree: `eb8d111b6e0c318336b818aabeacc3d575ac3279` / `84a4bded3a29dc0789723574212638fcf38b8935`.

Evidence: selection log `/tmp/backup-disable-storage-eb8d111b-run3-selection.log`; authoritative receipt `/tmp/backup-disable-storage-eb8d111b-run3-exit.json`. All wrapper phases joined; receipt reports no remaining owned effects.