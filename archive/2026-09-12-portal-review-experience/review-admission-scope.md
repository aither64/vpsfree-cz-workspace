# Scope and proportionality review

**Result: 0 Blocking, 0 Important, 0 Advisory findings.**

Reviewed exact committed deltas:

- `codex-web` `bdd79be2..83770217`
- `dev-workspace` `87606197..c3502742`
- `vpsfree-dev-workspace` `db25c77e..a0d7fdca`
- `workspace` `584ea0f6..ef75f045`

## Assessment

The admission repair is proportionate to the demonstrated reconnect failure:

- Admission is confined to `ObserverOnly` clients and centralized around connected RPC dispatch; interactive behavior remains unchanged at [client.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/client.go:596) and [client.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/client.go:614).
- The fixed restoration queue is private, generation-cancelled, and limited to four workers rather than becoming a public scheduler framework at [observer.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/observer.go:14).
- Disconnect and close reuse the same cancellation ownership at [client.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/client.go:574) and [client.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/client.go:939).
- The portal’s per-thread gate is a small consumer-local mechanism placed before its existing authority slot, with reference-counted retirement and caller cancellation at [activity.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/activity.go:70). It directly addresses duplicate browser reads without expanding provider APIs or changing timing persistence.

The completed-deletion repair is similarly bounded:

- Portal retirement first proves destination, authority, worktree, and journal absence under the runtime lock, then consults the existing verified removal marker at [creation_store.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_store.go:168).
- `FindCompletedRemoval` factors the existing marker scanner instead of creating another persistent registry or migration at [removal.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/session/removal.go:34).
- Only the exact receipt, binding, and evidence files are moved into existing deletion recovery storage at [creation_store.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_store.go:195).
- The CLI validates the existing marker and exact retired IDs before creating a binding at [dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2839). Fork repeats the check at its second destination lock, covering its real two-lock race without generalizing the lifecycle protocol.
- The archive correction is only historical wording, not lifecycle reconciliation machinery, at [creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:143).

The tests added in the reviewed commits are proportional to owned behavior: concurrency admission, generation cancellation, exact deletion identity, timestamp ordering, fork’s second lock, and name reuse. They do not duplicate exhaustive Codex protocol behavior.

Commit placement is coherent: provider scheduling is isolated in `83770217`; portal admission remains in the activity feature commit; deletion recovery remains in the creation feature commit; downstream commits contain only dependency pins. The final lock files consistently select provider `83770217`, runtime `c3502742`, and organization package `a0d7fdca`.

## Residual risks and pending gates

- Removal lookup enumerates the retained recovery root in both Go and Ruby. Its cost grows with deletion history, but introducing a new index, schema, or purge contract would be disproportionate without demonstrated scale pressure.
- Packaged VM, live App Server/browser, creation flow, profile upgrade, and rollback validation remain pending as recorded in the packet.
- I ran no tests and made no edits or Git mutations.