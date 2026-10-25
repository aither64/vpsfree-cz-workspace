# HaveAPI 0.30.1 publication acceptance and recovery

Prepared by implementer2; execution and candidate approval remain lead-owned.
This is an operational checklist, not evidence of publication. Architect's
[release brief](release-0.30.1-plan.md) controls scope and ownership. Owner0 owns
Git, version metadata, tagging and shared setup; owner1 independently verifies
public destinations. The separate downstream Rust crate is outside publication
scope. No build, upload, approval, dispatch, rerun or settings change is requested
by this record.

## Binding and prerequisites

- [x] Session/environment match `2026-10-22-haveapi-release` in
  `/home/aither/workspace/ai/vpsfree.cz`; live roster revision 34 retains
  implementer2 as ready with workspace-write access.
- [x] Helper baseline reviewed at `090a188cb4ef3477324718627f4ae3415d1c0975`,
  tree `e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2`.
  [Exact helper/workflow hashes](release-0301-helper-baseline.json) bind the
  inspected files. This baseline still says 0.30.0 and is not a 0.30.1 artifact.
- [x] One [read-only snapshot](release-0301-publication-prerequisites.md) in
  owner0's prepared top shell, exit0 at 20:06:00 UTC. No observed 0.30.1
  registry/tag/release collision; protected reviewer and v* tag policy present.
  Enabled-variable GET403 leaves its value UNKNOWN. The prior offline shell
  stop remains [retained separately](release-0301-publication-prerequisites.json),
  without a registry conclusion. Do not repeat setup or probes independently.
- [ ] Confirm `HAVEAPI_RELEASE_ENABLED=true`, required reviewers and applicable
  tag policy on the protected `release` environment. Record denied access as
  unknown. Public metadata/source cannot prove registry account publisher
  settings unchanged; actual tagged-workflow/OIDC preflight is authoritative.
  Expected publisher tuple remains `vpsfreecz / haveapi / release.yml / release`.
  Read no credentials and change no settings. PHP deploy-key/known-host and
  mirror provenance checks remain required in the workflow.

## Candidate evidence before protected approval

All following identity fields are **pending owner0/tag-run handoff**: final
0.30.1 source, annotated tag object/peeled head, run/attempt, original artifact
ID/digest, manifest SHA-256, resolved tools/locks and every package hash. Never
substitute the development build or original 0.30.0 artifacts.

- [ ] Record supported `haveapi-0.30` ancestry, six accepted backport mappings,
  final version metadata, committed final review and quick-check receipts.
- [ ] Bind annotated `v0.30.1` to exact final source and the actual tagged run.
  Retain full successful build/test/package logs and reconcile known automatic
  CI failures before approval. A build-only run cannot prove publication.
- [ ] Preserve the original `release-<run-id>` artifact in a fresh
  `release-0.30.1-<run-id>/original-artifacts` directory. Verify manifest
  source/version/tag/run and every checksum before lead approves this candidate.
  Record Actions artifact ID/name/digest/expiry. No rebuild after approval.
- [ ] Inventory ten manifest payloads and eleven eventual GitHub assets:
  four gems (`haveapi-client`, `haveapi`, `haveapi-go-client`,
  `haveapi-rust-client`), npm `haveapi-client-0.30.1.tgz`, browser
  `haveapi-client.js`, `haveapi-client-php-0.30.1.tar`, `release-notes.md`,
  `haveapi_client-0.30.1-py3-none-any.whl`, `haveapi_client-0.30.1.tar.gz`,
  plus `release-manifest.json`. Any Actions-only smoke receipt is separate.
- [ ] Lead approves only the reviewed original candidate through the existing
  protected environment. Owner2 does not approve, publish locally or spoof CI.

## Ordered live evidence and independent destination proof

| Stage | Required observation against the original new artifact |
| --- | --- |
| Draft/preflight | Exact retained assets in private draft; all registry and PHP conflict checks before uploads; stage only missing original Python files. |
| PyPA | OIDC uploads staged files once; exact project/version, only the unique expected wheel/sdist filenames and both SHA-256 values. |
| RubyGems | Client, server, Go, Rust in order; exact name/version/platform `ruby` and each manifest SHA-256; no npm before Rust confirmation. |
| npm | Exact name/version and retained tarball SHA-512 integrity. |
| PHP | Atomic master/tag update, packaged snapshot paths/content/modes and Composer 0.30.1; `HaveAPI-Source: <actual final source>`; preserve mirror-owned metadata. |
| Final/GitHub | All registry confirmations under one shared deadline, then public release; all eleven assets and notes byte-match retained originals. |
| Packagist | Independently confirm exact 0.30.1 version/source ref after mirror indexing; indexing lag is distinct from push failure. |

Owner1 owns the independent one-pass destination verification under the
[existing protocol](release-destination-verification-plan.md), using the new
run and bytes. Preserve full exact public identities/hashes and uncertainty;
never install or execute registry downloads for this check.

The corrected helper retries **GETs only**: canonical no-cache metadata and,
after missing/valid incomplete metadata, at most one same-endpoint nonsecret
cache-distinct read per observation round. Transient preflight reads have a
60-second deadline; post-upload Python completeness and each gem/npm have
600 seconds; final validation shares 600 seconds. Backoff is 2/4/8/15/30 seconds,
with Retry-After as a minimum; zero/past/malformed values cannot remove positive
backoff. TLS/auth/schema/identity/platform/hash conflicts stop immediately.
Normal Net::HTTP proxy compatibility remains; publishing credentials never
enter these GETs. Retain phase/package/version/attempt/elapsed/status/missing
fields and bounded allowed cache/retry headers, without bodies or credentials.

## Failure-path coverage and recovery gate

The reviewed fake-clock/transport tests are retained evidence; this checklist
does not authorize running live failure injections or repeating those tests.

| Boundary | Existing deterministic evidence at the reviewed baseline |
| --- | --- |
| Cached negative, transient vs terminal, deadlines/Retry-After, HTTPS/proxy/header safety | `utils/release/spec/registry_query_spec.rb`: canonical/fresh pair, finite positive waits, shared deadline/no late request, no redirect/conflict masking or payload logging. |
| Strict file identity and staging | `utils/release/spec/publish_spec.rb`: partial/regressing/disjoint/404/transient views retain validated positives only for invocation-local staging; invocation reset/conflicts tested; one complete response required after upload/finally. |
| Accepted but unconfirmed | Publisher specs: no second upload, later npm/PHP/GitHub not attempted; exact tag/run/manifest recovery diagnostic. |
| Existing versions, PHP and retained artifacts | `utils/release/spec/release_spec.rb`: exact matches skip, conflicts stop before writes; mirror provenance/untagged changes guarded; original artifact restored on rerun, missing/expired accepted artifact refuses rebuild. |

[Final review](followups-final-review.md) independently passed 97 registry/
publisher examples; [owner receipt](followups-p1-receipt.md),
[extended verification](followups-verification-handoff.md) and
[seven exact-head CI results](followups-final-ci-receipt.md) retain supporting
evidence. New release quicks/review/tag-build evidence must be linked separately.

On failure, preserve exact source/tag/run/attempt, original artifact/manifest,
draft assets, all logs and accepted-upload timestamps. Inventory every logged
successful upload by exact original identity/hash before lead selects recovery.
**404 does not establish that upload failed.** Do not blindly reupload, move tags,
replace/rebuild bytes, use skip-existing or relax acceptance. Explicit failed-job
recovery uses the same run and original artifact; rerun-all also restores it.
Missing/expired accepted artifacts require retained original draft assets and
operator-assisted recovery, never substitution. A source fix requires a
separately authorized new patch version. Owner0 retains all mutation ownership.

## What a successful 0.30.1 can establish

Actual protected OIDC publication and strict final identity/hash confirmations
can demonstrate the fixed helper's real success path and ordered completion.
Preserve naturally occurring retry/cache-distinct logs and claim only the paths
they show. A clean first publication cannot experimentally establish delayed
visibility, timeout exhaustion, cache regression or failed-job skip/recovery;
those remain supported by deterministic tests and review. Do not manufacture
transient failures. The original PyPI incident's exact response is unknown;
the Rust incident established a cached negative followed later by matching
metadata/payload, without a simultaneous negative/positive control or proof
that a no-cache request caused recovery.

Next handoff: owner0 supplies the exact safe ready environment and final
candidate identity; lead coordinates tagged CI/protected approval; owner2 then
reconciles publication and any recovery evidence. No watcher is launched here.
A future fresh policy watcher may observe only the exact authorized run/head/
attempt, stop at the approval boundary, and preserve logs without rerunning it.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
