# General review

Reviewer: fresh gpt-5.6-sol / xhigh, General lane. I reviewed the committed
configuration correction and retained series directly. I did not launch
subagents, run integration tests, or mutate project, cluster, branch, or session
state.

## Findings

No Blocking, Important, or Advisory findings.

## Review evidence

I inspected correction range
`a4c43133ee98057e79a3355ecb5d4bad814b4957..0e0a985ad5daa12ab5ad50fec5ac4cf55b204358`
and complete retained range
`8ef765d339ac792ef4f01a5c7a160e48600adcaf..0e0a985ad5daa12ab5ad50fec5ac4cf55b204358`,
including every commit message and diff. The final five-commit series keeps the
monitoring rule, deployment runbook, notification-template pin, and vpsAdmin
pin as separate reviewable changes. Range-diff proves those four retained
patches are unchanged, drops only the local auth-route workaround
`b13a7a8d`/`d7792d1a`, and adds the focused cleanup commit `0e0a985a`.

The cleanup commit has one coherent purpose. It removes the proxy's three input
overrides, removes the four now-unused root baseline declarations, prunes their
nine unreachable lock nodes, and updates the release-specific runbook for the
resulting shared-proxy dependency update and rollback. Its commit message
describes the final behavior and deployment consequence. The two generated
`confctl` pin messages remain unchanged, as required by repository guidance.
There are no tracked or staged worktree changes; `.bin/rubocop` and
`.bundle/config` are untracked local tooling artifacts outside the reviewed
tree.

The input-validation evidence compares all 108 machine mappings. Only
`cz.vpsfree/containers/prg/proxy` changes, and only its selected `nixpkgs`,
`vpsadminos`, and `vpsadmin` roles change. They now resolve respectively to
`nixpkgsStable` `21a67dc4`, `vpsadminosOsStaging` `c065fa2f`, and
`vpsadminServices` `050ea526`; the notification-template pin remains
`f944ba03`. Recursive comparison shows that every retained root input graph and
revision is unchanged after lock pruning.

The final shared frontend file is byte-identical to configuration default
`8ef765d3`. The exact pinned vpsAdmin module at `050ea526` owns
`/_auth`, `/webauthn`, and `/oauth2/password-reset`. The recorded 18-result
module evaluation covers all three paths on both production and maintenance
auth hosts under normal, selected global-production maintenance, and local
instance maintenance states, with consistent proxy or 503 behavior.

The available quick checks support the committed tree: Nix formatting,
`git diff --check`, active commit hooks, strict MkDocs, full proxy toplevel
derivation evaluation, retained-input graph comparison, all-machine role
comparison, and isolated auth-route evaluation passed. The initial failed
machine-name assertion and ambient missing-gem rebase attempt were probe/tooling
issues; the corrected machine-key check and pinned development shell passed.

## Residual validation limits

The proxy toplevel has been evaluated to a derivation but has not yet been
built for this correction. The planned closure/package and system-generation
diff, actual generated Nginx inspection, and other shared-proxy workload checks
therefore remain necessary after review. No production deployment or rollback
was performed, so retention and restoration of the preceding generation and
post-rollback checks of the other proxied sites remain operational validation.
These limits are explicit in the packet and runbook and do not invalidate the
committed correction.
