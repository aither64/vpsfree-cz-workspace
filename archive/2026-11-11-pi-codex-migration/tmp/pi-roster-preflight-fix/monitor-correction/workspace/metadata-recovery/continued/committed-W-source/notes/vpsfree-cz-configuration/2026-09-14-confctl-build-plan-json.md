# Read buildPlan directly for machine-readable validation

Parsing the JSON printed inside a confctl build log failed with an unterminated
string at roughly 16 KiB. The logger splits long subprocess output into chunks,
so a single log line does not necessarily contain one complete JSON object.

Evaluate directly in the configuration worktree instead:

```sh
nix eval --json --impure --no-write-lock-file --no-update-lock-file .#confctl.buildPlan > /tmp/vpsadmin-build-plan.json
```

Read that file and filter the intended consumers before recording their input
roles and exact revisions. This verified all 11 vpsadmin channel consumers at
the selected feature pin. Keep the unfiltered full plan transient.

Related initiative: work/2026-09-14-kernel-history-fix.
