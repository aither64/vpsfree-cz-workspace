# P2: HTTP, dashboard, request measurements and site configuration

Owner `implementer1`; implementation authorized by the user and released by lead
following accepted [P0 preflight](implementation-preflight.md). Source and saved
settings verified in the exact bound session. No production mutation, HTTP server,
SSH retry, deployment, default integration or lifecycle action was performed.

## Current committed state

Published whole head is `fab23ed26aefaed635c41cdb89ff30bf82632c61`, with service
`463704f2046b1a888ae18777ba4932e9d118872e`, COMPAT
`562f6bd5fe78456d7ce23be5982165659cd5931f` and org configuration
`2ed95c94f5be096b2142d96c84eb0f00b5e040be`. Actual final tree is
`475aff53b0a094cf863ecf74889e57012b044b99`. The final source change from exercised
`8d5093e3d65f561dd305898074dd8add5e49323e` affects only the native fixture generator;
all P2 files are unchanged. Fresh package/source proof is in
[final source identities](final-source-identity.md) and
[package receipt](artifacts/final-packages-acceptance.json); [state](state.md)
owns current acceptance/CI status. Original review provenance and P0 production
activation limits remain unchanged. No new source/check/index/runtime action was
performed for this evidence refresh.

### Historical fold/check scope at 2120ec2d

The earlier consolidated service was the same literal `463704f2`, with COMPAT
`39f7e73746d0157bdd8b734a76d13f9b974b7890` and whole head
`2120ec2de70b9daa38588a8ad79a8296ec3e6167`. Its tree matched the pre-fold corrective
head `fcf49d91c618abf6ab2a766d3a7c4fdc8ede91c3`:
`ec81e39192b08402eea967a1bdb1978761e36e2a`. This is historical tree-equivalence
evidence, not the current final tree. The [core packet](implementation-core.md),
[fold receipt](artifacts/p1-final-fold.json) and
[range-diff](artifacts/p1-final-fold-range-diff.txt) preserve the exact operation.

Cached Go tests (1.136s), vet and binary rebuild passed at that earlier `2120ec2d`
head; [receipt](artifacts/p1-final-head-check.log). Earlier `93293739` review and
corrective receipts retain their actual historical scope. P0 activation gaps remain.

## Original delivery history and owned files

Org configuration base `ca96c95a1fee04793468785d8323a759615b2b4e` → initial
`33ee9f01a9d18b9da8f39e5878869c1ff08719ef`, one logical commit:
`images: prepare the managed repository service`. Clean and unpushed at package
handoff. Its six owned paths are:

- `cluster/org.vpsadminos/int.images/config.nix`
- `cluster/org.vpsadminos/proxy/config.nix`
- `configs/image-repository-proxy.nix`
- `modules/services/osctl-repo-server.nix`
- `docs/operations/image-repository.md`
- `tests/image-repository-config.nix`

vpsAdminOS implementation worktree base `d2fe1489f0b0b213fb247aeee6e081d349adaf42`.
P2 contributes eight source-stable paths under `osctl-repo-server/`: `http.go`,
`dashboard.go`, `accesslog.go`, `http_stats.go`, `stats.go`, `http_test.go`,
`stats_test.go`, `HTTP.md`. First consolidated service head was
`a9ce2d4f79775873b35a34cb596792515f761a98`, after the lead-approved ordinary
rebase folded a caused core caller fix into the logical service commit. Earlier
logical service head `66338b0e811eeffb7400882008f7ed86e7515d9f` contained the narrow
authority/expiry fix before peer commits or publication. Earlier accepted head
`41e5c83e769115cefddb193237b4b05823d3d80f` is retained here as the exact revision
for the earlier check receipts. The eight P2 files are unchanged between these
original and amended service heads. A second explicit bare-repository path diff
from `66338b0e8` to prior `a9ce2d4f7` is also empty for all eight P2 paths. The lead approved one complete initial-service commit because core main
already references HTTP/observer and P2 statistics uses the initial core schema.
Core owner2 staged these eight P2 paths in its allocated combined window,
alongside its core/main/Nix paths: 24 authorized paths total, excluding COMPAT
and P3. P2 did not independently stage or commit the shared vpsAdminOS index.
The commit and required hooks completed, then owner2 released an empty index.
P2 retains diagnosis/follow-up ownership for these contributions.

## Resulting behavior

Native v1 INDEX/file/alias and `/runs/<key>/v1/` requests stream directly without
redirects. GET/HEAD length and file metadata, ranges, strong ETags and sealed-run
IMS/304 are covered. Public date-based validation returns conservative full 200
responses to avoid stale same-second replacement/rollback; strong ETag validation
remains available. Missing/unready/expired views use core reader errors, with no
static/public fallback. The caller closes the core-opened inode after serving.

Public HTML and `/dashboard.json` serialize an explicit aggregate DTO: catalog,
file/storage totals, run/item state counts, expiry and bounded daily request rows.
They exclude requester IP/UA, raw run/source records and work-item messages.
Canonical links and directory/alias listings escape content through Go templates.

A bounded asynchronous observer emits private schema-1 JSON Lines events and
separate daily SQLite aggregates. The raw log includes bounded/escaped requester
IP, socket peer, UA, context, status/bytes/duration/ranges/outcome; queries and
arbitrary headers are absent. Log files are 0600 under a 0700 directory, with
finite byte/file rotation and interrupted-tail repair. Daily rows omit requester
fields and have day/row bounds. Queue pressure, failed log opens/writes or stats
errors increase health counters; they never block an image response. Observer
shutdown requires a finite context.

The site service is opt-in and public route replacement requires another explicit
`publicServing` option. Producer/publisher/admin have separate SSH users, groups,
forced restricted commands and 0660 sockets. Distinct public keys and all capacity/
retention budgets are deployment-supplied; no production keys or limits are guessed.
The edge overwrites canonical requester IP; internal nginx trusts only its configured
edge peer and Go trusts only loopback nginx. Shadow run routes preserve existing
static public serving. Public cutover removes static/fancyindex bypass paths.

## Verification and exact scope

- Pure HTTP/log fixtures with installed Nix-profile Go 1.26.8:
  `CGO_ENABLED=0 go test http.go dashboard.go accesslog.go http_stats.go types.go http_test.go`
  passed (last observed 0.031s). Initial ambient CGO compile failed because gcc was
  absent; pure standard-library fixtures then used CGO disabled. This was not a
  replacement for the full SQLite/C compiler check below.
- Lead's fresh watcher used the targeted repository Nix Go/C environment:
  `nix develop .#osctl-repo-server --command sh -c 'cd osctl-repo-server && go test ./... && go vet ./...'`.
  Full Go test/vet passed; root tests 0.659s, Go 1.26.10. Evidence
  `/tmp/p1-go-check-2.log`, read by P2. Includes P2 SQL aggregate persistence,
  requester-independent grouping, day retention and row limits. Final source-stable
  pinned Go test/vet/build also passed before the original combined commit
  `41e5c83e769115cefddb193237b4b05823d3d80f`, as reported by
  core owner2: root tests 0.979s, receipt
  [p1-go-final.log](artifacts/p1-go-final.log). Combined commit hooks passed in
  [p1-commit.log](artifacts/p1-commit.log), with advisory 72-column warnings only;
  required workspace 80-column bounds were retained. Both final logs were read by
  P2. These logs retain their original `41e5c83e7` check/hook scope; they are not
  relabeled as an exact amended-head test. For `66338b0e811eeffb7400882008f7ed86e7515d9f`,
  the lead reported focused full tests (1.087s) plus vet green after the core
  authority/expiry fix; its new core packet is pending. P2 performed no new tests
  or source changes for this receipt correction.
- HTTP fixtures cover native JSON semantics/formats, public/run canonical/aliases,
  identity bytes, GET/HEAD framing, ranges, sealed IMS304, public replacement cache
  freshness, strong ETag, path rejection, safe errors, requester/header spoofing,
  public DTO privacy, JSONL escaping/permissions, log failures, queue pressure,
  interruption events and rotation/tail repair. No listener or VM was launched.
- Org fixture:
  `timeout 20s nix eval --offline --impure --no-write-lock-file --json --file tests/image-repository-config.nix`
  passed all six assertions: disabled default, separate restricted roles, duplicate
  key rejection, finite fixture bounds, shadow route preserved and public route via
  the service. Synthetic fixture key strings are not deployment credentials.
- Nixfmt 1.5.0 from pinned input store path formatted all five owned Nix files.
  `bundle exec overcommit --run` and actual commit hooks passed. A changed local
  Nixfmt plugin signature initially refused; its code was inspected and signed via
  ordinary `overcommit --sign pre-commit`, then hooks reran without bypass.
- `git diff --check` passed. Org source remained clean after its final commit.
  Main agent personally applied the writing/humanizer pass to settled HTTP labels,
  errors, HTTP.md and site operations prose; no rewrite was required.

## Historical consolidated branch receipt

The first consolidated service commit was `a9ce2d4f79775873b35a34cb596792515f761a98`;
its complete reviewed vpsAdminOS head was `932937390c876e4afcc5df6e0da653a39177af58`, after
COMPAT `9f78583b57d03bcda7e7a42d2acd196c4ee04d7a`. Core owner2 retained the old
range/backup ref and equivalence evidence in [implementation-core.md](implementation-core.md).
That historical tree is `3844d6372319f75f2c3ff92094a8a83ab0ad978e`, unchanged by
that history consolidation. P2's eight paths have no changes through that fold.

Final-head Go tests (0.990s), vet and binary build passed under the declared Nix
shell against whole head `932937390c876e4afcc5df6e0da653a39177af58`;
[p1-post-consolidation.log](artifacts/p1-post-consolidation.log) read by P2.
Earlier logs above retain their original revision scope. Exact final Nix proof
and whole-branch independent review remain lead-owned; no listener or new P2
source/test command was launched for this receipt update. Org commit remains
`33ee9f01a9d18b9da8f39e5878869c1ff08719ef`; P0 activation limits remain unchanged.

## Review correction: artifact path boundary

Reviewer0 found a blocking mismatch in the reviewed service: HTTP passed the
`v1` schema segment to the store's six-component tuple resolver. The mock reader
accepted the same wrong path, so earlier HTTP fixtures did not prove real-store
artifact serving. The original green receipts above retain that limitation.

The narrow correction makes HTTP the sole schema-prefix normalization owner:
strip `/v1/` before `Reader.OpenFile`, preserving all external URLs and core APIs.
Only `http.go` and `http_test.go` change. The mock uses the actual relative-path
contract, and a real Store+HTTP regression uploads/publishes public version 13,
seals a candidate version 14 with pinned baseline 13, and checks binary bytes,
default/latest aliases, HEAD lengths, no redirects, unsealed 503 and missing
candidate/format/version/run 404 behavior.

Full tests plus vet passed against base
`932937390c876e4afcc5df6e0da653a39177af58` with this two-file working patch:
`nix develop .#osctl-repo-server --command bash -c 'cd osctl-repo-server && go test ./... && go vet ./...'`,
root tests 1.063s, exit 0;
[receipt](artifacts/p2-http-review-fix.log). No listener or long integration.
The lead directly accepted this narrow correction, with no new public contract.
Correction committed as `0870311705f8c10920a57c32307a5e199fb879f3`, direct parent
`932937390c876e4afcc5df6e0da653a39177af58`, exactly the two owned files. Normal
Nixfmt and commit-message hooks passed; [commit receipt](artifacts/p2-http-review-fix-commit.log).
Index and worktree were verified clean and the short window released before
updating this record. The earlier reviewed range remains historical evidence; this caused correction
was folded into final service `463704f2046b1a888ae18777ba4932e9d118872e` by its
owner at the lead-allocated final clean boundary. No rebase was performed by P2.

Initial commit attempt wrapped the unrelated root Gemfile in `bundle exec` and
failed before Git ran because its pinned RuboCop was absent. HEAD was unchanged;
only the two owned paths were unstaged and the empty index window released before
repair. [Original failure](artifacts/p2-http-review-fix-bundle-failure.log).
The installed normal hook loads Overcommit 0.71.0 without a Gemfile directive;
core owner confirmed the prepared command is plain `git commit -F` inside the
targeted Nix shell. Ruby/Overcommit resolution was checked without installing,
signing, changing or bypassing hooks. No additional source/test changes resulted.

## Remaining review corrections: partial JSONL and automatic maintenance

F8: A short/failed file write left a fragment in the open log, and the reused
JSON encoder retained its first error. The correction restores the previous
complete byte boundary after every failed/short write; if truncation fails, it
closes the file for tail repair before another write or rotation. Each queued
access event uses a fresh encoder. The failed event is omitted and counted by
`log_failures`; asynchronous download behavior remains unchanged.

Fault injection covers partial-error, short-write-without-error and failed
truncate/reopen paths. Every retained line in active and rotated files decodes
as schema 1, the incomplete event is absent, and subsequent complete events are
preserved. Only `accesslog.go` and `http_test.go` changed for this correction.
Full Go tests/vet passed (root 1.221s, focused faults 0.018s),
[receipt](artifacts/p2-maintenance-log-review-fix.log); core owner's subsequent
shared full tests/vet also passed (1.131s),
[receipt](artifacts/p1-review-core-final.log). The earlier mixed in-progress batch
that reported five log failures exposed the sticky-encoder cause; it was not
accepted as core verification.

Go correction committed `fcf49d91c618abf6ab2a766d3a7c4fdc8ede91c3`, parent
`df143b4608b4780867c4da5b49493855859612c2`, normal hooks green;
[commit receipt](artifacts/p2-log-review-fix-commit.log). Index/worktree were clean
and the short window released before records. Service-owner folding of caused
review fixes later completed at the allocated clean boundary, as recorded in the
current state above; P2 did not rebase.

F4: Enabled site service now has a conventional persistent fifteen-minute timer
and one bounded oneshot. A dedicated `repo-maintenance` user has only the admin
socket group. The unit requires the active service and admin socket, requests
`expire` then `reclaim` with a fresh UUID per operation/tick, and stops before
reclaim on expiry/protocol failure. Timeout is 120s by default; systemd prevents
overlapping starts of the same unit. Existing writer lease/reference rules apply;
this does not invoke/change public catalog GC or add a cleanup daemon.

Org changes were confined to module, existing fixture and operations guide.
The fixture passed all eight truths, including ordered/private/bounded automatic
maintenance; [receipt](artifacts/p2-maintenance-config-review-fix.log).
Nixfmt and normal hooks passed; lead directly inspected the correction and applied
the final English writing pass to the new operations section.

Under the explicitly allocated org window, these changes were amended into the
single new logical org commit `2ed95c94f5be096b2142d96c84eb0f00b5e040be`, parent
`ca96c95a1fee04793468785d8323a759615b2b4e`;
[amend receipt](artifacts/p2-maintenance-org-amend.log). Old reviewed
`33ee9f01a9d18b9da8f39e5878869c1ff08719ef` is retained at
`refs/heads/2026-11-04-container-image-build-pipeline-org-before-maintenance-fold`.
The old tree `7836db60ad5789537233199be36840127fccb7cb` changed by the accepted
three-file maintenance diff. Captured staged final tree and actual amended tree
both equal `b20594a59063001f07137959a5b19fb73e2f63a1`; no old/new patch-equivalence
claim is made for the substantive correction. Original old-range receipts remain
scoped to their original heads. Org index/worktree clean, window released.

No new schema, public API, production activation, live maintenance, deployment,
claims or session lifecycle actions occurred. P0 activation gaps remain in force.
All P2 review corrections are committed and ready for lead acceptance; no further
P2 source work is planned except concrete findings.

## History, schema and remaining gates

Org has one final logical commit and no migration. Its earlier local `2f059a6`
was amended before publication to align shutdown grace and message wrapping;
there is no externally consumed predecessor. vpsAdminOS creates a new local
SQLite schema, version 1, owned by P1, including the initial `http_daily` table
provided by P2. It is unreleased/undeployed and has no predecessor migration or
optional table-existence upgrade guard. Public v1 protocol remains compatible.

Production P0 access/capacity/admission/routing/current-catalog facts remain
unverified activation blockers. Do not enable the service/public writer or stop
legacy timers from this package. Before adoption, exclude all old writers and
prove coherent import/hash/alias and current-catalog recovery export. No claims,
input pin changes or live operations are included here.

P2 was accepted by the lead with both source subdeliverables committed and
quick checks green; this receipt follows the later equivalent history refresh. No active P2 source edits or shared index ownership remain.
Independent final review, longer integration/shadow checks and coordinated feature
publication are lead-owned after intended commits and quick checks are complete.
Follow-up findings remain with this package. No additional broad checks were run
while awaiting the core index window.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/)
