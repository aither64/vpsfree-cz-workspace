# Package and protocol validation

The final consuming workspace at `9edf553` builds as:
`/nix/store/prpvck3v35xbvyz60gfwprz9p3lsagal-dev-workspace-0.2.0`.
It selects runtime `d3bfd0f`, organization `a30de6c`, provider `8377021`
and Codex 0.154.0.

The Nix package build passed every Go package, 296 Ruby tests with 2,979
assertions and 73 host tests with 438 assertions. There were no failures or
errors; the Ruby suites reported 12 and 3 declared environment skips. The
installed protocol coverage check passed during packaging. The installed
`workspace-host check-codex --codex <package>/libexec/codex/bin/codex` then
passed the full experimental schemas and model defaults for Codex 0.154.0.

The new plan-goal regression runs actual Ruby read_goal and verifies recovery
of an older raw frozen receipt. Focused Go race checks passed in 1.912 s;
broader creation/fork/plan race coverage passed in 32.353 s. General and risk
review of that committed delta found no issues before the final package build.

## Full generic and host validation

The complete generic `nix flake check --print-build-logs` passed on runtime
`f2512c1` with provider `8377021`. Its host-module idempotency VM passed in
321.90 s, covering configuration changes and rollback, certificate renewal,
authentication, and retained certificate/password state. It used cached kernel
artifacts. Later commits add the activity route alias, install all sources
required by the existing protocol checker, and align portal goal hashes with
the unchanged CLI. They do not change the host-module or lifecycle contract,
so the VM was not repeated. Each later consuming package passed its full
Go/Ruby/host build suite.

The selected Codex 0.154.0 binary also passed the provider's actual fresh-thread
contract in 1.254 s. That check owned an isolated temporary Codex home and
cleaned its probe process/data. The provider and Codex pin did not change in
the later runtime repairs.

All four feature worktrees were clean after explicit origin/master fetches,
and their current heads contain the fetched default branches. Features remain
unmerged. All owned acceptance fixtures and temporary package/browser GC roots are
removed; installed profile29 retains the deployed package. Deployment and real creation results are in
`deployment-results.md` and `creation-integration-results.md`.
