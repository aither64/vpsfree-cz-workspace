# 2026-07-10-kb-czech-fixes

## Repositories

- Coordination workspace:
  `/home/aither/workspace/ai/vpsfree.cz`
  - Shared branch: `master`
  - Initiative: `2026-07-10-kb-czech-fixes`
- `vpsadmin`:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git`
  - Authority ref: `origin/master`
  - Authority commit:
    `299147166ecb8459c712ed8a5c4dd14f673663fc`
  - Feature branch: `2026-07-10-kb-czech-fixes`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-10-kb-czech-fixes/vpsadmin`
- `vpsfree-sms-gateway` (historical read-only input from the first cluster
  attempt; no longer used by the capture repository):
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-sms-gateway.git`
  - Authority ref: `origin/2026-06-15-vpsadmin-events`
  - Authority commit:
    `af7b3faf`
  - Feature branch: `2026-07-10-kb-czech-fixes`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-10-kb-czech-fixes/vpsfree-sms-gateway`
- `vpsadmin-kb-captures`:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-kb-captures.git`
  - Feature branch: `2026-07-10-kb-czech-fixes`
  - Worktree:
    `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-07-10-kb-czech-fixes/vpsadmin-kb-captures`
  - Commits:
    - `838b3ef` (`captures: add standalone reproducible screenshot framework`)
    - `af5525e` (`captures: add Czech vpsAdmin screenshot inventory`)
  - SSH remote:
    `git@github.com:vpsfreecz/vpsadmin-kb-captures.git`
  - GitHub repository created by the user:
    `https://github.com/vpsfreecz/vpsadmin-kb-captures`
- `haveapi` (read-only background):
  `/home/aither/workspace/ai/vpsfree.cz/repos/haveapi.git`
  - Inspected current `origin/master`:
    `350547447ba42dfa765e09c762dd916ad0acce03`

## Status

- The mandatory-review findings have been corrected. The standalone cluster,
  fixture setup, complete 60-image capture, strict validation, and visual
  review all pass. Draft staging is complete.
- Detailed audit written to `kb-label-audit.md`.
- Added create-only DokuWiki media operations to `bin/kb-page` and committed
  them on the coordination workspace `master` as `5e2b40b`.
- Preparation tooling is committed separately on coordination workspace
  `master` as `2b6f7ea`; the reusable dev-cluster note is `b06f2f3`; the audit,
  exact source snapshots, complete previews, migration manifest, and
  synchronized screenshots are committed as `e3ae318`.
- A disposable draft media upload was written, downloaded byte-for-byte, and
  deleted. No smoke-check media remains on the wiki.
- Created 30 review pages and 60 media assets under
  `drafts:2026-07-10-kb-czech-fixes` using create-only writes. The review entry
  page is
  `https://kb.vpsfree.cz/drafts:2026-07-10-kb-czech-fixes:domu`.
- Read every draft page and media asset back through the API. All 30 page
  sources match the local previews byte-for-byte and all 60 media SHA-256
  hashes match the manifest.
- Non-draft publication remains subject to explicit user approval.
- All 60 Czech screenshot assets are generated and tracked in the standalone
  repository. The inventory maps 63 page references to exact scenario
  checkpoints and stable semantic draft/permanent media IDs.
- The user chose stable semantic screenshot names without order or revision
  suffixes. Git and DokuWiki will retain revisions of canonical media IDs.
- The user also required the capture repository to own its complete dev-cluster
  lifecycle and fixture setup with no runtime coordination-repository
  dependency. The repository now vendors and adapts the cluster definition,
  pins upstream inputs in `flake.lock`, and has passed a fresh acceptance run.
- The capture feature branch was pushed to
  `origin/2026-07-10-kb-czech-fixes`.

## Commands run

- `bin/dev-session current` and environment verification.
- `bin/kb-page whoami --wiki cz`.
- Read-only DokuWiki JSON-RPC through the `bin/kb-page` client:
  - `core.listPages` with namespace `""` and depth `10`;
  - `core.getPage` for every returned page;
  - `core.listMedia` with depth `10`;
  - selected `core.getMediaInfo` checks.
- `git -C repos/vpsadmin.git fetch --prune origin`.
- Created the initiative vpsAdmin worktree from the user's updated
  `origin/master` at `299147166ecb8459c712ed8a5c4dd14f673663fc`.
- `git -C repos/haveapi.git fetch --prune origin`.
- Read vpsAdmin `AGENTS.md`, `doc/i18n-cs.md`, WebUI PO/POT catalogs,
  API English/Czech YAML catalogs, and relevant WebUI source at the authority
  commit.
- Compared KB text to flattened WebUI and API English/Czech label pairs, then
  manually reviewed navigation-shaped and emphasized text.
- `ruby -c bin/kb-page`.
- `ruby test/kb_page_test.rb`: 25 runs, 104 assertions, 0 failures, 0 errors.
- Draft media smoke check using `media-save --create`, `media-info`,
  `media-get`, SHA-256 comparison, and `media-delete`.
- Started the standalone repository's single-node dev cluster with local
  networking. Local networking was used because another initiative owns the
  one VPN-visible bridge-cluster slot.
- Created a local canonical bare `vpsadmin-kb-captures` repository and feature
  worktree, then connected the user-created GitHub repository over SSH.
- Pinned the Nix development shell and Playwright browser in `flake.lock`.
- Ran the complete capture command against vpsAdmin commit
  `299147166ecb8459c712ed8a5c4dd14f673663fc`.
- Ran `bin/validate --update`, strict `bin/validate`, JavaScript syntax checks,
  Ruby syntax checks, and `bin/check`.
- Ran the mandatory standalone change review. It found four blocking areas:
  console readiness accepted a service banner, CLI traffic output had no
  finite row, fixtures reused arbitrary cluster objects/dynamic dates, and one
  coordination commit mixed tooling with the generated review bundle. It also
  requested stronger result/immutability validation and resolution of six
  exact duplicate-image groups.
- Regenerated the standalone flake lock with vpsAdmin pinned at
  `299147166ecb8459c712ed8a5c4dd14f673663fc` and successfully evaluated the
  repository-owned cluster outputs with `nix flake show --impure`.
- Ran `bin/devcluster refresh kb-captures` against the repository-owned cluster
  after adding its osctld socket and pool readiness checks.
- Ran `bin/capture --cluster kb-captures --language cs`; all 60 checkpoints
  completed in one process.
- Ran `bin/validate --update`, `nix develop -c bin/check`, and
  `git diff 4f6a144..HEAD --check`; all passed.
- Generated and visually inspected contact sheets for all eight scenarios.
- Pushed the two capture commits to
  `origin/2026-07-10-kb-czech-fixes`.
- Rechecked all 30 live source pages immediately before draft creation; their
  revisions and byte-exact content still matched the recorded snapshots.
- Verified identity, create ACL, and nonexistence for the exact 30 page and 60
  media draft targets.
- Uploaded all 60 draft media objects with `bin/kb-page media-save --create`,
  followed by all 30 pages with `bin/kb-page save --create`.
- Read all 30 pages back and compared their bytes, then read all 60 media
  objects back and compared their SHA-256 hashes.
- Fetched all 30 public draft renders, confirmed all 63 expected embeds and no
  legacy screenshot references, and fetched all 60 unique rendered PNG URLs.
  The first URL check retained HTML-encoded `&amp;` query separators and received
  HTTP 412 for resized images; decoding the extracted HTML URL fixed the test.
  The reusable lesson is recorded in
  `notes/cross-project/2026-07-10-dokuwiki-rendered-media-url.md`.
- Stopped the standalone `kb-captures` dev cluster after verification.
- Re-ran the three coordination generators and confirmed the complete review
  bundle remained unchanged.
- Re-ran `ruby test/kb_page_test.rb`: 25 runs, 104 assertions, no failures.
- Re-ran `nix develop -c bin/check` in `vpsadmin-kb-captures`: 60 assets, 63
  references, and 60 PNGs; syntax and inventory checks passed.

## Results

- Accessible page inventory: 116 pages.
  - 6 root pages
  - 1 draft page
  - 32 `informace` pages
  - 63 `navody` pages
  - 3 `private` pages
  - 5 `uzivatele` pages
  - 6 `wiki` pages
- Pages requiring draft copies for text and/or screenshot work: 30.
- Pages with no direct text or screenshot work in this initiative: 86.
- Screenshot work: 63 affected references to 60 unique media files across
  18 pages. Their revisions range from 2014-10-29 through 2025-03-16.
- The exact mapping, page locations, screenshot list, intentional exceptions,
  and no-change page coverage are recorded in `kb-label-audit.md`.
- Screenshot feasibility check:
  - the initiative single-node dev cluster ran with the expected WebUI/API
    hostnames;
  - the host has about 395 GiB of free disk and 72 GiB of available memory,
    which is sufficient for the services VM, one node, and headless Chromium;
  - vpsAdmin's Playwright suite provided patterns for login, Czech language
    switching, and page helpers; the standalone repository now supplies the
    dedicated deterministic KB scenarios and viewport/crop conventions;
  - another initiative's bridge dev cluster
    (`2026-07-02-haveapi-i18n`) is currently running. The dev-cluster tooling
    allows only one VPN-visible bridge cluster at a time. This initiative uses
    local networking to avoid changing or stopping the other session's
    cluster; this is the recorded reason for departing from the bridge default.
- The first coordination-workspace cluster evaluation failed because its
  dev-cluster flake references
  the private `vpsfree-sms-gateway` repository with a `github:` input, which
  returned an unauthenticated 404. An isolated worktree temporarily supplied
  that input as a local path. The standalone capture repository eliminated
  this runtime dependency. The original workaround is recorded in
  `notes/cross-project/2026-07-10-devcluster-private-github-input.md`.
- Reproducible screenshot repository result:
  - 60 manifest assets and 63 source-page references;
  - eight scenarios: getting started, networking, storage, console,
    VPS management, Playground, environments, and account;
  - 54 WebUI assets, five live-console assets, and one real CLI asset;
  - deterministic fixtures for two VPSes, a snapshot, public key, traffic,
    NixOS generation metadata, and an unconfirmed TOTP device;
  - 60 PNGs with dimensions, SHA-256, sanitized route provenance, and the
    current vpsAdmin commit;
  - the acceptance run completed all 60 checkpoints in one process and strict
    validation passed.
- Mandatory-review resolutions:
  - console checkpoints wait for guest-specific Alpine/OpenRC/login output,
    rather than accepting a remote-console service banner;
  - the CLI checkpoint validates a real finite traffic row for the fixture VPS
    and its actual network interface before rendering stable documentation
    output;
  - fixtures identify and recreate only their own labeled objects, reject
    duplicates, and normalize dates and volatile counters;
  - validation binds every result to its exact scenario, checkpoint, driver,
    output path, and SHA-256, while protecting accepted assets from mutation;
  - the six duplicate-image groups were replaced with distinct checkpoint
    captures, and strict validation rejects any duplicate PNG hashes;
  - the coordination history is split into tooling, durable note, generated
    review bundle, and state commits.
- Draft result:
  - 30 complete Czech review pages;
  - 60 new semantic Czech media IDs and 63 embedded image references;
  - no production page or legacy media write;
  - byte-for-byte page verification, SHA-256 media verification, and rendered
    page/media checks passed.

## Open questions

- Before publication, decide whether to modernize the old Slovak article
  `navody:vps:obnova_webu_zo_zalohy` beyond its UI labels. The current plan
  deliberately limits that page to localization/navigation corrections and
  screenshot recapture.
- The current WebUI catalog translates the mount toggle button `Enable` as
  `Zapnuto`. The plan avoids turning that odd button text into prose by
  describing the operation naturally while retaining the exact UI labels only
  where necessary.
- No publication naming decision remains: draft and permanent screenshot IDs
  use functional-topic, language, and semantic-view components. English
  variants will reuse the same topic/view structure in the `en` namespace.
- The standalone GitHub repository and its corrected feature branch are ready
  for review.

## Cleanup

- The standalone initiative dev cluster has been stopped.
- The three initiative worktrees (`vpsadmin`, `vpsfree-sms-gateway`, and
  `vpsadmin-kb-captures`) remain in use.
- Temporary capture credentials, console tokens, raw terminal streams, fixture
  state, and contact sheets are under the ignored `tmp/` directory in the
  capture worktree and are not committed.
- The 30 review pages and 60 review media assets remain in the draft namespace
  for user review.
