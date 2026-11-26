**Result: incomplete.** The driver SHA256 matches the expected value, but the operation directory and driver are owned by `aither`, not `root` as required. No `start.json` or `exit.json` exists.

I did not write the readiness receipt or observe a start because the preflight ownership condition failed. The driver was not executed.