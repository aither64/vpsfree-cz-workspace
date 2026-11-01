# PR74 publication plan — approval required, not executed

Related PR: https://github.com/vpsfreecz/vpsadmin-webui/pull/74
Old remote head alias: `refs/heads/dev/haveapi-async-client`.
Own registered branch: `refs/heads/dev/vpsadmin-haveapi-upgrade`.
Repository: `git@github.com:vpsfreecz/vpsadmin-webui.git`; target `main`.

The user permits PR reuse. That does not yet authorize rewriting the exact
published commits. GitHub cannot retarget PR74's head to our new branch. Reuse
requires replacing its existing remote alias only after a concrete final-head
approval. The old session's local registration/branch/worktree/records and PR63
remain untouched. The new branch stays registered and tracks its own remote ref.

Old feature base: `7860521f30826c3886c89c35e8ab6f4e082e0a4b`.
Old published head: `5dd2333b9af230d4a81c8f772cbbb08d39b14913`.
Published commits that replacement would remove from PR74's visible series:

- `0d05a2584bf30ee4acfa1d64bf00325cdda62934` — injectable package pilot.
- `5dd2333b9af230d4a81c8f772cbbb08d39b14913` — prior package proof docs.

Old authorized local final content also includes:

- `3b2eed453f385ee37d07c7339edcce8fc28ffd31` — local archive dependency.
- `8772bab21cd8739bf4672cdf4976aea2a6e59de3` — production replacement.

New base: `5a2d2bdc3ad7a827038f877d75959916528db844`.
New exact final head: `014f7b9c9f451d6275af73c4af30a24668b77b7b`.
New complete range: `5a2d2bdc3ad7a827038f877d75959916528db844..014f7b9c9f451d6275af73c4af30a24668b77b7b`.
`content-mapping.json` describes final production source carried forward,
current-main reconciliation and new release metadata. The new branch contains
one final registry dependency stream plus production adaptation. No database or
persisted-format migration, deployment or externally consumed new boundary.
The old source commit is not an ancestor of the reconstructed branch.

Execution conditions and ordered steps:

1. Finish commits, quick checks, mandatory final review and longer checks.
2. Publish only our own branch over SSH and verify its exact remote head.
3. Lead presents this exact old/new range, source map and no-migration conclusion
   for explicit authorization to rewrite PR74's two published commits.
4. After that approval, freshly inspect PR74 and ls-remote for its head ref. If
   the actual old head differs from the approved `5dd2333b...`, stop and refer
   the changed range to the lead; do not infer permission for newer commits.
5. Use an exact lease, not a general force push. With the final approved head
   substituted for FINAL_SHA, the intended command is:

   git push origin FINAL_SHA:refs/heads/dev/haveapi-async-client --force-with-lease=refs/heads/dev/haveapi-async-client:5dd2333b9af230d4a81c8f772cbbb08d39b14913

6. Verify our own branch and PR74's head alias both equal FINAL_SHA and its PR
   metadata still targets main. Cancel only superseded queued/in-progress CI for
   that exact PR head branch under the verification procedure.
7. Record the exact fresh lease evidence and both resulting refs. Update the
   related PR's title/body around the final implementation as directed by lead.

Neither branch publication nor PR update authorizes main integration or deployment.

The initial reviewer inspected prior head
`39f8fd7d2bee0c4754f0f9921d97855da7fbdddf`. Direct narrow R2 remediation was
folded into final head `014f7b9c9f451d6275af73c4af30a24668b77b7b` with preserved
authorship. See `review-r2.md` and exact old/new `review-r2-range-diff.txt`.
The current approval candidate is the latter head/range above; the old published
PR74 commits and exact lease remain unchanged. No rewrite approval or push yet.
