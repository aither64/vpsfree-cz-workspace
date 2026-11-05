# I13: independent repositories, public mirrors and failover

2026-11-05, implementer0; prior packets accepted, capacity/session/env confirmed.
Unchanged workspace/repository guidance and skills reused. Fixed bare source
O=`2951a632c4254a44747a8da326e3dde897eaa0e2`; org configuration
C=`ca96c95a1fee04793468785d8323a759615b2b4e`, proxy evidence reused from I2.
Only this file written; no runtime, HTTP, DB, Git mutation or lifecycle actions.
Source behavior/proposal only; production and actual failover remain unverified.

## Current clients

- O `osctld/lib/osctld/utils/container.rb:7-17`: without `--repository`, use
  every enabled repository in the selected pool; explicit `--repository`
  selects just that named alias. It does not take a list of alternative URLs.
- `:31-44,75-90` tries each repository, zfs then tar, returning the first
  available image. Missing images and repository-unavailable errors allow the
  next repository. This is not a promise to recover from every import, content
  or application error. Prior I0 establishes insertion order, not priority or
  health-aware load balancing. A stale first repository can satisfy the lookup.
- O `osctl/lib/osctl/cli/app.rb:666-667,2196-2208,2231-2234` exposes explicit
  image repository selection, named repository add and URL reconfiguration.
  Existing nodes can configure separate mirror aliases/URLs; no automatic
  fleet-wide discovery or rollout of mirror URLs is established here.
- O `osctl-repo/lib/osctl/repo/remote/repository.rb:7-9` accepts one root URL;
  `downloader/base.rb:29-35,54-80` connects that host and retries that endpoint.
  It has no mirror manifest/discovery/failover list. DNS/proxy routing can keep
  one URL, or operators/orchestration can select/configure another URL. Explicit
  `--repository` bypasses osctld's other-alias fallback.
- C `cluster/org.vpsadminos/proxy/config.nix:100-104` puts the public hostname
  through one configured HTTPS proxy to one images backend. More backends
  behind that same proxy do not remove its failure domain. Independently
  reachable mirror URLs plus explicit client configuration, or separately
  designed front-door redundancy, are needed to cover proxy failure.

Independent repositories have their own catalog/tag/default authority and may
serve different bytes for the same tuple. A mirror reproduces one upstream
public generation. Existing v1 clients do not enforce cross-repository byte
equivalence; mirrors must establish it during synchronization (I10). Do not
treat independent repositories as interchangeable trusted replicas by name.

## Small portable public export/import boundary

Proposal only; keep this a future single-writer public replication interface:

1. Export one sealed public generation: generation ID, schema version, exact
   v1 INDEX bytes/hash (all tuples/formats/tags/defaults), and an immutable
   manifest mapping canonical tuple/format paths to object digest, byte size
   and stable HTTP modification time. Bind manifest identity to that catalog.
   Export **only** published catalog objects and referenced public payloads;
   no private workflow runs, incoming files, logs, credentials or global stats.
2. Authenticate the upstream/import source. A read-only mirror fetches only
   missing objects during sync into nonserved storage; check manifest/catalog
   consistency and every referenced payload's size/hash. It builds its local
   v1 canonical-path mapping, including defaults/tags, as in I10. No primary
   request is needed for normal mirror INDEX/artifact serving.
3. Activate catalog and mapping together only after every referenced file is
   present and valid, using one atomic local generation switch. Interrupted,
   corrupt or incomplete sync leaves the previous complete generation active.
   Preserve I10 HTTP framing/Last-Modified behavior and I2 old-index reader
   limitations; no client protocol change or per-request primary fallback.
4. Logical GC follows the imported upstream generation: stop advertising
   withdrawn tuples/formats/tags when that generation activates, not according
   to independent mirror keep-count rules. Physical objects may remain for
   old-index reader grace, rollback and active transfer references. Delete only
   after those references/grace expire; a manifest is not permanent retention.
5. Record active generation and last successful sync/lag locally. If sync's
   source retention lease expires or an object disappears before import,
   abandon that incomplete snapshot and obtain a current complete one. Never
   fill gaps with different-generation bytes or activate half a catalog.
   Keep serving the last complete generation under an explicit stale-serving
   policy, or withdraw that endpoint when its allowed staleness expires.
   Current clients do not interpret mirror lag, so enforce health/withdrawal
   outside their v1 lookup rather than implying freshness they cannot check.

This boundary permits independently serving read-only mirrors without a
cluster, consensus, multiple publishers or replicated private session state.
Scheduling, endpoint rollout, concrete retention/grace and stale-serving limits
remain future operator/design decisions. It does not change current SPOF claims.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/>.
