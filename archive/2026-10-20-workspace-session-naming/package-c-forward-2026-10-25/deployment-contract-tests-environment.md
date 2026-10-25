# Optional checker tests: unsupported environment invocation

The owning repository is the coordination workspace, at
`worktrees/2026-10-20-workspace-session-naming/workspace`.
`test/deployment_contract_test.rb:5` requires `minitest/autorun`.
The declared test environment is `flake.nix:70–80`: the workspace's
`checks.x86_64-linux.deployment-contract` derivation takes `pkgs.ruby`, copies
its source, makes it writable, patches bin shebangs, then invokes
`ruby source/test/deployment_contract_test.rb`.
A scoped source/documentation search found no separately documented direct
quick invocation for that suite.

I instead invoked the test through the configuration repository's Nix shell:

```sh
# Incorrect environment for this workspace test; do not repeat.
nix develop --command ruby /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-workspace-session-naming/workspace/test/deployment_contract_test.rb
```

Its cwd was `worktrees/2026-10-20-workspace-session-naming/vpsfree-cz-configuration`.
That repository declares Ruby3.4 via devPkgs and a tools shell, with an RSpec-based
Gemfile that does not declare minitest. The active Ruby3.4.9 environment could not
load minitest/autorun. The preserved [failed log](deployment-contract-tests.log)
shows the LoadError before any test ran; the recorded exit is1 in4.246s.
This does not establish a failure in the owning declared check, nor a product
regression. It is not recorded as a pass. No dependency install, environment
override, framework/source edit or repeated failing invocation was attempted.

The declared owning command for a later separately authorized utility is:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-workspace-session-naming/workspace
nix build --no-link --no-write-lock-file --print-build-logs .#checks.x86_64-linux.deployment-contract
```

This is a new derivation realization/source-copy operation of uncertain duration,
not a known-quick direct interpreter invocation. It was not launched under the
source-only package; the sole current utility owns independent A/B verification.
Main chooses its future release/watcher. The actual final-lock checker
`bin/check-dev-workspace-deployment --workspace-root ... --configuration-root ...`
already passed in the configuration Nix shell, as did required Nixfmt and semantic
graph checks. These distinct required checks are recorded in quick-checks.json
and semantic-lock-proof.json. Source publication does not imply readiness.
