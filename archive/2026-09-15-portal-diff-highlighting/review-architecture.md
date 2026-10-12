# Architecture and repetition review

## Findings

No Blocking, Important, or Advisory architecture findings in the reviewed
committed ranges.

## Reviewed scope

| Repository | Base | Head |
| --- | --- | --- |
| dev-workspace | `9a1b16464e45d722110b448a79315a0f3ce134aa` | `5d853b6b0c2608549a1f0e940c680ccb40a14bec` |
| vpsfree-dev-workspace | `c6afe2905506fba0b8e372e0436b570f5597f8bd` | `b75cc8a6270219ca2fc25c1e292ce030fc33e45d` |
| workspace | `259c0c3fe7d4f3d454f8b27172cb7a8f99ca79be` | `80b93a8c6b120ce178b4a6479901fde12156e3d5` |

Reviewed each commit and final diff, applicable `AGENTS.md` files, the packet,
plan/state/diagnosis, adjacent model and rendering code, locked CodeMirror
implementation and declarations, tests, packaging, and relevant documentation.

## Architecture assessment

- Runtime commit `5d853b6` changes the existing owning boundary:
  `portal/review-ui/editor-model.js:1,46,89`. The public `presentableDiff`
  export in locked `@codemirror/merge` 6.12.2 accepts the existing `DiffConfig`
  and returns the same `Change` coordinate contract. Its implementation calls
  the configured raw diff and then applies presentation cleanup. No local
  duplicate of the library algorithm or new compatibility layer is introduced.
- Both layout entry points still delegate to `reviewProjection`
  (`editor-model.js:111`), and both render its marks through the same
  `changeDecorations` function (`editor.js:97`). Each library invocation sees
  only the removed/added strings of one validated Git block; projection clips
  its marks to source rows. Git classification, line positions, immutable
  source text, and Shiki foreground tokenization retain their existing owners.
- The four new cases (`editor.test.mjs:82`) exercise the two public projection
  entry points, reuse the existing independent Git-range/source-preservation
  checks, and assert visible marked text. The small layout helper does not
  duplicate a behavioral policy or require a new test abstraction.
- Consumer discovery through imports and package constructors confirms the
  existing direction: runtime `flake.nix:25` builds the portal assets;
  extension `flake.nix:81` consumes runtime `lib.mkPackage`; workspace
  `flake.nix:47` consumes extension `lib.mkPackage` with site configuration.
  The consumer commits change only their intended source pins and lock nodes.
  There is no downstream highlight implementation needing a matching fix.
- `nix/review-ui.nix` already includes both modified files and runs the editor
  tests when building the assets. The feature therefore reaches the consuming
  package through the existing reproducible build path. The runtime comment
  records the relevant design rationale; checked README and portal-guide
  contracts remain consistent with the implementation.

## Residual risks and verification gaps

- Presentation cleanup remains a heuristic, as explicitly accepted in the
  packet. These examples do not promise whole-line emphasis for every unrelated
  rewrite or semantic correspondence between paired lines.
- This review inspected the tests and recorded quick-check results; it did not
  independently repeat them or execute package builds, browser acceptance,
  activation, or rollback. The planned consumer build and original-comparison
  verification in both layouts remain necessary deployment evidence.
- No schema or package-constructor contract changes are present. Existing
  activation preflight and rollback obligations still apply to deployment;
  this review does not authorize any session lifecycle action.
