---
lifecycle: complete
---

# Cluster status metadata fix

Phase: complete. Deployment, live acceptance and integration passed. The user
explicitly said "no need to wait for CI", so the remaining CI wait is waived. The storage cluster card reports running, ready and ten services
without a decode error. Runner/disks and all recorded cluster state hashes are
unchanged. All three exact final feature heads are merged into remote master.

## Phase checklist

- [x] Investigate helper status and agree existing-card scope.
- [x] Implement and document compatible strict metadata decoding.
- [x] Commit, pass focused checks and independent whole-branch review.
- [x] Pass full runtime/composed Nix checks and build aitherdev.
- [x] Recover the explicitly selected interrupted archives.
- [x] Deploy aitherdev, activate the user profile and verify the live card.
- [x] Merge all three exact final feature heads and remove integration targets.
- [x] Final CI wait waived by the user; preserve the running workflow and evidence.

## Final repositories and authorization

| Repository | Retained branch | Exact merged head |
| --- | --- | --- |
| aither64/dev-workspace | 2026-10-06-cluster-status-metadata | e3315a483f3d3536d492ecbe40f2655449cf630f |
| aither64/vpsfree-cz-workspace | 2026-10-06-cluster-status-metadata | 57bd3304b7901d2c942f5f50ecd8897b53bde1ef |
| vpsfreecz/vpsfree-cz-configuration | 2026-10-06-cluster-status-metadata | 6f6aff9029cd57e1a0f9201356f7fdc9f6480671 |

User: "you can deploy aitherdev using vpsfree-cz-configuration and merge the fix
into the default branches when it is verified." The accepted plan names these
three master targets. No separate integration approval remains.
Workspace and configuration final rebases preserve the reviewed pin patches;
range-diffs report equality. The configuration base additionally includes the
separately released WebUI pin and deployment record. Both composed runtime pins
still select e3315a4; the extension and unrelated inputs were preserved.
Fresh SSH fetches prove local/remote feature heads equal the recorded heads and
all are ancestors of origin/master; see integration-proof.json.

Worktrees remain under worktrees/2026-10-06-cluster-status-metadata/{dev-workspace,
workspace,vpsfree-cz-configuration}. Canonical project clones remain under repos/.
The two owned detached integration targets were removed with normal non-force
worktree removal after their pushes. Feature and auxiliary CI refs are retained.
Shared master stayed on master, with unrelated files/index changes preserved.
This initiative was created separately with --as-is --no-codex --no-attach after
current reported no session and no trusted/environment binding. Subsequent
commands set both verified identity variables; no roster was invented.

## Implementation, review and verification

Runtime changes are one coherent commit, three files, 195 additions/5 deletions.
The private helper response accepts validated optional webuiSource and maintenance
metadata, retaining strict unknown-field and envelope checks. Public Status and
the existing card contract are unchanged. Legacy responses remain accepted;
malformed metadata and contradictory maintenance readiness fail closed. No
persistent state changes or migrations. Owning explanation:
dev-workspace/docs/workspace-portal.md. Deployment history remains in rollout.md.

Standalone independent reviewer used the installed default review-purpose role,
gpt-6.1-sol/xhigh/read_only, catalog digest
3343a06cbc8d3c181df52770086fb807894f9990132bb0792048e0ddabb764f8.
All four review lanes passed with no findings; complete branch history has no
obsolete paths and explicitly no migrations. The same reviewer checked both
mechanical companion pin histories/composition. See review-result.md,
review-packet.md and composition-inventory.md. Patch-equivalent final rebases
retain that review and integration authorization. Configuration hooks ran in its
Nix environment without bypass, and the generated confctl message was retained.

Focused cluster/web checks passed. Full runtime and composed nix flake check
operations passed, including local host smoke; the composed package build and
both aitherdev builds passed. Original runtime local log contains only completion
summary, not full streamed output; composed-checks.log is complete. Final build
6f6aff90 passed in98 seconds, generation2026-10-06--22-23-52.
Deployment-contract checks passed on final locks. All long operations used fresh
catalog-policy Luna/low utility watchers, never development team members.

CI37514351752 passed fast checks on exact e3315a4. Initial CI37510298035 and
master CI37526123525 failed the same unchanged archive-status test; the master
host VM smoke job passed. Full failed logs were inspected. Isolated repetition
failed7/100 on feature and20/100 on installed baseline4c3ea2e; all affected web
sources are identical. The test races background display reconciliation/CAS;
execution independently rechecks journal identity after acquiring its mutation
lock. This existing race is outside the decoder patch, and a green repeat does
not fix it. See ci-investigation.md and the linked reusable workspace note.
Actions API rerun was refused by read-only token permissions. SSH-published
auxiliary refs at unchanged e3315a4 trigger normal CI without source/empty commits.
Final exact-head repeat37526974373 was running at last observation. The user
waived waiting; instructed its watcher to stop only its local observation and
leave the remote workflow running. The observer confirmed its local watch exited
130 after Ctrl+C, with no remaining local process and no remote cancellation.
Last captured fast job was still running; final CI conclusion is unknown.
final-ci-repeat.log and .exit preserve that observation, not a test failure.
No superseded same-branch CI remains; workspace/configuration have no applicable
feature workflow. The default-only host job already passed on the same SHA.

## Deployment, recovery and live acceptance

Final system: /nix/store/r3c1kcrjmqgq48vjsvkmz3nwkzj6hggy-nixos-system-aitherdev-26.05.20261006.b253099.
Application: /nix/store/b2q12p1725bqrb4nrd6yfjg28hgsggcf-dev-workspace-0.2.0.
The final rebased system differs from initial4q2w8x1h only in the confctl
configuration-info.json link. Normal dry-activate-first/switch deployed it,
exit0, about118 seconds; both system/firewall health checks passed. Invocation
f4a69b858eb44a3498462bd7a0e40a2b has no remaining process. Application profile
switch invocation133a32c410be4034a5ac307bcf996cfb passed in102 seconds. Portal
workspace-portal@vpsfree-cz.service is active. Repeated verify-live.py passed
following final system activation. Safe evidence: live-verification.json,
cluster-before.json and cluster-after.json. Full rollout is recorded separately.

The user explicitly approved resuming the original Sep18 and Oct2 archive
operations; Oct2 was already completed by its owner. Sep18 recovery needed
temporary non-force removal of two clean fix-owned worktrees whose Git admin
names reused old sealed names; restored exact refs afterward. The user then
said "contineu" after the handoff selecting three additional interrupted archives
(portal-creation-performance, session-modes-review-timing, upload-display-limits).
Those ordinary retries refused state.md0600 against sealed0644 projection.
Independent byte/path/mode hashing proved exact target equality with only the
projected mode correction. Restored only those three state modes and resumed the
normal installed executors under child umask022; all three exited0 and cleared
lifecycle blockers. Receipts/ownership proofs were preserved. Reusable notes:
notes/dev-workspace/2026-10-06-archive-git-admin-name-reuse.md and
notes/dev-workspace/2026-10-06-archive-child-umask.md.

The first profile attempt correctly refused the storage lead's in-progress turn,
leaving the old profile selected. A ten-minute read-only idle wait never passed.
Asked whether to wait or interrupt; the user's next "continue" was read as
approval to interrupt only that exact still-active turn, and this interpretation
was stated before acting. Normal portal interrupt returned ok and require-idle
then passed. The supported switch completed. No conversation was retired or
resumed automatically, and no cluster/guest was reset. Warnings for unproven
worktrees in other sessions were left to their owners.

## Handoff and remaining action

No required implementation, deployment, integration, approval or CI wait remains.
Leave this initiative open for follow-up; completion does not authorize its
archive/delete/stop. The remote CI workflow continues under the user's no-wait
direction. The existing archive-test race remains documented outside this fix. The existing consolidated daily tracking checkpoint236a9deb
is retained; current records stay updated without a second same-day checkpoint.
Stable URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-06-cluster-status-metadata/
