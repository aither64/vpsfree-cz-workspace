# 2026-08-07-security-advisories-6-12-95-2

## Repositories

- `security-advisories`
  - branch: `2026-08-07-security-advisories-6-12-95-2`
  - worktree:
    `worktrees/2026-08-07-security-advisories-6-12-95-2/security-advisories`
  - upstream default: `origin/2026-07-13-security-advisory-automation`
  - rebased base: `7cb4fb19253c853f720520dee37698c71def2189`

## Status

- Active session slug matches `VPSFREE_DEV_SESSION_SLUG`.
- The feature branch was fetched and rebased on the current default branch.
  Obsolete evidence-support commit `e99c446` was dropped because the default
  branch already contains the deployed typed kernel-history implementation.
- The original 14 dossiers now accept exact cumulative v2, v3, and v4 active
  identities. Their public responses identify patch 6.12.95.2 as the first fix
  and patch 6.12.95.4 as the cumulative patch that currently carries it.
- Five new dossiers are committed separately for CVE-2026-46093,
  CVE-2026-64551, CVE-2026-64561, CVE-2026-64562, and CVE-2026-68480.
- The five new dossiers identify patch 6.12.95.3 as the first fix and corrected
  cumulative patch 6.12.95.4 as the active replacement.
- Repository instructions and regression coverage now model reboot boundaries,
  effective patch removal, accepted cumulative replacement, internal inventory
  events, and the distinction between security-fix correctness and activation
  safety.
- Fresh evaluation resolves every dossier as 12 `mitigated`, one
  `not_affected`, and zero blocking nodes.
- Publication and merge approval has been withdrawn. Only unpublished draft
  synchronization is authorized.
- Mandatory standalone review passed after both Important findings were fixed.
  Later draft reconciliation exposed two evidence-history issues: the deployed
  coverage watermark changes on every observation, and internal inventory
  observations can omit unchanged patch metadata. Both fixes are committed;
  the same reviewer confirmed the cumulative-transition correction with no
  remaining finding.

## Reviewed source identities

- security-advisories base:
  `7cb4fb19253c853f720520dee37698c71def2189`
- vpsAdmin: `63c2c44f6ca04ab958f3d72f777add389b77b162`
- deployed vpsAdmin kernel-history contract:
  `988ce4a0d1c0bbbe495963c5e8e3ed2190eaba1d`
- vpsAdminOS: `837baf04054c6ee0e71d288b8870ac42a6990c38`
- production configuration:
  `6f7992f124656e6febf45bb10e35a5fe4276981a`
- boot-kernel source:
  `a2384967b90f24d2470c9eb15f0e66d938df7e08`
- v3 live-patch delivery source:
  `7ebdba98330ffa65ce536dd810c307ad198c0f69`
- corrected v4 vpsAdminOS commit:
  `89773cc3af15dc280935fbac8f20c2d8e1cc2a98`
- deployed v4 vpsAdminOS revision:
  `02dfcc956bff56a2fb3dbce734dba259b9dfb123`

## Evidence and results

- Final corrected evidence collected at `2026-08-09T17:09:32Z`:
  - source generated during the same coherent collection;
  - node-set digest:
    `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`;
  - evidence digest:
    `8f9cd6f617c73fa761489860bcc1e3bd1daa2ef7d3e138e0b471b957f7b5873d`.
- Corrected evidence collected at `2026-08-09T15:32:45Z`:
  - source generated at `2026-08-09T15:32:09Z`;
  - node-set digest:
    `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`;
  - evidence digest:
    `e1de06fc1460d406bfaffc3b5e353d197089b262daa541d52a47a94995dd9b27`.
- Fresh production evidence collected at `2026-08-09T12:52:48Z`:
  - source generated at `2026-08-09T12:51:59Z`;
  - node-set digest:
    `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`;
  - evidence digest:
    `7d3a2e02320ee446c2fb1499eb29b00958d8e9ed46ec36b3cad6018cb8ae3940`.
- Reviewer follow-up evidence collected at `2026-08-09T13:29:20Z` after adding
  `CONFIG_MITIGATION_SRSO`:
  - the single kernel configuration reports `CONFIG_MITIGATION_SRSO=y`;
  - evidence digest:
    `e52b6a5f13c673573df5ac51e1b856a301f611d4f1f5990aa5c2aea38d7f9689`.
- All 12 current compute nodes report booted 6.12.95 with loaded, enabled,
  non-transitioning `livepatch_4`, patch version 4, and reported release
  6.12.95.4. Storage node 161 is excluded by VPS-only workload.
- Staging nodes 400 and 401 report active v3 from approximately
  `2026-08-07T17:29Z`. The later inventory observation is internal metadata,
  not evidence that effective v3 protection disappeared before v4 activation.
- The operator reports that applying v3 crashed AMD node5.brq. Its repaired
  history records a reboot at `2026-08-07T18:15:46Z` without carrying v3
  forward; the five v3-first CVEs remain affected there until v4 activation at
  approximately `2026-08-09T03:06Z`.
- Node 300 received v4 last, at approximately `2026-08-09T11:48Z`, but the
  original 14 CVEs remain continuously mitigated there since patch 2 was
  activated at `2026-08-06T02:25:10Z`.
- Every one of the 19 live-patch evaluations is complete with 12 `mitigated`,
  one `not_affected`, no `unknown`, and no currently vulnerable node.
- For the original 14 CVEs, ordinary compute nodes and staging retain their
  patch-2 mitigation dates from 6 August. Node 214 (`node5.brq`) correctly starts
  a new interval at patch 4 on 9 August because its v3 activation crash and
  reboot genuinely cleared livepatch state.
- For the five patch-3 CVEs, staging nodes retain their patch-3 mitigation date
  `2026-08-07T17:29:10Z`; production nodes first became mitigated by patch 4 on
  9 August.

## Verification

- `bin/security-advisory validate`: 24 dossiers validated.
- Targeted dossier RSpec: four examples, zero failures (seed 39871).
- `bundle exec overcommit --run`: passed.
- RuboCop: 28 files inspected, no offenses.
- Full RSpec: 123 examples, zero failures (seed 6400).
- All intended changes are committed with active repository hooks. The 14
  cumulative updates were folded into their owning CVE commits; the five new
  dossiers remain one commit per CVE. The rewrite preserved the exact final
  tree.
- Mandatory review initially found two Important issues in CVE-2026-68480:
  - Safe-RET introduction boundaries were conservatively overstated;
  - `CONFIG_MITIGATION_SRSO` was not requested from node evidence.
- Resolution:
  - global introduction is now Linux 6.5, with exact stable starts 5.10.189,
    5.15.125, and 6.1.44 and their introduction commits;
  - every maintained branch has regression-checked introduction metadata;
  - the dossier requires `CONFIG_MITIGATION_SRSO`, fresh evidence reports `y`,
    and its complete evaluation was regenerated;
  - fixes were folded into the owning CVE and common-support commits.
- Post-fix verification passed:
  - RuboCop: 28 files, no offenses;
  - full RSpec: 124 examples, zero failures (seed 43036);
  - targeted dossier RSpec: five examples, zero failures (seed 12881);
  - all 24 dossiers validate.
- The same reviewer confirmed both findings resolved with no new finding. Its
  targeted run passed five examples with seed 36761, and `git diff --check`
  passed at clean head `f1cc2e5812d606f375a0f3df1bede9e8de340ce8`.
- Branch head `f1cc2e5812d606f375a0f3df1bede9e8de340ce8` was pushed. GitHub Actions
  RSpec run 31316173213 and RuboCop run 31316173198 both passed.
- Drafts 11 through 18 were reconciled and verified as unpublished. Their
  content revisions are 27, except newly created draft 25 for
  CVE-2026-46093, which is revision 13. Each exact remote snapshot has a
  committed submission baseline.
- Synchronization stopped safely before writing CVE-2026-64508 after the
  collector repeatedly observed node 401 change `evidence_revision` during a
  current snapshot read. A direct sample showed revisions changing every 30
  seconds, at observations `2026-08-09T14:35:36Z` and
  `2026-08-09T14:36:06Z`.
- The deployed API's `evidence_revision` includes reconstruction coverage and
  therefore changes on every unchanged observation. Its `snapshot_revision`
  is the digest of actual kernel state and is carried by every component.
  Commit `4449ea5` now guards current components with `snapshot_revision`,
  separately rechecks event and reconstruction structure, ignores only
  non-regressing `observed_through` advancement, and retains the latest
  collection revision for provenance.
- Collector-focused RSpec passed 25 examples with seed 13600. Post-fix full
  RSpec passed 126 examples with seed 38314, and RuboCop passed all 28 files.
- Mandatory reviewer follow-up found no Blocking or Important issue. Its one
  Minor finding required rejecting a coverage watermark rollback or
  disappearance; the amended commit and reverse-time regression test resolve
  it. The same reviewer confirmed no new findings after independently passing
  25 collector examples (seed 13014), focused RuboCop, and `git diff --check`.
- Mandatory follow-up review found the blanket exclusion of internal inventory
  events Blocking because such an event can report `transition: true`; it also
  hid eBPF, sysctl, module, and deployment security-state changes.
- The resolution retains every event snapshot. For internal observations, the
  evaluator carries a preceding effective patch only when unchanged identity
  metadata is omitted or an inactive configured successor temporarily replaces
  the reported inventory. Public lifecycle events remain authoritative, and a
  runtime transition or real loss of an accepted patch still ends mitigation.
- The evaluator explains mitigation using the transition that began the
  continuous interval, not the newest cumulative patch.
- Regression coverage verifies accepted v2-to-v4 and v3-to-v4 replacements,
  missing internal patch metadata, inactive successor inventory, unrelated
  deployment observations, a real transitioning inventory snapshot, first-fix
  public wording, and preservation of the earlier mitigation date.
- Post-correction verification passed:
  - all 24 dossiers validate;
  - full RSpec: 132 examples, zero failures (seed 49210);
  - focused collector, evaluator, and dossier RSpec: 84 examples, zero failures
    (seed 31985);
  - RuboCop: 28 files, no offenses;
  - `git diff --check` passed.
- Common lifecycle commit `9989dee` and 19 separate CVE correction commits
  through head `2cc4621` passed all active pre-commit and commit-message hooks.
- Mandatory reviewer follow-up on `2ef1496..2cc4621` found no Blocking,
  Important, or Advisory issue. Its independent focused RSpec passed 84
  examples, touched-file RuboCop and `git diff --check` passed, and it confirmed
  the worktree, 20-commit split, evaluation provenance, completeness, and
  v2/v3/v4 chronology.
- A later direct node 401 comparison showed that its `snapshot_revision`
  advanced every 30 seconds solely because the eBPF program's `verified_at`
  timestamp advanced. Slow event and reconstruction-history reads between the
  two current-state guards therefore made a coherent collection needlessly
  unlikely.
- Current component reads are now kept in the narrow snapshot-consistency
  window. Event and reconstruction-history reads occur before that window and
  retain their separate post-read consistency checks. A production collection
  succeeded with the revised ordering, including node 401.
- The final production evidence above was used to regenerate all 19
  evaluations. Exact assertions confirmed the original CVEs retain patch-2
  dates except for node 214 (`node5.brq`), whose reboot cleared that state,
  while the new CVEs begin with patch 3 on staging and patch 4 on production.
- Collector-focused RSpec passed 27 examples with seed 10401. Post-correction
  full RSpec passed 133 examples with seed 41385; RuboCop passed all 28 files;
  all 24 dossiers validate; and `git diff --check` passed.
- The reviewer found that folding the collector ordering fix into the existing
  cumulative-livepatch commit made that commit too broad. Common live-patch
  behavior is now isolated in `abef4eb`; collector ordering and its tests are
  isolated in `1170d07`; and the 19 owning CVE commits follow separately. The
  three corrected draft baselines follow them; clean branch head is `fd65408`.
- The split preserved exact final tree
  `b2bb942774d5014b131bfc125cfe8271e16e9be0`. Post-split collector and
  reconciler RSpec passed 50 examples with seed 52694, focused RuboCop passed
  all three files, and `git diff --check` passed.
- The same standalone reviewer confirmed the split resolves its Blocking
  finding. It found no remaining Blocking, Important, or Advisory issue and
  verified all 24 commit scopes and messages, both patch identities, the
  unchanged final tree, and the clean worktree.
- User review rejected naming deployed cumulative patch 6.12.95.4 in public
  responses because every later rollout would make that wording stale. All 19
  English and Czech responses now name only the first fixing version: patch 2
  for the original set and patch 3 for the five additions.
- Repository instructions and regression coverage now require each public
  response to contain only its first fixing `6.12.95.x` live-patch version.
- Repeated draft synchronization was slow because every one-CVE apply repeated
  the same complete 13-Node evidence collection. `sync` and `ready` now accept
  an explicit `--evidence` document for related batches. Reuse expires when the
  oldest Node receipt or history-coverage timestamp reaches the evaluator's
  15-minute limit; collection time therefore reduces the usable batch window.
  Per-advisory revision preconditions and exact post-write readback remain.
  README and repository instructions require one immediate collection,
  sequential writes, and a committed baseline between writes.
- Regenerated evaluations use evidence collected at
  `2026-08-09T18:32:53Z`, node-set digest
  `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`,
  and evidence digest
  `02c1697f89bab0a2c3669982cb5d6fb0841e6201fba44b53a823cba659023442`.
  Exact projections confirm all 19 node conclusions and mitigation dates are
  unchanged.
- Post-wording verification passed: all 24 dossiers validate; full RSpec 139
  examples, zero failures (seed 23058); RuboCop 28 files, no offenses; and
  `git diff --check` passed. All commits passed active hooks.
- The wording policy is folded into common commit `7ba2a8c`, each response and
  evaluation into its owning CVE commit, and shared evidence reuse is isolated
  in `bef8b31`. Clean branch head is `bef8b31`.
- Mandatory review found that a fixed 30-minute reuse limit could outlive the
  evaluator's 15-minute per-Node freshness check, and that malformed JSON root
  or timestamp types could escape as raw Ruby exceptions. The amended feature
  derives expiry from the oldest evaluator-relevant Node timestamp, normalizes
  structural and timestamp errors, and covers receipt, history-coverage,
  non-object, and future-timestamp cases. Focused Reconciler RSpec passed 29
  examples with seed 41490 and focused RuboCop passed.
- The same standalone reviewer verified the evaluator-derived deadline against
  production-shaped evidence, confirmed controlled malformed-input errors,
  and found no remaining Important or Advisory issue. A final commit-message
  amendment removed the stale 30-minute claim without changing the reviewed
  tree.
- Exact-head GitHub Actions passed for reviewed head `bef8b31`: RSpec run
  31330558236 and RuboCop run 31330558233.
- One shared production collection completed at `2026-08-09T19:05:52Z` with
  node-set digest
  `f434faac03a83c7ba7329214924bdb7561a5c619dd09b9f53a9dd9c660e9092e`
  and evidence digest
  `db62cc20e4ad013a1b3f63db3d89ca77c0b3f93e8f2607c79fa4d5379e27c0cc`.
  Its oldest evaluator freshness timestamp was `2026-08-09T19:02:30Z`, giving
  an exact reuse deadline of `2026-08-09T19:17:30Z`.
- All 19 drafts synchronized and passed exact post-write verification from
  that one evidence document. The 18 existing updates and their hook-checked
  one-CVE commits completed in about one minute; CVE-2026-68480 was created as
  draft 29.
- Read-only `ready --evidence .state/evidence.json` passed for every CVE before
  expiry. Each result reported 12 `mitigated`, one `not_affected`, the exact
  draft revision, and `ready: true`.
- All 19 submission baselines reference stable reviewed dossier commit
  `95cf3613779426a711a18ab2d0f6b5eec444a5d7`. Generated baseline refreshes are
  folded into one commit per CVE; shared-evidence tooling is isolated in
  `0a1d871`; clean head is `e201d89`.
- Final feature branch head `e201d8934d3314a143c53ed2636c902be0405fbf`
  is pushed. GitHub Actions RSpec run 31331136385 and RuboCop run 31331136387
  both passed.
- Draft correction remains in progress. Publication and merge remain
  prohibited.

## Current remote draft state

- All records written in this initiative were verified as `draft` with no
  publication timestamp.
- All 19 records contain the durable first-version-only response and were
  verified as `draft` with no publication timestamp.
- Final draft revisions are: 11/40, 12/40, 13/40, 14/40, 15/40, 16/40, 17/40,
  18/40, 19/39, 20/27, 21/27, 22/27, 23/27, 24/27, 25/17, 26/17, 27/14,
  28/14, and new draft 29/13.
- Exact local submission baselines are committed for every draft. Publication,
  notification email, and merge remain prohibited.

## Commands run in this revision

- fetched all affected canonical repositories and inspected their default
  revisions;
- rebased the security-advisories feature branch on `7cb4fb1` from inside
  `nix develop` with active hooks;
- read current production draft and node-evidence state without mutation;
- `nix develop -c bin/security-advisory validate`;
- `nix develop -c bin/security-advisory collect`;
- `nix develop -c bin/security-advisory evaluate CVE-...` for all 19
  live-patch CVEs;
- `nix develop -c bundle exec rspec spec/dossiers_spec.rb`;
- `nix develop -c bundle exec overcommit --run`;
- focused commits plus interactive autosquash onto the existing owner commits.

## Open questions

- None.

## Cleanup

- Keep the local and remote feature branches.
- Keep the initiative worktree because the branch is neither merged nor
  abandoned.
- Do not publish, send email, merge, or remove the worktree.
