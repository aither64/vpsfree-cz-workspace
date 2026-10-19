---
lifecycle: archived
---

# osctld autostart fix

## Current phase and latest direction

Post-reboot central-log verification complete for both staging nodes after
2026-10-18 22:10 CEST. Node1:47/47 autostarts successful, final22:16:45.
Node2:60/60 successful, final22:25:26. No newboot EMFILE/EOF or allocator/ENOMEM
failure in complete windows through22:28:48/22:29:16 respectively. Both OS2abbe3cc,
Linux6.12.113. Node1 initial swap EBUSY then later actual activation events;
node2 both devices activate successfully during boot. Central logs only, no
current /proc/swaps or CT state query. Existing histfile and Munin faults plus
one ct-top-missing batch per node remain separate from autostart; no new fixes
or remote mutation. Architect combined assessment accepted: [evening reboot summary](reboot-2210-summary.md),107/107 autostarts successful. Summary registered in portal; no further collection pending. Session remains open.

## User-reported staging deployment

User reports deploying the fix to staging successfully (follow-up conversation,
2026-10-18). Recorded as operator-reported success; this session did not perform
or independently inspect that deployment. Follow-up asks about file-descriptor
limits and scaling from 47 to 500 containers. Architect owns bounded source-only
explanation; no new test, node operation or swap work is authorized by this check.

## Phase checklist

- [x] Inspect both nodes after22:10 reboot; complete central logs, both owner reconciliations and architect combined assessment accepted (107/107).

- [x] Verify exact session binding and retained Full-team roster/access.
- [x] Diagnose reboot logs and agree osctld-only design/endpoint.
- [x] Implement child-preparation acknowledgement and deterministic regressions.
- [x] Add packaged-helper and parallel-autostart VM regression.
- [x] Quick checks, hook-enabled cohesive commit and negative baseline control.
- [x] Independent final review and narrow test-delta review.
- [x] Focused VM verification and feature-branch publication.
- [x] GitHub RSpec and RuboCop.
- [ ] Broader GitHub CI (queued; no final result).
- [x] Osctld default-branch integration (user explicitly authorized later).
- [x] Confirm colleague covers swap kernel bug; stop duplicate swap planning.
- [x] Staging deployment reported successful by user; not independently inspected.
- [ ] Larger-node capacity qualification (not performed).

## Repository and history

- Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-autostart-log-analysis/vpsadminos
- Branch: 2026-10-18-autostart-log-analysis
- Base / origin/staging: d531fc90888e3eabf17889b0dff94c648866cea4, fetched and unchanged before publication.
- Exact local/published head: 60f9ed1c153a734880e002b63d6ab7ed5fe87d0e.
- One logical commit: osctld: prepare child descriptors before applying process limits.
- Four paths,501 additions / 1 deletion: SwitchUser source/spec, focused VM and registration. No migrations, pins, package versions, public contracts, persisted formats, retry policy or configured-limit changes.
- Original unpublished review head21e4dfb was amended only for two test assertions. Production source/spec identical; actual helper SHA25696ca72b3ee79bbff5627b2939674987725923706ec64669720c2ad5bfc58389f. No obsolete history, fixup residue, repeated update streams or migration lineage.
- Portal comparison captured exact base/head. Remote feature ref retained; no PR. Later authorized coordinator integration is recorded below.
- Final tracked/index/untracked worktree clean. Owner removed only generated libosctl/tmp after no consumers; ignored native.so retained. Native VM runner reaped guest/virtiofs and removed its disk; evidence retained. No session lifecycle action.

## Owners and acceptance

| Owner | Result |
| --- | --- |
| architect0 | Accepted private-handshake design in design.md; excludes swap/history/kernel/retry redesign |
| implementer0 | Source/unit regression, source comments, native-env diagnosis, cohesive message/publication script and owned artifact cleanup complete |
| implementer1 | VM test, narrow runtime assertion corrections, package/limit/console acceptance and native-cleanup proof complete |
| reviewer0 | Independent read-only saved gpt-6.1-sol/xhigh final review plus affected test delta; no findings |
| lead | Identity, tracking, Git serialization/transport, checks monitoring, acceptance and handoff |

## Verification evidence

- Focused unit:30 examples / 0 failures seed 19302, unit-check-patched-ruby.log.
- Deterministic control: corrected example passes; exact d531fc9 baseline fails expected premature-limit stage, ordering-control.log. Shared source/index never overwritten.
- Final commit/amend Nixfmt and RuboCop hooks passed; no bypass. Message width warnings use stricter hook60/72 thresholds; repository80-column limit honored.
- Final-review.md retains original all 4 lane review, final-review-delta.md covers final60f9ed1c. Explicit clean-history/no-migration/no-update-stream conclusions. Final review precedes each long VM run.
- VM final exact head: osctld/switch-user-prlimits,3/3 examples passed,388.46 s. Logs vm-retry.log and vm-final-run/*.log. Real package source identity/hash proved;1,200 inherited FDs at preparation NOFILE 8192/8192 -> unprivileged UID 65534 workload NOFILE 1024/8192 and7 open FDs. Two containers autostarted in parallel, real init limits confirmed, exec/console/clean stop passed. No unexpected EMFILE/EOF.
- Same cached6.12.113 kernel as baseline; no kernel compilation/config/pin change. Initial boot~4 min then services progressed normally, KVM/shm capacity confirmed; native deadline respected.
- First VM failed two test assertions, not observed product behavior: Nix source alias string mismatch and normal TTY-close EOF logs. Owner corrected with File.identical? plus exact expected-close exclusion, preserving hash and broad unexpected error checks. Quick checks/hooks and independent delta review passed before retry. First-run evidence retained vm-first-run.

## Exact-head GitHub checks

- RSpec39120729978:success (all component suites), https://github.com/vpsfreecz/vpsadminos/actions/runs/39120729978
- RuboCop39120729979:success, https://github.com/vpsfreecz/vpsadminos/actions/runs/39120729979
- CI39120729965:queued, https://github.com/vpsfreecz/vpsadminos/actions/runs/39120729965
- Broader CI is self-hosted full OS build/ci-tagged VM tests/livepatch matrix, distinct from planned focused local verification. No manual dispatch, rerun or cancellation. Exact status snapshot ci-final-status.json; check queued run before claiming it passed or final integration readiness.

## Environment and investigation provenance

- Reboot shutdown began10:15, new boot10:21.48 starts, 25 success markers, 23 EMFILE/EOF failures; original logs retained. Parent lowered container prlimits before child cleanup completed. Actual production FD occupancy/limits unmeasured (node SSH denied); no daemon FD leak claim.
- Initial workspace plan/state committed b014fbeb before project commits/publication. User paused/resumed twice; stopped exact owned operations and preserved files/index each time.
- Hook signature repaired using documented Nix shell, reviewed config, hooks enabled. Member shells lacked Nix daemon/network; lead transport ran owner-authored commands without taking source work. Watcher API unavailable on resumed runtime, monitoring skill fallback announced; parent owned runs.
- Interrupted named-shell bundle install was incomplete. Explicit install/check resolved it; native extension then required patched Ruby in DEFAULT root shell, as documented notes/vpsadminos/2026-07-25-local-osctld-native-ruby.md and 2026-08-22-osctld-rspec-nix-shell.md. Correct root component bundle/native rebuild passed. No application/native API workaround or shared-cache reset.

## Next action and scope boundaries

Osctld integration is complete under explicit user direction. Our swap work is stopped after confirming colleague coverage. Broader CI remains separately queued. Deployment requires a separate request. Prepared future rollout in design.md: record intended-running/stopped CTs and queue, use supported osctld update/restart, retry only selected intended-running stopped CTs, verify health/no EMFILE/EOF; avoid forced pool-wide autostart trigger. No kernel reboot required for this fix. Old binary rollback reads existing state but reintroduces race.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-18-autostart-log-analysis/

## New direction: merge osctld, then plan swap

User explicitly instructed: “ok, so please first merge the osctld fix. then create a plan to fix the swap bug.” Approval scope is vpsadminos feature2026-10-18-autostart-log-analysis -> remote default refs/heads/staging, exact reviewed/published60f9ed1c153a734880e002b63d6ab7ed5fe87d0e (or patch-equivalent rebase only under procedure). No deployment approval and no swap implementation approval. First merge, then substantive swap planning.

Selected package coordination guide read in full (selected-coordination-guide.md), including contract/operations. Catalog covers vpsadminos/staging. Merge-only operation uses queue with no machine reservation. Implementer0 owns premerge technical inventory/refs; lead owns user approval-bound queue admission and acceptance. BroaderCI stillqueued; focused/local checks plus GitHubRSpec/RuboCop and final independent review passed.

- Queued merge job0381853c-c5a8-4334-b7e9-828ee68d26b8, approvalf9ed43af-9641-4a6f-aaa4-87289d045f0f, exact snapshot82aff0d3; attempt9f718650-981e-462c-b294-e9bbb00ea851 claimed. No machine reservation (merge-only). Retained immutable review/verification evidence bound to snapshot; no direct Git bypass. Await success/remote proof before swap planning.

- Merge verified: coordinator succeeded/applied/verified, local and remote staging 60f9ed1c; feature retained and worktree clean. osctld-merge-summary.md preserves approval and receipts. No resource wait/uncertainty remains for this operation.
- Swap planning backlog: architect0 owns decision-complete swap-plan.md; implementer0 exact 6.12.113 patch-owner/lineage/version/pin strategy; implementer1 bounded service-failure and large-sparse-swap regression design. Source/commit/build/deploy changes not authorized. Stable 6.12.113 incident focus, no 6.18 upgrade/histfile, retain accounting and published history.

## Descriptor limit and container-count explanation

Source acceptance inspection: daemon.rb sets its NOFILE soft/hard to131072;
container default NOFILE soft is1024. The original failure was in a freshly
forked startup helper inheriting the daemon descriptor table: applying the CT
limit before cleanup could leave no free eligible descriptor for opening
/proc/self/fd. Container count and concurrent activity can increase inherited
FD occupancy, but no fixed containers-per-node threshold follows. Corrected
ordering cleans first, then applies configured limits; the1200-inherited-FD
regression validates that boundary. A500-container stress/capacity qualification
was not run. Actual daemon FD headroom is a separate per-process concern and
requires worker /proc/PID/limits and /proc/PID/fd measurements, preferably during
startup bursts. No daemon leak established, no limit increase proposed.

## Evening reboot verification evidence

2026-10-18 Amsterdam/CEST central-log windows start22:10. Node1 complete capture
through22:28:48; node2 through22:29:16. Logserver timezone verified. Independent
owners collected timestamp-bounded streams without line caps and excluded sshd
and container-kernel noise; no node operations or remote writes.

Node1 FINAL accepted: newboot22:14:08;47selected,47distinctattempts,
47successmarkers and47ct_on_start events; finalsuccess22:16:45. No postboot
EMFILE/EOF/executor/retry/allocator failures.47EOFs belong to preceding shutdown.
Swapon EBUSY at22:14:09, followed by service success claims; actual kernel swap
activation messages for sda22:18:46 andsdb22:19:04. These are activation events,
not a current /proc/swaps snapshot or proof of who activated them. No original
bitmap ENOMEM. Known excluded histfile/getent remains; recurring Munin plugin
errors and recovered startup warnings observed. OS2abbe3cc, Linux6.12.113; no full
kernel source SHA in logs. Evidence reboot-2210-node1-summary.log and host/runit.

Node2 FINAL accepted: boot22:23:02;60selected=60uniqueattempts=60uniqueRUNNING
setsidentical, no newbootSTOPPED. Parallel16, final22:25:26.757208. Zero original
EMFILE/EOF/executor and allocator/ENOMEM/OOM traces. Both swap devices activated
22:23:43, corroborated service success. Same OS/kernel prefix as node1. Startup
socket/network recovered. MuninIRQ/sensor errors persist from old boot; single
60-VPS ct-top-missing batch22:26:14 (all alreadyRUNNING) without repeat through
capture, subsequent sample recovery not proved. Histfilegetent persists/user
excluded.60oldshutdownTTYEOFs precede newboot. Evidence node2-analysis.log and
host/runit under reboot-2210 prefix. No source/build/node/recovery operations.
