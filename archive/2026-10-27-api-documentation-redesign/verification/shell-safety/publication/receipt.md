# Shell-safety publication

Published `2026-10-27-api-documentation-redesign-shell-safety` to
`git@github.com:vpsfreecz/haveapi.git` after accepted independent final review.

- Head: `ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b`
- Tree: `30efb19e02a756036771767745a9858fe968f95b`
- Parent: `ae46cf27a9afb6558d386c293cec7231dd6c423d`

Fresh SSH observation found the target absent. One full-SHA push used the
absent-ref lease, `--no-follow-tags`, and normal executable pre-push hooks in
the existing declared frozen root environment. It exited 0 in 3.156109843403101
seconds. Fresh SSH readback confirmed the exact head and tree.

All 195 pre-existing remote refs, symbolic default, and pre-existing local refs
were unchanged; no unrelated additions appeared during this publication window.
Original 2f6, style 1b and instructions ae46 refs remained unchanged. Candidate
source/index stayed clean; checked source hashes, locks, copied guide and hooks
were unchanged. Fetch, push and readback handles completed without uncertain
effects. SOURCE/Git/NETWORK ownership was explicitly RELEASED before CI.

Authoritative operation evidence: [result.json](result.json),
[push-exit.json](push-exit.json), [push.log](push.log),
[remote.before.txt](remote.before.txt), [remote.after.txt](remote.after.txt).
The result's `no_CI_query_yet` records the release checkpoint before the query.

One initial exact-head CI metadata snapshot at
`2026-10-29T22:40:44.757751+00:00` returned ten attempt-1 runs:

| Status at snapshot | Workflow | Run |
| --- | --- | --- |
| Success | i18n health | 40967607802 |
| Success | RuboCop | 40967607946 |
| Success | Python | 40967607853 |
| Success | PHP | 40967607822 |
| In progress | Server RSpec | 40967607913 |
| In progress | Server performance | 40967607906 |
| In progress | JS | 40967607924 |
| In progress | Rust | 40967607851 |
| In progress | Go RSpec | 40967607878 |
| In progress | Ruby client RSpec | 40967608013 |

Release was absent from this snapshot; whole-head CI success is unestablished.
See [ci-initial-summary.json](ci-initial-summary.json) and
[raw metadata](ci-initial.json). No waiting, polling, reruns, dispatches,
logs/artifacts, tests or builds followed. No active or uncertain owned effects
remain. Lead received publication/release promptly, then the snapshot status.
Independent security re-audit remains lead-owned; no default integration,
consumer update, deployment or lifecycle action was performed.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/)
