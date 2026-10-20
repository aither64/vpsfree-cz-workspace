# Three existing-draft updates: preparation

Status: prepared only; execution is not released. Implementer0 owns the current
Git/source-publication slot. No Git inspection, project CLI, API operation or
Nix-shell startup was performed during this preparation. Source candidate
`0b2f060e61c5480ccd09e93d2ecbace39bcb27a1` comes from the lead's brief and has
not been independently checked with Git here.

This adapts the [original operator procedure](README.md) to updates only. Its
sequential readback, normal-hook checkpoint and stop/recovery rules remain in
force. The original create-only `inspect-step.rb` must not be invoked for this
batch: its no-baseline/create assertions and original order are inapplicable.
Use the update-specific requirements below and the recorded fingerprints in
[updates-prepared.json](updates-prepared.json). Do not alter the original
60-draft ledger, raw outputs or checkpoint lineage.

## Release gate and exact changes

Require successful full RSpec and RuboCop feature CI at the exact reviewed
source head, with both run identities and terminal results retained by the
lead, followed by explicit execution release and the actual exclusive Git and
remote-write slot. Preparation supplies none of these gates. Initial execution
HEAD is the candidate above unless the lead explicitly supplies a replacement.
No dry-run or API call is allowed before release.

| Order | CVE | Existing draft | Starting revision | Intended change | Predicted final revision |
| --- | --- | --- | --- | --- | --- |
| 1 | CVE-2026-74753 | 85 | 13 | Twelve unknown results become mitigated at their reviewed retained corrective boots; storage exclusion remains | 25 |
| 2 | CVE-2026-53260 | 112 | 13 | Storage remains unknown; add the exact reviewed EN/CS current-non-RT / historical-unknown note | 14 |
| 3 | CVE-2026-72069 | 113 | 13 | Same scoped storage-note change; storage remains unknown | 14 |

Perf's public advisory text is unchanged. Eleven mitigation boundaries use
retained 6.12.113 boots; the other uses the earlier retained 6.18.49 boot. These
are supported terminal boundaries, not claims that uncertain earlier exposure
was absent. All twelve non-storage RT rows are unchanged, including their
times and notes. The storage note is exactly:

- EN: `Current kernel lacks the required real-time mode; its earlier configuration is not established.`
- CS: `Současné jádro nepoužívá potřebný režim reálného času; jeho dřívější konfigurace není doložena.`

The starting schema 2 baselines and their revision-13 remote digests are
preserved. Their old dossier digests intentionally describe the prior submitted
content; do not require those old digests to equal the updated dossiers before
sync. The new evaluations must match the updated dossier digests. The existing
reconciler verifies the prior remote snapshot against its old baseline before
writing. Its managed remote digest includes content revision, so an otherwise
unchanged remote object at a different revision also fails the baseline guard.

## One update at a time, after release only

1. Reconfirm session/environment, exact owned worktree/branch and released HEAD.
   Verify complete clean worktree/index, retained ancestry from `8d1413ef`,
   executable normal hooks and no hook/source-identity override variables.
   Verify the frozen snapshot SHA-256 is still
   `61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274`.
   Recheck the prepared file fingerprints and original 60-ledger hash. Retain
   the lead's accepted review and exact source-CI receipts. Stop on drift.
2. Use one owned persistent Nix shell with normal hooks and `umask 077`; reuse
   the existing idle shell only after verifying its identity/environment.
   Expected HEAD is the released source for update 1, then the preceding
   verified update checkpoint. Keep new raw outputs in restricted ignored
   `.state/draft-sync-followup/<CVE>/`, separate from the original creation
   receipts. New sanitized results belong in a separate `updates-ledger.json`.
3. Select the next CVE in the exact table order. Require its existing submission
   file to match the prepared revision-13 schema 2 baseline, ID and remote
   digest. Require the current dossier/evaluation fingerprints to match the
   accepted source, the same 13-node set and the exact intended conclusions.
   Compare current public advisory attributes to the retained original remote
   attributes; they must be unchanged for all three. This includes RT public
   fields: its optional localized storage note is a separate node field.
4. Deliberately run and inspect the existing dry-run, with stdout/stderr only
   in the restricted raw directory:

   ```sh
   bin/security-advisory sync --evidence .state/evidence.json "$cve" \
     > "$raw_dir/dry-run.json" 2> "$raw_dir/dry-run.stderr"
   ```

   Require exit 0, `dry_run: true`, `create_advisory: false`, exact draft ID/CVE,
   dossier digest, unchanged public attributes and exact desired 13 node rows.
   The existing tool reads and verifies the owned draft before returning this
   plan. Dry-run itself does not perform the fresh-evaluation equality check.
   Require no baseline or other source changes from this read-only step.
5. Recheck expected HEAD, whole clean worktree/index, snapshot and baseline
   hashes. Apply this one update only:

   ```sh
   bin/security-advisory sync --apply --evidence .state/evidence.json "$cve" \
     > "$raw_dir/apply.json" 2> "$raw_dir/apply.stderr"
   ```

   Existing sync evaluates the frozen snapshot in memory before its first
   write, compares all reviewed conclusions, and uses revision preconditions.
   There is no standalone evaluation rewrite or extra evidence collection.
6. Require exit 0 and exact returned remote readback: same stable draft ID,
   `state: draft`, exact external ID and single CVE association, unchanged
   public EN/CS attributes, same 13 node identities, and exact desired states,
   times and localized notes. Require predicted revision 25 / 14 / 14 for the
   respective update. This follows twelve / one / one changed node rows and
   no parent, CVE, create or delete changes. An unexpected revision is a stop,
   even if the resulting text appears acceptable.
7. Require the matching schema 2 submission baseline: same draft identity,
   returned remote digest/revision, updated dossier digest and actual
   pre-commit source HEAD. Only this CVE's submission file may have changed.
   It is an existing-file modification, not an added/replaced dossier.
8. Stage only that exact submission path and commit through normal hooks
   using a temporary `-F` message file, with an explanatory body and lines no
   longer than 80 columns. A suitable subject is
   `CVE-2026-NNNNN: checkpoint reviewed draft update`. Verify the staged path,
   diff check, hook receipts, commit parent, one-file scope and clean whole
   worktree/index. No next write before this checkpoint succeeds.
9. Record only CVE, draft state/ID/revision, checkpoint SHA and node counts in
   the new sanitized ledger. Advance only after verifying that row. Report
   each of these three checkpoints to the lead, and any uncertainty immediately.

## Stop, recovery and completion

Stop on the first nonzero exit, uncertain outcome, wrong identity, create plan,
missing/unexpected baseline, revision/content drift, dirty source, snapshot
change or hook failure. Preserve all evidence, baselines and completed commits.
No blind retry, recreate, adopt, reset, stash or automatic rollback. If only
the commit failed after a verified remote update, repair that checkpoint through
lead-coordinated recovery without another remote write. Do not repeat a write
to reconstruct a missing ledger row.

Final local proof must show three exact update-only remote readbacks, 39 node
rows, three normal-hook one-submission-file commits, unchanged source and
evaluations from the released head, frozen evidence unchanged, and a clean
whole worktree/index. Preserve all 60 original recovery commits and consumed
source ancestry. Return the complete separate ledger, final HEAD and exclusive
slot. Do not infer publication readiness from the perf resolution: both RT
storage rows remain unknown, and the separate CIFS assessment is unchanged.

No API/client replacement, source edits, collection, evaluation rewrite,
manual JSON, ready, publication, email, branch rewrite, push, default-branch
integration or lifecycle action is authorized in this loop. Pending period
scope questions authorize no additional CIFS or RT state changes.
