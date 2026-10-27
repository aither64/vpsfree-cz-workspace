# Correct the independent-feature consolidation guard scope

Remove the local shared-master query/equality from this consolidation only.
It is not a consumed input or operation target. This supersedes the ef1→7d5
expectation refresh in `workspace-f520-shared-master-drift-disposition.md`;
that refresh retained an invalid scheduling dependency. Do not refresh again.

Saved v2 `effects-v1/consolidate/summary.json` remains exit1/5.121251s,
postflight null, SHA256
`7fb9f9acef030e3c2a273c28b836376dc834b4d505f285cd56e53bf3902ed7ba`.
All ten command receipts returned0, joined with empty groups and no signals;
all70 saved evidence entries match. Both guard attempts observed localmaster
`0fe886f56031da55d16aa30e6f110243a0ed0e28` before SSH/add/commit. Saved own
feature/preservation remain0c, generated pair57a0812a/392ea143 and raw9ac are
unchanged. These are saved observations, not a completed current preflight.
No new local-master/SSH, foreign-record or source observation was performed.

The accepted `run-phase.py:299` protected guard checks own branch, SSH origin,
local shared master, retained own refs and hooks. Only the local-master clause
at303 is irrelevant here. The v2 adapter uses its own feature HEAD/tree and
full620 source/57420 tree/index guards, fixed parent3e72, then scoped two-file
add and normal `commit --amend`; it does not read code from or write master.
`preserved_guard` uses the exact own ref/bundle and fixed base. `remote_gate`
separately requires SSH master3e72 and ownfeature0c. No other consumed dependency
on local master was found in this call path. The Git procedure permits
independent feature work while shared tracking advances; it requires no claim
or shared-master lock for this work.

Owner0's smallest successor implementation:

1. Keep the imported original driver/spec/guard and both failed packets
   immutable. Add a local `protected_feature_guard` in the existing successor
   adapter: the original protected guard's branch/origin/retained-ref/hook
   checks with only the local-master query/equality statement omitted. Call
   it from the adapter's guard at every generated/staged/committed/postflight
   phase. Do not catch the old failure, replace Git output or mutate `G.S`.
2. Remove v2's in-memory sharedMaster adaptation and new accepted-master release
   requirement. Bind this scope disposition in the successor spec/manifest;
   keep old master values solely as historical packet data. Fresh exclusive
   results and ordinary parent release remain required, without a new master
   snapshot or another diagnosis phase.
3. Preserve every other guard and operation: session/access/tools, own branch,
   HEAD/tree, full620 bytes/modes/blobs, full57420 tree/index entries and flags,
   exact accepted9ac before staging, generated pair and semantic lock graph,
   preserved refs/bundle, hooks, fresh SSH3e72/0c, two-file amend, final sole
   parent3e72, whole-history/diff proof, settlement and mandatory postflight.

Static acceptance should compare the local guard to the original (allowing
module qualification) and show exactly that one omitted statement; inspect
all guard call sites so none still invoke the old local-master assertion.
Parse/compile the adapter without import/execution and retain the normal small
source delta. No new test harness or live-master observation is needed.
Actual feature/source/index/remote/hook drift still stops normally. No rebase,
Nix repeat, application change, shared claim, foreign-content read or cleanup.
Integration retains its separate target/ancestry gates. This authorizes no
execution; lead owns release. Session remains open.
