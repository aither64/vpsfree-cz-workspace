# Final committed citation review

Independent reviewer: `/root/citation_review`, selected standalone
`gpt-6-astra` / `xhigh` fallback. Reviewed the general, architecture,
scope/proportionality, and risk/compatibility lanes, including their complete
references. Overall risk: high. No source edits or long builds were performed.

## Findings

One Blocking finding and three Important findings. Fix B1 before long
integration tests; fix or explicitly dispose of the Important findings before
continuing under the review procedure.

### Blocking B1 — The new passive requests are missing from the required protocol corpus

Owner: codex-web `a204708d32c12bfe547c5c8bbbcf1b4396490bcb`.
Location: `codex/citation_history.go:192`, `:238`;
`test/codex_protocol_contract.py:314-342`.
Lanes: general, risk/compatibility.

The citation worker adds one `thread/turns/list` and one `thread/items/list`
call site, but the schema request corpus was not updated. Both packages run the
call-site coverage check before their Go tests, so neither selected package can
pass its checks or produce a usable verified artifact.

The coordinator supplied the initial CI failure while this review was being
completed. I inspected both retained logs and the corpus/call-site scanner.
Both fail with `thread/turns/list` implemented 12 versus covered 11, and
`thread/items/list` implemented 4 versus covered 3. See
[client CI](client-ci-initial.log) and [runtime CI](runtime-ci-initial.log).
The runtime's session-creation VM consequently fails at its package dependency,
before exercising the VM.

Add corpus entries for the exact citation request shapes and run the quick
coverage/schema checks before resuming package or integration builds. This is
missing coverage, not evidence of an incompatible native request shape; keep
the pinned Codex version.

### Important R1 — Pending citations lose their retry path when a newest-page row becomes older

Owner: codex-web `a204708d32c12bfe547c5c8bbbcf1b4396490bcb`.
Location: `conversation/assets/conversation.js:336-340`, `:448-450`,
`:1242-1247`; also consumed by dev-workspace's custom browser.
Lanes: general, risk/compatibility.

`rememberCitations` ignores pages without a request cursor. That covers every
newest-page read. If a completed message is still awaiting source recovery when
new entries push it out of the newest page, the overlap merge retains the row,
but nothing registers it for citation repair. It is not an active-turn repair
candidate either. Newest-page retry scheduling only examines the new page, so
the visible old row can remain `[source pending]` indefinitely, even if the
worker has already found the source.

Reproduced with the committed shared module and Nix Node, without modifying a
file:

```js
const h = createTranscriptHistory();
const row = (id, extra = {}) => ({
  kind: "agentMessage", turnId: id, itemId: id,
  turnStatus: "completed", text: id, ...extra
});
const page = entries => ({
  threadId: "t", status: "idle", hasOlder: true,
  olderCursor: "cursor-before-page", requestCursor: null, entries
});
h.applyNewest(page([row("a", {citationsPending: true}), row("b")]));
h.applyNewest(page([row("b"), row("c")]));
```

Result: all three rows remain, row `a` has `citationsPending: true`, but
`h.gap === false`, `h.citationsPending === false`, and `h.repairCursor` is
undefined. The scheduler cannot revisit it.

Track unresolved retained rows as they leave the newest page and recover them
through an appropriate current history cursor. Add a regression for completed
pending rows crossing that boundary, including preservation of already loaded
rows. The existing test covers only a page explicitly loaded with an older
cursor.

### Important R2 — The repository browser acceptance fixture cannot load the new shared module

Owner: dev-workspace pin
`08898005d057acb6fa025341808134f104ace9e7` and citation consumer
`2f2966bf518b84490e310304d28214ffcbe24f9a`.
Location: `test/repository_browser.cjs:77-85`; provider
`conversation/assets/conversation.js:2`.
Lanes: architecture/consumers, general.

This fixture imports `createCopyButton` from `conversation.js`. That module now
unconditionally imports `./citations.js?v=1`, but the fixture serves only the
previous companion modules. The new request falls through to HTTP 404, preventing
the entry module and repository review UI from initializing. Adding the asset
to `TestShippedBrowserClientMatchesSessionAPI` did not fix this separate consumer.

I evaluated the fixture's actual request handler with stubbed browser startup
and the committed provider files:

```text
/conversation.js       200  imports citations.js
/citations.js?v=1      404
```

Serve `citations.js` in this fixture and verify its import closure. This is a
failure in the retained manual browser acceptance harness; I did not claim that
the default packaged suite invokes this particular script.

### Important R3 — The inherited and new codex-web pin updates remain an unconsolidated stream

Owner: dev-workspace complete series
`ea3f9d36397e8c2c846bd456e51385d73a3a358a..2f2966bf518b84490e310304d28214ffcbe24f9a`.
Lanes: general/history, scope.

`0aef1e247865ace614a41341d6a0e4a24f4b6b62` updates the codex-web source,
Go module, lock, and vendor hash from `c064ce09` to `f3633de`.
`08898005d057acb6fa025341808134f104ace9e7` updates the same selection stream
again to `a204708`. The packet identifies the earlier revision as deployed, but
does not establish why the intermediate pin must remain in this unmerged branch
after the final update. The final provider contains the required optional
question and selected-provider behavior.

The deployed baseline is real: I independently compared all 502 tracked files
of `d68f88a` against
`/nix/store/gn8az8v3j2yw8mv8cxq6b68zy0jgblgc-source` using Git blob hashes and
found no mismatches. That establishes the behavior and exact ref to preserve.
It does not establish a need for both pin updates in the new branch. The
workspace Git procedure explicitly distinguishes these obligations.

Preserve the original deployed/source feature refs, keep the inherited
functional changes, and consolidate this branch's dependency selection to one
final update. Alternatively, record a concrete supported-consumer or state
boundary explaining why the final update alone is insufficient, and obtain an
explicit disposition under the review procedure. Publication, deployment, or
the desire to retain rollout SHAs alone is not that boundary.

## Reviewed ranges and history conclusions

The inventory's heads match the worktrees, all four worktrees were clean, and
each supplied base matches the merge base with its available `origin/master`.
I inspected each complete series and final diff, rather than only the citation
commits.

| Repository | Base | Head | Complete series |
| --- | --- | --- | --- |
| codex-web | `c064ce09cfcea8d8af6bf676635a53cd823f772c` | `a204708d32c12bfe547c5c8bbbcf1b4396490bcb` | `641907f` optional questions; `f3633de` selected provider; `a204708` citations |
| dev-workspace | `ea3f9d36397e8c2c846bd456e51385d73a3a358a` | `2f2966bf518b84490e310304d28214ffcbe24f9a` | `0aef1e2` optional questions/pin; `eeff83f` archive recovery; `d68f88a` naming provider; `0889800` citation pin; `2f2966b` citation presenter |
| workspace | `650495d6bea856c75c5d717526c9a888f7f2fcf6` | `c0187a433a95c4c42b4baa6e3cd872be468fca84` | `0723c3f` investigation records; `05e1b67` implementation plan; `c0187a4` runtime pin |
| vpsfree-cz-configuration | `6e79db5ab5e3b4e35ba3db1c1c8b94c4b833abd2` | `34249ae7a131c03aad8e8af6a3e68e19a24042a0` | `34249ae` generated confctl runtime pin |

The inherited optional-question, provider-routing and archive-recovery
implementations remain present in the final tree. Their functional changes have
distinct purposes and corresponding tests/documentation. I found no abandoned
citation protocol, removed functional approach, fixup-only implementation
commit, or unused branch-only migration path. The inherited archive recovery
adapter continues to support existing journal/receipt formats and should not be
removed as citation cleanup.

The runtime's codex-web dependency stream is the repeated stream identified in
R3. The provider has one Goldmark dependency addition; workspace has one runtime
selection update; configuration has one generated runtime selection update.
There are no further repeated dependency streams in the supplied ranges.
Retain the generated confctl message as generated.

History is therefore **not yet clean for final readiness**, due to R3. Existing
deployed refs remain support/recovery evidence and should be retained separately
when consolidating the new branch.

## Migration and compatibility conclusion

**No migrations.** There are no new database migrations, durable server-state
versions, conversation rewrites, runtime contract versions, or native Codex
upgrades in these ranges. Consequently there are no migration versions needing
merge/release/deployment/external-use provenance. The inherited optional-question
feature adds its own browser-storage records; older clients ignore those keys.
Archive recovery operates on the existing schema-2/schema-4 journals and
schema-3 receipts, rather than introducing a new persisted format.

Citation fields are optional additions to transcript JSON. Raw message text and
durable message identity remain intact. An older browser can ignore the fields;
a new browser receiving an older transcript falls back to the original text.
Go consumers and shipped assets must use the matching provider revision, as the
prepared pins do. Software recovery remains subject to the existing workspace
package-transition policy; additive citation data does not bypass that policy.

The current source selections are aligned: runtime `2f2966b` selects codex-web
`a204708` through both `portal/go.mod` and its flake; workspace's nested override
and configuration's `devWorkspace` both select `2f2966b`. Their codex-web content
hashes agree. The workspace extension remains at `767dfd587e346168e1443e65ccdb67ce748f3fe3`.
The configuration diff changes only the expected runtime/client lock identities.
The user-profile application and system-side host configuration retain their
existing deployment split. Refresh these pins after source fixes or history
consolidation.

## Architecture, safety and scope

Ownership is appropriate: codex-web owns extraction, code-aware token parsing,
UTF-8 spans, passive source recovery, shared copy behavior and generic DOM
rendering. The actual production consumers were verified through Go imports,
`TransformTranscript`, the module/flake pins and the browser import path:
the generic conversation UI/reference application and dev-workspace's custom
Markdown presenter. R2 identifies an additional test consumer of the module.
The source-recovery feature is not duplicated in the portal.

The portal renders substituted Markdown through its existing Goldmark renderer
and Bluemonday sanitizer. The generic renderer creates anchors/text through DOM
APIs. Source destinations are restricted to HTTP(S) without embedded
credentials; titles and copied Markdown are escaped. No source URL is fetched
by the server. User messages and artifact rendering do not enter citation
resolution.

History lookup uses trusted thread identities, passive native reads, bounded
worker concurrency and per-client caches. It skips items following the cited
message. The existing HTTP resolver still checks opaque conversation authority,
canonical cwd, origin, read capability and thread identity on each request.
No new browser-selected socket, filesystem path or thread authority is exposed.
The inherited provider route is confirmed at the shared lifecycle RPC boundary
before inference. I found no concrete authorization, sanitization, or destructive
operation regression in the reviewed changes.

The added mechanisms serve the requested paged-history and streaming behavior.
Documentation ownership is appropriate: the shared reference describes the
public contract, the portal guide describes visible behavior, and rollout
evidence stays under this initiative. The authoritative aitherdev operation
procedure remains separate from feature documentation.

## Verification and remaining limits

Independent checks performed here:

- Exact heads, clean worktrees, merge bases, complete commit lists and diffs.
- `git diff --check` for both implementation ranges.
- Git blob comparison of all 502 deployed-baseline files.
- The R1 shared-history reproduction and R2 fixture-handler reproduction using
  the recorded Nix Node executable.
- Static inspection of source/copy rendering, request authority, actual consumers,
  pins, inherited implementation/tests, and changed documentation.

The packet reports passing focused Go/race tests, 74 shared browser contracts,
portal sanitizer checks, and the server-backed browser contract. I inspected
their coverage; those checks do not cover R1 or R2. Cache generation/file
replacement/append invalidation and browser retry timing have limited direct
coverage and remain useful focused follow-ups.

No long suite, native integration run, full aitherdev build, activation or merge
was performed by this reviewer. The independently inspected automatic CI logs
establish B1; they supersede the packet's earlier statement that no full package
suite had started. Fix B1, resolve or explicitly dispose of the Important findings,
refresh exact pins, and continue the planned package/integration and
artifact-preparation checks. This report does not certify artifacts that have not
yet been built or authorize activation/integration.
