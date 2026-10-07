# Shared workspace file links

Implement the accepted portal file-link plan. The live portal returns 404 for
`/home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/lifecycle.md:93`
because its mapper only handles session worktrees and published artifacts.
The user selected all Git-tracked shared workspace files and directed
implementation, including aitherdev deployment through vpsfree-cz-configuration.

## Components and readers

- dev-workspace owns shared-path rewriting, redirects, bounded source reads,
  viewer UI, tests and the lasting explanation in docs/workspace-portal.md.
- This coordination workspace selects the published runtime through its existing
  nested dev-workspace flake input, preserving the extension and sibling inputs.
- vpsfree-cz-configuration selects that same runtime through the dev-workspace
  channel/devWorkspace role and deploys cz.vpsfree/machines/aitherdev.
- codex-web, the extension source, nginx routes and KB content need no changes.
  Readers are workspace operators and developers maintaining the portal.

## Behavior

Add /workspace-files?path=<relative-path>#L<line> and the read-only
GET /api/workspace/file?path=<relative-path> API. Return the existing source
preview structure with source=workspace. Preserve :line, :line:column and #Lline
references, redirects for previously copied absolute paths, and all existing
session interfaces. Reuse the viewer and confinement helpers. Rendering maps
paths without filesystem reads; opening a file verifies the workspace Git root,
literal tracked regular-file membership and safe confinement.

Shared files include documentation, root AGENTS.md, scripts and notes. Exclude
work/, archive/, worktrees/, repos/ and Git metadata from this new reader; session
files retain their existing authorization. Do not serve arbitrary host files,
untracked files, symlinks or special files. Show current working contents,
including uncommitted edits, with existing preview limits and line selection.

## Compatibility, deployment and recovery

No persisted formats, schemas, migrations, seeds, generated clients, CLI,
App Server protocol, NixOS module options or runtime transition policies change.
New routes and source=workspace are additive; existing session payloads remain
unchanged. Old portal generations cannot open new shared-file URLs, but can
still read all retained state. Browser assets and templates must update together
without stale cached modules requesting the wrong API. No coordinated node or
guest updates are required.

After committed changes, quick checks and independent final review, run packaged
verification and build aitherdev. Verify matching final runtime identities with
bin/check-dev-workspace-deployment. Deploy aitherdev from the configuration
feature worktree using confctl with dry activation first, then activate the
composed application from the workspace feature worktree through the stable
workspace-host user-profile command. Preserve all existing cluster ownership
and lifecycle refusals. Recovery follows forward-only package transitions:
retry the same candidate or publish a newer corrective package; do not force
an older profile or discard another session's state.

Publish feature branches. Implementation and deployment authorization does not
authorize integrating any feature branch into master. Keep the initiative active
after deployment, ready and awaiting explicit repository/target merge direction.

## Verification

Quick checks cover shared/source-file Go tests, JavaScript contracts and syntax,
diff whitespace, configuration evaluation and matching runtime pins. Cases
include the exact reported link, shared docs/AGENTS/scripts/notes, suffixes and
encoded names, old redirects, no-Git/mismatched roots, rejected namespaces,
untracked files, symlinks, special files, traversal and malformed queries.
Verify browser API selection, line highlighting, missing-line and size/binary
notices, copying links, and unchanged active/archived session behavior.

Run independent whole-branch review using mandatory-change-review before long
packaged checks and host builds. Long verification uses fresh policy watchers.
Final live evidence must show the original URL redirecting to the viewer and
the API returning the lifecycle document with line 93 selectable.
