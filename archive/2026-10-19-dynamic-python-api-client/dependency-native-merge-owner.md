# Native dependency-refresh merge receipt

The user approved merging HaveAPI into master after verification and requested no release.
The lead granted preflight, then native fast-forward/master-only SSH publication under
held claim `d58eb8f6-0789-4ad6-829d-b6bd7927cc91` revision 2.

- Old master: `c1823f3d70365b0442d0e2171bdf83bd4c6dbe31`.
- Final local/remote master and retained feature: `a8ea3132e7efe601aaa8965afe648459b3dab5c5`.
- Final tree: `9a596258d912ca2075c36ded30d11b3984c656ae`.
- Ordinary declared root Nix environment, native Ruby 3.4.11 and existing prepared gem home used.
- The four-commit/seven-file reviewed diff remains unchanged; no migrations or history rewrite.
- Fresh owned temporary target checked out exact prior master. Native checkout and explicit normal post-checkout hook both exited 0.
- `git merge --ff-only a8ea3132e7efe601aaa8965afe648459b3dab5c5` exited 0; the explicit normal post-merge hook also exited 0.
- Explicit normal pre-push hook with actual old/new master update exited 0; native non-force `git push origin refs/heads/master:refs/heads/master` exited 0.
- Historical/final configuration and both custom hooks were byte-identical. Signature verification stayed enabled; no signing, trust change or bypass was needed.
- SSH ls-remote independently confirmed master and retained feature at the final head. Target and feature were clean at the exact final tree. All four frozen component locks remain unchanged.

## Bookkeeping assertion and independent verification

After successful publication, the execution helper exited 1 at its ref-map assertion.
It expected master and origin/master to advance but omitted the resolved object change
of symbolic origin/HEAD, which still points to refs/remotes/origin/master. The original
`result.json` retains state failed and `commands.log` remains unchanged. No successful
Git operation was retried, and the original helper execution is not relabeled as passed.

The separate post-effect receipt verifies the expected symbolic target and recent
master/push reflogs, both exact remote heads, tree and cleanliness. Then the authorized
ordinary `git worktree remove` removed only the fresh dependency-merge target, exit 0.
No owned process had a working directory in that target. All original command handles
and follow-up commands completed; no fixture or background verification was launched.
The complete 2,173-ref map was equal immediately before/after target removal, SHA256
`597ea4ca8935d76593e4b3a46c0e430a9f850514583dc54a1138f1506c792a92`.
The stash ref/object `bd8d94b3b6f40a60a18aa4b30c03193459890495`, recovery refs,
retained feature and old coordinator payloads remain preserved.

## Initial master CI snapshot

Read-only exact-head initial inventory; no wait, retry, cancellation or watcher.

| Workflow | Run | Observed state |
| --- | --- | --- |
| clients/ruby RSpec | [39500813934](https://github.com/vpsfreecz/haveapi/actions/runs/39500813934) | success |
| release | [39500813821](https://github.com/vpsfreecz/haveapi/actions/runs/39500813821) | in_progress |
| i18n health | [39500813837](https://github.com/vpsfreecz/haveapi/actions/runs/39500813837) | success |
| RuboCop | [39500813782](https://github.com/vpsfreecz/haveapi/actions/runs/39500813782) | success |
| clients/python | [39500813822](https://github.com/vpsfreecz/haveapi/actions/runs/39500813822) | success |
| clients/go RSpec | [39500813857](https://github.com/vpsfreecz/haveapi/actions/runs/39500813857) | success |

## Evidence

- [preflight.json](verification/dependency-refresh/native-merge/preflight.json): SHA256 `ee3538c9e16d85b38393e8927ac5f7bfc2bb4ccf14b554a08c0a5782b479219a`.
- [commands.log](verification/dependency-refresh/native-merge/commands.log): SHA256 `efdf7aac1000eeee817dea0b6e0714ec951df474291e99a82e71412ae8d618c5`.
- [result.json](verification/dependency-refresh/native-merge/result.json): SHA256 `dadc52dde2d33b6d15301b1d7869b4e4fec4707e3f26e6192bcfed305a6fd139`.
- [post-effect-verification.json](verification/dependency-refresh/native-merge/post-effect-verification.json): SHA256 `f33f134c94e5a6845d7f9f4ccba493a7d1f776a7a750b18c82c48b01052f6343`.
- [cleanup.log](verification/dependency-refresh/native-merge/cleanup.log): SHA256 `88dd01cc0ae1ef6b501c2d4a1e14ed300c4f35e8df628e5ae44ac5d76e03dd1b`.
- [master-ci-initial-runs.json](verification/dependency-refresh/native-merge/master-ci-initial-runs.json): SHA256 `625c96f970c194862a2678f8880ffc99e0c1fb8a427722bffea3a8d8a2f53ef6`.
- [master-ci-initial-jobs.json](verification/dependency-refresh/native-merge/master-ci-initial-jobs.json): SHA256 `ad69e328c5d8eafd264d6db0dce800dd90960d0562501aa56bfb8416d4f7ffef`.

The lead owns claim release and post-merge CI monitoring. No source changes, local
test repeats, tag/version/registry/PR/release/deployment or session lifecycle actions.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-dynamic-python-api-client/
