# Inventory refinement finding dispositions

Reviewer0 completed the original four-lane whole-branch review at
Vcc8e9e7e / Wa9d0b5e9 / C525c02fe / K819c4824: no Blocking findings,
one Important and one Advisory. The pending tooltip correction is excluded.
See network-counter-review1-result.md for evidence and history conclusions.

## Tooltip clipping: Important, GENERAL

Original W a9d0b5e9402faafef937894f50463da3c27e8935.
NetworkCountLabel in NetworksPage:120 places descriptions inside TableCard's
overflow-x-auto viewport and Card's clipped container. Native hosted pictures
show incomplete count descriptions despite passing visibility assertions.
Reviewer source inspection also identifies the new disabled-IP description
at IpAddressesListTable:182 in that same clipped viewport; a final-row case
can hide its focused description.

Disposition: fix within the accepted presentation boundary. Architect owns
the minimal shared inventory hint contract; implementer owns scoped code and
bilingual geometry/clipping regressions in existing hosted smoke. Preserve
copy, table/card layouts, IDs and count semantics; no dependency/framework,
global Badge rewrite, ledger waiver, filter, API or schema change. No local
CI/tests/builds. Root will inspect final correction, normal amend/publish,
verify hosted current-head evidence and update exact consumer pins. Review
continues against original committed snapshots and excludes mutable fixes.

Other completed source reviews and the accepted W shared-OPTIONS timeout
Advisory remain separately recorded; this remediation does not resolve that
availability/feedback issue.

## Disabled-network policy error response: Advisory, GENERAL/risk

Original V cc8e9e7e421a258a46279304c910f88e2ad33147, introduced by the owning
API/admission commit 5b6700dc604c851be6b8fccd013897cc57aea5ce.
Network#ensure_enabled! raises IpAddressInvalid with the localized denial.
IpAddress.Create, Network.AddAddresses and VPS.Update do not translate it;
HaveAPI 0.29.8 safe_exec therefore returns generic server_error / HTTP 500.
Explicit Assign already translates that exception. Rejection remains atomic;
this is a feedback/error-contract issue, not an admission bypass or data loss.

Disposition (lead, 2026-10-08): accept this Advisory as a recorded residual
under mandatory-change-review step 8. The current follow-up refines inventory
readers and presentation, leaving allocation/ownership actions unchanged.
The source conclusion is verified against the three public rescue paths, the
exception registrations and the declared HaveAPI safe_exec implementation.
No denied HTTP request was executed. A future bounded correction should
translate the denial consistently and exercise all three HTTP entry points;
the passing model exception tests do not certify their response contract.
Do not describe expected denial feedback as uniformly localized or these
actions as successful. No exception catch is added in this presentation fix.

Final affected disposition (2026-10-08): RESOLVED at committed Wce856841, independently confirmed by retained reviewer0 under GENERAL/architecture/scope. All12 final EN/CS desktop/mobile descriptions are complete/readable. Review2 has no new findings. Expected-denial HTTP500 and OPTIONS-timeout Advisories remain accepted and unresolved. See network-counter-tooltip-review2-result.md.
