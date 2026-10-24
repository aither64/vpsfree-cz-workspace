# A follow-up source packet

Source complete and SSH-published; final independent review and longer
verification remain parent-owned. No default integration or deployment occurred.

- Base: `57972192e30fe52ab33b867c8fe4d171f59a7fd5`.
- Deployed predecessor: `852e8c51091512bc79ca6c921ef1f5ccc46a9535`.
- Published head: `6e32a9043ee6367d92bfaf8d3ebdf48036e275f9`.
- Branch: `2026-10-20-dev-workspace-portal-improvements`.
- SSH remote: `git@github.com:aither64/codex-web.git`.
- Clean worktree and unchanged remote master are in identity.json/remote-proof.txt.
- Safety ref: `2026-10-20-portal-improvements-deployed-a852e8c5`.

## Complete history and migration conclusion

series.txt contains six exact commits, three original deployed commits retained
unchanged and three focused additions. range-diff.txt proves the unchanged prefix.
whole-range.diff and inventory.txt cover all 15 paths; followup.diff covers the
13 changed paths since deployed A. No migrations, database or persisted schema
changes, Codex/native protocol version changes, dependency/lock pins, obsolete
followups or superseded pin streams exist. Supported deployed behavior and
citation baseline remain literal ancestors. No original history was rewritten.

The new groups are optional native pending revision/SSE authority; passive
browser lifecycle/control/history ownership and freshness; and upload metadata
read recovery. Each owns its tests and reference paragraphs. No generic event
system, paging authority change or automatic mutation replay was introduced.

## Interfaces and cache versions

`PendingRevisionProvider.PendingRevision(threadID string) uint64` is additive;
the base client interface and generic SSE updates remain. Authorized optional
providers advertise ready.pendingInvalidation; named pending hints accompany
changed revisions. Native revision bookkeeping is in memory and retires with
watch/pending state; the getter performs no native RPC and has its own tiny
mutex rather than waiting behind transport writes.

`createConversationSync` exposes onPendingInvalidation and a read-only
pendingInvalidationSupported getter. Mounted controls use a 15-second success
floor plus due timer with advertised support and force/coalesce on actual
invalidation, reply/reconnect/manual retry. Legacy generic behavior remains.
`createUploadClient.list({signal})` adds passive cancellation; metadata reads
have ten-second deadlines. `mountUploads.refresh()` exposes explicit metadata
retry. Draft/selection and accepted write receipt semantics remain.

Example mounted module is conversation.js?v=21; sync.js?v=3; uploads.js?v=7.
The B integrator must publish matched assets and the exact A pin for the full
multi-tab guarantee. docs/reference.md is the authoritative changed technical
document. All new visible labels/errors/prose received lead writing clearance.

## Quick evidence

quick-results.json contains exact argv/workdir/head, exit codes, durations and
log paths. Focused native/handler checks passed: codex 0.030s, conversation
0.017s. Syntax plus all six Node contract files passed 85/85 in 1.507s.
Whole-range git diff --check passed. No hook framework is declared; hooksPath
is unset and canonical hooks contain only samples; no hook was bypassed.

Coverage includes 50 deterministic controllers and zero hidden streams/timers,
initially hidden/BFCache restoration, retired callbacks/capability, delayed old
pending/queue/history success/error/finally, real current timeout warnings,
200 output hints over simulated 100s (six freshness reads), coalesced immediate
control invalidation, preserved offscreen citation repair/filters, original
submission/upload selection order matrix, metadata network/backoff/deadline,
body cancellation/malformed JSON, storage failure and zero-write recovery.

Development fixture corrections: legacy brief-hide expectation changed to the
new contract; existing actual upload fixture needed chunkBytes in its limits;
new history draft fixture needed send capability and an explicit durable target.
One coalesced resumed control successor is completed explicitly by its fixture.
Own failed test runners were accounted for and stopped; final checks are green.
These setup corrections are evidence, not commit-message content.

## Prepared later verification, not executed

After final independent review, parent fresh Luna/low utility may launch:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-dev-workspace-portal-improvements/verification/a-followup-6e32a90/post-review-package.sh
```

This guards exact clean A, bounds the standard declared default and generic
source checks to 1200s, saves JSON derivation/output identities and logs, and
retains output roots under this evidence directory. It does not select a
package or mutate live state. The script passes bash -n; no package build was
launched. Default check includes full Go, protocol corpus coverage and all
browser contracts. Existing quick receipts stay separate.

Real Firefox acceptance belongs to the final composed B fixture and must await
its exact published source and final review. Use design.md's pinned driver,
Firefox, display and 1800-second runner shape; B owns
portal/internal/web/firefox_tabs_acceptance.cjs. Record real document visibility,
50 initialized tabs, native discard/restoration, continuous foreground operation,
read/SSE budgets, prompt freshness and one durable dispatch. Deterministic tests
do not establish actual Firefox visibility or reproduce the reported incident.
No HTTP/2 host change or blanket deadline increase is warranted by current
source/host evidence. No full/browser/live/long verification was run here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
