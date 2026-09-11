# Mandatory change review packet v40

## Requested outcome and acceptance criteria

Review the final four-layer component split and its quiesced, reversible
namespace cutover:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` independently pins the same generic runtime for the
privileged host module. The tracked trees of both generic repositories must
contain no case-insensitive `vpsfree` or `aitherdev` name. Workspace domains,
display data and provider selection belong only to each registered root's
`.dev-workspace.json`; reusable packages must not provide a second authority.

Acceptance requires immutable construction, strict provider/consumer
contracts, independently meaningful commits, byte-accurate retryable
forward/reverse migration, and an operator order which excludes mixed old/new
runtime processes and concurrent writers.

Initiative: `2026-09-09-workspace-components`

- Plan: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/plan.md`
- State: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/state.md`

| Component | Worktree | Base | Exact pushed head |
|---|---|---|---|
| `codex-web` | `worktrees/2026-09-09-workspace-components/codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `7a05da0cd79b19f3c9a0a8fa23b7043a1f984d4e` |
| generic `dev-workspace` | `worktrees/2026-09-09-workspace-components/dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `00e637534ed09fcfa5303e89e4dd9305d57baa33` |
| organization `dev-workspace` | `worktrees/2026-09-09-workspace-components/vpsfree-dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `c4bcc881d75f3bfe0ff886151f86d3671a895dde` |
| workspace | `worktrees/2026-09-09-workspace-components/workspace` | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `4ed7d7c342c86cf5e640f266c74334a4c3cd9e35` |
| configuration | `worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration` | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `83dc833882f4ece00f1db9748cffa53f713c82f2` |

All five worktrees are clean, `git diff --check` passes and each exact head is
pushed. The immutable workspace compatibility bridge is
`701f8cdba7728e83921e5a720ff08cd4f8c60bfe`; the final workspace flake does not
export it.

Exact dependency pins are:

```text
workspace@4ed7d7c -> organization@c4bcc88
  -> generic@00e6375 -> codex-web@7a05da0

configuration@83dc833 -> generic@00e6375 -> codex-web@7a05da0
```

## Review v39 findings and remediation

- General found that the new organization repository still selected its dated
  feature as GitHub's default branch. A neutral `master` exists. The attempted
  administrative correction failed with HTTP 403, so the explicit decision is
  to accept this repository-metadata deviation for this deployment and require
  a repository administrator to select `master` later. Exact consumer pins and
  runtime behavior are unaffected.
- General found stale wording in generic commit `27cf51d`. The unmerged history
  was rewritten; `897c100` now describes only the extension boundary it owns.
- Architecture found unrestricted namespace `gsub` could rewrite sibling
  prefixes. The organization migration now rewrites only an exact declared
  root or its slash-delimited descendants. Regression coverage includes exact,
  descendant, sibling-prefix and embedded-string cases.
- Architecture and Risk found the occupied target inventory was not
  independently reproducible. The organization repository now contains
  `docs/test-recovery-inventory-20260911.tsv`, covering every path, type, mode,
  numeric owner/group, size, mtime, link target and regular-file hash. The
  runbook compares before and after the atomic rename and checks aggregate hash
  `7a820b2d31468f9d8f546feec7d8f8cf96ddfe1ee0ee62f34bbd1f5057b2d990`.
- Scope found a now-unused packaged workspace-configuration interface. It has
  been removed from the generic catalog, organization package and workspace
  consumer. The registered root is the sole configuration authority.
- Risk required browser admission to close before idle validation, privileged
  certificate writers to stop before host preflight, and both conditions to be
  maintained through forward and reverse operations. The runbook now stops and
  verifies the router first, stops all non-tmux user writers, stops and verifies
  the root certificate timer/service, and proves no substrate reconciler
  remains. Rollback mirrors these barriers.
- Risk required exact recovery actions for current legacy state. The runbook
  records the audited stable package path, all three cluster slugs to reset,
  all five sessions to restart for tmux identity initialization, all ten
  sessions to quiesce, and postcondition checks.
- Risk required a complete host-layout regression. New NixOS VM check
  `host-migration` constructs real pair-based host state, converts it to the
  deployed old layout, snapshots content and ownership, runs actual forward
  migration and the new reconciler, then reverses and compares the exact
  original snapshot and key material.

These remediations changed every reviewed boundary, so all four lanes are
rerun from fresh context for v40.

## Ownership and intended commit boundaries

- `codex-web` owns reusable Codex App Server conversation integration and its
  browser/client protocol. Its seven feature commits separate moves, policy,
  persistence, integration, documentation and generic-name enforcement.
- Generic `dev-workspace` owns sessions, portal, profile, host module,
  extensions and the generic authority/tmux contracts. Test implementations
  are standalone files wired by `flake.nix`. Extension validation, activation
  aliases, namespaces and tmux metadata remain in distinct owning commits.
- Organization `dev-workspace` owns vpsFree commands, skills, providers, site
  validation and the private one-time migration helper. Its initiative tail is
  policy, package, schema-5 migration, GitHub workflow and site validation.
- The workspace owns repository policy, concrete site data, bridge/final
  selection and cross-repository deployment proof. Its commits separately own
  registration, configuration, package consumption, source removal, bridge,
  final namespace and deployment verification.
- Configuration owns privileged host values and activation. Its four commits
  are channel declaration, one generated exact input pin, host-module adoption
  and aitherdev defaults. The newest `confctl` message is unedited.

The organization repository retains filtered predecessor source provenance;
those commits predate the initiative tail and do not affect the final tree.

## Public interfaces and consumers

Generic runtime variables use `DEV_SESSION_*`, `DEV_WORKSPACES_*`,
`DEV_WORKSPACE_*`, `DEVCLUSTER_WORKSPACE` and `DEV_SESSION_LIFECYCLE_*`.
Generic tmux options use `@dev_session*`. Package construction exposes commands,
skills and cluster providers only. The organization package is the current
consumer; the workspace and configuration pin its generic provider revision as
shown above. The workspace registry stores a resolved domain snapshot derived
from its root configuration.

## Compatibility and deployment assumptions

This is an intentional one-time incompatible namespace change. Mixed old and
new runtime clients are unsupported. All conversations must be idle, all
lifecycle transactions absent, all three development clusters reset, browser
admission closed and every non-tmux writer stopped before migration.

Migration preserves paths, bytes, modes, ownership, credentials, TLS material,
profile generations, tmux sessions/windows, authorities and portal manifests.
Opaque identifiers and arbitrary serialized strings are not globally
rewritten. No schema-5 migration journal has been deployed, so it has no older
new-format upgrade target. Compatibility, final and previous generations plus
both journals remain available through acceptance and rollback verification.

The user authorized aitherdev deployment, Codex-session restarts and resetting
the current development clusters. Configuration deploys directly from its
feature worktree and is not merged. The final user profile must be built from
the registered shared workspace root, which requires that reviewed workspace
feature to fast-forward into shared `master`; that integration is still an
explicit approval boundary.

The target user namespace contains only the 11 inventoried test-recovery roots
described above. They are preserved by exact same-filesystem rename and never
deleted or merged. The privileged host migration runs only while certificate
renewal and the reconciler are stopped. The exact operator order and reverse
procedure are in `vpsfree-dev-workspace/docs/namespace-migration.md`.

## Quick verification

- All worktrees are clean and pass `git diff --check`.
- Correct tracked-file scans remain empty for case-insensitive `vpsfree` and
  `aitherdev` in both generic repositories and for `aitherdev` in the
  organization repository.
- Generic `workspace_host_test.rb`: 73 runs / 453 assertions, no failures.
  Its flake passes complete no-build evaluation.
- Organization migration: 43 runs / 831 assertions, no failures. Its flake,
  including the new VM derivation, passes complete no-build evaluation.
- The committed recovery manifest exactly matches the live target tree and its
  aggregate hash.
- Workspace deployment tests: 2 runs / 9 assertions. Its flake passes no-build
  evaluation. The real cross-worktree checker proves matching portal domains
  and generic revision `00e6375`.
- Configuration was updated only through
  `confctl inputs channel set --commit`; Nixfmt and hooks passed, transient
  `.bin`/`.bundle` files were removed, and its flake passes no-build evaluation.
- Exact `codex-web` Actions run `34555724208` passed. Exact-head generic run
  `34564353768` and organization run `34564709694` are in progress. Superseded
  organization run `34561021962` accepted cancellation; the token still returns
  HTTP 403 when cancelling superseded generic run `34560736452`.

Long full flake builds, both NixOS VMs, bridge/final package builds, aitherdev
build and dry activation remain deferred until this review is clean.

## Review disposition and risk

Overall risk is **High** because the change affects persisted user/root state,
credentials and TLS, systemd/tmux ownership, destructive migration, public
cross-project contracts, deployment order and rollback. Run General,
Architecture, Scope and Risk with fresh `gpt-5.6-sol` reviewers at `xhigh`.

General should verify final commit boundaries, generated-message handling and
documentation. Architecture should verify contract ownership and removal of
the second workspace configuration authority. Scope should verify that v39
remediation did not retain obsolete compatibility surface. Risk should verify
exact namespace replacement, recovery inventory, quiescence, privileged writer
barriers, VM coverage, retry and rollback.

## Non-goals and fixed decisions

- Do not support mixed old/new runtime processes or final legacy aliases.
- Do not rewrite opaque identifiers or arbitrary serialized strings.
- Do not upgrade never-deployed migration journals.
- Do not infer or recreate a retained tmux server's old filesystem alias.
- Do not delete or merge isolated test-recovery data.
- Do not expose the migration helper as a normal user command.
- Do not duplicate workspace presentation in package catalogs.
- Do not integrate default branches without explicit authorization.
- Accept the organization repository's temporary feature-branch GitHub default
  until an administrator can change it to the existing neutral `master`.
- Do not merge the configuration branch merely to deploy aitherdev.
- Do not archive, delete or permanently retire the initiative.
