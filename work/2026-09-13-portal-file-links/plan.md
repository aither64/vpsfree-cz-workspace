# 2026-09-13-portal-file-links

## Goal

Open absolute file links in portal conversations and curated Markdown artifacts
in a read-only source viewer at the referenced line. Previously copied portal
URLs containing the absolute filesystem path must work too.

## Affected repositories

- Generic dev-workspace owns Markdown rewriting, source resolution, HTTP routes,
  and the browser viewer. Reuse its repository review editor in full-file mode.
- vpsfree-dev-workspace and workspace consume the generic package through exact
  input updates. Use dedicated feature worktrees for both consumers.
- codex-web needs no change: the portal already supplies transcript HTML through
  its transformation hook. vpsfree-cz-configuration needs the same generic
  revision because the workspace deployment contract requires exact host/runtime
  pins. This updates the host-module input through confctl; the application
  itself continues to come from the user profile.

## Approach and decisions

- Canonical repository links use /files/<slug>?repository=<id>&path=<relative>#L10;
  curated artifact links use /files/<slug>?artifact=<relative>#L10. A read-only
  session file API resolves the same target and returns content/source status.
- Rewrite Markdown link destinations without changing original message text.
  Recognize absolute paths, :line, :line:column, and #Lline references. Use one
  parser for rewriting and old absolute website-path redirects. Preserve ordinary
  external links. Decode URL escaping once and validate path components.
- Show the current worktree file, including uncommitted edits and staged new
  files. Require Git index membership. Untracked files, Git metadata, symlinks,
  traversal and non-regular files are unavailable. Revalidate repository identity
  and access on every read. Reuse existing verified repository discovery.
- Allow plan.md, state.md and explicitly registered artifacts. Follow the
  existing active/archive tracking location; do not expose arbitrary workspace
  or host files.
- After archival, read the exact recorded final commit from the canonical Git
  repository and label it clearly. Missing active worktrees fail without silently
  substituting committed content. Links are live references, not snapshots taken
  when a message was generated, so lines can move after edits.
- Reuse syntax highlighting, selectable line numbers and line reveal. Preserve
  normal browser navigation, reload and opening links in new tabs. Render
  Markdown as source. Show useful missing-file, missing-line, binary and preview
  limit messages. Reuse 512 KiB/12,000-line repository preview bounds.

## Compatibility and deployment

Read-only additive routes and rendering changes introduce no persistent schema,
database, Codex protocol, CLI, Nix option, or journal migration. Existing stored
transcripts and manifests remain unchanged. New and old package generations can
load the same state; rollback restores the old rendering/404 behavior.

The user authorized aitherdev deployment. Update generic -> organization ->
workspace package pins, set the matching devWorkspace input with confctl, build
the complete package and aitherdev configuration, dry-activate, use workspace-host
switch from the workspace feature worktree, then activate the host configuration.
Do not merge configuration default branches as a deployment shortcut. No nginx
route change is needed. Keep the
session and branches open. The user subsequently authorized default-branch
integration and cleanup; archive/delete remains outside the requested cleanup.

## Testing plan

Quick Go and Node/editor checks cover the supplied examples, historical
transcripts, redirects, access boundaries, index/worktree differences, archived
final commits, artifacts, escaping, binary/size limits, and line endings. Commit
all intended changes and run mandatory review (high risk due to remote file-read
authorization; general, architecture, scope and risk lanes, sol/xhigh) before
long packaged and live browser integration tests. Resolve findings and inspect
branch GitHub Actions results. Verify authenticated viewer/API access and line
anchoring through the deployed portal, including normal navigation and new tabs.

## Integration and cleanup

The user requested merging into default branches and cleaning up. Fetch every
default branch, preserve newer work, integrate independent repositories from
fresh temporary worktrees with fast-forward-only merges, and integrate the
workspace feature through the shared master checkout without staging unrelated
changes. Keep local and remote feature branches. Remove the clean initiative
worktrees and transient captures after validation, retain curated evidence and
commit one consolidated integration/cleanup record. Leave the session available
for follow-up; no archive or delete is requested.
