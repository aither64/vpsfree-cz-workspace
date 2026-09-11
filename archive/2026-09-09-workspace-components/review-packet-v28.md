# Mandatory change review packet v28

## Outcome and acceptance criteria

Review the remediated strict four-layer split:

```text
vpsfree-cz-workspace
  -> vpsfreecz/dev-workspace
  -> aither64/dev-workspace
  -> aither64/codex-web
```

`vpsfree-cz-configuration` separately consumes the generic host module. The
current tracked trees of both generic repositories must contain no
case-insensitive `vpsfree` or `aitherdev`; their flake checks enforce this.
Concrete domains, credentials and cluster defaults belong to the workspace
consumer, organization tools belong to `vpsfreecz/dev-workspace`, and the
generic repositories own only reusable behavior.

The final organization/workspace package must have no old activation variable,
user namespace, router path or tmux metadata alias. One immutable compatibility
package exists only at the exact workspace bridge commit for cutover/rollback.

## Initiative and exact review boundaries

Slug: `2026-09-09-workspace-components`

- Plan: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/plan.md`
- State: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-workspace-components/state.md`

| Component | Base | Head | Worktree |
|---|---|---|---|
| `codex-web` | `dc5cdf8deb10abfd9f631428d051bfb087a2c5b8` | `c3200c4497d39e7840690cd4b205efbdd389f0f4` | `worktrees/2026-09-09-workspace-components/codex-web` |
| generic `dev-workspace` | `f39f8e62097b5e9da9de8a5eb678131b1e478e35` | `f7968552d61ac3e5b497e8cdc5a892400f4a60d6` | `worktrees/2026-09-09-workspace-components/dev-workspace` |
| organization `dev-workspace` | `9b8d07e12c1115aef1c09cfafbc71ba10e167853` | `ba9ff08e21682c1c832b241a394597edc46763f5` | `worktrees/2026-09-09-workspace-components/vpsfree-dev-workspace` |
| workspace | `a3a3804a2acfd114796a63995b8f16ca3537f4a4` | `97213a5b1718c8e1ba0de7fce9ba570d854de7da` | `worktrees/2026-09-09-workspace-components/workspace` |
| configuration | `e5458562a2a8cb12fe002be20b2d82e6a741f7ee` | `d16567fa94a5cca2529a940cd466b7109e448448` | `worktrees/2026-09-09-workspace-components/vpsfree-cz-configuration` |

All heads are committed, pushed and clean. Merge bases equal the listed bases.
All range diffs pass `git diff --check`.

Exact dependency pins:

```text
workspace@97213a5 -> vpsfreecz/dev-workspace@ba9ff08
  -> aither64/dev-workspace@f796855
  -> aither64/codex-web@c3200c4

configuration@d16567f -> aither64/dev-workspace@f796855
```

## Final commit shape

- `codex-web` retains published implementation commits. `6cc18a3` removes
  deployment-specific names and `c3200c4` adds the generic-source check.
- Generic `dev-workspace` retains published feature history. `4c6b62a` and
  `6279fbf` add generic compatibility parameters. `1c8c8e4` closes the exact
  catalog-key, executable-file and immutable wrapper-metadata boundaries and
  makes package switching use the canonical default output. `f796855` moves
  all remaining host-test construction out of `flake.nix`.
- The organization feature keeps the intentional 134 filtered provenance
  commits, then has four final-design commits only: `b308dc9` adds repository
  policy/license, `6db744c` owns and packages the organization extensions at
  the one final generic pin, `576a0c2` adds the complete schema-3 migration and
  compatibility contract directly, and `ba9ff08` adds CI. No intermediate
  migration schema, retry fixup or superseded dependency pin remains.
- Workspace has three final-design commits: `c89e19b` performs the complete
  four-layer delegation with workspace schema 2, `de9b928` selects the exact
  compatibility package, and `97213a5` selects the final generic namespace.
  No superseded three-layer design or schema-1 workspace manifest remains.
- Configuration has one input stream and two host changes: `cac2608` adds and
  locks the channel directly at `f796855`, `5c187fb` adopts the module, and
  `d16567f` selects new paths. Its final tree was produced with `confctl`, and
  all repository hooks passed.

## v27 findings and remediation

The duplicate activation-alias Blocking finding from all lanes is fixed:

- the organization constructor defaults aliases to `[]`;
- only workspace `migrationBridge` supplies
  `VPSFREE_WORKSPACE_ACTIVATION`;
- generic wrappers use immutable `--set`, not ambient-overridable
  `--set-default`;
- final and bridge package metadata have exact positive/negative checks;
- migration validation requires the bridge's exact singleton alias list and
  the final package's exact empty list.

Architecture/General Important findings are fixed:

- generic Nix evaluation rejects unknown top-level extension sections and
  unknown provider fields;
- installed/runtime catalogs require command/provider targets to be regular
  executable files, skills to be directories and configurations to be files;
- organization cluster defaults must be Nix paths, are copied into the store,
  and are checked as JSON objects during package installation;
- negative checks cover mutable/malformed cluster defaults;
- host test fixtures and evaluation now live entirely in
  `nix/tests/host-module.nix`.

Risk compatibility is fixed for archived sessions: forward/reverse inventories
now include both `work/*/portal.yml` and `archive/*/portal.yml`, validate those
exact paths, preserve their bytes/metadata in the journal and test an archived
old-socket manifest through forward and reverse. Retained threads therefore
remain revivable.

The unmerged organization, workspace and configuration histories were rebuilt
as described above. Their final trees are byte-identical to the previously
reviewed/remediated snapshots; only commit organization changed.

## Compatibility and deployment gate

The two-generation migration and exact rollback behavior remain as described
in `vpsfree-dev-workspace/docs/namespace-migration.md`. The migration locks
runtime and fallback lifecycle locks in both directions, hands the live tmux
server between keepers, validates all paths before mutation, records the exact
bridge package/metadata digest, and refuses reverse unless the final package
and immediately previous recorded bridge are selected.

The user authorized aitherdev deployment, Codex-session restarts and resetting
the running development cluster. Default-branch integration remains separately
governed. The actual registered workspace root still has old namespace policy
and source-local KB commands on shared `master`; therefore alias-free final
deployment is explicitly blocked until the user authorizes fast-forward
integration of reviewed workspace commit `97213a5` into local shared `master`.
No attempt is made to bypass that gate with an uncommitted overlay.

Generic flake outputs `workspace-host` and `workspace-portal` remain as
published generic compatibility names: they contain no organization naming and
are not part of the old vpsFree namespace. New package switching uses the
canonical default output. Final workspace commit `97213a5` does not export
those aliases; bridge commit `de9b928` exports `workspace-portal` only because
the deployed predecessor needs it to install the bridge.

The endpoint hostname/alias necessarily appears in both workspace metadata and
host/DNS configuration. This small cross-owner duplication is accepted; live
acceptance verifies portal metadata, DNS, TLS SANs and nginx routing together.

## Quick verification

- Generic `dev-workspace`: `ruby test/workspace_host_test.rb` passed with 71
  runs and 445 assertions; no-build flake evaluation and the extension-catalog
  check build passed; forbidden-name scan is empty.
- Organization `dev-workspace`: migration tests passed with 11 runs and 99
  assertions; no-build flake evaluation passed; forbidden-name scan is empty.
- Workspace: both bridge and final commit shapes pass no-build flake
  evaluation at the exact final dependency pins.
- Configuration: no-build flake evaluation passed at the exact final pin;
  `confctl` and repository hooks passed while generating it.
- `codex-web@c3200c4` exact-head GitHub Actions is green. New generic and
  organization CI runs were triggered by the remediation pushes.

Long full package checks, the NixOS VM, both exact workspace package builds and
the aitherdev configuration build remain deferred until review is clean.

## Risk and lanes

Overall risk remains **High** because public cross-project contracts, user/root
persisted state, credential/TLS paths, systemd topology, destructive migration,
deployment order and exact rollback are affected. Rerun General, Architecture,
Scope and Risk with `gpt-5.6-sol` at `xhigh`.

## Non-goals and decisions

- Do not rewrite published generic history.
- Do not support mixed old/new runtimes or old organization-specific aliases
  in the final package.
- Do not integrate a default branch without explicit authorization; no
  uncommitted policy overlay is an acceptable substitute.
- Do not archive, delete or retire the development session.
- Do not change vpsAdmin databases, APIs, daemon protocols or deployed
  vpsAdminOS nodes.
- Historical prose is not mass-rewritten; machine-consumed archived manifests
  are migrated because revive depends on them.
- The organization repository's GitHub default-branch metadata remains an
  external owner-only correction because the current token receives HTTP 403.
