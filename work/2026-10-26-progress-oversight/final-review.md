# Final review: progress oversight

Reviewed runtime `960dd816b7e56cbdd4af0da15bf0b26257775151..d4e59794e593db46e497b07b1dd7148704b4347f`
and workspace `0fe886f56031da55d16aa30e6f110243a0ed0e28..45b6b6e445e0668bc17f1d46ab07d6b8a14b3cc3`.
All four lanes: general, architecture/repetition, scope/proportionality, and
risk/compatibility. Independent standalone review; no source edits or long tests.

## Findings

1. **Blocking: scheduled observer failures enter the ordinary automatic retry worker, which can run inference while development is idle and outside the observation budget.** Runtime commit `d4e59794`, `portal/internal/web/progress_observer.go:407` submits through `workspacecodex.Client.SendWithOptions`. That method captures normal retry snapshots (`portal/internal/workspacecodex/turn_retry.go:305`), and the existing retry worker includes every ready team member (`portal/internal/web/turn_retry.go:165`), including observers. Session retry policy enables capacity and cybersecurity retries by default (`portal/internal/turnretry/policy_store.go:265`). Reproduction sequence: schedule a progress check; finish all non-observer work; fail the observer turn with `serverOverloaded` or `cyberPolicy`. The retry worker can start a continuation with no non-observer activity check. Its new turn is also outside `Pending.Turn`, so the progress deadline refuses to interrupt it. Repeated capacity failures can continue beyond three minutes. Pausing progress does not control this worker either. Keep automatic progress submissions out of ordinary retry dispatch, or make their retries subject to the same active-development gate, owned identity and original deadline. Preserve ordinary manually requested observer assignments if those retain normal retry behavior. Add a regression using the real workspacecodex retry admission/worker boundary; the current progress fake overrides `SendWithOptions` and cannot catch this. Lanes: risk/compatibility, architecture, general; contradicts the explicit idle and budget scope.

2. **Important: unrelated development transcript/activity failures prevent an already-running observer from reaching its timeout.** Runtime commit `d4e59794`, `portal/internal/web/progress_observer.go:258` and `:279` perform root verification, root reads/activity and every non-observer member read before processing `state.Pending` at `:293`. Any error returns immediately. For example, after a check starts, one active implementer's activity snapshot becomes stale or its transcript read repeatedly fails while the observer remains reachable and active. Every sweep exits before the exact owned-turn cancellation at `:323`, so the three-minute budget is unenforced for the duration of that unrelated failure. Settle/cancel an existing owned pending check independently of collecting evidence for a new check; failed development activity should prevent new inference and notices, without preventing reachable pending-turn cleanup. Test an overdue pending observer with failing lead/member evidence. Lanes: general, risk/compatibility.

3. **Important: removing and re-adding an observer can permanently block progress checks for that root.** Runtime commit `d4e59794`, `portal/internal/web/progress_observer.go:294` preserves `state.Pending` whenever the selected observer differs. A check can finish between minute sweeps, then the user removes that now-idle observer and adds a replacement through the supported team controls. The pending record still names the old member; every later sweep returns `scheduled observer changed`, and `State.Due` cannot admit a check while `Pending` exists. Pause/resume does not clear or reconcile it. The same problem occurs if the first of multiple observers is replaced while another remains ready. Reconcile the saved observer identity against its retained retirement/completion evidence and retire the old pending check safely, without transferring its ownership to the replacement. Add a remove/re-add regression after native completion but before result collection. Lanes: general, risk/compatibility.

## History, contracts and scope

The runtime's complete feature series is one cohesive behavior commit with its
supporting tests and docs. The workspace's three commits separately cover
verification policy, team defaults and the generated runtime selection. No
obsolete feature approaches or fixup history remain in these reviewed ranges.
There is one runtime input update and no repeated update streams requiring
consolidation. The final lock change preserves the extension and sibling inputs.

The workspace remote merge base currently also precedes three shared-master
coordination commits (`ef1b79d33`, `7d5ac6860`, `0fe886f56`); their diffs contain
archive/session tracking and prepared KB artifacts, rather than additional
progress-feature implementation. The supplied feature base is the current local
master. Recheck the target and final range before integration.

**No migrations.** The separate optional schema-1 progress record has no
intermediate upgrade migrations, and the packet records only disposable use.
Roster, lifecycle and native protocol formats remain unchanged. The owning
runtime/docs and site policy split is appropriate; full-access execution remains
an established behavioral trust boundary. The verification guidance is bounded
and does not waive required checks. No unrelated framework or approval gate was
introduced.

## Evidence and remaining limits

Inspected both complete feature series and final diffs, the runtime's retained
team, activity, submission and retry consumers, pinned codex-web paging, relevant
tests and documentation. Both feature trees are clean; `git diff --check` passes.
The supplied focused checks cover basic idle handling, concern recurrence,
response capture, restart identity and exact-turn interruption. They do not
exercise the retry interaction or the pending failure/replacement cases above.
Broader packaged validation and the disposable pilot remain pending. Do not
claim final readiness until the findings are resolved or handled under the
mandatory review policy.
