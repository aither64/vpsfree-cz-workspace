# Accepted-fork source-lock fixture handoff

Status: prepared, uncommitted, frozen for lead-selected first integration run.
Owner1 retains all B Git operations. No integration test has been executed by
implementer0; formatting and Ruby syntax checks alone passed (see final.json).

Only two new application paths are owned. See final.json for exact file hashes,
owned.patch for the complete addition, and source-inventory.json for read-source
identities. The initial and final relevant source inventory did not move during
this package; creation_test.go, including its 409/200ms source-EX assertion,
is unchanged. Completed Ruby guard and EX-helper handoffs were not edited.

The actual Handler acceptance launches Go runCreation/initializeCreation and
runCreationCommand. Its executable seam loads the repository Ruby implementation
and invokes DevSession::CLI. Test injection supplies the disposable environment,
fixed profile identity, a real super-calling source stage observer, and counted
external native/provider/tmux responses. Real source/lifecycle validation,
with_slug_lock/with_host_lock/flock, provider registration validation, request
binding, fork journal, tracking, runtime authority, completion writers, terminal
reconciliation and receipt recovery remain in use. Unknown external commands
refuse. No Go completion proof or receipt is synthesized by this fixture.

A separate Ruby holder opens the exact private source lock and checks its
device/inode before taking SH. Source EX1 pauses before binding, or EX2 pauses
after binding and release of destination locks. Explicit socket/pipe handshakes
hold/release the lock, bounded at five seconds; no sleeps/mock busy errors.
Both current source EX refusals must produce failed attempt1 before holder
release. The EX2 case also acquires both destination locks independently while
the source stage is paused. No fork journal or destination is fabricated.

The same original receipt/current attempt retries after release. Recovery must
produce exactly one external native fork and one destination, matching source,
thread, model/effort/provider, with real Ruby authority/completion evidence and
ready attempt2. Exact duplicate/restart retries must not invoke the CLI again;
stale attempt/wrong receipt conflict. Existing completion/binding bytes stay
unchanged. Fresh refused fixtures with replaced sources must fail with zero
native writes. A fifth case interrupts only external terminal creation after a
real fork journal/thread publication, moves disposable source tracking, and
requires ordinary journal-bound recovery without a second fork. That path may
restore the same settings through one counted external ensure-settings call.

No production API, native version, schema, migration, lock mode or waiting
behavior changed. Test comments preserve the controlled-evidence boundary;
no lasting product documentation change is useful for this test-only addition.
The 9f explicit-fork, 207 later plan-derived source-busy, and e7 new-session
preparation failures remain distinct and unwaived. This fixture cannot identify
an unobserved CI holder.

## First-run handoff

Lead chooses review/watcher order. No first run was launched here. Expected
fixture runtime is under10s excluding compilation, not measured; Nix/compilation
is uncertain. Every handshake is bounded at5s, Go test timeout45s. Do not retry,
change source or waive a missing/skipped case on failure. Preserve all logs,
exit/elapsed/source identities and controlled holder/stage diagnostics.

CWD: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace/portal`

```sh
nix shell --inputs-from .. 'nixpkgs#go' 'nixpkgs#ruby' 'nixpkgs#git' -c go test -mod=readonly ./internal/web -run '^(TestAcceptedForkSourceSharedLockRefusalAndReceiptRecovery|TestCreationFastSourceLockDoesNotWaitForLifecycleMutation|TestCreationReceiptRubyInitializerContract)$' -count=1 -timeout=45s -json
```

watcher-brief.json enumerates all21 required leaf cases: five new grouped cases,
one unchanged fast-lock case and15 existing Ruby-initializer contract cases.
Zero matches, a missing leaf or any skip is not a pass.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/)
