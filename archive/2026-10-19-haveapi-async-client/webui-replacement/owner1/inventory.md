# Production WebUI source handoff

Exact head `8772bab21cd8739bf4672cdf4976aea2a6e59de3`, tree `3302fcf2bc01f1885426a69c7ddc364b8cdd35ad`. Working tree and index clean. Both author and committer are Jakub Skokan <jakub.skokan@havefun.cz>, verified in the actual pinned Nix context. No declared hook framework or active hooks; no bypass. Source commit owns exactly 62 paths, including real-package test support and strict E2E coverage adoption. Dependency commit owns its separate 22 paths.

## Complete series and history boundary

Base `7860521f30826c3886c89c35e8ab6f4e082e0a4b`. Last fetched main `b9f47f06e0877eb4a160053c413c4b87dd4a3d55`; merge base remains `7860521f30826c3886c89c35e8ab6f4e082e0a4b`. Main is 20 commits ahead of this original base. No fetch/rebase/publication was performed in this source package. The earlier incoming-scope report still applies; current remote state was not refreshed.

```
0d05a2584bf30ee4acfa1d64bf00325cdda62934 api: add injectable HaveAPI package pilot
5dd2333b9af230d4a81c8f772cbbb08d39b14913 docs: record HaveAPI package proof
3b2eed453f385ee37d07c7339edcce8fc28ffd31 api: install the HaveAPI client as a normal dependency
8772bab21cd8739bf4672cdf4976aea2a6e59de3 api: use HaveAPI AsyncClient in production
```

The first two commits contain the previously published pilot and historical evidence. The normal dependency and production implementation supersede that approach; the final tree has no pilot app, runner, optional client factory or duplicate wire transport/decoder. Their published history is retained under the lead's explicit current boundary. This is not a consolidated readiness claim: the lead/reviewer must disposition obsolete history before branch readiness. Original exact proof refs/results remain historical, with no reuse claim for changed production source.

No migrations: no backend schema, stored-session or persistent-state change; no migration was merged, released, deployed or externally consumed. There is one normal dependency update stream, selecting HaveAPI f94e65e and one vendor archive/root lock/Nix integration in 3b2eed4. The original pilot changed no normal dependency pins. No repeated final dependency/pin stream remains in the tree.

## Quick evidence and remaining checks

All 39 changed API test files/289 cases passed in 9.52s against the actual installed dependency. App/tooling types passed; strict E2E coverage is 61 checked/202 deferred. Docs inventory 257 routes/64 API modules; audit 118 documents/75 requirements. Tailwind/pattern, scoped lint/format and structural gates passed; complete diffcheck passed. Initial fixture failures and their corrections are retained in evidence/production-domain-quicks/.

Final independent review and long app tests/build/Nix/ordinary browsers remain pending. The approved ordinary browser selection is overview, news_compact, authenticated_home_smoke, session_expiry_redirect, header_session_limit, vps_create_failures, vps_create_admin_flow, blocking_action_progress_modal and action_state_detail_page, using the normal Playwright runner/Chromium, no retries, max failures 1. Normal app dev fixtures are separate from the default bff/minified production build check. No live OAuth/backend/deployment certification is claimed.

See full-final.diff, final-paths.txt and commit-receipt.json for the complete candidate, paths and hash. Session remains open; no push, PR mutation, merge, deployment or lifecycle action was performed.

## Final diff inventory

```
 WORK_LOG.md                                        |   8 +
 docs/design/API_CONTRACTS.md                       |  43 +++
 docs/design/ARCHITECTURE.md                        |  11 +-
 docs/design/DOMAIN_COVERAGE.md                     |   2 +-
 docs/design/HAVEAPI_CLIENT.md                      |  82 ++++++
 docs/design/IMPLEMENTATION_INVENTORY.md            |   2 +-
 docs/design/PACKAGING.md                           |  34 ++-
 docs/design/README.md                              |   2 +
 docs/design/REQUIREMENTS.md                        |   8 +-
 docs/design/VERIFICATION.md                        |  24 +-
 docs/work-log/2026-10-19-haveapi-package-pilot.md  | 160 ++++++++++++
 .../2026-10-20-haveapi-production-client.md        |  48 ++++
 e2e/fixtures/haveapi.ts                            |   6 +-
 e2e/specs/app/authenticated_home_smoke.spec.ts     |  13 +-
 e2e/specs/public/overview.spec.ts                  |  17 +-
 package-lock.json                                  |  19 ++
 package.json                                       |   3 +-
 packages/frontend.nix                              |   7 +-
 scripts/check-package-source.mjs                   |  30 +++
 scripts/check-package-source.test.mjs              |  38 +++
 scripts/fixtures/e2e-type-coverage.json            |   8 +-
 scripts/fixtures/structural-debt-ledger.json       |  14 -
 src/lib/api/audit.test.ts                          |   5 +-
 src/lib/api/clusterResourcePackages.test.ts        |  17 +-
 src/lib/api/datasets.test.ts                       |  27 +-
 src/lib/api/dns.test.ts                            |  25 +-
 src/lib/api/dnsResolvers.test.ts                   |   5 +-
 src/lib/api/exports.test.ts                        |  17 +-
 src/lib/api/finance.test.ts                        |  11 +-
 src/lib/api/haveapi.call.test.ts                   |  25 +-
 src/lib/api/haveapi.refresh.test.ts                |  19 +-
 src/lib/api/haveapi.ts                             | 272 +++++++------------
 src/lib/api/haveapiEnvelope.ts                     |  30 ---
 src/lib/api/haveapiRequestClient.test.ts           | 226 ++++++++++++++++
 src/lib/api/haveapiRequestClient.ts                |  64 +++++
 src/lib/api/incidents.test.ts                      |   5 +-
 src/lib/api/infra.test.ts                          |   5 +-
 src/lib/api/ipAddresses.test.ts                    |  59 +++--
 src/lib/api/mailer.test.ts                         |  25 +-
 src/lib/api/migrations.test.ts                     |   5 +-
 src/lib/api/networkInterfaces.test.ts              |  13 +-
 src/lib/api/networks.test.ts                       |   7 +-
 src/lib/api/nodeHistory.test.ts                    |  14 +-
 src/lib/api/nodes.test.ts                          |  49 ++--
 src/lib/api/oom.test.ts                            |   5 +-
 src/lib/api/outageScopePaging.test.ts              |   3 +-
 src/lib/api/outages.test.ts                        |  55 ++--
 src/lib/api/payments.test.ts                       |  27 +-
 src/lib/api/profile.test.ts                        |  11 +-
 src/lib/api/public.test.ts                         |  11 +-
 src/lib/api/public.ts                              |  71 +----
 src/lib/api/requests.test.ts                       |  34 +--
 src/lib/api/securityAdvisoryUpdates.test.ts        |   9 +-
 src/lib/api/systemConfig.test.ts                   |  13 +-
 src/lib/api/transactions.test.ts                   |  11 +-
 src/lib/api/userDossier.test.ts                    |  11 +-
 src/lib/api/userLookups.test.ts                    |   3 +-
 src/lib/api/userNamespaces.test.ts                 |   7 +-
 src/lib/api/users.test.ts                          |  25 +-
 src/lib/api/vps.blocking.test.ts                   |   7 +-
 src/lib/api/vps.test.ts                            |  43 +--
 src/lib/api/vpsAccess.test.ts                      |   5 +-
 src/lib/api/vpsFeatures.test.ts                    |   3 +-
 src/lib/api/vpsMounts.test.ts                      |   3 +-
 src/lib/api/vpsUserData.test.ts                    |   5 +-
 src/lib/errorMapping.ts                            |   2 +-
 src/test/haveapiXhr.ts                             | 106 ++++++++
 tsconfig.e2e.json                                  |   1 +
 vendor/README.md                                   |  12 +
 ...nt-f94e65e35166a0bf8048a27c9d57c7d36957d65b.tgz | Bin 0 -> 55702 bytes
 vendor/haveapi-client-provenance.json              | 290 +++++++++++++++++++++
 vitest.setup.ts                                    |   1 +
 72 files changed, 1661 insertions(+), 617 deletions(-)
```
