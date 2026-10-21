# Runtime integration rebase follow-up review

The final source series is accepted. No new source findings remain. The runtime
and workspace replacements are suitable for the existing `patch_equivalent`
finish contract without redeploying solely for source integration. The release
helper has one operational defect to correct before use, described below.

Same independent reviewer `/root/final_review`, `gpt-6-astra` with `xhigh`
effort. This follow-up covers general/history and risk/compatibility. The
unaffected architecture and scope conclusions in `final-review.md` remain
accepted. Inspection was read-only except this report: no tests, builds,
deployment, source edits, coordination mutations or nested agents.

Reviewed exact final ranges:

| Repository | Base | Head |
| --- | --- | --- |
| dev-workspace | `dce4784fe0069b061dd76cdf689e2099b4b0e66d` | `ea3f9d36397e8c2c846bd456e51385d73a3a358a` |
| workspace | `4bc49561dd48842b5b26c2e247d6d6b8c6b8a513` | `fae19f1a4f5781fb2b74b0488de02bd834970811` |
| vpsfree-cz-configuration | `a2ad6da408715de811cc6d8ea7b29ac55ea341ec` | `0067299ab9739f522fec0780cda98649ae630406` |

All three worktrees were clean at inspection; their exact HEADs and regenerated
diff hashes match `merge-inventory.json`. Runtime and workspace whole-range
whitespace checks pass. Configuration is unchanged from the accepted
`config-refresh-review.md` range.

The runtime retains two ordered feature commits: `f57beef` for lifecycle
admission and `ea3f9d3` for archive reservation completion. Independent
range-diff and ordered stable patch IDs both confirm exact patch equality with
the previously reviewed `10eccec` and `6ab3b48` series. The upstream baseline
advance changes merge-hook preparation to resolve `ruby` through the initialized
repository shell instead of invoking `RbConfig.ruby` from the runtime package.
Its documentation and tests address the interpreter/native-gem mismatch,
environment restoration and missing-dependency diagnostics. This production
change is in a separate method from the feature changes; no conflicting
execution, locking, journal or receipt change was introduced by the rebase.

Workspace retains documentation commit `8029b350` and runtime-pin commit
`fae19f1a`. Its two ordered patches also match the original `14b36275` and
`4b22d04f` series exactly. The intervening workspace baseline changes only
tracking records. `merge-workspace-equivalence.json` records the reconstructed
final tree; the old and new feature heads have no nontracking differences.
Configuration retains one pin commit `18e0b9dc` and one guide commit `0067299a`.
There are no obsolete feature iterations, unused alternatives or redundant
input-update streams in these final ranges. The upstream runtime fix is
already merged baseline history, not a feature fixup to consolidate.

**No migrations** in the final feature ranges or the intervening runtime and
workspace baselines. Persisted schemas, lifecycle recovery formats and the
finish API are unchanged. Existing predecessor recovery paths still serve
supported deployed state and should remain.

Both consumer locks intentionally select deployed runtime
`6ab3b48f57981f4358094b47cac1ba724c458396`, with the identical locked hash. Local
and origin tracking refs named
`2026-10-19-lifecycle-lock-reliability-deployed` both retain that exact source.
The extension selection and dependency edges remain unchanged. Integrating the
rebased source does not require adding another pin update or deploying the
separate upstream hook-Ruby fix in this initiative.

The following replacement lineage is accepted for the reservation finish proof:

- Runtime: `09a407953026514ae84be81dab9442fd74b6a362..6ab3b48f57981f4358094b47cac1ba724c458396`
  to `dce4784fe0069b061dd76cdf689e2099b4b0e66d..ea3f9d36397e8c2c846bd456e51385d73a3a358a`.
  Ordered patch IDs are `a2ef7f3cbe5b2b86e0ace51f62a54fb222059f65` and
  `e326af1dc642bc85e3e9e2ea5809b7f5e2b6d48f` on both sides.
- Workspace: `dc97c0f0f422e0d6cc6e250c7241c12fe6b73de8..4b22d04f0fefddfd01e744f990d6d9ebb5cbea12`
  to `4bc49561dd48842b5b26c2e247d6d6b8c6b8a513..fae19f1a4f5781fb2b74b0488de02bd834970811`.
  Ordered patch IDs are `f202a0af7bd8a2e884d417964285d663cd21352a` and
  `e5a35cce23ca3db214853145c6d998bd90188eb9` on both sides.

This accepts feature-patch lineage, not identity of the complete runtime trees
or build artifacts. The original deployment, package tests and archive VM
evidence must remain attributed to runtime `6ab3b48`, workspace `4b22d04f` and
configuration `0067299a`. Do not describe those artifacts as built or deployed
from the rebased source heads. The lead reports focused checks passing with
5 tests and 31 assertions; this review does not attest completion of the
new-head CI run.

The finish implementation independently validates owner and reservation binding,
checksummed review/range/verification evidence, exact retained ranges, identical
ordered patches and an applicable exact merge approval. It then verifies current
registered heads, fresh remote ancestry, deployed coverage, unchanged live
system/profile state, settled jobs and absence of a lifecycle fence. Those
normal checks remain required; this report is suitable migration/review evidence
for both mappings, not a substitute for their receipts or live acceptance.

**Important operational finding — release helper still assumes the original
runtime head.** At inspection, `finish-reservation.py` takes final heads from
`journal['operations'][name]['snapshot']` and only permits a nonancestor mapping
for workspace `4b22d04f`. A manually refreshed existing runtime job can succeed
while the original integration journal retains snapshot `6ab3b48`; the helper
will reject current runtime HEAD `ea3f9d3`. Even if the journal snapshot is
updated through normal driver refresh, its workspace-only mapping assertion
still rejects the runtime replacement. This fails closed, but prevents the
authorized release.

Before running it, implement the brief's stated approach: bind final acceptance
to each succeeded job's authoritative snapshot/result, verify its exact current
registered head and remote ancestry, and emit both reviewed mappings using
applicable approval IDs. Restrict mappings to applied, owned deployment coverage
and deduplicate repeated coverage. Preserve the original journal as historical
request evidence; an unchanged requested-head summary must not be presented as
the final merged runtime. This is a bounded completion-script correction, not a
reason to alter the accepted feature series or hand-edit coordinator state.

The runtime job's recorded `baseline_changed` result occurred at `admitted`,
with no observed effect. A fresh snapshot and approval on that same job preserve
the dependent jobs and follow the supported refresh contract. After successful
workers, normal driver resumption and stable finish are appropriate. The user's
explicit instruction to merge all three repositories and release aitherdev now
provides integration and release authorization. It does not request archival of
this initiative.
