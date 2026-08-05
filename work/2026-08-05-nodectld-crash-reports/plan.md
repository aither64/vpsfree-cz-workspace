# 2026-08-05-nodectld-crash-reports

## Goal

Analyze all nodectld Ruby crash reports under
`tmp/nodectld-crash-reports/`, separate distinct failure signatures and
software builds, identify the most likely root cause(s), and recommend
concrete, testable fixes at the correct layer.

## Affected repositories

- `vpsadmin`: add a local package overlay for MariaDB Connector/C so every
  vpsAdmin service using mysql2 is rebuilt against a fixed client library.
- `vpsadminos` and nixpkgs are compatibility inputs only. No change is needed
  there because vpsAdmin already owns an overlay applied to its deployed
  services.

## Approach

1. Inventory every report by node, time, Ruby/mysql2/Connector-C build,
   signal address, native stack and Ruby call path.
2. Cluster reports into independent signatures and check for evidence of
   corruption or unsafe connection sharing in other threads.
3. Map native instruction offsets to the exact Connector/C source and compare
   relevant upstream fixes/releases.
4. Inspect nodectld database connection ownership, fork/thread lifecycle and
   mysql2 native calls for a trigger that explains the corrupted state.
5. Upgrade MariaDB Connector/C in the vpsAdmin overlay to the latest upstream
   release. Document CONC-709 and remove the override when the pinned nixpkgs
   provides that release or newer.
6. Build the overlaid connector and mysql2 consumer, then run the official
   malformed-metadata reproducer against both vulnerable and fixed clients.
7. Commit the package fix, run mandatory change review, and then run the
   appropriate integration validation.

## Compatibility and deployment

- Treat nodes as potentially mixed-version until the reports prove otherwise.
- A nodectld-only workaround should remain compatible with old/new API and
  database servers and must not change persisted state.
- A Connector/C, mysql2 or Ruby package fix requires a vpsAdminOS/system
  rebuild and rolling nodectld restart, but should not require coordinated
  updates of all nodes if protocol and schema behavior are unchanged.
- Any package upgrade or backport must be checked for ABI compatibility with
  mysql2 and rollback compatibility with the previous system generation.

## Testing plan

- Verify the report classification mechanically against all files.
- Reproduce or exercise the crashing query/result path under the exact old
  package versions, preferably with ASan/UBSan or valgrind where practical.
- Exercise MariaDB's official focused reproducer against both vulnerable and
  fixed packages. Do not vendor the third-party protocol reproducer into
  vpsAdmin CI; verify the package closures and keep the parser regression in
  its owning Connector/C project.
- If code is changed, run repository-local hooks and quick tests, commit the
  intended changes, then run mandatory change review before long integration
  tests as required by the workspace instructions.
