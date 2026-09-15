# IP release WebUI redesign review

Risk: high, because the changes add administrator actions over retained IP
allocations and expose separate administrator/member views. All four required
lanes use fresh gpt-6-astra contexts with xhigh reasoning.

Reviewed vpsAdmin `43530927dc814780e8b641fd5e5ce846bd9f4b79` on
`564cc80ea5d4420d0f2441c996fb0df2f82bb39c`; KB contracts
`2dfe4c7c3ba8e1e9675647eb100cf39e7a42ec3c`. Focused delta starts at
`d778e1b590a0cead8e7c39b8551bade88a28a2f8`; the first six runtime commits
were unchanged and had already completed the split-series review.

## General and architecture

Both lanes found the new Campaign.Exempt, Campaign.Address.Index and
Campaign.Notice.Index scopes missing from the endpoint coverage manifest.
This is Blocking for integration because the full API workflow requires every
scope to be registered. Added all three to covered_endpoints.yml; their request
specs already existed. The inventory spec with VPSADMIN_PLUGINS=all passes:
1 example, 0 failures, seed 8975.

General also found an Advisory inconsistency between restored row selections
and the Select all header after failed submissions. The form now initializes
header checked/indeterminate state from the selectable rows and uses the same
update function for later row changes. Empty tables disable the header.
Browser coverage checks partial creation selections after an invalid date and
all selected campaign rows after an invalid exemption reason. PHP syntax,
PHP-CS-Fixer, JavaScript syntax and whitespace checks passed.

Architecture reported no additional findings. Parameter definitions, batch
ownership, privacy, historical actor references, API client calls, navigation
and the exact KB pin were consistent.

## Risk and compatibility

**No Blocking, Important, or Advisory findings.**

Reviewed vpsAdmin `43530927d`, focusing on changes since `d778e1b5`, and KB `2dfe4c7c`.

The code supports campaign-scoped atomic exemptions, owner-scoped member access, admin-only actor fields, deleted-actor ID fallback, and serialization with release/close. CSRF checks and escaping remain intact. API-first deployment is documented; KB pins match the reviewed head.

Read-only checks passed: PHP/Ruby syntax, diff whitespace, and in-memory XTemplate rendering with 100-address admin/member forms, CSRF fields, actor privacy, and closed-campaign controls.

**Residual coverage gaps**

- [Concurrency tests](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsadmin/api/spec/models/ip_release_concurrency_spec.rb:234) use one-address batches. Multi-address interleavings and failure after an earlier row update are not directly exercised.
- [Deleted-actor tests](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsadmin/api/spec/api/resources/ip_release_campaign_spec.rb:59) use nonexistent actor IDs rather than actual account deletion.
- Database suites, browser integrations, and mixed-version rollout were not executed during this review. Their reported results come from the packet.

No files or external state were changed.

## Scope and proportionality

**No Blocking, Important, or Advisory findings in the scope and proportionality review.**

Reviewed vpsAdmin `43530927dc81`, focusing on the delta since `d778e1b5`, and KB `2dfe4c7c3ba8`.

### Assessment

- **The eight-commit split remains coherent.** The first six runtime trees are unchanged. Redesign behavior, tests and documentation remain in API commit `09f1ed102a` and WebUI commit `43530927dc`.
- **Bulk exemptions are proportionate to the accepted campaign-wide table.** The implementation reuses campaign and ordered row locks, validates campaign membership and release state, and updates within one transaction. The single-address endpoint delegates to it. No new locking framework or schema migration is introduced. ([Model, lines 91–111](https://github.com/vpsfreecz/vpsadmin/blob/09f1ed102a0d58c502c91080024e2be34fa79cd4/api/models/ip_release_campaign.rb#L91))
- **The added API surfaces preserve the intended boundaries.** Campaign lists and exemption actions require administrators; request lists remain owner-scoped. Raw retention/exemption actor IDs survive missing accounts and are excluded from member output.
- **Navigation, bulk selection and separate notice/release/close forms match the accepted redesign.** POST mutations retain CSRF checks; dynamic reasons and attribution are escaped. **Notice history** keeps its label. Closure explains that existing releases continue. ([Controller](https://github.com/vpsfreecz/vpsadmin/blob/43530927dc814780e8b641fd5e5ce846bd9f4b79/webui/pages/page_ip_release.php#L22))
- Deployment documentation specifies API-first rollout and discovery refresh. The KB commit changes pin metadata only and retains the existing OS dependency.

### Residual coverage gaps

I inspected the committed tests and independently checked rendering in memory: 100-address creation form boundaries, CSRF placement, failed-form selection preservation, escaping and deleted-actor visibility passed.

Database/concurrency suites, real browser behavior and the full KB check were not rerun here. The packet reports quick-check success; the redesigned browser scenario still requires runtime validation. Screenshot deliverables are outside the accepted scope.

The shared checkout advanced during review; this assessment remains limited to the requested committed heads.

## Reconciliation

The endpoint registration and checkbox restoration are narrow corrections
within the reviewed design, folded into the existing API and WebUI commits.
No additional reviewer pass is required for those corrections. The revised
browser flow remains required before live review handoff.

Remediated vpsAdmin head: `5e15045a67278569ef45fb5a2246291ff510887e`;
API commit: `2f2fefeb5`. The normal commit hooks passed and the explicit-lease
push succeeded. Hosted failure 104407949077 confirms the omitted endpoint
scopes; superseded 43530927 CI and API Specs runs were cancelled after the push.

General and architecture used collaboration agents. The retained collaboration
thread limit prevented another fresh reviewer, so risk and scope used fresh
read-only ephemeral Codex CLI contexts with the same model and effort, no
nested agents, no credentials and no cluster access. No review lane was omitted.

## Final validation

The browser integration passed on a75bb80d5 after the explicit-removal and
waiting-control corrections. All five Playwright tests passed; 1403.61 seconds
including build and teardown. See review-bulk-remove-results.md for the rerun
reviews and live cluster validation.
