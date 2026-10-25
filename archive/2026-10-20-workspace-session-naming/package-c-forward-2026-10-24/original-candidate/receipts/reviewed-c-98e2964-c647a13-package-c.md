# Package C: prepared deployment input updates

Both final feature branches are published over SSH with exact remote proof and
quick checks passed. Mandatory independent final review and long verification
remain lead-owned and pending. The missing structured retry-advice cause and
fixture correction are recorded in `package-a.md`. These source revisions are
not deployment or readiness proof.
No machine claim, activation, default-branch integration or lifecycle action ran.

| Repository | Initial base | Prepared head |
| --- | --- | --- |
| workspace | `20716e4431b0c6d2d78a41e1e638a1f6305860e4` | `98e2964727133d5a4871f70be205b90e29eff20f` |
| vpsfree-cz-configuration | `c1057731d34513b6ee3bb1dfb4a3e4832fdc67c9` | `c647a130564dd91219af96af8f83a1ab69fc0bb6` |

Both are registered own worktrees under `worktrees/2026-10-20-workspace-session-naming/`,
on the same-named feature branch. Both tracked working trees are clean. Current
final locks select runtime `ae0399b31746bc14ea2fcbe3185f36d8e4b04885` and
client `96077b6257bd7dac05930312a29eaf00fc900b3c`.

The workspace has one functional update to its existing direct nested runtime
URL and generated composed lock. The extension remains at
`767dfd587e346168e1443e65ccdb67ce748f3fe3`, with its complete lock node unchanged.
No native, sibling or follows change and no node addition/removal occurred.
Only the exact runtime and transitive codex-web node identities changed.

Configuration has one generated `confctl inputs channel set --commit dev-workspace devWorkspace REV`
update from the proper original `bf6d4b0c` predecessor. Its generated changelog
is retained verbatim. Only `devWorkspace` and transitive `codex-web` lock nodes
changed; native, siblings, follows paths and node set are preserved. No database
migrations or functional configuration changes are present.

## Quick evidence

- Required current deployment procedure, selected installed coordination and
  operations guides, configuration AGENTS/README/channel definitions and
  `docs/operations/codex-providers-aitherdev.md` read. The initially assigned
  older guide was deliberately removed by `c1057731`; the lead confirmed the
  current replacement. It was not restored.
- Configuration worktree creation initially failed in ambient post-checkout
  Overcommit because required gems were unavailable. `nix develop --command bundle check`
  proved the declared tools environment complete. Retrying exact registration
  there succeeded. Hooks were installed and trusted normally, without bypass.
- Workspace lock refreshes used `nix flake update vpsfree-dev-workspace/dev-workspace`;
  no lock was manually edited.
- Generated configuration commits passed active Nixfmt and commit-message hooks.
  The generated full-revision changelog line has an advisory TextWidth warning;
  workspace/configuration procedures explicitly require keeping it unchanged.
- Exact semantic comparisons against each initial base prove only the two
  allowed lock nodes changed, including preserved node input/follows maps.
- `git diff --check` is clean for both base-to-head diffs.
- Workspace `flake.nix` passed `nixfmt --check` in the configuration's Nix shell.
- The final prepared cross-repository check passed in that shell:
  `ruby WORKSPACE/bin/check-dev-workspace-deployment --workspace-root WORKSPACE --configuration-root CONFIGURATION`
  reported matching site identity and runtime `ae0399b31746bc14ea2fcbe3185f36d8e4b04885`.
- No long build, native integration, CI rerun or activation was launched.

## History and pending work

Each owned update stream is consolidated to one commit. The workspace branch
also inherits four legitimate shared-master coordination commits above fetched
remote `9f6968ebae4f1fbb26ff548ddcbd6cf8332a5b8b`:
`7e66fed3`, `efb2448f`, `21e250a1` and `20716e44`. Those are not new package-C
source updates and were preserved. The final Nix-environment feature rebase
reported up-to-date with shared master `20716e44`; fresh SSH upstream bases were
unchanged. Never rewrite shared master to remove these records. Complete exact
series, file lists and migration conclusions are in `package-c-final-inventory.json`;
own base-to-head patches are `workspace-final.diff` and
`vpsfree-cz-configuration-final.diff`.

Intermediate pre-review, undeployed source provenance: A `b81f8058`/`ee119a01`,
B `268f2e87`/`d9ea3925`,
workspace `00f2f313b188a0ad6b1fddd3b5f34c7bde0e0a0a` and configuration
`7ecabea3fb198829929380fea003abfcba10c90b`, followed by prepared workspace
`5b827cc8d0e07320e092ff0c146f1f86dd146eab` and configuration
`a03df3859725b38e67dd0025adf3e500e97310f3`. Old unpublished configuration
updates were dropped through ordinary owning-branch rebases to `c1057731`, then
the final confctl command regenerated its message from `bf6d4b0c`. No repository-wide
reset, clean or stash was used. No supported deployed consumer requires those
intermediate source heads.

Next: lead assigns mandatory final review of the complete committed deliverable,
then required fresh watchers run long verification. Implementer0 retains A/C
review-fix ownership. Long verification and activation remain lead-owned.
Routine pin updates require no additional project prose; existing deployment
guidance remains accurate.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
