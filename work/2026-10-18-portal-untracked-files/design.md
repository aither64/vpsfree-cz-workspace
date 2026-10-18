# Portal untracked-file design and verification brief

The lead owns this bounded implementation. There is no retained team roster;
independent final review uses the installed catalog fallback. Keep all application
changes in the generic dev-workspace repository.

## Interfaces and flow

Keep /files/<slug>, /workspace-files and their current JSON APIs and source enums.
Source links remain pure path mappings. Every file request independently checks
the trusted workspace/session/repository identity. A shared helper admits exact
regular Git index members or exact non-ignored untracked paths using literal
pathspecs and NUL-delimited output. Read current disk bytes with OpenRegularFile
and ReadSourcePreview. Fail closed on Git failures, unsafe modes or paths.

The session artifact selector first retains existing explicit catalog access.
Other eligible paths resolve under the actual session tracking root and use
the workspace Git index/ignore policy. A session-only fixture without a workspace
Git repository must keep working for already published artifacts. Do not expand
artifact listing/preview/download authorization. Use generic session-file viewer
labels so unpublished files are described correctly without new wire values.

## Invariants and compatibility

Preserve repository ownership checks on each request, shared/session routing
boundaries, no-symlink confined opens, regular-file checks, literal names,
Git metadata restrictions for new access, no-store headers and preview bounds.
The local host operator is trusted; remote input remains untrusted. Do not add
hostile-local-operator hardlink/mount/ancestor protections outside repo policy.
Published artifact semantics and normalization remain unchanged. Index members
remain readable when a later ignore rule matches them; only new untracked reads
depend on excludes. Sensitive ignored unpublished records remain unavailable.

Archived tracking paths use archive/<slug>; old work/<slug> links follow session
lookup. Archived repository reads remain immutable final-commit blobs. No new
snapshot, journal, schema or migration is introduced; older versions retain
readable state and narrower access. No coordinated fleet update is required.

## Deployment and recovery

Publish dev-workspace, select its exact revision through the workspace's nested
runtime URL and configuration's dev-workspace/devWorkspace channel. Preserve
extension and unrelated inputs. Check composition; independently review completed
committed changes before long tests. Build/prepare outside execution claims, then
use approved system and profile jobs under the same aitherdev reservation.
Keep reservation during UI review. Default-branch integration needs separate
user direction. Package failures use supported original-attempt forward recovery.

## Acceptance and checks

Quick Go file-reader/HTTP and JS contracts must cover the actual malformed catalog
case plus absent artifact registration, untracked project/shared/tracking files,
Git/local excludes, explicit publication, tracked ignored files and active/archive
tracking resolution. Check path encoding/Unicode/line references, wrong ownership,
missing files, symlinks and special files, binary/size/line preview limits.

Final review includes whole-branch history and "no migrations" conclusions.
Longer verification: runtime flake checks and package, composed workspace checks
and package, matching configuration preparation/CI. A fresh watcher owns each long
batch. Live acceptance opens the original Rust link, then verifies disposable
untracked/ignored files through the deployed APIs and viewer. Preserve unrelated
sessions and remove only our disposable fixtures.
