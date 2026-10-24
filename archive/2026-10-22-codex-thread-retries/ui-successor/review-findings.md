# Presentation review findings and disposition

Review scope: A f8629067 / B39497062. Reviewer0, retained Sol/xhigh/read_only,
all four lanes complete. Full report saved review.md. Exactly one Important
finding, called P1 in final report and I1 by lead/owner; no Blocking/Advisory.

## I1: activity-only footer growth fails to follow (Important, general)

Reviewer source evidence: B static/app.js2756 mounts an independent footer;
the observer around4299 watches only fixed viewport size. New activity or
increased notice height grows scrollHeight without a viewport resize. With
overflow-anchor:none, a conversation already following bottom can leave the
new notice/actions below the visible area. Fixture manual scrolling before
captures masks this transition.

Disposition: fix required, assigned implementer1. Observe footer layout through
the existing follow contract; preserve scrolled-up anchors/composer selection.
Add idle-to-visible and notice-height-change assertions without manual scrolling.
Keep the fix in the owning presentation commit, A dependency unchanged, preserve
old reviewed source and direct before/after evidence. Capture held pending fix.

Owner draft remedy: one added `transcriptResize.observe(retryRoot)` in existing
observer; no A API or new framework. Fixture starts null, checks initial following,
reveals activity and varies reason height, asserting bottom distance <=2px
without manual scrolling. Existing scrolled-up/focus checks retained.

Verification: owner focused quick checks passed (b-i1-quick.log: Node17/0fail/0skip,
shipped-browser HTTP1.069s, fixture compile0.047s). Final B480231f5127c69ae210f0d17796a57481cdc2e28,
tree6f951eba4574836750d888238db605dca89c7dca, clean and exact SSH feature matched.
Lead directly inspected full394→480 two-path delta and range-diff: exactly one
product observer line; fixture adds isolated null/height transitions and response
barrier. First seven commits/A selection unchanged; owning UI commit amended.
The existing observer applies the existing per-filter follow flag without changing
scrolled-up behavior or focus. No new design/public/authority boundary.

Disposition: source remedy accepted under mandatory-review step9; no redundant
review turn. No unresolved findings prevent the focused capture. Actual geometry
assertions remain pending the authorized capture, not claimed passed from source.
Owner receipt b-i1-final.json SHA256
a5298d19a24d8e8f59460c8eb1b11369f3063ade5d01fdc086cb36136c7eff58.
Original394 review/ref/bundle/evidence preserved in reviewed-39497062/.

## Browser startup correction after failed capture1

Capture1 at clean480 failed at first20-message assertion with zero messages;
no images. Owner identified omitted zero-delay scheduler drain while the fixture
clock was paused. Existing mode_refresh browser contract uses readiness followed
by clock.runFor(0). Added that same pattern after every goto/reload and bounded
failure screenshot/JSON/page/request evidence. Actual cause remains unproved
until the next empirical run; no TLS/product/assertion relaxation.

Lead inspected full480→5e342788 one-file diff: fixture only, first seven commits
and all product bytes unchanged. Quick shipped-browser1.019s, fixture compile0.046s,
syntax PASS. Final5e342788c7178ac1cb93c25591bdc42a83386c6b/treeed95652b08dc7a5d3e2a54745974a0431bed1bc2,
clean and fresh SSH ref matched. Direct bounded test correction accepted under
step9, no new design/public contract. Preserve failed attempt and old480 evidence;
one new watcher/capture2 follows refreshed command/receipt.
