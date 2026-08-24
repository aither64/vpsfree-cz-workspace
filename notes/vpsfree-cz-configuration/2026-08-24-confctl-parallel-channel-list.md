# Run confctl channel inspection serially

## Symptom

Running several `confctl inputs channel ls` commands concurrently in one
configuration worktree can print the correct channel mapping and still exit
nonzero. The invocations contend on the shared Nix evaluation cache, Bundler
state, and second-granularity `.confctl` log paths.

## Workaround

Run channel inspection commands sequentially when their exit status is used for
verification. After a concurrent failure, rerun the affected channel alone and
use that result.

## Verification

Sequential inspection of the `vpsadmin`, `staging`, and `production` channels
all succeeded for `work/2026-08-23-vpsadmin-supervisor-issue/`.
