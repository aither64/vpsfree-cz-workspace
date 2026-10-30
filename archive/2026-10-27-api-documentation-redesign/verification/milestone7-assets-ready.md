# M7 owner3 source/check readiness

Own only these application paths, now source-stable:

| Path | SHA-256 |
| --- | --- |
| servers/ruby/lib/haveapi/public/css/documentation.css | bd7bb2fadc9c856fad95e65b87b4a415611248efb6f82e8e4db2792ca295bc53 |
| servers/ruby/lib/haveapi/public/js/documentation.js | b2374dce1c5bf5fac5413b7111f954384fe5f8bcf4aed1bd55f34fc265a81b34 |
| servers/ruby/spec/client_examples/assets/documentation_test.cjs | ee8dc63f63fa5b5b8e4a85df1c0dbf7caae535fa25917e0f52e84bf5387ce473 |

Implemented primary/owner-subsection geometry, current-owner expansion and
focus deferral, native heading permalink styling, idempotent structural
inside-code-block copy wrapper, slash search focus through the existing drawer
without query changes/storage/new fetch, page-union options and per-group
meaningful detail selection. Missing custom metadata retains old behavior;
malformed metadata chooses Simple without dropping its renderer; absent group
clients retain the existing unavailable message. Saved thorough and other
language client choices survive singleton pages/events. No IDs reconstructed,
client capability table, schema/key/rank/cache policy or source templates changed.

Final inline prepared-Nix batch passed all three existing scripts:
make test-documentation-assets (with actual fixture projection env), plus
Node --check for JS and its existing test. Owned trailing whitespace/newline
check passed. No browser/HTTP/build/dependency work/Git/index/hooks/commit.

Actual HTML supplied by owner0:
[resource](milestone7-reference/dom/resource.html),
[authentication](milestone7-reference/dom/authentication.html).
Read-only projection [asset-dom-projection.json](milestone7-reference/asset-dom-projection.json)
was consumed via DOCUMENTATION_REFERENCE_FIXTURES by the existing Node script.
Its exact HTML SHA values were resource1dd8b6bb2556f331945a5d596e5559ae170d746b33e8ffcb9f6c203328a49e7a
and authb0b778b8e244fc1629bf27e4f0a8161854b12d5109caeba1f9f7808b2e1af520.
Tests exercised both primary actions/providers and every actual subsection
native-landing threshold. Handcrafted tests additionally cover up/down/provider
geometry, deferred focus hiding, clipboard success/failure/current selected panel,
async invalidation, no wrapper duplication/code contamination, slash modifiers,
IME/editor/composed path exclusions, actual drawer state and no shortcut fetch,
single/mixed/custom/malformed/no-example metadata and preference restoration.

M7 real browser/responsive acceptance remains pending committed affected review
and separately coordinated fresh HTTP receipt. All previous M6 evidence retains
its actual source scope. No material design deviation or new visible copy.
Source/check/process/Git quiet; no active owned operation. Await serial Git slot.
