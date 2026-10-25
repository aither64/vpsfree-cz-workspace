# Package C: final published deployment inputs

Final C branches are published over canonical SSH, quick checks and hooks passed,
and source/refs are frozen. Both select reviewed B
`e515437822e6a2ee7e61be7b613d1e058dad56d7` and unchanged verified A
`4300c40b6406161afc74c124c40155f28a557032`. Longer package/build verification and
deployment remain lead-owned. These pins are not deployment or readiness proof.

| Repository | Registered initial base | Effective owning base | Published final head |
| --- | --- | --- | --- |
| workspace | `20716e4431b0c6d2d78a41e1e638a1f6305860e4` | `e8d723317f5640e87c32e475cf954952d6b74550` | `c740bbf735e4fb2e6eb4f984476861c63ea8a47e` |
| vpsfree-cz-configuration | `c1057731d34513b6ee3bb1dfb4a3e4832fdc67c9` | `c1057731d34513b6ee3bb1dfb4a3e4832fdc67c9` | `4383ab0f54e5eb0035c5dd35df3b3d160e81359f` |

Both registered worktrees remain under
`worktrees/2026-10-20-workspace-session-naming/`, on the same-named feature
branch, with clean tracked working trees. Exactly one authored runtime update
remains per consumer. Workspace changes only its existing nested runtime URL and
generated composed lock; extension
`767dfd587e346168e1443e65ccdb67ce748f3fe3` is preserved byte for byte.
Configuration changes only its channel-owned generated lock. Native/sibling
inputs, node sets and inputs/follows paths are preserved. There are no migrations.

## Quick and publication evidence

- `nix flake update vpsfree-dev-workspace/dev-workspace` generated the workspace
  lock; only its runtime node changed relative to prior published C. A4300's
  complete client node remained unchanged.
- Configuration's prior update was removed by an ordinary owned-branch rebase
  to c105 in its Nix environment. Required
  `confctl inputs channel set --commit dev-workspace devWorkspace e515437822e6a2ee7e61be7b613d1e058dad56d7`
  then generated one final commit from the proper bf6d4b0c predecessor, retaining
  the complete four-commit B changelog verbatim: dependency9d741a1, functional
  4c6b9f1, notification-stage fixture915b904 and archive diagnostics e515437.
- Active Nixfmt/pre-commit and commit-message hooks passed; generated TextWidth
  is the expected advisory warning. No hook bypass or manual lock edit.
- Semantic comparisons against each effective base and prior published candidate
  passed. Only runtime/client nodes differ from the bases, and only runtime
  differs from prior C. Every node input/follows map and unrelated node is equal.
- Final declared-shell command
  `ruby WORKSPACE/bin/check-dev-workspace-deployment --workspace-root WORKSPACE --configuration-root CONFIGURATION`
  passed for the expected site at exact runtime e5154378. Workspace flake.nix
  passed nixfmt; owned diffs passed `git diff --check`.
- Workspace amendment used its declared Nix environment and a temporary message
  file. Normal rebase to shared master e8d reported up-to-date.
- SSH publication used explicit old-head leases: workspace3dbda147 and
  configuration88fb32b8. Both resulting remote refs were checked against the
  full final heads above. Source/refs are frozen after publication.
- Exact-final-head GitHub queries returned no runs. Workspace has no workflows;
  configuration has only a scheduled/manual daily-update workflow. Nothing was
  triggered or awaited, and no superseded active C run required cancellation.

## Review, history and source lineage

Original independent final review covered C98e2964/c647a13 with the full A/B
deliverable and no migrations. Lead subsequently accepted the direct A replay
remediation and fixture-only deletion under the narrow-fix policy; A4300's
corrected native watcher passed. Reviewer0 separately completed B's notification
and archive diagnostic affected-lane reviews without findings, assessing its
complete four-commit history as coherent with no migrations. This C update is
pure input selection and generated metadata; it requires no new standalone
content review. Lead owns final mechanical acceptance and exact build gates.

Original reviewed C snapshots are `reviewed-c-98e2964-c647a13-*`. The immediately
preceding published C3dbda147/88fb32b8 patches, full inventories, prior mechanical
deltas, proofs, narrative and recipe were saved as
`reviewed-c-3dbda14-88fb32b-*` before replacement. All are undeployed provenance;
no supported deployed consumer requires those intermediate pins. Older setup
and consolidation history remains in those snapshots. No repository-wide
reset/clean/stash was used.

The workspace preserves the original four inherited coordination ancestors above
remote default9f6968eb and now also tracking-only e8d72331, whose three paths and
commit metadata are inventoried without copying other-session record contents.
The registered initial base20716 remains recorded. Effective owning basee8d
keeps the final authored series to one pin commit. Other-session tracking was
not edited. Configuration's base remains fresh origin/masterc105.

Exact complete series, initial/effective/reviewed/prior ranges, trees, SSH refs
and migrations are in `package-c-final-inventory.json`. Committed owned-file blob
proof and semantic checks are in `package-c-final-semantic-check.json`. Complete
final input graphs are `package-c-workspace-final-lock.json` and
`package-c-vpsfree-cz-configuration-final-lock.json`, with hashes in the inventory.

Own base-to-final patches are `workspace-final.diff` and
`vpsfree-cz-configuration-final.diff`. Both original-reviewed→final and
prior-published→final deltas are saved as `package-c-*-review-refresh.diff` and
`package-c-*-prior-to-final.diff`, scoped only to owned flake files.
`package-c-*-own-range-diff.txt` compares the owning one-commit ranges; it excludes
other-session content. The fifth upstream ancestor is metadata/path inventory
only.

`package-c-activation-recipe.md` now selects the exact final heads. It remains
prepared instructions for lead execution, with named confctl generation capture,
copy outside machine ownership, dry activation/no-reboot switch and ordinary
application profile switch. No command in it was executed by implementer0.
Existing configuration deployment guidance remains accurate, so no product prose
change or extra main-agent writing pass was needed.

No long tests, system/application builds, claims, activation, merges or lifecycle
actions were performed by implementer0. A/C follow-up-fix ownership is retained.
Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
