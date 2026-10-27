# SDK 0.1.1 trusted publication

**Version 0.1.1 is published and trusted publishing is confirmed.** Corrected
run [40566122638](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/40566122638)
succeeded from reviewed/integrated source **60a1b5d1b911c610bd993d93ae2b28d1932a0ccc**
and replacement tag **v0.1.1**. Public `latest` is 0.1.1. Registry bytes and SRI
match accepted corrected tag artifact **12762393553** exactly. npm identifies
the GitHub trusted publisher; signed provenance binds the package digest to the
expected workflow, commit, tag, run and `release` environment. No retry, token
fallback or second upload was performed.

[Final public identity and provenance proof](#final-public-identity-and-provenance-proof)
is below. Earlier failed runs, preserved original tag/artifacts/receipts, exact
replacement approval and recovery evidence are retained as historical records;
their pending-state wording describes those checkpoints.

- Repository: `git@github.com:vpsfreecz/vpsadmin-typescript-client.git`.
- Base/default: `main` at `149c72f11acef67224a47ed77711a3abb805fbd4`.
- Reviewed head: `4689d00ca4acf0cc26a3507fc3c238b687b53475`, published on
  `2026-10-27-prepare-client-releases`.
- Complete series: published 0.1.0 source
  `38a25ad88d0bf3018670184620cf69cdb71e92e7`, then 0.1.1 metadata commit
  `4689d00ca4acf0cc26a3507fc3c238b687b53475`.
- The actual 0.1.0 registry publication and matching receipt justify retaining
  that exact source boundary. No migrations or obsolete approaches remain.
- New diff: four files, +5/-5. Only package/root-lock versions, README install
  literal and required lock digest change. Runtime 0.30.2, generator 18b45aed,
  schema, provenance, generated sources and workflow remain unchanged.
- Lock SHA256: `949ca1c8a761e9ca73d6562f7a0542ff3f0d1c2d5a79a0628083d44029cf7ab6`.
- Quick checks: six existing release tests, metadata/pin identity assertions,
  unchanged-source comparison and `git diff --check` passed. No hook framework
  is declared.
- [Final source/configuration review](sdk-0.1.1-review.md): no findings.
- [GitHub setup receipt](sdk-trusted-publishing.md): protected release
  environment, tag policy/ruleset and enabled variable independently verified.
- [Canonical feature CI run 40561183090](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/40561183090)
  passed at the exact reviewed head; fresh pinned Luna/low watcher completed
  observation. Offline regeneration, build, source/consumer type checks, all 10
  tests and the extracted package consumer passed.

The clean detached integration target is
`worktrees/2026-10-27-prepare-client-releases/vpsadmin-typescript-client-target`
at the base above, with the pinned Nix environment available. Fresh SSH reads
before and after feature push still showed default `main` at that base and no
`v0.1.1` tag. No repository claim is held.

## Accepted feature artifact

Immutable Actions artifact **12761975542**, name
`npm-package-4689d00ca4acf0cc26a3507fc3c238b687b53475`, retains the original tarball
and receipt. Download ZIP digest matches GitHub:
`sha256:fb1b27e0c9af11108ccdba86ef23e6da4d091a6e8038be27650f65141e2dcb36`.

- [Tarball](sdk-0.1.1/feature/vpsadmin-typescript-client-0.1.1.tgz): 308,653 bytes,
  1,358 files; public 0.1.1, MIT, exact runtime peer 0.30.2.
- [Receipt](sdk-0.1.1/feature/receipt.json): source `4689d00ca4acf0cc26a3507fc3c238b687b53475`,
  tag null (feature validation).
- SHA256: `9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`.
- SHA512 integrity:
  `sha512-G7YlKCe4jX/ikmDYUT4SdZM2hf8Qvi1mQYNVetdNtHYYm4fzfLhBhcQEZYgDs7shVaAA5Bk6NCwcezqRPAWohA==`.
- [Workflow log](sdk-0.1.1-ci.log) and
  [artifact API inventory](sdk-0.1.1-ci-artifacts.json).

`tools/release.mjs verify` accepted the original downloaded archive and receipt.
Payload metadata equals the reviewed source. Included LICENSE, README, generator
record, schema/provenance/exporter lock and generated ownership manifest match
source bytes. No local full batch, rebuild or repack was performed. The later
release tag workflow produces its own tag-bound immutable artifact; its actual
archive/receipt must be accepted before protected publication.

Feature artifact checkpoint SSH proof (before later approved integration):
remote `main` remained
`149c72f11acef67224a47ed77711a3abb805fbd4`, feature is exact
`4689d00ca4acf0cc26a3507fc3c238b687b53475`, no `v0.1.1` tag exists, and the
feature worktree is clean. The clean detached integration target was at that base. No main merge/push,
tag, protected approval or npm upload ran during that feature checkpoint.

## Integrated tag build and protected gate

Lead records explicit user approval for SDK `main` integration and release.
The short repository claim was released and verified at 18:40:05Z, before CI
and tagging. Lead remotely proved `main` at exact reviewed head
`4689d00ca4acf0cc26a3507fc3c238b687b53475`. Annotated tag `v0.1.1`, object
`cb914823d2e74e9565e56a1af770b0d129fd0876`, peels to that head. Main native CI
`40562092686` succeeded.

GitHub created two native push run records for `release.yml`, both attempt 1,
same tag/head/actor. Canonical **40562213084**, created 18:40:51Z, completed build
job `122393957336` successfully at 18:41:36Z and waits for protected approval in
publish job `122394355033`. Duplicate **40562213605**, created 18:40:52Z, is
pending behind concurrency with no jobs or pending deployments at inspection.
No cause is established for the duplicate records. Approve only the canonical
run; lead will reject the duplicate protected request when it appears. Neither
run was canceled or retried.

Canonical immutable artifact **12761282299** has verified ZIP digest
`sha256:b7910cb22652b39f45d3a0f5fab8191a1cc6112a5c904bc654374bbca38376ae`.
The original [tag archive](sdk-0.1.1/tag/vpsadmin-typescript-client-0.1.1.tgz)
and [tag receipt](sdk-0.1.1/tag/receipt.json) were downloaded unchanged. Existing
release tooling accepted their exact source, tag and integrity. Archive bytes,
SHA256 and SHA512 are identical to the accepted feature artifact above; the
receipt additionally binds `v0.1.1`. MIT/public identity, runtime, included
LICENSE/README/schema/provenance/exporter lock/generator record/ownership
manifest all match source. No local build or repack ran.

The canonical pending environment is `release` / `25494232596`, reviewer
`aither64`, and API reports `current_user_can_approve: true`. Publication awaits
lead approval. Build logs are retained in
[sdk-0.1.1-tag-build.log](sdk-0.1.1-tag-build.log); artifact metadata in
[sdk-0.1.1-tag-artifacts.json](sdk-0.1.1-tag-artifacts.json).

## Canonical protected approval

Lead approved only run `40562213084` for environment `25494232596`; GitHub
returned deployment `7367285707` at reviewed source `4689d00` and `v0.1.1`.
Lead freshly proved exact main, annotated tag object and peeled commit before
approval. A fresh catalog-pinned Luna/low watcher now observes the canonical
publish job `122394355033` and duplicate `40562213605` protected-gate status.
No cancellation, retry or approval is delegated to the watcher. Public registry
0.1.1 returned HTTP 404 at the initial post-approval read; final publication
identity/integrity/provenance reconciliation remains pending below.

## Canonical publish failure and effects reconciliation

Canonical run **40562213084**, publish job **122394355033**, failed with exit 128.
Its original artifact `12761282299` remains retained unchanged. Preflight and
receipt verification both passed at 18:45:50Z. The actual next command was
`npm publish release/*.tgz --ignore-scripts --access public --registry https://registry.npmjs.org`.
npm treated `release/vpsadmin-typescript-client-0.1.1.tgz` as a GitHub shorthand,
then ran `git --no-replace-objects ls-remote
ssh://git@github.com/release/vpsadmin-typescript-client-0.1.1.tgz.git` and failed
SSH public-key authentication at 18:45:51Z. This concerns archive argument
resolution, not the npm account's trusted-publisher settings.

The exact pinned npm 11.19.0 parser was reproduced read-only:

- `release/vpsadmin-typescript-client-0.1.1.tgz`: type `git`, hosted `github`.
- `./release/vpsadmin-typescript-client-0.1.1.tgz`: type `file`, local archive.

Pinned npm's `lib/commands/publish.js` obtains the manifest at line 97 and invokes
OIDC only at line 147, then registry publication later. The failed Git lookup
happens while resolving that manifest. Therefore this attempt did not reach OIDC
or package upload; neither trusted-publisher acceptance nor a provenance
attestation was established. There was no npm token fallback. A plain retry of
the unchanged job repeats the source bug.

Fresh cache-distinct public reads at **2026-10-27T18:48:35Z**, with no-cache
headers, returned HTTP 404 for exact version 0.1.1; the package index omitted
0.1.1 and still had `latest: 0.1.0`. This corroborates the pre-upload failure.
[Exact canonical publish log](sdk-0.1.1-canonical-publish-job.log) lines 785–796
records the original failure. No upload, retry, source edit, retag, rebuild,
repack, settings change or fallback was performed during diagnosis.

The duplicate **40562213605** completed its build and now waits in publish job
**122397107267**, environment `release` / **25494232596**, with
`current_user_can_approve: true`. It remains unapproved. Lead owns rejecting that
exact unnecessary request, independently of the canonical failure. Recovery
requires source/design direction for the local archive prefix and version/tag
policy; no account-setting change fixes this argument-parsing failure.

## Bounded workflow repair prepared

Committed clean feature head **60a1b5d1b911c610bd993d93ae2b28d1932a0ccc**, not pushed
at this checkpoint, changes only `.github/workflows/release.yml` (+2/-1): the
publish argument is `./release/*.tgz`, with the lead-approved explanation that
npm treats an unprefixed relative archive as GitHub shorthand. Version stays
0.1.1; no helper, new test framework or imported-action change was added.

The actual corrected command was extracted from the workflow and run once with
`--dry-run --json` appended in a disposable `release/` fixture containing the
original tag tarball. Pinned npm 11.19.0 / Node 24.21.0, an empty environment
apart from tool PATH and explicit empty user/global npm configs plus an isolated
cache, and `--ignore-scripts` kept account/OIDC credentials out of the check.
Dry run exited 0, prepared package `vpsadmin-typescript-client@0.1.1`, and returned
the exact original receipt integrity. Original and fixture SHA256 remained
`9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`; the fixture
was removed. This proves local archive preparation, not OIDC authorization.
[Dry-run evidence](sdk-0.1.1-publish-dry-run.log) is retained. Its initial evidence
reader assumed flat npm JSON; the package-keyed result was then accepted from
saved output without repeating the command.

All six existing release tests, metadata/lock digest checks, source invariance
and `git diff --check` passed. The new [focused diff](sdk-publish-path-fix.diff)
awaits affected independent review before feature push/full CI. Complete
retained source history is `38a25ad8` (published 0.1.0), `4689d00` (integrated,
accepted artifact, failed before publishing 0.1.1), then `60a1b5d` (repair).
No migrations or obsolete approaches remain. Original tag object/artifact/logs
remain untouched; source integration and any exact failed-tag replacement need
new explicit user direction. No version/tag/source-default mutation, retry,
publication or token fallback ran during this repair.

Lead rejected duplicate run `40562213605`'s exact protected request; API returned
deployment `7367397343`. The duplicate later concluded failure with no pending
protected requests. No second upload was approved.

Independent implementer0 [effects reconciliation](sdk-0.1.1-recovery-reconciliation.md)
confirmed both failed runs terminal, rejected duplicate publish with no steps,
no pending deployments, unchanged public 0.1.0/latest, absent 0.1.1 and unchanged
original artifact/receipt. Remote source and original tag identities remain
consistent. No new check or mutation was required to accept that report.

## Reviewed path-fix CI and new source receipt

Affected final review cleared exact `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`
without findings ([report](sdk-path-review.md)). Feature push fast-forwarded
4689 to that head; public main and original tag remained unchanged.
[Canonical feature CI 40564838735](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/40564838735)
passed full validation, all ten tests and packed consumer; publish was skipped.
Fresh pinned Luna/low watcher retained [log](sdk-path-ci.log) and
[artifact inventory](sdk-path-ci-artifacts.json). No local full duplicate ran.

Immutable artifact **12762995825** has verified ZIP SHA256
`0182e62353991160a8db7cbaf33d324a5835793e3db68ce65df801892bc20b2e`.
Its unchanged [archive](sdk-0.1.1/path-fix-feature/vpsadmin-typescript-client-0.1.1.tgz)
and [receipt](sdk-0.1.1/path-fix-feature/receipt.json) pass existing release-tool
verification and payload acceptance. The receipt binds source **60a1b5d** with
null tag. Original **4689d00 / v0.1.1** receipt remains separate and unchanged.
The two tarballs are byte-identical, with original SHA256 **9d262825…f566e8**
and full SHA512 integrity above. The workflow-only repair did not alter payload.

Final SSH proof after acceptance: feature **60a1b5d**, main **4689d00**, original
annotated tag object **cb914823…fd0876** peels **4689d00**. Both feature and
prepared integration target are clean; target remains at 4689. This checkpoint
is ready for explicit user approval of the main fix and any exact failed-tag
replacement. No version, main, tag, settings, retry or publication change ran
under this feature verification package.

## Approved exact tag replacement and corrected gate

User explicitly approved integrating fix 60a1 and replacing only failed SDK tag
v0.1.1. Lead fast-forwarded/pushed/proved main at exact reviewed source
`60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`, released and authoritatively verified
claim `8f6f47a4-e8f5-44b7-af0d-61fb4854fca9` at 19:06:16Z before tag/CI.
Create-only recovery ref
`refs/recovery/2026-10-27-prepare-client-releases/v0.1.1-failed` preserves original
tag object `cb914823d2e74e9565e56a1af770b0d129fd0876` / source4689. The exact
old-object lease replaced only v0.1.1 with annotated object
`f4cb49ab54214d043d34716d30a43f14224d6ce2`, peeling to60a1. Remote proof is
lead-owned. Original artifacts and receipts remain separate and unchanged.

Corrected tag run **40566122638**, attempt1, completed build **122407724542**
successfully and waits in publish **122408377105** at environment **25494232596**
`release`, reviewer aither64, `current_user_can_approve:true`. Main native run
**40566050671** succeeded. No additional current-head tag run was observed.
Fresh pinned Luna/low watcher retained [build log](sdk-corrected-tag-build.log),
[run metadata](sdk-corrected-tag-run.json),
[artifact inventory](sdk-corrected-tag-artifacts.json) and
[pending gate](sdk-corrected-tag-pending-deployments.json).

New immutable artifact **12762393553** ZIP digest verifies as
`sha256:02201988efb321351bf3e0d162bbf5c411a4c59281a0520709be697a8121d33b`.
The original [corrected-tag archive](sdk-0.1.1/corrected-tag/vpsadmin-typescript-client-0.1.1.tgz)
and [new receipt](sdk-0.1.1/corrected-tag/receipt.json) were downloaded unchanged.
Existing tooling accepted source60a1/tagv0.1.1 and integrity. Payload records
match source and the complete tarball is byte-identical to the original failed
source4689 artifact: SHA2569d262825…f566e8 and the same full SHA512 above. Both
source receipts are preserved; neither is relabeled. Publication awaits lead's
approval of this exact corrected gate. No rebuild/repack, retry, token fallback,
Git/source/settings mutation or protected approval ran in this acceptance step.

Corrected protected approval: lead approved only run40566122638 for environment
25494232596 after fresh main/tag/peeled proof60a1/f4cb/60a1 and per-run approval
eligibility. GitHub returned deployment **7367860943**, source60a1/tagv0.1.1.
Publish job122408377105 is queued; actual OIDC outcome and public integrity/
provenance reconciliation are the next verification step. No other approval
was delegated or performed.

## Final public identity and provenance proof

Corrected run **40566122638** / publish job **122408377105** succeeded. The runner
executed 19:16:08–19:16:50Z; verified-archive publication ran 19:16:17–19:16:47Z.
Its log records signed provenance and `+ vpsadmin-typescript-client@0.1.1`.
npm's temporary processing message preceded public indexing; this prompted
read-only confirmation, not a retry. Public package time is
**2026-10-27T19:18:54.829Z**; cache-distinct index read at **19:19:19Z** showed
0.1.1 and `latest: 0.1.1`.

- [Public npm package](https://www.npmjs.com/package/vpsadmin-typescript-client/v/0.1.1)
  and [public registry metadata](https://registry.npmjs.org/vpsadmin-typescript-client/0.1.1):
  exact name/version, MIT and canonical repository match the corrected receipt.
  `_npmUser` is GitHub Actions, with trustedPublisher `id: github` and
  `oidcConfigId: 3bb51631-4704-43ac-9e90-622e84fcc9c5`.
- The public tarball was downloaded and compared byte-for-byte with corrected
  artifact **12762393553**, source60a1/tagv0.1.1. SHA256 is
  `9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`;
  registry SHA512 integrity is
  `sha512-G7YlKCe4jX/ikmDYUT4SdZM2hf8Qvi1mQYNVetdNtHYYm4fzfLhBhcQEZYgDs7shVaAA5Bk6NCwcezqRPAWohA==`.
- [npm attestations](https://registry.npmjs.org/-/npm/v1/attestations/vpsadmin-typescript-client@0.1.1)
  contain the npm publication statement and SLSA v1 provenance. Both subjects are
  `pkg:npm/vpsadmin-typescript-client@0.1.1`, with SHA512
  `1bb6252827b88d7fe29260d8513e1275933685ff10be2d664183557ad74db476189b87f37cb84185c404658803b3bb2155a000e4193a342c1c7b3a913c05a884`,
  matching the archive.
- Provenance names repository `https://github.com/vpsfreecz/vpsadmin-typescript-client`,
  workflow `.github/workflows/release.yml`, ref `refs/tags/v0.1.1`, resolved commit
  **60a1b5d1b911c610bd993d93ae2b28d1932a0ccc**, GitHub-hosted builder, push event,
  and invocation **40566122638/attempts/1**.
- [Public Sigstore record](https://search.sigstore.dev/?logIndex=3523718588)
  payload hash equals the exact npm provenance payload. Node crypto verified its
  DSSE signature; the npm bundle's certificate DER equals the public Rekor
  signer. Certificate SHA256 is
  `f12edec8b543e2db702335b1ec39d2b3c40d5a5d4510dc1629a59a85a51e3f33`.
  Its issuer is `https://token.actions.githubusercontent.com`; extensions bind
  the exact source/workflow/ref/run and expose environment **release**, including
  subject `repo:vpsfreecz@1721481/vpsadmin-typescript-client@1434281100:environment:release`.

This establishes actual direct trusted-publisher acceptance and public artifact
identity, beyond GitHub settings or certificate existence alone. The actual
workflow has no npm token configured; the publication used its protected OIDC
path. No manual/token fallback, local rebuild/repack, upload retry, extra approval
or source/settings/ref mutation was performed during final verification.
Only this current-head tag run was observed; earlier duplicate4689 was rejected.

Retained evidence: [metadata](sdk-0.1.1/corrected-published-metadata.json),
[attestation bundles](sdk-0.1.1/corrected-published-attestations.json),
[decoded provenance](sdk-0.1.1/corrected-published-provenance.json),
[Rekor response](sdk-0.1.1/corrected-publish-rekor.json),
[public signing certificate](sdk-0.1.1/corrected-publish-certificate.pem),
[successful publish log](sdk-corrected-publish-job.log) and
[run/job evidence](sdk-corrected-publish.json). Original source4689 and corrected
source60a1 receipts remain separate; the original failed tag recovery ref and
replacement tag identities above remain unchanged. No claims or machine holds
belong to this verification package. No further release action is needed.
