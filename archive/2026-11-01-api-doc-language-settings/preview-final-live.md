# Final API documentation preview

Verified live URL: <http://aitherdev.int.vpsfree.cz:4567/v1.0/>.
Public examples: <http://aitherdev.int.vpsfree.cz:4567/v1.0/?resource=test&doc_lang=cs>.
Localized token comments: <http://aitherdev.int.vpsfree.cz:4567/v1.0/?page=authentication&doc_lang=cs>.

The lead released this refresh after independent review, exact-head local checks
and all 12 hosted CI checks passed. The live server uses the exact isolated Git
export `51047a211d71f817ab25f2def1692517f00c15c6`, tree
`9500a75d5f7976796a580b15a512990e6d86b7b0`. Fresh comparison verified all 933
exported Git blobs with no missing or mismatched files. The existing session-local
in-memory fixture and real Go/Rust/TypeScript profiles remain configured.

Active user service: `haveapi-doc-language-preview-20261101.service`.
Ruby PID: `139933`; invocation: `0689ec0c763940f685fa8b97299e38e6`.
Started: `2026-11-01 23:14:04 CET`; listening on `0.0.0.0:4567`.
Working directory:
`/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview-source-51047a21`.
Runtime Ruby:
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`.
Log: [preview.log](preview.log).
[Exact runtime receipt](preview-final-runtime.json),
[source receipt](preview-final-source.json).

All four existing bounded Chromium/Playwright checks passed on the live URL:

- [Native/JavaScript selectors](preview-final-native-live.json): native resource
  and authentication forms, query/locale retention, generated TypeScript,
  singleton controls, selected open code and accessible collapsed alternatives;
  immediate JavaScript switches, both Apply buttons hidden, explicit URL
  selection before stored preferences and no load-time storage writes.
- [UI](preview-final-ui-live.json): Czech horizontal unnumbered breadcrumbs,
  Jazyk, edited overview and hidden/usable native language Apply behavior.
- [Generated clients](preview-final-generated-live.json): Go, Rust Async/Blocking
  and TypeScript API client executable examples and package identities in both
  English and Czech.
- [Comments/code](preview-final-comments-live.json): localized comments and
  generated labels, preserved executable lines and command/package literals,
  generic localized TypeScript limitation without schema/sample names.

Browser errors: none. Hostname/LAN health and mounted JavaScript, highlighter and
CSS returned HTTP 200. The preview remains restricted to the existing internal
network/VPN route; same-host LAN/name access was verified.

Recovery retains the preceding exact ebc export,
[service definition](preview-ebc-service.txt) and
[preload](preview_profiles-ebc.rb). Earlier recovery records remain in
[preview.md](preview.md). No project source/index, dependency installation,
host/firewall/proxy or session lifecycle changes were made by this package.

Leave the live service running. The final loopback candidate also remains running
under `haveapi-doc-language-candidate-20261101.service`, PID `29112`, invocation
`4398ca8e9b6b4ffaa81e64947146bfdf`, on `127.0.0.1:14567`; no cleanup was
performed or scheduled.

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-api-doc-language-settings/).
