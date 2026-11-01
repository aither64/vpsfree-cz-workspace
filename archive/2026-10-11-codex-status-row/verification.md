# Compact status row verification

Final exact revisions are in final-heads.json. Quick checks passed: JavaScript
syntax, existing unit browser contracts, focused Go activity/team/server checks
(latest 1.467s), whitespace and final semantic deployment pin contract at 17222c37.
Each feature worktree is clean and each branch has one commit. Consumer locks
change one owning runtime node and select identical revision/content hash;
extension, siblings and follows paths remain unchanged.

Independent final review covered all four applicable lanes and complete branch
history. Its one Important completed-plan visibility finding was restored and
verified directly under the narrow-fix policy. Test-only corrections following
the first browser run exercise that existing contract. See review.md and
review-remediation.diff for scope and conclusions; there are no migrations.

The first real-browser batch exited 1 before builds and CI. Full failure evidence
is verification-v1.log, with atomic verification-v1.status and phase. Question
and presentation tests relied on the obsolete literal accessible name Codex;
the accepted shared row/tab wording makes that dynamic. The new completed-plan
fixture did not emit the existing transcript update event. Stable tab locators,
explicit status assertions and fixture refresh notifications correct the tests.
Production behavior is unchanged by these test corrections.

The second batch exited 1 only in presentation_browser_test.cjs at line 268;
verification-v2.log preserves the complete evidence. Its nonblocking-prompt
fixture retains working state after the earlier answer response, so the lead's
new expectation of Waiting for your answer was incorrect. Corrected that one
test assertion to Codex is working; syntax and whitespace checks passed. All
other browser scripts passed, including compact team and completed-plan cases.
This correction changes no production behavior and is folded into the same
single functional commit with mechanically regenerated consumer pins.

A fresh utility monitor_compact_release owns the final batch in verification.sh,
with complete logs and atomic status/phase. The complete final-head browser suite
passed in 193.773s. Browser coverage
includes Chromium/Firefox desktop/narrow geometry, full hover/accessibility,
wait/approval/answer ordering, completed-plan visibility, stale/failed/late
observations, membership removal, member selection and hidden-page polling.
Runtime/composition/host builds and exact-head CI subsequently passed.

Final batch completed with exit 0 and phase complete. Runtime derivation checks,
composed workspace flake checks and candidate package passed. Each package
variant's Ruby batches reported 405 runs / 5463 assertions / 12 declared skips,
12 runs / 50 assertions / no skips, and 127 runs / 994 assertions / 3 declared
skips, with zero failures and errors. The composed policy/provider and deployment
contract checks passed. The aitherdev build produced generation
2026-10-11--10-45-01; full confctl build output is retained in the configuration
worktree's .confctl/logs/2026-10-11--10-44-34-confctl-build.log.
Final CI [38124238272](https://github.com/aither64/dev-workspace/actions/runs/38124238272)
and superseded 38123891506 succeeded. Every previous superseded CI run also
succeeded. No operation remains running in this verification batch.

Built candidate: /nix/store/v3ysv2w5zxc1rj36fbdrs4x59zh4vckm-dev-workspace-0.2.0,
retained by candidate-package. Runtime transition contract matches the installed
predecessor; native Codex is packaged as a separate root and is checked by the
normal launch-identity gate and post-deploy proof. All final worktrees are clean,
with one complete reviewed/focused-verified commit per repository.

Superseded CI 38122847951 and 38123289184 succeeded. Token permissions refused
cancellation of superseded runs with HTTP 403; no credentials were changed.
38123891506 was observed separately from final-head CI 38124238272; both are
accounted for and succeeded.

Deployment and live acceptance passed; full execution/recovery evidence is in
[rollout.md](rollout.md). The post-deploy check verified health, exact served
JS/CSS bytes and template, selected candidate, unchanged native root, all four
active user units and native/tmux PID continuity. The read-only live browser
check observed focused idle reviewer0 and architect0 with lead working, showing
the peer summary in the sole row without an attention marker. Desktop and
narrow views preserved full hover/accessibility wording, readable timers and
page width. The parent visually inspected both cropped reviewer screenshots.
Atomic rollout.status and live-status.status are 0. Results:
[post-deploy-result.json](post-deploy-result.json),
[live-status-result.json](live-status-result.json).
Fresh exact-ref and saved-diff proof is in [readiness-refs.json](readiness-refs.json).

After separately approved fast-forward integration, master
[CI 38127097132](https://github.com/aither64/dev-workspace/actions/runs/38127097132)
passed on the same runtime head 17222c374bf48c65edc36895e07408c65f1e7b53.
Both fast package/focused checks and master-only host activation, renewal,
rollback and user-service boot tests passed. The fresh utility watch exited 0
in 11m42s with no remaining handles; [merge-ci-result.json](merge-ci-result.json)
records the exact revision and successful conclusion. Final fresh remote proof
confirms every registered feature head merged into its remote master branch:
[integration-final-refs.json](integration-final-refs.json). No rebase, patch
change or second deployment was needed.
