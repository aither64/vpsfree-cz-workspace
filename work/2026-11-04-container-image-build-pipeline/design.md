# Container image pipeline — final implementation brief

Investigation/proposal only, revised 2026-11-05. Owner: architect0. I0–I13 are
accepted evidence. Product decisions are settled; this is the authoritative brief
for future implementation packages. It supersedes earlier normative alternatives
in the investigation records. No implementation,
repository creation, builds/tests/CI, deployment, integration or session lifecycle
action is authorized or performed by this proposal.

## Recommended shape

Build a **single small Go service for public and workflow-run repositories**, behind
the existing HTTPS proxy. Store images as ordinary immutable local files and keep
catalogs, run state and bounded statistics in one local SQLite database. Runs pin
baseline metadata and add their own verified image references; they do not copy
the public payload tree. No OverlayFS, hardlinks, filesystem snapshots/clones,
distributed object store or registry is needed. The VPS has no snapshot controls.

Recommend public serving through the same service because it provides one owner
for file lifetime/GC and records public requests directly. A staging-only service
with live-public fallback would see changing/deleted bytes, would still need to
control public file retention for consistent runs, and would need public log
collection for download statistics. Those costs remove much of its simplicity.

Run it initially in the existing `images.int.vpsadminos.org` VPS managed by
`vpsadminos-org-configuration`: NixOS userspace on a vpsAdminOS host. Go/SQLite and
ordinary files need no native vpsAdminOS runtime or privileged mounts. Preserve
`images.vpsadminos.org`, its HTTPS proxy and v1 URLs. A separate VPS is only a later
capacity/isolation choice. Bound staging storage and reserve public-serving headroom.

Code home: a new `osctl-repo-server/` Go component in **vpsadminos**, beside
`osctl-repo`, which owns the image-repository protocol. Package it through that
repository's Nix definitions. Org configuration owns deployment, proxy routing and
site limits. No new Git repository is proposed or created.

## Three entry points, one build path

| Trigger | Build selection | Publication |
| --- | --- | --- |
| Default-branch push (`staging` at inspected source) | Changed/affected images; shared-tool changes expand the affected set | Automatically publish each independently verified eligible image. |
| Weekly schedule | Full configured image/variant catalog at current default source | Preserve full rebuilds, partial success and configured public GC. |
| Manual dispatch | All or explicitly selected images | Trusted default source publishes automatically; other refs remain staging-only under this proposal. |

Resolve exact source/input identity and expected image/variant work items once per
run. A fails/B passes still permits B's public update; successful full-view sealing
or unrelated full CI is **not** a publication gate. Publication may collect the
eligible subset at run end, preserving configured alias order and full-catalog GC;
no new early-publication cadence is required. Explicit result-aware conditions must
avoid Actions skipping export/publication merely because another image failed.

The run plan freezes selected image names/variants, configured ordering, tags,
defaults and GC policy from the exact source. Resolve each item's actual image
configuration **once at dispatch in its intended build environment**, including
date-derived versions. Persist that assigned descriptor and pass the captured
configuration through build/test/export using a supported override; do not evaluate
RELVER again or predict it before midnight. Verify output tuples against that
descriptor. A retry retains it with a new item-attempt ID; a changed identity needs
an explicit new assignment/run attempt. Unchanged images do not need rebuilding.

Keep the initial bounded pool of run-lived VM workers on existing self-hosted
runners. One coordinator dispatches work dynamically; each VM runs one image's
build → existing image tests → export, then reuses its builders for another image.
Start Guix/Gentoo early while leaving capacity for quick work; builder affinity is
soft because Gentoo and many quick distributions share Fedora. Immediate per-image
results do not wait for all other builds/tests. Current multi-image `--jobs` has
such barriers; reuse OSVM's persistent lifecycle with per-image commands instead.

Workers have separate disks/state/output/cache/log paths and host port assignments,
serial internal execution, and keep-failed off. New workflow runs get fresh workers.
Ordinary image failure does not prove builder corruption: drain/quarantine uncertain
state before reuse. I7's targeted `osctl-image ct del --type builder --force <CTID>`
needs exact ownership/idle checks; it can kill an active CT and only recreates on
next `UseOrCreate`. Preserve verified exports, discard suspect unverified work, and
replace an uncertain worker for a bounded recorded retry. No reset API is needed.

Useful parallelism is initial scope, with count/resources chosen from measurement.
The user reports a recent 18-hour total run; no per-image duration or speedup has
been measured here. The longest image remains a lower bound on elapsed time.

## Simple file and metadata model

- **Image files:** a unique immutable file ID, checksum, size and format. Same-tuple
  replacement receives a new file ID; existing bytes/attributes are never modified.
  Files remain outside SQLite. Complete and verify an upload before committing a
  visible reference; interrupted uploads stay pending and are retryable.
- **Public catalog:** full tuples, tar/ZFS file references, tags/defaults and HTTP
  metadata. A transaction selects an updated catalog coherently.
- **Run:** repository/run-ID/attempt, source/input identity, pinned public-baseline
  catalog, expected changed items, candidate receipts and readiness/expiry state.
  A new run pins metadata references, not another copy of image bytes.
- **Statistics:** bounded daily aggregates, separate from image validity/lifetime
  authority. Requester details belong only in the private structured access log.

SQLite is a single local file, not a database service. Its transactions keep
catalog changes, expected results and retained references coherent without writing
our own multi-file metadata journal. File commits precede database references;
recovery can reclaim unreferenced interrupted uploads. One mutation authority
serializes import/publication/GC. Protect reference lookup-to-file-open from races
with deletion. Metrics are queued/batched separately: logging failure or pressure
must not block an image response; show incomplete/dropped measurement if necessary.

Use SQLite transactions with foreign-key enforcement, WAL and durable commits.
Receive into a unique pending file, verify its size/hash, flush it, rename it to its
immutable final ID and flush the parent directory **before** committing a visible
catalog/receipt reference. A crash before that transaction leaves only an orphan or
pending upload; a crash afterward must leave durable bytes. Reconcile pending/orphan
files on restart without deleting active uploads. Reclamation first marks an
unreferenced file unavailable for new references under the writer/read-pin boundary,
then unlinks it idempotently; failed unlink remains retryable and accounted for.

### Control and state contract

Restricted SSH invokes the local admin CLI, which submits commands to the service's
single local writer; it does not edit SQLite/files independently. The logical
operations are begin/status/renew, bind item, upload/result, finish/seal, publish,
expire/reclaim and public-generation export/import. Exact command spelling and
internal types are implementation details, not additional product decisions.

Runs have stable repository/run/attempt IDs and states **open → finished → sealed**,
with **expired** terminal retention state. Finish freezes outcomes and marks any
unfinished work interrupted; a finished run with failed items remains unsealed but
retains eligible receipts. Each work item has queued/running/verified/failed/cancelled
outcome and numbered attempts. Only a complete successful build/image-test receipt
plus all verified files can produce verified status. A later attempt supersedes
unfinished earlier attempts; a late old result cannot overwrite it. Ordinary image
failures are not automatically retried; diagnosed worker failure permits a bounded
recorded retry after its owned state is drained/replaced.

Every mutation has a stable request ID and request digest. An identical retry returns
its stored result; reuse with different content is a conflict. Unknown IDs, source/
tuple mismatch, failed integrity and invalid state fail explicitly without changing
visible state. Busy/interrupted transport can be retried with the identical request;
conflicts require status inspection. Sealing and publication are independent,
idempotent recorded outcomes. Sealed contents never change; expire removes access
and references through retention rules. Run reads before seal return not-ready,
unknown paths return 404, and expired run URLs return 410 rather than public fallback.

### Pinned fallback and full-CI readiness

A run lookup has explicit ownership, rather than “try a candidate file, then public”:

1. **Expected changed tuple/variant/claimed alias:** only that run's successful,
   verified candidate reference can satisfy it. Pending, failed, missing/corrupt
   output or a missing declared format never falls back to baseline.
2. **Unchanged tuple:** use the pinned baseline reference and retained file bytes.
   A missing preexisting dependency is an explicit error, not live fallback.
3. **Unknown path:** return 404. A run is not advertised ready before sealing.

The Go service synthesizes the complete INDEX and resolves canonical paths from
these mappings. After selected work is terminal, seal only when every expected
candidate has its same-run source/tuple/format/hash receipt and final alias/default
resolution is valid. The sealed run URL is immutable; later deliveries require a
new attempt. This supplies **all unchanged distributions plus new replacements**.
Preflight suite image/tag/variant dependencies too: today's public catalog may
already lack a required old distribution, which is not repaired by metadata pinning.

Choose pinned fallback, not live fallback. A pinned INDEX pointing at mutable
`/srv/images/...` files would still drift on same-version replacement or GC; the
service must actually own and retain immutable files. Active-run references keep
old bytes available even after their public catalog entry is removed.

Full CI deliberately waits for selected builds and this one seal. Producers remain
parallel and stream per-image results; there is no per-image consumer scheduler.
The image-build workflow reuses `image-scripts/tests` inside each worker;
`image-scripts/test@X` stays a focused local/debug path. General integration tests
still boot the OS under test. Add one run URL/readiness identity to `--test-config`
and consume it in common pool setup, including runtime-created pools. Assert the
exact default repository before first fetch; pool-active alone precedes repository
configuration. Preserve intentional custom-repository fixtures and use fresh
run-scoped caches, since existing cached clients can fall back to cached bytes on
HTTP errors. Most ordinary `osctl ct new` commands remain unchanged.

## Existing v1 over HTTP

Keep public `/v1/INDEX.json` and canonical tuple paths ending in
`image-archive.tar` or `image-stream.tar`; a run adds `/runs/<run-key>` before `v1`.
Preserve variants, architectures, format omissions, JSON tags/defaults and documented
alias paths. Existing clients ignore the pathname values inside INDEX, so Go must
stream the selected file at the requested canonical path, not redirect to a file
ID or upstream URL. No osctl/osctld client protocol upgrade is required.

Preserve GET/HEAD, identity bytes and valid length/framing. Existing clients use
If-Modified-Since/Last-Modified and 200/304; ETag alone is insufficient and redirects
are unsupported. Sealed URLs have stable validators. Mutable public URLs must not
return stale 304 after replacement/rollback, including same-second changes;
conservative 200 is compatible when a validator is ambiguous. Ordinary Go file
serving can support ranges, but current vpsAdminOS clients do not require resume.
Public INDEX and payload requests remain separate: public pruning retains its
existing old-index boundary, even while private run references keep the bytes.

HTTP reads cannot mutate state. Keep administrative operations behind restricted
SSH invoking the service's local CLI/serialized writer: begin run, receive/import,
seal, publish and maintenance. No public mutation API or admin web interface is
needed. Authenticate run/source eligibility through trusted workflow admission;
a manifest's claimed SHA alone grants no publication authority. Keep publication
credentials out of worker builds and exclude untrusted PR code from persistent
self-hosted runners. Existing nginx/TLS remains the front door.

Use distinct restricted producer and publisher SSH roles. Producers can create
their allowed repository's staging runs, upload and finish/seal them; they cannot
change public state. A separate protected publishing job receives the publisher
credential, outside worker VMs/build execution. Repository/workflow/ref admission
and secret access are enforced by CI/runner settings outside editable PR code.
That job checks trusted GitHub event/run metadata and exact source SHA against the
allowed default-branch policy, then requests publication of the matching receipt
set. The service requires publisher authority and matching stored identity; producer
metadata alone is not authorization. Other refs have no automatic promotion path.

## Public GC and staging lifetime

Preserve the exact configured public policy in
`os/configs/image-repository.nix:252–350`: vendor/variant/arch/distribution groups,
first matching rule, native tuple-string catalog order and keep counts. Preserve
configured add/tag precedence, defaults and alias removal; completion order must
not change tags such as Debian's shared `oldstable`. Match supported Ruby rule
semantics explicitly in Go and compare results against native fixtures.

Public GC removes public entries/aliases and makes their public URLs unavailable
as today. It does **not** immediately unlink a file still referenced by a run,
pending commit, bounded rollback state or in-flight read. Physical reclamation
removes only unreferenced files safely. A private run reference never keeps an
expired version listed or downloadable through the public catalog.

Failed/missing builds are not deletion requests; successful default-source results
merge into fresh public state in configured order, then full-catalog GC applies,
including named-subset and mixed-failure runs. Four old matches plus a failed new
one stay four; five old matches can still prune to four. Unmatched fixed versions
and variant/family separation retain their current behavior.

Run leases/finite TTL, quotas and abandoned-run expiry bound staging references;
expired URLs fail explicitly. These limits are separate from public keep-count
policy. Runners retain only transient export/upload scratch and may clean it after
verified server acknowledgement through future bounded/retryable CI cleanup.
Ordinary new immutable uploads consume space, but creating another run does not
copy its baseline payloads. Actual storage headroom and limits remain unmeasured.

Publication starts from the freshly read public generation, not a run's baseline.
The request names that generation and the eligible receipt set; the writer compares
it again inside the transaction. A concurrent advance requires refresh/re-evaluation,
never a blind replay. Skip superseded tuple replacements using source ancestry and,
for equal source, the service's recorded run-admission order; the trusted publisher
checks ancestry against current provenance, failing closed when unavailable. Older
runs cannot restore newer aliases/defaults or GC policy. Apply accepted results in
configured order, then current authorized defaults/GC, and atomically select a new
generation. Record updated, failed, superseded and policy-pruned items separately.

## Independent repositories and future mirrors

An independent repository has its own catalog/tag/default authority and GC policy;
another configured service instance is sufficient. A mirror reproduces a particular
public generation of the **same** repository. Keep stable repository IDs in catalog,
run, file-reference and export identities from the start; do not hardcode one global
repository. This requires no multi-tenant administration UI or repository CRUD.

The first deployment remains one instance with one logical publisher per repository,
so that instance is initially a single point of failure. Separate the reader path
from publication: reads need only the locally selected catalog and immutable files,
not a working publisher or a per-request call to another instance. A future read-only
mirror can use the same binary with its own local files, SQLite catalog and caches.
Do not share SQLite over NFS or add a distributed database, consensus or multiwriter
publication. Mirroring reads does not make new uploads, staging runs or publication
available when their publisher is down; writer failover is a separate future design.

Define a portable public generation export/import boundary initially, useful for
backup/migration as well as future mirrors: stable repository/file/generation IDs,
schema version, exact v1 catalog/hash, and canonical-path-to-file manifest with
digest, size and HTTP metadata. It must not expose internal SQLite row IDs or depend
on the publisher's local paths. Export public catalogs/files only, excluding private
run state, incoming uploads, credentials and access logs. Authenticate the import
source; generation equivalence comes from verified manifests/bytes, not a matching
repository name. See [I13: mirror boundaries](investigation-mirror-boundaries.md).

Future sync verifies complete local generations before atomic selection and keeps
the last complete generation during interrupted transfer. The initial export
interface pins source files with a bounded transfer lease; expiration requires a
fresh export. Future mirrors follow imported logical GC, retain their local read/
rollback references and enforce explicit stale-serving limits. Actual sync daemons,
private-run replication and additional hosts are outside the first delivery.

Read availability also requires independent disks/hosts and HTTPS ingress. The
existing single TLS proxy remains a failure domain. Current clients discover no
mirrors; osctld's other-alias fallback is limited to missing/unavailable images and
is bypassed by explicit repository selection. URL/routing changes and front-door
HA remain future work; neither transparent failover nor writer availability is
promised by the first deployment.

Statistics and private access logs stay local to each instance. Label dashboard
counts with repository/instance and active generation; they are not fleet totals.
Optional future aggregation must never become a download dependency. Initial scope
is repository identity, reader/writer separation and portable export/import with a
round-trip proof. A sync daemon, additional machines/endpoints and writer failover
remain future work, with no resource or deployment action authorized here.

## Public dashboard and private access log

Use one public dashboard with simple server-rendered catalog/build/status pages,
storage/expiry summaries and daily artifact requests/bytes/statuses by image,
version/variant/format. Requester IPs and User-Agents appear only in private
operational logs, never public HTML, embedded data, JSON feeds or metrics labels.
There is no private dashboard, requester-browser/API or new login system.
Existing server/SSH/log-tool access suffices for examining requester details.

Write a dedicated versioned **JSON Lines access log**, one JSON object per request
at response completion or interruption, with no sampling by default. Document a
small schema: UTC timestamp, request ID, trusted client IP and socket peer, method
and path without query, status, response bytes, duration, public/run scope and run
ID, resolved tuple/format/file ID where applicable, User-Agent and response outcome.
Separate INDEX/HEAD from artifact GETs and identify ranges/206, 304, errors and
interruptions. These are requests and bytes written, not unique people or completed
imports; retries can repeat bytes, NAT shares IPs and User-Agent is client supplied.

Keep this log private with configured permissions, rotation and finite retention;
it is not a dashboard asset. Emit structured application diagnostics separately
from access events. Escape and bound strings; do not dump credentials, arbitrary
headers or queries. Log-write failure and dropped events must be observable,
but logging/backpressure must never block or fail image downloads.

The HTTPS edge overwrites the canonical requester-IP header from its socket peer;
Go trusts it only through the exact configured proxy chain. If internal nginx
remains, explicitly preserve/rewrite it from trusted peers. Effective routing,
header overwrite and spoof resistance need proof. Route requests through Go for
one authoritative measurement; cache/static bypass would make its counts incomplete.
No GeoIP, identity system or larger analytics service is proposed.

## Ownership, migration and recovery

Native `osctl-repo remote` remains compatible. Native local add/rm/default and
legacy `rsync --delete` cannot keep mutating service-owned files: add overwrites
bytes and rm unlinks without regard to run references. Keep local tools for offline
fixtures/import/export, or an explicit future adapter. Reuse native **GC policy**,
not destructive local-rm execution against managed files.

Begin with a disposable catalog/import and the run routes while testing old-client
compatibility. Production adoption requires sole writer ownership: exclude legacy
rsync/native writers/GC, inventory one coherent INDEX, actual files/formats, hashes,
tags/defaults and path bounds, and record the exact imported baseline. Existing
regular payload files can be adopted in place with assigned IDs once protected
from all old writers; this avoids mandatory initial copying/moving. New uploads
use new immutable paths. Alias symlinks become metadata resolution.

Then switch existing public v1/alias routes to Go, keeping HTTPS/URLs. Do not leave
static fallback to legacy payload paths: it would expose logically pruned files.
Preserve basic catalog browsing/download links, replacing current fancyindex with
a small equivalent listing rather than retaining a bypass. Validate the exact
imported baseline and old-client behavior before enabling automatic publication.

Back up metadata together with its retained file references. Recovery can select a
known catalog with correct HTTP freshness. Returning to the legacy static service
after new promotions requires export/materialization of the intended current
catalog and reconciled writer state; merely restoring the stale old directory or
rsync source would lose updates. Keep import/file-map and recovery evidence. This
new local persistence requires its own schema/restart/recovery checks, but no fleet
upgrade, database migration in vpsAdmin or coordinated node rollout.

## Implementation packages and preflight

This is a sufficient package brief; there are no remaining product decisions.
The table defines future allocations, not current code releases. Lead acceptance
and the user's next implementation instruction release work; deployment/integration
retain their separate authorization. Routine internal types/CLI spelling are settled
by owners under these contracts, not another architecture exercise.

| Package / owner | Files and deliverable | Dependencies; acceptance/checks; required evidence |
| --- | --- | --- |
| P0 / implementer1 | Existing runner and org images/proxy configuration assessment; site preflight below | Read-only/site checks when authorized. Record observed capacity/admission/routing/import facts and chosen configurable limits; unresolved fact blocks only dependent deployment or privileged execution. |
| P1 / implementer2 | New `osctl-repo-server/` storage/catalog/control/CLI, Go module and entry point; Nix package; service README and `docs/specifications/image-repository.md` | This brief. Crash-safe file/DB order, state/idempotency/authorization, immutable run refs, exact GC, portable import/export and restore. Quick fault/contract/native-GC fixtures; exact revisions, changed files and results. Own shared types/entry point/package files. |
| P2 / implementer1 | Disjoint server HTTP/dashboard/access-log files; org `int.images`/proxy configuration; site operations guide | P1's recorded control/reader interfaces and P0 routing facts. Old v1/aliases/validators, public-only aggregates, private parseable logs, trusted requester chain and nonblocking metrics. Protocol/log/privacy fixtures and source/config evidence. |
| P3 / implementer0 | `osctl-image` captured-config support; repository-builder OSVM/batch seams; workflow helpers/YAML; common test-config/pool readiness; image/testing docs | P1 command/receipt contracts and P0 runner admission. Three triggers, dispatch-frozen date/variant identity, parallel warm workers/reset isolation, per-image eligibility, one full-CI URL and no baseline masking. Queue/identity/consumer/failure checks; source/input manifests and exact evidence. |
| P4 / implementer1 | Org deployment configuration/operations guide; vpsfree legacy build-host configuration; session rollout evidence | P1–P3 committed/reviewed and shadow checks accepted. Exclusive coherent adoption, v1 route move, old-client validation, automatic-publication enablement, timer retirement and verified current-catalog recovery export. Record exact source/system/profile heads, commands and outcomes. |

P1/P2/P3 can work on disjoint files after relevant shared contracts are recorded;
P2 can use catalog fixtures while core develops. P1 owns shared Go types, main,
module/package wiring and README merges; P2 sends changes there to that owner.
P3 owns workflow/test integration. Lead assigns short exclusive index/commit/rebase
windows within each shared repository and sequences overlapping edits. Each owner
supplies complete base/head/file/check and history/migration evidence through fixes.
Core docs belong with the Go component/protocol; pipeline docs in existing image/
testing guides; repeatable site operations in org configuration. Rollout receipts
and temporary facts remain session records. No new Git repository is required.

| Preflight owner | Bounded fact/check and decision | Failure condition |
| --- | --- | --- |
| implementer1 | Runner CPU/RAM/disk/KVM/virtiofs and VPS space/I/O; configure worker count, upload limits, reserved public headroom, leases/TTL/log retention | No safe useful parallel capacity, disk headroom or finite retention: do not launch that workload/admit uploads until limits/resources are corrected. Do not invent speedup or traffic numbers. |
| implementer1 | SSH forced-command roles, external workflow/ref/runner admission, publisher-secret separation; exact proxy peers/header overwrite and reachability | Untrusted execution can obtain publication authority, spoof requester attribution or bypass the intended route: block affected activation. |
| implementer0 | Required suite tuples/tags/variants and every normal static/runtime pool's exact URL/readiness/fresh cache | Missing unchanged dependency or live fallback: report a dependency/wiring error; no false full-CI pass or automatic rebuild of untouched images. |
| implementer1 with implementer2 | Active public catalog/files/aliases/hashes, all old mutators, current activated heads and coherent backup/export | Cannot exclude a writer, validate a file/path or prove recovery materialization: block production adoption, continue disposable fixtures. |

These are site/verification facts, not open product choices. Numeric limits are
configuration established by P0 and verified under actual workload; they must not
silently become unlimited when unknown.

## Delivery and verification order

1. Establish P0 facts and implement core/protocol/dashboard against disposable data.
2. Add workers/workflows/full-CI wiring with the same service contracts; prepare all
   intended commits and quick checks. The lead then invokes independent final review,
   including whole-branch history/migration and durable SQLite upgrade/recovery scope.
3. Run the longer shadow campaign below: complete catalog, mixed failures, exact GC,
   old clients, immutable active run and portable export/materialized restore.
4. After separate deployment approval, exclude/stop the old writer, capture/adopt
   the coherent baseline, move public routes, validate old clients and recovery,
   then enable automatic publication and retire the old timer. Preserve URLs and
   prevent any overlapping rsync/native writes. No coordinated node upgrade.
5. If rollback is needed after new publications, export/materialize the intended
   current catalog and reconcile legacy source/freshness before re-enabling rsync;
   never expose a stale tree as recovery. Preserve the exact rollout evidence.

Quick proof covers protocol fixtures and old-client behavior; expected missing/failed
candidate despite baseline; alias/default/formats; transaction interruption and
safe file reclamation; exact GC comparison; trusted-source publication; spoofed
requester headers and logging/metrics failure without failed downloads. Check public
HTML/JSON/metrics contain no IP/UA; parse every access-event line as versioned JSON,
including escaped strings, trusted IP, error/interruption bytes and UTC/duration.
Round-trip a portable public generation into independent local state; verify IDs,
catalog/alias/hash equivalence and that incomplete imports never replace ready state.
Quick checks are scoped to changed code; retain exact successful evidence rather
than repeating it without changed inputs. Planning records alone trigger no automatic
review, and no implementation review/test is being run during this planning task.

Longer proof: mixed A-fail/B-pass publication even with blocked full CI; unchanged
and new distros from one pinned run URL across runners; same-tuple public update
and public GC while an old run downloads; worker reset/concurrency; coherent
legacy import, restart, public route switch and recovery export. Measure file/DB
space, request throughput and worker CPU/RAM/I/O before choosing concurrency and
retention values. Each longer batch records revision, inputs, command, expected
duration, risk and stopping condition. Stop on corrupt/mixed bytes, unexpected
publication/authority, failed cleanup or resource-budget exhaustion; diagnose before
retry. Unexpected local kernel builds follow workspace cache-investigation rules.
Use the normal fresh verification watcher for long/uncertain checks. Finish once
the named acceptance evidence passes; no open-ended performance/analytics campaign.
Active site facts remain unverified in this planning turn; no runtime checks ran.

## Evidence

All source inspection used fixed canonical bare revisions: vpsadminos
`2951a632c4254a44747a8da326e3dde897eaa0e2`, org configuration
`ca96c95a1fee04793468785d8323a759615b2b4e`, and builder configuration
`f4069909b55fbed907cb658f350ec6a59f97e05a`. The lead matched remote defaults on
2026-11-04 around 21:57 UTC; no claim is made about active production revisions.
The configured builder pins vpsAdminOS `dd188397abe37d0bc33f4c5dfb3605206ce5e326`;
I1 records equivalent relevant builder module directories at the inspected head.

Current decision sources: [I10 HTTP/fallback](investigation-http-service-contract.md),
[I11 file ownership/GC/adoption](investigation-service-storage.md),
[I12 proxy/statistics](investigation-download-stats.md), and
[I9 full-CI wiring](investigation-complete-ci-view.md).
Retained facts: [I0 tests](investigation-vpsadminos.md), [I1 builder](investigation-builder.md),
[I2 public clients](investigation-publication.md), [I3 hosted runners](investigation-hosted-runners.md),
[I4 collisions](investigation-batching-concurrency.md), [I5 parallelism](investigation-parallel-workers.md),
[I6 catalog GC](investigation-scheduling-gc.md), [I7 reset](investigation-builder-reset.md).
[I8 filesystem staging](investigation-staging-service.md) remains historical
constraint evidence; its copying/wrapper ownership design is superseded here.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/)
