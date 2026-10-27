# Index reconciliation and static continuation

Outer67453 ran the exact scoped Nix update once: actual exit0 in35.9206s.
The full runner exited1 in43.6139s at its subsequent raw-index guard. Both facts
remain in the original v2 receipts. No generated-guard/semantic/post-update proof
is retroactively added there. The original LANG refusal, accepted prepare,
preservation ref/bundle and every original expectation also remain untouched.

## Actual index diagnosis

Both raw indexes are separately preserved here: original6cc097e8 and post-Nix
c823fc4f. Each is valid Git index v2/count57420 with a correct SHA-1 trailer.
The full10,253,032-byte entry region is byte-identical, SHA256
`29ba5972123362887e04b318ac6317b803c829cf1b96b63d422752d3d0702ed9`.
Full old/new inventories include paths, modes, blobs, stages, all raw flags,
assume-valid, skip-worktree, intent-to-add and every stat/cache field. There are
zero entry changes. All57420 entries are stage0 and all three special-flag counts
are zero. Independent read-only Git CLI inventory matches the binary decoder;
all57420 `ls-files -v` tags are H and the staged delta is empty.

Only the derived TREE extension changes: its root record goes from valid
count57420/treeb86 to invalid count-1/noOID, making the extension23bytes shorter.
All5948 child TREE records/bytes remain identical. The extension size and index
trailer change accordingly. This is cache-only invalidation, without staged
content, flag or stat-cache changes. No specific writer is attributed from timing.
No broad store scan, Nix evaluation/hash query, upstream source fetch or native
investigation was used to invent a source-level cause.

Parent independently proved the same exact byte relation and accepted only that
equivalence in `parent-index-byte-equivalence-v1.json`, SHA256
`56c11acab2688b5a680a75e0d366790c3947d48fef7b51f75fbb6fd14d17fcf1`.
That receipt explicitly leaves source/semantic/consolidation acceptance pending.
Original `inputs.json` and `original-guard.py` are byte-identical historical
copies; their original6cc raw-index expectation is never replaced or reported
as passing against c823. New `continuation-inputs.json` binds the explicit parent
equivalence and actual successful Nix receipt, with generated files taken from
the real v2 after-effect snapshots. The old149 retained files are hash-bound.

## New, separately released continuation

This is static preparation only. New parent release records must name the new
manifest, actual accepted vendor receipt, exact index-equivalence receipt and
actual Nix receipt. Those records are absent until parent release. `ready.json`
contains exact argv/cwd and the unchanged v2 explicit environment construction:
all original nonnull values set, nulls absent, forbidden caller overrides refused
before filtering, only the three named optional transport/session variables
forwarded. No live environment values replace an expectation.

The launcher supports read-only `guard`, future `validate` and separately held
`consolidate`. There is no prepare or update action. The continuation runner has
no Nix invocation or Git fetch code. Complete runner/launcher diffs from v2 and
the three-line source-guard gate adaptation are preserved. The original strict
raw-index validator remains intact in original-guard.py.

Future `validate` uses new exclusive `effects-v3/validate` receipts. It verifies
actual Nix0 and actual generated c704 URL/a6fa lock bytes, retained history,
session/role/tools/hooks/protected inputs, exact approved c823 raw index and
all57420 semantic entries/flags. It independently validates the existing620
source files and full accepted c31 input graph, preserving extension767/rootd58,
client025/ea188/f20, unrelated nodes/edges/follows/filtering. It captures the
skipped narrow diff, whitespace, semantic and generated-byte receipts, with
fresh SSH default3e72/ownfeature7c3 gates before and after. No source/index/ref
mutation is part of validate. These fresh remote calls have not run yet.

New guard outputs explicitly identify this continuation and parent-approved
cache equivalence; they never claim the original raw-index gate passed. A
read-only static diagnostic may establish local source/graph facts but does not
claim parent acceptance or completed fresh remote postconditions.

Only after parent assesses actual validate success may a separate release run
`consolidate`. It must consume this new validate summary and exact generated
bytes, not either failed update summary. It preserves the old ef ref/bundle,
freshly rechecks remote/tool/source authority, stages only the two flake paths
and uses normal `git commit --amend -F` with the owned temporary messagefile.
Before staging, c823 is required. After authorized staging/commit, a full index
semantic comparison permits exactly those two new blob IDs while preserving
every other path/mode/stage/flag. Final original source/tree/history checks
require one logical commit over3e72, two changed files, clean state and all other
Git modes/blobs unchanged. Publication stays held.

## Failure and effect boundaries

All new phase/log directories are exclusive-create, with no retry or reuse.
Local guards30s/SSH90s/normal commit120s and owned command TERM/KILL joins5s each
remain finite. Preserve actual source/head/tree/index/status/staged effects on
failure, then return to parent. No replacement index, reset, stash, manual
restore, cleanup, output inference, test/build/checker/provider/native/VM,
publication/default integration, claim/deploy or lifecycle action is authorized.
No active/uncertain own command remains from diagnosis. The source stays frozen
at prepared/generated ef: only the two working flake paths differ, index entries
still describe ef exactly. Existing project update/deployment docs remain valid.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
