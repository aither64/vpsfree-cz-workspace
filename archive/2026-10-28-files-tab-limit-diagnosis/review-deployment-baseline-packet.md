# Affected final review: latest deployed archive baseline

User authorized "deploy it", then explicitly "Deploy only; leave the branches
unmerged". Do not merge, acquire repository claims, archive, stop or clean this
session. Actual deployment driver remains lead-owned after review and materialized
artifacts. Prior review.md/review-successor.md stay valid for unchanged scope.

## Exact final source and why it changed

At fresh pre-activation check, current live profile changed externally to
`/nix/store/kdqm98kwk1mly4i1rfx58lnz6cscn6z6-dev-workspace-0.2.0`, runtime
`76c9ad4fbd877992464d2a7f2a1a2fe60db043b1`, native Codex unchanged. Live system
also selects76c9. This is now runtime remote master. Our prior6a1 candidate
would drop that substantive already-deployed fix; no activation/claim occurred.

Upstream76c9 atop reviewed2caa changes exactly4files,+312/-37:
`docs/session-archive-recovery.md`,
`portal/cmd/workspace-portal/archive_explicit_test.go`,
`portal/internal/workspacecodex/archive_explicit.go`,
`portal/internal/workspacecodex/archive_explicit_test.go`.
It interrupts ancestry-proven native utilities outside managed admission while
preserving managed root/member retry and submission safeguards. Independently
inspect this affected behavior and tests, not just the owner's description.
No actual lifecycle operations are authorized or required by this review.

Runtime owner rebased only our Files commit6a1 onto76c9. New final runtime
`dd445cb0627f93375f1378af6b59d30ef8b34875`, base76c9. Range-diff
`2caa9419..6a1bfad8` versus `76c9ad4f..dd445cb0` is `=`. All14 task-owned
changed files byte-identical, including full app.js/assets/docs/API/scanner/tests.
Old6a1-to-dd differs only the upstream4files. No archive code authored here,
no Files design, asset-version, schema or dependency change. Parent independently
checked key Files sources identical. Quick Nix-shell checks passed web10.521s,
cmd1.178s, workspacecodex0.087s: Files/API/browser/assets and two disposable
archive watcher boundary tests. No live session lifecycle mutation.

New full historical series from initial4a002f52 is8commits:
cc106266,e9153e61,d0a9c5f6,fd9128a1,2beb55e2,2caa9419,76c9ad4f,dd445cb0.
Current remote-master-to-feature is exactly one Files commit14files,+1140/-92;
full initial range57files,+4069/-191. Prior reviewed inherited policies remain
supported; no predecessor review/approval is invented. Require final whole-history
and migration conclusion for the changed range without repeating unchanged review.

## Matching final consumers

All own worktrees are clean and published on branch
`2026-10-28-files-tab-limit-diagnosis` under the session worktree root.

| Repository | Base | Final head |
| --- | --- | --- |
| dev-workspace | 76c9ad4fbd877992464d2a7f2a1a2fe60db043b1 | dd445cb0627f93375f1378af6b59d30ef8b34875 |
| workspace | 4a3a9bd39fd244de49665853535fc87d5e8373e5 shared master | 10344897ad051dd68ec3adfc21f949e7cc52ec47 |
| vpsfree-cz-configuration | 7c999104833e8cf2dd8ac779a9e8e51876fb7d85 | c8e9701614fdb3735d086f7591a29cdfe1e4d453 |

Workspace remote base9d35428a8c8f82bf5f51aaf3adf23d2b338542f0 selects76c9;
shared base adds only two inherited tracking archive commits. Inventory metadata
only; do not open peer records, worktrees or transcripts. Task range one pin
commit, flake.nix/lock+5/-5. Configuration one regenerated confctl pin,+3/-3,
truthful76c9-to-dd generated changelog; required hooks passed. Exactold-head
force-with-lease publication and comparisons captured. No intermediate task pins
remain; old6a1/109/230 ranges and evidence stay in rollout receipts.

Both final locks select dd445 with
`sha256-5tPigdC6kl1wC4e8eaoo8XoPJnUnu9Yyb1caS0+Glpk=`. Quick deployment
contract passed. Complete semantic comparison: only intended runtime node
changes; all siblings/edges/follows, extension and native unchanged. No DB
migrations; review inherited communication/reporting/drop state conclusion
remains, not persistence-neutral.

## Bounded review and verification

Retain reviewer0 saved Sol/xhigh. Apply affected general/history,
risk/compatibility/lifecycle and scope review, reuse unchanged Files/architecture
inspection. No nested agents, source edits, long checks, actual archive, merge,
claims or deployment. Write `review-deployment-baseline.md`, keep old reports.
Report concrete blocker promptly, otherwise concise final conclusions.

Selected live runtime/composed source and exact graph receipts are in
rollout-preparation.md. Candidate runtime srcb5dmhd08..., compositionys3968dr...;
new composition drv k03x0d1pswirhpm04xbip8c6in6gxnys and contract
bq29dv61k6yv7q3x1dqngqqgn3xzkmhb. Owner independently compared the entire Ruby
aggregate .drv and16dependency identities to live76c9: identical. Native
derivationlh1jkv... identical. Some old outputs were GC'd; availability is not
proof and materialization is required before activation. No stale6a1 rebuild.

After review, build rooted final composition+contract (fullGo/Ruby/protocol/
browser checks) and exact host generation; monitor exact new CI40757650687.
Do not duplicate the unchanged generic runtime suite without a concrete gap.
Native Files/settings smoke's only prepared edit is expectedHEAD6a1-to-dd,
actual shipped assets and pinned environment unchanged; execute after review.
No new output success claimed yet. Lead acquires aitherdev only near prepared
activation; user refuses integration, so deployed claim remains held under
selected policy until later integrated-lineage evidence. No lifecycle action.
