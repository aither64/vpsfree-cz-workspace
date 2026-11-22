# P3 native routing core: committed finite checkpoint

The common-port milestone is accepted at
`7e6229da4745db05484864107c03a9c72ab06dfc`. The initial foundation TESTED base is the accepted
compiler correction `699d8f85b20b89772fbcb4d49ecccfb6d24b8f75`; it is not the
current parent. The actual component graph below uses committed
`d4e15e9d6b36fb2c4f4ff93e4f68a290494e265b` (paired central25af plus P7 metadata)
plus22 owned runtime/test overlays. The finite checkpoint is now committed as
`d3b0057f6b032d19a4b2cc86b81a3493e5220981` over that exact parent under release
da705a16. Lead main prose is closed and the exclusive23-path commit window was
released after full receipt verification. Ready for finite checkpoint acceptance
and lead-owned independent review; capacity/fix ownership remains with implementer1.
This is not full package or production completion. No activation, push, ref
cutover, real runtime/model or session lifecycle operation ran.

## Current finite original-input milestone

The exact [c05cd569 graph](tmp/p3i-native-persisted-inputs.json), committed d4e
plus22 owned overlays/121 inputs, passed the real Manager/Unix/pinned SDK case
**Go4.711s** (declared command9.992s). [Log](tmp/p3i-native-persisted-actual.log);
[fresh Luna/low result](tmp/p3i-native-persisted-exact-watcher-result.md).
One original Accepted receipt/full digest and native user remained unchanged;
physical requests were A,A,B, with exactly two public charges and one completed
read preserved in B context. Fake route/effect/failure/decision calls were
3/4/1/1. The original positively settled and the final worker was idle/unheld.
All operation-owned work joined. No production/B1/later-input/restart claim.

The final defect was token serialization of optional undefined LIVE SDK fields.
A small Node regression reproduced it red; token bytes now come from the
independently reopened public persisted prefix after exact serialized equality.
The raw transmitted hash recipe did not change. Node25 cases pass; the current
Go cold-load9-case scope separately passed0.336s, including exact preflight,
physical restoration without route authority and failed intent/no replacement.

The same finite wrapper passed the changed original-budget case on the exact
[c96a360e graph](tmp/p3i-native-budget-inputs.json), SHA256
`c96a360ef6bd590a14cea21d24bc84bd5709d026444b2130941857d8b07d0d68`:
**Go7.267s**, declared command12.408s. B tool success did not reset the original
one-hop budget: physical requests were A,A,B,B, never the available C; one
original Accepted receipt/user, exactly two charges and two completed reads
remained, with the earlier A result unchanged across routing. Fake route/effect/
failure/decision counts were3/6/2/2. Original settlement was positive and the
worker finished idle/unheld. [Log](tmp/p3i-native-budget-actual.log);
[fresh Luna/low result](tmp/p3i-native-budget-watcher-result.md). Launcher81907
joined terminal0; no operation-owned work remains running. Only the owning Go
test and native-routing-worker fixture changed since the happy graph. The
earlier happy source/graph stays its exact scope; no unchanged SDK batch ran.

Final assurance on the same c96 graph passed compile-only **Go0.012s**, the
27 explicitly selected native pure Go tests **1.785s**, and worker native-routing,
version and workflow-observation Node cases **27/27,0.348s**. The pure selection
excludes the two actual SDK cases and the separately proved pre-init old-worker
component. [Exact pure command](tmp/p3i-native-final-pure-command.json);
[pure log](tmp/p3i-native-final-pure.log). These are distinct scopes from the
actual fixture receipts above.
Technical runtime docs now contain the optional native section and all accepted
first-original/B1-after-physical-reset/recovery limitations. Main prose is closed
and the exact23-path commit window is completed/released. No Instructions or
ReadActiveHostInput source task began.

## Frozen source packet for lead review

The [checkpoint packet](tmp/p3i-native-core-checkpoint.json) freezes exactly
23 whole-file targets over actual d4e: 22 runtime/test paths plus the new
`docs/pi-runtime.md` native-routing section. Seven source/test files are new.
The [complete owned patch](tmp/p3i-native-core-checkpoint.patch) includes those
new files without changing the Git index. All22 runtime/test hashes match the
tested c96 graph; the index was empty at capture. The technical doc hash is
`f6a2c25a10241f801700106517db27d45851649e45068aa212b7131e5bd4b28e`.
Lead completed the main prose pass only on the new Optional retained native
routing section. Removing that new section reproduces the exact original doc;
closed common/workflow and later paragraphs are byte-unchanged. All22 tested
runtime/test targets retain their original hashes and test receipts. The prior
packet/patch remain under tmp/p3i-native-core-pre-prose-checkpoint.*.

All23 owned paths pass tracked/new-file whitespace checks and Go files are
gofmt-clean. [Format receipt](tmp/p3i-native-final-format-receipt.json);
[quick-check receipt](tmp/p3i-native-final-quick-receipt.json). Compile26887,
Node84995, Go80882 and actual-budget launcher81907 are joined terminal0. No
known operation-owned work remains running. The ordinary exact23-path stage
and temporary-file commit completed0; no push/lifecycle action ran. No database
migration, history rewrite or branch cutover occurred.
Retained schema3 is additive and strict old readers refuse it; existing1/2,
utility2, original submission bytes and H0 stay unchanged. Production writer
availability is not established by this finite checkpoint.

| Topic | Reader and authoritative home | Evidence or remaining limit |
| --- | --- | --- |
| Routing CAS, selection, holds, original lifetime | Runtime maintainers: project docs/pi-runtime.md, Optional retained native routing | Owning codecs, transaction/expiry tests and c05/c96 component scopes |
| Old-reader/target compatibility and restoration | Operators: same runtime section; existing host guide remains linked | Native3 owning inventory/predecessor guard and production consumer wiring remain absent |
| SDK omission, B1 and original recovery | Runtime/authority authors: same runtime section and adjacent bridge comments | Current-original-only witness; historical/restart/B1-after-reset unavailable |
| Exact source, commands, graph lineage and package gates | Lead/reviewer: this record and linked source packet | Committed d3b0057f over d4e; scoped tests retain original overlay graphs; no merge, review, activation or full-production claim |

## Completed commit receipt

[Actual receipt](tmp/p3i-native-core-commit-receipt.json), SHA256
`019288c5dfc648469ef9bce560ca3c2401a9590d140d442c92acb90a09a1e30d`,
binds head `d3b0057f6b032d19a4b2cc86b81a3493e5220981`, exact parent
`d4e15e9d6b36fb2c4f4ff93e4f68a290494e265b` and tree
`7b781df53f78db1c9d8cd526a5706f1c9d8e9f35`. The exact23-path change is
5460 additions/113 deletions, including all seven new source/test files. Every
staged/index, committed and current target hash equals the approved packet.
Owned paths and the complete primary worktree were clean; post-index was empty.
The ordinary cached Nix-shell `git commit -F` exited0 without bypass. No hook
framework or active non-sample hook is declared; no hook setup was changed.
All commit/check effects are joined.

The post-prose approved [packet](tmp/p3i-native-core-checkpoint.json) SHA256 is
`b60e2f061249b8f55a821098e3b255c96911a7fb845aeaf3aac3e2332970e259`;
its prepared patch SHA256 is
`6fbe3e0cc77960f90fabf795df84f9baa556501ebf02bdb48201ce980c562a92`.
The canonical committed [diff](tmp/p3i-native-core-committed.patch) SHA256 is
`9c8da1818ae31283264e08ccee2585d442ac994bb79bf83501683d384d13c8c9`.
The prepared patch ordered new files last; the canonical diff sorts all paths.
Exact inventory and blob hashes, rather than byte-order patch equivalence,
prove that the committed content is precisely the approved target content.
Lead was notified of immediate window release in report053ac26f.

## Completed pure milestone

Frozen graph [110 inputs](tmp/p3i-native-foundation-inputs.json), SHA256
`ea0ce415cae6123cf0e137ecb4c133546b3df277eb86e99a7ead7f2d7f4e8dd8`, is committed
699d plus only sixteen owned Go/JS source/test overlays. It excludes dirty peer
central, metadata and guard changes. Compile-only passed0.017s. On that exact
copy, the selected native/common pure cases passed **Go1.504s** and the conditional
worker-expiry/production-version smoke passed **Node6/6,0.307s**. Logs:
[Go](tmp/p3i-native-foundation-go.log), [Node](tmp/p3i-native-foundation-node.log).
Go command: [exact script](tmp/p3i-native-foundation-go-command.sh).
No SDK session, credential, model or installed runtime was used. The production
version smoke owns one finite Node process and loads no SDK. Go session27083 and
compile79216 completed0; Node command completed0 with no yielded session.

The checked scope covers strict retained3 request/state and original-expiry
codecs, unchanged old retained1/2 and utility2 bytes, no utility routing, bounded
CAS/baseline/max replay, recorded versus independently verified inspection,
recorded-only old generation for an unloaded mapping with no worker, held and
pending precedence, detached empty-array copies, full startup account-map join,
monotonic memory lifetime/activity invalidation and full-tuple conditional expiry.

Mapping transaction fakes prove complete pending publication before native calls,
positive initial rejection retaining proved physical0, exact applied replay,
virtual-to-physical reset without route authority, physical settings/routing
coherence with independent revisions, embedded B2 read/apply, nil-policy refusal,
VerifyCreation/Load pending refusal, lost reply/bad native proof/completion-save
failure retaining original pending/hold without replay, actual worker-version
requirement, and negative package/map/module/routes/attachment/current-state gates.
Package/route/module certificates in these fixtures are explicitly fake; they
confer no production capability or route proof.

The worker conditional-expiry tests show complete-input/generation comparison
before the first await, stale no_effect without abort/hold/certificate changes,
held exclusion before captured-session abort awaits, no replacement/dispatch on
matching uncertainty, duplicate held reply without another abort and malformed
request refusal. A stale fake input cannot abort a different fake active tuple;
actual positively admitted next-input integration remains required.

## Current source and settled seams

- New native_routing.go owns codec/validator, inspection, package permits and
  private mapping transaction. native_retry.go owns memory lifetime/expiry codec;
  native_retry_types.go keeps accepted exported-Go types and existing data-only
  validator semantics. conversation.go integrates strict schema dispatch and
  schema3 physical settings coherence; tool_policy.go preserves its independent
  enforcement proof. guarded_submission.go uses the separately granted pre-lock
  schema3 guard and post-lock permit checks before unchanged sendOwned.
- The loose partial package parser was removed. NativeRoutingPackageGuard is an
  optional Go-only owning callback on Manager Config and private supervisor.
  Supervise remains its five-argument nil wrapper; additive
  SuperviseWithNativeRoutingGuard supplies a trusted in-process callback to the
  same implementation. No runtimeConfig/H0/argv/receipt field changed. Nil/error
  is unavailable. Guards run outside c.mu/receipt/attachment locks and recheck
  captured full runtime/launch/root. No real composition wiring exists yet.
- Existing InspectRetainedConversations/ConversationRetention remains the
  committed owner3 whitelist1/2 and refuses3. No native3 cold inventory/export or
  guard capability is claimed. Owner3's two-file whole-metadata decoder and later
  inventory/predecessor/wiring remain separate windows. Native writer permission
  cannot come from injection presence, generic validatePackage, fake proof or
  source declarations.
- Attachment nativeRetry negotiation is intent only after both local guards,
  before Create if needed. Actual same-worker nativeRetry1 read-only version is
  required before conversion/pending/routing effects. Cold Load retains its
  existing ownership prewrite, then same-process pre-init version before any
  SDK/history/registration init; failure retains hold with no rollback/replacement.
  The version operation is now identity-fenced after init. The finite actual
  fixture exercises the same attachment and typed authority wire; its authorities
  are fake and no production composition wiring is supplied.
- The accepted cold inspection exception returns current control generation as
  an observation fence only when the strict saved mapping is unloaded and has no
  worker. It never rewrites saved generation or restores an original retry arm.
- Owner5 correction699d supplies detached nonnil FallbackOn:[] for empty categories,
  with unchanged original policy/digest. P3 still rejects nil/null at the virtual
  boundary and does not normalize it or choose physical mode automatically.
- Owner5 confirmed positive stop is terminal to a leaf instance. Success can reuse
  endInput/beginInput. A stopped instance can be disposed and explicitly unregistered
  only after exact positive settlement/effects proof and NEXT DISTINCT original
  admission, inside the next guarded pre-prompt deadline. Held/Unknown/unsettled
  originals cannot be rearmed. No leaf source edit or new reset API is allocated.

## Shared fixture amendment

Only fake-worker.mjs p3-fake/p3-model gained reasoning:true, SHA256
`8fedf32d3538f2cdd89324273e1ea715aedafce8b0d03460439eb0fee4e209af`.
Existing off cases remain valid, p3-other and alternate remain nonreasoning and
all response branches are unchanged. Node syntax/diff and pinned faux public
clamp checks pass. It was held unchanged for owner2's tagged combined fixture;
paired25af committed it and the existing P6 Reopen helper exactly, closing both
temporary holds.
Owner2 reports actual same-Manager initial ACK/Create p3-model high/full Default1/
Inspect/original Accepted witness/Verify under disposable root EX passed, followed
by a display-eligibility timeout. That proves the fixture line's high/session
support only, not full central flow, installed support or public initial root
allocation. Prior SDK receipts retain original5a673952 worker bytes. The pure
110-input graph does not execute this shared fake worker and retains its committed
version as a non-exercised input, with the held hash recorded separately.

## Checkpoint boundary and remaining work

The current source includes private SDK projection/registration and guarded cold
restoration, Manager live-authority route preflight and the narrow controller.Load
hook, exact four-purpose transport/codecs, once-only first-dispatch lifetime,
durable Accepted wait, independently reopened prefix and fresh route/effect/
failure certificates, conditional expiry/positive settlement, atomic workflow
observation and both bounded actual original-input cases. Pure/fake tests cover
the cold/pre-init and transaction refusal boundaries; they are not a restart
integration proof for edited history.

The exact commit and complete receipt are ready for lead checkpoint acceptance
and independent review. This report does not release capacity or claim full
package acceptance.
Existing real physical/domain adapters and P2/P7 all-cold/predecessor/production
wiring remain mandatory external dependencies; their absence keeps routing
unavailable. The current strict retained reader is committed by this checkpoint;
positive native3 inventory/export/guard use still needs lead acceptance and its
separate source window. Existing InspectRetainedConversations still refuses3. Historical omission witnesses
remain unavailable, including later original inputs and restart; unchanged B1
readers also refuse edited history after physical reset. Production completion
therefore needs a separately accepted solution preserving B1 and recovery.
No second history state append, host Send retry, receipt format change, session
lifecycle operation or production metadata activation is permitted.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/

## Earlier original-receipt component diagnosis (resolved for finite scope)

The first actual authority/SDK component used [121 frozen inputs](tmp/p3i-native-authority-inputs.json),
SHA256 `13fec1e4a6fb39cf8dbb36dbb9e846559f5cec5eed3692e9916914835de06ae2`,
committed d4e15e9d plus22 owned overlays in `/tmp/pi-native-authority-dy86fkzy`.
The clean copy compiled0.015s. Before this attempt, the focused pre-init old-worker/
route/expiry reply cases passed0.278s: the owning protocol with only nativeRetry
capability downgraded was refused and reaped before any init marker or SDK restore.
A fresh installed Luna/low watcher ran one exact original-receipt/charge case; it
failed (Go2.203s) after durable Accepted and before the first physical dispatch.
[Terminal log](tmp/p3i-native-authority-actual.log). No operation remains running.

Source inspection during diagnosis also found that tool-policy `running` spans
the complete original agent turn, including route callbacks. Treating it as an
active separate tool effect would incorrectly refuse routing; the first attempt
had not yet isolated its initial refusal. The affected gate now allows that exact live original while
requiring the current applied policy and zero active tool/callback/resource counts;
positive external prefix certification remains mandatory. Empty counts still do
not establish completion. A focused regression covers this distinction before
any changed-input component attempt. Private bounded purpose/stage diagnostics
identify the next refusal without recording provider or argument bodies. This is
the earlier unfinished component diagnosis, not route/writer acceptance.

The shared fake-worker8fed and Reopen6cf5 are now committed by the accepted paired
central25af checkpoint; temporary packaging holds are closed. Native tests use the
separately approved new `pi-runtime/test/native-routing-worker.mjs`, wrapping the
existing runWorker and pinned faux provider without another parser/harness.
All package, route, effect, failure and final-decision adapters in this component
are explicitly fake. Production native3 inventory/guards and real physical/domain
authorities remain unavailable dependencies.

## Prefix and SDK omission boundary

The changed 121-input graph
[83aa6e65](tmp/p3i-native-authority-second-inputs.json), after the running-turn
correction, still refused at effects:prefix (Go2.147s). The diagnostic-only graph
[4c47608f](tmp/p3i-native-authority-prefix-inputs.json) isolated exact matching
original binding/hash and a valid SDK system-message string that the Go view had
incorrectly decoded as a block array (Go2.089s). Logs remain separate:
[second](tmp/p3i-native-authority-second-actual.log),
[prefix](tmp/p3i-native-authority-prefix-actual.log). Both fresh Luna/low
watchers reported terminal exit1 and no outstanding operation.

The typed system-string correction preserves all transmitted raw branch bytes
and hash, permits UTF-8/newlines and refuses null. The smallest linear-prefix/
paired-tool, first-dispatch and running-original cases passed0.106s on the exact
[system graph](tmp/p3i-native-authority-system-inputs.json),
SHA256 `0b82c0c6309344695add7af07a9dd2be3ebc8417b0113a8e1d82e0b137ad53ef`.
The corresponding actual case reached physical A/read then A empty error, with
zero host failure/retry certificate calls, and held at its original15s lifetime
(Go17.050s). The watcher interface was unavailable in that continuation, so this
one bounded attempt used the skill's visible parent-monitoring fallback; tool
session7792 joined exit1. [Log](tmp/p3i-native-authority-system-actual.log).

Pinned SDK source identified the next concrete compatibility boundary:
agent-session._handlePostAgentRun -> _prepareRetry emits auto_retry_start before
_omitRecoveryAttempt appends a public linear context_edit targeting that failed
assistant with replacement:null, then emits generic entry_appended and awaits
backoff. Accepted owner5 native leaf follows that path and retains the raw
failed message; it does not separately attribute arbitrary context edits. New P3
bridge reused B1 linearEntries, which intentionally rejects every context_edit.
No blanket relaxation has been made. Architect1/0 subsequently accepted only
the exact process-local original/failed-stream/auto-retry/immediate-entry token,
proved closed extension/source set and independent whole-prefix checks recorded
at design.md:2149. Event/raw shape alone remains insufficient. Existing B1
guards stay unchanged; P3 appends no second edit/state and cannot repair/resume
the original. This resolved the finite current-original component boundary;
production support remains unavailable for the B1/recovery reasons above.

Additional small proof fixtures establish the actual receipt-engine first
dispatch follows durable dispatching, duplicates retain original deadline/bytes,
and an unsettled distinct original gets zero receipt/native effects. Pure prefix
negatives cover disconnected parents, changed original/hash/leaf, extra user and
missing/duplicate/unmatched tool results. These are fake source scopes, not a
substitute for actual route/charge composition; the later c05/c96 results above
provide that finite evidence separately.

The latest owning Go native pure selection passed1.119s after new bounded tests
proved Accepted-wait progress while conversation and receipt writers remain
locked, and schema3 workflow observations bind the atomic native selection and
refuse idle for pending/held originals. Those two new cases separately passed
0.093s. Conditional expiry now exposes a private memory completion channel for
joining its existing persistent-hold publication during component teardown; it
is not an authority or disk-format field. No SDK rerun followed this test/join
addition while the omission interpretation was still unresolved. Later checks
and actual results above retain their own exact source graphs.
