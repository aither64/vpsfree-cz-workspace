# Final review: portal untracked-file access

Read workspace AGENTS.md, its required project/session/documentation/git/
verification/deployment/commits procedures, each affected repository AGENTS.md,
and ~/.codex/skills/mandatory-change-review/SKILL.md plus all four lane refs.
Remain read-only; perform review directly without subagents.

## Request, ownership and boundary

User wants local file links (especially the Rust rewrite design) to open without
Git staging/artifact registration. User explicitly chose non-ignored files.
Accepted design/verification brief: work/2026-10-18-portal-untracked-files/design.md; plan/state nearby.
Implementation belongs in generic dev-workspace; workspace selects its nested
runtime input and configuration selects the same devWorkspace via confctl.
No codex-web or site-extension source changes. Discover consumers from actual
pins/wrappers. The browser API keeps routes/query fields and SourceKind strings;
artifact selectors also accept eligible unpublished session tracking files.
Explicit published artifact access remains available; publication still controls
artifact list, preview and download. Archived project source remains final-commit
blobs; untracked project files are not snapshotted. Archived tracking files use
actual session lookup plus current Git eligibility. No persisted format changes.

Local host operator is trusted to administer host per repository AGENTS.md.
Remote clients and paths remain untrusted. Assess confinement, no-symlink regular
opens, Git path eligibility, wrong repository/session selection and ignore rules.
Do not add hostile-operator mount/hardlink/physical-ancestor protections.

## Status and verification

All intended changes are committed and clean. Focused checks passed twice after
isolating the known host-provider fixture dependency using an absent
DEV_WORKSPACES_CODEX_PROVIDERS path; latest Go Source/WorkspaceSource subset passed
in 3.111s including JS viewer contracts. Untracked previews enforce existing bounds.
gofmt and git diff --check passed. Configuration Overcommit installed/active;
Nixfmt and commit-message hooks passed (generated message width advisory retained).
Composed workspace/configuration deployment contract passed at runtime 4218c6d3.
Long tests/builds have not started; run after resolving final review findings.

Documentation: dev-workspace docs/workspace-portal.md describes supported file
eligibility, publication distinction, archived behavior and wire compatibility.
The README already links the owning guide. Session records hold rollout details.
User-facing writing skill applied by the context-owning lead.

## Review assignment

Overall risk HIGH: expands authenticated file-access authorization and includes
matching deployment pins. Cover general, architecture/repetition,
scope/proportionality, risk/compatibility. No eligible retained reviewer exists:
initial session created with --no-codex; installed catalog fallback is
lead_reviewed/reviewer, gpt-6-astra, xhigh, read_only. Catalog and matching native
reviewer config are installed under
/nix/store/qxj0iagbq0s2fp8747hfhghvpfam0x6j-dev-workspace-0.2.0/share/dev-workspace.

Assess full base-to-head series and final diffs independently. No migrations,
superseded approaches, or repeated pin streams are present: one runtime behavior
commit, one final workspace runtime selection, one final generated configuration
channel update. Tests/docs accompany the behavior they specify. Explicitly
conclude whole-branch history, repeated-update consolidation and migration lineage.
Nothing has been merged/released/deployed from these feature branches.

Deployment is authorized, master integration is not. Activate system then separate
user profile through the coordinator. Aitherdev is currently reserved by
2026-10-17-archive-worker-authorization; do not bypass. No deployment performed.
Package recovery stays forward-only. Existing state is readable by older code,
which retains narrower access; no fleet coordination or schema conversion needed.

Return ordered findings with severity/path/line/commit, and explicit final
history/migration/repeated-update conclusions. If no findings, state that and
remaining test gaps. You may save the report only under this session tracking
folder (review-report.md), not edit application/project content.

## dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-portal-untracked-files/dev-workspace
Base: 679273d5369a20b68888397c27c813cece48d59f
Head: 4218c6d3d3edda587118e6053585b9e3d511aea2
Complete series:

```
4218c6d3d3edda587118e6053585b9e3d511aea2 portal: open non-ignored untracked file links
```

Final stat:

```
docs/workspace-portal.md                           | 37 +++++---
 portal/internal/repository/source.go               | 73 ++++++++++++----
 portal/internal/web/source_files.go                | 25 ++----
 portal/internal/web/source_files_browser_test.cjs  |  2 +-
 portal/internal/web/source_files_test.go           | 99 +++++++++++++++++++++-
 portal/internal/web/static/source-file.js          |  4 +-
 portal/internal/web/workspace_source_files_test.go | 18 +++-
 7 files changed, 205 insertions(+), 53 deletions(-)
```

## workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-portal-untracked-files/workspace
Base: c01902a5390da05be4e193176d7a8205bc0c5eb7
Head: 7a29fb0beb1d588fa950a51b78f5e262831c22fc
Complete series:

```
7a29fb0beb1d588fa950a51b78f5e262831c22fc inputs: select portal untracked-file support
```

Final stat:

```
flake.lock | 8 ++++----
 flake.nix  | 2 +-
 2 files changed, 5 insertions(+), 5 deletions(-)
```

## vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-18-portal-untracked-files/vpsfree-cz-configuration
Base: 647a3723a1095c6f5c5af44c81031105ee6d648c
Head: d30fc508454b89d82a8dc13c147057caa95d882d
Complete series:

```
d30fc508454b89d82a8dc13c147057caa95d882d inputs: set devWorkspace to 4218c6d3
```

Final stat:

```
flake.lock | 6 +++---
 1 file changed, 3 insertions(+), 3 deletions(-)
```

Workspace-only refresh: rebased the single pin commit over current shared master
c01902a5390da05be4e193176d7a8205bc0c5eb7 (tracking handoff only). git range-diff reports exact equality:
23e59bac = 7a29fb0b. Runtime and configuration heads are unchanged.
