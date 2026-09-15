# Campaign form-context follow-up review

Initiative: 2026-09-09-ip-release-mechanism. Tracking plan.md/state.md in this
same directory. Review this bounded delta to the already reviewed split series.

Repository: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsadmin
Delta base: 4d53fa1573bf5d0ba8de5d896153e4ca21dcfb5a
Head: fa3670345 (resolve the complete SHA locally).
The last WebUI commit was amended; compare the base/head trees, not an ancestor
range. The first seven commits are unchanged. The series still has eight
commits. Earlier four-lane review and fixes are in review-split-results.md.

The user accepted separating generic relative resource accounting, provenance,
network identity, shared IP reservation helpers, relative IP callers, cleanup,
campaign API and campaign WebUI. The user also requested a running review
cluster and real fixtures. No merge, production deployment or session closure
is authorized.

Live review found that XTemplate retains TABLE_FORM_BEGIN/END and hidden fields
after form_out. Campaign settings therefore wrapped subsequent address and
pagination tables in additional settings forms. Browser HTML correction could
swallow the first address's nested exemption form. The existing integration
exempted a later address and did not assert a unique settings form.

This delta adds a page-local form-context reset after rendering campaign settings
and member retention forms. It does not change generic XTemplate behavior.
Browser coverage now requires exactly one settings form and a distinct exemption
action on the first address's form. Review correctness, ownership and whether
this is sufficiently bounded. Similar local clearing exists in security_advisory.forms.php.

No API, DB, policy, locking, node, mail, or public interface changes. API behavior
and all accepted email wording remain as recorded. Notification overlay head
715c063396fa49277852b98d36347c8bec5160d3 is unchanged. KB is still at dfebd25c,
pointing to the earlier WebUI head; its mechanical exact pin update will follow
publication. Current managed pages/screenshots had no drift; no member prose or
KB navigation label changes in this delta. No new design documentation is useful
for the template-local reset; its rationale is in the owning commit message.

Quick checks: PHP syntax passes; IpReleaseCapacityContractTest passes (1 test,
2 assertions, existing PHPUnit deprecation); JS syntax passes; all commit hooks
pass. The earlier tree passed all 26 hosted API Specs jobs and all eight local
network/DNS/browser scenarios, including actual PTR-before-release. The new
browser assertions will run after this review. Live screenshots and form checks
will be rerun as part of the requested cluster handoff.

Risk: high conservatively because wrong form boundaries affect admin exemption
submission and thus release protection. All four lanes, gpt-6-astra/xhigh. This
is a small presentation fix; no schema, protocol, rolling-upgrade or persisted
state contract changes. Reverting it restores the malformed forms. No other
resource consumer or shared template interface changes.

The review cluster also exposed unrelated disposable setup issues: the legacy
CLI hostname and a DNS secondary service that exhausted retries before RabbitMQ
permissions were ready. Those are being repaired through normal development
configuration/service/API paths, without project code changes or production
mutation. The unsent primary campaign and eight addresses remain intact.

Perform the assigned lane yourself. Read mandatory-change-review and its lane
reference. Do not spawn nested reviewers or edit files. Return concrete findings
with severity and file/line references; explicitly say when none are found.
