# Scope and proportionality review

## Findings

No Blocking, Important, or Advisory findings.

## Assessment

The candidate is the smallest maintainable implementation of the user's
explicit decision to remove all three proxy overrides and the unmerged route
workaround:

- `cluster/cz.vpsfree/containers/prg/proxy/module.nix:5` retains the existing
  `nixos-stable`, `os-staging`, and `vpsadmin` channels and removes only their
  machine-local substitutions. There is no fallback, compatibility shim, or
  replacement override mechanism.
- `flake.nix:4` removes the four root inputs that existed only to support those
  substitutions. The generated `flake.lock` update removes nine unreachable
  nodes. `input-validation.json` records no added root input, no change to any
  retained root dependency graph, and a machine-mapping change only for the
  production proxy. Lock-node renumbering is generated representation churn,
  not new maintenance surface.
- The final retained series has no configuration-local password-recovery route
  or maintenance expression. The formerly copied logic is absent from
  `cluster/cz.vpsfree/vpsadmin/common/frontend.nix`, whose candidate version is
  byte-identical to configuration `origin/master`; the pinned vpsAdmin module
  at `050ea526` already owns the route and maintenance behavior. Dropping the
  workaround commit instead of retaining a revert removes the obsolete branch
  iteration from review and future history.
- Commit `0e0a985a` keeps the machine-channel correction, generated lock
  pruning, and the corresponding release-specific runbook correction together.
  That split is coherent: each part either implements the selected dependency
  resolution or documents its immediate deployment and rollback consequence.
  The retained monitoring, runbook, and generated service/template pin commits
  remain independent functional units.
- The runbook additions at
  `docs/operations/vpsadmin-password-recovery-deployment.md:25` and `:472` are
  proportional to the real shared-proxy impact. They require review of the
  system-generation diff, retention of the preceding generation, and checks of
  other proxied sites after rollback without inventing a new deployment or
  compatibility framework.
- No application tests or generalized conformance suite were added for this
  deletion. The supplied checks focus on owned behavior: all 108 machine input
  mappings, recursive retained-input resolution, the proxy toplevel
  derivation, and the three auth routes under normal and maintenance states.

## Residual validation limits

This lane reviewed committed configuration range
`a4c43133ee98057e79a3355ecb5d4bad814b4957..0e0a985ad5daa12ab5ad50fec5ac4cf55b204358`
and retained series
`8ef765d339ac792ef4f01a5c7a160e48600adcaf..0e0a985ad5daa12ab5ad50fec5ac4cf55b204358`.
It relied on the packet's completed evaluation artifacts and did not perform a
production deployment, runtime generation comparison, closure-package diff, or
final generated-Nginx inspection; those are deliberately subsequent rollout
checks. The unchanged API implementation was inspected only far enough to
confirm route ownership and was not re-audited.
