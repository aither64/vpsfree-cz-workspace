# Shared React browser verification and pagination correction

Reviewed source55a813b44edb915c7ed5ce68366d6d797a551606 first batch:
10passed,1failed,1notrun; native exit1,70.54s. `--retries=0`,
`--max-failures=1`, two workers; original receipt/log/artifacts preserved under
`react-rework-verification/browser*`. Eight EN/CS owner/admin detail cases and
desktop overview/old-API passed; mobile overview failed, mobile old-API did not
run. This failed batch is not a full pass and is not real API enforcement proof.

## Concrete cause and bounded fix

Trace shows requests in order: default VPS detection, explicitoomd refresh,
then selectednear_limit. First filter update URL lacked effective `limit`; while
the second exemption selection was pending, existing keyset pagination normalized
the first URL by addinglimit50. That writer used its earlier snapshot and dropped
the exemption. The last URL contains status+page+limit but no exemption; no combined
server request occurred. Existing latest-search ref handles the new component's
own rapid selections, but cannot stop another normalizer replacing its URL.
`pagination-diagnosis.json` preserves raw request and URL-snapshot chronology.

Smallest correction: pass existing `pagination.limit` to `VpsIncidentFilters`;
every filter update includes it with page1 and removedfrom_id. The hook sees a
canonical URL and has no second limit normalization to race. This alone proved
insufficient in the next affected browser batch (below). No shared pagination,
router, API/receipt/permission or general navigation change. Lead read exact
four-path `pagination-fix.diff` and accepted direct narrow-fix verification under
the mandatory review skill; no unaffected/full independent review rerun required.

Negative-before regression: first filter update'slimit wasnull instead of50;
1failed/1passed. Corrected component:21/21 focused tests passed, including rapid
combined filters, external/Backlimit100, unrelateduser and pagination reset.
Application types, structural audit(no new exception) and UI strings passed.
Logs: `pagination-negative.log`, `pagination-positive.log`.

The accepted correction is4paths,14+/8- including tests; intended staged app tree
`0a30ab5aa41988bde6172c99a68edb3ef71912ef`. Fresh Luna/low one-operation watcher
01a19123-7236-7560-bd6b-cd1f577e3cf6 owns only affected desktop/mobile overview2,
then previously notrun mobile old-API1; distinct logs/results. No broad repeat,
extra dependency restoration or build.

That follow-up stopped with1mobileoverviewpassed/1desktopoverviewfailed;
the old-API command never launched. Exit1,34.02s; stagedtree0a30unchanged.
Its trace shows first statusURL already canonical, but second selection ends with
exemption alone, losing status. Thus the initial correction removed one competing
normalizer without fully correcting deferred router-state publication. Native
server ended,portconnect111. Raw `browser-filter*`, `browser-followup-result.json`
and `router-diagnosis.json` preserve this attempt separately.

Existing `BackupCenterPage.tsx` uses React Router `flushSync:true` on filter edits
to commit before another control navigates. Apply that same single option to the
new component's navigation call, retaining its latest ref and canonical limit.
No new router layer/shared hook or public contract. `router-fix.diff` records
the complete4path17+/9- correction. A mocked option-contract guard fails before
(1/1), passes after(2/0); it is not presented as timing reproduction. The actual
browser traces are the timing negatives. Application types pass again. Intended
stagedtree4bee7d1455f35cd422fc385fafda18486f6ee3ea receives only affected2overview
plus previously notrun1oldAPI through a fresh Luna/low watcher; no retry flag or
successful unaffected repeat. Both overview cases and remaining old-API case
passed; tree unchanged and nativeport refused afterward. The fix was folded
into4343a02c with exacttree equality and lead direct acceptance. See
[final published receipt](react-shared-final.md) for capture/publication/CI.

## Source/capture and process limits

Original8detail results/captures retain exact55scope. The detail card/settings,
layout/overview, API adapter, two catalogs and browser fixture are byte-identical
after the list-only correction; SHA-256 inventory is
`detail-runtime-unchanged.json`. New overview captures must come from corrected
tree. Whole final runtime equivalence is checked after app consolidation and
again after routine evidence commit.

All browser identities/responses are synthetic. Missing unrelated fixture IP/
resource/storage data are visible gaps and not backend certification. Pictures
show actual implementation, with no screenshot-polish/product change implied.
Old b67captures remain historical and are never reused as new-label proof.

Original runner's immediate plain bind check returnedfalse, but laterconnect_ex111
and process scan show no listener/runner/watcher/Vite on5197. Native Playwright
server cleanup completed; transient socket reuse is not evidence of a live child.
SO_REUSEADDR bind succeeds; no process was stopped. Watcher initially searched
an unconfiguredlogs/browser-result.json; the actual direct browser-result.json
was present throughout. This receipt-path correction does not alter the failure.

First browser measured rootfree176232853504before/175608700928after; shmfree
50613551104both. Owned Vite cache8798208bytes, results4038656bytes and
report3993600bytes after; unrelated global disk changes are not attributed to
this run. BFFdeps/dist remain absent. No merge/deploy/lifecycle authorization.

[Portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
