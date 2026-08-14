# 2026-08-14-advisories-6-12-95-5

## Repositories

- `security-advisories`
  - branch: `2026-08-14-advisories-6-12-95-5`
  - worktree:
    `worktrees/2026-08-14-advisories-6-12-95-5/security-advisories`
  - upstream default: `origin/2026-07-13-security-advisory-automation`
  - base: `ad64a0524b1e0e9e628c444340b10680d7292185`

## Status

- Active session slug matches `VPSFREE_DEV_SESSION_SLUG`.
- Canonical repositories were fetched before creating the feature worktree.
- Scope is CVE-2026-64563 only. The 19 published v2/v3-first dossiers will not
  be refreshed for cumulative v5.
- The user initially withheld publication and notification email. After the
  reviewed draft was created, they explicitly authorized publication when the
  integration is done. A separate notification email is still not authorized.

## Commands run

- `bin/dev-session current`
- fetched `security-advisories` and vpsAdminOS upstream refs;
- inspected repository guidance, prior dossiers, tests, primary CVE sources,
  current vpsAdmin/vpsAdminOS/configuration source, and the 6.12.95 live-patch
  documentation;
- `bin/dev-session worktree add ... security-advisories --base
  refs/remotes/origin/HEAD --no-fetch`.
- `nix develop --command bundle exec overcommit --install`;
- `nix develop --command bin/security-advisory collect`;
- `nix develop --command bin/security-advisory evaluate CVE-2026-64563`.
- `nix develop --command bin/security-advisory validate CVE-2026-64563`;
- `nix develop --command bundle exec rspec spec/dossiers_spec.rb`;
- `nix develop --command bundle exec rspec`;
- `nix develop --command bundle exec rubocop --parallel --force-exclusion`;
- `nix develop --command bundle exec overcommit --run`.
- committed repository guidance as `3fb8ad3b86b7fa8f64fa3d2ca2dd74f0e4e9d6a7`;
- committed the dossier and regression coverage as
  `9cc4687823fbdae2a33254738d80cd08dba8dd26`.
- requested the mandatory standalone review of base `ad64a0524` through head
  `9cc4687`, including the exact source pins, evidence digests, verification
  results, and compatibility assumptions.

## Results

- vpsAdminOS documentation identifies CVE-2026-64563 as the only CVE first
  covered by live patch v5 (`6.12.95.5`).
- The Linux CNA record changed after the planning pass. Its current data
  identifies introduction commit `5d240a8936f6`, stable fixes in 6.6.151,
  6.12.103, 6.18.42, and 7.1.6, and the mainline fix in 7.2. The implementation
  uses this current primary-source boundary and keeps only 5.10, 5.15, and 6.1
  open-ended.
- The worktree helper returned nonzero because the ambient shell lacked the
  locked Overcommit gems, but the worktree and branch were created correctly.
  This known behavior is documented in
  `notes/cross-project/2026-06-07-overcommit-worktree-add.md`. Hooks are now
  installed and active through the locked bundle. The explicit invocation is
  recorded in `notes/security-advisories/2026-08-14-overcommit-bundle-exec.md`.
- Fresh typed evidence was collected at `2026-08-14T21:03:11Z`, with node-set
  digest `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`
  and evidence digest
  `4d54daedbb91b4c16c091e2f41f9ee5cd5ff3d657bbefe13add386e47b51e5cc`.
- All 12 compute Nodes report kernel `6.12.95.5`, active `livepatch_5` version
  5, and the accepted clean vpsAdminOS revision. `CONFIG_NETLINK_DIAG=m` and
  the loaded `netlink_diag` module confirm the vulnerable interface exists.
- Evaluation completed all 13 expected Nodes: 12 mitigated, the storage Node
  not affected, no unknown Nodes. Observed transition intervals span
  2026-08-14 20:34:30 through 20:36:56 UTC.
- Dossier validation passed. Focused dossier specs passed with 7 examples;
  the full suite passed with 152 examples. RuboCop inspected 29 files without
  offenses, and all configured pre-commit hooks passed.
- The first ambient `git commit` attempt stopped before creating a commit
  because its hook could not resolve the repository-local bundle. Running Git
  inside `nix develop` supplied the intended hook environment; both commits
  then completed with mandatory hooks active. The reusable invocation is
  included in the Overcommit note named above.
- Mandatory standalone review found no Blocking or Important issues and judged
  the change safe for unpublished draft creation with the standard fresh
  evidence and readback checks. Its one Advisory noted that `analysis.md`
  linked the live-patch coverage page through mutable `staging`; the link and
  review header were pinned to reviewed vpsAdminOS commit `d61ba246`.
- The link change invalidated the dossier digest as intended. Stale evidence
  produced 12 unknown Nodes and was rejected; it was not retained. A new
  snapshot collected at `2026-08-14T21:30:35Z` has evidence digest
  `c792ad8523b3b4c9b7b744d662c0366d92233c06d3ac60e97d32e5d0a3619232`.
  Reevaluation restored the reviewed 12 mitigated and one not-affected result;
  validation and all 7 focused dossier examples passed again.
- Committed the review follow-up as
  `39b2f458eb2baf5741aed3f3b817e6e24ca01222`.
- The same mandatory reviewer completed the follow-up with no findings. The
  immutable source pin fully resolves the Advisory, the regenerated evaluation
  reproduces from fresh evidence with unchanged conclusions, and final head
  `39b2f45` is approved for unpublished draft creation.
- Feature branch `2026-08-14-advisories-6-12-95-5` was pushed at `39b2f45`.
  GitHub Actions RSpec run `31842970646` and RuboCop run `31842970615` both
  succeeded on that exact head.
- Dry-run sync proposed a new advisory with the reviewed dossier/evidence
  digests. Applied sync created unpublished vpsAdmin advisory 30 at content
  revision 13 with 12 mitigated statuses, one not affected, and
  `published_at: null`; readback produced the exact `submission.yml` baseline.
- `ready` correctly refused to proceed while the new submission baseline was
  uncommitted. The baseline was committed as
  `9f2194813ba06007ec704a74d8d3186a5c3be6a4` before the final no-write
  readiness check.
- `ready --evidence .state/evidence.json CVE-2026-64563` returned `ready: true`
  for advisory 30, content revision 13, with 13/13 complete, 12 mitigated, one
  not affected, and no blocking Nodes.
- The same mandatory reviewer checked the baseline-only commit and repeated
  the GET-only readiness check. There were no findings; the baseline is
  mechanically consistent and final head `9f21948` is safe to integrate.
- Final feature head `9f21948` was pushed. GitHub Actions RSpec run
  `31843375838` and RuboCop run `31843375785` both succeeded on the exact head.
- Created fresh integration worktree
  `worktrees/2026-08-14-advisories-6-12-95-5/integration/security-advisories`
  on branch `integration/2026-08-14-advisories-6-12-95-5`, based on the fetched
  default branch at `ad64a05`, and fast-forwarded it to `9f21948`.
- Integration verification passed: dossier validation, full RSpec (152
  examples), RuboCop (29 files), Overcommit hooks, and diff/worktree checks.
- Fast-forward pushed `9f21948` to the upstream default branch. Default-branch
  GitHub Actions RSpec run `31843758881` and RuboCop run `31843758759` both
  succeeded on that exact head.
- Final production evidence collected at `2026-08-14T21:50:34Z` had node-set
  digest `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`
  and evidence digest
  `b75fe26d3b4e07e85d8bc2709349f6f577957042a1638b2fe3cbdb65ecf5e2c7`.
  Read-only readiness remained true for advisory 30, revision 13, with 12
  mitigated Nodes, one not affected, and no blocking Nodes.
- Read-only publication preflight verified the exact committed draft baseline,
  revision 13, publication permission, and `send_mail: false`. Using the user's
  explicit approval, the exact draft was published at
  `2026-08-14T21:51:18Z`. The publication readback returned advisory 30 in
  `published` state at unchanged revision 13 with `send_mail: false`; no email
  notification was sent.

## Open questions

- None at this stage. Remote draft creation remains intentionally deferred
  until the committed dossier passes mandatory review.

## Cleanup

- Feature worktree removed; repository-local `.gems` and `.state` caches were
  removed with it.
- Integration worktree removed; its repository-local caches were removed with
  it.
- Keep local and remote feature branch refs after integration.
- Local feature branch, remote feature branch, and local integration branch
  retained as required. No branch refs were deleted.
