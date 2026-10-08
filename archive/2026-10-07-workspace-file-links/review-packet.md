# Independent final review: shared workspace file links

Requested outcome: the portal must open shared Git-tracked workspace file links,
including the previously failing lifecycle.md:93 reference, through its existing
read-only source viewer. Existing copied absolute URLs must redirect. The user
selected tracked shared files, then requested implementation and aitherdev
deployment through vpsfree-cz-configuration. No default-branch merge is approved.

## Scope and complete branches

Initiative: 2026-10-07-workspace-file-links, workspace root
/home/aither/workspace/ai/vpsfree.cz. Read plan.md, design.md, state.md,
branch-inventory.md and heads.json in this directory. Each registered feature
branch is named 2026-10-07-workspace-file-links, with its dedicated worktree under
worktrees/<slug>/<project>. The inventory supplies the exact base/head and every
commit. dev-workspace-final.diff, workspace-final.diff and
vpsfree-cz-configuration-final.diff are the corresponding complete final diffs.
Inspect Git history and current code rather than relying only on these summaries.

- Runtime e3315a483f3d3536d492ecbe40f2655449cf630f to
  9e8e6e87a5a4844d4639ddf4008de483d1897f4c: three focused commits, the viewer,
  the lifecycle prerequisite and its stable archived test fixture. Viewer tests and explanation accompany its read
  boundary; the small extraction reuses existing tracked-file reads. The second
  commit corrects receipt contention discovered during packaged verification.
- Workspace 48a0d980c24a7e725b40c8854c8e992935639afe to
  70035dfe565058054e30efe2562c655c80dd183c: one runtime-selection commit.
- Configuration 6f6aff9029cd57e1a0f9201356f7fdc9f6480671 to
  5447020fccf99705e65a907cfe6e80684a5a1577: one generated confctl pin commit.

There are no migrations, schema changes or seeds. Initial published runtime/pins
were used for verification but never deployed, merged or released. Superseded
downstream pins were consolidated. No superseded implementations or fixups
remain. All three feature heads are
committed and published; final-head longer verification has not started.

## Acceptance and limits

The new /workspace-files page and /api/workspace/file API support tracked regular
files at the configured workspace Git root. source=workspace appears only on
the new API. Paths under work/, archive/, worktrees/ and repos/ stay outside
this reader; existing session readers retain their rules. Traversal, Git
metadata, untracked files, symlinks and special files must fail. Preserve line
suffixes/escaping and existing preview limits. Show current working contents,
including newly staged files and uncommitted edits. Existing session pages and
archived sources must remain compatible.

Non-goals: host-wide file serving, directory browsing, rendered documentation,
downloads, historical shared-file snapshots, changes to codex-web/extension
sources/KB content/nginx routes, new persistent formats, and default-branch
integration. The local operator is trusted to administer the host. Evaluate
remote input validation, ordinary mistakes and concurrent operations; do not
invent defenses against a compromised operator's mounts or hardlinks.

## Ownership, consumers and documentation

dev-workspace owns workspace-aware Markdown rewriting and file access. It
consumes codex-web's generic conversation provider and already supplies its
presentTranscript hook. The shared mapper applies to conversations and artifact
Markdown. The existing source viewer is the API consumer; new page data chooses
its API while the session slug remains the compatible fallback. Source previews
and confined regular-file opening are existing dev-workspace abstractions.

The workspace flake consumes the extension, which consumes dev-workspace; its
direct nested runtime input preserves the extension at
0ff827df13e82dfab4b536ff29979280f264e8f5. Configuration devWorkspace selects the
same runtime through its existing dev-workspace channel. Only those exact runtime
nodes changed, preserving all sibling nodes and follows edges. No dependency
direction or Codex/App Server revision changes.

Runtime docs/workspace-portal.md describes the new routes, source metadata,
current shared contents and namespace exclusions. README already links that
guide. Technical rationale and verification constraints are in design.md and
the plan; the feature's supported contract remains in its owning project.
Individual rollout evidence will live in rollout.md, not the project guide.
The main lead applied the user-facing writing skill to the final English copy.

## Verification and rollout

Quick checks passed with pinned Nix tools: focused Go source-file tests in web
and compiled repository packages (2.125 seconds), source_files_browser_test.cjs
for both APIs and shared line 93, JavaScript syntax, and git diff --check.
Tests cover the representative doc path, AGENTS/scripts/notes, encoded names,
line references, structural mapping without filesystem reads, old redirects,
shared page without a session, exact Git root, current staged/unstaged bytes,
missing/untracked files, reserved session paths, .git, symlinks including parent
components, FIFO rejection, binary/size limits, duplicate/unknown queries, and
existing active/archived source behavior. The deployment contract passed with
matching runtime identities. Configuration hooks passed; generated confctl
message width warning is retained under the explicit local policy exception.

After accepted review, fresh Luna/low utilities run packaged runtime/composed
checks, CI and the scoped aitherdev build. The parent deploys the configuration
feature with dry activation first, then the workspace user-profile package.
Do not bypass lifecycle journals, busy-session or cluster-adoption refusals.
The installed package remains forward-only: retry the same generation or use
a newer corrective package. No node/guest coordinated rollout or persisted
conversion is needed. Existing browser routes continue working; HTML/static
responses use no-store, and the new page/API must be served by the new generation.

## Reviewer policy and requested lanes

Overall risk: high, because access to shared workspace files expands a remote
read boundary and the deliverable has cross-project deployment ordering.
Review general, architecture/repetition, scope/proportionality and
risk/compatibility lanes. Read each reference under mandatory-change-review.
Explicitly conclude on whole-branch history and migration lineage.

The live same-session roster is null. Use the mandatory standalone fallback,
lexicographically first review-purpose role (reviewer) from the installed
default development team (delegated), model gpt-6.1-sol, effort xhigh. Catalog:
3343a06cbc8d3c181df52770086fb807894f9990132bb0792048e0ddabb764f8. The matching
native behavior is share/dev-workspace/agent-teams/delegated/reviewer-xhigh.toml.
This temporary reviewer does not change the roster. Remain read-only; do the
review directly without nested agents. Return findings by severity with concrete
file/line and commit evidence, or clearly state no findings and any test gaps.

## Required final revision review after verification-driven correction

The previous final review passed the viewer. The old packaged suite then failed
in the unchanged delete-journal companion to the baseline archive race. Runtime
8f0f40a0 is a separate coherent prerequisite fix in operation_state.go: CAS
acceptance returns a boolean; display refresh ignores a lost CAS as before,
while mutation readers repeat fresh receipt/journal proof within their existing
15-second context and generation lock. The response is the accepted proposal,
not an independently recopied receipt. Keep all identity, persistence and
missing-record revision protections. Tests explicitly require rejected stale
CAS proposals; all archive/delete replacement and CAS cases passed at 300
repetitions (34.758 seconds), lifecycle-fix-quick.log. Docs describe the invariant.

Read the updated lead design brief and inventory. Review the final combined
branches, especially the additional lifecycle design, across all four lanes.
This is a related real new review turn using the same independent reviewer,
with unchanged model/effort. Reaffirm whole-branch history and no migrations.
The source viewer is unchanged from the previous reviewed commit. Both final
pins match 8f0f40a0; sibling nodes remain unchanged and the deployment contract
passed again. Configuration consolidated its generated final pin message
with both upstream commits; hook results passed. No unreviewed long final-head
checks or deployment have started. The old composed check was cancelled as
superseded and has no surviving operation. The first host build stopped at an
EOF confirmation without building; use confctl build --yes for the final run.
Original CI rerun was denied by token permissions; a new automatic CI run
37585421799 now targets the corrected runtime.

## Last test-only revision

Runtime9e8e6e8 stabilizes the existing archived observation test's updatedAt
fixture by capturing it once. Production code remains exactly as previously
reviewed8f0f40a0. The otherwise unchanged mock generated time.Now().Unix() on
every read; crossing a second boundary correctly fails archived metadata
equality proof. Clean baseline reproduces the original fixture failure at500
repetitions in5.165s; corrected fixture passed500 repetitions in5.120s. Evidence
archived-fixture-baseline.log and archived-fixture-quick.log. No production
metadata checks or queue assertions were weakened.

Review this committed narrow test correction in the general lane, final matching
pin provenance, and the complete final history/inventory. Preserve conclusions
from the previous four-lane review for unchanged implementation, architecture,
scope and production risk. Source has three focused coherent commits and the
downstream superseded pins are consolidated. The final deployment contract
passes runtime9e8e6e8 with unchanged siblings. No migrations or formats.

CI37585421799 and host build passed at the prior reviewed runtime8f0f40a0;
local runtime failed the changing timestamp fixture and old composed run was
cancelled as superseded. Current automatic CI37586905151 selects9e8e6e8. New
long local checks and deployment will start after this narrow final review.
