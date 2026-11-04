# Reviewed asset-version preview candidate

Status: meaningful warm-cache regression and all retained candidate browser
acceptance passed. The lead subsequently released the final live refresh after
exact-head local/hosted checks; [live receipt](preview-cachefix-live.md) records
the final runtime. This file retains candidate preparation evidence.

Exact head: `eb91a4d031c2c1f1c6ec6dd1aaed62e1f320eea7`; tree
`d6b39fec8fe094471b47ac9054d890df6abf767c`. All 933 exported Git blobs match,
with zero missing/mismatched files. [Source receipt](preview-cachefix-source.json).
The exact export is `preview-source-eb91a4d0` in this session directory.

Candidate service: `haveapi-doc-language-cachefix-candidate-20261101.service`.
Ruby PID: `1615810`; invocation: `9c909eceefe0408fb251077c08886a2f`.
Started: `2026-11-02 14:34:54 CET`; loopback only `127.0.0.1:14569`.
Health passed. [Runtime receipt](preview-cachefix-candidate-runtime.json),
[log](preview-cachefix-candidate.log).

[Warm-cache evidence](preview-cachefix-warm-candidate.json) records the genuine
51047 HTML/assets → genuine candidate HTML/assets sequence in a single Chromium
context per locale, without hard refresh, cache clearing or interception. Old
stable JS/CSS fetched once and were reused across another no-store HTML
navigation. Old JS visibly exposed the singleton control, establishing the test
precondition. Switching unchanged genuine HTML to the candidate fetched both
content-digest URLs, with actual received-file hashes:

- JavaScript: `c9282c372706b505d054615cb20665679468dd784111048167ab10933e6148ab`.
- CSS: `02a787414658c963be0a016e622a895fc61605fab03df0358750bdc910a147b3`.

English and Czech passed at the exact reported path `/v1.0/?doc_lang=en` and its
Czech equivalent. Actual Go/HTTP each retained `details: [simple]`, hidden
wrapper, computed `display:none` and 0×0 wrapper/select geometry. Ruby restored
two visible detail options. The English label is Language; Czech remains Jazyk.
Direct native candidate Go/HTTP en/cs each submitted exactly one
`example_detail=simple` and retained resource/query/locale after real Apply.

Retained exact-head Chromium checks also passed:
[refinements/capability](preview-cachefix-refinements-candidate.json),
[native](preview-cachefix-native-candidate.json),
[UI](preview-cachefix-ui-candidate.json),
[comments/code/privacy](preview-cachefix-comments-candidate.json),
[real generated profiles](preview-cachefix-generated-candidate.json).
No browser page errors occurred. Capability evidence remains separate in-process
real OAuth fixture HTML, with no added OAuth service.

The disposable warm-cache HTTP fixture ended with the bounded browser check; it
was not a live proxy or host configuration. It served only genuine app HTML and
actual fixed assets, leaving application metadata and visibility logic untouched.
All persistent preview/candidate services remain running. Before the final refresh,
the live preview was exact ef4, PID `1487623`.
No project source/index, dependency install, host, lifecycle or cleanup operations
were performed. Exact ef4 export/profile/service recovery is retained.
