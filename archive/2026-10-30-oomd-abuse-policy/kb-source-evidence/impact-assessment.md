# Legacy WebUI source impact

## Historical assessment — pre-generic source range

Reviewed application range ac10a62f1cb0fc890378ae83cdf18dd0e29f049a..
5a59ead40a283f74d211c7afde4d4d69aab28785; KB baseline vpsAdmin
939159f27b5d627930281d5fac0c0aa9ba53bfc7. SSH remote proof matches published
final feature head and unchanged master. Scope jointly supplied by architect0,
legacy owner1 and lead, checked against final diff by template/KB owner3.

Inherited939→ac10 final WebUI diff has only composer.lock and php-packages.nix.
It does not change PHP labels/routes/landmarks/gettext. Therefore inherited
packaging churn needs no blind fingerprint refresh. App feature adds OOM list
indicator after USED DISK, admin filters, and VPS detail section after existing
first base table. Existing semantic IDs/routes retain their intent; no KB
navigation instruction changed. Final checker decides fingerprint drift.

Affected screenshots: getting-started/vps-list, restore-backups/playground-vps-list;
each Czech/English. Four PNGs. Existing base-vps fixtures produce count0/5+0/10.
No new OOM scenario or managed-page expansion. getting-started/vps-details crop
selects h1+first table and excludes the appended OOM section; final PHP inserts
vps_oom_details directly after first table_out. No detail capture unless later
geometry/source changes invalidate that fact.

Bound pages: CS informace:novacci, EN information:new_members, CS
navody:vps:obnova_webu_zo_zalohy. EN playground concept has no current page
binding but the inventory still requires both locales. No prose correction
identified from source inspection. Lead owns any actual future page candidates;
production writes/deployment are outside this package.

Exactly five pin files changed:flake.nix,flake.lock,captures.json,
contract/navigation.yml,contract/pages.yml. Complete lock-node/edge comparison
confirms only vpsAdmin selected revision/hash/lastModified/original revision
changed. OS6bdf458fd9105379860234ff33d352e55844f08f unchanged. No fingerprint,
semantic ID, scenario, fixture, test, page prose or screenshot source changed.

Later source review/capacity admission precedes full screenshots-topology runtime.
Source check allows missing media only; strict final inventory+visual four-image
review+hosted exact-head strict Check remain required later.

## Current source handoff — generic policies

Assessed PHP source: `4db0de750500baffb16c7fbc0ac30a2aa198baa7`, tree
`63cc6814777d1435750dcf12901cef0e12aefc16`, parent
`93dcd30d0ed1b6db43ae6e04111fb8c53b544891`. Owner4's
[committed-source packet](../g-php/packet.md) and
[eleven-blob inventory](../g-php/committed-source-hashes.json) bind the accepted
synthetic UI/token-equivalent formatting evidence. Architect independently checked
this source. Final history consolidation produced equivalent successor
`5aa1df7b51fc22c9d35a2d7f6aec889afa54b303` with the exact same complete tree
`63cc6814777d1435750dcf12901cef0e12aefc16`. The
[history receipt](../nov17-generic-policies/g1/final-history-receipt.json)
binds the retained old source, complete old/new ranges, empty old-to-new diff,
ordinary hooks and clean registered feature branch. This is proven source
equivalence. The [publication receipt](../nov17-generic-policies/g1/publication-receipt.json)
now verifies this exact successor on the SSH feature ref, with explicit old-head
lease and unchanged default branch. Canonical runtime/media proof remains pending.
Earlier sections retain only their recorded source and screenshot claims.

The [G-PHP design addendum](../design.md#kb-impact-addendum--g-php-2026-11-18-exact-source-scope-closed)
is the bounded follow-up contract. The generic Incidents sidebar destination is
`?page=adminvps&action=incidents&veid=ID`. Old feature landmarks
`vps.oom-summary`, `.oom-details` and `.oom-settings` are superseded by generic
`vps.incidents.menu`, `.page`, `.policy`, `.settings`, `.permission` and `.warning`.
The old IDs were never registered in the current navigation contract; no existing
registered path is being removed. The later menu binding must fingerprint both
the static declaration and its related route helper.

Reassess `getting-started/vps-list` and
`restore-backups/playground-vps-list` in Czech and English. The permanent incident
column is gone, and zero-threshold fixtures render no hostname warning. The list
navigation crop hides `#aside`, so the sidebar label alone is outside that crop.
The detail concept `getting-started/vps-details` also needs final zero-fixture
geometry review: its rectangular h1-to-first-table crop includes an intervening
threshold warning, although zero thresholds render none. The old unconditional
claim that an appended detail section is outside the crop no longer applies.
Only images actually changed need canonical bilingual regeneration; the older
four-PNG requirement is reassessed, not discharged.

Keep existing page/image bindings and the incident article-pair follow-up named
in the design addendum. Canonical media/runtime provenance and strict/visual proof
remain pending. This handoff changes no KB repository, pin, screenshot, page,
staging state or capacity allocation and does not revive the parked capture work.
Root has released implementer0's G-KB source/navigation and article-pair preparation;
the final five-file pin and pinned contract check may now consume that exact
published successor within the existing root allocation. The pin/check results
remain owner0's follow-up evidence. Ordinary demo screenshots do not replace
canonical KB media.


### Test-only backend successor

Published `ee9025a8c99f3714d483daed0a6f028520594fbc`, tree
`d4e44289ae0ea1c7fbfb6b00c31eca914d0f4c10`, differs from accepted `5aa1` only in
`api/spec/api/covered_endpoints.yml` and the existing API discovery spec. The
[complete correction receipt](../nov17-generic-policies/g1/ci-coverage-final-receipt.json)
proves every other path/mode/blob identical, including all PHP/navigation/gettext,
API runtime/schema and exporter inputs. The exact accepted `5aa1` source and KB
pin remain retained under root's explicit input-reuse direction; this does not
relabel an export or imply new canonical runtime/media evidence. Owner0's reported
KB `4be305f13fcd15ba79c5c7bde95a277a6164f442` source-check handoff remains at its
own recorded input and scope; no pin/capture/check work is initiated here.
