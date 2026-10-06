# Complete branch inventory

## codex-web

Base: 32775fa7fdd9bc9b41aef74b7f195e5c3bc0f8d5
Head: 3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-04-upload-display-limits/codex-web

3d07cf60cfde5d117a181a9bdb6d90a5860f6f0c uploads: show selected file count and total size


 conversation/assets/conversation.css   |  2 +-
 conversation/assets/conversation.js    |  4 +-
 conversation/assets/uploads.css        |  6 +--
 conversation/assets/uploads.js         | 11 +++-
 docs/reference.md                      | 11 +++-
 test/uploads_browser_contract_test.cjs | 99 +++++++++++++++++++++++++++++++++-
 6 files changed, 121 insertions(+), 12 deletions(-)


## dev-workspace

Base: 6a972b9ab01077611b2c60e0fc726c185e050315
Head: 3edc605d81a30a4d49560426e0128b388b856493

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-04-upload-display-limits/dev-workspace

13bcfc100e0a9cd0f56b2b89943adb7350cf824f uploads: allow fifty files per prompt and preparation
0ed4e9f9856d14c7e5c3db90a76073ba028e5b6a web: let creation upload cards grow with the page
3edc605d81a30a4d49560426e0128b388b856493 deps: pin codex-web with upload summaries


 README.md                                          |  14 ++-
 docs/session-preparations.md                       |  34 +++++-
 flake.lock                                         |   8 +-
 flake.nix                                          |   2 +-
 nix/workspace-portal.nix                           |   2 +-
 portal/go.mod                                      |   2 +-
 portal/go.sum                                      |   4 +-
 portal/internal/uploads/store.go                   |   5 +-
 portal/internal/uploads/store_test.go              |  69 +++++++++++++
 .../web/preparation_browser_contract_test.cjs      |  36 +++++++
 portal/internal/web/preparation_store.go           |   3 +-
 portal/internal/web/preparation_test.go            | 115 ++++++++++++++++++++-
 portal/internal/web/static/app.js                  |   2 +-
 portal/internal/web/static/creation.js             |   2 +-
 portal/internal/web/static/preparation.js          |   2 +-
 portal/internal/web/static/style.css               |   1 +
 portal/internal/web/templates/creation.html        |   8 +-
 portal/internal/web/templates/index.html           |   8 +-
 portal/internal/web/templates/session.html         |   8 +-
 portal/internal/web/templates/source-file.html     |   2 +-
 test/README.md                                     |  10 ++
 test/creation_browser.cjs                          |  90 ++++++++++++++--
 22 files changed, 384 insertions(+), 43 deletions(-)


No superseded approaches, fixup commits, unused compatibility paths or unapplied intermediate formats. Test expectation fixes were folded into their behavior commits before publication. No migrations: no schema versions introduced, merged, released, deployed or externally consumed. Provider revision was pushed solely for downstream dependency resolution. Runtime count/recovery and layout remain separate commits; generated provider pins are separate. Tests and docs remain with the behavior they explain.
