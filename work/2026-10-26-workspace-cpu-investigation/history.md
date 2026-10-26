# Runtime history consolidation

Current published feature head is `fffbd0d59fffc09667cb39878d9f7da8bdcd3806`
on base `deed45f04fc0698b2f2f408b2816ac124913d582`: the four unchanged CPU
commits below, followed by the separately retained submission-storage fixture
repair. The benchmark remains exactly `d209..0fd31`; its completed results do
not measure a different pair. Prior independent reviews/equivalence and ranges
remain preserved. Limited final test-fix/history/composition reviews passed with no findings.
All exact final heads are now deployed and integrated into approved remote master
branches; claims are released. Consumer final heads are recorded in
consumer-preparation.md, execution in rollout.md.

## Submission-storage fixture repair retained separately

The lead accepted implementer2's `fffbd0d5`, parent exact `f23e717c`, affecting
only `nix/tests/session-archive-lifecycle.nix` and
`portal/cmd/workspace-portal/archive_explicit_test.go` (54+/1-). The direct idle
helper now selects the portal's SQLite state root; its regression test proves
the legacy fence refusal, unresolved SQLite receipt and eventual idle success.
Owner evidence: 2 focused tests passed in 0.182 seconds; Nix parse/diff checks
passed. No runtime behavior, timeout, dependency or migration changed.

This repairs an existing base fixture and is intentionally a fifth logical
commit, as directed by the lead. No runtime history was rewritten. Final tree
is `f8e908bf0889505eaead1d0bd16ffd11ddb4358d`. Fresh serialized fetches retained
the same three defaults. Normal SSH feature push exited zero and remote proof
returned full `fffbd0d5`; replacement CI run is `40412890007`. Completed failed
`40406137477` was retained. Runtime and consumer old heads are preserved on local
`2026-10-26-workspace-cpu-investigation-before-submission-fixture-refresh` refs.
No new long check or build was launched by implementer3.

## Archive-permission baseline refresh executed

Under the assigned Git flock, fetch confirmed exact `deed45f0`. The ordinary
Nix-shell rebase replayed four commits without conflict or source edits. Old head
`0fd31c1fa8858ef15d516e58c883f8dea9aa727e` remains on local
`2026-10-26-workspace-cpu-investigation-before-archive-refresh`.
Final tree: `83cb08ff3eca758d2608fac768d1acec283f929e`. Ordered final commits:

1. `d107f34f6cc162c0db8ab1a2c5318d0439427801` — cache
2. `37763cb1ef35df0464ce9ac656727484adba14a9` — coordinator and receipt fixture
3. `d8820b85b1ee3ab16c279a5c40cc5af0b3dec098` — benchmark
4. `f23e717c2fa33803d889414b243591c9a97846d6` — retry

Reproduce the range comparison in the runtime repository:

```sh
git range-diff --no-color \
  d2099c62656bc2a36c306918a92832ba1e1a0cc0..0fd31c1fa8858ef15d516e58c883f8dea9aa727e \
  deed45f04fc0698b2f2f408b2816ac124913d582..f23e717c2fa33803d889414b243591c9a97846d6
```

Observed pairs: `deec3201 = d107f34f`, `627060cd = 37763cb1`,
`090e6379 = d8820b85`, `0fd31c1f = f23e717c`. Computing
`git show --format= --binary COMMIT | git patch-id --stable` for every ordered
old/new commit gives the same four IDs printed in the earlier target-refresh
receipt below. Whitespace check passed; tree/index are clean. No migrations or
new pin streams exist in runtime; its dependency lock is unchanged.

SSH feature-only publication used exact lease `0fd31c1f`; push exited zero and
fresh `ls-remote` proved full `f23e717c`. No default ref was changed. Replacement
push Check run is `40406137477` and remains untouched. Manual old-head observation
`40404893088` was initially retained; the lead later recorded its host success
and submitted its cancellation. That watcher owns final disposition; implementer3
did not cancel it or request another status check. Benchmark exports and results
remain tied to their original source pair and were neither changed nor rerun.

## Upstream freshness preflight (before refresh)

Session/environment and saved implementer3 access were reverified. Serialized
SSH fetches succeeded. Default snapshots now are runtime
`deed45f04fc0698b2f2f408b2816ac124913d582`, workspace
`83282a493a6961d352b8ad0e2dfa3b17624fd46c`, and configuration
`cba1f93fcf2d0c2be35d4fb3dd868ba537c38656`. At this preflight, reviewed feature
heads `0fd31c1f`/`3ac31bcb`/`f302aed8` remained unchanged and all feature trees
were clean. The executed refresh above supersedes that temporary freeze.

Runtime adds one archive-permission repair commit: 14 paths, 382 additions and
31 deletions. Its cleanup/check/recovery/tracking helpers, package installation,
archive documentation and tests share no path with the 19-path CPU feature.
It temporarily enables owner-write on verified session directories, restores
survivors' modes, and reconciles that addition during legacy recovery. Journal,
snapshot and runtime contracts, dependencies and flake inputs are unchanged.
Deploying the old candidate would remove this newly live behavior; preserve it.

Workspace adds its matching nested URL/lock update plus two tracking commits;
only the pin changes reusable content. Other sessions' record contents were not
inspected or changed. Configuration adds only its matching lock update. Complete
35/64-node comparisons with the previous defaults find only runtime source
metadata changed to `deed45f0`, NAR
`sha256-6MXV0ja7B6zFzE9fq7qGhD6FTTpf2gmXiQMRw8EpMFE=`; every edge,
follows path and sibling node remains identical.

Recommended next package, subject to lead direction: preserve current reviewed
ranges and running campaign identities; rebase the four CPU commits onto exact
`deed45f0`, prove ordered patch IDs/range-diff equivalence, then reconstruct each
consumer's single final pin atop its fresh default using the existing supported
pin routines. Consumer overlaps are confined to owned pin files. No rebase,
push, pin change, build or deployment was performed for this assessment. Textual
conflict freedom is expected from disjoint runtime paths, not yet executed.

## Previous target refresh

The lead authorized rebasing the four reviewed CPU commits from old base
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686`, old head
`f81358ef9a651f63ec88e755d8ee382a5f9c9936`, onto exact upstream
`d2099c62656bc2a36c306918a92832ba1e1a0cc0`. Upstream adds the already merged
background-tab title correction in seven browser/template/test/documentation
paths, with no dependency change. It is not part of this initiative's CPU patch.

Under the assigned Git flock, ordinary rebase replayed all four commits without
conflict or manual source editing. Final tree is
`12b6c042c63f7f87c666d94d51135912fac0b650`. Final ordered series:

1. `deec3201f885b6f7758dfe1f2d768fa4da938bd2` — cache
2. `627060cd0f726b9dba4a430217022d69fda70598` — coordinator and receipt fixture
3. `090e6379e85c558ec5f4848f92be5b2465219290` — benchmark
4. `0fd31c1fa8858ef15d516e58c883f8dea9aa727e` — retry

[Range-diff](history-target-refresh.range-diff) reports `=` for all four pairs.
Ordered [old](history-target-old.patchids) and [new](history-target-new.patchids)
stable patch IDs compare exactly equal:

```text
adccaaaa47763038517878ff76f8c302a180a293
14cacbbd788cb0396698b8554566e89178df1e61
4d8f0cea8decf820e14489bcfb79369484a2a086
71f332e3b10913bf0da0f1cb5d648ba24cf71eb3
```

Old head is retained on local
`2026-10-26-workspace-cpu-investigation-before-target-refresh`. SSH publication
used exact feature-only lease `f81358ef9a651f63ec88e755d8ee382a5f9c9936`;
push exited zero and fresh remote proof returned exact `0fd31c1f`.
No default ref changed. Superseded Check `40398517195` was confirmed running on
`f81358ef`, then canceled; final status is completed/cancelled. Current-head run
`40398791893` was left untouched. Full verification belongs to the lead's utility.

Controlled benchmark baseline is now `d2099c62`, with identical fixture files
copied from this final candidate into the baseline export. `7e6d7c9c` remains
the original deployed-source/live-measurement baseline in historical evidence.
No migration or repeated pin stream was added by this refresh. Approval's named
repository/target set is unchanged, as confirmed by the lead.

## Receipt-fixture repair fold and publication

The lead accepted `217e3e51dac86db9871fadfe59fae9d5185882ac`, a test-only
14+/2- fix in `test/workspace_host/live_switch_test.rb`, with focused 2-test,
25-assertion evidence. Its production tree matched reviewed `31157faf`; the
change corrects the scheduler fixture by seeding real due work and refusing
unexpected collection fallthrough.

Under the assigned Git flock, a fresh fetch confirmed published feature
`31157fafde754a6ebd8a413f1e91ff4d0f97da1b`. The repair was folded into the
coordinator commit with ordinary interactive rebase, retaining reviewed base
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686` and four logical commits:

1. `f5ebb144330c30ea535d4e09a045db6db07fc65b` — cache, unchanged
2. `9073b32a3dfbb46ff8b89a0a65562259f74f9581` — coordinator and receipt fixture repair
3. `1e1f7c81d9077ef830c1d2eef7f5bae67d8c4863` — benchmark
4. `f81358ef9a651f63ec88e755d8ee382a5f9c9936` — retry

Both old repair head `217e3e51dac86db9871fadfe59fae9d5185882ac` and new
`f81358ef` have exact tree `0ddf3cdf7750de53792947c46fa92c763b3e5d4e`;
`git diff --exit-code` passed. The old head is retained on local branch
`2026-10-26-workspace-cpu-investigation-before-receipt-fold`.
[Full range-diff](history-receipt-fold.range-diff) records the fold; no application
source, migration or pin changes were introduced by consolidation.

SSH publication used the exact feature-only lease
`--force-with-lease=refs/heads/2026-10-26-workspace-cpu-investigation:31157fafde754a6ebd8a413f1e91ff4d0f97da1b`.
Push exited zero and fresh `ls-remote` proved `f81358ef` on that feature ref.
No default branch changed. Current-head GitHub Check `40398517195` was queued;
old `40397520343` was already failed/completed, so no superseded active run
needed cancellation. No full check/build was launched here.

Consumer fetches were the only downstream action before the lead's pause;
published workspace `e89948a82a09631b8f442bc23b627e5f56599d91` and configuration
`c9b529cf861955f1747a9c350e46905ac663d889` still pin `31157faf`. No later
pin edits/commits, builds, claims, activation or integration were performed.

## Earlier consolidation checkpoints

Owner: implementer3. Lead explicitly assigned serial consolidation after accepting
the two direct review remediations. No publication, consumer pins, deployment,
repository claim or application-source edits were performed here. Independent
final history conclusion remains with reviewer0 through the lead.

Canonical repository: `git@github.com:aither64/dev-workspace.git`.
Feature branch: `2026-10-26-workspace-cpu-investigation`.
Target/base throughout: `refs/heads/master`,
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686`.
The serialized `git fetch origin` confirmed that exact remote-tracking master
before rewriting. The feature was unpublished; published default history was not
rewritten. Both rebase batches used the assigned Git flock, clean owned checkout
and empty index. Ordinary scripted interactive rebase and `git commit -F` ran
without bypassing hooks. Cache/coordinator commits remained identical.

## First batch: exact final-tree preservation

| Identity | Value |
| --- | --- |
| Old head | `4201b61d8e31573f2be37149d290e5343c2401c2` |
| Old tree | `144380422aad17c46b0150a4e565bcd06bc0a4b6` |
| Consolidated head | `d0a77c18f7b3f25bafc6db6a3e28c8a81ffece59` |
| Consolidated tree | `144380422aad17c46b0150a4e565bcd06bc0a4b6` |

`git diff --exit-code OLD_HEAD CONSOLIDATED_HEAD` exited zero: exact tree equality,
including modes and all files. The old head is retained on local branch
`2026-10-26-workspace-cpu-investigation-pre-consolidation`; the equal-tree checkpoint
is retained on `2026-10-26-workspace-cpu-investigation-consolidated-equal`.
Branches were retained and not published.

Complete original six-commit series and disposition:

| Old commit | Disposition |
| --- | --- |
| `f5ebb144330c30ea535d4e09a045db6db07fc65b` cache | Kept unchanged, first |
| `24f8870a0f9b2dcb871c8bc717424ec1906da817` coordinator | Kept unchanged, second |
| `69c45ad5b71a0eecb06bd782d5260a910b26a838` benchmark | Folded with its direct review fix below |
| `74df2ed3868d953bea2eeea9d2af0f717d29622d` retry | Folded with its direct review test below |
| `dd2e11fc4ed1420e39f175d9a7d4e1ab17e96adc` time-only retry test | Folded into retry |
| `4201b61d8e31573f2be37149d290e5343c2401c2` benchmark warm-up/reaction fix | Reordered and folded into benchmark |

The resulting benchmark commit at this checkpoint was
`13b5fa0e8be146309a549d30ce99eff459dd1b17`; retry was the consolidated head above.
[Full old/new range-diff](history-consolidation.range-diff) records both folds.
No intended patch was dropped or superseded behavior retained.

## Second batch: explicit one-off benchmark documentation

After proving equality, the lead-authorized clarification changed only the
opening paragraph of `docs/cpu-benchmark.md`: the long comparison is one-off,
opt-in, skipped by ordinary tests and CI, and must never become a routine gate.
That narrow documentation change was committed and folded into the owning
benchmark commit. It is separate from the equality claim above.

| Identity | Value |
| --- | --- |
| Final head | `31157fafde754a6ebd8a413f1e91ff4d0f97da1b` |
| Final tree | `03e9f52e1c77442ce41ef1a240976b990a75cc3b` |
| Delta from equal-tree checkpoint | `docs/cpu-benchmark.md`, 4 insertions/3 deletions |

`git diff --exit-code CONSOLIDATED_HEAD FINAL_HEAD -- . ':(exclude)docs/cpu-benchmark.md'`
exited zero. The full remaining diff is exactly that paragraph; no application,
fixture, test, dependency or configuration content changed in this second batch.
`git diff --check` passed and checkout/index are clean.
[Documentation-only range-diff](history-oneoff.range-diff) confirms the benchmark
wording delta and patch-equivalent retry replay.

Final complete four-commit series, in order:

1. `f5ebb144330c30ea535d4e09a045db6db07fc65b` — portal: share bounded coordination display snapshots
2. `24f8870a0f9b2dcb871c8bc717424ec1906da817` — coordination: skip retained owners without scheduler work
3. `a0068be489f1dc2f3f6543c3a81a8b63d9b789c2` — test: add controlled portal and coordinator CPU fixture
4. `31157fafde754a6ebd8a413f1e91ff4d0f97da1b` — portal: skip unchanged settled retry admission

## Verification and provenance

No migrations, schema versions, dependency/channel pin updates or repeated pin
streams exist in this branch. No migration was merged, released, deployed or
externally consumed. All six original intended patches survive in four logical
commits; obsolete fix-only history is folded into its owner. These are implementer
inventory conclusions for independent review, not the independent conclusion.

Existing quick evidence applies to the exact preserved implementation tree,
including the benchmark remediation validation (4.576 seconds, two conversations
warmed, one update observed and notification delivered) and the lead-accepted
time-only retry test. No expensive checks were repeated for history-only changes.
The separate wording clarification needed only focused diff inspection/check.
The one-off benchmark remains unlaunched; future launches must use this final
head after the lead accepts independent final history review.


## Final integration conclusion

Afterfinalfixture/consumerreviews, exactdeployedheadsfffbd0d59fffc09667cb39878d9f7da8bdcd3806,
workspace718bbaa210a4b7912dd2aa4b1bd1e4dc33a78f4b andconfig530efc29e5a6e5579c304ec22d3a10062cd0ecc4
wereffmerged+normalSSHpushedeachapprovedmaster. Freshremoteequalheadsand
literalancestryprovedbuilds/integrated-lineage.json. Runtimefiveseriescoherent,
eachconsumeronepin, no supersededfeaturehistory/migrations/repeatedstreams.
Deployedexactfinalheadsareliterallyintegrated; no equivalent-successorclaim
needed. Oldunselectedf23/0fdpinrefsretainedforprovenanceonly. Allrepoclaims
releasedimmediatelyafterfreshremoteproof,machinereleasedafterverificationand
completeintegratedlineage. Detailsrollout.md. Sessionopen,branchesretained.
