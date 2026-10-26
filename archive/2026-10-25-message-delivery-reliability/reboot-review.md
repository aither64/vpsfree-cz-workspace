# Findings

## Blocking — an orphaned durable backup can become an empty authoritative ledger

Lane: **risk and compatibility**, with general-lane coverage implications.
Repository: `codex-web`; backend commit
`0314a832b786682633074a9d032e48adff4d7800`, final head
`f391c5e98c1cb9adab60dbe3dd5dcf019c0f3089`.
Location: [codex/submission_migration.go:203](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/codex-web/codex/submission_migration.go:203),
in the empty-phase path beginning at line 162; backup publication is at lines
192–195 and import/journal commit at lines 287–294.

The supported legacy-only import has a recoverable interruption state that
startup silently treats as a fresh installation:

1. The persistent primary JSON path is absent; the socket-adjacent legacy JSON
   contains receipts, including an unresolved `submitting` attempt.
2. Initialization creates schema 1, reads the legacy source, and preserves
   `database.schema3-backup-<digest>`. `atomicSubmissionFile` syncs the file and
   its containing persistent directory before returning.
3. The process/machine stops before the import transaction commits. SQLite has
   no committed receipt rows or `migration_phase`/`import_sources` journal.
   Reboot removes the legacy directory under `/run`; the checksummed backup
   remains beside the database.
4. On restart, lines 164–202 inspect only the original predecessor paths. Both
   are absent, so `chosen` stays nil. Line 203 supplies an empty ledger; the
   subsequent transaction commits zero receipts and sources with no digests.
   Initialization publishes fences and marks that database ready, without
   inspecting or reporting the retained backup.

The receipt bytes remain in the backup, but normal reads/exports now report them
absent and the newly ready journal permanently bypasses their import. This loses
the uncertainty fence that must prevent another native submission. For example,
`SendWithOptions` at `codex/client.go:5269` sees no prior attempt, and at line
5307 records a new prepared attempt. The HTTP retry's history lookup can recover
visible acceptance, but missing history does not recover the lost `submitting`
state: `SendAttemptedWithOptions` at line 5503 returns false without error, and
the handler proceeds to `Send`. Native IDs provide correlation, not duplicate
suppression. Thus an unresolved earlier send can become eligible for replay.

**Required correction:** before accepting an empty-phase initialization as
empty, detect this database's retained migration evidence and fail closed when
the predecessor needed to resolve it is absent. Do not select an unreferenced
backup by guesswork: checksum names alone do not establish source precedence or
which of multiple snapshots was authoritative. A durable intent protocol is an
alternative if justified, but explicit refusal is sufficient for this case.
Preserve the backup and avoid publishing a ready empty journal or fences.

Add a focused regression constructing the post-backup/pre-import-commit state,
removing the volatile source, and asserting refusal plus unchanged backup bytes
and no ready empty ledger. The five cases at
[codex/submission_database_test.go:281](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/codex-web/codex/submission_database_test.go:281)
all start from a completed import and retain its journal/rows, so none covers
this failure. This conclusion follows the committed control flow; I did not run
a crash reproduction or modify a fixture.

This finding does **not** assert recovery before any durable copy exists. The
legacy `/run` source had no reboot durability then. Here durable evidence already
exists and is ignored; refusing an ambiguous empty initialization is within the
migration's data-safety boundary. Fix before further long integration acceptance
or activation.

No additional Blocking, Important or Advisory findings were identified in the
affected refinement. The candidate is not ready while this finding remains.

# Review identity and scope

Assigned independent standalone reviewer: `/root`, catalog role
`gpt-6.1-sol/xhigh`. This is the user-directed fallback because the previous
reviewer cannot receive another turn through the available native API: direct
input to its v2 subagent is rejected. The original reviewer
`/root/message_delivery_final_review`, its `gpt-6.1-sol/xhigh` settings, original
exact ranges and [report](review.md) are preserved. I authored none of the
implementation and used no nested reviewers or agents.

Risk remains **high**: persisted receipt state, migration, host reboot recovery,
delivery uncertainty and forward-only package compatibility. I read the mandatory
review skill in reviewer mode, all four lane references, the complete
[affected packet](reboot-review-packet.md), original packet/report, plan, design,
state, applicable workspace procedures and repository AGENTS. The workspace
feature's AGENTS is identical to the shared workspace copy. Documentation and
handoff guidance informed evidence placement; this report is the only write.

This is an affected-lane review of the reboot refinement and refreshed exact
heads, with complete history assessment. The original review supplies the
unchanged behavior assessment. I compared the original library head `7c84dc4`,
narrow-fix head `0d17f1e`, and refined head `f391c5e`, and the original/final
runtime and downstream ranges. The narrow attachment fix retains the original
empty selection and adds a mounted-browser regression; the timing fix supplies
the sole scoped attempt ID. Runtime deltas beyond pins are the three diagnosed
fixture corrections. These preserve the earlier assessed design.

# Complete branch history and dependency selections

All four checked worktrees were clean and matched the supplied final heads.
The recorded bases below are also their merge bases with the locally available
`origin/master` refs; I did not fetch or certify current remote tips.

| Repository | Recorded base | Reviewed final head | Complete ordered series |
| --- | --- | --- | --- |
| codex-web | `872c7ad3962f9fa9b17358244e27f3e3fac59fc5` | `f391c5e98c1cb9adab60dbe3dd5dcf019c0f3089` | `66ab8c0`, `0314a83`, `f391c5e` |
| dev-workspace | `10bb047513c82d1310e8fcaa797e8772f948dd8a` | `48476400290d4d106d0d123ab0268692d3801c48` | `013b5c14`, `afc1f9f9`, `48476400` |
| vpsfree-cz-configuration | `d12a77374b18e15fe7600f95307114e2e1882828` | `229b8e9f4fd2d0b14e34775fecd3b3a777cab3a9` | `229b8e9f` |
| workspace | `b1b86b2b8a075666ccdef7f9d254047be972508a` | `136caa22748d3d4e63e471f4b7c007ab4e58fbdb` | `df1944a20`, `7253da4a1`, `00fe575af`, `01c06f603`, `136caa227` |

I inspected the complete series, messages, final changes and original-to-final
comparisons. The workspace's first four commits remain shared-master
coordination ancestry; its merge base with shared local master is `01c06f603`.
Its delivery feature diff is only `flake.nix` and `flake.lock`. Those earlier
records are unchanged from the original review and are not additional delivery
implementations.

**History conclusion:** no obsolete unmerged approach, fixup commit or
transitional migration remains in these final series. The bootstrap correction,
review remediations, reboot refinement and fixture corrections are folded into
their owning logical commits. The separate dependency/backend/browser and
dependency/storage-package/plan-browser splits remain coherent. The coupling of
admission claims and transport restoration still justifies the backend split.

**Repeated-update conclusion:** no redundant repeated pin stream remains.
SQLite modules/vendor selection is owned by `66ab8c0`; the runtime's Go/Nix
library selection by `013b5c14`; configuration's runtime channel selection by
`229b8e9f`; and the workspace's nested runtime selection by `136caa227`.
Superseded intermediate selections are absent from the final series, with no
claimed consumer boundary requiring their retention.

Semantic lock comparison confirms that the runtime changes only its codex-web
node; configuration changes only codex-web and `devWorkspace`; the workspace
changes only codex-web and nested `dev-workspace`. All select library `f391c5e`
and runtime `48476400` with matching locked hashes. The Go pseudo-version is
`v0.0.0-20261025102342-f391c5e98c1c`. The existing channel maps `dev-workspace` to
`devWorkspace`; the workspace retains its nested override, extension and sibling
inputs. Native Codex remains 0.163.0. These are inspected selections, not proof
that the final packages have been built or activated.

# Migration, architecture and compatibility conclusions

The sole migration is in backend commit `0314a83`: deployed schema-3 JSON to
SQLite `user_version=1`, then schema-4 predecessor fences, with `imported` and
`ready` journal phases. Bootstrap publishes the schema atomically. There are
**no migrations** in dev-workspace, configuration or workspace. No intermediate
branch schema is retained as a supported predecessor, and no migration merely
upgrades an abandoned feature iteration.

The packet explicitly reports that no intermediate migration/schema has been
merged, released, deployed or externally consumed; prior builds and CI databases
are disposable. This is supplied provenance, not a live-state audit. Under that
provenance the consolidated migration lineage is sound; its pre-commit recovery
behavior has the Blocking defect above. A later fix need not preserve an
undeployed intermediate schema.

For the reviewed committed boundaries:

- `imported` recovery keeps the committed rows and journal, requires the exact
  configured source paths, rejects changed present contents, and verifies the
  database-sibling backup's expected name and checksum when an imported source
  has disappeared. It publishes fences without reimporting records.
- `ready` recovery validates configured identities and every present fence
  before restoring missing fences. It neither imports the backup nor rolls back
  newer records. Requiring the original backup after readiness would be
  unnecessary because the database is authoritative.
- The shared ordered predecessor-lock helper is an appropriate library-owned
  boundary. Initialization uses its already-locked verifier, avoiding recursive
  acquisition; the ready fast path acquires the same ordered locks. The change
  introduces no parallel downstream implementation or speculative framework.
- The runtime's portal/provider constructors retain common socket-derived
  persistent paths, with a socket-adjacent legacy fallback. Its existing new
  contract gate requires schema/policy 1 once SQLite files or sidecars exist.
  Predecessor application writers must still be excluded by the normal package
  transition. Old JSON backups are not a supported rollback over newer receipts.

The owning library's README/reference link to `docs/submission-storage.md`,
whose changed text correctly describes the committed-import and ready
boundaries. The runtime guide links to that owner. No security, ownership or
proportionality defect beyond the stated orphan-backup data-safety finding was
identified in this affected review.

# Verification evidence and remaining gates

Independent checks in this turn were read-only inspection, commit/range
comparisons, semantic lock comparison and `git diff --check` for all four full
ranges; whitespace checks passed. I ran no Go/browser/native/integration tests,
CI retries, builds, live SQLite reads or deployment commands.

The packet reports five new restart/refusal cases and the refined full library
Go suite passing (about 22.7 seconds). Their assertions preserve the unresolved
receipt/digest, verify private persistent backup placement, restore missing
fences, and refuse a corrupt backup or changed source. They simulate retained
post-commit states rather than the orphan-backup interruption described above.

Broader portal Go, pinned native contracts, library CI, runtime fast and
archive/revive CI, and a composed-profile build are **previous supplied
verification**, including earlier candidate heads. They were not rerun or
re-attested for the refreshed exact package derivations here. The earlier
configuration build stopped at its confirmation prompt; a prepared `--yes`
invocation is not a successful build or activation.

Creation CI `40182797562` remains failed, not accepted by retry. The supplied
failure concerns a busy fork-source slug lock. I confirmed `libexec/dev-session`
is unchanged across the final runtime range and inspected
`verify_creation_source!`/`with_slug_lock`: the rejection path predates this
feature. The competing process is still unidentified. This evidence separates
that observed failure from the changed submission storage; it does not prove
creation acceptance or justify a blind rerun.

I also inspected [recover-original-attempt.py](recover-original-attempt.py) as
prepared operational evidence: it checks ready/schema identity and the exact
payload fingerprint/indexes/empty claim, refuses a queued counterpart, makes and
syncs a consistent SQLite backup, then rechecks and compares the full original
row under `BEGIN IMMEDIATE` before updating payload/state/claim together with
an exact-one-row requirement. It does not send a message. Its disposable results
are supplied evidence. Current complete native history, original
pre-transmission proof, appropriate writer exclusion, held machine ownership
and compatible activation remain execution prerequisites; absent history alone
does not permit resetting the attempt.

Remaining gates are the orphan-backup fix and focused coverage; final package
and applicable lifecycle acceptance tied to the corrected exact inputs; and
actual activation, migration/integrity, health/naming/conversation continuity
and original-attempt reconciliation. The rollout's selected-source list and
some state summaries still name older candidates and must be reconciled before
execution. No migration, profile/system activation or live original-attempt
repair was performed by this review or established by these prepared records.
Review and successful checks do not authorize default-branch integration.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-25-message-delivery-reliability/
