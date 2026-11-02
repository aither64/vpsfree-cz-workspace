# Final asset-cache preview

Live URL: <http://aitherdev.int.vpsfree.cz:4567/v1.0/?doc_lang=en>.
The English sidebar label is Language; Czech remains Jazyk. Go and HTTP
singleton detail controls are hidden. Ruby restores its two-choice detail control.

Exact source: `eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7`; tree
`d6b39fec8fe094471b47ac9054d890df6abf767c`. Fresh comparison verified all 933
exported Git blobs with no missing or mismatched files. The lead released the
refresh after independent review, exact-head local checks and all 11 applicable
hosted checks passed. [Source receipt](preview-cachefix-source.json).

Active service: `haveapi-doc-language-preview-20261101.service`.
Ruby PID: `1688000`; invocation: `3ba77a243dc247feb7e4b1e1a13afb38`.
Refreshed: `2026-11-02 14:45:35 CET`; listener: `0.0.0.0:4567`.
Working directory:
`/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-api-doc-language-settings/preview-source-eb91a4d0`.
Runtime Ruby:
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`.
Log: [preview.log](preview.log).
[Exact runtime/asset/launcher/preload receipt](preview-cachefix-live-runtime.json).

Six bounded actual Chromium suites passed with no page errors:

- [Warm cache and direct Go/HTTP](preview-cachefix-warm-live.json): genuine 51047
  HTML/JS/CSS first warmed both stable entry URLs and reused them across another
  ordinary navigation. The same context then loaded unchanged genuine live HTML
  without hard refresh, cache clearing or interception. Both content-digest URLs
  were fetched with the expected file hashes. English/Czech Go and HTTP had
  `details: [simple]`, hidden wrapper, computed `display:none` and zero geometry;
  Ruby two choices returned. Direct reported URL and real native Go/HTTP Apply
  also passed, with one scalar detail value and resource/query/locale retention.
- [Refinements](preview-cachefix-refinements-live.json): singleton visibility,
  saved Thorough, Ruby top-level require before `begin`, localized comments;
  separate exact-source capability fixture DOM/form order.
- [Native selectors](preview-cachefix-native-live.json),
  [UI](preview-cachefix-ui-live.json),
  [localized comments/code/privacy](preview-cachefix-comments-live.json), and
  [real generated profiles](preview-cachefix-generated-live.json) passed.

Live entry-asset retrieval returned 200, with body SHA-256 equal to the URL query:

- JavaScript: `c9282c372706b505d054615cb20665679468dd784111048167ab10933e6148ab`.
- CSS: `02a787414658c963be0a016e622a895fc61605fab03df0358750bdc910a147b3`.

Health passed through the hostname and LAN route; highlighter returned 200.
This demonstrates the fixed cache failure mode and exact reported control states,
without inspecting the user's own browser cache. The warm-cache HTTP fixture
was bounded to the check and did not alter the live server or host configuration.
Account capability evidence remains separate real in-process OAuth fixture HTML;
no OAuth service was added to the preview.

The preceding ef4 exact export, [service definition](preview-ef4-service.txt) and
[profile preload](preview_profiles-ef4.rb) remain for recovery. All persistent
preview/candidate services and the session remain running. No project source/
index, install, host, lifecycle or cleanup action was performed by this package.
Earlier rollout/recovery records remain in [preview.md](preview.md).

[Stable session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-api-doc-language-settings/).
