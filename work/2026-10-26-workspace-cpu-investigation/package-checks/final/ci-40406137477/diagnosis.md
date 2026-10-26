# Archive CI failure and bounded fixture correction

Owner: implementer2. Failed head:
`f23e717c2fa33803d889414b243591c9a97846d6`.
Correction: `fffbd0d59fffc09667cb39878d9f7da8bdcd3806`.

## Evidence and cause

Full failed job [archive-job.log](archive-job.log) was downloaded from archive
job `121864252338` in [run 40406137477](https://github.com/aither64/dev-workspace/actions/runs/40406137477).
[run.json](run.json) binds the exact head and job conclusions. The artifacts
API returned zero artifacts; its complete result is [artifacts.json](artifacts.json).

The first archive scenario successfully creates the managed session and its
worktree. It then spends 900.20 seconds in the **pre-browser** direct
`workspace-portal thread require-idle` loop. Every attempt rejects its submission
storage with `decode queue attempt ledger: json: unknown field "storage"` and
`delivery stage=legacy-ledger-load ... failed=true`. See log lines 4374–4395
for initial failures and 7758–7762 for the final traceback.

The direct helper omitted `--user-state-root`. `threadCommand` passes that
explicit empty flag value to `newCodexClient`, which selects the socket-adjacent
schema-3 JSON path and no submission database. The running portal uses the
selected private SQLite database. Its migration fences the predecessor JSON
path with a schema-4 record containing `storage` and the database path. A helper
reading that fence as a schema-3 ledger correctly refuses it. Retrying cannot
repair the mismatched storage selection.

The ordinary Ruby idle-check caller already supplies its selected state root.
The VM direct helper did not. The invocation and storage-selection code are
unchanged between 0fd31 and f23; upstream deed45f0 adds later directory-removal
coverage, after this gate. The CPU scheduling/cache paths and archive execution
are not reached in this failing step. This is a fixture invocation defect,
not evidence that the fail-closed storage reader should accept the marker.

This differs from the earlier local 0fd31 browser hydration timeout. Its exact
cause remains unproved; this failure does not explain or reproduce it.

## Correction and focused proof

The VM helper now receives `--user-state-root` with the existing fixture's exact
state directory. There is no production, storage-format, migration, timeout,
native version or dependency change.

The regression test reuses `threadCommandAppServer` and the actual `threadCommand`:

1. An actual selected client reserves a prepared send in SQLite, creating the
   real legacy migration fence.
2. The helper with no state root reproduces the exact unknown-`storage` error.
3. The helper with the selected state root sees the current unresolved receipt
   and refuses to claim the conversation idle.
4. After discarding that exact unsubmitted fixture receipt, the same selected
   helper proves the otherwise-idle conversation idle.

Quick checks passed before commit:

```sh
nix develop --no-update-lock-file --command go -C portal test -mod=readonly \
  ./cmd/workspace-portal \
  -run '^(TestThreadRequireIdleUsesSelectedSubmissionStorage|TestExplicitArchiveCommandSavesQueueInSelectedPrivateStorage)$' \
  -count=1 -v -timeout=30s
```

Both tests passed, package elapsed 0.182 seconds. `nix-instantiate --parse` on
the VM expression and `git diff --check` also passed. The two-file correction
contains 54 insertions and one deletion. Commit used the shared Git flock,
owned paths only and normal unbypassed hooks; the index and checkout are clean.

## Remaining verification

No long VM, build, rerun, push, rebase, consumer refresh or deployment was
launched. The lead owns narrow-fix review and one targeted archive VM check:

```sh
nix build --no-link --print-build-logs .#checks.x86_64-linux.session-archive-lifecycle
```

Run it through the required verification watcher after the lead's review. It
must exercise browser archive, repair/restart and revival after the corrected
storage gate. A previous green archive run is not a substitute for this fix's
targeted acceptance. Reuse existing exact-input checks for unaffected scope
according to the lead's receipts. The old browser diagnostic overlay remains
available only if this targeted run exposes a separate tracing gap.
