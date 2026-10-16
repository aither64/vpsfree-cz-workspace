# Declared payload: unapplied proposal

Prepared only in this session directory. Product remains clean at
`edb90d2fe2190d88d8b9d2d21bd0def79eedc898`, tree `66674e848f160c5dc7be63da6e14c590ef043ec5`; index untouched. Verified
current session and retained roster18 implementer0 Sol/xhigh/workspace_write;
both environment identity markers absent. Reused unchanged required workspace
procedures, read product AGENTS/policy and decision.md, and confirmed unchanged
accepted design SHA256 c80fea979d8fe48c48d98b78a81b21dd8ea596e31d0c45e8eda296abdb1382b9.
No product patch was applied while parent runtime43016 remains active.

`proposal.patch` targets only
`tests/suite/dist-config/nixos-persistence-upgrade.nix`, after the existing
oldInitial switch and before first payload creation. It adds one
`lib.optionalString (variant.layout == "declared")` block; deleting that exact
insertion restores the complete prior suite byte-for-byte. Other script bodies,
all snapshots/assertions and every production/fixture definition are unchanged.

Guards require exact /guest-backing and payload target mountpoints, correct
/persistent/backing identity, directory shape, and payload source/target -ef.
Separate find-H calls inspect source and target with min/maxdepth1, including
hidden entries. Each command substitution explicitly propagates find failure;
both outputs must be empty. Only after those guards does install-d-m0750 use
the live preservation-test user/group names on the one target. No hardcoded
account ID, recursive metadata operation, source replacement, mount/service
change or allocation-state/map/data mutation is included. Device+inode is
captured before install and compared afterward, followed by source/target
identity again. The mountpoint object must remain unchanged.

Patch SHA256 `c9b191a7c762a8c3fd43092faa6b13951b23e47f8029ddbcff2f5bb9443ad980`.
Original suite SHA256 `6ee1209f09242bb3876514377365f23811e41a6dd91e63c3f4be895f89ec57e8`.
Proposed suite SHA256 `f70b6a6ab9dacf62e453e0716316411a17a4abc8148f283425a14c9eb8c107c9`.

Only proposed static checks ran: prepared nixfmt--check, Nix parser (no
evaluation), prepared Ruby-c on combined static suite with inert placeholders,
and bash-n on the proposed guest fragment. All passed; exact commands/results
are in static-checks.log/.json. No tests, callbacks, harness, guest fragment,
Nix evaluation/build, runtime, hooks, staging, refs, commit, push, nested agent
or failed-guest action was launched. The current product suite still exactly
equals before.nix and product status/index remain clean.

The proposal is frozen for lead inspection. Product application requires the
explicit follow-up after the immutable runtime is terminal. Parent owns actual
generated script evaluation, dependent checks, folding/review/publication and
new declared-backing runtime acceptance. These static checks establish syntax,
not guard execution or guest success.
