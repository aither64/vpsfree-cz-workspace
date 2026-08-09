# 2026-08-08-dns-caa-record

## Repositories

| Repository | Branch | Worktree | Base | Current head |
| --- | --- | --- | --- | --- |
| `vpsadmin` | `2026-08-08-dns-caa-record` | `worktrees/2026-08-08-dns-caa-record/vpsadmin` | `c0d87bebf36c6d29b7861990890e8c650fa1afca` | `4caf3d023c0fdc6b4c298af1d9396451dae976e1` |
| `vpsadmin-kb-captures` | `2026-08-08-dns-caa-record` | `worktrees/2026-08-08-dns-caa-record/vpsadmin-kb-captures` | `3d394b377db1e57375bd1af0f8d19f9b72a1a8b3` | `24cae14e916d1f90996b90c98c7bc1090e914e00` |
| `vpsfree-cz-configuration` | `2026-08-08-dns-caa-record` | `worktrees/2026-08-08-dns-caa-record/vpsfree-cz-configuration` | `2051708717b170afd34820817945bf858f93bb19` | `8bd17074060bec81e2adefcaae1e5f383511cffa` |

All remotes use `git@github.com:vpsfreecz/PROJECT.git`. All three feature
branches track their same-named remote branches.

## Current status

- The vpsAdmin implementation, exact configuration-channel pin, and capture
  contract pin are committed and pushed.
- The initiative session is owned: `VPSFREE_DEV_SESSION_SLUG` and
  `bin/dev-session current` both report `2026-08-08-dns-caa-record`.
- The top-level checkout remains on `master`. Its unrelated changes are
  preserved. In particular, `dev-clusters/vpsadmin/nix/test.nix` has an
  unowned modification which changes notification-template option placement.
- The workspace VM dev cluster is stopped. It was not started because the
  shared dev-cluster tooling is dirty. Starting it would evaluate unreviewed
  work belonging to another session, contrary to the initiative plan and
  workspace isolation rules.
- Validated Czech and English KB candidates are staged at their real page IDs.
  The staging container is running and owned by this initiative. Both pages and
  their language pairing were verified; the English manifest is the current
  pending promotion guard.
- No live system was deployed and no production KB page was written.

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
- Committed and pushed vpsAdmin as
  `4caf3d023c0fdc6b4c298af1d9396451dae976e1` (`api: add CAA records to
  internal DNS zones`).
- Updated `vpsfree-cz-configuration` with
  `confctl inputs channel set --commit vpsadmin vpsadmin REV`. The final
  generated commit is `8bd17074060bec81e2adefcaae1e5f383511cffa`
  (`inputs: set vpsadminServices to 4caf3d02`) and changes only `flake.lock`.
  Its full locked revision is the final vpsAdmin head.
- Updated the capture repository's flake, lock, capture inventory, and
  navigation contract to the same SHA. `bin/check` found no navigation or
  screenshot drift. Committed and pushed as
  `24cae14e916d1f90996b90c98c7bc1090e914e00`.
- Fetched 116 Czech and 70 English production KB pages read-only. Prepared
  guarded candidates for `navody:server:primarni_dns` and
  `manuals:server:primary_dns`, documenting CAA syntax, flags, and tags. The
  one-page manifests are `kb-release-cs.yml` and `kb-release-en.yml`.
- After `2026-06-15-vpsadmin-events` released staging, claimed it with
  `bin/kb-stage start`. Staged and verified the Czech manifest, then staged and
  verified the English manifest and re-verified Czech. Both one-page candidates
  and the single Czech/English pair passed. The container remains running and
  owned by `2026-08-08-dns-caa-record`.
- The release tool maintains one pending manifest. The English manifest is
  pending with digest
  `8c3443c96bca1e73d7580b4b8614a2a72b0198c7e0ea64dbbf227a5c34b380e9`;
  both language pages remain staged for review. If production publication is
  later approved, promote English first, then restage, verify, and promote
  Czech. No production write was attempted.
- Both internal review page URLs return HTTP 200. The staging endpoints are
  HTTP-only; HTTPS is not configured for these internal names.
- The workspace-wide staged whitespace check reports pre-existing trailing
  spaces and conflict-marker-like DokuWiki text in the verbatim production KB
  snapshots. Those bytes are intentionally preserved because source hashes and
  guarded promotion depend on exact content. The authored tracking files,
  manifests, and indexes pass the scoped check; the two edited candidates also
  retain inherited whitespace outside the guarded replacement.

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
- `confctl ls --tag vpsadmin` selected 17 systems. A full build on the
  intermediate reviewed SHA succeeded as generation
  `2026-08-09--00-10-03`. A second full build against the exact final SHA
  succeeded for all 17 systems as generation `2026-08-09--00-30-14`.
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
  https://github.com/vpsfreecz/vpsadmin/actions/runs/31281639745. Attempt 2 is
  in progress on the same final feature head.
- The intermediate libnodectld workflow failure was investigated from its
  logs: `named-checkzone` was absent from the job environment. Adding `bind`
  to the declared Nix shell fixed the environment; the final-head workflow now
  passes. Superseded aggregate CI runs were cancelled only after their head no
  longer matched the pushed branch.

## Decisions and constraints

- Existing rows and transaction payloads are unchanged. New APIs work with
  old libnodectld through the existing generic renderer; no database migration,
  generated-client update, vpsAdminOS change, or coordinated DNS-node rollout
  is needed.
- Old API versions can still load and serve persisted CAA rows after rollback,
  but cannot validate edits. Remove CAA rows or roll forward before a planned
  API downgrade.
- Configuration receives the exact reviewed feature SHA on its feature branch
  only. Configuration `master` was not integrated and no live confctl deploy
  was attempted.
- The intended development deployment is the single workspace VM topology on
  bridge networking, left running after its smoke test. Do not start it while
  shared dev-cluster tooling contains unresolved unowned changes; do not modify
  or revert those changes.
- No production KB write is authorized.

## Remaining work and cleanup

- Monitor aggregate CI attempt 2. Attempt 1's sole failure was investigated and
  identified as an unrelated early services-VM kernel Oops; do not treat a
  green rerun as replacing that diagnosis.
- Dev-cluster deployment and live UI/API/DNS smoke testing are blocked by the
  unrelated dirty shared launcher file described above.
- Review the staged Czech page at
  `http://kb-cs.aitherdev.int.vpsfree.cz/doku.php?id=navody:server:primarni_dns`
  and English page at
  `http://kb-en.aitherdev.int.vpsfree.cz/doku.php?id=manuals:server:primary_dns`.
  Production promotion still requires direct user approval.
- Keep KB staging claimed while the pending release is under review. Release
  without discarding only after pending promotion is complete; discarding it
  requires an explicit cleanup decision.
- Keep worktrees and feature branches until the work is merged or abandoned.
  Remove worktrees after completion but retain branch refs unless explicitly
  asked to delete them.
