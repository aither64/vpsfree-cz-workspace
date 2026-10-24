# Package C post-review nonpublishing commands

The concrete launch packet is now [package-c-post-review-brief.md](package-c-post-review-brief.md),
with an exact-source manifest and prepared driver. It includes the required
singleton Terraform `workflows` integration command, complete Nix source/input
receipts and serialized watcher instructions. It supersedes the manual launch
outline below. All live commands remain unexecuted and gated on completed review.

Prepared only; none of these live updater/package checks has been run. Use a
fresh verification watcher after complete independent review. Exact source heads
and bases are in `package-c-branches.json`. Prepare clean disposable checkouts
of those exact C heads, their declared development environments and ordinary
hooks. Do not run these in the feature worktrees or a shared checkout. No push,
workflow dispatch, merge or deployment is part of this check.

For each checkout, set `CONFCTL_FLAKE` to
`github:vpsfreecz/confctl/7ba361d22a4aac044cb02abf8397800bcf5726bf#confctl`, supply
`GITHUB_TOKEN` through the watcher environment without recording its value, and
set `RUNNER_TEMP` to an owned directory outside the checkout. Save the original
lock before any command and keep its SHA-256 and initial Git HEAD in the receipt:

```sh
export UPDATE_OLD_LOCK="$RUNNER_TEMP/flake-update-baseline.lock"
cp flake.lock "$UPDATE_OLD_LOCK"
sha256sum "$UPDATE_OLD_LOCK"
git rev-parse HEAD
```

HaveAPI (the helper includes its existing `nix flake check`):

```sh
./utils/update-nixpkgs.sh
```

Terraform provider (retains `vpsadmin` selection and commit format):

```sh
tools/update-vpsadmin-flake-input.sh
```

IRC bot (retains semantic `nixpkgs`; provider resolves its terminal follows):

```sh
tools/update_nixpkgs_flake.sh
```

For vpsAdminOS, run the exact final workflow's `Update flake inputs` and
`Commit and push changes` shell blocks in order, removing only the last
`git push origin "HEAD:${GITHUB_REF_NAME}"` line before execution. The update
command is:

```sh
nix shell "$CONFCTL_FLAKE" -c confctl inputs update --forward-only --all
```

For status, run the exact final workflow's `Update flake input`,
`Update Go dependencies`, `Check committed dependency updates`, `Run tests`,
`Build Nix package` and `Push changes` shell blocks in order, removing only the
last `git push origin "HEAD:${{ github.event.repository.default_branch }}"`
line before execution. Set `UPDATE_START_REF` to the original checkout HEAD.
This preserves the existing Go dependency/vendor update and package checks.
The guarded update command inside that workflow is:

```sh
nix shell "$CONFCTL_FLAKE" -c confctl inputs update --forward-only nixpkgs
```

Bind extracted shell blocks to the exact reviewed source blob and inspect that
no publication command remains before running them. Do not reimplement their
metadata, commit-format or dependency-update logic in the verification driver.
Preserve existing required long checks, including Terraform's integration test
procedure, under the lead's final verification selection.

After each successful helper/check sequence, use the same final check as the
workflow; it validates the published Git blob, not mutable worktree bytes:

```sh
final_lock="$RUNNER_TEMP/flake-update-final.lock"
git show HEAD:flake.lock > "$final_lock"
nix shell "$CONFCTL_FLAKE" -c confctl inputs check-update \
  --old-lock "$UPDATE_OLD_LOCK" --new-lock "$final_lock"
git log --format='%H %s' -3
git status --porcelain
sha256sum "$UPDATE_OLD_LOCK" "$final_lock"
```

For an update rejection (3), stop the sequence before commit/publication and
record full old/candidate revisions and path/reason; verify original lock/index/
HEAD remain unchanged. An evidence failure (1) needs diagnosis and is not a
successful rejection. Live channel state can legitimately reject, so do not
force an update or retry from a rebased stale candidate to obtain success.

Receipts must name exact C/provider heads, actual packaged Nix executable and
version (the wrapper prepends its own Nix), selected input/terminal path,
commands/statuses, baseline/final hashes, generated commits, log paths and any
unfinished operation. Compare status/IRC parent revisions to prove only their
resolved leaf selection advanced. The focused offline 40-scenario receipt is
separate evidence and does not substitute for this package/runtime validation.
