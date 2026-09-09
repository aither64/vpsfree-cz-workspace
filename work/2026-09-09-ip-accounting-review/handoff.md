# IP accounting report

The script is in the `vpsfree-maintenance-tasks` feature branch
`2026-09-09-ip-accounting-review`, under `2026-09-09-check-ip-accounting/`.

On an API host, run from the task directory:

```sh
./check_ip_accounting.rb --output /root/ip-accounting.json
```

The new file contains JSON grouped by user, environment and IP resource. It
compares allocated IP size, confirmed/enabled resource usage, resource limits
and assigned package totals. Mismatches include record IDs for reconciliation.
Uncharged addresses appear separately. The README documents every field and
provides a jq filter for inventory overages.

Exit codes are 0 for a clean report, 2 for findings and 1 for failure. The script
uses a read-only database snapshot and refuses to overwrite an existing file.
No production execution or reconciliation has been performed.

Validation: 16 database-backed examples passed; runtime smoke checks confirmed
JSON output, exit statuses, no overwrite and database enforcement of read-only
access. Script syntax and RuboCop passed. All four mandatory review lanes are
complete. Recorded usage delegates to vpsAdmin's model. Accepted limitations
and performance evidence are in review-resolution.md.

A synthetic scan of 1,000 users with six IP resource limits each took 43.259
seconds. Production load is unmeasured: run during a quiet period and use Ctrl+C
if database load becomes excessive. This is a user-account audit; orphaned
ownership and assignment chains are outside its scope.

Final commit: `0e4531b2a9839152c74a970c472bf65a3cc3c0c9`.
The local branch and both worktrees remain available for review.
