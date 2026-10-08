# Whole-branch inventory

All changes are committed. Runtime has three coherent commits: the viewer, a lifecycle receipt correction required by packaged verification, and a test-only archived timestamp fixture correction. Downstream branches each contain one final pin commit; superseded unapplied pins were consolidated. No obsolete implementations, fixups or unused transition paths remain. No migrations, schema changes, seeds or persisted conversions; no such versions were merged, released, deployed or externally consumed. Earlier heads were verification inputs only.

## dev-workspace

Base: `e3315a483f3d3536d492ecbe40f2655449cf630f`

Head: `9e8e6e87a5a4844d4639ddf4008de483d1897f4c`

```text
d9142d84039a51cce9998ce5048a580fb7c4be3e portal: open shared workspace file links
8f0f40a04f5dcf1b590eb4cb8562bfecebe2962d portal: retry lifecycle proof after receipt contention
9e8e6e87a5a4844d4639ddf4008de483d1897f4c test: keep archived fixture metadata stable
```

 docs/workspace-portal.md                           |  17 ++
 portal/internal/repository/source.go               |  54 +++++--
 portal/internal/web/operation_state.go             |  39 +++--
 portal/internal/web/operation_state_test.go        |   4 +-
 portal/internal/web/server.go                      |   5 +
 portal/internal/web/source_files.go                |  75 +++++++--
 portal/internal/web/source_files_browser_test.cjs  |  20 ++-
 portal/internal/web/source_files_test.go           |   2 +-
 portal/internal/web/static/source-file.js          |   4 +-
 portal/internal/web/templates/source-file.html     |   2 +-
 portal/internal/web/workspace_source_files_test.go | 177 +++++++++++++++++++++
 portal/internal/workspacecodex/observation_test.go |   4 +-
 12 files changed, 356 insertions(+), 47 deletions(-)


## workspace

Base: `48a0d980c24a7e725b40c8854c8e992935639afe`

Head: `70035dfe565058054e30efe2562c655c80dd183c`

```text
70035dfe565058054e30efe2562c655c80dd183c inputs: select the shared workspace file viewer
```

 flake.lock | 8 ++++----
 flake.nix  | 2 +-
 2 files changed, 5 insertions(+), 5 deletions(-)


## vpsfree-cz-configuration

Base: `6f6aff9029cd57e1a0f9201356f7fdc9f6480671`

Head: `5447020fccf99705e65a907cfe6e80684a5a1577`

```text
5447020fccf99705e65a907cfe6e80684a5a1577 inputs: set devWorkspace to 9e8e6e87
```

 flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)

