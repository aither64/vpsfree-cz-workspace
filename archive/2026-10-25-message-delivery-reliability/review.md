# Independent final review

Reviewer: `/root/message_delivery_final_review`, assigned standalone
`gpt-6.1-sol/xhigh` catalog fallback. All four lanes were reviewed directly:
general, architecture and repetition, scope and proportionality, risk and
compatibility. No nested agents, source edits, live state mutations or long
integration tests were used.

## Findings

### Important — automatic retry can borrow a newer draft's attachments

General lane; `codex-web` commit `7c84dc4d29566d99d7935627920dd653565aa379`,
`conversation/assets/conversation.js:1594`.

When the retained send has no attachments, its durable record omits
`attachmentIds`. The automatic retry expression
`retained?.attachmentIds || uploads?.ids() || []` therefore selects attachments
from the current composer. A user can encounter this by receiving transient
non-delivery for an attachment-free message, then adding a file to a new draft
while retries are paused or backing off. The retry passes the original text and
the new draft's attachment IDs to `sender.send`. Its exact-identity check rejects
the mismatched payload before a network request. The resulting error lacks the
explicit transient non-delivery fields, so `failSubmission` stops the scheduler.
The original message remains unsent despite the automatic-recovery promise.

A focused reproduction in the repository's Nix environment created an original
attempt with no attachments, then evaluated the mounted retry's selection with
a valid UUID for a newer draft upload. It returned:

```json
{"error":"Retry the pending send operation before submitting another message","calls":1,"originalAttachments":[],"selectedAttachments":["00000000-0000-4000-8000-000000000002"]}
```

`calls: 1` is the original failed request; the retry never reached the client.
Select `retained.attachmentIds || []` whenever a retained attempt exists, and
consult composer uploads only for a new send. Add a regression at the mounted
retry boundary that retains the original empty attachment list and preserves the
newer draft upload. This is a narrow correction within the reviewed design.

### Advisory — SQLite stage diagnostics omit the attempt identity

General lane; `codex-web` commit `5c42185745bcd02eb036487feb1c285db15ea381`,
`codex/submission_database.go:64`.

`submission-transaction` events construct a delivery identity with only the
thread, although single-attempt scopes already contain the attempt ID. The
runtime logger consequently prints an empty `attempt=` for these events. Slow
initial lookups and receipt commits cannot be directly attributed to a browser
attempt when multiple operations affect one thread. Send/admission events still
have identities, so this does not affect delivery safety. Consider attaching the
sole scoped ID when one is present, retaining an empty identity for genuinely
thread-wide transactions.

No Blocking findings were identified. Resolve the Important finding or record
an explicit acceptance decision before proceeding under the review policy.

## Reviewed ranges and complete history

The checked worktrees were clean. Their complete recorded base-to-head series,
final diffs, commit purposes and messages were inspected:

| Repository | Base | Head | Complete series |
| --- | --- | --- | --- |
| codex-web | `872c7ad3962f9fa9b17358244e27f3e3fac59fc5` | `7c84dc4d29566d99d7935627920dd653565aa379` | `66ab8c0`, `5c42185`, `7c84dc4` |
| dev-workspace | `10bb047513c82d1310e8fcaa797e8772f948dd8a` | `9bf4282185f9440eb9257d71d03636a353ee1282` | `1aa8a764`, `0d1b27fa`, `9bf42821` |
| vpsfree-cz-configuration | `d12a77374b18e15fe7600f95307114e2e1882828` | `59ade10f2c8b14de54303528e66e1538572d6a4d` | `59ade10f` |
| workspace | `b1b86b2b8a075666ccdef7f9d254047be972508a` | `db59ca58df9b649c01aeca7a5303bde270b53db2` | `df1944a20`, `7253da4a1`, `00fe575af`, `01c06f603`, `db59ca58d` |

The workspace's actual merge base with shared `master` is `01c06f603`.
The four preceding commits in its recorded range are shared-master ancestry,
not superseded delivery implementations. Its delivery feature changes only
`flake.nix` and `flake.lock`. No obsolete unmerged design, follow-up fix commit,
or abandoned compatibility shim remains in the reviewed series.

Dependency changes are separate from behavior. The backend/storage split's
coupling rationale is sound: durable claims and transport restoration must agree
on who may reset an admitted attempt. Browser behavior and runtime package
integration are separately reviewable commits.

There are no repeated dependency update streams left to consolidate. Each final
stream has one owning update: SQLite modules/vendor hash in `66ab8c0`, the
runtime's Go/Nix codex-web selection in `1aa8a764`, configuration's devWorkspace
selection in `59ade10f`, and the workspace's nested runtime selection in
`db59ca58d`. Their transitive codex-web changes are the expected same final
revision. The previously published `073f6db` is absent from these final series;
its disposable-use provenance does not require an intermediate pin commit.

## Migration lineage and compatibility

The sole migration is the owning library's direct schema-3 JSON import into
SQLite `user_version=1`, with schema-4 JSON predecessor fences, in `5c42185`.
There are no migrations in dev-workspace, configuration or workspace. The packet
reports no merge, release, live deployment or external consumption of an earlier
branch schema; the final history introduces the final schema directly. Its
migration lineage is sound under that stated provenance.

Schema creation and version publication share a transaction. Version-1 receipt
tables are not silently recreated. Import validates the selected predecessor,
preserves checksum-named backups, commits data with its journal, then publishes
both fences before marking ready. Interrupted publication verifies exact source
identities. Scoped transactions preserve unrelated rows; admission claims prevent
an older failed operation from resetting a newer admitted send. Native I/O runs
outside database transactions.

The explicit writer-acquisition boundary is supported by the pinned
`github.com/coder/websocket v1.8.14` implementation: writer acquisition performs
no message write. Errors after writing begins retain uncertainty. The original
reported lock-acquisition error is consistent with a pre-transmission failure;
complete current history and the original evidence must still be reconciled
before repairing its retained receipt.

The runtime's portal, provider and observation-command constructors select the
same socket-derived persistent paths. Passive activity/model clients do not own
submission mutations. Archive export now uses the library's scoped API while
preserving its held-prompt format. Package transitions require exact integer
storage capabilities once SQLite state or sidecars exist. Older JSON writers
refuse the fences; restoring an old JSON backup is not a supported rollback.

The detached plan-dispatch context is created after plan validation, retains its
operation deadline and observes service shutdown. Browser retries require all
three explicit non-delivery fields and preserve the original identity. The
generic attachment-selection finding is the exception to the intended retained
payload behavior.

The library owns the reusable state machine/store/scheduler, and the runtime
consumes it through Go imports and its pinned browser source. Configuration's
channel selects the matching host module; the workspace retains its independent
extension revision and nested runtime override. Matching final selections and
unchanged native Codex avoid a protocol-version transition. No unrelated system
or extension input changes were found.

## Documentation, checks and remaining gates

Reviewed documentation includes codex-web's README, `docs/reference.md` and
`docs/submission-storage.md`, the runtime's README and
`docs/workspace-portal.md`, configuration's provider/deployment guide, and the
initiative plan/design/state/packet. Lasting migration and forward-recovery
semantics are documented with their owners. Exact rollout actions remain in the
initiative. A routine configuration pin does not need separate feature docs.

Independent quick verification:

- `git diff --check` passed for all four reviewed ranges.
- `nix develop --command node --test test/delivery_retry_browser_contract_test.cjs`
  passed: 3 tests, 0 failures. These tests do not exercise the mounted retry's
  interaction with a newer upload draft.
- The focused Nix/Node reproduction above confirmed the Important finding.
- The existing deadline, migration, stale-claim, contention, plan-disconnection,
  archive and package-contract tests were inspected. The packet's broader Go,
  browser, Ruby and protocol results were considered as supplied evidence; they
  were not redundantly rerun by this reviewer.

Packaged/native/lifecycle acceptance and actual activation remain outstanding
gates, not review results. In particular, verify the two-predecessor import,
post-migration package refusal/forward recovery, archive/revive, and the shipped
plan/ordinary retry flow against disposable state before touching live receipts.
Post-activation health, naming, ongoing conversation continuity and database
integrity still need actual deployment evidence.

The lead's subsequent `review-ci-addendum.md` reports runtime CI `40181256989`
failed its package prerequisite before any VM test ran. Its three diagnosed
failures concern a stale app asset version assertion and isolated JavaScript
contexts lacking the newly referenced `deliveryRetries` binding. Those narrow
fixture corrections were inspected in the committed runtime delta
`9bf42821..60e4e8704715e305508b0ce7105852e0a96fafe4`. They preserve the substantive
design and correctly repair those fixtures. That delta's `git diff --check`
reports trailing whitespace at
`portal/internal/web/submission_notice_contract_test.cjs:17`; remove it before
final quick-check acceptance. Refreshed downstream pin heads remain additional
to the exact ranges above. Retain this report's bindings and record the verified
final revisions after remediation. A green retry without addressing the
diagnosed fixture failures would not supply package acceptance.

The original-attempt repair is a separately prepared operation; no reviewed
repair script exists yet. Before executing it, retain a consistent SQLite backup,
hold the appropriate application writer exclusion, reconcile the exact original
UUID against complete native history and the original pre-transmission evidence,
and condition any database update on that exact row's full retained identity,
state and claim. Change payload/state/claim consistently in one transaction,
require the expected row count and preserve every unrelated receipt. Recover
acceptance if found; missing history alone never permits resetting the attempt.
Reuse the original UUID after any justified restoration. This review does not
authorize default-branch integration or any unrelated attempt reset.
