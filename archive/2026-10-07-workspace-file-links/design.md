# Shared file viewer design and verification brief

## Verification-driven lifecycle correction

Packaged builds reproduced pre-existing archive/delete receipt races. The
clean baseline also reproduces the archive failure. Reliable verification and
deployment require a focused correction in operation_state.go: distinguish a
discarded reconciliation proposal from an accepted proposal, and retry mutation
proof from a fresh receipt and journal when another writer wins the CAS. Keep
display refreshes best-effort; they may discard stale proposals as before.
The mutation reader must return the exact accepted proposal, rather than recopy
an independently changed receipt after acceptance. Retry within its existing
15-second cancellation context and existing shared generation lock, retaining
receipt persistence, missing-record revisions and all mutation identity checks.
No persisted format, public API, generation policy or destructive command changes.

The full packaged check later exposed a test-only time boundary: the archived
observation fixture generated time.Now().Unix() for every read, so otherwise
stable metadata changed across a second boundary. Capture its updatedAt once
before starting the mock server. This bounded fixture correction retains the
production metadata equality check and cold archived queue boundary. Keep it
as a separate test commit and include the final heads in related independent
review. Verify the exact fixture repeatedly and retain original failure logs.

Keep this prerequisite in a distinct focused runtime commit. Update both pins
to the resulting exact head and have the same independent reviewer cover all
lanes affected by the lifecycle change and complete final branch history.
Quick verification: existing reconciliation CAS tests plus archive/delete
replacement tests under 300 iterations. Packaged checks and live viewer
acceptance remain the longer checks. Do not accept the previous failed runs as
successful verification or suppress the failing tests.

The originating lead owns design and application edits. The newly created
initiative has no retained team roster, so ordinary lead work applies without
adding members. Use the installed catalog only for the temporary final reviewer
and fresh verification utilities. Design and implementation use xhigh effort.

## Owning interfaces

dev-workspace owns workspace-aware Markdown and file access. Keep codex-web
unchanged. Extend source_files.go's structural mapper to accept valid shared
relative paths before applying the existing session-shaped rules. Repository
source.go owns ValidWorkspaceSourcePath: ValidSourcePath plus exclusion of the
top-level work, archive, worktrees and repos namespaces. Existing .git rejection
applies in every path component. Both structural mapping and the API use this
same policy so links cannot bypass session publication by changing their route.

Add /workspace-files?path=... and GET /api/workspace/file?path=... . Queries must
contain exactly one path value and no other keys. Use the existing source line
suffix parser and #L fragment semantics. Old absolute-path requests use the
same mapper/redirect. Shared routes do not require a session or its repository
registration; they remain behind existing workspace authentication/security
headers. The API returns SourceFile with source=workspace, a relative path,
no repository/revision, and the existing bounded ReviewBlob.

## Read boundary and reuse

Add ReviewReader.WorkspaceSource. Verify Git --show-toplevel equals the
configured canonical workspace and reject a non-Git or nested-root mismatch.
Use the existing sanitized, bounded, optional-lock-free Git runner and literal
ls-files --stage -z membership. Extract the existing live tracked-file read
from Source into one private helper shared by repository and workspace reads;
keep archived Git-blob behavior unchanged. Open via session.OpenRegularFile
and read via ReadSourcePreview, preserving 512 KiB/12,000-line/UTF-8 limits.
Allow current bytes and newly staged regular files. Do not add directory listings,
downloads, host-wide roots or mount/hardlink defenses against the trusted local
operator. Remote paths remain untrusted; confinement, tracked-file membership,
special-file and symlink rejection protect that boundary.

## Viewer

Reuse the source-file page and CodeMirror editor. Add a page-provided API URL
for shared files, retain the existing slug-derived API as the fallback for
existing session pages, and label source=workspace as Current workspace.
Make the template's session navigation optional and allow a valid shared viewer
without .Session. Invalid links render the existing explanatory unavailable
page; missing/untracked files return a bounded 404 API error. Preserve the
existing missing-line, clipboard, binary and limited-preview behavior. The
portal already serves HTML/static assets with Cache-Control: no-store; verify
this remains true so new markup and API selection cannot use stale modules.

## Compatibility and rollout

No schema, persisted state, package policy, CLI or App Server changes. New source
metadata appears only on the new endpoint. Existing viewer pages and browser
modules remain compatible. No vpsAdminOS nodes or guests need coordinated
updates. Keep the installed extension/Codex/sibling inputs fixed when composing
the published runtime. Use the configuration dev-workspace channel/devWorkspace
role for the same exact runtime, verify the deployment contract, build and deploy
aitherdev from its feature branch with dry activation first, then select the
workspace user-profile package. Never bypass busy-session, lifecycle-journal or
cluster-adoption refusals; await the normal supported idle state or report an
external blocker. Forward-only corrective packages are the recovery path.

## Acceptance and checks

- The exact absolute lifecycle.md:93 link rewrites and old URLs redirect.
- Shared AGENTS/docs/scripts/notes work only for tracked regular files.
- Session paths retain their original reader and never work through the shared
  endpoint. Repositories and .git stay excluded.
- Encoded names, literal escaped colons and all supported line references survive.
- Invalid/duplicate queries, traversal, untracked files, symlinks/FIFOs, missing
  files and Git-root mismatch refuse promptly.
- The browser chooses the correct API, highlights/copies the chosen line, shows
  binary/size/missing-line notices, and leaves session viewer contracts intact.

Quick checks: focused source-file Go tests, source_files_browser_test.cjs,
JavaScript syntax, git diff --check, and downstream identity checks. Unit test
fixtures must use generic names because dev-workspace's generic-source check
rejects site-specific identifiers. Run final committed whole-branch review with
general, architecture, scope and risk lanes before packaged tests and host builds.
Long checks and CI use fresh catalog-resolved Luna/low utilities. Live validation
uses the configured private CA and existing operator credentials privately,
records only public status/path/content summaries, and proves line 93 is present.
