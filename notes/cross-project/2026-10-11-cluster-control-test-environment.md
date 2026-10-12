# Cross-project provider test environment

Running extension Ruby provider tests inside the generic runtime's Nix shell
does not inject extension defaults. Status exits before JSON with a missing
VPSADMIN_DEVCLUSTER_DEFAULT_CONFIG error. Export both provider default config
paths from the extension's test/fixtures plus DEVCLUSTER_RUNTIME_CONTRACT and
DEV_WORKSPACE_RUNTIME_CONTRACT from the selected runtime. This matches the
extension flake's testEnvironment. The corrected status cases passed.

Build selection is passed to Nix through provider-specific TOPOLOGY and NETWORK
environment variables, rather than positional build arguments. Tests should
observe that environment when asserting retained selection.

Creating a configuration worktree can fail after checkout when the shared
Overcommit hook runs outside its Nix shell. Keep the created checkout and retry
registration, then run bundle check, bundle exec overcommit --install and
bundle exec overcommit --sign inside nix develop before committing. Do not
bypass the hooks. This setup succeeded for the initiative.

Related work: work/2026-10-11-cluster-controls/.

During integration, the configuration's pre-push hook also refused when Git ran
outside its Nix shell, with the same missing Bundler gems. Repeating the exact
push through the configuration's nix develop ran the hook normally. Checkout,
merge and push all need that environment; no hook was bypassed.
