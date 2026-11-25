# First native failure — bcc5

Existing spec228 expected from_id empty after policy select, actual999999/20s.
The cursor-reset listener is in webui/public/js/vps.js52, loaded only by
page_adminvps.php1154–56. page_incidents.php does not load that script.
Earlier synthetic preview injected vps.js and missed the actual route boundary.
No source edit, retry or assertion change. Small faithful remedy: place reset in
the incident filter context, remove the unreachable VPS binding, and check the
filter without injecting vps.js. Root coordinates the public pin/history/review
window before mutation. Existing admin inheritance/prefill/pending/reset, permission,
zero/reached, saved two-policy and member privacy assertions preceding228 executed.
Filter submission/history row checks after228, notices/foreign-report/Czech/final
logout were not reached and are not claimed. This differs from oldEE final logout.

Original failure precedes helper guard. Progress records verified-owned-group SIGINT
after first native example failure; nativeexit1/wrapperexit1 remain literal.
The utility narrative no-cancellation statement is corrected by script/state.
All native/utility/source handles joined and ordinary teardown left baseline guests
unchanged. No source mutation or dependent heavy release.
