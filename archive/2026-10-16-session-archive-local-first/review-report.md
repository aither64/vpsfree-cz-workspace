# Final independent review

## Findings

### R1 — Blocking — Git recovery does not prove that the retained file objects are recoverable

Risk/compatibility and general lanes. Runtime commit `179a1dee`,
`libexec/workspace-archive-recovery.rb:120` (`verify_snapshot!`), with capture at
lines 31–49 and removal in `libexec/workspace-archive-cleanup.rb:364`.

For a Git-backed snapshot, verification checks only that the saved ref resolves
to the expected commit and that the commit object has type `commit`. Neither
check reads its blobs. `raw_git_contents?` hashes the original checkout against
the object IDs recorded in the tree; that proves the original bytes match those
IDs, but does not establish that the corresponding object contents exist and
are intact in the retained repository. The new batching also deliberately skips
creating individual refs for blobs already named by HEAD.

A clean, stat-matching checkout can therefore be archived after a required blob
has become missing or corrupt: status/tree/index inspection, the original-file
hash, and the current snapshot verification can all pass. The operation then
force-removes the only intact working copy. The same gap permits corruption
between capture and removal to escape the final check. This is an ordinary data
integrity failure within the documented trust boundary, not a hostile-local-user
scenario.

Require integrity/readability proof for the exact Git tree needed for restoration
before destructive removal, delegating object validation to Git and keeping the
work proportional to the retained tree. Preserve the original files or refuse if
that proof fails. Add focused missing/corrupt-blob cases before capture and after
capture but before removal; assert that the original checkout is retained.

### R2 — Important — Retrying an interrupted Git-backed restore never repopulates missing files

General and risk/compatibility lanes. Runtime commit `179a1dee`,
`libexec/workspace-archive-recovery.rb:157` and `:179`.

Restoration invokes `git worktree add` only while the target directory is absent.
Once that directory exists, the Git-backed branch only restores permissions and
copies administration state. If the process or host stops after Git has created
the worktree registration and some files but before checkout has finished, the
saved `restoring.json` allows entry on retry, yet the retry skips checkout.
`restore_permissions` then fails on missing files, or the final digest fails on
partial contents. Every subsequent ordinary retry follows the same path. The
full-copy branch does repopulate its owned incomplete target, so the optimization
introduces this regression.

Reconstruct file contents from the saved Git tree for an owned incomplete restore
before applying the saved permissions/index. Keep the completed-receipt guard
that protects later operator edits. Use the raw retained representation so a
changed filter/line-ending configuration cannot make reconstruction depend on a
new smudge result. Add an interruption fixture with a valid registered target and
missing/partial tracked contents, then prove exact bytes and index after retry.

### R3 — Important — A hung tracking hook can indefinitely block local lifecycle work

Architecture, general and risk/compatibility lanes. Runtime commit `2d7e8efe`,
`libexec/workspace-tracking-sync.rb:121`–`:129`, calling
`libexec/dev-session:7496`–`:7543`; new tracking service has
`TimeoutStartSec=infinity`.

The retry worker holds the session creation lock and slug lock while acquiring
the shared tracking lock and running the Git commit. Only fetch has a timeout;
the commit and its hooks are unbounded. A hanging pre-commit hook therefore
retains the archived session's locks indefinitely. Revival cannot coalesce the
pending transition, and after a revival receipt is queued a subsequent archive
can be blocked the same way. Because the worker processes receipts sequentially,
later sessions' bookkeeping also stops. A shared tracking-lock waiter can extend
this blockage to other sessions.

Bound retry attempts, including waiting and external hook execution, and release
the lifecycle locks on timeout while retaining a pending receipt and normal
owned-index cleanup. Do not bypass hooks. Validate a hanging-hook case with a
concurrent same-session revive/archive, and verify that unrelated staged changes
survive and the latest transition is eventually synchronized. This closes the
gap between the stated local-completion goal and the new background execution.

### R4 — Advisory — Portal restart can leave the final finish time set to the shutdown time

General lane. Runtime commit `2d7e8efe`, `portal/internal/web/server.go:2941`
and `portal/internal/web/operation_state.go:399`.

On portal shutdown, the archive wait returns cancellation while its independent
unit continues. The executor writes `FinishedAt` immediately. After restart,
reconciliation can correctly recover the worker as running and later complete,
but it assigns the actual worker exit time only when `FinishedAt` is empty.
Consequently a successful archive can display the earlier portal-shutdown time
as its finish time. Treat observer cancellation as nonterminal for the worker,
or clear/replace this timestamp from the authoritative worker result. Extend the
restart test to cover the stored receipt and final timestamp, not just worker
survival.

## Reviewed scope and evidence

Independent reviewer: `/root/archive_final_review`, assigned installed-catalog
fallback `lead_reviewed/reviewer`, `gpt-6-astra` / `xhigh`, read-only except this
report. No retained reviewer exists in the threadless initiative. All four lane
references and the mandatory-review skill were read, along with root/repository
instructions, relevant routed lifecycle/Git/documentation/verification/deployment
guidance, the packet, plan, state, design, changed code, adjacent implementation,
tests and owning documentation. No subagents, source edits, deployment or tests
were launched by this reviewer.

Exact committed ranges inspected:

| Repository | Base | Head | Ordered feature series |
| --- | --- | --- | --- |
| dev-workspace | `2b22de8d273a3b75e6cdd62c398fdb2630871d5a` | `2d7e8efe09687ffbe873033359c4d4e998ddbfd5` | `1b2a0e7e`, `3c57e2ea`, `179a1dee`, `2d7e8efe` |
| workspace | `5a9cb6b6f431f930d88fc0d8aa7b9c9cca652b4f` | `65acdda7fea71c8e12c564d72a99df8436e91b3a` | `078e8c88`, `0fcf9d9c`, `65acdda7` |
| configuration | `ae98e9dbf05cd3f6b2d0c32255a4cb2d58c3865b` | `0ced1926547bf4d41ab3d8a5f7ebf01ba840ade9` | `8f9b857d`, `81ab9fad`, `0ced1926` |

The runtime and configuration bases match their locally available origin/master
merge bases. Workspace origin/master is locally `78a18ccc`; the nine intervening
shared-master commits through `5a9cb6b6` are coordination tracking/archive work.
The intervening diff has no feature changes outside work/archive/notes. These
existing shared-master commits must not be rewritten as part of feature cleanup.
The three worktrees were clean and remained on the packet's heads when inspected.
Runtime `git diff --check` passed. Remote refs were not fetched during review.

Inspected quick evidence: final focused Ruby reports 7 runs / 122 assertions;
focused and rebased Go evidence passes; the later `rebased-session-go.log` also
passes the entire internal/session package and the exact command-timeout error
regression. The corrected synthetic predecessor-journal schema is appropriate.
The focused tests do not cover R1–R3. Long package, scale, real systemd restart and
deployment acceptance remain outstanding, as intended by the review gate.

## Whole-branch history and repeated-update conclusion

The whole committed feature series and final diffs were inspected, including the
inherited Codex baseline. No obsolete unmerged implementation approach or
fixup-only commit remains in these series. The Git-recovery change and the
local-completion/supervision change have coherent separate purposes. Keeping
local journals, retry receipts/service, completion proof and portal execution in
the latter commit is justified: enabling local completion without its durable
retry/status and compatibility support would leave an incomplete contract.

The inherited runtime commits `1b2a0e7e` and `3c57e2ea` are exact retained source
commits, not recreated archive iterations. The update-codex rollout record
documents successful system/profile jobs against configuration `107255f8` and
the preserved runtime, with actual native Codex 0.163.0 verification. The workspace
skills/override composition at `65acdda7` matches `f5da0f7e` apart from this
initiative's runtime selection. Keeping supported baseline behavior is correct.

Each logical runtime consumer-pin stream is consolidated: workspace has only
`0fcf9d9c`; configuration has only `0ced1926`. The old `107255f8` devWorkspace pin
was not copied into this branch. Configuration's separate `81ab9fad` updates the
system llm-agents input, while runtime-transitive llm-agents is part of its
devWorkspace input; these are distinct consumer roles, not redundant updates.
Runtime has one Codex/codex-web dependency update. No redundant repeated pin
stream remains, and no exception justified solely by development deployment is
needed. Retain the exact other initiative's deployed refs and rollout evidence.

## Format, migration and compatibility conclusion

No application database migrations. The persisted format lineage is explicit:
inventory 1 to 2; Git/full-copy record format 2; archive journal 2/3 to 4;
cleanup sidecar 1/2 to 3; revive journal 3/4 to 5; new tracking receipt 1; portal
operation store 1 to 2. Existing predecessor journals and full snapshots are real
supported persisted boundaries, not shims for discarded unmerged designs.
New formats have not been deployed by this initiative according to its packet
and state. There is no intermediate migration to consolidate.

Legacy archive/revive journals retain their synchronous commit policy. New
journals use `tracking_saved`; private receipts preserve exact operation and
tracking proof before runtime retirement. Revival replaces the receipt under
the same session locks; deletion removes it after its own transition. Sensitive
sessions retain their Git exclusion path. The normal lifecycle, ownership,
coordinator and package-generation fences remain in place.

The host checks inventory-2 recovery, tracking receipts (including synced ones)
and schema-2 portal stores on package selection and candidate activation. A
target lacking the corresponding capabilities refuses them. Outstanding
lifecycle journals already fence package changes. Old portal readers cannot
read the new receipt fields, so retaining the execution capability fence is
necessary. Recover forward; do not delete persisted evidence to downgrade.
R1 and R2 prevent accepting the recovery contract as implemented despite this
sound version lineage.

Actual consumers are correctly placed: generic dev-workspace owns lifecycle,
private state and supervision; the workspace selects it through the unchanged
extension `767dfd587e346168e1443e65ccdb67ce748f3fe3`; configuration maps its existing
dev-workspace/devWorkspace channel to the host input. Both final locks select
runtime `2d7e8efe`, codex-web `a0561fad`, and llm-agents `e85b9921` for the runtime;
the separate system llm-agents role selects the same revision. The application
remains a user-profile package. System-before-profile activation and preservation
of the update-codex owner's reservation are appropriate; no fleet-wide or
database rollout is introduced.

Before deployment, refresh against the other owner's final deployed configuration
baseline. Its current state records a separate pending DeepSeek configuration
correction (`9721c331`) for fields rejected by Codex 0.163.0. This review does not
certify deploying an older configuration over that correction once it lands.

## Distinct lane conclusions and remaining acceptance

- General: history, commit splits and focused verification are coherent. R1–R3
  need remediation or the policy's explicit decision process; R4 is a bounded
  presentation defect. Reusable docs are in the runtime, site instructions link
  the behavior, and rollout evidence is kept in session records. Clean the
  accidental “The For” sentence in the archive guide when touching it.
- Architecture/repetition: provider ownership, existing lock/commit helpers and
  systemd supervision fit the existing design. No speculative framework or
  equivalent downstream implementation was introduced. R3 exposes the concrete
  coupling that the background retry still retains with lifecycle locks.
- Scope/proportionality: the change addresses the measured copy/ref cost and
  portal deadline failure without changing archive eligibility or curating
  artifacts. Using Git and systemd is proportionate. `RemainAfterExit=yes` units
  are never collected after terminal receipts expire, so each attempt retains
  manager/unit state until an explicit stop or manager restart. Record that
  bounded operational residual and a follow-up cleanup policy; it need not grow
  into a task framework or block this feature on its own.
- Risk/compatibility: the trust boundary, version gates, coalescing locks and
  deployed baseline preservation are appropriate. R1 is a destructive data-safety
  blocker, and R2 is a recovery interruption gap. Long acceptance should include
  exact-byte restoration, the specified fault cases, real systemd cancellation/
  restart and receipt reconciliation, legacy journals, incompatible-package
  refusal and final composed package/service activation.

Conclusion: **not ready for long integration tests or deployment** until R1 is
fixed and R2/R3 are fixed or explicitly decided under mandatory-review policy.
Whole-branch history and format lineage are acceptable; no merge authorization
is supplied by this review.
