# HaveAPI 0.30.1 publication acceptance and recovery

Current authority, 2026-10-24: the user explicitly requested actual library-lock
removal, master integration, a supported 0.30 backport and release 0.30.1. Lead
routes execution under [library-lockfile-policy.md](library-lockfile-policy.md).
This authorization includes the lead's eventual protected-environment approval
of the **new reviewed candidate and its original tagged artifact**. It does not
approve old candidate 91, permit settings/credential changes or allow an approval
before those concrete identities exist.

This is a plan update only: no API/registry request, download, approval, dispatch,
rerun, setup or mutation ran. Candidate source/tree, tag object/peeled source,
new run/attempt, artifact ID/digest/expiry, original manifest and all new package
hashes remain **UNSET**. Owner0 owns Git/backport/version/tag/release actions;
owner1 owns coordinated environments and later independent destination evidence;
lead owns candidate acceptance, protected approval and recovery selection.
Owner2 prepares/diagnoses publication evidence when assigned. Separate downstream
Rust-crate publication is outside scope.

The earlier 090a prerequisite snapshot and old 91 build are historical evidence,
not current collision/configuration or new artifact proof. The pre-lock-policy
plan is preserved as
[release-0301-publication-acceptance-pre-library-locks.md](release-0301-publication-acceptance-pre-library-locks.md).

## Exact candidate and artifact gate

After actual master integration proof, owner0 supplies the new supported-release
base/head/tree, genuine backport mappings, final version/changelog metadata,
source inventory and required quick/final-review receipts. Do not assume old
six-commit counts or reuse an obsolete Version commit. Apply the accepted lock
policy: ordinary local resolution before checks, prepared `check-inputs`, all
nine actual dependency-lock records retained, and Rust packaged-lock verification
against the original manifest in a tools-only restored checkout. No resolution
is allowed while restoring or publishing original artifacts.

Before approval require all of the following, bound to one new candidate:

1. New final reviewed source is the actual 0.30.1 candidate, **not**
   old 91d4293e0c346f25aa04a6252e2b5ad0f9070263 or development 7ac. Required actual
   version-sensitive Go/Rust subset and affected-candidate build/test/package
   evidence must apply. The controlling
   [version-sensitive brief](release-version-sensitive-verification.md) remains
   applicable except for the explicitly superseding local-lock/tracked-path
   policy in the accepted library-lock brief.
2. Immutable annotated `v0.30.1` peels to that source; the exact tagged workflow
   run is `event=push`, repository vpsfreecz/haveapi, release.yml and matching head.
   Record run/attempt/jobs and the successful original build, with publish waiting
   at its protected environment. Never approve a similarly named build-only run.
3. Original Actions artifact is the run's `release-NEW_RUN_ID`, nonexpired, with
   exact artifact ID/name/digest/created/expiry and workflow-run identity. Preserve
   it in a new session-owned directory, never over old official/development bytes.
4. Its unchanged manifest records schema/version/tag/source/run identity and all
   ten payload checksums. Verify every byte, filename, type, package identity,
   declared dependency and retained prepared lock using the actual candidate
   verifier under a qualified tools-only environment. Retain the original
   manifest SHA and individual package hashes. Missing artifact/manifest/lock
   evidence blocks approval; no substitute rebuild or old 91 payload.
5. Record exactly eleven eventual GitHub assets: four gems (client, server, Go,
   Rust), npm tarball, browser bundle, PHP tar, release notes, Python wheel/sdist
   and manifest. Artifact-only smoke receipts remain separate, not extra packages.
6. Fresh preflight metadata has no unexplained identity/hash/source conflict.
   Existing exact published content is handled by the real helper's skip logic;
   any conflicting existing0.30.1 destination stops for lead diagnosis. Do not
   move a tag or overwrite an accepted registry version.

No new broad local/feature/tag verification campaign is prescribed here. Use the
lead-selected authoritative final-head campaign and its original bytes.

## Fresh read-only facts required after candidate/environment handoff

These are **future bounded GETs**, not commands executed by this plan. Owner0/1
coordinate one pass, preserve exact URL/status/timestamp/allowed headers/JSON
and distinguish present, missing, conflicting and unreadable. A403 is UNKNOWN,
not a successful configuration check. Existing retained snapshots are not fresh.

| Source | Exact GET/required fact |
| --- | --- |
| Release permission | `repos/vpsfreecz/haveapi/actions/variables/HAVEAPI_RELEASE_ENABLED`: value true; denied access remains unknown and actual tag preflight must establish readiness. |
| Protected environment | `repos/vpsfreecz/haveapi/environments/release` plus its `deployment-branch-policies`: actual environment ID, required reviewers and applicable v* tag policy. No settings write. |
| Tag/run binding | `repos/vpsfreecz/haveapi/git/ref/tags/v0.30.1`, then returned annotated-tag object; `actions/runs/NEW_RUN_ID`, its exact attempt jobs and artifacts: actual candidate head/event/workflow/attempt/build/artifact identities. |
| Approval boundary | `repos/vpsfreecz/haveapi/actions/runs/NEW_RUN_ID/pending_deployments`: exact release environment ID and current lead approver eligibility, bound to this waiting candidate. |
| RubyGems x4 | `https://rubygems.org/api/v2/rubygems/NAME/versions/0.30.1.json` for haveapi-client, haveapi, haveapi-go-client, haveapi-rust-client; strict name/version/platform ruby/SHA-256 versus each new original gem. |
| PyPI | `https://pypi.org/pypi/haveapi-client/0.30.1/json`: exact project/version and unique expected wheel/sdist names with original SHA-256. Missing, partial, duplicate/unexpected and conflicting are distinct. |
| npm | `https://registry.npmjs.org/haveapi-client/0.30.1`: exact package/version and expected sha512 integrity token computed from the original new tarball; retain its tarball URL. |
| PHP mirror | GitHub `repos/vpsfreecz/haveapi-client-php/commits/master`, `git/ref/tags/v0.30.1` and peeled commit if present: latest tagged provenance, target conflicts/untagged changes and exact HaveAPI-Source binding. Never push/reset in this read-only pass. |
| Packagist | `https://repo.packagist.org/p2/haveapi/client.json`: exact 0.30.1 record/source URL/ref when present; indexing absence is separate from mirror push state. |
| Draft/public Release | `repos/vpsfreecz/haveapi/releases/tags/v0.30.1`: release ID/tag/draft/publication/assets. Missing before preparation is not proof of later publication; a draft/public record alone is not package hash proof. |

Use explicit `gh api --method GET` for GitHub and only official HTTPS registry
hosts. Bound the individual request duration and retain the real outcome; do not
loop/poll or invent a transient failure. The accepted canonical/no-cache and
same-endpoint nonsecret cache-distinct confirmation policy belongs to the actual
publisher. Any additional diagnostic pair/pass is specifically lead-coordinated.
404 does not prove an earlier upload failed or establish PyPI name ownership.
Never inspect credentials/tokens/proxy settings, change publishers/variables/
secrets or infer account publisher configuration from public package metadata.
The expected trusted tuple is vpsfreecz/haveapi/release.yml/release; actual tagged
workflow/OIDC preflight remains authoritative where API visibility is limited.

## Exact protected approval command: lead only, after the gate

The user release direction authorizes this later lead action once the new
candidate/artifact gate passes. Read pending deployments immediately before it;
require the matching release environment and this exact new run/head/attempt.
The reviewable session `approval.json` must contain:

- `environment_ids`: an array containing only the fresh numeric ID of release;
- `state`: `approved`;
- `comment`: the exact reviewed source/run/attempt/original artifact/manifest SHA
  link or receipt identity, so the approved bytes are explicit.

The concrete command is:

```sh
gh api --method POST \
  "repos/vpsfreecz/haveapi/actions/runs/${NEW_TAG_RUN_ID}/pending_deployments" \
  --input /ABSOLUTE/NEW_CANDIDATE_EVIDENCE/approval.json
```

NEW_TAG_RUN_ID, approval.json and every candidate identity are **UNSET now**.
This command is not executed by owner2 or included in the read-only snapshot.
Never submit it for old 91, a build-only run, a different attempt/head, a missing
original tagged artifact, a conflicted version or an unreviewed candidate. Do not
use rerun/dispatch as an approval substitute. If actual permission/configuration
refuses, preserve the response and return the concrete blocker to lead without
credential or settings changes.

A fresh policy watcher may observe the one exact authorized run/attempt and
retain logs. The lead owns this mutation driver; the watcher never approves or
reruns. No watcher is launched by the plan.

## Ordered publication and one independent terminal pass

| Stage | Required evidence against the new original artifact |
| --- | --- |
| Draft/preflight | Original exact assets retained in draft; all registry/PHP conflicts checked before uploads; only missing original Python files staged. |
| PyPA | OIDC action uploads staged original files once; helper confirms both exact wheel/sdist identities and hashes. |
| RubyGems | Client, server, Go, Rust in order; exact names/versions/platform ruby/manifest SHA. No npm before Rust confirmation. |
| npm | Exact package/version and original tarball SHA-512 integrity. |
| PHP | Atomic master/tag update; exact packaged paths/contents/modes and Composer 0.30.1; full HaveAPI-Source final commit; mirror-owned metadata preserved. |
| Final/GitHub | One shared final confirmation deadline, then draft becomes public; all eleven downloaded assets and notes match originals. |
| Packagist | Independent exact 0.30.1/source ref after indexing; lag reported separately. |

Apply [the destination protocol](release-destination-verification-plan.md) with
**new 0.30.1 identities only**; that historical 0.30.0 document does not supply
current inputs. After terminal publication, the assigned owner performs one
read-only pass: exact registry identity/hash checks, PHP immutable commit snapshot
path/content/mode comparison, Packagist source ref, public release flags/body and
all eleven original asset hashes. Public downloads go to a new separate evidence
directory and are never installed or executed. Record every comparison and
uncertainty; no polling/reupload/settings/Git mutation. An extra follow-up needs
lead coordination. Registry/workflow success alone is not whole-release proof.

## Bounded confirmation and recovery

The reviewed helper retries **GETs only**. It uses canonical no-cache metadata
and at most one same-endpoint cache-distinct read for missing/valid incomplete
metadata per observation round. Transient preflight reads have 60s; post-upload
Python completeness and each gem/npm confirmation have 600s; final destinations
share 600s. Positive backoff is 2/4/8/15/30s with valid Retry-After as a minimum.
TLS/auth/schema/identity/platform/digest conflicts remain immediately fatal;
normal Net::HTTP proxy behavior remains, without publishing credentials in GETs.
Retain bounded phase/package/version/attempt/elapsed/status/missing diagnostics
and allowed cache/retry headers, never payload bodies/auth/full environment.

PyPI invocation-local strict positive union affects staging only. Later 404 or
smaller matching views cannot schedule a known-present file for reupload. Every
response still validates strictly; post-upload/final completion requires **one
complete response**, never union-derived success. No durable journal or upload
retry loop is introduced by this plan.

The deterministic fake clock/transport/control tests and reviewed recovery
semantics are prior evidence; fresh affected-candidate quick/review/build results
must be linked separately. On any failure preserve source/tag/run/attempt,
original artifact/manifest/draft, full logs and upload timestamps. Inventory all
logged successful or uncertain uploads against original identity/hashes before
lead selects an explicit same-run original-artifact failed-job recovery. Never
blindly reupload, use skip-existing, move tags, rebuild accepted bytes, mask a
conflict or treat a cache-distinct 404 as upload-failure proof. Missing/expired
Actions artifacts require retained original draft assets/operator recovery;
if no originals remain, a separately prepared version is required.

A successful clean publication proves the actual ordered success path and strict
final identities. Claim naturally occurring retry/recovery paths only if captured;
clean success cannot experimentally prove visibility delays, timeout exhaustion
or failed-job skip/recovery. Do not inject live failures. The old PyPI response
was not retained; its exact cache cause remains unknown. The original Rust
incident proves a cached negative followed later by correct payload/metadata,
not that no-cache caused recovery. Preserve those causal limits.

Next handoff: owner0/1 supply the exact safe candidate-bound environment and new
source/tag/run/original artifact identities. Until then all fresh facts and
approval payloads remain pending; no API or publication operation is active.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
