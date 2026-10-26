# Findings

## Important — accepted plan creation waits while retaining destination and provider admission locks

Lanes: **risk and compatibility**, general.
Repository: `dev-workspace`; commit
`101a1850253e7cb17f89c8e01f7d11a1b0860948`.
Location: [libexec/dev-session:4058](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/dev-workspace/libexec/dev-session:4058),
called from `start` at line 975 inside `with_creation_lock(slug)` at line 933.

Changing the shared `verify_creation_source!` helper to wait also changes the
accepted plan-session path, not only the two fork checks. `start` already holds
the destination creation lock when it calls this helper. Its
`with_creation_lock` wrapper additionally retains
`WorkspaceProviderAdmission.with_creation`'s shared `creation-admission.lock`.
An external source reader can therefore make this accepted plan request retain
both locks for the remaining initialization-command budget, before any
destination journal or native creation exists.

This contradicts the accepted design's source-wait boundary and the new helper
comment/documentation saying no destination locks are held. It has a concrete
operational consequence: a workspace-wide provider transition cannot obtain
exclusive creation admission and reports `waiting-creation`
(`libexec/workspace-provider-sessions.rb:360`), even though this worker is only
waiting for a source reader. Other destination operations also encounter its
creation lock. The fork path correctly releases destination/provider admission
before both source waits; the plan path does not.

Move fresh plan-source verification outside the destination creation/provider
admission section, preserving the existing journal-owned recovery path and
rechecking destination/journal state under its lock before effects. Add a
focused accepted-plan case with an external source holder that proves destination
and provider creation admission are available during the wait, rejects a changed
source, and cancels without native creation. The new
`TestAcceptedForkWaitsForSourceReadersAndRevalidates` exercises only the fork
endpoint, so its destination-lock assertions cannot establish the plan guarantee.

I found no unbounded deadlock in the inspected production paths: the Go worker
and process-group cancellation still bound this wait. This is an Important
violation of the specified admission boundary, not evidence of an unlimited
hang. Fix it or record an explicit decision accepting the narrower plan behavior
and correct its documentation before proceeding.

No Blocking or additional Important/Advisory findings were identified in this
affected review. The exact inherited baseline and consolidated pins are sound;
the source-lock finding above remains a readiness condition.

# Scope and retained review

Independent retained standalone reviewer `01a172a0-e739-7563-85b4-f3c8fc7f0ef2`,
assigned `gpt-6.1-sol/xhigh`; all four lanes reviewed directly. No nested agents,
source edits, live-state mutations, long tests, builds or CI retries. Only this
report was written. Risk remains **high** because the candidate combines
persistent delivery receipts, package compatibility and lifecycle admission.

I read the complete [baseline packet](baseline-review-packet.md), mandatory
review skill and all four references, current repository AGENTS, applicable
workspace guidance, design/state/resolutions, rollout and relevant owning docs.
I reused [review.md](review.md) and [reboot-review.md](reboot-review.md) for
unchanged delivery, storage and browser behavior, preserving their exact ranges
and reviewer settings. This turn assesses the new source wait and preservation
of the newly selected baseline, with complete final history and pin assessment.

The orphan-backup guard is the earlier prescribed narrow correction: when all
predecessors are missing, the empty-phase initializer refuses if this database's
backup prefix remains. The final delta adds that refusal, its regression and
matching storage documentation; it does not guess a backup or create a new
schema. The parent's failure-before/pass-after and full-suite results remain
supplied verification. No redundant confirmation test or review of that narrow
fix was requested or run here.

# Reviewed exact series and consolidation

All four worktrees were clean and matched these heads. I inspected their complete
recorded base-to-head histories, final changes, messages and comparisons with
the earlier reviewed ranges.

| Repository | Base | Final head | Complete ordered series |
| --- | --- | --- | --- |
| codex-web | `872c7ad3962f9fa9b17358244e27f3e3fac59fc5` | `8b60554bc10c2a6bcbf9732a8b77ad959c317036` | `66ab8c0`, `a9086b0`, `8b60554` |
| dev-workspace | `10bb047513c82d1310e8fcaa797e8772f948dd8a` | `101a1850253e7cb17f89c8e01f7d11a1b0860948` | `c33f5191`, `f29686a5`, `ec53874b`, `902f7554`, `9ed22854`, `76b5c0cf`, `101a1850` |
| vpsfree-cz-configuration | `d12a77374b18e15fe7600f95307114e2e1882828` | `f20e1863f4562faeb8e0db017e6bff3df8b5fae8` | `f5d55557`, `f20e1863` |
| workspace | `cb89659dfe30af6ce3d8f789c8f5eed60e8451be` | `b08175448ae4a22937a7baee8e5888210b75538e` | `9368c8fe9`, `9ab0a185c`, `b08175448` |

**Whole-branch conclusion:** no obsolete unmerged delivery approach, redundant
fixup or transitional migration remains. Earlier delivery corrections are
folded into their owning backend/browser commits. Source-lock waiting is a
separate, independently reviewable behavior commit. The three inherited runtime
commits and two inherited workspace commits preserve the deployed storage
baseline; they are not abandoned delivery iterations.

**Repeated-stream conclusion:** no redundant repeated dependency/channel update
remains in these series. SQLite dependencies/vendor selection is owned by
`66ab8c0`; runtime Go/Nix codex-web selection by `902f7554`; configuration's final
devWorkspace selection by `f20e1863`; workspace's nested runtime selection by
`b08175448`. The earlier configuration pin `2d33a9ca` and workspace pin
`564979a0` are absent from the new series, while their baseline behavior and
original storage-retention refs remain available. Deployment provenance has
not been used to justify redundant intermediate pin commits. The browser
commit's `flake.nix` check-list change is test wiring, a separate purpose from
dependency selection in the same file.

# Deployed-baseline preservation and migration lineage

The packet identifies the selected predecessor source as `ec53874b`. I compared
all **591 tracked blob contents** at that commit with the supplied immutable
source `/nix/store/61cgny1cyg3mrpi2g75yfdvhklxjbm7a-source`: none was missing or
different. I did not activate, switch or independently audit live services.

Runtime `ec53874b` is an ancestor of the candidate. Range comparison of its
three delivery commits with the previously reviewed three shows only the final
library/version/vendor identities and inherited `archiveRecoveryPolicy: 3`
context; browser behavior is patch-equivalent. The source-lock correction is
then added separately. Archive recovery, compact tracking, source-checkout and
coordinator-GC implementation files are unchanged from the deployed baseline;
the new archive receipt export integration retains its earlier reviewed patch.
The final contract preserves archive policy 3 and adds submission schema/policy 1.

For the workspace, I compared the complete parent-to-commit raw mode/blob
deltas of `7f94bfa79` versus `9368c8fe9` and `eda0d9944` versus `9ab0a185c`.
They are identical across **17,204** artifact-removal paths and **11**
storage-maintenance paths respectively. This includes the archived deletion
inventory available in Git, rather than relying on its omitted stored diff.
The final workspace feature adds only `flake.nix` and `flake.lock` selection
changes over those inherited commits. Configuration retains the exact
`f5d55557` retention-documentation commit; relative to deployed `2d33a9ca`, its
final tree changes only the intended lock selections.

The delivery migration remains the owning library's direct schema-3 JSON import
to SQLite `user_version=1`, followed by schema-4 predecessor fences and the
`imported`/`ready` journal. It is in `a9086b0`. The packet reports that no delivery
migration revision has been merged, released, deployed or externally consumed;
all such databases were disposable. This is supplied provenance, not a live
database audit. **Its consolidated migration lineage is sound**, with no upgrade
step for an abandoned branch schema.

There are **no new database migrations** in runtime, configuration or workspace.
The inherited runtime `c33f5191` does introduce persisted compact archive format
3 and policy 3; it is the already deployed baseline described by the packet,
and is retained unchanged, including its predecessor recovery readers. It must
not be mistaken for an undeployed transition that this initiative may remove.
The source wait itself changes no schema, API or journal format.

# Locking, ownership and verification limits

For forks, both Ruby source EX stages are outside destination creation/runtime
locks. Each rechecks lifecycle/manifest and the accepted source identity after
acquisition; journal-bound recovery bypasses the vanished source using its
recorded native thread. Ordinary direct CLI fork acquisition remains nonblocking
under its existing rules. The helper and flock behavior stay with the runtime
that owns session admission; no parallel lock protocol was added downstream.

The Go initializer releases its source snapshot/message lock before launching
Ruby, avoiding a parent/child self-wait. Its transition SH lock remains in force
through creation, so package selection cannot cross the operation. Browser
runtime holders acquire transition admission before their runtime lock.
The production initializer has a four-minute context, with a 210-second command
budget; `processgroup.Run` kills and drains the process group on cancellation,
releasing a blocked Ruby flock. The controlled test covers both fork stages,
stable/replaced source, shutdown cancellation and journal-owned recovery with
one native fork. Its external effects are fixture substitutes; it is not native
or provider/package-transition acceptance. The plan path's extra retained locks
are the finding above.

Semantic lock comparison confirms runtime changes only its codex-web node;
configuration changes codex-web and devWorkspace; workspace changes codex-web
and nested dev-workspace. They agree on library `8b60554` and runtime
`101a1850`, including locked hashes. The extension remains `767dfd5`, siblings
are unchanged, and native Codex remains 0.163.0. The Go pseudo-version selects
`v0.0.0-20261025105210-8b60554bc10c`. These are inspected inputs, not successful
builds of the exact final composition.

Independent verification in this turn was read-only inspection, blob/delta and
range comparisons, semantic pin comparison and full-range `git diff --check`
for all four repositories; whitespace checks passed. The reported 4.7-second
focused Go/Ruby test, Ruby syntax check and composed-lock check are supplied
quick-check results. Earlier native/portal/VM/build results remain bound to
their earlier inputs. I ran none of those tests and did not retry failed CI.
The historical CI lock holder is still unknown; the controlled SH-holder
reproduction establishes the mechanism, not that holder's identity.

The packet's `docs/message-delivery-operations.md` path does not exist. Actual
owning guidance is codex-web `docs/submission-storage.md`, runtime
`docs/workspace-portal.md` and `docs/dev-sessions.md`; current exact actions are
in [rollout.md](rollout.md). Those explain the relevant contracts without
requiring a new operations file solely to match the packet's suggested name.

Remaining gates: resolve/decide the plan-lock finding; final composed package,
native and applicable creation/lifecycle acceptance against corrected exact
inputs; then separately authorized activation and health/naming/conversation,
receipt-integrity and original-attempt reconciliation. The prepared original
repair remains unexecuted and must use current acceptance/pre-transmission
evidence; absent history alone does not permit replay. The updated rollout
correctly plans stale-plan recovery rather than sending an obsolete plan.

No integration approval exists. Locally cached configuration `origin/master`
has also advanced to `95f10b50` with unrelated channel updates beyond the reviewed
base; the candidate does not include those commits. Reconcile the target and
apply the required equivalence/check gates before claiming final merge readiness.
No remote fetch, merge, machine-claim action or mutation of another initiative
was performed here.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-message-delivery-reliability/
