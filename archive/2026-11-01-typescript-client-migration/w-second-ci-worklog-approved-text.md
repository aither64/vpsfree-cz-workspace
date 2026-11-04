Replace the optional-workflow paragraph's final two sentences beginning
“This procedure has not yet been exercised” with:

The isolated build/pack/override/restore cycle subsequently passed on WebUI
`8d0bb48a` and client `e16663a9`, with durable exit 0 after 236.009 seconds.
Typechecking, 23 binding tests and both forced Vite resolutions passed. The
packed README matched the corrected source, while built client files were
unchanged. `npm ci` restored every installed client file; all 2,580 tracked
canonical/snapshot source files were unchanged and owned server effects were
absent. This was a disposable development snapshot, not a new committed archive
or registry release.

Replace “Nix and the isolated API runner continue to verify committed inputs.”
with:

Nix retains the committed input checks. The isolated API runner is outside this
override workflow; use its separately verified archive and receipt under the
existing runner procedure.

Append the following section verbatim, then apply the existing Markdown formatter:

## Second browser CI and touched-spec validation

On published `d3d5efbe`, core CI
[41450042642](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41450042642)
passed all three jobs. Browser run
[41450042371](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41450042371)
ended at the native 40-minute limit in all three projects. Its retained logs
contain 103 partial failure headings across 27 additional specs, outside the
previous 30-spec repair: 32 Chromium, 30 mobile Chrome and 41 mobile WebKit.
These are observed headings, not completed suite totals. Trace selection and
progress differences do not establish an engine-specific cause or certify
unreported cases as passed.

The 27 leaf specs now use canonical successful response namespaces, resource
references and declared field types. Existing rejection, permission, secret,
cursor, geometry, uncertain-outcome and no-replay assertions remain. Sixteen
edited deferred files were adopted completely; strict coverage is 134 checked
and 148 deferred, with zero diagnostics. The original baseline, sourceRevision,
surviving deferrals and compiler options are unchanged. Production source,
shared mocks, dependencies, archive/provenance inputs, runners and CI selection
or limits are unchanged by this repair.

Executing all existing cases in the touched specs exposed two further advisory
fixtures before the complete workflow could run. Creation now supplies the real
initial parent revision and verifies successive CVE baselines. The assessment
scenario preserves the observed revision through individual and bulk node
updates, publication and readback. It uses the supported localized note fields
and canonical retraction/outage references. The actual production guards stay
strict. Each committed affected review, including the final `3ca34e34` source,
completed with Blocking 0, Important 0 and Advisory 0. The complete history has
one generated-client input stream and no database or persisted-format migrations.

The native local runs used two workers, no retries, a first-failure stop and the
existing 900-second limit:

| Tested source | Selected cases | Native result |
| --- | --- | --- |
| `96d9c996` | 220 | 42 passed, 1 failed, 1 interrupted, 176 unrun; exit 1 after 155.366 seconds |
| `129bf840` | 178 | 15 passed, 1 failed, 1 interrupted, 161 unrun; exit 1 after 115.406 seconds |
| `3ca34e34` | 164 | 164 passed; exit 0 after 732.546 seconds |

The last run includes all 12 advisory cases, including one earlier pass repeated
after its file changed. Joining it with 56 individually proven passes from
unchanged files covers all 220 original local identities across the 27 specs:
110 Chromium and 110 mobile Chrome. Each identity is counted once; this is not a
claim that all 220 executed on one head. Actual input equality and native report
identities support the retained results. All three runs retain durable terminal
receipts and recorded owned-process/listener absence evidence. The earlier
failures and interruption limits remain recorded.

This completes the bounded local fixture selection. Native WebKit and the
larger unchanged matrix still require final-head CI. Earlier API and Nix results
retain their exact inputs; tree equality does not establish final-head derivation
or provenance equality. The user keeps the released-client transition pending;
a compatible published dependency is still required before merge. No registry
publication, default integration or deployment is claimed.
