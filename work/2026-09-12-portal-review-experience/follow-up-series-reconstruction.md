# Portal follow-up focused series reconstruction

- Worktree: `worktrees/2026-09-12-portal-review-experience/dev-workspace-series` (detached).
- Base: `d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2`.
- Reconstructed head: `820277e6cc3aa7ff9acb0396feb3314e7f84996a`.
- Original final target: `0474e62d982faaac80c823744c1aac3cc53b1681`.
- Both full Git trees: `19a507d97a5cce1a51490807a7ddf4fab853d550`.
- Whole-tree diff and whitespace checks passed; both primary and detached worktrees were clean. Primary HEAD was left unchanged.

## Ordered commits

- `36a2997` inputs: pin shared conversation copy controls
- `1e33b23` portal: keep accepted steers visible until transcript observation
- `b1374e8` portal: clarify the waiting-for-instructions label
- `541e077` repository: return complete commit messages and file statistics
- `3c14009` portal: share repository discovery and bound Git admission
- `4cfa56c` portal: cache immutable review data and coalesce duplicate reads
- `3557355` portal: restore durable comparisons at their recorded revisions
- `eea9497` portal: batch repository reads and include the first file preview
- `c1265c2` portal: highlight complete sources in repository reviews
- `e9a037d` portal: wire query tabs and shared copy controls
- `820277e` portal: make repository reviews shareable and easier to navigate

## Original-to-reconstructed mapping

- `ebc0e4a` provider pins -> `36a2997`, before browser copy-helper use.
- `5bc5f02` -> `1e33b23` receipts, `b1374e8` waiting label, `e9a037d` query-tab/shared-copy wiring.
- Native DTO/statistics commit `8ad9f5e`, plus `03f06b3` logical-line fix -> `541e077`.
- Remaining `b924a15` -> `3c14009` discovery/admission, `4cfa56c` immutable cache, `3557355` durable restore, `eea9497` batching/inline preview.
- `5eeed4e`, notice whitespace from `3410222`, editor/worker grammar and boundary changes from `2ddfc9e` -> `c1265c2`.
- `a10fcb6`, strict eight-file retention from `7d2c272`, version normalization from `534ce67`, and lazy-editor correction from `0474e62` -> `820277e`.

## Verification

Each intermediate backend stage passed focused native/HTTP/session tests. Cache, durable and batch stages passed these under the race detector. Shipped-browser/API contracts were checked at backend stages and wiring/UI stages. Exact timings and paths are in `follow-up-series-reconstruction.json`.

The editor build and all seven editor tests passed (4.276 s). Run `node build.mjs` before `node --test editor.test.mjs`: the bundle test consumes `dist/review-build.json`. The first isolated check used the reverse order and failed only on missing generated metadata; it was corrected before the editor commit. Renderer dependencies were exposed by a temporary symlink to the primary checkout’s existing node_modules, then the symlink and local generated dist were removed. No tracked production changes were made to fix setup.

The renderer is now committed before wiring and UI; all commits used `git commit -F`, followed by a detached-only interactive rebase of the last three commits to establish their final order.

Final full Go suite passed with `GOWORK=off go test ./...` in the narrow runtime Nix toolchain: command 0.084 s; cluster 0.394 s; processgroup 1.098 s; repository 8.736 s; session 2.203 s; web 39.684 s; workspacecodex 0.154 s. No long integration or deployment was run.
