# Architecture and repetition review

Reviewer: fresh `gpt-5.6-sol` / `xhigh`, architecture-and-repetition lane. I
reviewed the committed configuration correction directly, including the exact
candidate and both packet ranges, repository rules, retained commit series,
input/channel composition, the pinned vpsAdmin frontend provider, representative
consumer configuration, and supplied validation artifacts. I did not launch
subagents or modify project repositories, branches, clusters, or sessions.

## Findings

### Blocking

No findings.

### Important

No findings.

### Advisory

1. **The runbook describes the proxy rollback twice with different target
   terms.** Commit `0e0a985ad5daa12ab5ad50fec5ac4cf55b204358` adds an
   instruction at
   `docs/operations/vpsadmin-password-recovery-deployment.md:472-476` to restore
   the retained pre-rollout system generation. The existing continuation at
   lines 491-495 then instructs the operator to roll the proxy frontend back to
   the approved preceding configuration together with the WebUI and API hosts.
   The section does not identify these as alternative partial/full rollback
   branches or establish that the two targets are identical. An operator can
   therefore interpret them as two proxy deployments, while a later runbook
   edit can update one rollback target or ordering rule and leave the other
   stale. This proxy carries unrelated sites, so the ambiguity concerns more
   than the password-recovery route. Consolidate this into one proxy rollback
   step, name its exact target and intended position relative to the API masks,
   and keep the other-site verification with that single step.

## Architecture assessment

The implementation otherwise improves ownership and removes repetition. The
proxy declares only the normal `nixos-stable`, `os-staging`, and `vpsadmin`
channels in
`cluster/cz.vpsfree/containers/prg/proxy/module.nix:5-9`; `flake.nix:87-114`
owns their central mappings. The consumer import in
`cluster/cz.vpsfree/vpsadmin/common/all.nix:8-15` derives the vpsAdmin module
from the machine-selected input. At pinned vpsAdmin head `050ea526`,
`nixos/modules/vpsadmin/frontend.nix:246-289` is the single owner of auth route
and maintenance behavior, including `/oauth2/password-reset` at lines 269-273.
The configuration tree contains no local copy of that route or maintenance
predicate; dropping `d7792d1a` removes the former second owner.

The four obsolete root baseline declarations and their unreachable lock nodes
are removed together with the only machine override that consumed them. The
supplied `input-validation.json` checks all 108 machine mappings, reports only
the proxy's three intended role changes, and reports identical retained input
graphs. The retained route, monitoring, runbook, and generated pin commits are
otherwise preserved as shown by `rebase-range-diff.txt`. I found no new
registry, hidden extension interface, speculative abstraction, or repeated
configuration rule that needs extraction.

## Residual validation limits

This was a read-only static review; I did not run builds or integration tests.
I relied on the packet's passing full proxy toplevel evaluation, recursive lock
graph comparison, and 18 isolated auth-route/maintenance checks. Those checks
exercise both auth hosts and the three maintenance modes, but they do not yet
inspect the final generated nginx configuration from the built proxy closure or
exercise an actual proxy generation switch/rollback. The packet intentionally
leaves that inspection for the post-review build and leaves production rollout
to the operator.

