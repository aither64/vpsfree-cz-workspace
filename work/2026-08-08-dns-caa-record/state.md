# 2026-08-08-dns-caa-record

## Repositories

| Repository | Branch | Worktree | Base | Current head |
| --- | --- | --- | --- | --- |
| `vpsadmin` | `2026-08-08-dns-caa-record` | removed after merge | `f90895a1a301232d10d603cc3790adbe4816d143` | `63c2c44f6ca04ab958f3d72f777add389b77b162` |
| `vpsadmin-kb-captures` | `2026-08-08-dns-caa-record` | removed after merge | `3d394b377db1e57375bd1af0f8d19f9b72a1a8b3` | `fe07bdf08d371c900fdc11f87f49be2dbc839d2b` |
| `vpsfree-cz-configuration` | `2026-08-08-dns-caa-record` | removed after merge | `2051708717b170afd34820817945bf858f93bb19` | `6f7992f124656e6febf45bb10e35a5fe4276981a` |

All remotes use `git@github.com:vpsfreecz/PROJECT.git`. All three feature
branches track their same-named remote branches.

## Current status

- The vpsAdmin implementation, exact configuration-channel pin, and capture
  contract pin are fast-forwarded and pushed to all three default branches.
  Same-named feature branches are retained locally and remotely; all initiative
  and temporary merge worktrees have been removed.
- The initiative session is owned: `VPSFREE_DEV_SESSION_SLUG` and
  `bin/dev-session current` both report `2026-08-08-dns-caa-record`.
- The top-level checkout remains on `master`. Its unrelated changes are
  preserved. In particular, `dev-clusters/vpsadmin/nix/test.nix` has an
  unowned modification which changes notification-template option placement.
- The workspace VM dev cluster is stopped. It was not started because the
  shared dev-cluster tooling is dirty. Starting it would evaluate unreviewed
  work belonging to another session, contrary to the initiative plan and
  workspace isolation rules.
- The corrected Czech and English KB candidates were promoted to their real
  production page IDs and verified byte-for-byte. Direct production reads show
  only `CAA` added to each supported-record list. KB staging has no pending
  release and its ownership has been released with retained data.
- No live system was deployed. The configuration default branch now selects the
  new vpsAdmin revision for the `vpsadmin` channel.

## Implementation

- Added CAA to the internal DNS record model, API metadata, English and Czech
  locales, and the metadata-driven WebUI record-type selector.
- CAA content is normalized to `<flags> <tag> "<value>"`. Supported flags are
  `0` and `128`; supported tags are `contactemail`, `contactphone`, `iodef`,
  `issue`, `issuemail`, `issuevmc`, and `issuewild`.
- Values must be non-empty printable single-line ASCII and cannot contain
  quotes or backslashes. Canonical content is capped at 64,512 bytes so a
  rendered BIND record remains safely below its 64-KiB line limit.
- Prometheus DNS-answer matching handles both dnsruby string and array CAA
  representations. The existing generic libnodectld renderer remains
  unchanged; create, update, and delete behavior is now covered by specs.
- Runtime and WebUI tests cover CAA creation, authoritative queries, updates,
  deletion, malformed input, metadata, and the type selector.
- `bind` is declared in the libnodectld Nix development shell so the real
  `named-checkzone` maximum-length regression test is available locally and in
  GitHub Actions.

## Commands and results

- Read the top-level and all affected repository `AGENTS.md` files, the WebUI
  documentation workflow, and `skills/mandatory-change-review/SKILL.md`.
- Fetched configuration `origin/master` and created its same-slug worktree at
  `2051708717b170afd34820817945bf858f93bb19`.
- `bin/dev-session worktree add` returned exit 78 after successfully creating
  the configuration branch/worktree because its post-checkout Overcommit hook
  ran outside the Nix shell and could not load locked gems. The worktree was
  verified clean and registered. The known workaround is recorded in
  `notes/vpsfree-cz-configuration/2026-06-10-worktree-overcommit-gems.md`.
- Installed and ran vpsAdmin Overcommit hooks. The first explicit run inherited
  the root bundle through `RUBYOPT`; rerunning without `RUBYOPT` exposed the
  genuinely missing CAA locale entries. Added both locale entries, regenerated
  catalogs, and reran all hooks successfully.
- The original vpsAdmin feature commit was
  `4caf3d023c0fdc6b4c298af1d9396451dae976e1`. After `origin/master` advanced
  to `f90895a1a301232d10d603cc3790adbe4816d143`, rebased it without conflicts
  as `63c2c44f6ca04ab958f3d72f777add389b77b162`. `git range-diff` confirmed the
  feature patch was unchanged, and the remote feature branch was updated with
  an explicit force-with-lease.
- Updated `vpsfree-cz-configuration` with
  `confctl inputs channel set --commit vpsadmin vpsadmin REV`. The final
  generated commit is `6f7992f124656e6febf45bb10e35a5fe4276981a`
  (`inputs: set vpsadminServices to 63c2c44f`) and changes only `flake.lock`.
  Its full locked revision is the merged vpsAdmin head.
- Updated the capture repository's flake, lock, capture inventory, and
  navigation contract to the same SHA. `bin/check` found no navigation or
  screenshot drift. Amended and force-with-lease pushed the final pin as
  `fe07bdf08d371c900fdc11f87f49be2dbc839d2b`.
- Fetched 116 Czech and 70 English production KB pages read-only. Prepared
  guarded candidates for `navody:server:primarni_dns` and
  `manuals:server:primary_dns`. Each candidate only adds `CAA` to the existing
  supported-record list; it does not single out CAA syntax on a page which does
  not document the formats of the other record types. The one-page manifests
  are `kb-release-cs.yml` and `kb-release-en.yml`.
- After `2026-06-15-vpsadmin-events` released staging, claimed it with
  `bin/kb-stage start`. Staged and verified both corrected one-page manifests
  and their Czech/English pairing. The English pending manifest had digest
  `7e0d0af66e28b988da4f65d3cd6268a98d341a1839d057474b1ee3f64c76a685`.
- With direct user approval, promoted and production-verified English first,
  then restaged, verified, promoted, and production-verified Czech. Production
  summaries were `Document DNS CAA record support` and
  `Doplnění podpory DNS záznamů CAA`. Final direct reads found only the supported
  record-list lines, with no CAA format paragraph. Released staging ownership
  after confirming `pending_release` was null; mirrored data were retained.
- Both internal review page URLs return HTTP 200. The staging endpoints are
  HTTP-only; HTTPS is not configured for these internal names.
- The first staged candidates over-documented CAA's format while the page only
  lists supported record types. Regenerated both candidates to list `CAA` only.
  The release guard refused to overwrite the old staged Czech page because it
  was no longer a clean production mirror. Since this initiative owned the only
  staged changes, reset staging to production, re-mirrored 116 Czech pages, 70
  English pages, and 224 shared media objects, then staged and verified both
  corrected manifests. Direct staging reads show `CAA` only in the supported
  type lists; the removed explanatory text is absent.
- The workspace-wide staged whitespace check reports pre-existing trailing
  spaces and conflict-marker-like DokuWiki text in the verbatim production KB
  snapshots. Those bytes are intentionally preserved because source hashes and
  guarded promotion depend on exact content. The authored tracking files,
  manifests, and indexes pass the scoped check; the two edited candidates also
  retain inherited whitespace outside the guarded replacement.
- For each repository, fetched current `origin/master`, created a fresh
  temporary merge worktree, used `git merge --ff-only`, validated from that
  worktree, and pushed `HEAD:master`. Default heads are vpsAdmin `63c2c44f6`,
  capture `fe07bdf`, and configuration `6f7992f1`. Temporary merge branches and
  all initiative worktrees were removed; feature branches were preserved.
- Fresh vpsAdmin and configuration worktrees initially lacked their ignored
  Bundler caches. Reinitialized each documented Nix environment, reran hooks
  successfully, and only removed caches after the hook-protected push. The
  first configuration push was rejected locally by its pre-push hook after an
  early cache cleanup; no remote ref changed until the successful Nix-shell
  push.

## Mandatory change review

- Standalone fresh-context review completed after the first committed version.
- No blocking findings and no advisory findings.
- Important finding: the initially unbounded CAA value could produce a BIND
  zone line above its accepted size and make the whole zone fail to load. The
  reviewer reproduced the BIND 9.20 boundary.
- Resolution: cap canonical content at 64,512 bytes, test 64,512 as accepted
  and 64,513 as rejected at the API boundary, and validate the exact maximum
  through real `named-checkzone`. The downstream configuration and capture
  pins were regenerated after the vpsAdmin head changed.

## Validation ledger

- Ruby and Nix syntax checks passed. JavaScript syntax passed through
  `nix shell nixpkgs#nodejs -c node --check`.
- API focused specs passed, including normalization, validation, metadata,
  operations, Prometheus matching, and the 64,512/64,513-byte boundary.
- The final libnodectld DNS-zone spec passed 6 examples, including an actual
  `named-checkzone` check at the accepted maximum.
- After the vpsAdmin rebase, the focused API suite passed 94 examples and the
  libnodectld DNS-zone suite passed 6 examples. All vpsAdmin hooks passed again
  both on the feature head and in the fresh merge worktree.
- API RuboCop and libnodectld RuboCop passed. `nixfmt --check` passed for both
  touched Nix tests. `ruby tests/ci-selection-test.rb` passed 16 runs and 55
  assertions.
- All vpsAdmin Overcommit hooks passed: Nixfmt, RuboCop, API/WebUI i18n,
  migration specs, PHP CS Fixer, and commit-message hooks.
- `./test-runner.sh test dns/server-zone-lifecycle`: 1 script, 2 examples,
  0 failures, exit 0 in 719.81 seconds. An earlier misspelled
  `dns-server-zone-lifecycle` selector ran zero tests and was not counted.
- `./test-runner.sh test tasks/prometheus-export`: 1 script, 1 example,
  0 failures, exit 0 in 579.54 seconds.
- `./test-runner.sh test 'webui#networking-dns'`: 1 browser script/example,
  0 failures, exit 0 in 791.99 seconds.
- Capture `nix develop -c bin/check`: 39 controls, 29 paths, 32 capture
  concepts, 65 bindings, 9 exceptions, and 118 PNG variants valid; its test
  groups passed 8 runs/50 assertions and 7 runs/17 assertions.
- `confctl ls --tag vpsadmin` selected 17 systems. Earlier reviewed and final
  pre-rebase generations were `2026-08-09--00-10-03` and
  `2026-08-09--00-30-14`. After repinning to the rebased vpsAdmin head, all 17
  systems built as generation `2026-08-09--13-48-55`; the integrated
  configuration commit rebuilt from its fresh merge worktree as generation
  `2026-08-09--14-10-04`.
- GitHub Actions on the final vpsAdmin head: RuboCop, Webui PHPUnit, Client
  Specs, i18n health, libnodectld Specs, and the complete topic-parallel API
  matrix passed. Aggregate CI attempt 1 ran the complete 117-test selection:
  116 passed, including all three CAA-relevant DNS, Prometheus, and WebUI tests.
  `storage/backup-remote-interrupted-recv` failed before its examples because
  the services VM hit a Linux 6.18.41 module-loader page fault in
  `__execmem_cache_free`; the API then never became ready. This matches the
  known unrelated runner failure documented in
  `notes/vpsadmin/2026-07-08-ci-services-vm-kernel-oops.md`. After inspecting
  the uploaded logs, requested a failed-job-only rerun at
  https://github.com/vpsfreecz/vpsadmin/actions/runs/31281639745. Attempt 2
  completed successfully on the same final feature head.
- The intermediate libnodectld workflow failure was investigated from its
  logs: `named-checkzone` was absent from the job environment. Adding `bind`
  to the declared Nix shell fixed the environment; the final-head workflow now
  passes. Superseded aggregate CI runs were cancelled only after their head no
  longer matched the pushed branch.
- On rebased head `63c2c44f6`, GitHub Actions completed RuboCop, WebUI PHPUnit,
  Client Specs, i18n health, and libnodectld Specs successfully on both the
  feature and `master` pushes. Topic-parallel API Specs and aggregate CI were
  still running when default-branch integration and publication completed.

## Decisions and constraints

- Existing rows and transaction payloads are unchanged. New APIs work with
  old libnodectld through the existing generic renderer; no database migration,
  generated-client update, vpsAdminOS change, or coordinated DNS-node rollout
  is needed.
- Old API versions can still load and serve persisted CAA rows after rollback,
  but cannot validate edits. Remove CAA rows or roll forward before a planned
  API downgrade.
- Configuration `master` now receives the exact merged vpsAdmin SHA through
  the `vpsadmin` channel. No live confctl deploy was attempted.
- The intended development deployment is the single workspace VM topology on
  bridge networking, left running after its smoke test. Do not start it while
  shared dev-cluster tooling contains unresolved unowned changes; do not modify
  or revert those changes.
- The user's merge-and-publish request directly authorized the two guarded
  production KB writes. No other production writes were made.

## Remaining work and cleanup

- Dev-cluster deployment and live UI/API/DNS smoke testing are blocked by the
  unrelated dirty shared launcher file described above.
- GitHub topic-parallel API Specs and aggregate CI for the rebased feature and
  `master` pushes remain to be observed to completion.
- Repository and KB publication cleanup is complete: no initiative worktrees
  remain, feature branches are retained, and staging ownership is released.
