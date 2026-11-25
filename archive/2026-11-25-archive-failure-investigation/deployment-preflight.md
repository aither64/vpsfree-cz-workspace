# Archive fix deployment preflight

Package B, implementer1, 2026-11-25. Read-only preparation; the only written
file is this evidence record. No worktree, commit, pin, build, machine claim,
activation, merge or lifecycle action was performed. Architect0 owns cause and
candidate design; lead owns deployment authority and integration coordination.

## Verified identity and guidance

`dev-session current` printed `2026-11-25-archive-failure-investigation`;
both environment identity values matched that slug and
`/home/aither/workspace/ai/vpsfree.cz`. Live roster retains implementer1 as
workspace_write, Sol/xhigh, with architect0/implementer0 as assigned peers.
Initial tracking commit supplied by lead: `172c14576`.

Read workspace AGENTS, projects, sessions, deployment, lifecycle, Git,
verification, documentation, coordination and agent-teams procedures;
documentation/handoff skills; configuration AGENTS and the historical
`docs/operations/workspace-coordination-aitherdev.md` from the then-inspected
bare HEAD (that guide is absent at final configuration `6f6cb452`); selected-package
`workspace-host coordination guide`, operations guide and workspace-update
guide; relevant runtime host/profile/cluster transition documentation. The
configuration guide's older release wording conflicts with current policy.
The selected runtime and workspace instructions require verified deployment
effects **and integrated deployed lineage** before machine release; UI acceptance
is not an additional release gate.

Current session, failed-source session and installed runtime feature session
have no private sensitivity marker in
`~/.local/state/dev-workspaces/sensitive-sessions/vpsfree.cz-8a2a555cb2f65b33/`.
No sensitive source excerpts are retained here.

## Exact installed state

| Component | Observed identity |
| --- | --- |
| Live system and system profile | `/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211` from both `/run/current-system` and `/nix/var/nix/profiles/system` |
| System configuration | `109d789f0a4ee875f8bd27a0b72ea76c38ee234a`, clean, `/etc/confctl/configuration-info.json` |
| Effective system runtime role | `devWorkspace` → input `devWorkspace`, `f3bd843f9858b87cef66d0949706f8af16ba9b13`, `/etc/confctl/inputs-info.json` |
| Other effective system roles | nixpkgsStable `94c3211b0ee8ba969a3f12eb4aff8ba0f72971dd`; home-manager `c47b2cc64a629f8e075de52e4742de688f930dc6`; llm-agents `91ff550fe42d4dd51dcf8b6bad87a0134fe7f314` |
| Configuration lock's confctl | `d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49` at deployed configuration revision |
| Selected user profile | `~/.local/state/dev-workspaces/profile` → `profile-290-link` → `/nix/store/1zn1a51qrsin83fszrprdjp45208vsj4-dev-workspace-0.2.0` |
| Package derivation | `/nix/store/s6qiklxmmdz409qlg26643mf0g8rafb1-dev-workspace-0.2.0.drv` |
| Installed runtime source | `/nix/store/vp5r16m56956rrm0dvza0li169qdjkaw-source` |
| Composed workspace source | `/nix/store/csv89jnlh1zrbi9xff9ahmkzjsg6zmgf-source` (referenced by the installed derivation's postInstall) |
| Installed runtime revision | `91cafd4c0c50ffb7208498a605707c4c3b1b1174`, proven by that immutable composed lock and matching source NAR |
| Extension revision/source | `bf12ac71a8a00b1581eed5352f99c1b2daaeff5b`; `/nix/store/nma0v0499qdyn4f2wwwdbzf5i49nhlip-source` |
| Installed codex-web | `2547d535eefd4154afef4125ea0fb76e5894a8b6` |
| Native package | `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0` |

The runtime source NAR is
`sha256-w8rK1jDoPlHI8Z/Im0Zeo/1qA5OkgCMhZEYCXOF6vSk=`.
Recursive Git object hashing, including every file, symlink and executable bit,
gives complete source tree `f3bff8f5008ade6561a92856eec22a25ac48488c`.
It exactly matches `91cafd4` and the equivalent earlier fixup tree `4f096ff`.
The immutable composed lock disambiguates the installed revision as `91cafd4`.

Local and origin feature refs `2026-11-23-pi-message-delivery` point at `91cafd4`.
Relative to observed origin/master `65544340f94ebb112872743738f84c1a7022b06a`,
the installed range contains exactly:

- `9bf34aa1963e3ba226ec678237cee3dacb2e7a25`: refuse conflicting team initial IDs.
- `91cafd4c0c50ffb7208498a605707c4c3b1b1174`: recover proven held team-message conflicts.

Origin/master is an ancestor of installed source; installed source is not an
ancestor of origin/master. The full `65544340..91cafd4` range changes 34 files
(4217 insertions, 232 deletions). The shared
workspace lock still selects `65544340`, and canonical bare HEAD is older still.
Neither is the installed baseline. A candidate must preserve this full deployed
range, with the lead deciding branch ownership and integration lineage. The
existing runtime source lock also preserves the complete transitive input graph;
the extension lock alone does not describe the composed runtime override.

Immutable graph references:

- Composition: `/nix/store/csv89jnlh1zrbi9xff9ahmkzjsg6zmgf-source/flake.lock`,
  SHA-256 `80cbb326de11cae8644d66cd76438222a4ddcd1819526f34af84cf2710293f72`.
- Runtime: `/nix/store/vp5r16m56956rrm0dvza0li169qdjkaw-source/flake.lock`,
  SHA-256 `ca7f6a807e2a32d76deb463a44677023e3fac2236ce93c82426c54307aefa51f`.
- Extension: `/nix/store/nma0v0499qdyn4f2wwwdbzf5i49nhlip-source/flake.lock`,
  SHA-256 `b2282ff7b51986f792cdfe5207c928699a085684c2183e539c434e55341a07bb`.
- System graph: committed configuration `109d789f0a4ee875f8bd27a0b72ea76c38ee234a`,
  its flake/channel records, and effective `/etc/confctl/inputs-info.json`.
  Effective role revisions above take precedence over inferring them from the
  root lock alone, which contains different home-manager/llm-agents revisions.

## Target and supported route

Exact selector: `cz.vpsfree/machines/aitherdev`; confctl adapter. Host module
declares target `172.16.106.40`, host `aitherdev`, location `int`, domain
`vpsfree.cz`, and channels `nixos-stable`, `home-manager`, `llm-agents`,
`dev-workspace`. Channel `dev-workspace`, role `devWorkspace`, maps to flake
input `devWorkspace`. Its host module supplies the substrate, not the application.

Profile machine identity is
`machine:github.com/vpsfreecz/vpsfree-cz-configuration:cz.vpsfree/machines/aitherdev`;
the installed policy explicitly bridges legacy `machine:vpsfree:aitherdev`.
New deployment uses a schema-2 claim against the session's registered committed
configuration feature head. At handoff the session manifest registers the runtime
repository, but not configuration; configuration registration and prepared locked
inputs remain preconditions.

If the architect releases a runtime/host deployment, the minimal supported route
is the following. These are preparation instructions, not executed commands:

1. Preserve the installed runtime range and extension; finish core changes,
   commits, quick checks, final independent review and applicable longer checks.
   Publish the exact candidate runtime. Use owned workspace/configuration feature
   worktrees; do not repin from the older shared lock or alter a peer checkout.
2. In configuration's Nix shell, select an exact unmerged published revision with
   `confctl inputs channel set --commit dev-workspace devWorkspace REVISION`.
   Preserve generated messages/locks and unrelated inputs. Keep workspace's direct
   nested `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` and update only
   that runtime selection via `nix flake update vpsfree-dev-workspace/dev-workspace`.
   Run `bin/check-dev-workspace-deployment --workspace-root WORKSPACE_FEATURE --configuration-root CONFIG_FEATURE`.
3. Prepare the final committed system/application generations outside machine
   ownership. Configuration commands are `confctl build cz.vpsfree/machines/aitherdev`
   and `confctl deploy --generation GENERATION --copy-only cz.vpsfree/machines/aitherdev`.
   Retain the exact named generation, store paths, source/input graph and rollback
   metadata. Use the monitor skill for builds/checks expected to exceed one minute.
4. Lead acquires a separate machine-only schema-2 claim selecting repository
   `vpsfree-cz-configuration`, selector above, adapter `confctl`. After authoritative
   held status, run `workspace-host coordination verify-machine SESSION --as-is --id CLAIM_UUID --repository vpsfree-cz-configuration --selector cz.vpsfree/machines/aitherdev --json`.
5. Activate the prepared generation under that claim:
   `confctl deploy --generation GENERATION cz.vpsfree/machines/aitherdev dry-activate`,
   then the same command with action `switch`. Do not add `--reboot`; preserve
   configured auto-rollback. Verify both live-system and system-profile links.
6. Select the composed application with ordinary
   `workspace-host switch --source WORKSPACE_FEATURE`, passing the exact verified
   `DEV_SESSION_SLUG`, `DEV_SESSION_WORKSPACE` and `DEV_WORKSPACE_CLAIM_ID`.
   System activation precedes profile selection. Keep the same machine claim.
7. Verify profile/source composition, portal/router/coordinator health, naming,
   retained conversation and tmux continuity, and effects of every command.
   Preserve source-owned recovery on any partial/uncertain result. Integrating
   deployed lineage requires separate explicit repository/target approval.
   Release the exact owned claim promptly once verification and integrated
   lineage are proven, and verify released status.

## Transition gates and unresolved preconditions

- At package acceptance, lead reports authoritative aitherdev claim `6097deba`
  held by the parent owner. This session has no machine ownership and must not
  activate while that hold remains. Selected profile/source identity alone does
  not prove the parent's deployment effects, integration or release complete.
- Architect/lead must choose a candidate preserving installed `91cafd4` and its
  parent range. Current shared workspace and deployed host runtime selections
  are different from installed application provenance; reconcile final locks
  explicitly and pass the deployment checker before activation.
- The ordinary failed archive remains in the portal lifecycle store as
  `kind: archive`, `state: failed`, `phase: checking`. No `.archive.json`,
  `.removal.json`, `.revive.json` or `.archive-cleanup.json` was present in
  this registered workspace's `worktrees/.locks` at inspection. The registry
  contains only `vpsfree-cz`. A failed portal receipt is distinct from a pending
  filesystem lifecycle journal; candidate admission must reread authoritative
  state. Any newly present journal blocks conflicting package changes and keeps
  its original recovery command. This package does not authorize a retry.
- The maintenance status read reported complete, continuations settled and
  restoration completed. This historical status is not complete fresh admission
  proof, nor permission to cancel/recover another operation.
- Candidate must preserve service registry schema/policy 1, cluster schema 1,
  tracking limit 8388608 and transition policy at least 3, current backend/native
  registration capabilities, typed claim/history readers and machine bridge.
  Never reset clusters, clear journals or downgrade retained state to pass.
- Selected runtime live-switch policy is 2 and reporting policy 4. A same-native,
  same-registration compatible candidate can leave Codex/tmux running while
  refreshing portal/router. A native/registration change needs the supported
  maintenance/idle route and original recovery contract; profile transitions
  remain forward-only. Do not assume compatibility solely from source build.
- No candidate, build result, review, configuration registration, fresh machine
  claim or integration approval exists within package B. Final artifact/input
  identities and fresh remote ancestry must be retained by the rollout owner.
  Deployment permission does not authorize default-branch integration or any
  exact session archive, deletion or stop.

## Read-only command evidence

Principal observations used `dev-session current`, filtered live team listing,
`workspace-host status`, `workspace-host coordination guide`,
`readlink -f` for profile/system links, `nix-store -q --deriver`,
`nix derivation show`, `nix hash path`, immutable lock reads, targeted `git show`
of configuration `109d789` and selected guides, exact-range `git log`, and
`git merge-base --is-ancestor` against observed origin/master. Source identity
was calculated in memory and matched against recent canonical commit trees;
no Git objects/metadata were written. The old bare configuration HEAD and raw
root lock were explicitly rejected as evidence of effective deployed roles.

No tests were run: this package prepares operations and source identity, with no
code changes. No reusable procedure changes were needed; the stale configuration
release wording is reported to lead rather than edited outside this package.
The assigned evidence file passed `git diff --no-index --check /dev/null FILE`.
Lead accepted package B; further candidate work requires its next explicit package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/
