# Source-backed migration corrections

Design decisions for the migration, 2026-11-01. API source is
`610a96f8ce523afbcd3e4374a70047dbe3264b0d`; HaveAPI validation source is
`209a7ac0c2fe6cd1b78735f50b5e60d979309543`. Domain owners3–7 independently traced
their assigned declarations, execution and existing specs; architect reconciled
the decisions. This is source evidence, not a live API test or implementation
completion claim. No demonstrated exporter defect was found in these cases.

These are corrections needed to use the actual contract, not new backend
features. They do not block work on the generator, generated client or shared
executor. Lead releases domain execution after the pilot and owns user-facing
prose. Owners must follow
local localization/KB impact guidance before visible behavior edits, reuse keys
only when accurate, and send new wording to lead.

## Shared rules

HaveAPI `parameters/typed.rb:46–47,87–100,158–161` permits explicit null only for
explicitly nullable optional input. Omission is different from clearing. Schema
types form the maximum supported input surface; live metadata/permissions can
restrict it further. Never widen generator input or cast merely because a page
used to send null. A future incompatible/expanded live profile needs refreshed
generated support, not a generic raw-request escape.

Generated outputs preserve unknown/absent values. Do not invent current-session
identity, recipient roles, entity IDs or content revisions to fit UI models.
Canonical wire envelopes replace old fixture namespace guesses.

## Domain dispositions and ownership

| Area / owner | Source evidence | Required migration behavior / visible effect |
| --- | --- | --- |
| Host-IP assignment — i4 API/admin, i3 VPS page | `api/lib/vpsadmin/api/resources/host_ip_address.rb` Assign has no input; it uses `host.ip_address.network_interface`. Specs `host_ip_address_spec.rb:680–778` post an empty input. | Call generated Assign with path only. Confirm the existing parent interface and routed eligibility. Remove arbitrary target-interface/VPS selectors; never add an implicit routing write. i3 alone edits `VpsNetworkPage`; i4 owns `IpAddressDetailPage` and `admin/networking/HostIpAddressesPage`, and sends i3 its API contract. |
| Traffic text search — i4 | NetworkInterfaceAccounting UserTop declares environment/location/node/date/limit/from_bytes, no q; specs `network_interface_accounting_spec.rb:516–592` cover these filters. | Remove q from adapter and `NetworkTrafficUsersPage` search/URL contract; keep real date/scope filters and byte pagination. Reset old q URLs visibly. Do not substitute an undocumented loaded-page search. |
| Environment/location text search — i6 | `environment.rb:30–35` and `location.rb:32–54` declare structured filters, no q; active admin pages do not filter returned rows locally. | Remove ineffective q controls, adapter inputs and URL/smart-search aliases. Preserve real filters and use the existing accurate stale-filter reset notice. No new loaded-page search or backend filter. |
| DNS host lookup — i4/i3 | HostIpAddress Index uses exact `addr`, with spec `host_ip_address_spec.rb:204–222`; duplicate q helper in `dnsTransfers` has no production caller. | Remove the unused duplicate helper/q. Preserve the actual `exports` exact-address/eligibility flow, owned by i3; coordinate imports rather than edit its files concurrently. No intended visible DNS change. |
| User-data search — i3 | `vps_user_data.rb:23–45` declares/applies user/format only. `UserDataTemplatesPanel` forwards q without local filtering; E2E fixture invents q support. | Remove unsupported text search and q/search/label/id search aliases; retain server owner/format filters, initialization picker behavior and pagination. Explain/reset old q URL state. Chosen scope is removal, not a new page-local search. |
| VPS clone descendants — i3 | `vps.rb:908–927` has no subdatasets input; `api/models/transaction_chains/vps/clone/os_to_os.rb:170–172,355–371` traverses source-pool descendants without that flag. | Remove the selector, draft/default and payload field from `VpsCloneModel`/`VpsCloneCard` and the adapter. Preserve declared options. Existing Subdatasets summary label becomes an unconditional fact, so copied-parts review never implies this tree can be excluded. Do not broaden this to unrelated external datasets or mounts. No generated client widening or silently discarded false. |
| Dataset list conveniences — i3 | `dataset.rb:42–50` has no without_snapshot_in/reversed; owner inventory found no production callers of these adapter options. | Remove the unused options and wire keys without adding a replacement or changing visible behavior. |
| OS template filters and picker eligibility — i3 | `os_template.rb:39–41` declares location/family/hypervisor/cgroup/script/cloud-init filters, not q/enabled/supported. `:48–54` restricts nonadmin Index to enabled templates and omits enabled from their output; admins receive the field. | Remove ineffective admin filters/URL aliases but retain real filters and output fields. VPS pickers use the actual authenticated API role, not interface mode: admins require enabled:true; a known nonadmin Index may omit enabled because of server restriction. Explicit false/null or unknown scope is unavailable. Preserve scope-bound caches, selection checks and raw-page cursor/count provenance; local eligibility filtering is not a collection search or completeness claim. |
| Mount controls and edit fields — i3 | `vps.rb:1330–1347,1407–1414,1462–1464` has no type/use_default_map. Create permits mountpoint/mode but not master_enabled; Update permits only on_start_fail/enabled/master_enabled. `MountDataset:34–55` chooses mount type internally. | Remove invented type/default-map controls, defaults, summaries and wire fields. Keep mountpoint/mode on create and read-only on edit; master_enabled is admin edit only. Do not translate the removed boolean into a namespace-map mutation or add mapping UI. No implicit delete/recreate. Missing labels/history counts remain unknown rather than fabricated wire fields. |
| VPS disk history — i3 | `vps.rb:1849–1872` Status output contains memory/swap/CPU but no disk fields; current VPS output has diskspace/used_diskspace. | Retain current disk values and use existing unavailable/empty historical-chart behavior. Remove invented historical wire fields and series; never project the current reading across history or replace missing readings with zero. |
| User-create monthly payment — i5 | `user.rb:9–45,126–130` omits monthly_payment; payments `resources/override.rb` adds it to read outputs only. `plugins/payments/api/resources/user_account.rb:6–8,60–79` exposes the separate update. | Remove the ineffective creation control, draft/default 300, validation and payload in `UsersModel`/`UsersCreateModal` and owned adapter/tests. Keep explicit account editing after creation; no hidden second write or promised backend default amount. |
| TOTP confirmation — i5 | `user.rb:917–950` declares hash output and returns recovery_code. HaveAPI `params.rb:112–123`, `action.rb:482–508` frame it under `totp_device`. | Read generated `data.recovery_code` and retain nonempty secret guards. Canonicalize fixtures; scalar/alternate envelope shapes fail rather than being guessed. |
| Account paid date — i5 | `plugins/payments/api/resources/user_account.rb:6–8,75–85` has nonnullable paid_until; omission leaves it unchanged, a valid date updates account and user expiration. | `AdminUserPaymentsPage` allows valid date updates and unchanged omission; reject a requested populated-date clear visibly. No sentinel, silently omitted clear or backend extension. i5 owns this page and `profile.test.ts`; i7 does not edit them. |
| Reminder clear — i5 user, i3 VPS | `lifetimes.rb:217–223,358–374,581–593`: expiration_date nullable, reminder nonnullable; setting expiration resets reminder to supplied value or nil. | Clear reminder using the observed expiration_date with reminder omitted; expiration_date:null clears both. Preserve a nonnull reminder explicitly when changing expiration should retain it. Reuse existing lifecycle helper semantics. User page needs correction; active VPS lifecycle code already does this. Replace only the stale VPS null-reminder fixture. Do not claim an atomic compare-and-swap guarantee for lifecycle setters. |
| Lifetime state-log pagination — i6 API, i3 shared panel, i5 user props | `lifetimes.rb:170–183` orders by created_at ascending; HaveAPI `model_adapters/active_record.rb:48–62,79–95` filters id greater than from_id without imposing ID order. Offset is unsupported; ObjectState supplies no timestamp/ID ordering guarantee. | Show one bounded initial batch with existing limit 50. Remove offset/prev-next from `LifecyclePanel`; do not derive an ID cursor from timestamp order, scan automatically or claim lossless continuation. This is earliest chronological history, not latest or necessarily complete. Lead replaces the existing inaccurate pagination hint with honest bounded-history wording. i3 alone edits panel/tests for both kinds; i6 keeps limit-only helpers/full receipts, i5 owns surrounding user-page props. |
| Session identity / mail recipients — i5 | `user_session.rb:6–26` omits current; model's current is server thread-local. `user.rb:1453–1458` recipient output has id,label,description,to,enabled, not roles. | Omit fabricated current-session badges/count assumptions; keep ordinary close confirmation/token safeguards. Where empty to requires unavailable role information, show destination unknown rather than asserting a primary-address fallback. No member-side extra admin fetch or local role map. |
| Settings route — i5/W | `plugins/webui/api/resources/webui_user_setting.rb` declares canonical collection and namespace/key paths only; runtime config's arbitrary substring paths have no matching server contract. | Use generated canonical paths; API base owns mount/version. Keep settings namespace/key configurable. Accept canonical path with benign trailing slash normalization; reject other resource-path config before send with visible server-sync configuration failure. Do not silently ignore it, guess another endpoint or add handwritten generated client routes. W owns shared config/docs; i5 owns adapter. |
| HelpBox language — i7 | `plugins/webui/api/resources/help_box.rb:22–31,72–94,170–171,192–195` declares nonnullable language; omission on create yields no language, omission on update preserves it, omission on admin filter selects all. | Unlocalized create omits language. Remove ineffective unlocalized-only server filter/reset stale filter visibly. Prevent localized→unlocalized update clear; unchanged language can be omitted, existing unlocalized records stay valid, real language-ID changes remain supported. Never turn clear/filter requests into silent omission. |
| Outage entity / news timestamp — i7 | `outage.rb:327–330,409–414` reads optional entity_id, omission yields nil for Cluster/custom. NewsLog published_at is nonnullable; active editor already supplies valid timestamps. | Preserve desired omitted entity_id instead of adding null. Remove unsupported inactive timestamp-null helper convenience; active news behavior unchanged. |
| Payment replies — i7 | Payment GetPaymentInstructions returns `{instructions: rendered HTML}` as hash; PaymentStats is singular `/payment_stat`, with user_count/estimated_income hash. Legacy specs accepting multiple shapes do not prove multiple wire contracts. | Use generated user instructions/payment_stat namespaces and typed fields; retain HTML handling policy. Remove raw string/plural namespace guesses and misleading fixtures. |
| Public outage/news views — i7 domain, W public adapter | Public Outage blacklists admin counts; Handler.user is absent for nonadmin (`outage.rb:463–466,493–496`). News public reads exclude future records; localized message is read-only. | i7 owns generated-backed domain view helpers in outages/newslog; W owns `public.ts` and reuses them. Validate identity, allow absent optional public fields; admin handler writes require actual user.id. Do not preserve fixture-only user_id. Keep translated editing fields separate from localized display message. |
| Registration correction / template choices — i7 | Requests plugin `plugins/requests/api/resources/registration.rb:78–128` makes token Preview/Update public, constrained by id/access_token/pending_correction. Its `resources/override.rb` opens Location Index/Show, OsTemplate Index/Show and Language Index; anonymous template reads restrict enabled and supported to true, returning only id/name/label/hypervisor_type. | Correction actions and all three dropdowns use getPublicApi even in a signed-in browser, with separate public caches and no authenticated retry. i7 owns explicit public correction lookup helpers in requests.ts, using generated actions and narrow option views/receipts. Public template rows rely on this exact server restriction, not a fictional member role or fabricated flags. Authenticated RequestResolveResources instead filters actual enabled:true and supported:true locally after removing unsupported wire flags. A retained current-reference display is not proof of eligibility. Require an eligible fetched template for public correction submission, admin VPS provisioning or an explicit template change; do not block request-correction/deny/ignore or approval without VPS and without template change solely because the unchanged template is unavailable. No edits to shared executor/public.ts are required. |
| Node limits — i6 | `node.rb:21–29,344,366` defines max_tx/max_rx/max_vps nonnullable; the current live-nullable UI branch is hypothetical compatibility. | Accept valid numbers including zero; omit unchanged/unset fields; populated null-clears are unavailable with this generated client contract. A live nullable discrepancy does not license casting. Other edits and node capability pilot continue. |
| Advisory node notes — i6 | `security_advisory.rb:428–435` declares optional nullable locale notes; `:475–483` processes only present keys, with Create/Update using this helper. | Replace nonexistent generic note with separate cs/en drafts mapped to cs_note/en_note and each locale's own output. Reuse accurate Note/language labels. Blank create can omit; unchanged update omits, deliberate clear sends null for that locale only. Never overwrite an unread note with an automatic blank or copy text between languages. Preserve capability/profile and revision rules below; no generic locale framework. |

## Advisory concurrency and locale contract — i6

The lead accepted this boundary. It belongs to the advisory domain phase, not the
initial node capability pilot.

`security_advisory.rb:53–56,65,105–109,323,354` and
`models/security_advisory.rb:62,125` establish required revision preconditions,
409 conflicts, row locking and a single draft revision increment. The same parent
revision is required for existing CVE and NodeStatus create/update/delete flows.

- Freeze the server revision and reviewed parent/child data when opening the
  editor or confirmation. Require a nonnegative safe integer, including genuine
  zero. Missing/null/malformed revision makes writes unavailable; do not default.
- Preserve unsaved form values when query props refetch. Preflight compares fresh
  state/revision to the frozen baseline; submit that baseline revision. Never
  stamp a freshly fetched revision onto old text or replay a rejected write.
- A stale/draft conflict keeps the draft for explicit reload/review/merge. A
  valid returned parent-update revision can become the next observed revision.
- Serialize existing child writes; remove the CVE `Promise.all`. Child receipts
  lack parent revision, so after each accepted mutation read exact parent Show.
  Continue only if the actual observed revision is the documented single step
  above the previous one and state is still correct. The expected increment is
  a comparison, never a synthesized revision sent to the server.
- Intervening writes, failed read-back or uncertain outcomes stop the sequence.
  Retain completed subset and remaining intention; reconcile before retry. The
  multi-call operation is not atomic and feedback must not suggest otherwise.
- Required locale summaries are real fetched values explicitly mapped to the
  generated cs/en fields. Advisory draft Create and AdvisoryUpdate Create/text
  Update require all declared summaries; parent draft Update permits partial
  fields. Missing required locale values are validation errors. A live required
  language profile outside the generated snapshot is visibly unsupported until
  regeneration; never synthesize translations or pass arbitrary locale records
  with a cast.

Focused acceptance adds required/missing/zero/stale revisions, refetch-preserved
drafts, child serialization and unexpected revision progression, partial outcomes,
canonical DTO/envelope cases and input negative checks to existing suites. These
checks remain owned by each implementation package and do not claim completion
until run. No API behavior/schema changes are authorized by this record.
