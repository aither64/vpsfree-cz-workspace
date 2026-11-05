# Container image build pipeline — final plan

The product scope and architecture are settled. User authorized implementation with "ok, implement it" on 2026-11-05.
The plan now guides active feature work; production activation and default-branch
integration are separate steps.
The authoritative technical contracts, package owners and acceptance checks are
in [design.md](design.md). Source findings are indexed in [state.md](state.md).

## Goal

Make container-image building, verification and publication visible in GitHub
Actions, eliminate the need to publish new images before CI can test them, and
shorten the current serial weekly run through useful parallelism. The latest
18-hour weekly duration is user-reported, not a measurement from this session.
Keep the existing public host and client URLs, independent successful-image
updates, scheduled full rebuilds and the configured public garbage collection.

## Affected repositories

- **vpsadminos:** new `osctl-repo-server/` Go component and Nix package;
  shared VM-worker build engine; Actions entry points; common test repository
  configuration/readiness; protocol, operations and testing documentation.
- **vpsadminos-org-configuration:** service/storage/limits, restricted SSH
  operations, existing images VPS and HTTPS proxy routing, trusted requester
  forwarding, logs and deployment/recovery instructions.
- **vpsfree-cz-configuration:** retire the legacy build-host timer/publisher at
  cutover and preserve a reconciled recovery path.

No new repository, machine or running-node protocol upgrade is required.

## Settled architecture

1. **Parallel image builders.** Existing self-hosted runners start a bounded,
   on-demand VM pool for each run. Each worker executes one image's build,
   existing image tests and export, then takes another item and reuses builders.
   Dynamic dispatch, slow work started early and soft builder affinity avoid
   stranding quick jobs behind Guix/Gentoo. Internal worker operations are serial,
   so fixed test IPs remain isolated. Workers start fresh on the next workflow;
   resetting a suspect builder requires idle ownership/draining or replacement
   of that worker. Preserve already verified outputs.
2. **Central Go service.** Deploy one service in the existing
   `images.int.vpsadminos.org` NixOS VPS on vpsAdminOS, managed by org configuration.
   It serves public and workflow-run repositories behind the existing HTTPS
   proxy. Immutable ordinary image files hold bytes once; one local SQLite file
   holds catalogs, run/receipt state and bounded statistics. No OverlayFS,
   hardlinks, guest snapshot controls or per-run payload-tree copies.
3. **SSH ingestion and immutable CI views.** Upload each verified image to the
   service independently. A run pins the current public catalog as metadata and
   adds verified candidate references. Every selected image/variant must have
   its own successful same-run receipt before sealing. Old baseline content can
   never conceal a failed or missing rebuild. Full CI receives one sealed URL
   containing unchanged baseline distributions plus new candidates.
4. **Small test changes.** Reuse `image-scripts/tests` inside the build workers;
   keep `image-scripts/test@X` for focused local/debug use. General integration
   tests still boot their own OS VMs. One common repository URL/readiness contract
   covers normal and runtime-created pools; intentional repository fixtures stay
   explicit. Most existing container-create commands remain unchanged. Full CI
   waits for selected candidates; no per-image integration-test scheduler.
5. **Independent public publication.** Successful build plus image-test results
   from trusted default-branch source are independently eligible. Publish exact
   uploaded bytes into fresh current public state, applying configured alias
   precedence. If A fails and B passes, B still publishes; A has no replacement
   delta. Neither full-view sealing nor unrelated full CI is a global gate.
6. **Retention.** Preserve exact public GC grouping, matcher order, version
   ordering, keep counts and tag/default behavior, including subset/mixed-failure
   runs. Removing a public entry removes public visibility. Physical files remain
   only while retained public/run/export/recovery references need them. Run expiry,
   leases and quotas bound staging; request failures are never deletion commands.
7. **One public dashboard, private access log.** Public pages show aggregate
   image/build/storage/request statistics. IPs and User-Agents appear only in a
   documented versioned JSON Lines access log with private permissions and finite
   retention. No private dashboard, new login system or analytics platform.
   Configure trusted requester forwarding at the HTTPS edge; statistics/logging
   failure must not block downloads.
8. **Future mirrors.** Stable repository/file/generation identities, local reader
   state and portable public export/import are initial foundations. Independent
   repositories can use separate configured instances. Actual read-only mirror
   synchronization, extra hosts/frontends and writer failover are later work.
   Initial deployment remains a SPOF, including its current HTTPS proxy.

## Build entry points

| Event | Selection | Publication policy |
| --- | --- | --- |
| Default-branch push | Changed images and affected dependencies | Automatically publish individually verified successes. |
| Weekly schedule | Full configured public image/variant catalog | Same verification, partial-success publication and public GC. |
| Manual dispatch | All or selected images | Trusted default source uses the same publisher; other refs stage only. |

All modes use one source-pinned build/upload path. Authority to publish comes
from restricted workflow/service credentials, never a caller-provided branch
flag. Persistent privileged runners must admit trusted revisions only.

## Ordered delivery

1. **Preflight and fixtures:** refresh implementation baselines, inventory the
   live catalog/legacy writers, confirm runner admission/resources, service disk
   budget, SSH roles, proxy routing and all normal test-pool/image dependencies.
   These are implementation checks with named owners in design.md, not open
   product decisions. Fail the affected package before activation if they fail.
2. **Service core and protocol:** durable files/SQLite transactions, run and
   receipt contracts, v1 HTTP, exact GC, coherent legacy import/export and
   independent publication. Prove these against disposable data first.
3. **HTTP/dashboard/logs and deployment candidate:** implement disjoint service
   surfaces against agreed core interfaces; package through Nix and prepare site
   configuration without changing production. Verify old clients, cache behavior,
   public requester-data exclusion and private JSONL output.
4. **Workers, Actions and CI:** integrate the parallel pool, frozen work identity,
   uploads, three triggers and common sealed-repository configuration. Prove new
   images absent from public and unchanged distributions both work in full CI.
5. **Committed-change review and shadow verification:** pass quick checks and
   independent final review, then run bounded integration checks and one full
   weekly shadow run. Record resource/storage/timing measurements before selecting
   operational limits. Long checks use the normal verification watcher workflow.
6. **Controlled cutover:** exclude old writers, capture/import the exact live
   baseline under exclusive ownership, verify compatibility and switch the public
   HTTP routes. Enable the new publisher/schedule and retire legacy timer/rsync.
   Record source/configuration/input and import/recovery evidence. Deployment and
   repository integration retain their normal explicit approval gates.

Future package ownership and safe overlapping-file sequencing are defined once
in design.md. P0/P1/P2/P3 and native compatibility deliverables are committed and independently
reviewed; findings were corrected within their existing contracts. Service/native
runtime checks pass. The real two-worker smoke passed for three Alpine images:
45 image tests, overlapping workers, same-builder reuse, sealed payload hashes
and cleanup. A single-VM common-repository/runtime-pool consumer check is in
progress; it does not establish full-suite or weekly-shadow coverage. Exact heads,
checks, remaining runtime limits and ownership transitions are in state.md.

## Required acceptance scenarios

- Two useful worker pipelines overlap, reuse builders and isolate fixed IPs;
  a slow image does not prevent another worker completing a quick image.
- An idle owned builder can be reset/recreated; uncertain cleanup does not return
  a worker to service or erase other verified results.
- New and unchanged distributions use one run URL; a failed selected image cannot
  pass through baseline or stale-cache fallback.
- A fails/B passes still uploads/publishes B for default source, even with blocked
  full CI. Push, weekly and manual selection policies are covered.
- Old v1 clients retain URLs, formats, aliases and HTTP/cache behavior.
- Native and new GC results match for rolling/fixed versions, variants, aliases,
  named subsets and failed builds. Active runs keep pinned bytes after public
  replacement/pruning; expired unreferenced data is reclaimed safely.
- Interrupted upload, restart, duplicate/conflicting receipt, concurrent public
  update and stale publication cannot expose partial or incorrect state.
- Public HTML/JSON/metrics contain no IP/UA; JSONL logs are parseable and private,
  trusted requester identity is correct, and log failure cannot fail downloads.
- Portable public export/import preserves a complete catalog and file hashes;
  failed/incomplete import cannot replace the last complete reader state.
- Legacy adoption and recovery export preserve exact intended public state;
  restoring stale rsync input is never a rollback shortcut.

## Compatibility and recovery

Public v1 URLs, defaults/tags, archive/ZFS formats and existing node clients stay
compatible. The service becomes sole catalog/file-lifetime owner; legacy native
local writers/destructive GC and rsync cannot run concurrently. New local SQLite
persistence needs schema/restart/recovery checks, but no vpsAdmin schema migration
or coordinated running-node upgrade.

Keep a verified service metadata/file backup and portable catalog export. Recovery
selects validated state with correct HTTP freshness. Reverting to static serving
requires materializing the intended current catalog and reconciling the legacy
writer source before re-enabling it, preserving successful intervening updates.

## Remaining checks and first-version limits

Worker count, CPU/RAM/I/O budget, upload/run/storage limits and retention durations
are configurable and set from preflight/shadow measurements. Live revisions,
actual filesystem inventory, credential admission and effective proxy headers are
not yet verified. No numerical speedup or historical download statistics is claimed.
These checks do not reopen the chosen architecture.

Actual multi-host mirrors, redundant HTTPS ingress, multiwriter publication,
automatic writer failover, a private dashboard and global analytics are outside
first delivery. Existing snapshot/clone controls are unavailable and unnecessary.

Planning records alone do not trigger independent final change review. Intended
implementation is committed and independently reviewed; accepted review and runtime
fixes remain within their existing contracts. Verification and rollout retain
separate evidence and approval requirements. Full weekly shadow, production
preflight and cutover remain unproved. The session stays active and open.
