# Committed review remediations

Read review-packet.md and review.md first. All four findings are addressed.
Base remains 9634151b9836311c331a58880fbb4c46133fd98f. Final head is f094a94b50836028a62920c75f2ebd2a9ea97d94.
The two fixes are folded into their owning commits; working tree is clean.
The complete current series is:
fd06d9d9f4aebb581882f3b5d061664c6da95eaa archive: check readiness before stopping agents
f094a94b50836028a62920c75f2ebd2a9ea97d94 portal: prepare archives with lead-assisted cleanup

## Remediations

1. The checker selects saved authority with read_only:true. Authority loaders
   have an additive read-only option, never create missing directories in that
   mode, and the checker validates the creation identity without invoking the
   mutating retirement helper. Fresh modern/legacy-authority regressions prove
   exact authority bytes and tmux identity stay unchanged.
2. A shared current-preparation predicate is checked again while holding the
   native message mutex. The overlapping test delays acquisition after initial
   admission, accepts cancellation, releases the worker and proves zero sends.
3. The checker validates parent directories from discovered containers, checkouts
   and Git administration records. Group and nested-container tests prove refusal
   before shutdown or archive-journal publication.
4. A read-only require-archive-identities team command uses existing native root
   and member proof, permits active turns and rechecks the atomic roster snapshot.
   It never creates members, acquires a writer operation lock or weakens final
   idle checks. It adds ProveArchivedRootThread to the internal teamruntime client
   interface; the pinned concrete client already implements it. This native
   contract/implementation deserves affected architecture/risk/general review.
   The strict executor remains unchanged. Missing/wrong-cwd/wrong-source roots,
   unavailable native endpoint, wrong member cwd/project and active-turn cases
   are covered. CLI flags still bind Codex home, cwd, socket and authority.

## Verification

- Ruby new/remediation readiness batch: 6 tests, 104 assertions, all passed.
- Go preparation/cancellation/native identities/strict archive readiness checks:
  web 3.322 seconds, teamruntime 2.130 seconds, command package compiled; all pass.
- Diff whitespace and syntax checks pass. No long integration test started.

Please perform a real follow-up review of these committed remediations and the
new native identity helper. Reuse your exact saved model/effort. Apply the four
original review lanes where affected, with explicit final history/migration
conclusion after folding. Do not launch subagents or edit implementation. Save
the follow-up report as review-followup.md next to this packet.
