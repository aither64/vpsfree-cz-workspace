# Current compact performance evidence handoff

Final head `39e98020070fabcceca32f8fabcf0440f0d8763e` is one coherent commit
atop integrated `1741a25e1df45f06f9966942d5c34a97967ebb3e`. Full series:
`39e98020070fabcceca32f8fabcf0440f0d8763e performance: measure representative request batches`.
Full diff: 18 files, +1346/-239; compact delta from stable reviewed
`bdb034436e0dffbc39537a481442c3a2880cea9c`: 9 files, +148/-82.
All earlier backup refs and original evidence remain retained. Checkout/index
clean; no running handles, push, integration, backport or publication.

The single required `make test-performance` passed 124 examples, zero failures,
exit 0 in 68.014 seconds (`compact-quick.log`, `compact-quick-result.json`).
Final eight-file RuboCop, ordinary pre-commit/commit-message hooks and diff
checks passed. Only layout corrections followed the suite. Original focused
40-example failure remains in `compact-focused.log`: inconsistent test-only
operation counts were corrected, and the full suite passed. Real repeated API
coverage retains one response example/count 8 and one counter record for eight
operations. A controlled three-case report serializes to 3,011 bytes without
samples or bodies. Last-operation and malformed summary/provenance negatives,
meaningful regressions, auth/version/source checks remain covered.

Samples format 2 retains metrics, distinct response examples/counts and one
uniform validated counter record/count. Live checks still validate every
operation. Replay checks retained summaries and identities; it does not reprove
individual request ordering or every live authorization/counter operation.
`doc/performance.md` documents that boundary and unsupported-format rejection;
the lead accepted its final plain-English pass. Reports contain identities and
per-case metric/correctness results only.

No migrations, persisted-state, production runtime/API or published dependency
changes. No obsolete update stream remains in the one-commit series; exact
JSON development preparation remains consolidated. This compact amendment
changes no fixtures, calibrated budgets, reference, locks, environment, workload
inventory, batch policy, cap, timing/allocation thresholds or workflow limits.
Affected independent final review precedes hosted quick/weekly and master
integration, then exact master backport and separate release metadata.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/>

## Historical batching receipts (superseded heads)

# Representative batching: current master handoff

Current base `1741a25e1df45f06f9966942d5c34a97967ebb3e`; final feature head
`68464a7fbf662c31df4d743a8edc82d6093c3406`. One coherent commit,
11 files, +625/-154. Checkout/index clean; no commands running. No push,
integration, backport or publication performed. Review remains lead-owned.
Full inventory and binary diff: `batching-master-68464a7f-inventory.json` and
`batching-master-68464a7f.diff`. Prior local heads 344351/44c53/db14 are superseded;
their receipts remain historical and the narrow amended deltas are documented.

Quick checks: 102 performance examples passed in 65.33s; final 24 affected
examples passed in 32.7s after count/warmup, watchdog and replay refinements.
The review finding's workflow assertion passed its sole affected example after
the weekly timeout amendment. Eight changed Ruby files passed lint; ordinary
pre-commit and commit-message hooks passed. Commit-message lines satisfy the
80-column requirement. Final amendment hooks passed without warnings.
Logs: `batching-focused-checks.log`, `batching-final-affected-reconciled.log`,
`batching-lint-accepted.log`, `batching-timeout-assertion-{focused,amend}.log`.

The live 256-operation control measured 0.829103s baseline and 1.217886s
candidate and detected the slowdown. Tests retain meaningful cheap-call
regression checks, stricter weekly thresholds, explicit inconclusive reporting,
common counts, short or zero warmups, and deadline cleanup across API, SQLite
and documentation categories. Batch boundary supervision adds no per-request
IPC or allocation instrumentation. Weekly timeout is 45 minutes; quick is 10.

Actual full-page Rust observations, bodies and memory evidence remain in
`batching-shape-probe/`: 16-resource admin/member 5.277/3.568s; 32-resource
10.956/6.959s; peak RSS 136,152 KiB. Final validation of those retained bodies
confirmed 193/128/385/256 displayed examples, Rust code, exact expected
authorization counts and private-marker isolation, without rendering again.
See `batching-final-page-validation.json`. The original large 64-resource probe
is retained separately and is not a repeated gate.

Prepared gems remain in the original release checkout's `.gems` and
`clients/rust/.gems`; checks explicitly reused them. The master Rust lock was
copied with only own .2-to-.0 identities changed, retaining constraint operators
and all external bytes (`batching-master-rust-input.json`). No re-resolution.

The footer review correction passed 17 focused lineage/HTML examples in 8.21s
(`footer-focused.log`), with real served HTML replay and narrow negative controls.
The helper requires one exact footer matching the verified own VERSION; raw
body/hash/byte receipts and replay remain authoritative. See
`footer-amend-final.log` for final lint/hooks and the three-file affected delta.

No migrations, persisted-state changes, product runtime changes or dependency
pin update streams. VERSION, changelog, flake.lock, fixed reference and existing
calibrated budget bytes remain unchanged. Master review, exact-head hosted
quick/weekly/component checks and integration precede the exact -x backport and
separate .2 metadata. Old release `776220f3` and original `5832ccc6` artifacts
remain retained and must not publish as the final deliverable.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-haveapi-backport-release/>
