# Warm-cache entry-asset acceptance

Status: exact reviewed eb91 candidate warm-cache acceptance passed; see
[candidate receipt](preview-cachefix-candidate.md). After the lead's final local/
hosted release, the live eb91 refresh and six bounded suites also passed; see
[live receipt](preview-cachefix-live.md). All persistent services remain running.

The architect's accepted diagnosis is recorded in
[singleton-warm-cache-diagnosis.json](singleton-warm-cache-diagnosis.json).
Its experiment proved the cache mechanism, using current ef4 HTML throughout.
It did not inspect the user's actual cache. This acceptance uses the stronger
genuine old-HTML → genuine successor-HTML sequence.

[preview_warm_cache_check.cjs](preview_warm_cache_check.cjs) uses the existing
Chromium/Playwright installation without browser request interception, which
could disable the browser cache. After release it will:

1. Read genuine 51047 overview HTML from the already-running old loopback
   candidate and genuine successor HTML from its newly authorized candidate.
   Read actual JS/CSS bytes and original file modification times from their
   exact exported sources. Do not rewrite either HTML document.
2. In a disposable loopback HTTP fixture, warm the browser with old stable JS
   and CSS URLs, matching the actual no-Cache-Control/no-ETag plus Last-Modified
   behavior. HTML remains `private, no-store`. A second ordinary navigation
   must reuse both stable cached assets; old JS must visibly expose the
   Go/HTTP singleton, proving this is a meaningful regression case.
3. Switch the fixture to genuine successor HTML/bytes in the same browser
   context. Without hard refresh/cache clearing, navigate to the exact reported
   path `/v1.0/?doc_lang=en` (and Czech). Assert real network requests for both
   JS/CSS digest URLs with SHA-256 values matching the actual files. Select real
   Go and HTTP; assert `details: [simple]`, hidden wrapper, computed `none` and
   zero wrapper/select geometry. Return to Ruby and assert two choices reappear.
4. Separately use the real successor candidate with JavaScript disabled for
   en/cs × Go/HTTP: exact one `example_detail=simple` FormData/URL scalar, real
   Apply, preserved resource/query/locale and hidden singleton controls. Check
   English Language and Czech Jazyk on ordinary successor HTML.

The fixture serves a frozen, bounded set of genuine documents/assets for browser
cache testing. It does not act as a live proxy, alter application metadata,
overlay controls or change host configuration. It exists only while the bounded
check runs. A 55-second browser deadline prevents a new long monitoring campaign.

Prepared invocation after review release:

```sh
/nix/store/l07gdbxylzfl8pbx9pxy6fyg95w4hjwy-nodejs-24.19.0/bin/node \
  work/2026-11-01-api-doc-language-settings/preview_warm_cache_check.cjs \
  http://127.0.0.1:RELEASED_CANDIDATE_PORT /absolute/exact-successor-export \
  /absolute/session-local-warm-cache-result.json
```

Existing profile, native, comment and capability suites were also rerun and
passed on exact eb91. The live service refresh remains separately gated by the
lead's final exact-head local/hosted release, which was later supplied and executed.
The warm-cache receipt proves the
accepted mechanism regression and exact Go/HTTP states; it does not inspect the
user's own browser cache.
