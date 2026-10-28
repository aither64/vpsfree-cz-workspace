# 2026-10-28-files-tab-limit-diagnosis

## Goal

the "Files" tab in dev-workspace portal is broken, it says that it has a hit file count limit or file size limit and it shows nothing. See what it is about and suggest a solution.

## Affected repositories

- `dev-workspace`: lazy directory API, browser tree, tests and documentation.
- Coordination workspace: tracking plus a feature worktree for composed runtime pins.
- `vpsfree-cz-configuration`: matching `dev-workspace` channel pin and aitherdev build preparation.

## Approach

The user accepted the implementation plan with "Implement the plan".
`architect0` finalizes the decision-complete brief in `design.md` before source
implementation. `implementer0` owns one coupled runtime package through source,
tests, technical docs, quick checks, commits and review fixes. `implementer1`
owns dependent workspace/configuration pins and build preparation after the
final runtime feature revision is published. `reviewer0` independently reviews
the complete committed branches after quick checks, before long verification.
The lead owns tracking, acceptance inspection and approval-bound coordination.

## Decisions

- User steering after inventory: the viewer need not list every file at once;
  directories can start collapsed. Primary proposal is now genuine lazy,
  directory-by-directory browsing: initial root children only, fetch children
  when expanded, and bound huge individual directories. Visual collapse alone
  cannot resolve a recursive backend listing failure. Partial recursive listing
  is an optional interim mitigation, not part of the selected implementation.

- Implementation is authorized; default-branch integration and actual activation
  require separate explicit approval after the concrete result is reviewable.
- Alphabetical pages selected by the user: directories first, case-sensitive
  UTF-8 basename ordering. Fixed 200-entry/256 KiB pages, stateless generation-bound
  keyset cursor, immediate-directory scans only and bounded memory.
- Use dedicated feature worktrees for all three repositories. Publish feature
  branches; preserve unrelated shared state and required hooks.
- Initial diagnosis did not inspect another session. The user's follow-up
  "see what sessions have so many files and why, it is suspicious" authorizes
  read-only metadata inventory of session tracking roots and narrowly selected
  nonsecret tracking prose to explain contributors. No peer worktrees, teams,
  transcripts or private runtime state are in scope; no cleanup is authorized.
- Do not clean, compact or alter the inventoried peer sessions.

## Compatibility and deployment

Keep the legacy recursive endpoint compatible for old clients; add an explicit
directory endpoint. Preserve session-root/nofollow/path checks, ignored-file
visibility, work/archive selection, direct file links and preview/download guards.
No state/schema/CLI/Codex migration. New UI requires the new API and must never
fall back to recursive scanning. App assets and backend roll out together.

Select one exact runtime revision in the workspace's existing nested input and
configuration's confctl-owned `dev-workspace`/`devWorkspace` channel. Preserve the
extension, native Codex and unrelated pins; check the deployment contract.
Build the composed application and aitherdev before approval or machine claims.
When authorized, deploy changed host closure through confctl before user-profile
selection; keep transitions guarded and recover forward. No activation is yet
authorized. Machine release requires verified deployment and integrated lineage.

## Documentation

Readers: the user and a future implementer. Preserve investigation evidence and
the proposal in [design.md](design.md), with the current phase and limitations in `state.md`.
Update runtime portal docs with supported browsing/compatibility behavior.
Keep review/build/rollout evidence under this session. Lead applies the required
user-facing writing workflow to visible copy before final commits.

Follow-up inventory findings belong in `file-inventory.md`; report exact observed
counts separately from inferred reasons for generated/vendor/cache/test files.

## Testing plan

Focused Go and browser contract/syntax checks first. Cover lazy nonrecursive
root loading, >5,000-child pagination, byte boundaries, mutation/409 behavior,
confinement, collapse/cancellation/concurrency, refresh/selection and legacy links.
Commit intended changes, inventory full base/head series and pin/migration lineage,
then independent review. Resolve findings before long full Go/package/composed
workspace/host checks, launched by fresh catalog-matched verification watchers.
Keep test/build data outside tracking trees; retain compact receipts only.
