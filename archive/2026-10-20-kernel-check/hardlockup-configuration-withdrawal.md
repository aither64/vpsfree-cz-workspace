# Configuration change withdrawn

The user moved panic policy into vpsAdminOS alongside the existing soft-lockup
policy. The former site sysctl commit is withdrawn. Implementer2 owns the OS
replacement under [the accepted brief](design.md#move-panic-policy-to-vpsadminos).
No configuration input update accompanies this relocation.

The replacement is published as vpsAdminOS commit
`f3e91f6213934bf5d1a2ca52a7fdc6e63941a647` on staging base
`252b80dfdb4bced0713e8423ef7ba3d5600d05dd`. See the
[OS implementation and verification packet](os-hardlockup-verification.md)
for its exact scope, passed quick checks and final-review handoff. This link
does not imply integration, downstream consumption or deployment.

Repository `vpsfree-cz-configuration`, retained branch
`2026-10-20-kernel-check`, worktree
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-kernel-check/vpsfree-cz-configuration`:

| Identity | Final value |
| --- | --- |
| Comparison base and feature head | `37a338b25192d9271ee211110800c2dc6a094a57` |
| Remote master and retained feature ref | `37a338b25192d9271ee211110800c2dc6a094a57` |
| Final tree | `3fe68adea99cb4c69568bd1c1d1fb0866ccdbe40` |
| Local master, unchanged | `86e19685313270d88e4db30038c056ce4b807abd` |
| Feature commits / final diff | 0 / empty |

Before rewriting, exact SSH fetch and ancestry checks established that obsolete
commit `8515b68288be7f6c78ed010f93d1424c377973fd` was not an ancestor of current
remote master. Only the owned local and remote-tracking feature refs contained
it; default source/history had no hard-lockup sysctl assignment. Session records
and public coordination status showed no integration, deployment or known
supported external consumer. The prior system builds failed before compilation
or deployment. These checks are bounded session/ref evidence, not a claim about
unobservable external use. See [preflight](hardlockup-withdrawal-preflight.json).

After the lead's explicit bounded brief (subsequently matched by the architect's
written brief), the clean owned worktree used its declared Nix environment and
ordinary hooks for:

```sh
nix develop -c git rebase --onto \
  37a338b25192d9271ee211110800c2dc6a094a57 \
  8515b68288be7f6c78ed010f93d1424c377973fd 2026-10-20-kernel-check
git push \
  --force-with-lease=refs/heads/2026-10-20-kernel-check:8515b68288be7f6c78ed010f93d1424c377973fd \
  origin refs/heads/2026-10-20-kernel-check:refs/heads/2026-10-20-kernel-check
```

Both commands exited 0. [Rebase log](hardlockup-withdrawal-rebase.log),
[push log](hardlockup-withdrawal-push.log) and
[remote proof](hardlockup-withdrawal-remote.txt) retain the results.
`git status --porcelain` is empty; `git diff --exit-code origin/master HEAD`
passes, and `git rev-list --count origin/master..HEAD` returns 0. The old commit
is absent from final history; it was dropped rather than paired with a revert.
The branch/ref remains published. Local and remote master were not changed.

The true registration base remains `86e19685`. Its six commits through final
head are existing upstream baseline history: `38687a84`, `4da29db6`,
`86bb8a73`, `d5c95e93`, `9a31f946`, `37a338b2`. They are not feature-owned
updates. The final feature range contains no obsolete approaches, migrations,
dependency/input/channel updates or generated artifacts. No migration was
merged, released, deployed or externally consumed by this package.

The [branch CI query](hardlockup-withdrawal-ci.json) returned no runs, so no
superseded active run needed cancellation. No missing-secret system build was
rerun for the withdrawn configuration assignment. No reset, clean, stash,
commit addition, ref deletion, merge, deployment, production change or lifecycle
action was performed. No owned operation remains active.

[Final identity receipt](hardlockup-withdrawal.json) records exact pre/post heads
and checks. The [previous verification package](hardlockup-verification.md)
and its accepted review/build-failure receipts remain historical evidence for
`8515b682`; they do not certify the separate OS implementation.

The native comparison refresh was attempted with exact final base/head but
refused because they are identical (`comparison base and head are identical`).
No false nonzero comparison or manual manifest edit was substituted; this
registered withdrawal artifact provides the final zero-diff proof. Any retained
comparison for `8515b682` is historical.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/>
