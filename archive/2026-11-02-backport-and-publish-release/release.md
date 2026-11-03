# HaveAPI 0.32.2 release receipt

**Completed and publicly verified on 2026-11-02.**

- Public release: https://github.com/vpsfreecz/haveapi/releases/tag/v0.32.2
- Release branch and retained feature head: `1ef9b204ba45bb261d3334be5c555cc1856b713b`.
- Annotated tag object: `7f8f656ca7655bafaf2cf5e7095573806085a442`; peel equals final head.
- Tagged workflow `41529223599` attempt 1 succeeded; protected publishing job
  ran 21:42:21–21:46:34 UTC. GitHub Release `432000718` became public at 21:46:31 UTC.
- All feature/tag/target component and performance checks pass. Target build-only
  `41528866548` attempt 2 succeeded after the documented cache-transfer failure.
- Independent review completed; sole narrow bilingual command finding resolved
  and directly verified. No migrations. No remaining approval or release blocker.
- Repository claim released and resulting state verified before publication.
  No machine deployment/claim or session lifecycle action occurred.

## Final public availability and immutable evidence

Independent registry reads at `2026-11-02T21:48:45.592157+00:00` verified all five
RubyGems SHA-256 values, npm integrity/SHA-1 against the approved tarball, both
PyPI file SHA-256 values and Composer/Packagist 0.32.2 indexing. Public GitHub
Release assets were downloaded independently: all 12 match the original approved
tagged artifact, including exact manifest bytes.

Original publication artifact: `13181726847`, `release-41529223599`, 1,317,335 bytes,
archive SHA-256 `d1c126edd509a21424bc5a056c5c8ebfbd984a0aaf97c96de291def0351c2459`.
Public source/input/hash manifest:
https://github.com/vpsfreecz/haveapi/releases/download/v0.32.2/release-manifest.json

Manifest SHA-256: `7c53624cc059434279e6eba6f8a9ec151a57897f41e96f0b1d261e1b58fa728b`.
It binds final source/run/version, every payload hash, complete text of ten
resolved dependency locks and actual tool versions. Source commit includes the
complete selected Nix flake/input graph. These published immutable receipts
preserve recovery inputs after local raw artifacts are eventually retired.

| Published file | SHA-256 |
| --- | --- |
| `haveapi-client-0.32.2.gem` | `ba86c3fdaafc57ed40c6164fbdce6aee019e8e72e7f85ef07fb03af727828187` |
| `haveapi-0.32.2.gem` | `3b4621b3bf8ded453066b413378f74fcddd7934e8b6bac4e2530db507cb7e624` |
| `haveapi-go-client-0.32.2.gem` | `3dd293c560b304d1960364d4b286f220e62bd28939a7e1da59d39db519487bfb` |
| `haveapi-rust-client-0.32.2.gem` | `ca01b2408a63edac5369edeb74d898d81f1b65ead14922f0a25c2a4cc8cfd28e` |
| `haveapi-typescript-client-0.32.2.gem` | `4b207bfc2f389787fdba2c874a446b21069f84155c0b91e096df8836d7be26c2` |
| `haveapi-client-0.32.2.tgz` | `0392eb805023047d12e1086cffd96dfb65bd13f4b4afdffdad715cce437b0f47` |
| `haveapi-client.js` | `b719496b1944f111fc893bf17e0358bd86403828ef665b124cd79d67fa3e2d00` |
| `haveapi-client-php-0.32.2.tar` | `badb22608a4a7962cbdb87c66ca28afbcf3841d16fe8db2e6ec46b41c9ab40de` |
| `release-notes.md` | `52f651fe2854fc593662493aff64a54ca8e271ae9ba845375011c92ee58e1810` |
| `haveapi_client-0.32.2-py3-none-any.whl` | `3c444f4e359ff28400c6b52a9bf4cac3bebeb3322fb1e4b5e07cb6014b4660d6` |
| `haveapi_client-0.32.2.tar.gz` | `09a0051bf2c4d29f49d1d9c471b12b73097761bd3f9584d3248185f3a924315f` |

PHP mirror `master` and annotated `v0.32.2` both resolve to
`f6b7f98cf6e28e7f98067f77d8af4379f4e08c8f`; PHP tag object is
`2bf2c0e3ee1b5cd420d17caed8eb7047b6fff7c7`. Its tag/commit explicitly record
`HaveAPI-Source: 1ef9b204ba45bb261d3334be5c555cc1856b713b`.
Packagist indexes the same commit at version 0.32.2:
https://repo.packagist.org/p2/haveapi/client.json

Raw supporting receipts: registry-verification.json, public-asset-verification.json,
public-release.json, php-public-{tag,tag-object,commit}.json and
ci-publication-evidence/. Full CI result: [ci-publication-result.md](ci-publication-result.md).
Read-only fresh SSH proofs confirmed HaveAPI release/feature/tag heads and PHP
mirror master/tag lineage. Both owned checkouts remain clean.

Final verified publication notification sent through the active exact-pair
communication grant to `2026-11-02-haveapi-vpsadmin-release`, message
`c3217ac5-8415-4ce4-bf37-a5c144f3ff51`. Downstream work remains separately owned;
no peer files or worktrees were accessed. No user action is required here.

The session remains open with branches, clean worktrees and recovery artifacts
retained. No archive, deletion, stop, removal or cleanup was requested/performed.

## Preparation and execution history

## Authorization and immutable identities

Original user request in this conversation: “Backport commits from haveapi
master into haveapi-0.32 and make a new patch release 0.32.2, publish it.”
This explicitly authorizes HaveAPI/haveapi-0.32 integration and the normal
coordinated 0.32.2 publication, including the release workflow's PHP mirror.
It does not authorize HaveAPI/master integration or a fleet deployment.

Canonical source repository: git@github.com:vpsfreecz/haveapi.git.
Release target: haveapi-0.32. Configured session target matches it.
Initial target: 9efeadf91d894e01d1d4f4a3e3fc64c6309785c7.
Accepted master source: f29c1e4675bc1f79641faa619b8c68ecec923c71.
Exact backport mapping and compatibility contract: [design.md](design.md).
No database or persisted-state migrations. No machine is deployed/reserved.

## Delivery gates

- Implementation and quick-check evidence: [implementation.md](implementation.md).
- Independent final review: pending.
- Exact candidate/full history and migration conclusion: pending.
- Branch CI/full release validation: pending.
- Final target/ref proof and repository claim release: pending.
- Annotated tag identity and remote peel: pending.
- Tagged workflow candidate artifact and manifest hashes: pending.
- Protected environment approval and publication receipts: pending.
- Public registry hashes, PHP source/tag, Packagist and GitHub Release: pending.

## Publication preflight

GitHub environment `release` exists with required reviewer aither64 and
prevent_self_review=false. Repository variable HAVEAPI_RELEASE_ENABLED=true.
Authenticated GitHub identity is aither64. Fresh initial checks found no
v0.32.2 remote tag or GitHub Release. Actual registry/OIDC/key preflight is
performed by the existing workflow before uploads.

## Recovery

Use the exact original tagged workflow, source, retained artifacts and draft
Release if publication partially fails. Reconcile original accepted uploads
against retained hashes before retrying failed jobs. Never move the tag,
overwrite immutable versions or rebuild accepted artifacts. See the owning
HaveAPI release procedure for authoritative recovery steps.

## Integration preparation

Clean detached target checkout:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-backport-and-publish-release/haveapi-integration`,
HEAD 9efeadf91d894e01d1d4f4a3e3fc64c6309785c7. Fresh remote target unchanged.
Actual post-merge hook executed as preparation, exit 0, signatures accepted;
Overcommit 0.74.0 loads with no configured post-merge actions. Root Gemfile,
flake/lock and hook configuration/source are identical baseline/candidate.
Existing feature root Nix environment supplies its prepared tool bundle without
copying dependencies/source. No shared mutation or claim yet.

Approved merge command from feature worktree, only after final review/full CI
and a held repository claim with fresh target/feature/cleanliness checks:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-backport-and-publish-release/haveapi-integration merge --ff-only 1ef9b204ba45bb261d3334be5c555cc1856b713b
```

See implementation.md for target preparation evidence. The command above is
prepared, not executed.

## Narrow independent-review correction

Original review base/head: 9efeadf91d894e01d1d4f4a3e3fc64c6309785c7 →
dca492c680b8d52f1e4c8b51e89cb7a97fc83c38. New candidate range uses the same
base → 1ef9b204ba45bb261d3334be5c555cc1856b713b. All twelve upstream backport
objects unchanged. Local doc correction now also updates the Czech command to
supported runtime0.32.0; metadata patch is identical. Lead independently checked
old/new tree delta: exactly this one command token. No migrations/deployment.
Original range and quick evidence retained, with review-fix-range-diff.txt and
review-fix-narrow.diff. Narrow fix verification uses existing shared_pages
sample-consistency assertion and refreshed final-head quick evidence.

B1 direct verification complete at final1ef9b204: lead inspected exact old/new
one-token tree diff/range-diff; existing shared_pages assertion aftermake doc
passes1example/0failures, all11 refreshed quick checks pass, source clean.
Independent review has no other findings. Proceeding to fullCI; not yet published.

## Development branch publication and full CI

Feature1ef9b204ba45bb261d3334be5c555cc1856b713b pushed overSSH to
2026-11-02-backport-and-publish-release. Initial ambient-shell push was refused
by Overcommit signature check before remote mutation; the same push in declared
prepared Nix shell succeeded with hooks enabled. No signing/bypass performed.
Fresh remote target remains9efeadf91d894e01d1d4f4a3e3fc64c6309785c7.
Final comparison captured against that exact base/head.

Eleven automatically triggered exact-head runs assigned to fresh standalone
Luna/low verification utility, full_access explicit danger-full-access/never.
Run identities and stopping conditions are in ci-feature-prompt.md. Release
build-only run41527342376; performance41527342340; all component checks included.
Result/progress/status receipts will be recorded before integration. No repository
claim or protected publication approval yet.

## Full verification accepted before integration

All eleven feature-head workflows passed; no active runs/failures remain.
Evidence: ci-feature-result.md and verification-watcher/status-final.json.
Release build41527342376 retained artifact13180298796, release-41527342376,
1,317,331bytes, archiveSHA25683ab290d63979948514d1d111a3a218d8dce0d5720025220d42546e4eb2d3330.
Downloaded feature-artifacts/release-manifest.json binds version0.32.2,
source1ef9b204ba45bb261d3334be5c555cc1856b713b, run41527342376, all eleven
payload hashes, ten complete dependency lock texts and tool versions. Existing
`cli.rb verify` passed in the tools-only top-level Nix shell. No package rebuilt.
Final14-commit series rechecked against completed review plus prescribed narrow
fix; no obsolete history/repeated update stream, no migrations. Selected package
unchanged from fully read coordination guide. Short approved merge claim next.

## Approved target integration completed

Repository claimfece7749-add0-4225-9219-c56c154d7b03 was authoritatively held
by this session before fresh remote/feature/target/cleanliness/ancestry checks.
Ordinary fast-forward and declared post-merge hook completed successfully in
prepared Nix environment. Non-force SSH push advancedhaveapi-0.32 from
9efeadf91d894e01d1d4f4a3e3fc64c6309785c7 to
1ef9b204ba45bb261d3334be5c555cc1856b713b. Fresh SSHls-remote proves both target
and retained feature branch equal exact final head; target checkout is clean.
No command remains unfinished or uncertain. Claim status inspected, released,
and resultingreleasedstate verified at2026-11-02T21:30:16Z before records/CI.
No machine claim or session lifecycle action. HaveAPI/master untouched.

## Annotated tag and post-integration CI checkpoint

Remote annotatedv0.32.2 tagobject7f8f656ca7655bafaf2cf5e7095573806085a442,
peels toexact final1ef9b204ba45bb261d3334be5c555cc1856b713b; fresh SSHproof
matches release branch. Initial tag push was started before local creation
completed and failed with absent source ref; both commands reconciled completed,
local annotated object/peel verified and remote absence proven before successful
ordinary retry. Tag never moved or replaced.

Tagged release run41529223599 started. No protected publication approval yet.
Unexpected automatic target-branch build-only release run41528866548 failed;
same-source feature run41527342376 previously passed. Implementer0 explicitly
owns log/artifact/root-cause diagnosis and evidence before any retry. No source
edit, retag, publish or blind rerun authorized. Remaining target/tagCI runs
continue independently; no repository/machine claims held.

## Diagnosed infrastructure failure and bounded recovery

Implementer0 inspected original41528866548 job125563604995 complete logs:
Nixcache.nixos.orgconnection resets/SSL EOF/curl55, resumed tzdata nar at
byte203920 returned HTTP416 at21:30:24.978Z. Missing
/nix/store/fsrw69w5mx838p7xydbdvywhwl6wnbjw-tzdata-2026e cascaded to shell
dependency failure before Ruby checker/tests/build/artifact-discovery/upload.
No source defect evidenced; failed run0 artifacts, publication skipped.
LogZIP41,425bytes,SHA2565ac8dda0cf7265e1d749f40a13cfa1300e93dfd48e22b1aa34724e5352d49cd7;
compact diagnosis and failed-release-41528866548* receipts retained.
Tagged same-source run already passed this shell boundary. Lead requested one
failed-job retry of build-only41528866548 after diagnosis; API succeeded.
No tagged rerun or source/pin edit. Further failure requires new diagnosis.

Fresh phase2 Luna/low utility monitors exact target/tag IDs in
ci-tag-gate-prompt.md, including target build-only attempt2. It returns at
protected-ready tagged build/artifact gate with component/performance results.
A still-running duplicate build-only retry is carried into the final publication
watcher rather than holding completed tagged artifacts behind redundant work.
No protected publication approval yet, and no claims held.

## Authorized downstream coordination

Runtime verified exact-pair active communication grantc61cca2368b7b2cd5e144bc85b118e6c
with2026-11-02-haveapi-vpsadmin-release. Peer requests notification after registry
publication for their independently authorized downstream work. Lead replied
message4dd90377-fcd5-4f88-8e64-f94fb2dfe76d to60b13ab3-6cc3-4332-9239-30a7d461318a
with pending status, exact tag/source and compatibility constraints. No peer
files/team/worktrees accessed, no downstream task or integration authority
adopted. Final deliberate notification follows verified publication only.

## Exact protected candidate accepted

Phase2 utility completed: alltag components and target component/performance
checks pass. Taggedbuild41529223599 succeeds; publish waits onrelease environment
24722193856,current_user_can_approve=true. Target duplicatebuild41528866548
attempt2 still running and will be monitored alongside publication.

Original tagged artifact13181726847,release-41529223599,1,317,335bytes,
archiveSHA256d1c126edd509a21424bc5a056c5c8ebfbd984a0aaf97c96de291def0351c2459,
downloaded totag-artifacts. Its own manifest binds0.32.2,v0.32.2,source
1ef9b204ba45bb261d3334be5c555cc1856b713b,run41529223599, allpayload hashes,
tencomplete local locktexts andtoolversions. Existing top-Nix tools-onlyverify
command passes. Release notes inspected and match reviewed CHANGELOG.
This original tagged artifact is the publication input; no feature-artifact
substitution, rebuild, source edit or retagging. Original explicit user request
authorizes this0.32.2 publication. Lead prepared exact protected approval body
inpublication-approval.json; approval next. No repository/machine claim held.

Protectedapproval API accepted for exact taggedrun41529223599,release environment
24722193856,deployment7504079024,source1ef9b204,tagv0.32.2. Only original
artifact13181726847 approved. Fresh publication utility observes this run and
targetduplicate attempt2to completion, preserving success/failure receipts.
No further source or registry mutation is delegated to utility. Final independent
public registry/hash/PHP/Packagist checks remain after workflow completion.
