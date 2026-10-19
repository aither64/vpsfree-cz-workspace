# Independent remediation review

**One Blocking and one Important finding remain.** The original registration
blocker and eight of the original Important findings are corrected by inspection.
The recovery-capacity finding is only partially corrected. The Blocking finding
below was discovered while checking the ordinary admission path against retained
lifecycle records. Do not begin long checks or deployment before resolving it.

Reviewer: `/root/coordination_review`, retained independent reviewer,
GPT-6 Astra / xhigh, read-only except for this report. All four assigned lanes
were applied: general; architecture and repetition; scope and proportionality;
risk and compatibility. No nested agents, source edits, integration, deployment,
or long tests were performed.

## Findings

1. **Blocking — normal completed session creation permanently blocks
   coordination admission.** Runtime commit `882a034fc6ba77b0ad0ef2aad57f8080a8257eda`,
   `libexec/workspace-coordination-host.rb:136`.

   `with_coordination_session_admission` rejects the existence of any
   `SLUG.creation.json`, without examining its state. Normal managed creation
   deliberately retains this file after completion:
   `dev-session:3663` writes the same journal back with `state: ready`, and
   `dev-session:4076` places it in the exact directory matched by this glob.
   Consequently a normally created managed session cannot prepare, approve,
   submit, cancel, finish, or reconcile an operation. The scheduler uses the
   same admission function and cannot process such an owner either. Merely
   finishing creation or retrying cannot remove this refusal.

   A focused Nix-environment probe invoked the actual admission method with a
   retained ready creation receipt; it returned code 5,
   `session lifecycle recovery must finish first`, before yielding. Only the
   outer generation wrapper and runtime-path lookup were substituted; the
   rejecting method was unchanged. Existing coordinator fixtures create
   manifests directly and omit this retained receipt, so they miss the normal
   product path.

   Distinguish a validated completed creation receipt from an unfinished
   creation operation using the owning lifecycle contract. Preserve refusal of
   malformed, mismatched, and unfinished records. Add a Host-path regression
   with the complete retained creation evidence of a normally created session,
   including a scheduler admission case. Do not delete the receipt as a fix.

2. **Important — recovery accounting still under-reserves notification and
   retained completion growth.** Runtime commit `882a034fc6ba77b0ad0ef2aad57f8080a8257eda`,
   `libexec/workspace-coordination.rb:288` and `:628`.

   Cancel and finish now bypass the admission ceiling, and terminal retries are
   correctly bounded. However admission reserves only six 16 KiB result units
   per pending job or reservation. That does not bound the records subsequently
   added to the ledger. Each outbox event stores a complete immutable native
   options object, including retained lead instructions, under the 256 KiB
   transport/roster bounds. Those options are materialized after admission,
   without a separate size reservation. Delivered events keep their options;
   outstanding events are not counted in the admission formula, and terminal
   jobs cease contributing to its reserve before all their events are delivered.

   A focused in-memory probe through the actual `Store#request`, validation,
   and `Engine#transition` accepted 100 small jobs: 71,285 ledger bytes before
   ready transitions. One valid-size 200,000-byte retained policy per ready
   event produces 20,151,584 bytes, exceeding the 16,777,216-byte hard limit,
   even before terminal events and results. This is a capacity calculation
   using permitted payload sizes, not a real native transport test. Real
   snapshot overhead does not close the several-megabyte admission gap.

   The hard transaction check safely refuses overflow, but then already
   accepted notifications cannot settle; `finish` requires their delivery.
   Other settlement writes also compete for the remaining bytes. Thus bypassing
   the 14 MiB admission check does not establish the promised recovery reserve.
   Account for all retained payload classes and outstanding notifications, or
   impose explicit supported bounds and a storage representation that makes the
   reservation conservative. Test admission followed by actual option/result
   materialization and settlement. The new tests that insert a filler receipt
   at the ceiling and finish one small reservation do not exercise this growth.

## Prior finding disposition

| Prior finding | Re-review conclusion |
| --- | --- |
| 1: registration necessarily fails | Corrected. Preflight precedes registry mutation; private registration mode proves the settled selected profile token and repeats reservation admission. Candidate activation keeps its claim requirement. |
| 2: suspension cannot resume | Corrected for retained coordination state. Explicit generation-checked resume restores services before clearing the flag; suspend compensates attempted service changes and retains a pause when compensation fails. |
| 3: completion can affect a later generation | Corrected. Completion reacquires the transition lock and checks the full selected profile token, package and pending evidence before clearing recovery or restoring terminals. |
| 4: lifecycle journal discarded too early | Corrected. Exact lifecycle operation/incarnation bindings precede mutation, and finalization precedes journal deletion. Revival freezes its archive association before tracking changes, including old revival journals without an archive-operation field. |
| 5: unavailable owner starves delivery | Corrected. Workspace/owner/fence eligibility is applied before the two-event delivery bound. |
| 6: remote recovery blocks the scheduler | Corrected in the inspected dispatch path. Independent deterministic reconciliation units retain the original request and share the nonblocking worker lock; unknown outcomes retain resource ownership without consuming every unrelated worker slot. |
| 7: confctl settings evaluated under claim | Corrected by source inspection. Activation calls `ConfCtl::Nix.stateless`; the actually pinned Nix/NixLegacy/NixFlake implementation supplies `max_jobs: 'auto'` and avoids Settings initialization. |
| 8: no capacity for cancel/finish | Partial. Ceiling bypass, request bounds, exact retry receipts and rejection of fresh-ID terminal completion are present. Finding 2 above remains. |
| 9: stale configuration baseline | Corrected. Before machine intent the worker fetches the sealed configuration target and requires it to be an ancestor of the prepared source; failure yields `needs_refresh` without adapter activation. |
| 10: installed guidance absent | Corrected. Both guides are installed and printed with selected package/catalog identity. Fresh root/member technical bindings reference the command while leaving retained role instructions and model/effort/access unchanged. |

The lifecycle finalization test checks journal retention on injected completion
failure; it is narrower than a full archive/delete/revive interruption-and-retry
test. The new systemd test exercises independent worker survival, a stalled
reconciler and another workspace using private fixtures. It remains unrun, as
required at this review checkpoint. The adapter regression still substitutes
the confctl classes; a fresh-process test using the real pinned constructor
with Settings/evaluation made fatal remains useful acceptance evidence. None of
these limited tests proves live native transport or self-deployment continuity.

The two explicitly accepted conservative recovery limits remain accepted:
missing `request.json` requires operator recovery, and canceling an undeployed
operation does not waive integration proofs for `finish`. Native pre-RPC
submission ambiguity remains fail-closed with the same message identity.
Active-first display of both active and completed jobs matches the selected UI
scope.

## Complete history and migration conclusion

| Repository | Base | Reviewed head | Complete feature series |
| --- | --- | --- | --- |
| dev-workspace | `7c07b540a5e45cac4b39351f713cf3528e4df614` | `b0ec2f10525e0bc410ee8052c726241bcf209943` | `882a034fc6ba77b0ad0ef2aad57f8080a8257eda`, `b0ec2f10525e0bc410ee8052c726241bcf209943` |
| vpsfree-dev-workspace | `7157c8098dcf60127aa4df823fab82b4185ad22a` | `a15bcd53e802eb9f46dac713a94a80a4b89024c6` | `04c3b736e7db54e03987c2fb1ba9dca593a73d56`, `a15bcd53e802eb9f46dac713a94a80a4b89024c6` |
| workspace | `90005ea3a7a170b23699c38933b111b046ce43f8` | `873d434db870272c5a8d9bc70d522ca5e76a2923` | `40b010a55be876769a085eaa227d1c8771075bbe`, `873d434db870272c5a8d9bc70d522ca5e76a2923` |
| vpsfree-cz-configuration | `a3255cbecc9ccb0f65800e928fc2c3c728ae16bb` | `966e0a9bc18a381c62e204a98474d43b5f619109` | `566934faee84ee1e5bf1c02458c3f1c8c90b62ae`, `966e0a9bc18a381c62e204a98474d43b5f619109` |

Verified all actual heads and complete eight-commit series, commit messages,
tracked cleanliness, and byte equality of each saved final patch with Git's
base-to-head diff. Re-inspected the remediation diff and affected final paths;
the prior review covers unchanged implementation. Fixes were folded into the
owning functional commits. No obsolete unmerged approach, fixup series or
redundant intermediate pin remains. The runtime state-machine bundle retains
its coherent rationale; UI, adapter, input updates and site policy remain
separately reviewable. No additional history-split finding.

There is one extension runtime update, one workspace extension/nested-runtime
composition update, and one generated configuration `devWorkspace` update.
Every effective runtime pin selects `b0ec2f10525e0bc410ee8052c726241bcf209943`;
codex-web remains `5f15b9293f9b1eef7469a34d7b2044c743160283`. Configuration
still pins confctl `7bee58a52372b95c2198ce3f2a719807a3c2c66b`. Generated
configuration history is preserved. Workspace now starts at shared master
`90005ea3`; its range-diff adds only the expected final pins and installed-guide
reference. The configuration documentation rebase is patch-equivalent.

**No database migrations.** New coordination schema 1 directly contains the
final private lifecycle-binding collection; there is no superseded schema
migration on these branches. Existing lifecycle journals, pending-Codex records,
manifests, clusters and submission schemas remain unchanged. The packet reports
that coordination state remains unmerged, unreleased, undeployed and externally
unconsumed. That provenance makes folding the private-schema changes sound.
Older package generations still cannot ignore coordination state; matching
contracts, retained artifacts and forward recovery remain required.

Runtime/adapter/site/configuration ownership remains appropriate. The new
reconciliation service addresses the demonstrated scheduler failure without
adding a generic execution framework. Installed guidance is appropriately owned
by the runtime and preserves deploy-first discovery. No additional speculative
hardening or scope-expansion finding under the trusted-local-operator model.

## Verification and remaining phase

Read the successful final quick evidence: 25 coordinator tests/130 assertions,
145 Host tests/1099 assertions, one lifecycle regression/15 assertions, four
adapter tests/20 assertions, Ruby syntax and focused native-policy Go tests.
The packet also records JS syntax, native-helper tests, portal compilation,
workspace derivation evaluation and composition checks. Two short reviewer
probes described above ran in the runtime Nix environment; they created only
temporary/in-memory fixture state. No live runtime state was changed.

- Phase: remediation review complete with findings.
- Completed: all ten prior findings assessed; new behavior, final histories,
  pins and migration provenance reviewed.
- Remaining: fix normal-session admission and recovery-capacity accounting,
  then focused verification and any review warranted by the chosen changes.
- Blockers/risks: the findings above; real systemd/native/confctl/profile
  integration and no-reboot continuity remain unverified.
- Next action: lead reconciles the findings before longer checks and the
  authorized deployment. Default-branch integration, reboot and archival remain
  unauthorized.
