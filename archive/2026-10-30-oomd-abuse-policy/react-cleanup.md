# React reproducible-data cleanup

Authorized bounded cleanup completed after the application/check package finished.
No tests, builds, npm install, GC, shared cache removal or lifecycle action ran.
The lead explicitly accepted package/own-process reference scope after unrelated
root processes could not be inspected. The own-package scan found zero live
cwd/executable/fd/mapped-file references. Three protected same-UID services did
not reference the package and remained outside that scope. Removals ran as the
ordinary user; no further privileged scan was attempted after lead direction.

Exact allocated bytes removed:

- Frontend `node_modules` including its Vite/cache output, BFF `node_modules`
  and generated `dist`: 314,359,808 bytes.
- Corrected browser report/results duplicates and ignored non-Markdown assets
  from the original browser report: 7,049,216 bytes.
- Three now-unused cleanup/proc-scan/inventory helpers in `/tmp`: 20,480 bytes.
- Total: **321,429,504 bytes**
  (306.539 MiB).

Every removed repository/session artifact was checked as ignored and untracked;
no top-level candidate was a symlink. No broad Git clean/reset was used. Exact
paths and allocation values are retained in
[the receipt](react-verification/cleanup-receipt.json).

All committed PNGs/docs, all log/JSON/patch/review receipts, the two original
report Markdown diagnosis copies and original failed browser results remain.
The latter retain 6,234,112
allocated bytes. Preserved files passed before/after SHA-256 comparison.
Generated HTML reports no longer exist; retained failure traces can be opened
again with a subsequently installed browser toolchain if needed. Existing
historical report-directory links describe disposed reproducible output.

`df -B1` for `/dev/vda1`, before removal:

```text
Filesystem         1B-blocks         Used       Avail Use% Mounted on
/dev/vda1      1055740375040 953696575488 48340045824  96% /
```

Immediately after payload removal:

```text
Filesystem         1B-blocks         Used       Avail Use% Mounted on
/dev/vda1      1055740375040 953375408128 48661213184  96% /
```

Final observation after helper removal and receipt preservation:

```text
Filesystem         1B-blocks         Used       Avail Use% Mounted on
/dev/vda1      1055740375040 953386934272 48649687040  96% /
```

Filesystem free-space changes also include concurrent writes/removals elsewhere;
the allocated path inventory above is the exact owned cleanup accounting.

Source proof: HEAD `b67c7917e8758e707e0b88512f055eab9fbd8529` and tree `ce3b38c9ba4245e363dab48f8a8cc63882c90791` match before
cleanup, `git status --porcelain=v1` is empty, all removed payload paths are
absent, and preserved hashes are unchanged. PR115, branches, worktree
registration and session lifecycle remain intact. No implementation scope added.
