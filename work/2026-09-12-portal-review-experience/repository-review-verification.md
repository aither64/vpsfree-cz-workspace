# Local repository review verification

Implementation owner: repository-review agent. Ready for root's focused commit and
mandatory review. No project push or long integration test was run by this agent.

## Delivered

- Bounded native Git reader: verified canonical repositories/worktrees, immutable
  pair snapshots, local 50-commit pages, commit comparisons, raw NUL-delimited
  file metadata and on-demand original blobs. No GitHub dependency for review.
- Private additive comparison records under the existing workspace-specific portal
  state directory; history browsing saves the pair. Integrated exact heads retain
  the last viewed pair; archive reads use final heads/canonical repositories;
  original-base fallbacks preserve the warning about upstream commits after rebase.
- All changed files appear as stacked sections. Sidebar clicks scroll to the chosen
  section; near-viewport content loads lazily. Distant editors and blobs are
  released beyond eight retained sections, keeping measured placeholders. A click
  destination remains stable while neighboring lazy editors settle, until the
  user scrolls, touches, drags, or types in the comparison pane.
- Read-only CodeMirror split/unified views, remembered split default, three-line
  context, no merge controls, bounded detailed diff computation and deletion
  blocks. Dynamic styles receive the page CSP nonce. Dark colors match the portal.
- Locked current packages: merge 6.12.2, state 6.7.4, view 6.43.11, esbuild 0.28.2.
  Self-hosted assets include licenses for every locked runtime/build dependency,
  including optional esbuild architecture packages, plus an integrity manifest.

## Focused results

Passed with Go/GCC/Node from the repository-pinned Nixpkgs:

```
GOWORK=/tmp/portal-review.go.work GOFLAGS= go test ./internal/repository ./internal/web -run 'TestReview|TestRepositoryReview|TestSessionDetails'
node --check portal/internal/web/static/repository-review.js
```

Coverage includes local unpushed commits, rebase/current merge-base selection,
retained old snapshots, integrated and archived comparisons, missing worktrees,
wrong branches/names, tabs/newlines in renames, binary/invalid UTF-8/large/long files,
symlinks, submodules, final newlines, 50/2 commit pagination, root commits, output
caps/timeouts, scoped opaque snapshot/file/commit identities, origin enforcement,
private persisted records, restart recovery and corrupt-record rejection.

The bounded-output test caught promoted `bytes.Buffer.ReadFrom` bypassing `Write`.
A named buffer fixes it; the actual Git subprocess test now proves the cap. See
`notes/dev-workspace/2026-09-12-git-output-cap-readerfrom.md`.

The isolated Nix asset derivation built successfully:

```
nix build --impure --no-link --print-out-paths --expr 'let pkgs = import /nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source {}; in pkgs.callPackage ./nix/review-ui.nix {}'
```

Output:
`/nix/store/qahf3qnx2gskkx0p19pjf3yqhibm9464-workspace-repository-review-assets-1.0.0`.
All three output files are byte-identical to `npm run build` from the local locked
installation: JavaScript bundle, complete license notice, dependency manifest.

## Chromium UI harness

`artifacts/repository-review-browser.cjs` is a focused fixture server/browser
harness. Run from the dev-workspace worktree using the Nix Node, playwright-driver
and Chromium packages. Set `PLAYWRIGHT_MODULE` to the driver's output path,
`CHROMIUM_EXECUTABLE` to its executable, `REVIEW_ASSETS_DIRECTORY` to the Nix output
above, and optionally `REVIEW_SCREENSHOT_DIR` to a writable screenshot directory.

The final run passed:

- Two cards at 1440×900; one card and usable stacked comparison at 390×844.
- Commit-body disclosure and DOM identity survive status HTML refresh.
- All 30 changed-file sections exist, with only 17 blob requests during the entire
  scenario; selecting the final file reveals it fully after neighboring loads.
- Split has both line-number gutters; unified has only the current-file gutter.
- No editable content surfaces or merge controls in either mode.
- Open comparison scroll survives status refresh; changed-head notification leaves
  the viewed pair unchanged until explicit refresh.
- Zero page exceptions or CSP violations, with all assets loaded from the fixture
  origin.

Curated screenshots: `artifacts/repository-review-desktop.png` and
`artifacts/repository-review-mobile.png`.
