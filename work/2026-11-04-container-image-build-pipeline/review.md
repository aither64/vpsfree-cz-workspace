# Final independent review — reviewer0

Reviewed vpsadminos d2fe1489f0b0b213fb247aeee6e081d349adaf42..932937390c876e4afcc5df6e0da653a39177af58 and vpsadminos-org-configuration ca96c95a1fee04793468785d8323a759615b2b4e..33ee9f01a9d18b9da8f39e5878869c1ff08719ef. High risk; general, architecture/repetition, scope/proportionality and risk/compatibility lanes. Retained reviewer0, gpt-6.1-sol/xhigh/read_only, independent, no overrides or nested reviewers.

This is the report on the assigned committed ranges. Concurrent remediation (including later 087031170 and dirty successor files) is outside this report's provenance. Remediation acceptance belongs to the lead under the skill's narrow-fix/affected-lane rules. Source review only: no tests, builds, services, deployment, Git mutation or lifecycle actions. Complete report supplied to lead for saving under tracking lock because retained higher-priority instructions require read-only access.

## Findings, in severity order

### F1 — Blocking: every real artifact request receives an invalid resolver path
Lanes: general, risk/compatibility. Commit a9ce2d4f79775873b35a34cb596792515f761a98.
osctl-repo-server/http.go:119 forwards "v1/vendor/variant/arch/distribution/version/image-stream.tar" to Store.OpenFile. store.go:290 passes it directly to resolve, whose catalog.go:145-147 requires exactly six components without v1. Public and sealed-run INDEX requests work, but all real artifact GET/HEAD requests return 404. HTTP tests use a fixtureReader accepting the seven-component form (http_test.go:37), while core tests call the six-component form, so separate green suites miss the integration failure. Normalize once at the HTTP/Reader boundary and cover real Store plus HTTP canonical/alias/public/run payload bytes. Lead has accepted and assigned this narrow fix; the successor is not reviewed here.

### F2 — Important: parallel uploads can spend the same reserved filesystem headroom
Lanes: risk/compatibility, general. Commit a9ce2d4f.
osctl-repo-server/upload.go:28-47 accounts pendingBytes against MaxBytes but checks filesystem availability using only the new upload's size plus ReservedBytes. Earlier admitted streams that have not written yet reserve no filesystem capacity. For example, free space 100, reserve 20 and two initially stalled uploads of 60 each are both admitted if MaxBytes permits them; concurrent writes can consume the protected reserve and reach ENOSPC, including for SQLite/public operation. Apply a conservative shared reservation to filesystem admission as well as the logical quota, preserving the existing upload mechanism. A concurrent delayed-stream admission check should prove the reserve cannot be oversubscribed.

### F3 — Important: sealing/publication blocks new downloads for a whole-catalog hash scan
Lanes: architecture/repetition, scope/proportionality, risk/compatibility. Commit a9ce2d4f.
control.go:105-106 holds the global Store mutex while seal at :419 and publish at :533 call verifyCatalog. store.go:428-458 reads/hashes every referenced payload, including unchanged pinned baseline files. Catalog/OpenFile require that mutex (:279, :284). Thus one small successful-image update prevents every new public lookup/download until the entire retained catalog is read, scaling the outage with repository bytes rather than the update. Tiny fixtures hide this. Keep byte verification at upload/adoption/import/export boundaries; normal catalog selection should validate already-verified immutable references without rehashing unchanged payloads under the reader boundary. Lead has accepted and assigned a bounded fix.

### F4 — Important: no delivered automatic expiry/reclamation makes staging lifetime finite
Lanes: general, risk/compatibility. Commits a9ce2d4f and org33ee9f01.
control.go:173-177 counts every run whose recorded state is not expired against MaxRuns. A passed lease only rejects reads; it does not change that state. markReclaim at :576-578 likewise retains those baselines/generations. main.go supplies no maintenance loop, and org modules/services/osctl-repo-server.nix:181-222 supplies only the serving service, no expiry/reclaim timer. README.md:99 delegates scheduling to an administrator without delivering it. After MaxRuns normal workflows, admission remains blocked until manual expiry; unused payloads also remain until manual reclaim. The supported automatic staging-retention contract needs a conventional bounded expire-then-reclaim loop/timer with distinct request IDs per execution and visible failures. No new cleanup framework is needed.

### F5 — Important: real SSH error exits bypass the publisher's structured conflict handling
Lanes: general, risk/compatibility. Commit 932937390c876e4afcc5df6e0da653a39177af58.
tools/image_pipeline/control.rb:53 raises a generic SSH failure before parsing response JSON whenever ssh exits nonzero. The actual forced ctl writes its JSON response and returns an error for !OK (socket.go:166-170; main.go:37-39), so ordinary service conflict/superseded responses take this path. Publisher's rescue ControlError at publisher.rb:45 never refreshes/retries the generation or records same-source supersession; its mocked control specs exercise a behavior the real transport cannot produce. Decode valid structured service failures before treating exit status as an unstructured transport failure; retain fail-closed handling for malformed/absent responses. Lead has accepted and assigned the fix.

### F6 — Important: automatic push selection is incompatible with its public-plan consumer
Lane: general. Commit 93293739.
.github/workflows/image-scripts.yml:66-73 feeds changed-image-scripts.rb output directly into tools/image-pipeline.rb:29-33. That detector inventories all source image directories, while the new consumer rejects any name absent from the configured public plan. A shared image-scripts/bin change or common.sh change emits existing devuan-4 (detector :148-154), but os/configs/image-repository.nix configures only devuan5/6: the entire automatic pipeline aborts before producing images. Intersect automatic affected selection with configured work; keep manual unknown-input rejection separately.
Also image-scripts/tests/** triggers this workflow but is not handled by the detector or the workflow's shared-change expansion. Such a push selects zero images and can seal/publish the unchanged baseline without running the changed image tests. Shared image-test changes must select their affected configured builds. Cover both real selection cases.

### F7 — Important: readiness preflight omits actual explicit CI tuple/variant requirements
Lanes: general, risk/compatibility. Commit 93293739.
tools/image-pipeline-plan.nix:51 uses only tests/distributions.nix.all, and coordinator.rb:110-113 assumes default vendor/variant for every dependency. The CI-tagged tests/suite/dist-config/nixos-resolvers.nix:18,50-56 requires nixos22.11/minimal and24.05/impermanence, absent from that matrix. The current preflight therefore reports ready even when those required baseline images are missing; full CI is then launched against an incomplete view. Complete the existing suite dependency inventory, including explicit vendor/variant/format requirements where used, and verify them before advertising the full-CI URL. Reuse the owning test declarations where practical; this does not require arbitrary historical-daemon support or an image-dependency scheduler. The packet candidly discloses this gap, but it does not satisfy the intended complete-suite preflight contract.

### F8 — Important: a partial log write corrupts subsequent JSON Lines after recovery
Lanes: general, risk/compatibility. Commit a9ce2d4f.
osctl-repo-server/accesslog.go:284-286 leaves a partially written event in the still-open file when Write returns n>0 plus an error (for example ENOSPC). The next successful Encoder.Encode appends directly to that fragment, yielding malformed JSONL; rotation can preserve the malformed line too. Trailing-event repair at :239-264 runs only on open, which this failure does not trigger. Preserve the last complete boundary and truncate/reopen after a failed/short write before another event; count/drop the interrupted event without blocking image responses. A partial-write then recovered-write fixture should prove every retained line remains parseable.

### A1 — Advisory: initialize schema 1 in one SQLite transaction
Lane: risk/compatibility. Commit a9ce2d4f.
store.go:86-90 calls db.Exec(schema), whose independent CREATE statements precede PRAGMA user_version=1. An interruption between statements can leave version0 with existing tables; restart reruns CREATE and fails duplicate-table. Initial database creation has no prior user state, so this is narrower than an upgrade/data-loss issue. A normal SQLite transaction avoids manual first-start recovery. No schema-existence guards or predecessor compatibility path are warranted.

## Scope and architecture conclusion

Compared the recorded user choices and acceptance criteria with both complete diffstats and the delivered milestones: vpsadminos64files/+6419/-152, org6files/+471/-9; implementation released around19:30 UTC and source/quick-check/consolidation delivered around20:17 UTC, with overlapping owners rather than summed clocks. This is the explicitly chosen Go public/run service plus warm builders and CI integration, not a release bump. Immutable files, SQLite, separated producer/publisher roles, the requested dashboard/private JSONL and portable public generation transfer have current accepted purposes. No speculative scheduler, registry, private UI, HA or replication subsystem is present. The architecture broadly fits the requested boundary. F3 is disproportionate normal-path integrity work; the fixes above should stay conventional and bounded. No additional architecture exercise is recommended.

Core ownership of catalogs/files, common test-runner ownership of repository configuration, and site ownership of SSH/proxy/deployment are appropriate. The native local writer/GC remains an independent oracle and must be excluded from managed production storage. Old remote clients reconstruct canonical paths, require direct200/304 behavior and can return cached data after HTTP failure unless force-check/fresh state is used; inspected Direct/Cached implementations support the chosen conservative public IMS policy and stable sealed URLs, subject to F1.

Inspected representative external framework consumers: vpsadmin b83b26e1ba1c8e869ae3ffbcb5801ed071c3844e, including flake imports, tests/all-tests.nix, tests/make-test.nix and cluster wrapper, with actual vpsadminos pin8e44a5124439b1f3048ffc56b1717614a5360358; and confctl cc40679d267165aecfa569128438bb55fe910268, including makeTestLib/makeTest wrappers, with pin67fcc17372d175b036706a1459a8b471bfc225e0. Existing calls remain compatible when imageRepository is absent. No downstream pin changes are required by this delivery. The new daemon default affects only newly missing defaults; persisted/custom repositories retain their URLs. Arbitrary older-daemon runtime-pool support is explicitly outside the contract.

Durable documentation is discoverable from the image-creation/testing/specification pages, service README/HTTP guide and org operations guide. They correctly separate prepared adoption/recovery from executed rollout and exclude concurrent native/rsync writers. Initial service/proxy SPOFs and future mirror limits are stated. Retention instructions are incomplete as identified by F4.

## Whole-history, migration and repeated-update conclusions

Reviewed all three vpsadminos commit messages/content and the entire final diff:
a9ce2d4f service;9f78583b native compatibility oracles;93293739 assigned workers/CI. Reviewed org's single33ee9f01 commit. The initial service's shared schema/executable/package and supporting docs/tests form a coherent initial deliverable; compatibility oracles and pipeline are separate logical commits.

Independently inspected range-diff from old d2fe1489..121d349f to d2fe1489..93293739. The e7d0f28 superseded-publication fix is folded into a9ce2d4f; compatibility/pipeline patches are unchanged. Both old/new head trees equal3844d6372319f75f2c3ff92094a8a83ab0ad978e. No obsolete approaches, fixup residue or unapplied transitional history remain IN THE REVIEWED RANGES. Subsequent caused-fix commits, including087031170, must be reconciled/folded into logical owners before final readiness, preserving this report and exact successor evidence.

Persistence inventory: one new initial SQLite schema1 in a9ce2d4f, directly creating the final schema, no supported predecessor and no transitional migration. Recorded provenance is unmerged/unreleased/undeployed/not externally consumed; source and available session records are consistent with it. There are no ALTER/rewrite migrations or stale-fixture schema-existence guards. A1 concerns atomic first creation, not a request to support another schema. No migrations in other vpsadminos components; no migrations in org configuration. Legacy repository adoption is a separately controlled import with writer exclusion, not a supported SQLite predecessor upgrade.

No repeated dependency/channel/input/generated-artifact update streams exist in either reviewed range. go-sqlite3v1.14.32 is one initial selection with its go.sum and vendorHash; no flake-lock/pin updates. Native JSON fixtures are one generated oracle set, not successive superseded updates. No intermediate release/consumer/state boundary is needed to retain redundant updates because none remain.

## Residual verification and decision

BlockingF1 must be fixed before long integration; ImportantF2–F8 require fixes or explicit recorded decisions. This review does not declare the evolving branches ready.

Quick-check results are supplied evidence, not rerun here. Post-fix checks should exercise real Store/HTTP and real ctl/transport errors rather than only independent mocks, and cover the bounded reservation/maintenance/selection/preflight/log cases above. The native four-scenario CLI/HTTP/client harness, exact-final Nix package/source-plan evaluation, admitted warm-VM concurrency/replacement, runtime pool install+first fetch in one command and full CI remain unproved. No speedup is established.

P0 admission/capacity/storage/proxy peers, coherent live catalog/legacy-writer exclusion, SSH control transport and production recovery remain activation blockers. Full-CI lease must cover queueing and consumers after producer heartbeats stop. No coordinated fleet upgrade is required for the supported new-worker/new-daemon path; old remote clients stay unchanged. No deployment or integration approval is implied.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/
