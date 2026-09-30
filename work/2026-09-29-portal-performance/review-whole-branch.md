# Whole-branch readiness review

## Requested outcome

Review the complete final history and final diff for the portal-performance
initiative before the user-authorized fast-forward integration to each
repository's `master`. Determine whether the implementation is correct,
proportionate, compatible, recoverable and ready to merge. Explicitly conclude
whether obsolete branch history, transitional behavior, unused compatibility
paths or migrations remain.

Acceptance requires:

- large conversations render through paged transcript reads instead of loading
  the full rollout before first paint;
- automatic archive eligibility observes Codex state without holding the
  exclusive transition lock across the workspace scan;
- interrupted retained-team archive journals can be completed safely and
  idempotently without replacing or reviving retained threads;
- aitherdev portal authentication uses the reviewed lower bcrypt cost while the
  generic host-module default remains 12 and the existing random password is
  retained;
- initial session HTML does not synchronously perform live repository
  discovery, while the established details refresh still reports discovery
  warnings, including for a mounted review panel;
- 30 authenticated no-scan loads and 30 loads overlapping a dry-run archive
  scan each have p95 usable time at or below two seconds, no failed loads,
  paged responses and zero legacy transcript responses;
- all five final branches have coherent history and no unresolved migration or
  mixed-version issue.

## Scope and records

- Initiative: `2026-09-29-portal-performance`
- Plan: `work/2026-09-29-portal-performance/plan.md`
- Design and verification brief: `work/2026-09-29-portal-performance/design.md`
- Current state and evidence index: `work/2026-09-29-portal-performance/state.md`
- Deployment/recovery record: `work/2026-09-29-portal-performance/rollout.md`
- Branch in every repository: `2026-09-29-portal-performance`
- User decision: integrate the final reviewed heads to each repository's
  `master`. Do not archive, delete or stop this session.

## Risk and lanes

- Overall risk: **High**. The change affects authentication cost, host
  configuration and deployment, destructive archive recovery, transition-lock
  behavior, a cross-project Go/Nix dependency chain, and browser transcript
  compatibility.
- Review lanes: General; Architecture and repetition; Scope and
  proportionality; Risk and compatibility.
- Reviewer: retained `reviewer0`, saved purpose `review`, read-only access,
  `gpt-6-sol` with `xhigh` effort. Do not override model or effort.
- Required workflow:
  `~/.codex/skills/mandatory-change-review/SKILL.md` and all four lane
  references under its `references/` directory.

## Final branches and complete commit series

### `codex-web`

- Worktree: `worktrees/2026-09-29-portal-performance/codex-web`
- Base: `e92dd887c888d5a9f50c70febc714f875cb44378`
- Head: `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`
- Remote `master` equals the base; the worktree is clean.
- Commits, oldest first:
  1. `0fad2e12e4156f512f1642222e065cabc0da72a7` — `codex: page transcripts without loading full turns`
  2. `f16fcff6fa9a5476545c98b50ecf1c2db04bf602` — `browser: page mounted conversations incrementally`
  3. `d210d3f7cc93981d0ab163b1fcf0718f9587f47e` — `browser: invalidate stale history reads after full replacement`
- Final diff: 12 files, 2,855 insertions and 85 deletions. It adds the optional
  transcript-page reader and HTTP endpoint, bounded background rollout metadata
  enrichment, browser paging/replacement behavior, protocol corpus coverage and
  reference documentation.

### `dev-workspace`

- Worktree: `worktrees/2026-09-29-portal-performance/dev-workspace`
- Base: `3b570f0a8b75d809a2753177590158e9dc4639f1`
- Head: `d20bb64c45db1d803fc3b7a8c2956049860d72dd`
- Remote `master` equals the base; the worktree is clean.
- Commits, oldest first:
  1. `7afe780f929773727693184c0c302f5340d61b2b` — `flake: select paged Codex conversation client`
  2. `38cc1220092d58ae0bcdb1f6a4a377a818fad6d7` — `portal: page large conversations incrementally`
  3. `9e25870d143f28c2e37763a5e6fd526dad1c9df5` — `session: observe automatic archives without exclusive locks`
  4. `9b54f7b46cd37fdd36679e619616ebd995f43be6` — `portal: preserve legacy transcript view on refresh`
  5. `67246cf25a40ad5029121b75c99f24434bf86d36` — `portal: track output across sliding legacy windows`
  6. `87430b813cb0e0017e844711e60f4b34a7c32513` — `portal: pin corrected codex-web history module`
  7. `9d48fc795de12f7725b0995d336c323c474c25e0` — `nix: validate the selected codex-web module pin`
  8. `9db7bc844a0332b7e00d21536c3bebf835928ece` — `nix: require the exact codex-web pseudo-version`
  9. `4999212df75216ccf93c010caecad46fc39c8061` — `session: recover archived threads without history scans`
  10. `fbd7a9e390b563f83d1787e2cddbd516eefeb558` — `session: preserve root archive retirement guards`
  11. `e58f8f61ce43058aba49361a0b3bd1ecd98af866` — `session: accept retained ready creation records`
  12. `b36691d52790dffb5e104900343dca7f841e55e6` — `session: recover partially archived retained teams`
  13. `47716d9e846b10698476728386b65b689abf8476` — `archive: verify packaged recovery and archived team members`
  14. `b9465ab61dfc4e9820e312b062cb7b96ed3f09b0` — `archive: load the packaged Ruby recovery verifier`
  15. `ec05cb9f008cc8d6bccfd23e9b15a69d9a66fa40` — `host: make portal bcrypt cost configurable`
  16. `d20bb64c45db1d803fc3b7a8c2956049860d72dd` — `portal: defer live repository discovery`
- Final diff: 45 files, 3,790 insertions and 372 deletions. It includes the
  paged portal consumer, passive auto-archive observation, guarded retained-only
  recovery, bounded host auth cost, deferred repository discovery, tests and
  durable operator documentation.

### `vpsfree-dev-workspace`

- Worktree: `worktrees/2026-09-29-portal-performance/vpsfree-dev-workspace`
- Base: `bd961682cecb0b3b2bf729a53d2e08bda3d48eb2`
- Head: `6a0a2eb873e7cb376092c74bdf82fc2c51c349da`
- Remote `master` equals the base; the worktree is clean.
- Commit: `6a0a2eb873e7cb376092c74bdf82fc2c51c349da` —
  `nix: pin the updated workspace runtime`.
- Final diff: `flake.nix` and `flake.lock`, 9 insertions and 9 deletions. Five
  successive development pins were consolidated before this review; the final
  tree is byte-identical to previously tested `c69343869c6f58e0c1585dc6784e771034e915d3`.

### Coordination workspace package

- Worktree: `worktrees/2026-09-29-portal-performance/workspace`
- Integration base: shared coordination `master`
  `1d04e6f35cdf966e7cc958e4f63d01a776356a4a`; the branch was cleanly rebased
  from recorded initial base `979ef666099a678b7738826169e7fa6cf0a2f1a7`.
- Head: `c3944c68e7efc29de9219862074defe8d6547ebc`
- Commit: `c3944c68e7efc29de9219862074defe8d6547ebc` —
  `flake: pin portal performance runtime`.
- Final feature diff against shared `master`: `flake.nix` and `flake.lock` only.
  Five successive package pins were consolidated before this review. The
  shared `master` commits absent from remote `master` change only `work/`,
  `archive/` and `notes/`; they are coordination records, not feature content.
- The final lock chain is extension `6a0a2eb873e7cb376092c74bdf82fc2c51c349da`
  -> dev-workspace `d20bb64c45db1d803fc3b7a8c2956049860d72dd`
  -> codex-web `d210d3f7cc93981d0ab163b1fcf0718f9587f47e`.

### `vpsfree-cz-configuration`

- Worktree: `worktrees/2026-09-29-portal-performance/vpsfree-cz-configuration`
- Base: `6c827ca2c1b18fe79171ecc8fea03ad80b803f82`
- Head: `bfb7b883f02df270cb93fb984793ef287c191b5a`
- Remote `master` equals the base; the worktree is clean.
- Commits, oldest first:
  1. `523142465afb652cf9308c16fe34189b914d0356` — `inputs: set devWorkspace to ec05cb9f`
  2. `bfb7b883f02df270cb93fb984793ef287c191b5a` — `aitherdev: reduce workspace portal bcrypt cost`
- Final diff: the dev-workspace lock pin and one aitherdev-only module option.
  The pin intentionally stops at `ec05cb9f...`: this system configuration
  consumes the host module and auth option, while the separately switched user
  profile consumes final application head `d20bb64c...`.

## History disposition

- The repeated pin-only histories in `vpsfree-dev-workspace` and the consuming
  workspace were consolidated to one final commit each. Final trees and Nix
  source hashes are unchanged; the exact package derivation remains
  `/nix/store/9maspddjxs6v4j9ffl0wqkgzv89mfi9s-dev-workspace-0.2.0.drv` and the
  output remains `/nix/store/5dzn1p13lcqfgp6lqdii20swa0v3346g-dev-workspace-0.2.0`.
- `codex-web` commits remain separate provider, browser-consumer and replacement
  invalidation units. The last unit is active final behavior, not a discarded
  approach.
- `dev-workspace` follow-up commits remain because they are distinct tested
  compatibility or safety units: legacy transcript refresh, sliding legacy
  output, exact pin validation, root retirement guards, ready-record proof,
  partial-team recovery proof, packaged verifier loading, host authentication
  and initial-render discovery. Several exact intermediate heads were built,
  exercised by CI, deployed as forward recovery packages or used to complete
  authorized archive journals. No removed design, dead dual path or unused
  branch-only migration is known. The reviewer must independently confirm that
  this separation is coherent and that no fix should instead be folded.
- Configuration keeps dependency pinning and aitherdev policy separate so the
  site cost can be reverted independently while retaining the module support.

## Migration inventory and provenance

There are **no database, schema, seed, persisted-format, API-version, protocol-
version or generated-client migrations** in any repository. No migration was
merged, released or externally consumed. The disposable rollout metadata cache
is explicitly non-authoritative and rebuildable. Archive recovery consumes
existing schema-1 journals and retained creation records without changing their
formats. The bcrypt deployment regenerates the htpasswd hash from the unchanged
password and is reversible by restoring cost 12 and switching configuration.

## Compatibility, deployment and recovery

- The transcript-page capability is optional; old portal consumers keep the
  legacy `/thread` behavior, while the new portal detects paging support.
- Browser replacement generations invalidate stale in-flight reads. Legacy
  recent-window output handling remains covered for mixed portal/provider
  behavior.
- Rollout metadata enriches display only, expires after 60 seconds and cannot
  authorize mutations. Server-side mutation checks remain authoritative.
- Automatic archive scans observe under shared locks, then reacquire exclusive
  locks and recheck all eligibility immediately before mutation.
- Recovery is journal-, generation-, retained-ID-, cwd-, project- and rollout-
  header-bound; malformed or conflicting state fails closed. It cannot create,
  replace, revive or adopt a member.
- The generic nginx bcrypt cost default is unchanged at 12. Only aitherdev sets
  cost 5 for a generated 64-hex-character credential. Rollback regenerates the
  hash from the same root-owned password.
- Configuration generation `2026-09-30--04-04-18` is active. The exact cost,
  ownership/mode, correct and wrong password behavior, HTTP 401/200 behavior,
  reconciler idempotence and five verification batches passed.
- The selected user profile is generation 73 with package
  `/nix/store/5dzn1p13lcqfgp6lqdii20swa0v3346g-dev-workspace-0.2.0`. Pin-history
  consolidation produces the same derivation and output, so no profile switch
  or system deployment is needed for the rewritten commit identities.

## Quick and longer verification evidence

- All worktrees are clean; `git diff --check` passes.
- Codex-web focused Go, Node/browser-contract, protocol-corpus, formatting and
  GitHub Actions checks passed at final head `d210d3f7...` (run `36620678434`).
- Dev-workspace focused Go/Node/Ruby/Nix/format checks passed. Full package
  verification passed, the host idempotency VM passed, and GitHub Actions passed
  final head `d20bb64...` (run `36661739189`).
- The pre-consolidation extension tree passed GitHub Actions run `36662350029`;
  the final consolidated head has the identical tree and a fresh flake
  evaluation passes.
- The final workspace head passes `nix flake check --no-build`, resolves the
  exact three-repository chain above and builds from cache to the unchanged
  exact package output.
- Configuration evaluation, formatting, lock proof, consuming system build,
  dry activation, system switch and post-switch authentication checks passed.
- Final no-scan browser gate: 30/30 successful, p95 usable 1.617 seconds, 34
  paged responses, zero legacy and zero HTTP errors.
- Final overlap browser gate after a seed plus 65-second metadata expiry: 30/30
  successful, p95 usable 1.558 seconds, 35 paged responses, zero legacy and one
  incidental HTTP error. The dry-run archive scan exited zero in about 14.3
  seconds and the browser process remained active at both scan start and end.

## Ownership and consumers

- `codex-web` owns Codex protocol reads, optional transcript paging and browser
  transcript mechanics.
- Generic `dev-workspace` owns session lifecycle/locking, portal composition,
  host-module authentication and the `codex-web` pin.
- `vpsfree-dev-workspace` is the vpsFree.cz extension and direct consumer of
  generic `dev-workspace`.
- The coordination workspace flake is the aitherdev user-profile consumer of
  the extension.
- `vpsfree-cz-configuration` consumes only the generic host module revision
  containing the bcrypt option and owns the aitherdev site override.

## Non-goals and residual risks

- No Codex version update, state-database edit, rollout rewrite, manual htpasswd
  edit, password rotation, archive-policy change or session archival is in
  scope.
- This does not identify a separate historical transition-lock holder; the
  confirmed old scan contention is fixed by bounded observation and recheck.
- The 4 KiB rollout-tail probe is best effort until the non-renewable 60-second
  rebuild; display metadata is not mutation authority.
- One overlap run counted a single incidental HTTP error response but had no
  failed load, page exception, legacy transcript response or gate violation.
