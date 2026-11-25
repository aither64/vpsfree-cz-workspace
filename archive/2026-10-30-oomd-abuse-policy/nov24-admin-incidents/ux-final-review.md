# Nov24 compact Incidents UX — independent final review

**One Important finding; no Blocking or additional Advisory findings.** React's affected source has no findings. PHP source acceptance remains conditional on UX-F1. Final geometry, browser interaction and deployment acceptance are still pending.

## UX-F1 — Important — Device-width pages retain off-screen fixed header controls

GENERAL/correctness and RISK/accessibility; affected PHP commit `b67983e7`.

`webui/public/template/css/admin-incidents.css:16`–29 switches the authorized Overview/History shell to device width, but does not constrain the inherited header children. `main.css:281` still sets `#slogan_wrap { width:1100px }`, and `#langbox` floats right inside that wrapper. The actual shared template places the language links there. At a390px viewport they remain near the far edge of the1100px wrapper and create document overflow. The authenticated header also retains `#logbox` width600 with absolute positioning and `#jumpto`'s100px offset (`main.css:152`–156). Changing only outer `.main` and header/nav minimum widths does not make these controls fit.

This violates the explicitly supported narrow-page contract introduced with the device-width override; it is not a request to redesign unrelated PHP pages. The current render receipts assert markup/meta/disclosure properties but contain no full authenticated mobile geometry proof.

Narrow correction: inside the existing narrow media query and `body[data-admin-incidents]` scope, allow header wrappers and authenticated control containers to fit/wrap naturally. Preserve language, session/logout, jump and navigation controls, zoom and discoverability. Do not change global CSS or hide overflow. Then perform the already planned390px mobile acceptance with the actual authenticated header/nav/sidebar and full document width, alongside1280px sidebar geometry. Owner4 retains the fix. Root acknowledged this finding and allocated9f98a141; in-flight fixes are outside this immutable-source report.

## Identity and reviewed scope

Verified `dev-session current` returns `2026-10-30-oomd-abuse-policy`; both identity environment variables are absent. Live roster44 confirms reviewer0/thread `01a18d34-69d3-74d2-ae70-df2584ed8a12`, saved `gpt-6.1-sol/xhigh/read_only`, execution `full_access`. Independent of authorship, with no overrides, fallback or nested reviewer.

Applied mandatory-change-review and all four lanes: GENERAL/history/documentation, ARCHITECTURE/REPETITION, SCOPE/PROPORTIONALITY, RISK/COMPATIBILITY. HIGH classification is retained conservatively for privileged saved decisions and current physical/mail outcomes. Read the current UX packets, plan/state and sufficient UX/viewport brief; reused unchanged applicable workspace/repository, synchronization, localization/locked terminology, writing and documentation guidance. Repository AGENTS bytes are unchanged from the previously reviewed bases.

Reviewed exact committed objects, initially clean, with final heads unchanged at completion:

| Repository | Full base | Final head | Final tree | Direct deployed parent |
| --- | --- | --- | --- | --- |
| vpsadmin, nonmounted vpsadmin-nov24-ux | 4062a8da3314aa7b48170b0d6f441446bad9b207 | b67983e7cdb4611447bf8f74db2b98c659d6c7a8 | 9546a6607141d3a16161afaff78d991c5d7d9deb | 8846c22b20d805ee3d63718d9d23a5be5319b4bf |
| vpsadmin-webui | 4499f90fe11df0e4df6f23e5fa54829e2254ec1b | d92652cb90b460b4bcf6adfc3e40922c90558196 | ac75aa77330b2fe0afaa02e07385627c86ea098e | ef6c72f4f626822e34934229170195f6d8091764 |

PHP new purpose changes10paths (+472/−314); React changes12paths (+607/−245), including supporting tests/catalogs/docs. Saved complete diffs match actual `git diff --binary` for both full ranges. Earlier review in final-review.md and accepted narrow remediations retain their exact original scope.

## Scope, architecture and correctness conclusions

The actual user asked for PHP sidebar navigation, a narrower vertical Overview, less density/text in React, removal of the quoted technical banners, and understandable History after inspecting deployed8846/ef6. Native disclosures, existing sidebar helpers and compact presentation are conventional, bounded solutions to that request. No new domain model, classifier, snapshot framework, transport/SDK fallback or global disclosure abstraction was added. The local viewport variable is necessary for the authorized narrow PHP shell and preserves the old1150 default elsewhere; UX-F1 completes that bounded accommodation.

PHP uses the established sidebar with preserved Overview/Reports/History semantic IDs and routes, including Reports list=1, existing Back/policy links and current-page marking. Vertical entries remove the wide matrix and100% content override. Only admin Overview/History loads the local CSS and device-width value; Reports/Show/New/member/unrelated routes retain their default assignment. Native details/summary provides keyboard operation without extra requests or JavaScript dependency.

React reduces Overview to four columns/mobile equivalents and shares count/status/outcome/disclosure components. Secondary controls remain mounted and enabled while More filters is closed. Active IDs, mode/permission (including explicitfalse), action/mail filters and nondefault direction open the disclosure and stay visibly marked. Outstanding still disables period fields. No local page-only sorting, membership changes or evaluator appears.

Both History presentations lead with source/time/VPS/policy, then separate the saved decision and count/threshold context from current action/mail outcomes. Decision none stays No action/Bez akce, without an invented reason. Error/skipped/audit-only and unknown/false membership remain visible when interpretation changes. Counts, periods, supplied remaining values and invalid limits remain distinct; a null permission is not rendered as false. Only the explicit completion timestamp supports confirmed shutdown; completed without it is Request completed. SMTP acceptance, pending/queued/suppressed/failed/uncertain/absent outcomes remain distinct. Shared physical identity, owner/deleted identity handling, timestamps and evidence links remain available in Details. Full detail labels such as Action state: Completed describe the request state without asserting physical confirmation.

The new summary helper is reused where semantics must agree; repeated desktop/mobile presentation uses the same owning components. PHP uses its existing API boundary and rendering helpers. No meaningful new duplicate authorization, evaluation or persistence logic was found. No architecture/scope finding beyond the concrete CSS failure was established.

## Frozen boundaries and compatibility

Independent path/blob inspection confirms PHP8846..b679 changes no API, schema, dependency lock, SDK, fixture or migration source. Reactef6..d926 leaves adapters/models/capabilities, controller/URL/cutoff logic, routes/sidebar, shared components/styles, manifest/locks/frontend dependency hash/provenance, flake and BFF unchanged. Earlier c27d..ef6 browser corrections/captures remain in their accepted owning UI purpose; this UX append does not relabel their evidence.

Old-API role/capability gates, query membership, server ordering, pagination, cutoff anchoring/Refresh and saved data semantics remain supported. The PHP viewport assignment preserves the existing default and static one-meta contract; UX-F1 qualifies narrow chrome. No API/client regeneration is warranted by these presentation changes. No persistence/engine behavior or deployment order is changed.

## Complete history, consolidation and migrations

PHP4062..b679 contains exactly three purposes: PHP926b, API8846 and UXb679. React4499..d926 contains exactly SDK5c291, UIef6 and UXd926. Both deployed parents are literal direct ancestors of their UX successor. These new UX purposes respond to a subsequent explicit user request after deployment, rather than preserving abandoned implementation attempts or appending redundant fixups. Keeping them separate is justified by that distinct delivered behavior/request boundary. Earlier fixes remain consolidated in their owning PHP/API/UI purposes.

No obsolete approach or redundant repeated dependency/input stream remains in these complete series. React has one unchanged SDK selection5c291; PHP adds no input stream. Prior deployed/ref/recovery identities remain literal, including retained ef6 evidence; no integrated/default history is rewritten.

**No new migrations in either full range or either UX delta.** Backend schema is byte-equal to4062. Consumed migration20261030180000 retains SHA256 `2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e`; obsolete20261115120000 is absent. No transitional migration or persisted-format change remains. The auxiliary client/archive and other delivery obligations from the prior combined review are unaffected.

## Documentation placement and preservation

All seven GENERAL questions were assessed:

1. PHP's existing docs index leads to incident-escalation.md; React's design handbook/workflow/REQ-051 and work log remain the appropriate entry points.
2. PHP UI semantics live with the backend/operator reference; React display/filter rules live in API_CONTRACTS/WORKFLOWS and its requirement register. Dated execution and pending acceptance belong in the existing work log/session packets.
3. Current guidance remains useful without private session context; the explicit post-deployment request and old screenshots retain their historical home.
4. Saved/current/no-reason/SMTP/completion statements match the reviewed presentation. PHP's stated narrow-screen adaptation is conditional on UX-F1 and later geometry acceptance; recorded quick results do not prove it.
5. Removing the requested visible banners did not remove their consequential cutoff, compatibility, recovery, mail or shared-stop contract from owning documentation. No supported safety requirement was silently retired.
6. Existing rollback/source-input, schema/data and staggered capability boundaries remain unchanged. The old rollout and preserved-data/Mailpit contracts retain their identities and applicability.
7. Authoritative explanations, existing links/anchors, terminology, machine identities and EN/CS placeholders are preserved. React adds16pairs and changes only the two approved existing values; PHP uses normal gettext maintenance. No member KB prose/media or semantic landmark change is introduced.

The docs are appropriately placed. No new product bundle, broad copy campaign or member media refresh is needed for the reviewed UX delta. KB's later mechanical final-source alignment remains separately owned; no wiki publication follows this review.

## Evidence and remaining gates

Inspected recorded PHP17tests/256assertions, four syntax checks, scoped formatting/catalog currentness, four actual EN/CS client/XTemplate renders and ordinary hook commit result0/70.868s. React's strict changed-source/real-import check,37focused tests and i18n/docs/lint/format checks passed in their recorded scope; later22view tests overlap. Original failures remain literal. I did not rerun any checks.

These prove source/fixture properties, not the new final browser geometry or a live deployment. Complete the narrow owner4 correction and focused verification, then the already planned EN/CS1280/390 collapsed/opened Details, active-filter, paging and Refresh acceptance. PHP mobile must use a context honoring viewport meta and include full authenticated chrome. React's current compressed desktop/mobile geometry and native disclosure interactions remain unexecuted.

Published compatible registry SDK adoption remains a React premerge prerequisite; this UX delta does not satisfy or waive it. No new frontend/system/VM build, CI success, current runtime acceptance, API/physical-stop/mail-delivery or KB-media result is inferred. Existing current live8846/ef6 and earlier source/rollout evidence remain scoped to those identities.

I performed only read-only inspection and wrote this requested report. No product tests/build/evaluation/browser/CI/runtime/source/ref/claim/default/publication/DB/deployment/lifecycle actions were launched. No command or uncertain effect remains. Root owns disposition and later authorized deployment; owner4/2 retain technical fixes. Narrow requested corrections need focused owner verification/root inspection, not an automatic whole-review rerun. Reviewer capacity returned.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)

