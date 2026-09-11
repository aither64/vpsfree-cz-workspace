# 2026-09-11-devcluster-packaging-investigation

## Goal

Investigate the packaged development-cluster startup failure reported by
2026-08-18-vpsadmin-password-reset and suggest concrete solutions covering both
vpsAdmin and vpsAdminOS. This is diagnosis and repair design, not implementation
or deployment of a provider change.

## Affected repositories

- vpsfree-dev-workspace: packaged providers, nested flakes, runner library,
  package construction and tests (primary suspected owner).
- dev-workspace: stable command dispatch and package-generation contracts.
- vpsadmin and vpsadminos: inspect source/input and test-runner interfaces as
  needed to distinguish application defects from packaging defects.
- Shared workspace: this initiative's tracking and investigation evidence only.

## Approach

Inspect retained failure logs and the exact installed package, trace both
providers through configuration and runner construction, reproduce failures
without touching another session's cluster, and evaluate repair alternatives
with isolated local probes. Record remaining runtime validation explicitly.

## Compatibility and deployment

No production, API, database, protocol, VM disk, or configuration changes are
authorized by this investigation. Proposed repairs must preserve current cluster
state schemas, recorded sockets/ownership, stable dispatcher locking and
generation checks, host-supplied defaults and mixed package transition rules.
No coordinated vpsAdminOS node update should be necessary for packaging repairs.
Any later live test must use its own cluster and bridge networking and avoid
unintended kernel builds. Do not reset or adopt password-reset state.

## Testing plan

Inspect both exact installed payloads; evaluate their Nix expressions and runner
package construction with existing pinned inputs without building VMs; run
relevant existing fast tests; use temporary standalone source copies if useful
to prove proposed path/configuration repairs. A passed package build alone does
not prove either provider starts. Document any untested live lifecycle steps.
