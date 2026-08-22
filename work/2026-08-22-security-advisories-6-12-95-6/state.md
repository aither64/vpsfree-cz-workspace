# 2026-08-22-security-advisories-6-12-95-6

## Repositories

- `security-advisories`: planned branch
  `2026-08-22-security-advisories-6-12-95-6`; worktree created under
  `worktrees/2026-08-22-security-advisories-6-12-95-6/security-advisories`
- `vpsadminos`: read-only inspection of `origin/staging` and live-patch history
- `vpsadmin`, `vpsfree-cz-configuration`, Linux upstream: read-only evidence
  sources as needed during candidate verification

## Status

- The user approved the 26-CVE candidate list.
- Complete bilingual dossiers and typed production evaluations have been
  prepared for all 26 CVEs.
- All 26 approved vpsAdmin advisories have been created as unpublished drafts
  and read back at content revision 13. Their exact baselines are committed and
  pushed. Final GitHub Actions are running on the baseline head.

## Commands run

- `bin/dev-session current`
- inspected the workspace and repository status
- fetched `security-advisories` and `vpsadminos` remotes over SSH
- read the security-advisories repository instructions and vpsAdmin security
  audit skill
- inspected live-patch-related vpsAdminOS history and advisory repository refs
- created the security-advisories feature worktree at baseline `9f21948`
- initialized the locked Nix/Ruby environment and installed active Overcommit
  hooks
- inspected the patch-v5-to-v6 canonical coverage diff, cumulative patch, and
  v6 implementation tests at vpsAdminOS commits `d9bd139cd` and `97a8c8fc6`
- cloned the official Linux vulnerability data and verified its pinned
  `d9dda40c` snapshot as well as current records
- cloned the vpsFree.cz Linux backport branch over SSH and verified all 26
  documented backport commit subjects through the GitHub API
- queried the vpsAdmin security-advisory index read-only for every candidate
- applied the workspace bilingual user-facing writing workflow after settling
  the technical assessments
- collected fresh production evidence at 2026-08-22 19:16:41 UTC with the
  expanded required kernel-option set
- validated and evaluated all 26 dossiers against the shared evidence snapshot
- ran `bundle exec rspec` and `bundle exec rubocop --parallel
  --force-exclusion` from the locked Nix environment
- attempted the first dossier commit in the ambient shell; the active
  Overcommit hook correctly stopped because its pinned gems were unavailable
- committed all 26 dossiers and the shared regression coverage from the locked
  Nix development environment, with all active hooks passing
- ran the mandatory fresh-context review against base `9f21948` and head
  `57b68da`
- verified the reviewer's primary-source findings against the deployed kernel,
  LXC configuration, production command lines, and current CVE CNA records
- recollected production evidence with `CONFIG_INET_SCTP_DIAG` and reevaluated
  all 26 dossiers
- reran dossier validation, RuboCop, and the focused dossier RSpec suite after
  the corrections
- stopped a redundant second production collection at the user's request when
  the prior coherent snapshot expired during editorial follow-up
- changed evaluation, sync, and readiness reuse to measure Node freshness at
  the snapshot's recorded collection time instead of later wall-clock time
- added regression coverage for delayed evaluation, delayed sync and readiness
  reuse, stale-at-collection rejection, and future-timestamp rejection
- reevaluated the two narrative-adjusted dossiers from the existing 20:02 UTC
  snapshot without another production collection
- ran the final mandatory follow-up review against commits `0f40b46` and
  `a850e72`
- ran the complete RSpec and RuboCop suites after the final review
- fetched the SSH remote and confirmed the baseline still matches remote HEAD
- pushed feature head `a850e72` and monitored its RSpec and RuboCop workflows
- dry-ran the remaining 25 draft creations and confirmed that each CVE was
  absent remotely immediately before the write batch
- created all 26 unpublished drafts sequentially, read each one back, and
  committed its `submission.yml` baseline before the next remote write
- ran readiness checks for all 26 drafts from the unchanged 20:02 UTC evidence
  snapshot; no Node evidence was recollected
- retried the baseline push inside the Nix environment after the ambient
  pre-push hook rejected its missing pinned Ruby gems
- pushed baseline head `ac41c2b` and started monitoring its GitHub Actions

## Results

- Verified active session slug:
  `2026-08-22-security-advisories-6-12-95-6`.
- Located vpsAdminOS patch-v6 commits `d9bd139cd` (implementation) and
  `97a8c8fc6` (canonical coverage documentation).
- The latest security-advisories baseline is `9f21948`; the remote repository
  currently advances through its long-lived automation branch rather than an
  `origin/master` ref.
- Patch v6 contains 63 selected security fixes, 46 with CVE assignments. The
  preceding patch-v5 documentation contained 20 assigned CVEs, all of which
  already have tracked dossiers. The v6 update therefore adds 26 advisory
  candidates: two fixes first carried by v6 and 24 CVEs assigned
  retrospectively to fixes already carried by v1 through v5.
- First carried by v6: `CVE-2026-64017`, `CVE-2026-74582`.
- Retrospective, first carried by v5: `CVE-2026-74469`, `CVE-2026-74480`,
  `CVE-2026-74516`, `CVE-2026-74565`, `CVE-2026-74569`.
- Retrospective, first carried by v3: `CVE-2026-68093`, `CVE-2026-68154`,
  `CVE-2026-68160`.
- Retrospective, first carried by v2: `CVE-2026-68156`, `CVE-2026-68158`,
  `CVE-2026-68162`, `CVE-2026-68338`, `CVE-2026-68398`, `CVE-2026-72137`.
- Retrospective, first carried by v1: `CVE-2026-68476`, `CVE-2026-72252`,
  `CVE-2026-72255`, `CVE-2026-72317`, `CVE-2026-72322`, `CVE-2026-72323`,
  `CVE-2026-72389`, `CVE-2026-72434`, `CVE-2026-72451`, `CVE-2026-72472`.
- All 26 are still published in the current official Linux vulnerability data,
  have an upstream 6.12 stable fix, match the documented vpsFree.cz backport
  subject, and are absent from both the local dossiers and the production
  vpsAdmin advisory index. The post-snapshot change to `CVE-2026-74582` only
  stripped email transport/signature headers; its CVE substance is unchanged.
- Fourteen additional security fixes first carried by v6 do not yet have a
  published CVE assignment and cannot be represented as CVE advisories now.
- The fresh evidence snapshot has Node-set digest
  `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`
  and evidence digest
  `41b2807f18e711cadfbbe643bc1a8968c5cf8726549a8d895077173b71f52c72`.
  All 12 compute nodes report active `livepatch_6` version 6 on boot kernel
  6.12.95 and clean vpsAdminOS revision `97a8c8fc6`.
- Every new evaluation is complete: 12 compute nodes are `mitigated` and
  storage node 161 is `not_affected` because it does not host the VPS
  interface assessed by these dossiers.
- Exact transition history restarts the continuous mitigation interval at v5
  or v6 for the retrospective CVEs because replacement rollouts contain a
  recorded interval without an accepted active patch. Durable response text
  still names the first live-patch release that carried each fix.
- The current configuration digest is
  `b996b11eacbebe6f739dee82eda4fb2fa608351501fabf98770729ff29d2443f`;
  every requested subsystem option is present. SCTP's `auth_enable` control
  is per-network-namespace and its host value is not a trigger-blocking
  condition, so it is not used as a required host sysctl.
- The full RSpec suite passed with 152 examples and zero failures in 4 minutes
  20.5 seconds. RuboCop inspected 29 files with no offenses. The focused
  dossier suite passed seven examples with zero failures after the lint fix.
- The committed dossier series spans `ab80c0b` through `94b7f1c`; shared
  regression coverage is committed as `57b68da`, which is the current branch
  head of the original series.
- Mandatory review found that four Ceph dossiers incorrectly treated AppArmor
  as an active mount restriction, five dossiers omitted CNA-listed EOL stable
  introductions, and the SCTP diagnostic dossier required the unrelated
  `CONFIG_NETLINK_DIAG` option. It also advised replacing AppArmor rationale in
  two reachable NFS assessments.
- Commit `79508a6` corrects all review findings. CephFS is now assessed as
  reachable to VPS root through user-namespace mounts; the public impact text
  records the supported disclosure or shared-kernel availability outcomes
  without claiming an unsupported node escape. Commit `6da3874` records the
  complete refreshed evaluation set.
- Refreshed evidence was collected at 2026-08-22 20:02:16 UTC. The Node set is
  unchanged, `CONFIG_INET_SCTP_DIAG=m` is reported, and the evidence digest is
  `d42987be19062f80312e80f6b9f1bb4d33433d95f7860cb2cac87339e586ef13`.
  Every evaluation remains complete with 12 mitigated compute nodes and one
  role-excluded storage node.
- Post-correction validation passed for all ten affected dossiers, RuboCop
  inspected 29 files with no offenses, and the focused dossier suite passed
  seven examples with zero failures.
- The mandatory follow-up review resolved all Blocking and Important findings,
  with only two Advisory-level omissions in the internal stable-boundary prose.
  Commit `a850e72` names those missing ranges and refreshes the bound
  evaluations.
- Commit `0f40b46` remediates evidence reuse. Schema-8 documents stay fully
  compatible: Node receipt and history timestamps must be no more than 15
  minutes old at `collected_at`, but the coherent document no longer expires
  during later review or synchronization. Recollection is explicit after a
  deployment or suspected state change.
- Evaluator and reconciler regression tests passed 92 examples with zero
  failures. The dossier suite passed seven examples with zero failures after
  CVE-2026-64017 and CVE-2026-74582 were reevaluated at 20:19 UTC from the
  20:02 UTC snapshot; both are again fully resolved at 12 mitigated and one
  not affected.
- The final independent review passed with no Blocking, Important, or Advisory
  findings. The reviewer independently ran the combined evaluator, reconciler,
  and dossier suites: 99 examples, zero failures. The recorded residual risk is
  intentional: a reused snapshot cannot discover a later deployment, so
  operators must recollect after an actual or suspected Node-state change.
- Final local verification passed: 154 RSpec examples with zero failures in
  5 minutes 25 seconds, followed by RuboCop on 29 files with no offenses.
- Remote HEAD remains `9f21948`, the initiative baseline, so no rebase is
  required before pushing the feature branch.
- Feature branch `2026-08-22-security-advisories-6-12-95-6` is pushed at
  `a850e72`. GitHub Actions RSpec run `32596905740` and RuboCop run
  `32596905733` both passed on that exact head.
- vpsAdmin draft IDs are sequential and all have content revision 13:
  `CVE-2026-64017` 31, `CVE-2026-74582` 32, `CVE-2026-74469` 33,
  `CVE-2026-74480` 34, `CVE-2026-74516` 35, `CVE-2026-74565` 36,
  `CVE-2026-74569` 37, `CVE-2026-68093` 38, `CVE-2026-68154` 39,
  `CVE-2026-68160` 40, `CVE-2026-68156` 41, `CVE-2026-68158` 42,
  `CVE-2026-68162` 43, `CVE-2026-68338` 44, `CVE-2026-68398` 45,
  `CVE-2026-72137` 46, `CVE-2026-68476` 47, `CVE-2026-72252` 48,
  `CVE-2026-72255` 49, `CVE-2026-72317` 50, `CVE-2026-72322` 51,
  `CVE-2026-72323` 52, `CVE-2026-72389` 53, `CVE-2026-72434` 54,
  `CVE-2026-72451` 55, and `CVE-2026-72472` 56.
- Every readiness check returned `ready: true`, the exact matching remote
  revision, and a complete 13/13 Node status set (12 mitigated compute Nodes
  and one role-excluded storage Node). No advisory was published and no email
  was sent.
- Submission baseline commits span `bdb87be` through `ac41c2b`. The feature
  branch is pushed at final baseline head `ac41c2b`. Final RSpec run
  `32597421156` and RuboCop run `32597421131` both passed on that exact head.

## Open questions

- None. Publication and email remain outside this approved draft-only task.

## Cleanup

- Removed the initiative's temporary commit-message files.
- Retained the feature worktree and branch for review. No worktree or branch
  refs were removed.
