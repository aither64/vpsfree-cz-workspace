# Rust post-review verification

Passed at reviewed and published feature head
`49e45527a5683ffe4c03d1b46a74ac137ffa2f9f`. Working tree remains clean.
Independent review: [rust-review-result.md](rust-review-result.md), no findings.

## Local batch

Fresh operation utility `/root/rust_verification_watcher`, gpt-6-luna/low,
native identity `dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`,
pinned catalog `495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`,
full access and approval never. Ran [rust-long-checks.sh](rust-long-checks.sh)
once in the owned pinned Rust shell, exit 0, approximately eight minutes.
The watcher's invocation included an unused trailing `.` argument to Bash;
the script takes no arguments and executed the reviewed batch unchanged.
No retry, setup repeat, source edit or optional fixture operation.

- Default all-target tests: passed, two library tests and async example built;
  disposable-server acceptance remains ignored.
- Blocking all-target tests: passed, two library tests and both examples built;
  disposable-server acceptance remains ignored.
- All-feature documentation: passed.
- Package listing and verified package build: passed, 699 files, 2.9 MiB
  unpacked / 176.7 KiB compressed. Package contains copied runtime, both new
  advisory action modules and manifest/lock; dependencies have no HaveAPI,
  Git or path dependency.

Logs/status: [rust-long-checks.log](rust-long-checks.log),
[rust-long-checks.status](rust-long-checks.status) (`0`). Warnings are existing
dead fields in empty user_request/webauthn resource handles and the expected
excluded real_vpsadmin test package warning. No failure or kernel build observed.

## Exact-head CI

[Run 41665561009](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/41665561009),
Rust client, completed successfully at the same exact feature SHA. Parent checked
final structured run state only after the watcher returned completion.

| Job | ID | Conclusion |
| --- | --- | --- |
| client (async) | 126019796178 | success |
| client (blocking), docs/package | 126019796449 | success |
| msrv, Rust 1.95 default/blocking | 126019795629 | success |
| regeneration | 126019796145 | success |

CI finished 2026-11-03T15:40:29Z. All required release-preparation verification
gates passed. No operation remains running; the single utility slot was released
to lead immediately on completion, for subsequent TypeScript verification.

## Limits and next action

Lead selected local matrix/docs/package plus CI MSRV/regeneration as sufficient
for this runtime-unchanged refresh. Opt-in real-vpsAdmin acceptance was deliberately
not prepared or run; no live authorization, advisory state-conflict, deployment
or published artifact claim. New methods still require compatible API support
and server permissions. No tags or release dispatch were performed.

Ready for integration, awaiting named repository/target approval. Clean detached
target remains at `3ec8c045dcefcca85b60ffccd38259cda29eeb60`; lead owns fresh
pre-merge checks/claim and approval-bound integration/publication. Feature
comparison is captured at that base and final reviewed head.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)
