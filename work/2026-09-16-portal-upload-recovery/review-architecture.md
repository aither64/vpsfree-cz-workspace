# Architecture and repetition review

## Findings

### Important A1: remember completed server deletion when local persistence fails

- Repository/commit: codex-web `20680804ac5301b27b2726b99f1ec4d9281a8305`,
  present at reviewed head `5c2c77b4649ec9aa6833ad0b7214f7702733e87e`.
- Locations: `conversation/assets/uploads.js:313-320`, with
  `save`/`failed` at lines 246-257 and `ready` at line 245.
- The server DELETE can succeed before `save(next)` fails. The catch path
  retains the old entry with `state: "ready"`, then `failed()` calls `save()`
  again. If that write succeeds, it clears `persistenceError`. Consequently
  `ready()`, the host `onChange` notification, and `ids()` all consider the
  deleted attachment usable. Another attachment's successful save can produce
  the same recovery after a longer storage outage.
- This is a missing state transition between remote deletion and durable local
  removal. Both real portal forms consume the shared readiness/ID contract
  (`dev-workspace/portal/internal/web/static/app.js:1213` and `:3025`). They can
  enable submission with a deleted ID, which the runtime then rejects in
  `portal/internal/uploads/store.go:796`.
- Reproduced using the exact reviewed ES module through a DOM double and the
  provider's pinned Nix Node. Start with one ready attachment, let DELETE
  succeed, fail exactly the next storage write, and permit subsequent writes.
  Result: `serverFileRemoved=true`, `count=1`, `ready=true`,
  `onChange={ready:true,count:1}`, and `ids()` contains the deleted ID. The
  persisted card retains `state:"ready"` and the storage error.
- Required correction: after successful server deletion, preserve an
  unavailable/pending-local-removal state before attempting local persistence.
  A later successful save must not make that ID usable. Cover a single failed
  write followed immediately by a successful write, as well as retry removal.
  No new endpoint or generalized persistence framework is needed.

### Important A2: recover existing identities before applying new-file policy

- Repository/commit: dev-workspace
  `b7bba46a73269a92f550aeee0a0a6dea81b655c3`, present at reviewed head
  `7bb347ccda2eba302d84fc0529ca6bbd6f4d1bc1`.
- Locations: `portal/internal/uploads/store.go:486` and `:502-508`, interacting
  with codex-web `conversation/assets/uploads.js:267-270` and `:309-311`.
- The predecessor validation rejects C0 and DEL, but permits C1 characters
  U+0080-U+009F. The new `unicode.IsControl` check rejects C1 before searching
  for a previously accepted client identity. An older successful create whose
  response was lost therefore cannot reconcile after upgrade if its name
  contains C1. Replay returns 400 although the existing upload remains. The new
  browser interprets 400 as definitive rejection and removes the card without
  deleting that server upload.
- This is an actual provider/consumer contract mismatch: rejection of the
  current request does not prove that a previous request using the same
  identity was never accepted. Retention eventually expires the orphan, but
  legacy removal does not perform the promised reconciliation and cleanup.
- Reproduced in a temporary archive of exact runtime head `7bb347c`, without
  changing the project worktree: create an uploading record, seed the unchanged
  catalog with the predecessor-valid name `input\u0085.eml`, then replay its
  identical client ID/name/size. Result: HTTP error 400, while `List` still
  returns the original ID in state `uploading`.
- Required correction: preserve identity validation and scope checks, recover
  an exact existing identity before applying the policy for new files, and
  retain conflict detection for changed metadata. Test legacy C1 recovery and
  deletion while confirming genuinely new C1 uploads remain rejected.

No additional architecture or meaningful repetition findings.

## Reviewed revisions

| Repository | Base | Head |
| --- | --- | --- |
| codex-web | `882c88ccfbebfb646fb2cafbe9bc6790141b2d13` | `5c2c77b4649ec9aa6833ad0b7214f7702733e87e` |
| dev-workspace | `5d853b6b0c2608549a1f0e940c680ccb40a14bec` | `7bb347ccda2eba302d84fc0529ca6bbd6f4d1bc1` |
| vpsfree-dev-workspace | `b75cc8a6270219ca2fc25c1e292ce030fc33e45d` | `471b412a17e5a508aa18f56e0495ff07cda3248f` |
| workspace | `94f8add7ca745ae9b35e2ee700e923663a2c5a02` | `54e330b05c9274c242a659cc287454415e812c3f` |
| vpsfree-cz-configuration | `b6e650ad902482b4c4e66b5a89a4275bed92419e` | `d7936f735c4850d447cea3a8e43dc50a0d80abd7` |

Reviewed personally with the assigned gpt-6-astra/xhigh lane; no delegation or
project-code edits. Read the lane instructions, local AGENTS files, packet,
plan/state, commit series, changed tests/docs, and adjacent implementation.

## Ownership and consumers checked

- Provider owns the browser state machine and HTTP encoding. Runtime owns
  filename/storage policy, identity recovery, scoped authorization, retention,
  and immutable file paths. This division is appropriate and the fix is shared
  by `mountConversation` and both runtime portal forms.
- Imports and workspace Go-module discovery identify dev-workspace as the
  external Go consumer; other discovered matches are worktrees of the same
  provider/runtime projects. Runtime Go module, sums, flake source revision and
  vendor-hash update move together. Its packaging already checks module/source
  revision agreement.
- Organization `lib.mkPackage` consumes the runtime; workspace consumes that
  organization package. Their exact transitive pins match the reviewed heads.
- Configuration imports only `devWorkspace.nixosModules.host`. Its older pin is
  `e9ed544b`; the host module and host-path files are unchanged between that pin
  and `7bb347c`. Application deployment remains owned by the user-profile
  package. No new system/application coupling was introduced.
- Provider imports uploads v3 and the actual portal imports conversation v9.
  Browser creation metadata is optional and does not change the Go catalog.
  UUID storage paths, restricted extensions, JSON prompt encoding, MIME header
  encoding, and text-node rendering retain their existing owners.
- Functional browser recovery and HTTP UTF-8 boundary changes are separate
  provider commits. Runtime validation and provider consumption are separate
  commits; remaining repositories carry dependency changes only.

## Verification and residual gaps

- Personally reran all three provider browser-contract suites through pinned
  Nix Node: 41 tests passed. Existing persistence coverage holds writes failed
  throughout the removal attempt, so it misses A1's intermittent failure.
- Both findings have targeted reproductions against exact reviewed code. The
  coordinator has acknowledged them and is preparing narrow corrections;
  this artifact records the original review, not validation of future commits.
- Real Firefox behavior, warm-cache upgrade/rollback, actual form acceptance,
  full package checks and deployment remain pending as stated in the packet.
  No long integration or deployment action was run by this reviewer.
