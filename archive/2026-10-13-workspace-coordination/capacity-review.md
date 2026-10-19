# Replacement independent capacity review

**No Blocking findings; three Important findings remain.** The replacement
review independently confirms the two findings in the earlier report preserved
below and identifies an additional worker-envelope failure. All three require a
fix or an explicit recorded decision before long verification or deployment.

Reviewer: `/root/coordination_capacity_review`, assigned installed
`lead_reviewed` reviewer settings GPT-6 Astra / xhigh / read-only; catalog digest
`437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd`.
Replacement was assigned because the previous reviewer's follow-up identity
could not be validated after repeated unreadable message payloads and a native
transport failure. During this review, the earlier reviewer wrote its report to
this same assigned path. Its text is preserved below as context; the conclusions
in this replacement section are independently reached and supersede its count.

Read the review packet, mandatory-review skill, all four lane references,
workspace/repository instructions and applicable routed procedures. Applied
general, architecture/repetition, scope/proportionality and risk/compatibility
lanes at high risk. No application edits, commits, nested agents, long checks,
deployment or integration were performed.

## Important findings

1. **Lifecycle preflight can succeed without retaining the capacity that the
   subsequently published recovery journal needs.** Runtime core commit
   `983d6772659d91413ba80d13c9a81ce03f980fd1`,
   `libexec/workspace-coordination.rb:447` and `:478`;
   `libexec/dev-session:1890`, `:1945`, `:2071`, `:2086`, `:2188`, `:2191`.

   `require_lifecycle_capacity!` checks an unreserved snapshot. Archive, revive
   and delete then publish an ordinary journal before calling the binding
   method, which applies the new-work ceiling again. A different session can
   use the intervening space: the lifecycle transition lock is shared
   (`dev-session:8953`), and the remaining locks are per session. A refusal at
   bind leaves an unfinished journal whose retry can continue failing at the
   ceiling. Retained terminal history need not free any space. That journal also
   prevents conflicting lifecycle/package transitions.

   An independent in-memory Store probe used only valid bounded retained
   receipts near 14 MiB. The exact lifecycle preflight accepted, a competing
   `Store#request` accepted, and `bind_lifecycle` then raised
   `coordination admission capacity exhausted`, retaining zero lifecycle
   bindings. The ordinary journal-before-bind order was separately inspected
   in all three commands. This probe establishes the interleaving; it is not a
   live archive/delete test.

   Make the exact future binding recoverable before publishing a journal that
   depends on it. Use durable reserved capacity or equivalent serialization
   without holding the ledger mutex over lengthy lifecycle work. Test journal
   publication, competing admission, interruption and successful retry of the
   same operation. Preserve operation/incarnation proofs and lock ordering.

2. **An admitted refreshed job can exceed the worker request limit and become
   permanently unreconcilable.** Same runtime core commit,
   `libexec/workspace-coordination.rb:1094`;
   `libexec/workspace-coordination-execution.rb:645`, `:675`, `:732`, `:72`.

   Each accepted refresh appends the old snapshot/result to `job.history`.
   Admission accounts for these bytes against the 16 MiB ledger, but dispatch
   embeds the *entire* accumulated job in `request.json`. Neither refresh nor
   dispatch checks that complete envelope against `MAX_REQUEST` (256 KiB).
   Both `Worker#initialize` and reconciliation read it with that smaller bound.
   Once claimed, the worker cannot even initialize; reconciliation refuses the
   same request, while cancel/refresh refuse claimed or uncertain jobs. Resource
   ownership is retained indefinitely despite there having been no worker
   effect. This is distinct from the accepted missing-request recovery limit:
   normal supported refreshes create the unusable request themselves.

   A pure in-memory probe ran the actual `Engine#mutate`, `Store#request`,
   validation, admission and `Engine#dispatch` methods. Seventy refreshes of a
   roughly 4 KiB snapshot all passed; the ledger was 328,055 bytes, but dispatch
   emitted a 304,400-byte worker request rejected by the 262,144-byte parser.
   Snapshot filesystem/Git validation, persistence and external dispatch were
   substituted; the test deliberately isolates admitted representation growth.
   The real snapshot path permits a 4,000-byte `changeScope`, so repeated valid
   snapshots can produce the same growth. Each individual refresh request fits
   the public request bound.

   Keep retained history in its owning ledger and seal only the fields the
   worker actually needs, or reject the prospective complete worker envelope
   before creating an execution claim. Preserve immutable request digests and
   exact attempt recovery. Add an end-to-end fixture with repeated valid
   refreshes and an actual worker-request read. Also cover one near-limit
   snapshot, because the dispatch wrapper itself adds bytes.

3. **Persisted result/artifact/request limits disagree about the trailing
   newline.** Same runtime core commit,
   `libexec/workspace-coordination-execution.rb:107`, `:224`, `:764`, `:673`;
   `libexec/workspace-coordination.rb:100`, `:699`;
   `portal/cmd/workspace-portal/coordination.go:32`.

   The result writers allow exactly 16,384 encoded JSON bytes; `atomic` adds a
   newline, and result import limits the entire file to 16,384 bytes. The same
   mismatch affects exactly 256 KiB saved artifacts and native request files.
   Unlike diagnostics, an authoritative observation cannot simply be truncated.
   The ledger writer correctly includes the newline already.

   An independent in-memory probe called the unchanged `Worker#result` with a
   complete JSON result of exactly 16,384 bytes. Its writer accepted a
   16,385-byte serialized file; the unchanged bounded parser rejected it. The
   actual `private_read` rejects it even earlier by `stat.size`. The probe
   substituted only the file writer to retain its bytes in memory.

   Use one consistent encoded/file bound across every producer and consumer,
   with boundary regressions that write and read/import the maximum accepted
   value and reject the next byte. Include reconciliation results, artifacts
   and the native helper's complete request file.

## Independent remediation, history and compatibility conclusions

The completed-creation fix is sound by inspection: Host admission reuses the
existing private ready-journal validator and manifest/goal proof, keeps the
receipt, and has full schema-2 Host-path and scheduler-tick regressions plus
invalid-evidence cases. The previous Blocking finding is resolved.

The former large-options ledger overflow is corrected by storing options and
native receipts as immutable checksummed artifacts. Deterministic event IDs
bound state churn; outstanding events remain charged after job completion.
The prospective ledger formula accounts for actual post-callback records and
request receipts, job settlement, retained deployment observations and one
unknown-to-applied disposition, unowned proof multiplicity, completion and both
frontier projections. The lifecycle race and protocol-bound findings above are
remaining contract failures, rather than grounds to replace this storage owner
or introduce another execution framework.

Independently verified all four actual heads, clean feature trees, merge bases,
complete eight-commit series and messages, and byte equality of each saved
binary final patch with Git's actual base-to-head diff. The exact bases, heads
and complete series are in the table in the preserved report below and match
`review-inventory.json`. Inspected the changed runtime, tests, shared runner
consumer, confctl adapter, portal, workspace catalog/routing, project docs and
configuration operations, with the previous review as unchanged-code context.

**Whole-branch history:** no obsolete unmerged approach, fixup series,
intermediate private schema or redundant pin commit remains. The core admission,
execution and recovery contract is coherently bundled; portal, adapter, pins,
site policy and configuration operations retain their independently reviewable
commits. No additional split finding.

**Pin consolidation:** one extension runtime update, one workspace composition
update and one generated configuration `dev-workspace/devWorkspace` update.
Resolved the actual lock paths independently: all select runtime
`ee6cef1a103f6287bca46603bf47fc71fa4b1c21`; workspace selects extension
`d921dfa3d24a6b154e46868c9e3a1b547bd3bfea`; codex-web remains
`5f15b9293f9b1eef7469a34d7b2044c743160283`; configuration confctl remains
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`. The direct nested runtime override
and generated confctl changelog remain. Range-diffs and final trees preserve
upstream Host generation/capture support, extension optional KB support and
unrelated configuration pins. The final configuration lock changes only the
intended runtime identity.

**Migration lineage: no database migrations.** Private coordination schema 1
introduces its final representation directly. There is no intermediate branch
migration to preserve. The packet records the iterations as unmerged,
unreleased, undeployed and externally unconsumed; no evidence inspected
contradicts that provenance. Existing lifecycle, manifest, cluster and Codex
submission formats stay unchanged. Matching package contracts, retained roots
and forward recovery remain necessary. No coordinated running-node update is
introduced.

Runtime/provider ownership, concrete adapter and consumer mapping remain
appropriate. The changes preserve the trusted-local-operator boundary and
remote portal authentication. Documentation distinguishes reusable operations
from the unexecuted rollout. No additional architecture, scope or documentation
finding beyond the recovery defects above.

## Verification limits and next action

Read the successful committed quick evidence: coordinator 29/159, Host
160/1212, lifecycle 1/15, adapter 4/20, syntax and focused Go policy checks.
The replacement probes ran in the runtime Nix environment and substituted
memory for writes; the combined successful probe finished in 1.63 seconds.
No source or live state was mutated. They do not prove real systemd, native
transport, confctl SSH activation, profile continuity or lifecycle interruption
recovery. Longer integration and candidate-build evidence remains outstanding.

- Phase: independent affected-lane review complete with three Important findings.
- Completed: remediation, full histories, pins and migration conclusions.
- Remaining: reconcile all three findings and run focused regressions, then
  authorized longer verification and aitherdev deployment.
- Risks: real systemd/native/confctl/profile and no-reboot continuity are unverified.
- Next action: lead owns fixes or explicit recorded decisions. Default-branch
  integration, reboot, archive and deletion remain unauthorized.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-13-workspace-coordination/.

---

# Earlier reviewer report, preserved as context

**No Blocking findings; two Important findings remain in the new capacity
paths.** Completed-creation admission is corrected. The new artifact
representation and prospective settlement accounting resolve the earlier
large-policy ledger overflow, subject to the lifecycle admission race and file
boundary mismatch below. Fix or explicitly reconcile these findings before
long verification or deployment.

Reviewer: `/root/coordination_review`, same independent GPT-6 Astra / xhigh
reviewer, read-only outside this report. Applied all four affected lanes:
general; architecture/repetition; scope/proportionality; risk/compatibility.
The unchanged workspace/repository instructions, applicable procedures,
mandatory-review skill and all four lane references read earlier in this
context remain applicable. No nested agents, application edits, commits,
integration or deployment were performed.

## Findings

1. **Important — lifecycle preflight does not reserve its required binding
   capacity across journal publication.** Runtime commit
   `983d6772659d91413ba80d13c9a81ce03f980fd1`,
   `libexec/workspace-coordination.rb:447`, `:478`, `:503`, and
   `libexec/dev-session:1888`, `:2069`, `:2188`.

   `require_lifecycle_capacity!` reads a ledger snapshot and checks hypothetical
   extra bytes, then returns without retaining a reservation. Archive/delete/
   revive subsequently publish their ordinary durable journal and call the
   binding method, which subjects the required binding to new-work admission
   again. Another session can consume the remaining admission space between
   those steps. Lifecycle transitions use a shared host transition lock
   (`dev-session:8953`), and creation/session locks are per session, so they do
   not exclude another owner's admission.

   The second check then refuses after the recovery journal already exists.
   Retrying that journal repeats the same capacity refusal. With retained
   terminal history at the ceiling and no pruning, the space need not become
   available; the unfinished journal also blocks conflicting lifecycle/package
   operations. In explicit archival, quiescing and recovery capture may already
   have occurred before binding.

   A short Store-level fixture reproduced: valid near-capacity ledger;
   lifecycle preflight accepted; another admission accepted; exact lifecycle
   bind refused with `coordination admission capacity exhausted`. The probe
   reproduced the capacity interleaving, not a complete live archive command;
   the journal-before-bind ordering was verified directly in all three command
   paths.

   Ensure that a successful preflight makes the bounded binding/completion
   capacity unavailable to competing new admissions before journal publication,
   or provide an equivalent durable recovery allowance for the exact journaled
   operation. Preserve the journal/incarnation and lock-order contracts. Add a
   two-owner interleaving regression that publishes the journal, admits competing
   work, and successfully resumes the same lifecycle operation without pruning
   or abandoning another owner's records.

2. **Important — several persisted payload bounds exclude the newline that
   their readers include.** Same runtime commit,
   `libexec/workspace-coordination-execution.rb:764`, `:107`, `:224`, `:673`,
   and `libexec/workspace-coordination.rb:699`, `:100`.

   Worker and reconciliation result writers accept JSON whose encoded size is
   exactly `MAX_RESULT` (16,384 bytes). `WorkspaceCoordination.atomic` appends
   a newline, while result import calls `private_read(..., limit: MAX_RESULT)`
   and bounds the complete file. Therefore an accepted maximum-size result is
   unreadable. A valid adapter observation can bring a complete result to that
   boundary after an actual effect; the scheduler cannot import its receipt.

   A focused probe called the unchanged `Worker#result` with exactly 16,384
   encoded JSON bytes. It successfully wrote a 16,385-byte file, which the
   unchanged result reader rejected as oversized. The same write/read mismatch
   exists for an exactly 256 KiB saved artifact, and for the assembled native
   request written through `atomic` before the Go helper's full-file size check.
   The ledger writer already accounts for this newline correctly.

   Make the encoded/persisted size convention consistent at each producer and
   consumer, including worker results, reconciliation results, artifacts and
   native request files. Do not truncate an authoritative observation. Add
   boundary checks for the maximum accepted persisted size and the next byte,
   covering write followed by actual read/import rather than JSON size alone.

## Remediation and design conclusions

Completed creation receipts are now handled through the existing Host reader
and ready-journal/manifest proof. The actual generation/session admission path
accepts the retained schema-2 fixture, preserves it byte-for-byte, and admits a
scheduler tick. Unready, malformed, mismatched slug, goal and team-binding
evidence is rejected. This closes the previous Blocking finding without
deleting lifecycle evidence or adding a second creation format.

Large immutable options and native receipts now use the existing checksummed
artifact store. Outbox records retain digests; send reconstructs and verifies
the options object, and the assembled envelope is checked before its digest is
adopted. Existing saved options are not replaced. Deterministic versioned event
IDs preserve the first payload/native identity through state churn and bound
events to five per job snapshot and two per reservation. Terminal jobs retain
the reserve for their outstanding events.

The prospective predicate runs after new records and their request receipt are
inserted. It accounts for job results/reasons/cancellation, exact deployment
coverage/contracts, one unknown-to-applied history disposition, missing and
undelivered events, completion proofs and both frontier projections. The unowned
proof calculation preserves the multiplicities used by `finish`. Encoded
diagnostics, event envelopes, receipt results and counters are bounded. Cancel,
finish and exact retries retain settlement access. No pruning, forced release,
new generic executor or replay of uncertain effects was added.

This is an appropriate extension of the existing storage owner, rather than a
second persistence service. The remaining findings concern enforcing its
chosen recovery contract. Runtime, extension adapter, site catalog and
configuration continue to own their respective boundaries. Earlier reviewed
registration, resumption, generation completion, lifecycle finalization,
outbox fairness, independent reconciliation, stateless confctl activation,
configuration-baseline and installed-guide fixes remain present.

The explicitly accepted conservative limits remain unchanged: absent
`request.json` needs operator recovery; canceled undeployed work still requires
integration for `finish`; ambiguous native pre-RPC submission retains its exact
identity and fails closed. Active-first display of active and completed jobs
still matches the selected scope.

## Whole-branch history, pins and migration lineage

| Repository | Base | Reviewed head | Complete feature series |
| --- | --- | --- | --- |
| dev-workspace | `fea04c6de25448751239099eca7101c43cb495c2` | `ee6cef1a103f6287bca46603bf47fc71fa4b1c21` | `983d6772659d91413ba80d13c9a81ce03f980fd1`, `ee6cef1a103f6287bca46603bf47fc71fa4b1c21` |
| vpsfree-dev-workspace | `505ffc457b3329af0b124075f417953c9cc42edd` | `d921dfa3d24a6b154e46868c9e3a1b547bd3bfea` | `eb3e5178bede6c0ff1d86d047ae60fc71cdcd080`, `d921dfa3d24a6b154e46868c9e3a1b547bd3bfea` |
| workspace | `90005ea3a7a170b23699c38933b111b046ce43f8` | `fd7a709b1f2b0f8b74c1349c9193cc49adad5603` | `0933c085c7a043d96d27dd6fc47edbef28eb6c42`, `fd7a709b1f2b0f8b74c1349c9193cc49adad5603` |
| vpsfree-cz-configuration | `0e394507395c04a6c11fd6d25c8284621061c140` | `d35aa2b2127a4ba500825c3cef197fae09e6db73` | `787137d4fe2a7c8d5baf142b113265e1b4675de5`, `d35aa2b2127a4ba500825c3cef197fae09e6db73` |

Independently verified actual heads, tracked cleanliness, the complete eight
commit messages/series, and byte equality between every saved binary final
patch and its actual base-to-head Git diff. Inspected the remediation diff and
rebase integration with the earlier review as the unchanged-code baseline.
Fixes remain folded into their owning functional commit. No obsolete unmerged
approach, fixup sequence, transitional schema or redundant pin commit remains.
The established core/UI, pin/adapter, composition/policy and docs/generated-pin
split remains coherent; no additional history-split finding.

There is one final extension runtime update, one workspace extension plus nested
runtime composition update, and one generated configuration
`dev-workspace/devWorkspace` update. All runtime paths select
`ee6cef1a103f6287bca46603bf47fc71fa4b1c21`, and workspace selects extension
`d921dfa3d24a6b154e46868c9e3a1b547bd3bfea`. Codex-web remains
`5f15b9293f9b1eef7469a34d7b2044c743160283`; configuration confctl remains
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`. Generated confctl history is
preserved. Upstream runtime `input:` and streaming capture/generation support,
extension optional KB support, and configuration's unrelated service/WebUI
selections remain in the rebased trees. Workspace policy and configuration
documentation retain patch-equivalent changes; the final configuration lock
diff changes only its intended runtime selection.

**No database migrations.** New private coordination schema 1 directly contains
the final digest-based notification representation and lifecycle bindings.
There is no intermediate branch migration or compatibility reader to retain.
The packet records all feature iterations as unmerged, unreleased, undeployed
and externally unconsumed. Existing lifecycle journals, manifests, clusters,
pending-Codex records and native submission formats are unchanged. Folding
these private-format changes is sound under that provenance. Matching package
contracts and retained roots remain necessary; recovery stays forward-only.

## Evidence and remaining phase

The recorded committed quick check exited zero: coordinator 29 tests/159
assertions, Host 160/1212, lifecycle 1/15, adapter 4/20, Ruby syntax and focused
native-policy Go checks. Read the new capacity and creation regression code.
Large-policy tests use substituted native calls and do not themselves validate
the Go TurnOptions schema or live transport; that integration remains pending.
The report packet also records final workspace instruction/composition checks.

Reviewer probes used temporary fixtures and the already available Ruby 3.4.9
interpreter from the runtime Nix environment. The first capacity-fixture setup
used an oversized filler receipt and was corrected; the two reported
reproductions then completed in about two seconds. One `nix develop --offline`
retry unexpectedly began broader source/environment realization and was
interrupted before running its probe. No long integration test or live runtime
mutation ran, and source trees remained unchanged.

- Phase: affected-lane review complete with two Important findings.
- Completed: creation fix, new capacity representation/accounting, rebases,
  final histories, pins and migration provenance assessed.
- Remaining: lifecycle capacity interleaving and persisted-byte boundaries;
  focused regression checks, then warranted longer verification.
- Risks: real systemd/native/confctl/profile integration and no-reboot
  self-deployment remain unverified.
- Next action: lead resolves or explicitly reconciles the findings before long
  checks and authorized deployment. Integration, reboot and archival remain
  unauthorized.
