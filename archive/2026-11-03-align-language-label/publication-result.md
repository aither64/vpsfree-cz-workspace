# Feature publication and CI

The independently reviewed head is published and all nine exact-head CI runs
passed on their first attempt. The worktree is clean and ready, awaiting merge
approval. There is no default-branch integration, deployment or release.

## Exact publication

- Repository: `git@github.com:vpsfreecz/haveapi.git`.
- Feature branch: `2026-11-03-align-language-label`.
- Reviewed/published head: `b606b4b3c32bf05779c05babeaa1c31a33dee6fa`.
- Fresh fetched `origin/master` and remote `master`:
  `f29c1e4675bc1f79641faa619b8c68ecec923c71`.
- `git rev-list --left-right --count origin/master...HEAD` returned `0 1`.
  No rebase or history mutation was necessary.
- `nix develop -c git push -u origin HEAD:refs/heads/2026-11-03-align-language-label`
  exited 0 with normal hooks and created only the feature branch.
- `git ls-remote --heads origin refs/heads/2026-11-03-align-language-label refs/heads/master`
  confirmed both exact remote revisions above.
- Public `dev-session worktree capture-comparison 2026-11-03-align-language-label haveapi --as-is`
  saved base `f29c1e4675bc1f79641faa619b8c68ecec923c71` and
  head `b606b4b3c32bf05779c05babeaa1c31a33dee6fa`.

The one-commit range and one-line CSS diff are unchanged from the passing
[independent final review](review-result.md). Local quick checks and required
commit hooks are recorded in [implementation result](implementation-result.md).
No migrations or compatibility changes are introduced.

## CI batch

Exact-head push runs discovered through `gh run list --commit`:

| Workflow | Run | Final conclusion |
| --- | --- | --- |
| clients/rust | [41724762299](https://github.com/vpsfreecz/haveapi/actions/runs/41724762299) | success |
| clients/php | [41724762419](https://github.com/vpsfreecz/haveapi/actions/runs/41724762419) | success |
| i18n health | [41724762346](https://github.com/vpsfreecz/haveapi/actions/runs/41724762346) | success |
| servers/ruby RSpec | [41724762893](https://github.com/vpsfreecz/haveapi/actions/runs/41724762893) | success |
| clients/js tests | [41724762273](https://github.com/vpsfreecz/haveapi/actions/runs/41724762273) | success |
| clients/python | [41724762283](https://github.com/vpsfreecz/haveapi/actions/runs/41724762283) | success |
| clients/ruby RSpec | [41724762649](https://github.com/vpsfreecz/haveapi/actions/runs/41724762649) | success |
| clients/go RSpec | [41724762240](https://github.com/vpsfreecz/haveapi/actions/runs/41724762240) | success |
| servers/ruby performance | [41724762471](https://github.com/vpsfreecz/haveapi/actions/runs/41724762471) | success |

A fresh operation-only Luna/low watcher completed observation of these nine exact
runs under the pinned/installed catalog digest
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7` and
installed full-access execution policy. Every run's `headSha` matched the
reviewed/published head. Observation took approximately six minutes. No failed
jobs or steps occurred, no reruns or cancellation were performed, and no runs
remain active. No redundant local long suite was launched. See the
[watcher evidence](ci-watch-result.md).

At the lead-requested progress checkpoint, the watcher reported approximately
four minutes since its initial status reads: eight runs had completed
successfully, with only `41724762471` (servers/ruby performance) still running.
Its active job was `Compare endpoint performance`, step
`Run the selected pair outside Bundler`. No failure had been observed.

After the final CI result, `git status --short` remained empty and a second
`git ls-remote` confirmed the same exact feature and master heads above.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-align-language-label/)
