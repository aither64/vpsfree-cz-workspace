# 2026-08-07-security-advisories-6-12-95-2

## Goal

Maintain unpublished vpsAdmin security-advisory drafts for all 19 CVEs fixed
by the cumulative vpsAdminOS live-patch series for boot kernel 6.12.95. Update
the original 14 patch-2 dossiers for the deployed patch 4 and add the five CVEs
first carried by patch 3, using patch 3 only as source and historical evidence
while distinguishing the first fixing patch from the corrected cumulative patch
currently deployed.

The user withdrew approval to publish or merge. This initiative is limited to
the feature branch and unpublished vpsAdmin drafts. It must not publish an
advisory, send notification email, merge the feature branch, or remove its
worktree.

## Affected repositories

- `security-advisories`: advisory dossiers, detailed analyses, reviewed
  per-node evaluations, workflow instructions, regression coverage, and
  unpublished draft submission baselines.

The Linux, vpsAdminOS, vpsAdmin, and vpsfree-cz-configuration repositories are
read-only evidence sources for upstream fixes, delegated KVM reachability,
deployed live-patch state, and production workload applicability.

## Approach

1. Rebase the feature branch on the current upstream default branch containing
   the repaired typed kernel-history evidence model.
2. Verify the five additional CVEs against their primary records, stable fixes,
   live-patch backports, published research where applicable, and the current
   vpsAdmin/vpsAdminOS platform source.
3. Add one bilingual dossier and detailed analysis for each new CVE. Update the
   original 14 dossiers to accept cumulative v2, v3, and v4 identities; the new
   five accept v3 and v4 only. Bind every accepted patch to an exact active
   module/version, boot kernel, and clean reviewed vpsAdminOS identity.
4. Treat an observed active v3 as a valid security mitigation while separately
   recording its AMD activation-safety failure. A reboot, effective patch
   removal, disabled state, or transition ends the prior mitigation interval.
   An accepted cumulative replacement and an internal observation that merely
   omits unchanged live-patch metadata do not. Retain internal snapshots so a
   reported runtime transition is still classified. Public responses name only
   the patch version that first fixed each CVE. Deployed cumulative
   replacements remain internal evidence because naming them in durable public
   text becomes stale on the next rollout.
5. Collect fresh production evidence using the deployed history model,
   regenerate all 19 evaluations, inspect the node5.brq reboot and staging
   v3-to-v4 transition, and require every active node to resolve without
   replacing an earlier continuous mitigation date with the v4 deployment
   date.
6. Commit one reviewable change per CVE, run quick local verification, and run
   the mandatory standalone change review. Resolve significant findings before
   any remote draft write.
7. Force-push the rewritten feature branch with lease, inspect GitHub Actions,
   collect one coherent production snapshot for the related batch, dry-run and
   apply synchronization only to unpublished drafts using that time-limited
   shared evidence, commit each resulting submission baseline, and run
   read-only readiness and draft readback checks.

## Compatibility and deployment

The repository changes are assessment data and unpublished draft preparation;
they do not change APIs, schemas, protocols, persistent runtime state, or
deployed configuration. Mixed patch states are represented explicitly. An
accepted live patch mitigates only an interval in which it is loaded, enabled,
out of transition, and bound to a reviewed clean software identity. Missing or
different identities remain affected or unknown rather than inheriting a later
state. An accepted cumulative successor preserves the mitigation interval for
fixes it carries forward; only an effective loss of protection starts another
affected interval.

Draft synchronization uses revision preconditions and fresh evidence matching,
so concurrent remote review or node-state drift stops the operation. Existing
drafts remain unpublished, new advisories are created as drafts, and
`send_mail` remains disabled. Publication and merge are intentionally outside
this plan.

## Testing plan

- Run `bin/security-advisory validate` for all dossiers.
- Collect one coherent production snapshot and evaluate all 19 live-patch
  dossiers with zero blocking nodes.
- Inspect exact v2 and v3 activation, node5.brq reboot, and v4 activation
  transitions from the repaired history. Verify that omitted metadata in an
  internal observation preserves effective patch state while a reported
  runtime transition does not.
- Run `bundle exec rubocop --parallel --force-exclusion`, `bundle exec rspec`,
  and the active Overcommit hooks from `nix develop`.
- Run the mandatory fresh-context change review before draft writes.
- Collect once immediately before the batch, dry-run and apply draft
  synchronization for each of the 19 CVEs with the same evidence document,
  then run `bin/security-advisory ready` with recent shared evidence and read
  every remote record back as an unpublished draft.
- Push the feature branch and require its current GitHub Actions runs to pass.
