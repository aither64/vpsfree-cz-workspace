# Batch1 failure — no rerun

Exact head757f7fd8, clean source. Fresh watcher c0302_full_tests_build ended
and reconciled exit1 in33.776s; no remaining operation. Script tests reported
228cases/227pass/1fail, so `npm run ci:tests` stopped before BFF/root-unit suite
and `npm run build` did not run (`&&`). Full batch1.log/.exit/.elapsed retained.
Failing case scripts/e2e-haveapi.test.mjs:142, description/direct-fulfill/envelope
shape test: line150 reads missing body's top-level meta.namespace.

Parent read-only diagnosis pending/recorded below. No source/Git edit or retry;
batches2/3 held. Lead receives evidence before assigning any bounded source fix.
Exclusive slot remains held pending coordinated disposition; watcher itself is
done, no Nix prefetch/build/browser command is running.

Diagnosis complete: fakePage.request('/api') defaultsGET and its assertion reads
raw.meta.namespace. Reviewed carried fixture intentionally handlesOPTIONS on
/api,/api/,/api/v7.0,/api/v7.0/ and returns okEnvelope(description), matching the
actual library request path. GET/api now follows genericfallback{status:true,
response:{}} and has no meta. Existing actual-library discovery test already
passes and checksOPTIONS/perbase/request headers.

Proposed bounded correction: script test only, issueOPTIONS and assert complete
{status:true,response:description} on the four existing supported description
paths, optionally with customconfigured description to prove payload passthrough;
keep raw201/direct-API-envelope assertions intact. No production/fixture/source-
guard change. Lead assignment requested before editing or rerunning. Preserve
failedfirst-run evidence; update source/quick/review identity if fix authorized.
