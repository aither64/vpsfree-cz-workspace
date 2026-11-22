# Explicit archive rejects a completed lifecycle

On October 14, explicit archive of `2026-10-05-network-ipv4-left-counter`
failed with `initiative lifecycle is complete; cannot archive it as archived`.
The session's anchored lifecycle was valid and its integrations were recorded.

The installed executor in
`/nix/store/2jxac4wqrj2j7sk2czi0p0fdfznn14wj-dev-workspace-0.2.0`
uses `archived` for manual CLI/browser archival. `archive` accepts a completed
source state, but the tracking projection calls `tracking_lifecycle_content`,
which still accepts only `active` or an already matching target. Completed and
abandoned source states fail when the target is `archived`. The helper's header
replacement also hardcodes `lifecycle: active`.

The mismatch was introduced by the October 12 change
`f02ed71165ebc6d64e70a21248ba84bdc55366d2` in `dev-workspace`. That change added
neutral explicit archival without updating the existing conversion helper.
Explicit-archive tests cover active fixtures. Existing completed-state tests
select the strict internal archive policy, whose target remains `complete`.

Loading the installed Ruby executor without executing its CLI and invoking only
the pure helper reproduced the exact error with the actual session state.
Active-to-archived and archived-to-archived succeed; complete-to-archived and
abandoned-to-archived fail.

The required correction is in the runtime's lifecycle conversion: accept valid
source lifecycles for an explicit `archived` target and replace the actual
matched lifecycle header. Preserve strict completion/discard checks and retry
policy. Add end-to-end explicit archive/revive coverage for completed and
abandoned inputs. This investigation did not implement or deploy that change.
Changing the session back to active would conceal the runtime bug and discard
its correct completion status.

This refusal occurs while projecting tracking, before the archive journal or
cleanup sidecar is published and before worktree removal or the tracking move.
Earlier preflight may already quiesce agents and capture recovery, so a failed
archive should not be assumed to have had no runtime effects.

Evidence and scope: `work/2026-10-14-archive-complete-investigation/state.md`.
