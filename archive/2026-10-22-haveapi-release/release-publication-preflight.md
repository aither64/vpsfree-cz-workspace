# HaveAPI 0.30.0 publication preflight

Read-only observation: 2026-10-22 20:22 UTC. Session/environment binding and
retained implementer1 access matched. Read workspace verification/Git procedures,
HaveAPI AGENTS/development/releases, actual `release.yml` and publisher/workflow/
artifact helpers. No credential contents were read. No source/index/hook/ref,
configuration, registry, workflow or tag mutation occurred. No downstream action.
Detailed official API receipts: [release-publication-preflight.json](release-publication-preflight.json).

## GitHub approval and setup gates

- Authenticated account: **aither64**. HaveAPI repository metadata reports admin,
  maintain and push access; default branch is master.
- Environment **release**, exact ID **24722193856**, exists. Required reviewer:
  **aither64**. `prevent_self_review=false`, `can_admins_bypass=true`.
  Deployment policy permits tags matching **v*** only. Use normal reviewer
  approval; bypass is unnecessary and was not attempted.
- The account is an eligible reviewer. API approval capability is not proven by
  repository admin status: the current credential's write permissions were not
  exercised. The official [pending-deployment review API](https://docs.github.com/en/rest/actions/workflow-runs#review-pending-deployments-for-a-workflow-run)
  requires a required reviewer plus fine-grained **Deployments: write**, or a
  classic token with `repo` scope. Inspect the future exact run's pending
  deployments and `current_user_can_approve`; browser approval by aither64 is an
  alternative. No pending 0.30.0 deployment exists yet.
- GET `actions/variables/HAVEAPI_RELEASE_ENABLED` returned **403 Resource not
  accessible by personal access token**. Its value remains unverified. The
  later tag build's `check-activation` is authoritative and requires literal
  `true` plus a nonempty required-reviewer rule. This read limitation does not
  block the separately authorized merge.
- Environment-secret name metadata and PHP mirror deploy-key metadata also
  returned 403. Presence, correctness and write scope of
  `HAVEAPI_PHP_DEPLOY_KEY` remain unverified; no secret/key content was requested.
- npm setup is accepted per the user's assurance. RubyGems/PyPI account trusted
  publisher entries remain **unverified**. Their public APIs cannot establish
  account configuration, name availability or pending publisher ownership.
  The new Rust generator gem and initial Python project support pending
  publishers as documented in [registry-readiness.md](registry-readiness.md).

## Public conflict and PHP checks

| Destination | Observed 0.30.0 state |
| --- | --- |
| HaveAPI GitHub `v0.30.0` tag and Release | Both API lookups 404 |
| RubyGems haveapi-client, haveapi, haveapi-go-client, haveapi-rust-client | All exact-version APIs 404 |
| npm haveapi-client | Exact version 404; latest 0.29.12, canonical repository vpsfreecz/haveapi |
| PyPI haveapi-client | Exact version and project APIs 404 |
| PHP mirror `v0.30.0` tag | 404 |

These results show no observed target-version conflict; they do not reserve
names or prove publication authorization. Recheck immediately before writes.

PHP mirror master is `84c46343171d3839c5de011035d96a0f50425a86`, matching
`v0.29.12`. Its composer package is `haveapi/client` version 0.29.12, below
0.30.0. Its commit records `HaveAPI-Source: 355c2990a4bfd3940d3234cb2077ad0127f43551`.
[Packagist metadata](https://repo.packagist.org/p2/haveapi/client.json) lists the
same 0.29.12 source. Public metadata passes the no-untagged-master/backward-version
checks in principle. Full PHP preflight still needs the protected job's deploy
key and retained exact PHP snapshot: it checks source/content conflicts,
preserves mirror-owned AGENTS/.github and later pushes master+tag atomically.
The webhook configuration and future Packagist indexing remain unverified.

## Exact release path and source constraints

1. Implementer0 performs the authorized integration and prepares **haveapi-0.30**
   from approved master before tagging. Observed newest release branch is
   haveapi-0.29; haveapi-0.30 is absent. `Artifacts#check_tag` requires version
   0.30 to equal the newest release line, exact local/remote tag source equality,
   and tagged source ancestry in `origin/haveapi-0.30`. The workflow must exist
   in the tagged source; install it on master and the supported release branch.
2. An annotated **v0.30.0** tag push in vpsfreecz/haveapi triggers the release
   workflow. Branch pushes, PRs and workflow_dispatch are build-only; dispatch
   cannot substitute for a tag publication. Tagged releases serialize through
   `haveapi-release` concurrency.
3. The tag build checks clean/version/branch/tag and activation, tests/builds or
   restores original artifacts, verifies the manifest and retains
   **release-<run-id>** for 90 days. Review its test results, candidate summary,
   source/version/manifest/checksums and artifact identity before approval.
4. The publish job waits on protected **release** ID **24722193856**. Lead
   coordinates exact-run approval through **Review deployments → release →
   Approve and deploy**, or the authorized API after confirming reviewer/token
   capability. Only this job receives contents:write and id-token:write.
5. It downloads the retained artifact ID, verifies bytes, prepares draft Release
   assets, configures RubyGems OIDC, then preflights PHP, all four gem hashes,
   npm integrity and PyPI files. It stages only missing Python files; official
   PyPA OIDC uploads them. The helper confirms Python, pushes Ruby client before
   dependent server/Go/Rust gems, publishes npm, atomically syncs PHP and makes
   the GitHub Release public only after destination confirmation. No rebuild
   follows approval. Packagist indexing is a separate confirmation.

Do not invoke `pypi-prepare`, `github-prepare` or `publish` as a harmless local
preflight: they stage or write and require the tagged Actions job. Safe current
preflight is official metadata plus helper inspection; exact protected-job checks
remain the authority. Recovery preserves original tag/artifacts and refuses hash
conflicts or missing original uploads; source corrections require a new patch
version rather than moving a tag/replacing published bytes.

Lead owns publication coordination. Implementer0 owns Git operations. This
package ends at this receipt; no launch, approval, polling or configuration edit.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
