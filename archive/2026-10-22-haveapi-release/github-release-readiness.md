# HaveAPI GitHub release setup readiness

Read-only authenticated GitHub API observations at **2026-10-22 15:26:06 UTC**
by architect0. Session identity and both environment markers were reverified
against `2026-10-22-haveapi-release` and the bound workspace before this audit.
No settings, source, Git refs, secrets or workflows were changed. No credential
values or unrelated secret names were read or printed.

## Observed readiness

| Check | Result |
| --- | --- |
| HaveAPI `release` environment | Exists; HTTP 200; created/updated `2026-10-19T15:10:24Z` |
| Required reviewers | Configured: user `aither64`; rule ID `69339754` |
| Self-review | Allowed (`prevent_self_review: false`) |
| Administrator bypass | Allowed (`can_admins_bypass: true`) |
| Deployment restriction | Custom policy enabled; exactly one rule: type `tag`, pattern `v*`, policy ID `63593301`; no branch rule |
| `HAVEAPI_RELEASE_ENABLED` value | **Unverified: HTTP 403**; cannot establish that it is `true` |
| Environment secret name `HAVEAPI_PHP_DEPLOY_KEY` | **Unverified: HTTP 403**; existence/metadata unavailable; no secret value requested |
| PHP mirror repository | `vpsfreecz/haveapi-client-php` exists, is not archived, default branch `master`; metadata reports admin/maintain/push access |
| PHP mirror write deploy key | **Unverified: HTTP 403**; key metadata unavailable; no key material printed |
| PHP mirror Packagist webhook | **Unverified: HTTP 403**; hook configuration/delivery status unavailable |

The required environment reviewer and tag restriction are present. Self-review
and administrator bypass are policy choices permitted by the current release
procedure; this audit records their actual settings without changing them.
The source workflow separately checks activation and required reviewers.

The four denied reads are **access gaps, not evidence of missing configuration**.
Repository metadata advertising admin access does not establish permission for
these particular API endpoints. An authorized owner must confirm the activation
variable, named environment secret, mirror write deploy key and Packagist webhook
before release. This audit cannot prove that any configured secret corresponds
to a mirror key, or that Packagist has indexed a future release.

## Source endpoints

All requests were authenticated `gh api` GETs to `api.github.com`. Responses were
filtered before output; webhook URLs/key material/secret values were not printed.

| Endpoint | HTTP |
| --- | --- |
| `/repos/vpsfreecz/haveapi/environments/release` | 200 |
| `/repos/vpsfreecz/haveapi/environments/release/deployment-branch-policies?per_page=100` | 200 |
| `/repos/vpsfreecz/haveapi/actions/variables/HAVEAPI_RELEASE_ENABLED` | 403 |
| `/repos/vpsfreecz/haveapi/environments/release/secrets/HAVEAPI_PHP_DEPLOY_KEY` | 403 |
| `/repos/vpsfreecz/haveapi-client-php` | 200 |
| `/repos/vpsfreecz/haveapi-client-php/keys?per_page=100` | 403 |
| `/repos/vpsfreecz/haveapi-client-php/hooks?per_page=100` | 403 |

This short setup audit makes no registry account assertions and is not an
independent change review or publication authorization. Registry-specific
prerequisites remain in [registry-readiness.md](registry-readiness.md).
