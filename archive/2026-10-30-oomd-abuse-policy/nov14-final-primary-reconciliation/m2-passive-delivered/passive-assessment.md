# M2-PASSIVE delta assessment (2026-11-14)

**Sufficient client-layer correction and candidate semantics; adoption/execution
remain held for exact build inputs and native-handler proof.** Full revised
`main.go` read (406 lines, 12,829 bytes), SHA256
`4c5f02d0a58c6b8b9ae85b5d2cf5807c548d363f19c67612bc4968f3508b59cb`.
Patch SHA256 `be1f7e95abe5109a9dfd2c4e29c0b5b7393c9cf733429989ffe5ae017257b8c8`.
This is source assessment, not independent final certification or executed checks.

## Verified delta

Our installed dd90 `codex/client.go` is exactly
`c8f0e7a1e0b516d2a0ced66a814a3346cd9339879f74c910fc94c239129acfe3`.
The delivered patch removes/adds one line only: append
`thread/backgroundTerminals/list` to the outgoing ObserverOnly allowlist at
line 1132. In-memory substitution yields exactly
`924f82257d2eafbc31a57bc26da2527ff116f8b1f9bd50886044c57d4410c0fb`.
No copy or patch was written/applied. The incoming readLoop bytes are unchanged.

Revised main line 384 sets `ObserverOnly:true`. Pinned `client.go:1416–1419`
therefore takes the no-answer branch for incoming requests before prompt
normalization/rejectUnsupported. The added outgoing method is admitted while
all other observer restrictions remain intact. This closes the original
client-layer automatic-reply gap **if the eventual binary uses this exact
private copy**; it does not establish server-handler purity. NewWithOptions /
Ensure / empty-watch / ReadTurnState-through-HistoryReader conclusions from the
[prior assessment](../m2-delivered/assessment.md) remain valid: existing-socket
connect plus initialize/initialized, no client-requested launch/resume/turnstart.
The outer gate still permits only three literal read methods and exact root/
utility IDs, with the background list restricted to utility.

The revised result no longer equates outer call ID with native item ID:
`OuterCallProvenance` is informational (lines 24,297,375). Listing keeps only the
row with processId `99295`, records its `ObservedItemID`, compares exact command
(including `--repo vpsfreecz/vpsadmin`) and cwd, then returns `candidate` or
`candidate-conflict` (lines 218–237). Missing historical inner ID is not invented.
A different command rendering yields conflict, not looser shell normalization.
`ListComplete` means only bounded list traversal finished; `EffectsProof` remains
false for every path. Exit0 means candidate present with matching displayed
command/cwd, not authenticated original identity, continuity, liveness beyond
that observation, terminal receipt or recovery permission. Empty/not-listed
cannot close the original 99295 receipt gap. The revised Notice states this.

Unchanged guards, paging, socket checks and output restrictions retain the prior
assessment's limits: exact utility project/source/cwd/unforked original terminal
latest turn, root ID/cwd with separately supplied monitor ownership, safe refusal
on changed parent snapshots, four pages/128 rows, duplicate/cursor refusal,
30-second RPC context, no atomic list/generation guarantee, exclusive mode0600
new output with encoding/close errors checked. Candidate command/cwd are bounded;
observed item ID is preserved as returned, subject to transport bounds. No raw
unrelated rows or transcripts are emitted. Consumers must inspect Outcome and
ListComplete, not just Candidate. Output path must be a canonical new file under
our private parent; socket path and expected flags remain exact in the packet.

## Minimum remaining dependencies before adoption

1. **Native pure-list proof:** the inspected installed Go client/contracts do not
   contain the native `thread/backgroundTerminals/list` handler. Supply exact
   pinned native version/source references or deliberately delivered relevant
   handler/callee text proving dispatch gets only the existing loaded thread's
   manager, performs bounded listing, and does not start/load/resume/subscribe,
   spawn/input/signal/kill a command, or otherwise change process ownership.
   Include absent/unloaded behavior and the row/pagination types. Peer confirmation
   of inner-vs-outer IDs resolves the intended classification, but does not prove
   those handler effects. No new source search/clone or runtime probe is needed
   from this assessment.
2. **Portable private build identity:** supply the pending copy manifest/recipe
   tying every copied package file/module dependency to our own immutable dd90
   inputs, main/patch hashes above and exact Go toolchain. Prove only that copied
   client.go changes and the binary imports it (not the unpatched installed/module
   cache copy). Record binary/input hashes. No project/module-cache/installed
   runtime/pin edits, environment-hook side effects or implicit downloads are
   part of adoption. The peer's earlier Go1.26.6/module digest claim remains
   unexecuted evidence until the exact recipe is available and accepted.
3. **Proportional quick checks and review:** after separate authorization, compile
   with the frozen private inputs; verify whole-copy diff/hash and gofmt. Focused
   existing/fixture controls should cover the newly allowed read versus rejected
   mutation, unchanged no-answer inbound behavior, candidate with distinct inner
   ID, mismatch/empty list, malformed/duplicate/nonadvancing pages and changed
   snapshot/socket or write refusal. Reuse supplied checks if their source and
   input identity are proven; no live native calls or new test framework is needed
   for these controls. Root then owns independent final artifact assessment and
   any single read invocation release.

A private one-line library policy addition plus fixed one-shot driver is bounded;
it is not an installed client change or a generic recovery framework. All effects
resolution remains outside this artifact. No build/install/test/copy/patch/native/
provider/history/lifecycle action was performed. Only assessment records changed.
a8 remains held; 3b remains resolved. Stop pending the two supplied contracts.
