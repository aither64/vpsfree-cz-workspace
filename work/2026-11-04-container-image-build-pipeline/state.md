---
lifecycle: active
---

# Container image build pipeline

## Current status

Planning is complete, 2026-11-05. Lead accepted the final architect-owned
[technical brief](design.md) at ~17:48 UTC, and [plan.md](plan.md) is the
consolidated scope/delivery/acceptance summary. Product and architecture decisions
are settled; only explicit bounded site preflights and implementation remain. No application changes, feature branches,
worktrees, running services, production access, builds or tests were performed.
No implementation, integration, deployment or session lifecycle action is implied
by "finish the plan". Session remains open.

## Phase checklist

- [x] Verify exact session identity and retained roster/settings.
- [x] Investigate build, test, publication, clients, GC and failure boundaries.
- [x] Resolve initial parallelism, builder reuse/reset and partial-success policy.
- [x] Resolve complete CI view for unchanged plus rebuilt distributions.
- [x] Select central Go public/run service, immutable files and local SQLite.
- [x] Preserve default-push, weekly and manual rebuild modes and existing public GC.
- [x] Select public aggregate dashboard and private structured access log.
- [x] Define future repository/mirror boundaries and acknowledge initial SPOF.
- [x] Accept final technical contracts and consolidate plan/state.
- [x] Finish final link/whitespace checks and consolidated tracking checkpoint.
- Implementation, quick checks, independent final change review, long verification,
  integration and deployment have not started.

## Settled decisions and explicit scope boundaries

The final plan/design describe current intent; older investigation files retain
source facts and may contain superseded recommendations. Earlier all-or-nothing
publication, serial-only first delivery, runner-host authoritative staging, per-test
changed-tuple routing, filesystem full-copy/OverlayFS/hardlink views and private
dashboard proposals are superseded. Do not implement them from historical notes.

- Existing self-hosted runners selected by user on 2026-11-04.
- Run-lived parallel worker VMs amortize startup/builders; useful overlapping work
  required initially. User reports last run 04:00–22:00 (18h), no measured speedup.
- Successful images publish independently of failed images or unrelated full CI.
  Exact current public GC policy remains; failure itself never requests deletion.
- Existing images VPS has no snapshot/clone controls (user fact). Service uses
  ordinary immutable files and SQLite metadata refs; no copies/links/mount views.
- Full CI uses one sealed baseline-plus-candidates URL. Required changed results
  need same-run verified receipts; baseline or stale cache cannot mask failure.
- Default-push changed/affected, weekly full, manual all/selected share one path.
- Go service proposed in vpsadminos/osctl-repo-server, org configuration deploys
  existing images VPS and HTTPS proxy; vpsfree config retires legacy writer.
- One public aggregate dashboard. IP/UA only private versioned JSONL access log,
  normal operator access, no private UI/new account system.
- Initial instance and current proxy remain SPOFs. Stable IDs/local reader and
  portable public export/import prepare future mirrors; no multi-host rollout,
  mirror daemon, consensus/multiwriter or global statistics in initial delivery.

## Package and investigation timeline

All source investigation packets below were delivered, read and accepted by lead.
Times are known report/acceptance bounds, not invented exact execution durations;
overlapping member work is not summed. Previous execution was complete/capacity
confirmed before later packages. All retained members kept saved model/effort and
workspace-write access. Architect0 owns design; lead owns plan/state; evidence
owners edited only assigned files. No application implementation was dispatched.
Future execution ownership/dependencies/acceptance are in design.md.

| Package / evidence | Owner | Acceptance / meaningful transition |
| --- | --- | --- |
| [I0 build/test/disposal](investigation-vpsadminos.md) | implementer0 | Accepted 2026-11-04 before 22:03 UTC |
| [I1 current builder](investigation-builder.md) | implementer1 | Accepted 2026-11-04 before 22:03 UTC |
| [I2 public hosting/clients](investigation-publication.md) | implementer2 | Accepted 2026-11-04 before 22:03 UTC; obsolete master inspection corrected to staging |
| [I3 hosted runners](investigation-hosted-runners.md) | implementer3 | Accepted 2026-11-04 ~21:59 UTC; official capacity/trust evidence |
| [I4 batching/collisions](investigation-batching-concurrency.md) | implementer0 | Accepted 2026-11-05; per-process IP allocation and reusable deterministic builders |
| [I5 parallel workers](investigation-parallel-workers.md) | implementer0 | Accepted 2026-11-05 before 08:52 UTC; global build/test barriers and worker VM seams |
| [I6 slow scheduling/GC](investigation-scheduling-gc.md) | implementer1 | Accepted 2026-11-05 before 08:52 UTC; Fedora/Gentoo mapping and exact policy |
| [I7 builder reset](investigation-builder-reset.md) | implementer0 | Accepted 2026-11-05 ~09:25 UTC; targeted delete ownership/cleanup limits |
| [I8 filesystem staging](investigation-staging-service.md) | implementer2 | Accepted 2026-11-05 before 11:53 UTC; native in-place writes; storage proposal superseded |
| [I9 complete CI view](investigation-complete-ci-view.md) | implementer0 | Accepted 2026-11-05 before 11:53 UTC; common repository readiness and expected-result gate |
| [I10 Go HTTP contract](investigation-http-service-contract.md) | implementer0 | Accepted 2026-11-05 before 14:22 UTC; native v1 and pinned fallback |
| [I11 service storage](investigation-service-storage.md) | implementer2 | Accepted 2026-11-05 before 14:22 UTC; immutable refs, public GC and legacy adoption |
| [I12 dashboard/proxy](investigation-download-stats.md) | implementer1 | Accepted 2026-11-05 before 14:22 UTC; trusted requester chain and measurement limits |
| [I13 mirrors](investigation-mirror-boundaries.md) | implementer0 | Accepted 2026-11-05 before 16:03 UTC; client failover limits and portable snapshots |
| Final design.md | architect0 | Assigned before 2026-11-05 17:30:42 UTC; saved ~17:46, accepted by lead ~17:48 UTC |

Final consolidation exceeded its 5–7-minute dispatch milestone. Progress concern
`final-plan-delivery` identified settled choices awaiting persistence. Lead cut
optional specification and requested a minimal saved brief; design.md was saved
with state/receipt/file-order/publication contracts, package table and bounded
preflights, then accepted. No blocker or new source investigation justified the
extra interval. Remaining work was final checks/checkpoint, not further design.

Earlier design revisions accepted at ~08:22, 08:52, 09:25, 11:53, 12:05, 12:13,
14:22 and 16:03 UTC on 2026-11-05 reflect user corrections/additions, not app
rework. Only final plan/design are normative. No extra roster members created or
reconfigured. Cross-session communication was not used. Transient same-session
assignment lock refusals did not require work takeover; sufficient delivered
packets were used or identical messages retried after locks released.

## Repositories, exact evidence and freshness

Inspection used canonical bare repositories and explicit immutable source IDs:

| Repository | Inspected ref/head |
| --- | --- |
| vpsadminos | default staging `2951a632c4254a44747a8da326e3dde897eaa0e2` |
| vpsfree-cz-configuration | master `f4069909b55fbed907cb658f350ec6a59f97e05a` |
| vpsadminos-org-configuration | master `ca96c95a1fee04793468785d8323a759615b2b4e` |

Lead independently matched remote defaults with `git ls-remote --symref origin
HEAD` on 2026-11-04 ~21:57 UTC. These are investigation baselines, not claimed
current production or implementation heads. vpsadminos master `4658d40...` is
obsolete; current consumer conclusions were rechecked on staging. Build config
pins vpsadminos `dd188397abe37d0bc33f4c5dfb3605206ce5e326`; I1 verified relevant
builder module directories equivalent at inspected staging head. Implementation
must refresh baselines and inspect effects before edits.

No project branches/worktrees registered or new repository created. Portal
manifest retains repositories: [] and artifacts: []; regular tracking files are
listed automatically. No exact final feature head or migration exists yet.

## Checks performed in planning

- dev-session current plus both DEV_SESSION markers matched the trusted binding.
- Same-session live roster checked before substantive assignments; retained
  settings/access respected. Design and evidence packages were bounded.
- Read required workspace procedures and documentation/handoff skills, relevant
  repository AGENTS/docs; members report required own reads.
- Lead read all packets and checked key source boundaries: image export/disposal,
  public consumer use, builder reuse/IP allocator, wrapper buildRc/postRun,
  global --jobs stage barriers and native GC grouping/order.
- Final checks: all 17 Markdown records, 38 local links, no missing targets or
  whitespace errors. No builds,
  benchmarks, mounts, live logs, credentials or host mutations.
- No prior CI success, active host revision, resource fit, download identity/count,
  numerical speedup or actual failover is claimed.

Planning/investigation records alone do not trigger independent final change
review. Completed future app/config/docs changes will require committed intended
changes and quick checks, then independent final review before longer checks.

## Remaining preflight checks and next action

The final design is accepted; numerical operational limits and live facts remain
implementation preflight rather than product decisions. Refresh refs/instructions,
confirm runner trust/KVM/capacity, exact live catalog/writers/storage headroom,
SSH roles and effective proxy headers, normal test-pool/dependency coverage.
Each preflight/package in final design has an owner, evidence and stopping rule.
No optional expansion into HA, global analytics or filesystem mechanisms.

After plan acceptance, the next phase is implementation in owned feature worktrees
using the final package order and ordinary review/checks. User has requested only
planning here. Integration and deployment need their separate normal direction.

## Tracking and session retention

Initial tracking commit: `3d01ff72d` (2026-11-04). No hook framework declared by
workspace; no hook bypass. The user now explicitly requested finalizing the plan;
one consolidated end-of-day planning checkpoint preserves final plan/design/evidence.
Workspace remains on shared master; preserve all unrelated work/index changes and
use the short tracking lock, no repository merge claim for tracking-only records.

Session remains active/open. No archive, stop, delete, finalization helper or
background cleanup is authorized. No services/clusters/machines were acquired.
Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/
