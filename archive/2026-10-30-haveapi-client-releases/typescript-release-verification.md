# TypeScript 0.2.0 publication verification

**PUBLIC VERIFIED — 2026-10-30 13:05:31 UTC.** npm 0.2.0 metadata and downloaded
tarball match the original accepted tag artifact and receipt. The public archive
is byte-identical to that retained artifact. Runtime remains exactly 0.30.2.

Owner: implementer3 for verification only. Lead owns Git refs, protected
environment approval and publication coordination under the recorded user
authorization. No approvals, npm uploads, publisher changes, reruns or ref writes
are performed by implementer3 or its watchers.

## Exact release identity and audit

Lead reports HaveAPI 0.32.0 publication completed and all destinations verified,
including Packagist, before pushing the approved TypeScript tag. Read-only SSH
remote verification confirms:

```text
main             e5786f69b7c223c3bb5b1de99b7f97186eec368a
v0.2.0 object    1b645b2190261268c566ed81c85543f4e51e6b55
v0.2.0 peeled    e5786f69b7c223c3bb5b1de99b7f97186eec368a
```

Audit note from lead: ordinary SSH tag push succeeded; server reported the
existing account's bypass for restricted tag creation. No rules were edited,
and no force push, retag or hook bypass occurred. This records the server's
authorization behavior; no configuration action is requested or performed.
Lead's pre-tag npm 0.2.0 endpoint check returned 404.

Exact tag workflow:
[41059048868](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41059048868),
push event, `head_branch=v0.2.0`, exact head e5786f69 above. Older feature/main
build-only artifacts remain historical and are not publication candidates.

Fresh pinned-policy Luna/low utility launched with explicit full access and
approvals disabled; [brief](typescript-watch-tag-build.md),
[launcher](typescript-tag-build-watcher.log). Its boundary is build completion
and protected release wait, retaining this exact tag run's immutable archive,
receipt, completed-build log and pending environment metadata. Parent validates
the artifact before the lead approves. Publication requires a different fresh
watcher after approval; no utility identity is reused.

## Accepted original tag artifact and protected gate

Build job **124073827740** succeeded, including tag prerequisites and
`Build and validate`; publish job **124074200061** waits for environment
**release / 25494232596**. Saved pending-deployment metadata reports
`current_user_can_approve=true`, reviewer `aither64`. No approval submitted by
this owner/utility. Tag-build watcher has stopped.

Original accepted tag artifact (preserve this ID, do not substitute branch or
main artifacts):

- ID **12978397388**,
  name `npm-package-e5786f69b7c223c3bb5b1de99b7f97186eec368a`.
- GitHub ZIP digest:
  `sha256:182d07bf0a44d555ea271c1c914d7af722427b7abdc7f2cc751339009f399c04`.
- [Tag tarball](typescript-tag-41059048868/artifact/vpsadmin-typescript-client-0.2.0.tgz),
  [tag receipt](typescript-tag-41059048868/artifact/receipt.json),
  [artifact metadata](typescript-tag-41059048868/artifacts.json),
  [jobs](typescript-tag-41059048868/jobs.json),
  [protected gate](typescript-tag-41059048868/pending-deployments.json),
  [direct completed-build log](typescript-tag-41059048868/build-job-direct.log),
  [watcher report](typescript-tag-build-watcher-report.md).

Receipt binds package `vpsadmin-typescript-client`, version **0.2.0**, tag
**v0.2.0**, source **e5786f69b7c223c3bb5b1de99b7f97186eec368a**, filename
`vpsadmin-typescript-client-0.2.0.tgz`:

```text
SHA256 36e699738830303fe8e1d76d102eacda025653dc75c07ce88d65a134c6ff3e3b
sha512-EugXnu4GEEdEXuaCh62MwCWQ4D9LkgmBuTnpLaSZM13NgwPbQkAWDiOdaQmr8Xt2lYsE4HrPuNEVrJsYuGJKkw==
```

Parent independently verified the downloaded original ZIP against GitHub's
digest/run/head binding, both tarball digests, exact receipt source/tag/version,
HaveAPI pin `0e7166a0f8f15827bfac051666a53bf449e999ec`, exact runtime peer/dev
0.30.2 and dev formatter 3.9.10. Archive generator pin, generated ownership
manifest and all three schema inputs are byte-identical to reviewed source;
all **674** owned JavaScript/declaration module pairs are present.

Tag build log confirms offline regeneration check, ten passing tests and
“Packed ESM, strict types and executor consumer passed.” The watcher's ordinary
whole-run log read was unavailable while the workflow waited and left an empty
`build.log`; parent resolved that evidence gap through the read-only completed
job-log endpoint. GitHub CLI's terminal-escape guard required the documented
`--allow-escape-sequences` option while redirecting output to the retained file.
No tests/build/workflow were rerun or artifacts rebuilt/repacked to obtain logs.

Artifact accepted and exact pending environment ID reported to lead. Lead may
approve under recorded user authorization. On confirmed approval, launch a new
fresh publication watcher, retain this original artifact identity, then verify
public registry version and integrity against the tag receipt before notifying
lead. No package is claimed published at this checkpoint.

## Approved publication and registry processing

Lead confirmed successful approval of environment 25494232596, deployment
**7438799627**, exact run 41059048868/tag v0.2.0/source e5786f69. Launched a
different fresh Luna/low observation utility; [brief](typescript-watch-publication.md),
[result](typescript-publication-watcher-report.md).

The workflow and publish job **succeeded**. Log confirms verification of the
approved retained archive, automatic OIDC provenance, and npm's acceptance:
`+ vpsadmin-typescript-client@0.2.0` at **2026-10-30 13:01:15 UTC**. npm also
reported that processing may take a few minutes. Public version endpoint still
returned 404 at 13:03:16 UTC, and its package index had no 0.2.0 entry. This is
not public verification; publication acceptance and registry availability are
recorded separately. No upload, workflow/job retry, token fallback or rebuild
was performed in response.

Evidence: [final run log](typescript-publication-41059048868/run.log),
[run/jobs summary](typescript-publication-41059048868/summary.json),
[deployment records](typescript-publication-41059048868/deployments.json),
[initial 404](typescript-publication-41059048868/registry.json).
Original accepted tag artifact ID remains **12978397388** and its receipt is
unchanged. Fresh read-only SSH proof still matches remote main/tag peel e5786f69
and annotated object 1b645b21. No ref or source mutation by this owner.

Publication watcher completed and stopped. A new short-lived policy utility now
observes bounded read-only registry propagation (ten samples 30 seconds apart,
download public tarball once available), without any publication mutation.
[Exact read-only batch](typescript-check-registry-propagation.py),
[brief](typescript-watch-registry-propagation.md),
[launcher](typescript-registry-propagation-watcher.log). Final acceptance will
compare public registry integrity and downloaded tarball bytes with the original
tag receipt; no public release claim until that comparison passes.

## Public verification completed

At **2026-10-30 13:05:31 UTC**, the version endpoint returned HTTP 200 and the
public tarball download completed. Parent independently checked:

- Package `vpsadmin-typescript-client`, version **0.2.0**.
- Public `dist.integrity` exactly equals the original accepted tag receipt's
  SHA512 integrity; downloaded SHA256, SHA512 and npm SHA1 all match.
- Downloaded public archive is **byte-for-byte identical** to artifact
  **12978397388**'s original tag archive, without rebuilding or repacking.
- Receipt source **e5786f69b7c223c3bb5b1de99b7f97186eec368a** and tag
  **v0.2.0**, embedded HaveAPI source
  **0e7166a0f8f15827bfac051666a53bf449e999ec**, package version, and runtime
  peer/dev **0.30.2** all agree.
- Fresh SSH proof preserves main/tag peel e5786f69 and annotated tag object
  **1b645b2190261268c566ed81c85543f4e51e6b55**.

Public npm metadata exposes the SLSA provenance attestation endpoint:
`https://registry.npmjs.org/-/npm/v1/attestations/vpsadmin-typescript-client@0.2.0`.
The successful publish log records GitHub Actions OIDC signing and transparency
log publication. No GitHub Release automation is expected for this repository.

Compact final [public verification receipt](typescript-publication-41059048868/public-verification.json),
[registry metadata](typescript-publication-41059048868/registry-available.json),
[downloaded public tarball](typescript-publication-41059048868/public-vpsadmin-typescript-client-0.2.0.tgz),
[download hashes](typescript-publication-41059048868/public-tarball-hashes.json),
[propagation watcher result](typescript-registry-propagation-report.md),
[publication watcher result](typescript-publication-watcher-report.md).

Initial 404s were an npm processing delay after successful acceptance. No
reupload, publish-job/workflow retry, token fallback, retag, rebuild, publisher
change or ref mutation was performed by this owner/utility. Original tag
artifact and receipt are preserved. Both observation utilities have stopped;
no unaccounted operation or claim remains. Lead was notified **PUBLIC VERIFIED**
and owns notification of consumer owner1 and session state/lifecycle handling.
