---
lifecycle: active
---

# Aitherdev disk retention

Phase: live collection verification, then authorized integration and release. The original
implementation, independent review, package checks, CI and aitherdev build pass;
manual cleanup is applied. Refreshed patches and pins pass focused quick checks.
The preceding owners have released the machine. The old system job stopped as
needs_refresh before activation (catalog changed). Final review/build/preparation
now bind the settled predecessor. Automatic retention is not activated yet.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-15-aitherdev-disk-retention/)

## Phase checklist

- [x] Investigate disk usage and agree policies.
- [x] Commit initial tracking and register isolated worktrees.
- [x] Implement seven-day host retention and coordination payload collection.
- [x] Commit, publish and independently review the original complete histories.
- [x] Pass original package checks, CI, deployment contract and aitherdev build.
- [x] Remove confirmed inactive temporary tests and old profile generations.
- [x] Rebase retention patches onto the first preceding rollout; regenerate pins.
- [x] Pass independent final composition/history review on the settled predecessor.
- [x] Pass final package/build checks and current-head CI.
- [x] Refresh native preparation and original jobs.
- [x] Complete native system/profile activation.
- [ ] Preview/apply live coordination GC, unmask automatic collection and verify.
- [ ] Integrate the exact final feature heads, then verify and release reservation.

User authorization: “Implement the plan” and “you can deploy aitherdev using
vpsfree-cz-configuration on your own”. This covers system switch and matching
application profile activation without reboot. The later instruction “when you'll
get the reservation, you have deploy and merge approval, then release it”
authorizes deployment, integration of this initiative's `dev-workspace`,
`vpsfree-cz-configuration` and workspace feature branches into their respective
`master` targets once our reservation is granted, followed by ordinary verified
reservation release. Preserve this ordering and the review/verification gates.
Archive, deletion and reboot remain outside the authorization; retain branches.

## Sources and verification

Native original comparisons are captured against reviewed bases 832d9f1a,
130c2248 and 72511fb2. New final comparisons are required after the refresh settles.

All feature worktrees are below
`worktrees/2026-10-15-aitherdev-disk-retention/`, on branch
`2026-10-15-aitherdev-disk-retention`:

| Repository | Published refresh candidate |
| --- | --- |
| dev-workspace | 2370232fd64dc35ce59409f82ad8704c8daa9f61 |
| vpsfree-cz-configuration | 177fb8ab50523323746903e0d5b72a2b0abe5106 |
| workspace | 5d77c1847e9fa54eb23622c59549ff83cab91d72 |

Settled candidates use bases 4e7ff517, 206f3025 and 60fd9da5 (settled-heads.json).
Native final comparisons are captured. Same independent reviewer accepted the
final composition/history under review-settled-packet.md (report review-settled.md)
with no new Blocking or Important findings across all four lanes. No new design
or source behavior was introduced. Runtime and host-policy
rebases are clean and patch-equivalent; the workspace policy is cleanly rebased.
Superseded pins were dropped and regenerated through the confctl channel and
the nested runtime input, preserving one update per consumer. Other inputs and
the extension remain unchanged. Range diffs, complete series and diffs are
saved in `*-refresh-range-diff.txt` and `*-refreshed{.diff,-series.txt}`.
Original reviewed refs remain under `refs/retained/.../original-reviewed`.
Focused refreshed checks pass: GC 16 tests / 64 assertions, host cleanup 12 tests,
diff checks and deployment contract. Configuration hooks pass. Runtime CI
38804083462 passes at intermediate 94b414e9 (runtime-ci-refresh.json). Final
runtime CI 38809866768 passes at 2370232f. Fresh Luna/low utility
/root/settled_verification ran verify-settled-retention.sh once: all four checks
and aggregate exit 0, no local kernel build. Evidence: *-settled.{log,status},
runtime-ci-settled.json and immutable verification-settled.json. Do not edit
review-settled.md or verification-settled.json once prepared; their hashes are sealed.

Fresh profile snapshot sha256:78468ab62662272ca936d499bc5f8532fea8fb6c9573652015f797eda5bff921
is approved/refreshed into the original dependency job. Candidate application is
/nix/store/7gr1y56cc22yk6ciy01l4gwk21kpvxs2-dev-workspace-0.2.0.
Machine preparation initially failed before snapshot publication because its
retained checkout lacked local Overcommit gems. Its pinned Nix environment
installed those dependencies and ordinary checkout hooks passed; no bypass.
Exact preparation retry passed. Artifact/source/coverage, current catalog adapter,
system/environment outputs and evidence hashes were inspected successfully.
Machine snapshot sha256:3a63e4b98225d96a63a1d8e848a999a77fc585a0051c2f16ac94c9c1681e5206
was approved by 71364c76-557d-49d2-a833-50c97436b894 and refreshed into the original
system job at revision 6. Target system:
/nix/store/sxzpx5xhzhxavyn0cwrnmzkfbim1hc8c-nixos-system-aitherdev-26.05.20261013.a033e66.
Fresh /root/activation_watch owns observation of both original jobs.
The observer completed at ledger 886: both jobs succeeded. System attempt
93ffb108-7a1e-4012-97f1-4b9285f21ad0 applied the target system; profile verified
7gr1y56c with token 567f10f39685496772e39435ec60fe55c073a284f90bb8399b102666f5870ca3.
Reservation is deployed_review. Post-activation host checks pass: managed launcher
resolves to its packaged helper, old launcher backup retained, both timers active,
no failed system/user units; portal/router/Codex/tmux/coordinator running.
See post-activation-host.json and activation-status.json. Installed live collector
preview is running while our temporary service mask remains in place.

Original runtime and workspace package checks pass, including aggregate Ruby checks and
workspace deployment contract. Runtime CI 38771321630 passes at the exact final
runtime revision. GC suite: 16 tests / 64 assertions; host retention: 12 tests;
existing stale-merge/refresh-history regressions: 2 tests / 14 assertions.
Configuration Overcommit hooks pass. The original configuration build succeeds:
generation `2026-10-15--18-57-43`, toplevel
`/nix/store/6z6ik6w9dl0jq0ci5xlq8yzn82zgvx0k-nixos-system-aitherdev-26.05.20261013.a033e66`.
No local kernel compilation occurred.

[Independent review](review.md), [original packet](review-packet.md) and
[committed remediation packet](review-remediation.md) preserve review provenance.
Reviewer `/root/retention_review`, catalog fallback GPT-6 Astra/xhigh, covered
all four lanes at high risk. Required fixes resolved: expiry belongs at admission,
live jobs remain executable/refreshable; integration driver locks/dependencies
exclude collection; expected_success is recognized. Whole histories are
consolidated, with one final pin per consumer and no obsolete history or migrations.
Configuration was independently reviewed at 985d08f4; its only subsequent source
delta is the directly verified test fixture’s `dir='/tmp'`, folded into the owning
commit. Production code and pins are unchanged. This narrow correction follows
review workflow step 9.

First long batch failures remain recorded honestly: the Python fixture followed
Nix TMPDIR=/build, and confctl received EOF at its build confirmation. The fixture
correction and `confctl build --yes` pass at the final revision. See
`{host-retention-final,aitherdev-build-final}.{log,status}`; earlier logs/status
remain preserved. A fresh Luna/low watcher owned the initial batch and CI. Its
interface was unavailable for a new watcher afterward, so the documented visible
parent fallback monitored the final build.

## Applied cleanup and limits

Removed `/tmp/ndns.27h2r2lc` and `/tmp/ndns.e87t01sh` after exact source, terminal
result, seven-day inactivity, hold and root /proc-reference checks. Measured
allocation removed: 30,927,568,896 bytes (28.8 GiB). Evidence:
[cleanup-retired-tmp-result.json](cleanup-retired-tmp-result.json).
The reviewed host helper then removed eleven more recognized inactive test trees
and their root registrations, and pruned nineteen old profile generations without
error. See `host-cleanup-{preview,apply}.log`. Available bytes observed afterward:
139,235,176,448 (about 130 GiB). Concurrent builds and background pressure GC mean
the net disk change cannot all be attributed to this initiative. Explicit store
GC can follow live coordination-root retirement.

The ad hoc KB tree came from archived network-counter verification campaigns,
not the normal KB tool’s default storage. Public native stop exited all g7-B
runner/child tuples, verified through the SDK; g4/g5/g7-A tuples were already gone.
Final socket cleanup refused: “unrecognized retained socket contents; no handoff
deletion”. No further native mutation or KB data deletion followed. Preserve the
private tree for manual retirement as discussed. Evidence: kb-observation.jsonl,
kb-after-stop.jsonl, kb-stop-b.{stdout,stderr,status}. No KB repository code change.

Active confctl rewrite temporary directories remain with their owning initiative.
Old .osvm-qemu disks and other sessions’ development clusters remain untouched.
Accepted collector residuals are documented: integration scratch directories and
owner-keyed notification roots remain retained after completion.

Initial inventory was old VM disks 245.7 GiB, Nix store 222 GiB, /tmp 113.1 GiB,
private KB campaigns 64.5 GiB and coordination sources 34.9 GiB. Setup observed
42 GiB free at 96% usage. Those figures are the initial baseline, not current sizes.

## Native deployment and next action

[Rollout record](rollout.md) contains exact requests, source/approval/snapshot
identities and the post-selection sequence. At native ledger revision 867:

- System job `3fb4d0ab-dd92-449c-9809-08fa102addf4`: needs_refresh, revision 6,
  attempt f46c4bf0-9e4f-4956-b9a5-6aa2eabb2058, baseline_changed before activation.
- Profile job `8d7fc8aa-0bcf-48c2-a5e6-13b08ba9548b`: waiting_dependency.
- Our reservation `c5f45df7-fb17-4aff-b6ef-7d1b277c28f3`: held, revision 2.
- Both preceding reservations are released; no foreign holder remains.

The resumed external conversation verified the same identity. The first fresh
catalog-selected Luna/low queue watcher completed at 20:36:35 UTC after observing
the holder change (system job revision 3; still waiting_resource). Its
[queue observations](deployment-queue-watch.jsonl) are registered in the portal.
A second fresh Luna/low utility completed at revision 801 with no target-state
change; only the global ledger revision advanced. The next observer uses
`watch-deployment-queue.py`, which ignores unrelated global revision changes.
Merge
approval is now recorded above; the optional pause question is superseded by
the user's direction to deploy, merge and release when our reservation is granted.
The latest filesystem observation was 143 GiB available (85% used); concurrent
background work still prevents attributing that net figure solely to cleanup.

The fresh final watcher observed our grant at 21:25:46 UTC and exited normally.
Continue final review/checks and refresh both original jobs with new snapshots.
If a snapshot needs refresh, use normal preparation and applicable verification;
never replay an uncertain activation. After successful profile selection, run the
installed collector’s dry-run, inspect actions/references, apply it, then remove
this rollout’s temporary runtime mask with
`systemctl --user unmask --runtime workspace-coordination-gc.service`.
The mask was created only after proving no previous override existed. It prevents
an automatic first sweep before live preview. Verify automatic collection, both
system timers, the managed ~/bin launcher/backup, system/profile identities and
service health. Keep the machine reservation during review; completion/integration
requires separate user direction and exact final-head proofs.

**Frozen evidence:** do not edit review.md or pre-deployment-verification.json;
their hashes are sealed into both submitted snapshots. State/rollout updates are safe.
The original candidate application (not yet activated) is
`/nix/store/1dgfq5qa9n8ii2aap8ija6shyzsgx63a-dev-workspace-0.2.0`.

## Ownership and tracking

The initiating external conversation owns implementation and administration.
Managed root `01a14062-599d-7f13-9cdf-5bbf6fbd4ae2` was initialized only for native
ownership; coordinator status events do not assign it duplicate work. No team
roster exists. Initial --no-codex shell closure exposed an empty-thread recovery
error, then normal start completed with valid provenance. The retained
configuration checkout’s missing local hook gems were fixed through its pinned
nix develop and ordinary checkout; hooks were never bypassed.

Initial tracking commits 7cf496e1 and genuine ownership-handoff checkpoint
72511fb2 are pushed on shared master. Current phase/evidence updates stay in the
working tree under the normal cadence. Preserve extensive unrelated shared files
and index changes. The application remains a user-profile deployment; configuration
selects its matching host contract and the managed cleanup helper.

## Live collection and integration checkpoint

Installed preview and apply both pass with retry=false. Removed 85 retired
worktrees and 701 roots; all payload paths are gone. Measured allocation removed:
42,259,800,064 bytes (39.4 GiB). Evidence: coordination-gc-{preview,apply}.json,
preview-inspection.json and apply-summary.json. Live/unknown references preserved.
Our exact runtime mask is removed; collection is a scheduler-created transient
unit, so an immediate systemctl start correctly found no persistent unit.
Automatic dispatch remains to be verified. Local sudo needs a TTY/password;
normal locked system cleanup is being started through authorized root SSH.
Native merge-only driver d818507e-4525-46ef-a5ca-81e9d70cf3b6 is preparing.

## Certified workspace refresh and live cleanup

Another initiative's tracking-only master commit 77bfc407 arrived after the final
lead pre-merge check. The pin-only recipe correctly refused its candidate because
it omitted our reviewed cleanup-policy file. Restored that unchanged policy and
the one generated pin in the exact journal-owned scratch checkout, retaining the
rejected candidate ref. Installed semantic verifier passes and Git merge-tree
reconstruction exactly matches the original reviewed change over incoming
tracking-only content. No product code/recipe changed. Certified-equivalence
retains original independent review. Final workspace candidate ac19d7ce25bf9a507eb20b944c2d213224193eb8;
runtime and configuration unchanged. Evidence: workspace-recovered-* and
workspace-refresh-verifier.json. Native driver resumed and submitted all three
merges; ordinary collector-lock contention returned exit75 once, then --no-wait
resume passed without replay. Native operation records own the exact results.

Root system cleanup/GC service completed success, exit0 at 23:58:46 local time;
102 additional root registrations removed, no further profile generations.
Automatic coordination collection dispatched successfully after mask removal
(journal 23:54:22), deferring safely while integration was preparing. Latest df
observation: about 163 GiB available. Keep evidence separate from net allocation
attribution because background work/GC continues.

## Integration d818507e-4525-46ef-a5ca-81e9d70cf3b6

Requested exact feature heads are integrated. See integration/d818507e-4525-46ef-a5ca-81e9d70cf3b6/summary.md
and integration/d818507e-4525-46ef-a5ca-81e9d70cf3b6/result.json for operation receipts. Feature refs and session retained.
