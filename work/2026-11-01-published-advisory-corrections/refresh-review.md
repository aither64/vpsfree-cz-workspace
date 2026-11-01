# Affected API baseline refresh review

No Blocking, Important or Advisory finding was established in this bounded refresh. The HaveAPI 0.32.1 baseline is source-compatible with the reviewed advisory mutation and consumer contracts. The refreshed API and KB histories are consolidated and contain no migrations. This clears the affected review gate for runtime acceptance; it does not claim the pending API/KB suites passed.

## Scope, identity and limits

Reviewer0, retained independent review-purpose/read_only member, native thread 01a19801-1fc5-70e3-ba37-8c0952a89392; saved gpt-6.1-sol/xhigh on codex-lb, no override/fallback or substantive authorship. dev-session current printed 2026-11-01-published-advisory-corrections from its tracking directory. Both session environment variables were absent, consistent with the trusted binding.

Read api-refresh-review.md, fixture-rebase.md and ci-snapshot-1902.md in full; reread mandatory-change-review and the general/history and risk/compatibility references. Inspected actual Git ranges, installed old/new gems, relevant metadata/authorization/preparation/documentation owners and current consumer pins. The actual change revealed no further architecture concern requiring a broader lane. No nested agents, source/session-file writes, tests, builds, fetches, remote mutations, production requests, integration, deployment or lifecycle actions.

This supplements final-review.md for the changed API dependency baseline and refreshed history/pin only. The earlier modern findings and their lead-owned reconciliation in review-reconciliation.md remain separate evidence. I did not broadly rerun or certify modern/client remediation here.

## Exact ranges and independent history proof

Previously reviewed API range:
610a96f8ce523afbcd3e4374a70047dbe3264b0d..
218e3180896debd3006b9a0583e557286702761d.

Refreshed API range, target master:
097226b22edf8b59f80b5dfaa55265e9d0cac633..
c8efabeb01ccca66b19425ee429e834d23cf3688.

Complete new series:
1. e200ab369bbc85ee7e5837091379a2899a261688 — api: support guarded advisory corrections and lifecycle actions.
2. c8efabeb01ccca66b19425ee429e834d23cf3688 — webui: manage advisory corrections, retraction and deletion.

Actual merge base equals 097226b22edf8b59f80b5dfaa55265e9d0cac633; local HEAD equals the submitted head and worktree/index are clean. Full final feature inventory remains 22 paths, +1930/-146.

The new target is exactly one upstream commit beyond the old base. Its ten dependency/package/schema-export/docs paths do not overlap the feature's 22 paths. Independent git range-diff confirms A differs only in the accepted CVE fixture capitalization and B is equal. I also reconstructed the expected final blob/mode graph read-only from the new baseline plus the old reviewed feature, replacing only that fixture blob; it exactly matches the submitted final tree 135f6a75154f1e4387fc912db26a5c6ae1abed08. Binary legacy webui/tests patches are equal.

The lowercase fixture correction is justified by the existing unchanged model-derived format validator: HaveAPI validates the uppercase CVE regex before the model normalization callback. No runtime validator or accepted public input was relaxed. The old exact-head CI failure, two affected examples and artifact identities are recorded, not waived or called a successful rerun.

No obsolete intermediate approach/fixup remains in the refreshed two-commit series. The already-upstream HaveAPI update is part of its baseline, not a redundant feature dependency update to consolidate. The API feature adds no repeated dependency/input/generated update stream.

## HaveAPI input and compatibility inspection

Inspected both the repository v0.32.0-to-v0.32.1 delta and the actual prepared installed gems under:

worktrees/2026-11-01-published-advisory-corrections/vpsadmin/api/.gems/ruby/3.4.0/gems/.

The actual haveapi-0.32.0 versus haveapi-0.32.1 library tree differs only in haveapi/documentation_oauth.rb and haveapi/version.rb. Both installed documentation_oauth.rb files equal their respective tagged source. The installed haveapi-client and Go/Rust/TypeScript generator library deltas are version files only. Dependency constraints/gemset hashes and schema-export exact-version guards consistently select 0.32.1. The upstream package lock's Bundler metadata also changes; no unrelated gem version change was present in its actual diff.

Thus the advisory-critical behavior is byte-unchanged across installed frameworks: resource/action description graph, labeled include choices, parameter serialization/validation, ActiveRecord validator import, authentication and authorization preparation, request execution and error formatting. In particular:
- authenticated root OPTIONS still filters action authorization;
- endpoint OPTIONS still runs prepare, while root descriptions do not provide per-record preparation authority;
- expected_state remains a String with machine-keyed labeled choices, and required content revisions remain Integer metadata;
- existing namespaced request/DELETE input behavior is unchanged.

These preserve the client six-action capability check and the modern advisory-local capability helper already reviewed. The companion client uses its own direct JSON HTTP transport; modern HaveAPI npm provenance remains 0.32.0, and legacy Composer remains 0.32.0. The protocol stays 2.0; the old PHP/JS/Ruby client request implementations receive no functional change in this patch release. No consumer pin upgrade or advisory capability downgrade is required by this baseline.

The changed runtime owner is optional HTML-documentation OAuth. New switch_user_revoke_params accepts a static String-to-String map, copies/freezes it, and rejects replacement of client_id/client_secret/token/token_type_hint. Parameters are merged only after a validated Switch user request, not on ordinary sign-out, authorization or token exchange. Existing fixed HTTPS-origin, session, CSRF, strict switch selection, timeout and failure behavior remain. Added upstream tests cover these boundaries; they were inspected, not executed here.

The vpsAdmin example supplies close_sso=1 to that option while retaining switch_user's private setting/default false. Its existing revoke provider supports close_sso. Updated docs accurately explain closing shared SSO separately from other access-token validity and preserve existing logout preferences. This path does not alter advisory API authentication, scoped tokens, mutations or announcement mail.

The schema exporter's override, guard and CLI help now agree on 0.32.1 without changing its snapshot algorithm or public API schema contract. The optional documentation configuration must be rolled back with a compatible framework: older HaveAPI rejects the new option. Upstream docs explicitly retain that paired configuration/bundle rollback requirement. No persisted format or data migration is added.

## Refreshed KB pin

Reviewed range, target master:
ce2c8cd9358c3636e5d39343e595df813a0b197f..
beeb258c72f84105b73b75fc4837e18b87e81cf2.

The complete series is one commit, beeb258c72f84105b73b75fc4837e18b87e81cf2, Pin KB contracts to expanded advisory management. Actual merge base/HEAD match the supplied range, and worktree/index are clean.

Independently parsed and compared the old/new lock graph: only the vpsadmin node changes; all unrelated nodes, root follows and selected node input edges are equal. The five source/lock locations agree on c8efabeb01ccca66b19425ee429e834d23cf3688. Selected narHash is sha256-bdD4JMawiPB5vHk+vRtWElZQ1z8ru0Dc+YwuYXkcd5I=. Explicit vpsadminos remains 6bdf458fd9105379860234ff33d352e55844f08f. Capture provenance is byte-equivalent apart from the top-level selected source revision.

The entire delta is still the same five pin files, +8/-8. One final logical vpsadmin pin stream is consolidated in one commit; no superseded pin/fixup remains. There is no added page/capture/content or modern-app dependency. Existing zero-advisory-binding conclusion is unaffected by this metadata/dependency-only baseline change.

## Explicit migration and readiness conclusions

NO MIGRATIONS in the refreshed API feature range or KB range. No migration/schema/seed file is changed, and the new upstream baseline also introduces no migration. There are no intermediate migration versions requiring merge/release/deployment/external-use retention, obsolete compatibility migrations or database reset provisions to assess.

The refreshed feature introduces the final behavior directly and retains no obsolete unmerged implementation approach. Repeated dependency/pin consolidation is sound as described above. The one accepted fixture correction is folded into A; B is unchanged. Prior reviewed ranges remain evidence rather than claims that a substantive deployed revision was literally merged.

No new product scope, advisory public contract or architecture expansion was introduced by this refresh. Original rollout constraints remain: update active sync consumers before resuming writes, finish API rollout, avoid mixed API pools, and retain compatible UI/API write pairs. Software rollback does not reverse corrections/retraction; advisory deletion recovery requires backup.

## Remaining verification

Read receipts confirm actual 0.32.1 bundle preparation and metadata/i18n health, focused lint/syntax, mandatory hooks and pin parse/graph checks. These are evidence for their stated scope, not runtime acceptance. I independently verified source/history/object-graph and lock equivalence only; no tests were run.

The two previously failed membership examples have not been proven passing by this review. Full/core advisory API/model/concurrency and outage-plugin coverage, legacy browser acceptance and strict exact-source KB bin/check remain required on the new graph. New exact-head CI was listed as queued/running in the packet; no fresh CI success or remote-target verification is claimed here. Pending acceptance should use the new exact source/input identity, not reuse prior long-run results solely from patch equality.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
