# BLOCKED future C recipe — no execution authority

**All commands below are UNEXECUTED and NOT AUTHORIZED.** USER deployment HOLD
is active. Creation acceptance remains FAILED/unresolved; full runtime flake
readiness is blocked. Independent subset results cannot waive either gate.
This source-only candidate does not authorize system/application builds, copy,
machine acquisition, dry activation, switching, profile selection or integration.
Main must first resolve readiness, inspect this exact composition, choose future
verification/builds and obtain the user's explicit deployment-hold lift. Fresh
physical-machine ownership is required near activation. No claim is held here.

| Component | Exact source candidate |
| --- | --- |
| Workspace | `cbf7864a75127a374d65fc9bbb7c4fdd6cea30d1` |
| Configuration | `a2ba6fe4ed06584b39ec8144b225e85428a6b036` |
| Runtime | `529e075ad07e2d967a8af4902584e37527115454` |
| Client | `801099102ef9af4a82c1f3853c53d6b442ecd4dc` |
| Extension | `767dfd587e346168e1443e65ccdb67ce748f3fe3` |

Old C113d/7510 selects stale runtime/client behavior and must never activate.
Its source/recipes/reviews/build receipts remain historical in the preservation
packet. New self-source NAR paths/system or composed-package outputs are unknown;
no optional metadata/build was generated. The final lock graphs contain exact
input identities. Existing A7nl4/Bknj9 source receipts establish source identity,
not readiness or a built composition. Never infer installed workspace/system Git
SHAs from store names. Recheck the actual selected/deployed baseline before any
future rollout; preserve newer recovery, conversations, retained roots and journals.

After separate future authority, a fresh lead-owned utility prepares builds and
copy outside machine ownership. These are retained command templates:

```bash
C_ROOT=/home/aither/workspace/ai/vpsfree.cz
C_SESSION="$C_ROOT/work/2026-10-20-workspace-session-naming"
C_WORKSPACE="$C_ROOT/worktrees/2026-10-20-workspace-session-naming/workspace"
C_CONFIG="$C_ROOT/worktrees/2026-10-20-workspace-session-naming/vpsfree-cz-configuration"
C_MACHINE=cz.vpsfree/machines/aitherdev

test "$(git -C "$C_WORKSPACE" rev-parse HEAD)" = cbf7864a75127a374d65fc9bbb7c4fdd6cea30d1
test "$(git -C "$C_CONFIG" rev-parse HEAD)" = a2ba6fe4ed06584b39ec8144b225e85428a6b036
test -z "$(git -C "$C_WORKSPACE" status --porcelain --untracked-files=all)"
test -z "$(git -C "$C_CONFIG" status --porcelain --untracked-files=all)"
cd "$C_CONFIG"
nix develop --command confctl build --yes "$C_MACHINE"
```

After a successful build, immediately capture the returned successful new/reused
generation before any subsequent build. Retain complete generation.json and exact
source/input/derivation receipts, not only these selected fields:

```bash
C_GEN_ROOT="$C_CONFIG/.confctl/generations/cz.vpsfree:machines:aitherdev"
C_GEN=$(basename -- "$(readlink -- "$C_GEN_ROOT/current")")
C_GEN_DIR="$C_GEN_ROOT/$C_GEN"
C_TOPLEVEL=$(nix develop --command ruby -rjson -e 'puts JSON.parse(File.read(ARGV.fetch(0))).fetch("toplevel")' "$C_GEN_DIR/generation.json")
test "$(readlink -f "$C_GEN_DIR/toplevel")" = "$C_TOPLEVEL"
cat "$C_GEN_DIR/generation.json"
nix develop --command confctl generation ls --local "$C_MACHINE" "$C_GEN"
nix develop --command confctl deploy --yes --generation "$C_GEN" --copy-only "$C_MACHINE"
C_PACKAGE=$(nix build --out-link "$C_SESSION/package-c-forward-2026-10-25/future-workspace-result" --print-out-paths "$C_WORKSPACE")
test -x "$C_PACKAGE/bin/workspace-host"
test "$(readlink -f "$C_SESSION/package-c-forward-2026-10-25/future-workspace-result")" = "$C_PACKAGE"
```

No result link/generation above exists from this package. Main must retain actual
full input graphs, source roots/NARs, predecessor package/system/profile paths,
exact generation auto_rollback/inputs/inputs_info and resolved artifacts. Preserve
configured auto-rollback. The host application lives in the user profile; config
selects its matching host module/runtime contract, without installing the app.

Only after a separately authorized rollout and exact held claim covering
`vpsfree:aitherdev`, set C_CLAIM to that verified owned UUID. Select the captured
literal generation by name; do not use a moving current/offset for activation:

```bash
cd "$C_CONFIG"
nix develop --command confctl deploy --yes --generation "$C_GEN" "$C_MACHINE" dry-activate
# Main inspects dry-activation effects before any switch.
nix develop --command confctl deploy --yes --generation "$C_GEN" "$C_MACHINE" switch
nix develop --command confctl ssh --yes "$C_MACHINE" -- readlink -f /run/current-system /nix/var/nix/profiles/system
```

Both system paths must match C_TOPLEVEL and system checks must pass before app
selection. Reconcile partial profile publication/uncertain effects; no reboot or
auto-rollback bypass. Then the ordinary selected-generation public switch, as
aither, uses the exact unchanged source and held claim:

```bash
env DEV_SESSION_SLUG=2026-10-20-workspace-session-naming \
    DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
    DEV_WORKSPACE_CLAIM_ID="$C_CLAIM" \
    workspace-host switch --source "$C_WORKSPACE"
test "$(readlink -f /home/aither/.local/state/dev-workspaces/profile)" = "$C_PACKAGE"
workspace-host status
```

That public switch repeats source preparation/build and checks package generation,
claim, compatibility and recovery under ordinary locks; there is no substitute
public package-path selector. Stop/reconcile any unexpected build or refusal.
Main verifies health/naming/conversation effects. Physical-machine release follows
verified effects and integration of complete deployed lineage into separately
approved defaults. No lifecycle action is authorized by preparation or release.

Command syntax is inherited from the previously inspected pinned confctl CLI and
current installed8ph coordination/operations guides; confctl's locked node is
unchanged to this package's current config base. The current site procedure is
`docs/operations/codex-providers-aitherdev.md`. Main must recheck syntax/baseline
if those inputs change. No command in this recipe was executed for this package.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
