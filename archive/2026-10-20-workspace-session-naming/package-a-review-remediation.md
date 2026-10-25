# A review finding: buffered post-completion errors

Implemented after lead released the completed review finding. Final published
A head: `f722adab914fa34da9d7c66bca63f9515e1ebf6f`. Lead accepted the exact correction and independently
verified the new regression; narrow remediation requires no reviewer rerun.
See `package-a-review-checks.md`, `package-a-review-correction.diff` and
`package-a-reviewed-96077*` for current verification and preserved old evidence.

Candidate: codex-web `96077b6257bd7dac05930312a29eaf00fc900b3c`.
Reviewer IMPORTANT finding confirmed by read-only source inspection:

1. Before `turn/start` reply binds the turn, `handle` validates and queues owned
   error notifications. It also queues exact completion notifications.
2. `bind` replays that bounded queue through `consumeLocked` in order.
3. A transient owned `willRetry=false` error followed by exact failed completion
   sets `transient=true`, `terminalFailure=true`, `settled=true` and a server
   error.
4. The next valid owned error is skipped by `consumeLocked`'s first `err != nil`
   guard. With successful unsubscribe cleanup, this can publish retry proof.
   The same event arriving after binding invalidates proof in `handle`.

Examples of the skipped event are permanent `unauthorized,willRetry=false` and
renewed `serverOverloaded,willRetry=true`. Neither may leave positive retry proof
after exact terminal completion. This is the existing fail-closed contract; no
new accessor, policy or native classification is needed.

## Applied narrow correction

Extracted the existing post-settlement/malformed-error invalidation into one
lock-required helper, used by both immediate handling and replay consumption.
Runs before `consumeLocked`'s existing error short circuit. It must clear
transient proof, retain the protocol-failure category and cancellation behavior,
and preserve early validation, ownership checks and the 32-event queue bound.
Do not move identity binding earlier or treat an error as settlement.

## Focused regressions and checks

Extend the fake-wire retry coverage with the same ordered sequence on both sides
of binding: transient terminal error, exact failed completion, then a valid owned
post-completion error. Cover permanent false, transient true and transient false
post-completion notifications. Early cases send the start reply only after all
events; late cases send it first. Successful cleanup must not restore retry proof.
Assert empty output, existing safe error categories, false direct/wrapped accessor, exactly one
turn/start and one successful unsubscribe, no redundant interrupt of the already
settled turn, and no provider diagnostic leakage. Keep existing ordinary early
terminal proof and native-progress success cases passing.

Known quick command to rerun in the repository's declared environment:

```bash
nix develop --command go test -mod=readonly ./codex -run '^TestEphemeral' -count=1 -timeout=45s
```

After quick checks and explicit authorization, consolidate this correction into
the owning unmerged A functional commit and publish using the exact old-feature
lease. Send the final A head to lead/B once; B and C then refresh their single
dependency/pin streams. Refresh the exact-head native recipe/catalog source path.
Lead owns renewed independent final review and later verification watchers.

Final evidence and lead focused acceptance are in `package-a-review-checks.md`.
Publication and consolidation completed at `f722adab914fa34da9d7c66bca63f9515e1ebf6f`;
B was notified once with the exact immutable source/catalog root. Product source is
frozen again; C awaits B's corrected exact published runtime before one refresh.
