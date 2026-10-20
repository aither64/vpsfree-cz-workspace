# Sequential unpublished draft synchronization

Prepared only. No API, Git, sync or reservation action has been executed for
this operations package. Implementer1 is the designated single writer only
after the lead releases execution. The user already approved unpublished
drafts for these exact 60 CVEs; this packet does not request another approval.

[order.txt](order.txt) and [order.json](order.json) preserve the exact order in
`approved-cves.json`. There are 60 unique IDs, equal to the three assessment
packages. Do not add, skip, reorder or automatically substitute a CVE.

## Release and source invariants

Before the first API request, receive the lead's exact reviewed final source
HEAD and execution release. Required gates are complete-source commits, quick
checks, final independent whole-branch review and the assigned longer checks.
All owners must have finished substantive writes. Obtain the actual exclusive
Git/remote-write slot at that point; no reservation is claimed by preparation.

Reconfirm the exact session/environment binding, owned worktree and branch.
The project worktree is
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-vpsadmin-kernel-cves/security-advisories`.
The expected branch is `2026-10-19-vpsadmin-kernel-cves`. At the beginning of
each CVE, HEAD must be the released source head or the preceding verified
submission checkpoint. The whole worktree and index must be clean, including
other owners' files and untracked source outside ignored `.state/`.

Keep the exact ignored `.state/evidence.json`, schema 8, collected
`2026-10-19T21:48:39Z`, byte SHA-256
`61904e984266df2f6c53435b2b026b0d0980b35a23ed843eebf95b23c27c9274`.
Do not collect, rewrite evaluations, alter attestations, or substitute a newer
snapshot. Stop if the file or deployment/security scope changes. An old wall
clock collection time alone does not invalidate this coherent snapshot.

Use the repository Nix environment for CLI and Git commits. Check that the
installed Overcommit pre-commit and commit-msg hooks are executable and active,
and that no environment variable disables or filters them. Do not install,
sign, bypass or rewrite hook configuration automatically. Do not set
`SECURITY_ADVISORIES_SOURCE_COMMIT` to conceal the actual current HEAD.

After execution release, enter one owned persistent `nix develop` shell for
the related sequential operation. Run the CLI and normal-hook commits inside
that same shell instead of restoring the Nix environment for each CVE. Keep
the shell in the exact owned project worktree. This only avoids repeated
environment startup: verify the exact expected source HEAD, frozen snapshot
and clean source/index at every step as specified below. Do not retain or set
hook-disabling environment variables. If the shell exits, stop and recheck
the last verified checkpoint before resuming in the repository environment.
No persistent shell is started during preparation.

## One CVE at a time

These are operator steps, not an executable batch. Select the next ID from the
ordered file only after the preceding baseline commit and sanitized ledger row
are verified. The operator reviews each dry-run before invoking apply. Unknown
node conclusions are permitted in an accurate unpublished draft; they must not
be replaced to make the batch appear complete.

1. Record expected HEAD, verify a clean index/worktree, confirm the snapshot
   hash and reread the selected committed dossier/evaluation. The first run
   expects no submission baseline or pre-existing approved-CVE draft. If that
   expectation changed, stop for duplicate/recovery reconciliation.
2. Use the owned persistent `nix develop` shell in the project worktree, entering
   it once after execution release. Use `umask 077`. Keep all CLI
   stdout/stderr and full returned snapshots under ignored, restricted
   `.state/draft-sync/<CVE>/`. Never copy raw Node rows, texts, notes, tokens or
   full submission output into the session ledger or user-facing output.
3. Run the existing dry-run with the explicit frozen evidence path:

   ```sh
   bin/security-advisory sync --evidence .state/evidence.json "$cve" \
     > "$raw_dir/dry-run.json" 2> "$raw_dir/dry-run.stderr"
   ```

   Require exit 0, the exact requested CVE, the expected create/update identity,
   the reviewed bilingual fields and exact evaluated active-node set. Inspect
   all node states and any unknown counts without changing them. Dry-run uses
   the committed evaluation; it does not itself prove fresh-evaluation equality.
   The apply step performs that guard in memory. An unexpected existing draft
   or baseline is a stop, not permission to overwrite or adopt it.
4. Verify HEAD, snapshot hash and clean source/index again. If a dry-run wrote
   a recovered local submission baseline, stop and use the recovery section;
   do not hide that change or proceed to apply with dirty source.
5. Apply exactly this one CVE through the existing tool:

   ```sh
   bin/security-advisory sync --apply --evidence .state/evidence.json "$cve" \
     > "$raw_dir/apply.json" 2> "$raw_dir/apply.stderr"
   ```

   Do not call `collect`, `evaluate`, `adopt`, `ready`, `publish`, email tools,
   custom API code or another CVE concurrently. Any nonzero exit, interruption,
   timeout or ambiguous response stops the batch immediately.
6. Require exit 0 and inspect the tool's final exact remote readback. It must
   have the expected advisory ID/external ID, `state: draft`, the exact single
   CVE, unchanged reviewed EN/CS fields, exact evaluated active-node set and
   states/times/localized notes, and the guarded content revision. The tool
   already enforces these equalities and reads the revision before and after
   child enumeration. Its returned snapshot is that readback, not a proposed
   request. No separate collection or publication-readiness call is needed.
7. Read `advisories/<CVE>/submission.yml`. Require schema 2 and the same
   advisory ID, remote digest and content revision as the verified returned
   snapshot, with the dossier digest and actual pre-commit source HEAD. Check
   that only this one submission file changed. If anything else changed, stop
   without resetting, stashing or staging it.
8. Write a temporary commit-message file under restricted ignored `.state/`
   and stage only this exact submission path. Use the normal hooks:

   ```sh
   git add -- "advisories/$cve/submission.yml"
   git diff --cached --check
   git commit -F "$raw_dir/commit-message.txt" \
     > "$raw_dir/commit.log" 2>&1
   ```

   Before committing, verify the staged set is exactly that one file. A suitable
   subject is `CVE-2026-NNNNN: record draft submission baseline`; the explanatory
   body binds the reviewed source/evaluation to the verified unpublished draft
   and explains drift/recovery protection. Wrap all lines at 80 columns. Keep
   check transcripts and local environment details out of the message.
9. Require the normal commit and hooks to pass. Read the resulting HEAD, confirm
   that the commit changed only this submission file, and confirm a clean whole
   worktree/index. Do not amend, rebase, fetch or push during this loop. Retain
   completed baselines. If the hook or commit fails, no next CVE write is allowed.
10. Append one sanitized ledger row containing only CVE, advisory ID, draft
    state, content revision, checkpoint SHA and state/count totals. Only then
    advance to the next ordered CVE. Report progress in five-CVE batches, while
    retaining one commit per CVE and immediate stop behavior.

The aggregate output is a count of verified drafts and explicit stopped/unknown
items. It does not claim publication readiness or permission to publish/email.

## Existing guard and readback ownership

The inspected `bin/security-advisory` CLI and `Reconciler#sync` own API access,
stable external-ID recovery, expected-content-revision chaining, exact remote
readback, per-operation submission checkpoints and evaluation equality.
`sync --apply --evidence` evaluates the supplied snapshot in memory with
`persist: false` and checks it against the committed result before its first
remote write. `ensure_source_committed!` checks the entire worktree. A successful
apply then calls `remote_snapshot(expected_revision: ...)`,
`verify_desired_snapshot!` and `persist_submission` before returning.

The internal per-operation checkpoints are local recovery records; they do not
replace the required normal-hook Git commit before the next CVE is written.
The operator packet adds sequencing and review, not another API/client or
reconciliation implementation. Source hashes inspected during preparation
are recorded in [prepared.json](prepared.json); recheck relevant guards if the
reviewed final branch changes them.

## Stop and recovery

On the first failure, uncertain outcome, unexpected existing draft, revision
drift, source dirtiness, snapshot mismatch or hook failure, stop the batch and
report the exact CVE/stage to the lead. Keep raw output, ignored evidence,
submission baseline and completed commits intact. Do not delete/recreate a
draft, retry apply automatically, reset the index/worktree, hand-edit an
evaluation, adopt a differing remote object, or continue with the next CVE.

The lead and designated owner inspect the existing external-ID/revision and
submission recovery path. A lost atomic-create response may be recovered by
the existing tool only when its exact untouched-create contract matches; a
different remote draft needs explicit review. A partial later write may already
have a local submission checkpoint. Any read-only recovery call is deliberate,
not a blind write retry, and the selected source snapshot remains frozen.

If a complete remote readback succeeded but only the Git commit failed, repair
the hook/index issue without another remote write, verify the submission and
commit that one baseline normally. If the process stopped after the commit but
before the ledger row, inspect the existing commit/readback and recover the row;
do not repeat the API write. Resume from the first unverified CVE only after
the lead accepts the concrete recovery evidence and releases the next step.
This is internal execution coordination, not a new user approval gate.

No cleanup, lifecycle transition, deployment, source integration, publication
or email operation follows automatically. Leave the session open.
