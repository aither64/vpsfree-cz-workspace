> USER DEPLOYMENT HOLD — 2026-10-25: this is a historical, unexecuted recipe.
> C113d/7510 is stale and must never be activated. Do not copy, acquire machines,
> dry-activate/switch systems or select a workspace profile until explicit user
> lift and a newly reviewed final forward composition. Preserve this recipe as
> historical evidence; current hold receipt is
> `forward-rollout-20261024/user-deployment-hold.json`.

# Package C: forward refresh activation recipe

Published forward candidates below passed owner quick checks. Full forward and
affected cancellation review passed with no findings. This mechanical runtime
selection refresh passed the lead’s independent equivalence inspection in
`forward-review-20261024/cancellation-composition-inspection.json`. Fresh
exact-input verification/builds remain lead-owned and pending their receipts.
This recipe was refreshed from the current confctl CLI, selected installed
coordination/operations guidance and site procedure. It is session-only,
unexecuted by implementer0, and grants no deployment or integration approval.
Old c740/4383 recipes and receipts remain in
`package-c-forward-2026-10-24/original-candidate/`. The reviewed c870/de4d
packet and recipe are preserved in
`package-c-forward-2026-10-24/reviewed-c870-de4d-before-cancellation-refresh/`.
Prior successful builds are stale for this source graph. Lead owns watchers, claims, rollout and verification.

| Source | Published candidate |
| --- | --- |
| Workspace | `113d7cf78c300483df5d71735fd5bea4adc4e7b9` |
| Configuration | `7510da63dae8bbb149d42d2a828e49a70a6fd27f` |
| Runtime selected by both | `37a87a8a81cd3c705b7c5ee4f39338c1db1cc6ce` |
| Transitive codex-web | `6e469863a69c7d35941ca2e15de9514223b58f4f` |
| Preserved extension | `767dfd587e346168e1443e65ccdb67ce748f3fe3` |

Workspace registered initial base remains `20716e44`; effective owning base is
`04f92aec`, retaining six inherited coordination/artifact commits above remote
default `aadb6645`. Configuration registered initial base remains `c1057731`;
its effective/default base is `25258cd3`. One authored runtime-selection commit
per consumer changes only workspace flake.nix/flake.lock and configuration
flake.lock. Complete history, old→new scoped diffs and no-migration conclusion
are in `package-c-forward-2026-10-24/inventory.json`.

The pre-rollout snapshot remains lead-owned
`rollout-resume-baseline-20261024.json`: selected package is
`/nix/store/l9sc1ksacdkm7iij99ggyg87bqsp9n15-dev-workspace-0.2.0` and ordinary
daemon PID 3387667 was unchanged. Recheck the actual baseline immediately before
rollout. No own installed workspace/system Git SHA is inferred from store paths.
Do not activate the old naming candidate or weaken schema-1 retry/policy and
forward-recovery guards. Preserve current conversations, provider settings,
private journals and package roots.

Available immutable candidate source identities (read-only metadata, no build):
configuration `/nix/store/w9p4g6grnq5jgcibbh29h8si0jd1cy8d-source`, NAR
`sha256-tOpXBSRzwh+CzI523TKxcn+kcRjZxxAiPzO+sF+cyIk=`; runtime
`/nix/store/d4l45ifray9zd5mw7g5i472dfp9nbif3-source`, NAR
`sha256-jzlNJ4RgAYPZVNlku3lBy4fcp9R2nf9QEyNU7uedbSM=`. Client source/NAR
remains the proven A6e469 identity in the A packet. Optional workspace metadata
retrieval was interrupted after more than four minutes without a result. The
published workspace revision and full input graph are exact; capture its actual
composed store path/NAR in the lead’s build receipt. This does not identify the
currently installed workspace/system Git SHAs.

## Build and copy outside machine ownership

After final review and the required verification gate, use fresh lead-owned
watchers for builds/copy and uncertain waits. Run configuration commands in its
declared Nix shell. Use the feature worktrees, with unchanged committed sources:

```bash
C_ROOT=/home/aither/workspace/ai/vpsfree.cz
C_SESSION="$C_ROOT/work/2026-10-20-workspace-session-naming"
C_WORKSPACE="$C_ROOT/worktrees/2026-10-20-workspace-session-naming/workspace"
C_CONFIG="$C_ROOT/worktrees/2026-10-20-workspace-session-naming/vpsfree-cz-configuration"
C_MACHINE=cz.vpsfree/machines/aitherdev

test "$(git -C "$C_WORKSPACE" rev-parse HEAD)" = 113d7cf78c300483df5d71735fd5bea4adc4e7b9
test "$(git -C "$C_CONFIG" rev-parse HEAD)" = 7510da63dae8bbb149d42d2a828e49a70a6fd27f
git -C "$C_WORKSPACE" status --short
git -C "$C_CONFIG" status --short

cd "$C_CONFIG"
nix develop --command confctl build --yes "$C_MACHINE"
```

Immediately capture the exact generation selected by this successful build,
before any other build in this worktree. A reused matching generation is valid.
Retain these values and the complete JSON in the lead's rollout record; restore
the same literal values when continuing in another shell:

```bash
C_GEN_ROOT="$C_CONFIG/.confctl/generations/cz.vpsfree:machines:aitherdev"
C_GEN=$(basename -- "$(readlink -- "$C_GEN_ROOT/current")")
C_GEN_DIR="$C_GEN_ROOT/$C_GEN"
C_TOPLEVEL=$(nix develop --command ruby -rjson -e 'puts JSON.parse(File.read(ARGV.fetch(0))).fetch("toplevel")' "$C_GEN_DIR/generation.json")
test "$(readlink -f "$C_GEN_DIR/toplevel")" = "$C_TOPLEVEL"
printf 'generation=%s\ntoplevel=%s\n' "$C_GEN" "$C_TOPLEVEL"
cat "$C_GEN_DIR/generation.json"
nix develop --command confctl generation ls --local "$C_MACHINE" "$C_GEN"
nix develop --command confctl deploy --yes --generation "$C_GEN" --copy-only "$C_MACHINE"

C_PACKAGE=$(nix build --out-link "$C_SESSION/package-c-forward-2026-10-24/final-37-workspace-result" --print-out-paths "$C_WORKSPACE")
test -x "$C_PACKAGE/bin/workspace-host"
test "$(readlink -f "$C_SESSION/package-c-forward-2026-10-24/final-37-workspace-result")" = "$C_PACKAGE"
printf 'workspacePackage=%s\n' "$C_PACKAGE"
```

The new dated result link retains the refreshed application package without
replacing the old candidate’s result root. Preserve confctl's generation
roots, complete `generation.json` (`toplevel`, `auto_rollback`, `inputs`,
`inputs_info`), both committed lock graphs and source identities in the existing
rollout receipt. Capture the predecessor system/profile/package identities too.
The copy-only deployment returns before activation and does not select a system
profile. No application copy is needed: the workspace user profile is on this
same physical aitherdev host (`vpsfree:aitherdev`, target `172.16.106.40`).

## Activate the exact prepared system, then application

Lead must first hold and verify the exact session-owned machine claim covering
`vpsfree:aitherdev`; set `C_CLAIM` to that existing held claim UUID. Repository
claims are separate. Recheck source identities and the retained generation
before proceeding. These commands select the captured generation by name,
preserve configured auto-rollback and do not request a reboot:

```bash
cd "$C_CONFIG"
nix develop --command confctl deploy --yes --generation "$C_GEN" "$C_MACHINE" dry-activate
# Review dry-activation effects before the switch.
nix develop --command confctl deploy --yes --generation "$C_GEN" "$C_MACHINE" switch
nix develop --command confctl ssh --yes "$C_MACHINE" -- readlink -f /run/current-system /nix/var/nix/profiles/system
```

Both returned system paths must equal `C_TOPLEVEL`, and required system checks
must pass before application selection. A live switch can precede failed system
profile publication; reconcile both identities and uncertain effects before
continuing. Do not use `boot`, `--reboot` or disable configured auto-rollback.

Then run the ordinary selected-generation public switch as `aither`:

```bash
env DEV_SESSION_SLUG=2026-10-20-workspace-session-naming \
    DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
    DEV_WORKSPACE_CLAIM_ID="$C_CLAIM" \
    workspace-host switch --source "$C_WORKSPACE"
test "$(readlink -f /home/aither/.local/state/dev-workspaces/profile)" = "$C_PACKAGE"
readlink /home/aither/.local/state/dev-workspaces/profile
workspace-host status
```

The public switch repeats source preparation and `nix build --no-link
--print-out-paths SOURCE`; the unchanged package must already be built. There is
no public package-path selector to substitute here. It verifies machine claim,
source identity, package compatibility and transition/recovery contracts under
the existing locks. Preserve active threads/guests, retained roots and journals;
stop and reconcile an unexpected rebuild, policy refusal or partial transition.
Record the exact selected profile generation/package and verify portal/session
effects using the lead's accepted rollout checks.

Machine ownership remains held through verified deployment effects and complete
integration of the deployed feature lineage into explicitly approved defaults.
Integration still needs separate approval. Lead then verifies authoritative
claim state, releases the exact owned claim and verifies release. This recipe
does not authorize session lifecycle actions.

## Source and CI evidence

Confctl is pinned by configuration to
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`. Inspected its `cli/app.rb`,
`cli/cluster.rb`, `conf_dir.rb`, `generation/{build,build_list}.rb`,
`nix_flake.rb`, `nix_legacy.rb` and CLI manual. Exact generation names resolve
through `--generation`; `current`/offset selectors are deliberately avoided in
activation. The current-link capture above follows `NixFlake#build_attributes`,
which publishes the successful new or reused build generation.

Read the selected installed package's coordination/operations guides and public
`workspace-host` switch/build source, workspace deployment procedure and current
configuration `docs/operations/codex-providers-aitherdev.md`. The obsolete guide
removed by `c1057731` is not part of this recipe.

Read-only GitHub queries on 2026-10-24 returned no feature-branch runs for
workspace `113d7cf7` or configuration `7510da63`. Workspace has no workflows;
configuration has only `daily-update.yml` with schedule/manual triggers and no
feature-push trigger. No C CI IDs exist to report, and no workflow was triggered,
awaited or rerun. The new configuration baseline’s CI guard is inherited unchanged.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
