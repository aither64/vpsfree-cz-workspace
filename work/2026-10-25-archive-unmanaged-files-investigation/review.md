# Final review: archive preparation

## Findings, ordered by severity

1. **Blocking — load the selected runtime authority before checking live tmux.**
   General / risk lanes; commit `3a28445270eb1df11b949c1fcc4dada7bad424f8`;
   `libexec/workspace-archive-check.rb:8`, `:50`.

   `archive_check` never calls the equivalent of `select_tmux_for_slug!`, so a
   fresh CLI runner still has `@selected_authority = nil`. With a normally
   running, correctly owned tmux session, `cleanup_session` finds the session
   and `ensure_retirement_identity!` rejects it as an untrusted same-name
   session. The portal invokes a fresh CLI for every check, so the retained lead
   cannot fix this blocker: even after relocating the cache, preparation repeats
   it and stops after three rounds. The same issue affects a retained threadless
   shell. The archiver itself loads the authority, which makes its internal
   checker behave differently from the advertised standalone command.

   A focused disposable Ruby probe created a valid authority for a live managed
   tmux fixture, then constructed a fresh runner. Its checker returned
   `ready: false`, five checks passed and the conversation error `refusing to
   retire an untrusted same-name tmux session`. Loading that same authority made
   all six checks pass. The existing new Ruby tests use absent tmux sessions and
   miss this failure. The new native VM scenario starts a real retained lead and
   is exposed to this defect.

   Load and validate the exact slug's selected runtime coordinates in the
   checker, keeping the operation read-only. Do not fix this only by selecting
   the authority and retaining the mutating retirement helper:
   `ensure_retirement_identity!` at `libexec/dev-session:8672` initializes a tmux
   identity and rewrites legacy authority records. A second disposable probe
   confirmed both writes during `archive_check` when such an authority was
   already selected. Use non-mutating validation or return an actionable blocker
   for identity that requires repair. Add a fresh-runner regression with an
   actually present owned tmux session and check that authority and tmux state
   remain unchanged.

2. **Important — recheck cancellation after acquiring the send mutex.**
   Risk / architecture lanes; commit `e0c6c248311cf488f291b9ff3e451e40cc400555`;
   `portal/internal/web/archive_preparation.go:375`, `:400`.

   `withArchivePreparationAdmission` checks the current receipt and active
   preparation at lines 314–324 before its action acquires the message mutex.
   Cancellation acquires that mutex, saves `canceled`, changes the receipt to
   failed and returns success. A worker descheduled between the admission check
   and mutex acquisition can then acquire it and send a new repair turn without
   another state check. Its later persistence fails, but the new native turn has
   already been accepted and can modify local files after cancellation succeeded.
   This exceeds the documented exception for an already accepted cleanup turn.

   A focused Go overlay probe delayed the worker immediately before acquiring
   the underlying message mutex, completed the real cancellation handler with
   HTTP 200 while native sends were zero, and released the worker. The worker
   sent one native repair, then returned `archive preparation was canceled or
   replaced`. The package source was not edited for this probe.

   Validate the receipt, attempt and preparation state again while holding the
   message mutex immediately before reconciliation/submission, retaining the
   existing lock order. Add an overlapping cancel/send regression; the present
   cancellation test cancels before the worker starts and cannot exercise this
   interleaving. The same check should reject work from a superseded attempt.

3. **Important — check the containing directories needed for removal.**
   General / risk lanes; commit `3a28445270eb1df11b949c1fcc4dada7bad424f8`;
   `libexec/workspace-archive-check.rb:66`.

   The permission walk starts at each checkout and visits only its descendants.
   It omits the session group, intermediate containers and the parent needed to
   remove the group. These paths are already available in the discovered
   container inventory. An unwritable checkout parent allows all six readiness
   checks to pass even though Git cannot unlink the checkout from that parent.
   Read-only nested containers similarly fail at `Dir.rmdir` in
   `workspace-archive-cleanup.rb:380`. This is a stable, discoverable blocker;
   the current flow proceeds to quiesce agents and begin journaled cleanup before
   encountering it.

   A disposable Ruby probe changed only the valid checkout's parent group to
   mode 0555. `File.writable?` was false, while `archive_check` returned
   `ready: true`, six checks passed and no blockers. Permissions were restored
   before fixture cleanup.

   Check writable/searchable removal parents and the discovered containers as
   well as checkout contents. Cover the group and a nested container in focused
   tests, with refusal before shutdown or lifecycle evidence is published.

4. **Important — validate retained native identity on the ready path too.**
   General / risk lanes; commit `3a28445270eb1df11b949c1fcc4dada7bad424f8`;
   `libexec/workspace-archive-check.rb:53`.

   The checker calls `ensure_archive_conversations_ready!` in explicit mode.
   For a retained root that helper returns at `libexec/dev-session:9235` after
   checking ordinary manifest shape and endpoint-string provenance. It never
   reads the native thread or validates its cwd, presence, archived state or
   retained team identity. A correctly shaped manifest therefore passes even
   when the selected native backend cannot supply that conversation. The portal
   admission helper also checks only tracking/receipt proof; native metadata is
   read later only when a repair message is needed. A session with no filesystem
   blockers goes directly to archival without that proof.

   This does not require making active turns a blocker. Read-only existence and
   ownership checks can allow an owned active turn. At present predictable
   native identity/availability errors first surface during explicit quiescence,
   after `quiesce_native_client!` and recovery-state changes at
   `libexec/dev-session:9288`. This misses the preflight-before-shutdown contract.

   Add a non-mutating retained-native readiness check shared by CLI and portal
   ready paths. Preserve the existing final journal-owned verification. Test a
   missing/wrong-cwd native root, unavailable native endpoint and retained-team
   identity mismatch, plus an owned active turn that remains permissible.

## Decision

The branch is **not ready for long integration tests** until finding 1 is fixed.
Findings 2–4 also require fixes or explicit recorded decisions under the mandatory
review policy. No implementation fixes were made during this review.

## Scope and history conclusion

Reviewed the complete committed range in the dev-workspace feature worktree:

- Base / merge base: `9634151b9836311c331a58880fbb4c46133fd98f`.
- `3a28445270eb1df11b949c1fcc4dada7bad424f8`: readiness reader, shared discovery
  callback, CLI gate, packaging, command documentation and owning tests.
- `e0c6c248311cf488f291b9ff3e451e40cc400555`: private preparation state, native
  repair orchestration, cancellation/restart, portal presentation, feature
  documentation and unit/native acceptance coverage.

The two commits have distinct, reviewable purposes. Their tests and supporting
packaging/documentation belong with their behavior. I found no superseded
unmerged approaches, abandoned compatibility paths or follow-up fix commits to
consolidate. **No repeated dependency, input, channel or generated-update streams
exist in this range. No history consolidation is required at this head.** Direct
review fixes should be folded into their owning unmerged commit as appropriate.

**No migrations.** The private archive-preparation record introduces schema 1,
but there are no database migrations or intermediate schema-upgrade steps. The
strict lifecycle receipt, archive/cleanup/revival journal formats and final
archive inventory are unchanged. The packet records no merge, release,
deployment or external consumption of this feature, and the inspected series
contains no competing lineage.

## Architecture, compatibility and documentation assessment

The generic runtime is the correct owner: its packaged CLI produces readiness,
the portal consumes it, and the existing archiver remains the destructive
executor. I inspected the pinned codex-web client
`v0.0.0-20261025105210-8b60554bc10c`: the existing send/reconcile ledger binds
text, action context and turn options to the original client message identity.
The preparation retains these coordinates before submission and observes the
accepted turn rather than trusting prose. No protocol or dependency bump is
needed for those methods. Runtime admission releases transition/runtime locks
between model-turn polls, and preparation does not publish lifecycle journals
or coordinator reservations. This is appropriately bounded to explicit archival;
automatic and journal-retry flows preserve their existing policy.

Separate private preparation files avoid adding fields to strict old receipt
readers. Orderly shutdown parks active preparation in a normal failed receipt;
a capable restart checks its original receipt/attempt/target before resuming.
Old packages can ignore the private file, while an intervening receipt change
prevents a later package from adopting it. The actual package-switch/older-reader
boundary is not proven by the mocked restart test and still needs packaged
verification. Package rollback is forward recovery under the existing runtime
policy, not automatic restoration of discarded checkout contents.

The new section of `docs/session-archive-recovery.md` is the right durable home
and is discoverable through README/session documentation. It explains
cancellation limits, preserved archive policy and destructive-phase recovery.
Its readiness and cancellation claims currently overstate the implementation
as described in findings 1–4. The initiative state still has older investigation
and implementation checkpoints; the coordinating agent should reconcile the
current summary and verification phase when recording this report.

## Verification and residual risks

Read the review packet, initiative plan/state/design, applicable workspace and
repository instructions, all four mandatory review lane references, complete
commit messages/file series, final diff, adjacent lifecycle/authority/receipt
owners, shipped UI changes, Ruby/Go tests and the native VM fixture. The worktree
was clean before and after inspection; `git diff --check BASE..HEAD` passed.

Focused reviewer probes used the repository Nix environment and disposable
fixtures only:

- Fresh-runner tmux-authority probe: 1 run, 10 assertions, pass; reproduced
  finding 1 and the difference after selecting the same authority.
- Selected legacy-authority probe: 1 run, 10 assertions, pass; demonstrated
  tmux identity creation and authority rewrite by the supposedly read-only
  helper.
- Container-parent permission probe: 1 run, 19 assertions, pass; reproduced
  finding 3.
- Go cancellation overlay probe: pass, web package 0.126 seconds; reproduced
  finding 2 without repository source edits. The temporary overlay was removed.

Two initial authority-probe constructions needed correction: the first used an
invalid fixture tmux ID, and the second reused the authority-writing runner,
which had already selected its authority. The successful probe uses a valid
saved authority and a fresh reader, matching a new CLI process.

The supplied quick-check results were inspected, not rerun wholesale. No long
integration, VM or live lifecycle operations were run. The synthetic Responses
provider uses a real native shell-tool cleanup, which is stronger than mocked
client tests, but the added VM scenario remains unexecuted and cannot establish
native compatibility yet. Its first scenario is exposed to finding 1.

After remediation, verify packaged repair, restart with inference held,
unrelated creation, old-readable shutdown receipts, browser cancellation and
journal-owned recovery after a post-preflight I/O failure. The test's inotify
permission change is scheduling-sensitive and should retain useful diagnostics
if the intended failure does not occur. External writers can always change
state after a read-only check; final locked validation and existing journals
remain necessary. A new ordinary turn appearing after the accepted repair can
also make the latest-turn identity check refuse safely; this is a manual-retry
case, not evidence that the repair was never accepted.

Reviewer: independent standalone `/root/final_review`; assigned installed-catalog
settings `gpt-6.1-sol` / `xhigh`, fallback because the initiative is threadless and
has no retained eligible reviewer. Overall risk: high. Lanes: general,
architecture/repetition, scope/proportionality, risk/compatibility. No nested
reviewers or subagents were used.
