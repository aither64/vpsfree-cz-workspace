# PENDING-A1 narrow remediation handoff

Published final A **ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5**; tree
`6ca1370f5e22e15f066c6c1573d6773b450650d7`. SSH lease was exact reviewed
`6e32a9043ee6367d92bfaf8d3ebdf48036e275f9`; remote master remains
`57972192e30fe52ab33b867c8fe4d171f59a7fd5`. Local worktree/index clean and
remote feature exact; remote retained refs preserve reviewed A6e and deployed
A852. Source/index/Git ownership is returned to lead. No B/C/config/pin edits.

The only mounted production behavior change retires `pendingLastRead` after
the current/hidden catch guard. A current failed forced read now retries at its
two-second failure backoff even after a recent success. Last prompts/notices,
2/4/.../30-second backoff, generation/singleflight/coalescing, access handling,
and the success fifteen-second floor remain. Example mounted import is v22;
a rendered template assertion binds that actual consumer. Sync v3/uploads v7
unchanged. No visible prose, public API, native, SSE, schema, authority,
scheduler, timeout, dependency, or transport change. Existing reference guide
already describes the intended contract; no documentation rewrite needed.

## Checks actually executed

All checks used A's declared `nix develop --no-update-lock-file` environment.

- `node --check conversation/assets/conversation.js`
- `node --check test/conversation_browser_contract_test.cjs`
- `node --check test/refresh_browser_contract_test.cjs`
- `node --test test/conversation_browser_contract_test.cjs test/refresh_browser_contract_test.cjs`:
  all seven reported cases PASS, duration 1440.934538 ms. `quick.log` retains
  this success followed by the initial Go vendoring error; overall initial
  batch exit 1 is accurately retained in `quick.exit`.
- `go test -mod=readonly ./cmd/codex-web-example -run '^TestStandalone' -count=1`:
  PASS 0.016 s (`consumer-quick.log`, exit 0). The initial plain Go invocation
  hit Nix-shell inconsistent vendoring before running tests; explicit read-only
  module mode resolved it, with no module/vendor/lock edits.
- Go formatting on both example Go files and `git diff --check`: PASS.
  No hook framework is declared: package.json is only private/type=module,
  core.hooksPath unset and the canonical hooks directory has samples only.
  Ordinary commit hooks were not bypassed.

The actual mounted regression uses virtual time but the shipped mount, event
callbacks and real retry timer callback: success t100000, typed forced503
t100100, no early retry, retry dispatch t102100, retained prompt, restored
full15s success floor and due read. Initial mount has two successful reads,
so the failing frozen negative reports actual3 versus expected4 total reads.
`frozen-source/` is an exact Git archive of A6e with only the new two CJS tests
overlaid; its shipped conversation.js is byte-identical to A6e. Same Node
command FAILS exactly at the missing two-second dispatch (703.738578 ms case,
728.39186 ms suite), six other cases pass. `negative-control.log`/exit1
preserved. It is not a setup failure.

Normal mounted abort-race ordering settles the retired catch before resumed
success. The additional direct extracted shipped schedulePending/refreshPending
regression deliberately holds old settlement until successor success, then
rejects the retired read: no notice or freshness reset; normal output remains
behind successor15s floor. No production testing hooks or new framework.

## Complete history and reconstruction

529524829526f41c628bd54d729241c52395c6b2 conversation: present transcripts after attachment decoration
7fb4ab212ba233b94370eeea131762b729ac2505 conversation: distinguish team traffic and quiet history fallback
852e8c51091512bc79ca6c921ef1f5ccc46a9535 conversation: reconcile inline submission failure notices
e8d6d01006d6f4f0c480d9300521b314e174078f conversation: distinguish pending control invalidations
8a2b0bea921b6751be916c442ada891edb4a0ed8 conversation: retire hidden reads and recover current controls
ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 uploads: recover passive file metadata reads


Six logical groups retained, no standalone fixup. Owning lifecycle group
`3d1b21de76df49ad39174ec5e3999d8cffd84bc6` became
`8a2b0bea921b6751be916c442ada891edb4a0ed8`; uploads group has only a new parent.
Five of six stable patch IDs equal; first four commit IDs are literally equal.
Full `range-diff.txt`, `patch-id-map.json`, `final-net.diff`, complete path/stat
inventory and `final-tree.txt` are retained. No migrations anywhere in A series;
none merged/released/deployed/externally consumed by this remediation.
A852 remains a literal ancestor. A6e is retained as an exact reviewed source
ref/receipt, not falsely described as an ancestor of the rewritten lifecycle.

`remediation.patch` is the complete five-path 131-addition/one-deletion A6e delta.
Applying it in a disposable index over A6e reconstructs final tree exactly.
Applying `remediation-inverse.patch` over final reconstructs A6e exactly.
`proof.json` records all95 other tree entries byte/mode-identical and all modes
unchanged; no files added or removed. `quick-source-sha256.json` proves checked
source bytes survived the fold. `expected-tree.txt` was captured before commit
and matches final tree. These proofs are primary; not a broad equivalence claim
for the intentional lifecycle fix.

## Remaining parent-owned gates

Parent reviewer step9 direct focused inspection/closure; imp1 single downstream
A pin and actual B mounted consumer v22 plus C/config mechanical closure after
B's separate Important finding. No long/browser/package runs or CI waits here.
Known same-feature workflow cancellation403 is retained policy/evidence; no
repeat denied cancellation attempt or claim of cancellation. No merge,
deployment, machine claim, live operation or session lifecycle action performed.
Leave session open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
