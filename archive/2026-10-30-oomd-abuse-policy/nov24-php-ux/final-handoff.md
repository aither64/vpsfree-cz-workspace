# Final PHP UX source and browser handoff

Final public source is `a25b2ae4a5a17e0ef1416b858833e79d4d4f2897`, tree
`c8332d430a13845fd3452e1ba203e05542d7b155`, on canonical SSH feature branch
`2026-11-24-incident-admin-php-ux`. The isolated source/index is clean. Served
`vpsadmin` remains clean at8846 and remote master remains4062. No activation,
runtime, default-branch or lifecycle operation was performed.

There is one UX purpose directly after8846, retaining the original author and
message. The full4062 range contains PHP926b, API8846 and UXa25b. Reviewb679 and
browser-proof1b1f have create-only retained refs; original screenshots, findings,
failures and raw utility receipts remain intact. No migrations changed in the
full range. The new UX purpose changes no API, schema, SDK, dependency lock or
fixture. `final-ux.diff`, `final-full-series.diff` and `final-history.txt` bind the
final history. Root's independent four-lane review found only the accepted F1;
the scoped correction and the later requested VPS identity label use narrow owner
checks without another review turn.

F1 resets the inherited fixed header widths/offsets only inside the authorized
page's narrow media query. Actual language links, session/logout/CSRF controls,
Jump and full navigation remain. The test uses the existing XTemplate lang_add,
logbox and menu/sidebar helpers. Two focused tests/57 assertions passed, followed
by normal hooks in68.204s. The final label-only change renders an original VPS ID
without a current hostname as VPS #999 without a link, while null remains Unknown.
Two affected tests/16 assertions, syntax/format, normal catalog currentness and
hooks in66.513s passed; the compiled Czech MO did not change. Earlier17/256 and
other passing proofs retain their actual input scope.

The full finite synthetic browser proof at1b1f produced eight initial collapsed
EN/CS Overview/History captures at1280 and actual mobile390, plus four English
keyboard-opened Details captures. Document width equals viewport width in all
cases; entries stay within content, desktop sidebar stays beside it, and mobile
language/logout/Jump/nav/sidebar controls have positive on-screen bounds. Jump was
editable and the logout dropdown opened within the viewport. Sidebar Reports,
History and Overview links, actual Reports form, user23/false-permission filters,
cutoff retention, Next offset25 and Refresh were exercised through actual PHP
rendered responses. All contexts closed. This proves the offline fixture/source
boundary, not a deployed runtime or real API result.

After the label correction, only four initial History captures were refreshed
at finala25b, with the full authenticated frame and no control changes before
capture. All four confirm VPS #999/no deleted link/no sort and repeat the affected
full-document/entry/control/sidebar geometry. Images for root's final inspection:

- `captures/history-label-final/history-en-1280-collapsed.png`
- `captures/history-label-final/history-en-390-collapsed.png`
- `captures/history-label-final/history-cs-1280-collapsed.png`
- `captures/history-label-final/history-cs-390-collapsed.png`

Accepted unchanged Overview and opened Details images remain under
`captures/pre-identity-label/`. The final label delta does not replay their flows.
The earlier browser harness failures are literal: PHP's existing nullable-argument
deprecation initially preceded JSON on stdout; diagnostics were routed to stderr.
A subsequent Reports assertion ran before navigation completed; it was changed
to wait for the rendered form. The resume retained passed desktop captures and
ran only unfinished cases. Existing PHP deprecation and omitted schema-export
presentation-label warnings remain in raw logs. No product fix was made for them.

Every hook/browser utility and parent handle is terminal/joined; exact utility
threads and command-item completion are in `final-receipt.json`. One earlier
report mistyped the final refresh utility thread; the authoritative actual thread
is `01a20e3e-fbb5-7ae3-8309-14e2ef90b095`. Current-head CI was inventoried once
without waiting. Only superseded same-branch CI45425269941 atb679 and CI45427801958
at1b1f received ordinary cancellation requests; current-head runs were untouched.

Source/Git/check windows returned to root before packet polish. Root retains final
visual acceptance and any later deployment allocation. Implementer4 retains PHP
technical follow-up ownership. Member KB controls/routes/source remain unchanged;
owner3's final pin/contract work is separately sequenced. No wiki/media publication
or new review/build/test campaign follows this handoff.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
