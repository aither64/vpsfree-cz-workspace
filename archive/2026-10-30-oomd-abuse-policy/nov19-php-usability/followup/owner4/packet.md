# Nov19 follow-up legacy simplification — owner4

The accepted top design and root copy define a source-only follow-up to public
bd18. The checked append is54fe8e649f01295df352b0b3894cf70a62b959a2,
tree16f136d1ffc9c25e29c75074ab41e865693f031a. Final consolidated head is0d1db93cd0d38b77f1e29c40ddd71b45581ecfff,
with the same tree. Authoritative terminal identities are bound in
receipt.json/history-progress.json.
No final-source live scenario, publication or demo refresh is claimed here.

## Source and quick acceptance

Eight paths change: incident_policy.forms.php, vps.js, existing IncidentPolicyTest,
existing incident-escalation Playwright source, POT/CS PO/MO, and the consequential
paragraph in docs/incident-escalation.md. checked-source.json binds exact bytes;
checked-followup.diff binds the delta from publicbd18. No API/schema/SDK/dependency,
fixture/topology, source producer or shared permission contract changes.

The form displays two raw nullable override fields and Save. Blank ordinary string
POST values become null independently; positive integers remain explicit, including
equality with a default. Admin/POST/CSRF/capability/readback and false shared
permission remain. Invalid arrays/nonintegers/zero/negative/native-integer overflow
are rejected before update; API cross-limit rejection and drafts are preserved.
A null saved override may show a valid effective number as placeholder only. An
existing override hides its inherited target; clearing it does not invent one.

The page landmark wraps only newly rendered policy/settings/permission content,
including the empty registry case. Existing prefix output is preserved outside it;
no redundant introduction or empty table remains. Only current status gets Last N
days. Saved periods and memberships retain historical meaning and privacy. The VPS
shutdown filter and legacy forwarding are both removed. The report route's local
cursor binding, active/retired registry and context remain unchanged.

quick.log:24 IncidentPolicyTest tests/237 assertions, formatter, gettext generation
and health, PHP and relevant JS/browser-source syntax all passed. render.php uses
actual PHP/XTemplate/gettext with the existing synthetic HaveAPI client. Four
normal/rejected EN/CS HTML outputs and PNGs were inspected. dom-results.json records
JavaScript-enabled and no-JS ordinary numeric form payload controls and the actual
report route without vps.js. These are offline controls, not real API/browser
integration acceptance. Existing browser scenario source retains the saved-policy,
privacy, member-denial, permission, navigation, retired-key and Czech coverage while
updating controls and adding server invalid-zero/draft assertions.

Earlier accepted livebd18 PASS remains limited tobd18; original cursor/resource
failures and oldEE logout/transaction limitations remain unchanged. The follow-up
requires root's affected independent final review and allocated targeted live
scenario. No heavy/VM/demo/CI action occurred in this package.

## Documentation and KB impact

Developer/operator reference: docs/incident-escalation.md now accurately describes
PHP blank inheritance/explicit overrides, instead of the removed Inherit action.
Existing docs/README.md entrypoint remains sufficient. No other technical-doc
statement required correction. Individual execution proof stays here.

Root-owned successor candidates were read and agree with the implementation;
their exact supplied hashes are unchanged (ENd48f6ab7, CS1b3fda4c). No KB edit or
capture/contract run was performed by owner4. Owner0's follow-up should reconcile
contract/navigation.yml source/related fingerprints for vps.incidents.menu and
vps.incident-reports.menu, paths vps.incidents.open/vps.incident-reports.open, and
pages cs navody:vps:incidenty / en manuals:vps:incidents. Their labels and routes
retain their meanings. The .page landmark is now a nonvisual div; .policy,
.settings, .permission and both sidebar IDs survive. Current-page geometry, raw
blank fields, removed reset/mode controls, Last N days labels and VPS-list filter
removal affect screenshots; assess the existing six bilingual concepts under the
already-owned KB workflow. No new semantic route or capture concept is needed.
Canonical KB media/runtime/strict gates remain separate.

## History and next dependency

Consolidation retains exactly four coherent fixture/API/PHP/password purposes:
63bd0c8ab17eff90f8ca1d840aa0beffed04e86c,
368b053239ace17de0d76b61f8298ab89cfd52d8,
8d71b464f9c3c8e71866054b1e649a4657059c67,
0d1db93cd0d38b77f1e29c40ddd71b45581ecfff.
Fixture63bd and API368 are literal commits; the follow-up belongs to PHP. The
original password HTML patch/message/name/email/author date remain exact. Public
bd18 and the checked append are retained via create-only refs before rewriting.
The final tree and complete537b binary diff must equal the checked append; no fifth
fixup stays in the final range. Full series, range-diff and hashes are adjacent.

Migration20261030180000 follows20261006120000 and retains original SHA256
2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e.
Obsolete20261115120000 is absent from every final purpose. Accepted original5aa1
export/SDK/KB consumption and prior disposable-state provenance remain literal;
this package changes no migration, data, deployment or default integration.
Preserved public commits are not described as literal ancestors of the successor.
No new dependency/pin update stream is introduced. The independent reviewer still
owns the whole final series/history/migration conclusion; root owns invocation.

All three fresh Luna utilities and native source commands are joined0; all six
command items completed0 and all three turns completed. Eleven recorded history
PIDs are absent. Backend source/index/quick-check/hooks/history window explicitly
returned to root in message1c9da8f9-a49b-4cec-95eb-2e3e60c12459. No heavy window
was used; no owned effect remains. The current session remains open.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

Normal append/PHP/H commits all passed their applicable hooks. PHP message
TextWidth warned on five lines over72; all lines remain within80. This is an
advisory, not a bypass. Original messages/logs are retained.
