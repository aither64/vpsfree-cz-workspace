# User-directed removal of HaveAPI guidance

The proposed vpsAdmin-specific HaveAPI documentation change has been removed
from this session's feature series and remote feature branch. The user rejected
it as a separation violation. No replacement policy was added to HaveAPI.
Rust documentation is unchanged.

## Verified range and operation

Before mutation, the owned branch was clean and had exactly one commit beyond
fresh public master:

- Old range: `f29c1e4675bc1f79641faa619b8c68ecec923c71` ..
  `dd200cc862b402c31f68a230de990de083efe306`.
- Sole commit: `docs: route vpsAdmin downstream client synchronization`;
  `AGENTS.md` plus `doc/agent-instructions/development.md`, 19 added lines.
- Fresh remote master remained `f29c1e4675bc1f79641faa619b8c68ecec923c71`.

Ordinary `git rebase --onto <master> <old-head> <owned-branch>` transplanted
the empty range, dropping that sole unmerged documentation commit. Normal hooks
remained enabled in the already prepared owned environment. No reset, revert
pair, new commit, default-branch write, merge claim or new setup/check suite.

Published over SSH with exact lease:

```text
--force-with-lease=refs/heads/2026-11-03-vpsadmin-client-sync:dd200cc862b402c31f68a230de990de083efe306
```

After push, local owned HEAD, remote feature and remote master all equal
`f29c1e4675bc1f79641faa619b8c68ecec923c71`. Tracked tree is clean,
master-to-feature commit count is 0, and the complete diff is empty.
No migrations, application/runtime/version/schema changes or replacement policy.

## Preserved recovery and review evidence

- Old reviewed head retained as
  `refs/dev-session/2026-11-03-vpsadmin-client-sync/rejected-vpsadmin-guidance`.
- Original patch retained at `haveapi-guidance-rejected.patch`, SHA-256
  `b394966f397b974e274630067ec7556bb3f91bd9e30c7d60e9507eb5a8656f12`.
- Original review packet/result and old/new transplant ranges remain in
  phase2-review-packet.md, phase2-review-result.md and phase2-rust-haveapi.md.
  Their former no-findings conclusion is historical; the user's scope rejection
  supersedes the HaveAPI proposal.
- Immutable detached generator checkout `haveapi-generator-0.32.2` and public
  `v0.32.2` still resolve cleanly to
  `1ef9b204ba45bb261d3334be5c555cc1856b713b`.
- Original manifest `initial_base_sha` remains that same old generator pin.
  Source/export/release receipts were not rewritten; no old pin is called merged.
- Rust remains clean at `823a4f8450fce4947310fc81bcdebdca91d9ffae`.

The supported explicit comparison capture was attempted with base=head=f29c1e46.
It refused: `workspace-portal: comparison base and head are identical`.
No private override or metadata edit was used. The prior captured reviewed range
remains historical; exact Git/remote evidence above proves the current zero range.

## CI and remaining authority

Superseded branch runs 41678912445 and 41678912475 were already terminal
success. No superseded active run existed, so none was cancelled. The ordinary
feature update naturally triggered current-head performance run
[41720217170](https://github.com/vpsfreecz/haveapi/actions/runs/41720217170)
at f29c1e46; it was in progress when handed to lead. It was not cancelled or
claimed as verification of a new feature. No manual tests/builds or workflow
dispatch were added for this removal.

The lead then assigned one fresh CI-only utility to account for that existing
run. Final GitHub run/jobs JSON confirms **completed/success** at the exact
f29c1e46 SHA, updated `2026-11-03T21:23:49Z`:

| Job | ID | Conclusion |
| --- | --- | --- |
| Compare endpoint performance | 126210688768 | success |
| Performance gate | 126214810059 | success |

The benchmark completed; `Record no-work selection` was skipped. Acceptance is
based on the actual terminal run/job conclusions, not the watch wrapper's exit.
Evidence in `haveapi-removal-ci/`: `run-41720217170.json` (full final run/jobs),
`run-41720217170-watch.log`, `run-41720217170-watch.exit` (`0`), and
`run-41720217170-watcher-result.txt`. No failed job required additional evidence.

Utility `/root/haveapi_baseline_ci_watcher` used fresh context, gpt-6-luna/low,
pinned catalog `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
native identity `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, and
danger-full-access/approval-never policy. It verified `dev-session current` and
both environment markers for this bound session, read the matching native config,
and observed only this run for approximately 7m50s. No tests, builds, workflow
dispatch, source edits, retries, cancellations, diagnosis or nested utility.
No operation remains running; the single utility slot was released to lead.

This accounts for an automatic baseline run. It establishes no new HaveAPI
feature-content gate and authorizes no baseline-product fixes.

Lead owns relocation and remaining integration coordination. Conditional user
approval requires the migration session to finish; no integration was performed.
No default push, deployment, lifecycle action, unregistration, ref deletion or
cleanup. Session and retained source checkouts remain open.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)
