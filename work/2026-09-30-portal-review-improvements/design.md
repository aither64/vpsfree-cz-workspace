# Portal review improvements: design and verification brief

Status: completed implementation brief. The lead accepted the repository,
forward-only recovery and separate WebUI backend boundaries. This document
records design and explicitly attributed verification evidence; planned checks
are not claims of execution.
Author: architect0, 2026-09-30.

## Scope, evidence and ownership

The approved plan covers seven changes: GPT-6.1 Sol workspace defaults; atomic
live model/effort editing; retained diff editors and Load all diffs; a GitHub-only
origin-provider boundary; staged and unstaged review including untracked files;
role-derived add-member settings; and the React WebUI alongside the PHP UI in
the vpsAdmin development cluster.

Session identity was verified with `dev-session current` in this tracking
directory. It printed `2026-09-30-portal-review-improvements`; both environment
identity variables were absent and the trusted thread binding matched.
Applicable workspace procedures and repository instructions were read before
designing. Read-only source inspection used these canonical revisions:

- `dev-workspace`: `7c133c562ac51076c1f45af46e180f8bfbabe836` (`origin/master`).
- `vpsfree-dev-workspace`: inspected initially at
  `bd961682cecb0b3b2bf729a53d2e08bda3d48eb2`; the registered implementation
  worktree was then fast-forwarded to merged `origin/master`
  `6a0a2eb873e7cb376092c74bdf82fc2c51c349da` before application edits.
- `vpsadmin-webui`: approved dependency
  `534caa83a5f97d2b40b4a126886649b14dc9e8d3`, including its AGENTS.md,
  packaging/service guides, module, and BFF credential contract.
- `vpsadmin`: the registered read-only worktree is now
  `5c76e3290481b297dcd0baa76d246133f0353d8f`. Its OAuth, schema and frontend
  contracts match the initially inspected `7045c81b`; packaged HaveAPI remains
  0.29.8. Current `codex-web` supplied protocol context. Neither repository is
  an application-edit target in this design.

At the architect's initial inspection this session had no project worktrees.
The lead subsequently created and registered the following from current remote
defaults before accepting the brief. All paths below are relative to the
corresponding repository unless stated.

| Repository/worktree under `worktrees/2026-09-30-portal-review-improvements/` | Owned changes |
| --- | --- |
| `dev-workspace` | `portal/internal/web/static/{app.js,repository-review.js,repository-review.css,style.css}`, `templates/{session.html,details.html}`, `web/{server.go,member_conversation.go,repository_review.go,repository_review_batch.go,repository_review_cache.go}`, `repository/{review.go,review_diff.go,status.go}`, new origin/snapshot helpers, `teamruntime/runtime.go`, CLI adapter/tests if needed, README and `docs/workspace-portal.md` |
| `vpsfree-dev-workspace` | `dev-clusters/vpsadmin/{flake.nix,bin/devcluster,nix/test.nix,README.md}`, `dev-clusters/lib/runtime.sh` links, optional focused WebUI Nix helper, `test/{devcluster_commands_test.rb,devcluster_status_test.rb,devcluster_nix_smoke.rb,fixtures/vpsadmin-config.json}`, runtime input in `flake.{nix,lock}` |
| `workspace` | `config/{agent-teams.nix,vpsadmin-devcluster.json}`, `AGENTS.md`, `docs/agent-teams.md`, matching policy checks in `flake.nix`/`test/`, extension input in `flake.{nix,lock}` |
| `vpsfree-cz-configuration` | Bounded fourth-repository candidate: one CNAME and monotonic SOA serial in `configs/internal-dns/zone.vpsfree.cz.`; shared DNS publication pending exact-target user approval. Existing aitherdev Codex deployment uses its already selected input; no input or system host code changes. |

The lead owns plan/state/portal artifacts and implementation assignments; the
implementer owns application changes. This architect edits this document and
the explicitly assigned DNS reconciliation in `plan.md`, plus any separately
assigned coordination prototype. A consequential departure
from these boundaries goes through the lead. No vpsAdmin API/schema, PHP product
behavior, generated clients, Terraform provider, node protocol, system host
code, KB content, or vpsAdminOS change is required. Shared internal DNS publication
has the separate approval boundary below. No coordinated node upgrade is
needed. The reviewed React repository remains an exact dependency; a discovered
defect there requires a separately agreed scope change.

## 1. Retain loaded diffs and load the complete comparison

The current `trimEditors()` destroys both the editor and content when more than
eight records are mounted. Remove that eviction for an open comparison. Its
successful file results and editor instances live until that comparison is
closed/replaced or the page is destroyed. Ordinary repository-card refresh,
scroll, temporary tab hiding, and HEAD polling do not discard them. Layout/file
version changes may replace the affected editor but retain its loaded content.
Collapsing a file may hide its editor without dropping the content; retain the
existing remembered collapse choice for that exact comparison/file identity.

Add **Load all diffs** to the comparison toolbar. It expands all listed files,
including the existing large-diff default collapses, and feeds the existing
bounded file queue: at most two browser requests, four files per request. It
does not start one request per file or bypass the server's four-worker budget.
Already loaded/in-flight files are reused. Show completed/total and failures;
retry only failed files. Binary, submodule and limited previews reach a completed
metadata-only state. Completion means every eligible text preview was loaded
and rendered, with any exceptions visible. Yield browser work between batches.
Navigating to a different comparison cancels work for the old one; late results
cannot populate the new view. Pausing visibility pauses reads and resumes the
queue without losing successful content.

Keep native browser Find. Retention fixes disappearing file editors, but
CodeMirror still virtualizes lines and hides unchanged regions; native Find
cannot be promised to search every line of every source. Loading all diffs does
not change that limitation. No search index, hidden duplicate text, or custom
search UI is in scope. Memory grows with explicitly loaded previews, within
existing per-file and server limits; preserve this deliberate tradeoff in docs.

## 2. Immutable staged/unstaged review

### Meaning and HTTP boundary

Keep the existing branch and commit comparison paths and durable IDs intact.
Repository cards gain separate **Staged changes** and **Unstaged changes**
actions only for verified active worktrees:

- Staged means the current HEAD tree versus the captured index.
- Unstaged means the captured index versus captured tracked working files plus
  non-ignored untracked files. A path changed in both places appears in both
  comparisons with the correct middle/index version.
- Untracked content appears only in unstaged review. Ignored paths are never
  traversed or included. No staging/discard/commit operation is added.

Extend `POST /api/sessions/<slug>/repository-comparison?repository=<opaque-id>`
with a discriminated request `{kind:"staged"}` or `{kind:"unstaged"}`.
The current `{snapshot,commit?}` committed-comparison request remains valid;
reject mixed selectors and unknown fields. The server resolves the registration
and worktree, never a browser-provided filesystem path/ref. Snapshot creation
requires the existing exact-origin mutation check and bounded request body.
`GET repository-comparison?...&snapshot=<id>` restores an uncommitted snapshot
only while it remains in this process. Existing `repository-file` and
`repository-files` consume its token and allowed file IDs through the same
authorization boundary.

Add response fields `kind`, `capturedAt`, `ephemeral:true` and `sourceHead` for
these views. Keep opaque snapshot/file tokens; do not present synthetic object
IDs as pushed commits or create fake commit messages. Render labels HEAD/Index
for staged and Index/Working tree for unstaged. Use distinct URL state for an
ephemeral snapshot; never store it as a durable `review` ID. A reload may reopen
the same snapshot while retained, but restart/eviction returns a clear 409
expired response with an explicit recapture action. Never silently recapture a
different worktree version behind an old file/line link.

An unstaged response also carries an additive `unverifiedSubmodules` metadata
list for captured index gitlinks. Each entry contains the validated path and
frozen index gitlink mode/object ID. These entries are outside `ReviewFile`,
changed-file totals and line statistics: they do not assert a working-tree
change. Display "working state not inspected", without claiming changed,
dirty or clean state. Keep the notice visible even when there are no ordinary
changed files. The list is immutable with its snapshot and bounded by the
existing admission/response limits; overflow fails explicitly without silently
omitting entries or increasing snapshot quotas. Older readers may ignore this
additive metadata. Staged and committed gitlink diffs retain their current
behavior.

Lightweight status may report staged/unstaged/untracked counts. Do not capture
file contents during the 15-second HEAD poll or perform a new all-workspace
scan. Refresh explicitly creates a new snapshot. Keep an open comparison fixed
even when the index, worktree or HEAD changes. Archived sessions expose only
their existing committed views, and authorization changes invalidate access to
old worktree snapshots.

### Capture algorithm and storage boundary

Introduce a focused reader (for example `repository/review_worktree.go`) and
process-owned snapshot store (for example `web/repository_worktree.go`). Keep
the committed reader's canonical Git-object path separate from the mutable
capture path. Extend resolved repository identity with a server-derived
worktree path; the current `Directory` points at the canonical common Git dir.

Implementer0 demonstrated that `git ls-files -m`, `git diff-files --name-only`
and `git status --porcelain` can invoke a configured hostile clean filter even
with global attributes and fsmonitor disabled. The lead accepted the following
read-only index-stat and filesystem discovery approach on that evidence. Do
not use those content-comparing Git commands for snapshot candidate discovery
or revalidation; disabling global attributes alone does not prevent repository
attributes from selecting a filter.

1. Revalidate canonical workspace, registered branch, common-dir and exact
   worktree identity using the existing `ReviewReader.Resolve` rules. Record
   HEAD and read index-stage entries and index stat records using read-only
   `ls-files --stage`/`ls-files --debug`, with NUL-delimited path records. Use
   `ls-files --others --exclude-standard -z` for untracked enumeration. Never
   parse paths by lines or interpolate them into shell commands. Discover
   tracked candidates using no-follow `lstat` comparisons against index stat
   records. Only stat-mismatched or racy tracked paths are eligible for content
   opens; untracked paths are candidates without an index baseline. Treat
   timestamp ambiguity and insufficient stat evidence conservatively as racy,
   never as proof that a path is unchanged.
2. Capture the index's stage-0 object/mode mapping and candidate paths before
   reading working files. Detect conflicted/unmerged stages explicitly; refuse
   the uncommitted capture with a resolve-conflicts message instead of choosing
   one stage. Keep committed comparisons usable. Intent-to-add has no staged
   content and contributes its working bytes to unstaged review. Sparse-index,
   split-index and skip-worktree cases must either be decoded by read-only Git
   plumbing or return a precise unsupported-state error; never repair an index.
3. Freeze every admitted before/after preview and file metadata before returning
   the comparison. HEAD/index sides come from exact blob IDs. Working files use
   bounded safe opens below the verified root; compare file identity, type,
   size and timestamps before/after the read. Symlinks display the link target
   itself and are never followed. Reject FIFO/device/socket reads. A directory
   symlink cannot authorize traversal. For an unstaged capture, freeze index
   gitlinks in `unverifiedSubmodules` without inspecting their working state.
   Dirty submodule state cannot be established safely without traversal; do
   not recurse, invoke submodule status, or reject unrelated file review with
   a blanket 422 merely because a gitlink exists. A gitlink's presence or stat
   information alone does not establish that its working state changed.
4. Compute exact diff ranges/statistics only from fully captured, compared
   content. The implementer may reuse Git's existing immutable-blob diff by
   writing admitted data with
   `hash-object --no-filters` to a private temporary object database. Any Git
   index used for tree synthesis must also be private. Set trusted Git paths
   explicitly after stripping inherited `GIT_*`; disable hooks, external diff,
   textconv, clean/smudge filters, fsmonitor, lazy fetch and optional locks. Do
   not run `git add` against real working files. An alternative bounded
   `--no-index` diff may use only the private captured files. It must preserve
   the current Myers/statistics contract and treat diff exit status 1 correctly.
5. Re-read HEAD, index-stage/stat records and relevant no-follow filesystem
   identities using the same filter-safe discovery path. Retry capture at most
   twice on detected concurrent changes, then return a retryable conflict.
   This is a stable bounded observation, not a
   filesystem-wide atomic transaction; no lock of the developer's real index
   or promise about undetectable concurrent ABA writes is made. After publication,
   content and counts come exclusively from the snapshot, never live paths.

Keep the current 512 KiB/12,000-line per-version preview limit and 5,000-file
comparison limit. Oversized/binary/special content retains frozen metadata and
an explicit limited/unavailable preview. An oversized candidate may be retained
as metadata-only without reading or hashing its full content. Show an explicit
"content not compared" warning: stat mismatch identifies a candidate, not proof
of a content difference. Do not claim exact content equality, an exact changed
line count, or zero changed lines for it. Never perform unbounded hashing to
resolve that uncertainty, or read a large live file on a later file request.
Any admitted partial preview is frozen during capture and cannot establish
full-file statistics. Unknown line totals must be shown as unavailable, not
silently counted as zero or binary; aggregate statistics must also preserve
that limitation. Extend stats metadata if necessary to distinguish limited
files from binary files. Preserve rename paths, mode changes, deletions, empty
files and missing final newlines. Rename detection uses captured data and a
bounded Git limit; a delete/add representation is acceptable when a rename
cannot be established, not a fabricated rename.

Bound transient storage: initially at most 32 snapshots, 64 MiB of admitted raw
preview bytes per snapshot and 256 MiB process-wide, in addition to existing
response, timeout and cache bounds. Fail an over-budget capture explicitly;
do not silently omit paths. Evict least-recently-used snapshots with no current
read leases. Include snapshot identity/kind in cache keys and release their
private objects only after in-flight readers finish. Private directories/files
use 0700/0600 and live outside the worktree and tracking tree. Prefer runtime
temporary storage; orderly shutdown releases only that process's resources.
After a crash, inaccessible leftovers may be handled by the established runtime
temporary-directory mechanism, never by broad session cleanup.

The real index bytes, worktree, refs, object database, config and reflogs remain
unchanged. Temporary synthetic trees/blobs never enter canonical repositories,
`portal.yml`, saved-comparison records, archive proofs or Git history. This
feature must not weaken `Source()`'s tracked-regular-file restrictions; untracked
review access is confined to an authorized snapshot and its enumerated files.

## 3. Repository origin provider

Add a small provider contract, for example `repository/origin.go` plus
`origin_github.go`, and move GitHub transport/link rules out of the generic
review/status code. A resolved origin has `provider:"github"`, validated
`repository:"owner/name"`, a display label and provider-produced HTTPS links.
The contract covers repository/branch/commit/compare/workflow URLs, remote head
and default-branch lookup, head comparison and workflows for the exact head.
The GitHub implementation keeps the current `gh` invocation, error handling,
timeouts and four-job enrichment limit. Inject the transport/provider in tests;
do not build a configurable plugin loader or second provider.

`Status` and `ReviewRepository` carry this neutral representation; templates use
origin label/error/URLs rather than hard-coded GitHub presentation. Local commit
history and local diffs must remain available when remote origin enrichment
fails or no origin is recorded. Provider URLs are built from validated identity
and escaped ref/path segments, never accepted as an arbitrary browser URL.
Only GitHub is recognized; unsupported origins cannot trigger arbitrary network
requests. Preserve exact local/remote head comparison and workflow-head filtering.

Compatibility boundary: `session.Repository.GitHub`, the persisted `github`
manifest field, CLI registration flags and strict schema-1/2 validators remain
unchanged. Convert that field at the repository boundary. Keep existing JSON
`github`, `githubError`, and link fields as aliases where already public; add
neutral fields rather than break old clients. Do not add an `origin` YAML key,
bump manifest schema, rewrite old manifests, or change
`repositoryReviewScope()`'s canonical identity serialization: that would break
previously saved review IDs. A future provider needs a separate persistence
migration decision. Archived GitHub links retain current behavior.

## 4. Atomic live Codex model and reasoning draft

Implement in `app.js` and `templates/session.html` for both lead and member
conversation views. Replace the two change-triggered saves with one explicit
**Apply** action and a **Cancel** action for the pair. Maintain distinct state:
confirmed server pair, editable draft pair, dirty flag, saving state and write
generation. A model change preserves the draft effort if supported; otherwise
selects that model's catalog default and visibly leaves the pair unsaved.
Never submit an unsupported/empty pair or choose another model silently.

Polling updates the confirmed pair, activity and active-turn state, but cannot
overwrite a dirty/saving draft or re-enable controls while a save is in flight.
The common `applyCurrentSettings()` path must explicitly delegate these live
controls to the draft controller rather than applying global defaults. Stamp
settings-bearing reads at request start. Ignore their settings fields if they
predate a completed write; still accept unrelated transcript data. A fresh
post-success read may update a clean draft, including a later native-client
change. Unknown/missing settings in a partial page response are not an empty
model or effort.

Apply captures the pair once and makes exactly one existing
`client.settings(model,effort)` call. Successful response installs the returned
pair, clears the dirty flag and refreshes from the server. On failure retain the
draft and show the error; do not falsely restore or report unsaved server state.
A timeout can have an uncertain server outcome: re-read and reconcile the exact
pair before retry, and never send a compensating settings update automatically.
Cancel restores the latest confirmed pair without a write. Draft edits can be
kept in bounded `sessionStorage` keyed by workspace/session/exact conversation
identity to survive page reload; discard a stored draft only after success or
explicit Cancel. Persist only selections, never an in-flight write claim.

Keep current active-turn restrictions: an active/unknown turn disables Apply
and live edits; becoming active preserves an already dirty draft for later.
While a save is pending, serialize or disable Send/start-queue/mode changes that
would race the pair. Preserve the collaboration mode and thread policy; changing
the pair must not reset instructions, access or session identity. Authorization,
mutation lock, supported model/effort validation and the existing idle gate are
server-enforced, not only browser controls.

The inspected `codex-web` handler already requires the explicit pair and the
client sends one `thread/settings/update` RPC under a per-thread lock, awaiting
the settings notification. No new protocol shape or Codex version is proposed.
Verify persistence through a real subsequent read, reconnect and next turn on
the pinned server. If the response/read differs, report the protocol defect to
the lead before expanding into `codex-web`. Member conversation writes must
continue to retain the accepted pair in the roster; a roster-write failure
after an App Server write is an explicit reconciliation error, not a success.

## 5. Role-based member defaults and GPT-6.1 Sol policy

Expose a single server-side role-settings resolver using the same `catalogRole`
policy used to create members. Resolve the current roster preset first, then
installed default development team, then installed default team. Preserve the
existing architect-to-designer alias and custom role names/purposes. The current
last-resort scan across other presets must reject disagreement in model/effort
as well as instructions/purpose/access; iteration order cannot choose a default.
Return resolved role model/effort together with policy provenance for rendering.
The add-member form uses those values when initialized or its role changes;
ordinary status/catalog refresh must preserve an explicit user override. An
unavailable required model leaves the selection visibly invalid and Add disabled.

For team `action:"add"`, model and reasoning effort are an optional pair:

| Request | Result |
| --- | --- |
| Both omitted | Resolve and validate the selected role's pair before allocating a member/thread |
| Both nonempty | Validate and preserve that explicit pair |
| One omitted, one empty, null, or an invalid pair | 400/validation error; no member, project or thread mutation |

Keep presence information during decoding so malformed partial requests cannot
become a default request by trimming. Existing explicit clients remain valid.
`configure` still requires the explicit pair. Unmanaged installs without a
catalog still require an explicit pair; do not invent role-specific models.
Both HTTP and CLI add paths use the same resolution rule. Resolve inside the
team operation's serialized decision boundary, validate against the live model
catalog before writing the creating roster, and save the actual pair once.
Retries of a creating member use that saved pair even if the package/catalog
changes. Do not rewrite existing ready or creating rosters, saved instructions,
access, lead settings or reviewer effort.

The requested Sol migration belongs in the consuming workspace:
`config/agent-teams.nix` lead/implementer/reviewer defaults become exactly
`gpt-6.1-sol`. Keep all existing reasoning effort levels, Astra architect and
Luna watcher settings. Update generated-catalog assertions in `flake.nix`, the
workspace role documentation/AGENTS wording and relevant instruction tests.
Do not globally replace model names in retained sessions or historical records,
and do not change generic unmanaged defaults without lead scope approval.
Before deployment, verify the account's `model/list` exposes the exact requested
model and required efforts; unavailable models are a visible deployment blocker,
not grounds for silently substituting GPT-6 Sol/Astra. No roster schema change.

## 6. Side-by-side development WebUI

### Inputs, source overrides and placement

Add `vpsadminWebui` to the packaged vpsAdmin cluster flake, pinned to reviewed
`534caa83a5f97d2b40b4a126886649b14dc9e8d3`; follow cluster `nixpkgs` and the
selected `vpsadmin` input. Its independent `frontend` and `bff` packages plus
`nixosModules.default` are the integration contract. The existing PHP package
`pkgs.vpsadmin-webui` is unrelated and must not be substituted for these outputs.

The runtime launcher requires this session's `vpsadmin` worktree and overrides
the cluster input with that path. The lead registered the clean selected API
head `5c76e329`; it descends from the WebUI's reviewed API input `a65a4df`.
The extension's packaged smoke input, `devcluster-vpsadmin` at `8d0ccafd`, is
older and lacks the OAuth default/start fields and password-recovery frontend
route. The enabled-WebUI smoke input must be `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`
or a verified compatible descendant; select the inspected `5c76e329` here.
Align that input before accepting an enabled-WebUI smoke result. The smoke
command supplies its own locked API path;
registering a runtime worktree does not update it. Retain disabled legacy config
coverage, but do not add missing-column guards or claim the old API supports
the new service. No new API migration is introduced by this initiative.

When this session owns `worktrees/<slug>/vpsadmin-webui`, use it through the
existing optional-worktree resolution and `--override-input vpsadminWebui`.
Keep that input's vpsadmin follow mapping aligned with the selected cluster API.
Record source revision/dirty provenance in the normal nonsecret build/status
information. Both packages must have matching metadata. This UI is built into
immutable packages; local source changes require `update <slug> services`, not
live npm/Vite or the PHP symlink mechanism. No npm install on the running VM.

Use a separate `containers.newadmin` on the existing services VM, with
`privateNetwork = false`, matching the current legacy container pattern. Import
the reviewed module there. Set its private nginx listener to
`127.0.0.1:18082` and BFF to `127.0.0.1:3001`, verifying no collision in rendered
configuration. The services VM's public nginx proxies TLS traffic to 18082.
This avoids merging the module's private vhost with the edge vhost under the
same hostname. No private listener is opened on an external interface.

Workspace configuration supplies `domains.newadmin =
"newadmin.aitherdev.int.vpsfree.cz"` and an explicit WebUI enable setting.
The extension uses generic fixture names. Existing external configs without
this domain/enable setting continue to evaluate with the new service disabled;
enabled configs require a distinct valid domain. Add the domain to generated
hosts/DNS and certificate SANs, reusing the existing CA-preserving leaf renewal.
Add a distinct React WebUI service link alongside the legacy Web UI link in
status/portal output; it uses the same seeded user accounts, never OAuth secrets.

### Atomic build provenance, status and failure recovery

Review correction at clean extension head `9e7ebebf611bd080fbfc8fca4253e5eab4cb9939`:
`dev-clusters/vpsadmin/bin/devcluster:785-807` first lets Nix advance
`result-config`, then writes or removes `webui-source.json`. A failure in that
second publication aborts start/update but leaves the selected build and its
status provenance inconsistent. The separate sidecar must stop being an
authority. No compensating two-file rollback or new lifecycle journal is needed.

Use the immutable JSON selected by `result-config` as the sole build/provenance
record. `dev-clusters/vpsadmin/flake.nix:130-133` already exports
`clusterConfig.json`; `nix/test.nix:1864-1867` already emits source revision and
dirty labels. In the selected smoke input `vpsadminos` at `15802517`,
`tests/make-test.nix:331-352` serializes `machines` and top-level `labels`
together with `writeText`. The shared runner reads `machines` from that JSON
(`dev-clusters/lib/devcluster_runner.rb:150-158`), while update reads its
`.machines[<name>].toplevel` (`bin/devcluster:1371-1386`). Keep that output and
runner interface intact; add source kind to the existing label object:

```json
{
  "labels": {
    "webuiSourceRevision": "<40 lowercase hexadecimal characters>",
    "webuiSourceDirty": "false",
    "webuiSourceKind": "pinned"
  }
}
```

The permitted dirty strings are exactly `"true"` and `"false"`; source kind is
exactly `"pinned"` or `"worktree"`. Emit all three labels only for an enabled
WebUI and force their validation during Nix evaluation before output
publication. Disabled builds omit all three. Preserve the runner's string-label
convention. Labels contain no credentials or mutable metadata-file paths.

The launcher supplies kind from its actual source selection alongside the
existing revision/dirty inputs, using
`VPSADMIN_DEVCLUSTER_VPSADMIN_WEBUI_SOURCE_KIND` and the flake/module argument
`vpsadminWebuiSourceKind`. Set it explicitly on every build (`worktree` for the
same-session override, otherwise `pinned`); do not inherit a stale caller value
or infer kind from a revision string. Explicit smoke path overrides also provide
their intended source kind. Failed source inspection must fail the preparation
instead of reporting clean state. Preserve the observed revision/dirty evidence
in the output; status must not recompute it from the now-current worktree.
The immutable output path identifies the built configuration. A dirty boolean
is diagnostic evidence, not a replacement for artifact identity or a claim
that a mutable worktree cannot change during a build.

Remove post-build creation, replacement and removal of `webui-source.json`.
Existing sidecars are ignored, including malformed or stale files, and are not
deleted as a prerequisite to building, status or activation. Keep the existing
single-output `nix build --out-link <result-config>` publication and Nix-managed
GC-root behavior; do not rename a temporary Nix root into the live root or
invent a second root/manifest transaction. Any selected-result validation after
the build is read-only and must abort start/update before runner launch, copy
or activation when it fails. It must never substitute an older build as if the
requested build succeeded.

For `status --json`, resolve `result-config` once and read that immutable target
once. Validate and translate its three string labels into the existing schema-2
`webuiSource: {revision, dirty, kind}`, with `dirty` a JSON boolean. Never combine
labels from repeated resolutions or supplement them from a sidecar, current
Git state, environment, or desired `config.json`. No root yet means source
metadata is unavailable and the optional field is omitted. A legacy result
with no WebUI labels also omits it. A present but unreadable/invalid result,
partial label set, malformed revision/dirty value or unknown kind fails source
reporting clearly; do not manufacture a valid provenance object. A legacy
two-label WebUI result needs a normal rebuild to obtain kind, not a guess from
its potentially stale sidecar.

`webuiSource` describes the selected built configuration, not proof of the
currently activated services VM. Derive its presence from result labels, not
the mutable desired enable flag: changing that flag after a build cannot change
the source of the selected result. Disabled legacy/new builds still emit no
source field. Existing service links/accounts retain their configuration-based
contract; a link and a running runner do not prove the new UI was activated.
No portal schema bump, VM protocol, database or persistent cluster-identity
migration is required.

Publication and deployment have distinct failure boundaries:

| Failure point | Selected result and required behavior |
| --- | --- |
| Credential/source preparation, evaluation or build fails before link publication | Preserve the previous result, or no result on first build; return failure and perform no runner/copy/activation action. |
| Process interruption during result-link replacement | The result names a complete old or new immutable JSON, never new machines with old sidecar provenance. Resolve and validate it on retry; do not infer deployment from its presence. |
| Link published, then Nix GC-root registration, read-only result validation or a later start/update step fails | A complete new result may remain selected. Return failure, report the failed phase, and stop before subsequent deployment actions. Do not promise restoration of the previous link. Retry the normal build to establish successful rooting/validation before using the selected result. |
| Copy/activation/refresh fails after build success | Keep selected build provenance truthful; earlier machine updates may have completed. Preserve the existing partial-update reporting and verify actual VM state before retrying. |
| Status read/parse fails | Return an explicit status error without fabricated or sidecar-derived provenance; status does not mutate the result or trigger a build. |

This distinction follows the installed Nix 2.34.8 implementation:
[`IndirectRootStore::makeSymlink` and `addPermRoot`](https://github.com/NixOS/nix/blob/2.34.8/src/libstore/indirect-root-store.cc#L4-L38)
replace the out-link with a same-directory rename, then register its indirect
root. Consequently even a nonzero Nix return can occur after link replacement.
The guarantee is coherent configuration/provenance and no automatic deployment
after failure, not rollback of every side effect or power-loss durability.

Owning files are `dev-clusters/vpsadmin/bin/devcluster` (source selection,
build path and status parser), `dev-clusters/vpsadmin/flake.nix` (kind input),
`dev-clusters/vpsadmin/nix/test.nix` (validated labels),
`test/{devcluster_commands_test.rb,devcluster_status_test.rb,devcluster_nix_smoke.rb}`
and `dev-clusters/vpsadmin/README.md`. The shared runner and GC-root helper need
no interface change. README recovery must say that failures before publication
retain the prior result, while failures after publication can leave a complete
new build selected without successful activation. Record the selected output
path and failure phase for recovery; retry through the normal helper, retain
credentials/BFF state, and preserve the compatible API/schema. Removing old
sidecars, resetting the cluster or reverting the API is not a recovery step.

Quick fixtures must inject failures after a successful mock build, not only
before Nix changes its out-link. Cover both retained/no-prior-result cases,
start/update, and enabled pinned/worktree/dirty/disabled variants. A mock Nix
that publishes complete new JSON and then returns nonzero must leave status
reading its coherent new labels and perform no runner/copy/activation. Inject
post-build result-read/parser failure and verify the same stop boundary. Traps
for the former sidecar `mktemp`/`jq -n`/`mv`/`rm` paths must prove those writes
are no longer attempted. Stale/malformed sidecars must not affect status.
Also test no-result and no-label legacy cases, partial/invalid labels, explicit
kind, disabled builds, a desired-config edit after building, and link replacement
between status resolution and reading: status returns one complete result or a
clear read failure. No combination may report the new result with old metadata.
Nix smoke evaluation must assert all three labels and their validation, reject
invalid kind/revision/dirty inputs for enabled builds, and retain disabled old
config coverage. Run package/build verification only through the existing
post-review watcher workflow; no long checks or deployment are part of this
design correction.

### Runtime settings, network trust and OAuth

Configure the reviewed module with the HTTPS public origin, cluster API URL and
its supported API version, legacy PHP origin, and these provider endpoints:
`https://<auth-domain>/_auth/oauth2/{authorize,token,revoke}` and
`https://<auth-domain>/oauth2/password-reset`. Callback is exactly
`<public-origin>/oauth/callback`; authorization start is `/oauth/login`.
Use scope `all`, type `web_server`, header `X-HaveAPI-OAuth2-Token`, namespace
`_meta`, and explicit cluster console/frame origins required by the product.
Verify the selected API configuration actually exposes this contract.

The BFF calls the provider with strict TLS validation. Give the container the
cluster CA and set `NODE_EXTRA_CA_CERTS` to that public CA file; never disable
Node TLS verification or select BFF legacy-test mode. The SPA calls the API
directly; the BFF does not proxy it. Selected HaveAPI 0.29.8 already emits
`Access-Control-Allow-Origin: *` and `Access-Control-Allow-Credentials: false`
on Origin-bearing responses and preflight, and registers
`X-HaveAPI-OAuth2-Token` among allowed headers. The SPA uses that token header
with `credentials: 'same-origin'`, so cross-origin API cookies are not sent.
Preserve this existing noncredentialed CORS contract; no exact-origin allowlist
or duplicate edge CORS headers are needed. Verify the actual preflight and API
responses through the cluster proxy, including Content-Type allowance.

The TLS edge overwrites Host, X-Forwarded-Host, X-Forwarded-Proto and
X-Forwarded-For from its own connection, with one forwarding address. Set Host
and X-Forwarded-Host to the configured public authority literally, including
any nondefault port; nginx `$host` drops the port and fails the module's exact
Host check. Set both `nginx.trustedProxyAddresses` and
`nginx.allowedClientAddresses` to `[ "127.0.0.1/32" ]`; trust defaults to empty
and otherwise rejects the edge's forwarding headers. Set X-Real-IP from the
edge socket and clear Forwarded and the module's other untrusted client-IP
headers. Disable duplicated
recommended proxy headers. Preserve the module's static/BFF route ownership,
CSP and no-store/session rules; the edge owns TLS/HSTS. Suppress access and
error logging for `/oauth` and `/oauth/` at the edge as the module does, including
upstream failure paths, so authorization codes do not reach logs. Other paths
retain diagnostics. Validate rendered nginx, not only attribute values.

Bridge mode is the acceptance/deployment path. Local mode currently forwards
host loopback 10443 to guest 443, while guest domain resolution uses the
services IP. Adding 10443 to public URLs does not provide a guest listener at
that port: the BFF cannot reach the same provider origin through that mapping.
The reviewed BFF requires authorize, token, revoke and recovery to share one
origin, so mixing browser 10443 with internal 443 endpoints is rejected.
Local enablement is blocked until a separately agreed routing solution proves
both browser and BFF reachability, exact authority, and callback consistency.
Keep existing local configurations usable with the new UI disabled and reject
an unsupported enabled-local combination clearly. Report any proposed network
scope expansion to the lead before implementation.

### Credentials, seed order and state

Generate a new three-file credential bundle at runtime under the verified,
ignored `.dev-clusters/vpsadmin/clusters/<slug>/webui-credentials/`:
`oauth-client-id`, `oauth-client-secret`, `session-secret`. Use secure random
values meeting the reviewed BFF's minimum 32-byte secret requirements, 0700
directory/0600 files, under existing lifecycle/per-cluster locks. Generate once
through a temporary directory and atomic publication. A partial, malformed or
foreign bundle fails closed; normal restart/update never rotates it. These
values never enter Nix expressions, Nix store sources, environment variables,
argv, config.json, status, tracking or logs. Pass runtime paths as strings only.

Expose the bundle through a services-VM-only runtime mount, not the common mount
set shared with nodes. Copy/load into narrowly readable guest runtime files for
the DB seed and the container's `LoadCredential` paths. Do not make the world
able to traverse credentials to work around UID mappings. The BFF's module
continues to use the dedicated `vpsadmin-webui-bff` account and its private
`/var/lib/vpsadmin-webui/sessions`; retain that state in the new container's
persistent root. Do not point it at PHP's `/var/lib/vpsadmin` tree.

Use a separate runtime OAuth seed service after and requiring database setup,
the existing `vpsadmin-devcluster-seed` service, and credential preparation.
Make `container@newadmin` require and start after this seed. Do not append secret
reads to the shared `devSeed`: it also runs inside initial database setup's
`seedFiles`, before the runtime credential dependency chain. The separate seed
uses the database service's user/group, package, working directory, schema and
RACK_ENV, with `LoadCredential` for runtime client ID/secret access. Failure
blocks the new container without making the PHP/API service depend on this
new seed.

Startup correction assessed at extension `e0f98557`: explicitly set
`containers.newadmin.autoStart = true` inside its existing enabled-only block
in `dev-clusters/vpsadmin/nix/test.nix`. The selected packaged smoke input
`devcluster-vpsadminos` `15802517` uses nixpkgs `21a67dc4`, whose
`nixos/modules/virtualisation/nixos-containers.nix:830-836` defaults this option
to false. Lines 1041 and 1097-1107 connect multi-user to `machines.target` and
add the container's `wantedBy = [ "machines.target" ]` only when auto-start is
enabled. Selected API `5c76e329` explicitly enables the separate legacy
`containers.webui` at `tests/configs/nixos/vpsadmin-services.nix:298-300`;
that setting does not apply to `newadmin`.

The existing selected services toplevel `jds0d7…` independently demonstrates
the missing boot edge: `container@newadmin.service` has the seed `Requires`
and `After`, but `etc/systemd/system/machines.target.wants/` contains the legacy
`container@webui.service` link and no `container@newadmin.service` link. Seed
`Before` and container `Requires`/`After` constrain a requested start; they do
not request that start. Keep those dependencies and add only the declarative
auto-start setting. The inspected dirty unit assertions at
`test.nix:1146-1158` are appropriate: enabled means auto-start, machine-target
membership and both seed dependencies; disabled means neither the container
definition nor its named service. Ownership and commitment of that application
change remain with the implementer and lead.

This changes services-VM boot wiring only, without changing credentials,
database schema, package interfaces or cluster lifecycle authority. Applying
the fix requires the ordinary reviewed package/services-update path when
authorized; neither a label-only profile switch nor this assessment applies it
to the running VM. Preserve retained credentials, compatible API/schema and BFF
state during recovery. Do not replace the fix with a manual container start or
declare readiness from runner-level `ready: true`.

In a DB transaction, upsert by the retained unique client ID with a distinct
name and set these fields explicitly:

- `redirect_uri = <public-origin>/oauth/callback`;
- `authorization_start_uri = <public-origin>/oauth/login`, an absolute HTTPS
  URI without userinfo or fragment;
- `authorization_start_requires_user_action = false` and
  `allow_single_sign_on = true`;
- `access_token_lifetime = :fixed`, `access_token_seconds = 1200`,
  `issue_refresh_token = true`, `refresh_token_seconds = 2592000`;
- `is_default = false` through the model setter, which stores NULL.

The proposed development token policy uses 20-minute access tokens and a
30-day refresh lifetime matching the BFF's default session duration; keep the
values explicit and document any adjusted policy. Refresh issuance must be
enabled: the schema defaults it to false, and the BFF cannot renew an expired
access token without a refresh token. Read the secret at runtime and use
`Oauth2Client#set_secret` only when the stored hash does not verify. Normal
`save!` with the nondefault setter is sufficient; never select the new client
as default or clear/change the PHP client's flag or credentials. Repeated seeds
must keep the same row and verified secret hash. Do not log credentials or add
a migration. A preparation/seed failure must not launch a stale newly requested
build.

Retain bundle and BFF session state across `stop`/`start` and services updates.
Credential rotation and explicit destructive cluster reset are separate operator
actions under the existing ownership rules. No such action is authorized by
writing this design. Existing cluster socket/generation/state-schema contracts
remain unchanged; adding a service is not permission to infer legacy ownership.

### Source proof and focused validation

These are source conclusions at the revisions above, not deployment proof.
Paths below are relative to the named repository; HaveAPI references use tag
`v0.29.8`. The comparison from `7045c81b` to selected `5c76e329` changes none of
the contracts below; the API gemset difference is an unrelated regexp_parser
update. The selected API worktree was clean during inspection.

| Contract | Source evidence |
| --- | --- |
| Required runtime API path and override | extension `dev-clusters/vpsadmin/bin/devcluster:540-545,628-631` |
| Separate smoke API selection | extension `flake.lock:79-103`, `test/devcluster_nix_smoke.rb:41-49` |
| Nondefault setter, secret hashing and validation | vpsadmin `api/models/oauth2_client.rb:10-49,90-110` |
| Refresh defaults and issuance/rotation | vpsadmin `api/db/schema.rb:1370-1386`, `api/lib/vpsadmin/api/authentication/oauth2_config.rb:215-294` |
| OAuth frontend and password recovery | vpsadmin `nixos/modules/vpsadmin/frontend.nix:256-273`; HaveAPI `servers/ruby/lib/haveapi/server.rb:920-922`, `authentication/oauth2/provider.rb:85-111` under the same library directory |
| CORS and allowed token header | vpsadmin `packages/api/gemset.nix:343-366`; HaveAPI `servers/ruby/lib/haveapi/server.rb:163-172,431-437`, `authentication/oauth2/provider.rb:81-83`, `authentication/oauth2/config.rb:135-143` |
| SPA header and cookie policy | WebUI `src/lib/api/haveapi.ts:369-379,433-442` |
| Seed ordering and legacy default preservation | extension `dev-clusters/vpsadmin/nix/test.nix:391-409,1338-1369,1681-1684`; vpsadmin `nixos/modules/vpsadmin/database-setup.nix:135-187` |
| Private listener, forwarding trust and route ownership | WebUI `nixos/modules/webui.nix:138-169,282-310,493-559`; edge example `tests/nixos/webui-vm.nix:23-37,80-85` |
| Credentials, session state and loopback-only BFF | WebUI `nixos/modules/webui.nix:433-474`, `bff/server.js:195-196,425` |
| Refresh and confidential authorization-code exchange | WebUI `bff/server.js:154-187,322-328,360-378` |
| Local origin conflict | extension `dev-clusters/vpsadmin/nix/test.nix:923-931,962-981`, `dev-clusters/lib/runtime.sh:1114-1117`; WebUI `bff/runtime-config.js:134-163`, `nixos/modules/webui.nix:532-534` |

The implementer should run focused command/status Ruby fixtures in the
extension Nix shell, then include an enabled bridge fixture in
`test/devcluster_nix_smoke.rb`. Evaluate disabled old configs in both modes and
the explicit unsupported enabled-local error. Assert seed/container dependency
ordering, path-only credential references, exact headers/listeners and unchanged
legacy services. The enabled fixture must force the services configuration and
its auto-start/unit assertions; disabled bridge/local fixtures must retain the
absence of the named React container/service. Removing auto-start in a
disposable fixture must fail the enabled assertion. After an authorized build,
inspect the new services result for the machine-target link and retained seed
dependencies. After authorized activation, separately prove
`container@newadmin.service` is active, seed completion succeeded, the private
nginx/BFF are healthy and the public TLS/OAuth/PHP checks below pass. The
existing `nix run .#devcluster-check` is the longer evaluation/runner check,
under the normal review/watcher gate; no framework expansion is needed.
In a disposable API fixture, seed twice and assert one stable
new client/hash, NULL default, unchanged PHP default, configured token lifetimes
and issuance/rotation of refresh tokens.

After committed-change review, use a watcher for `nix run .#devcluster-check`
and package/module checks. The reviewed WebUI offers
`nix eval --json --no-write-lock-file .#checks.x86_64-linux.module-eval.passthru.results`
and `nix build --no-link .#checks.x86_64-linux.package-contents`; neither replaces
the enabled cluster evaluation and real login checks. In an authorized booted
bridge cluster, check services and nested newadmin `nginx -t`, inspect
`ss -lnt` for private loopback 18082/3001, then probe through the public edge:

```sh
curl --cacert "$cluster_ca" -sS -D - -o /dev/null -X OPTIONS \
  -H 'Origin: https://newadmin.aitherdev.int.vpsfree.cz' \
  -H 'Access-Control-Request-Method: GET' \
  -H 'Access-Control-Request-Headers: X-HaveAPI-OAuth2-Token,Content-Type' \
  https://api.aitherdev.int.vpsfree.cz/
curl --cacert "$cluster_ca" -fsS \
  https://newadmin.aitherdev.int.vpsfree.cz/healthz
```

Expect preflight 200, wildcard origin, and both requested headers allowed.
Then verify authenticated API access, login/callback, token refresh, logout,
session retention, and unchanged PHP/default recovery behavior with a disposable
seeded account. Assert responses without logging access/refresh tokens, cookies,
callback state or authorization codes. Exercise upstream-failure OAuth log
suppression and credential failure in isolated fixtures. The lead's completed
live service and authenticated-flow evidence is recorded below; normal DNS
readiness remains a separate gate.

### Running bridge cluster: completed evidence and acceptance reference

On 2026-09-30 the lead's normal-host filtered status confirmed this exact
session is already `running`, `ready: true`, `single`, `bridge`, with clean
pinned WebUI `534caa83` and the expected PHP/React/API/auth URLs. The earlier
provider error was transient during state changes. Do not start, reset or
update this cluster for the label-only package cascade. The selected profile
is `aidlqw1…` (workspace `0e00eab5`); the lead also confirmed live portal
`gpt-6.1-sol` high/xhigh and the active thread's exact model/xhigh settings.
These facts complete those live model checks. The lead subsequently reported
the following live checks passed in this exact disposable bridge cluster:

- Real OAuth login/callback and rejection of reused one-use state;
  authenticated session and API access.
- BFF restart persistence, two OAuth seed reruns, and logout/revocation.
- Strict-CA TLS, static content, React health, CORS and legacy PHP checks;
  loopback-only private nginx 18082 and BFF 3001.
- Real provider refresh after changing only the authenticated server-side test
  session's `expires_at` to a truthy expired value: the BFF rotated the access
  token, restored a future expiry, preserved `sessionKey`, and the API accepted
  the refreshed token. Credentials and provider token lifetimes were unchanged;
  the lead deleted all secret temporary files after verification.

This is lead-reported completed evidence, not a new architect-run probe. The
bounded disposable-session refresh test satisfies this session's refresh gate;
no redundant 20-minute wait is required. It exercised the normal BFF/provider
refresh path, rather than merely testing an edited timestamp. Normal host/VPN
DNS and browser reachability remain separate from the `--resolve` service
checks and subject to the publication gate below.

The following commands and criteria remain a reference for any needed
inspection from the normal host context and this verified session; completed
checks do not need repetition without a relevant change or failure. The
architect's restricted shell cannot open the dispatcher transition lock or see
host processes/netlink; its absent PID observation is not a stopped-run proof.
Existing `runner.log`, per-machine logs under `state/`, and `result-config`
belong to the running operation. If further long readiness monitoring is needed,
assign a fresh Luna watcher to those existing logs; do not launch a second run.

```sh
slug=2026-09-30-portal-review-improvements
cluster_dir=/home/aither/workspace/ai/vpsfree.cz/.dev-clusters/vpsadmin/clusters/$slug
cluster_ca=/home/aither/workspace/ai/vpsfree.cz/.dev-clusters/vpsadmin/certs/default/vpsadmin-ca.crt
dev-session current
workspace-host status
set -o pipefail
vpsadmin-devcluster status "$slug" --json |
  jq '{schema,found,kind,state,ready,topology,network,webuiSource,
       services:[.services[]? | {label,url}]}'
jq '{newWebui,domains,network,services:{ip:.services.ip},topologies}' \
  "$cluster_dir/config.json"
jq '{labels,machines:(.machines | with_entries(.value |= {toplevel}))}' \
  "$cluster_dir/result-config"
```

The source distinction matters: `vpsadmin-devcluster config "$slug"` creates or
merges configuration, and `urls` also prepares state and prints credentials.
Neither is a read-only inspection command. Unfiltered `status --json` includes
`services[].accounts` secret fields; retain only the projection above. A truly
absent cluster returns `found:false`, not a provider failure. If that is ever
observed after ownership checks, the supported future start command is
`vpsadmin-devcluster start "$slug" --topology single --network bridge`, through
the authorized watcher/start workflow, without `--force`; it is not indicated
for the current running cluster. Do not invoke private helpers or infer new
start/stop/reset authority from this checklist.

1. **Host and selected build.** Verify `ip -br link show br0`, the configured
   bridge-helper executable and `/etc/qemu/bridge.conf`; resolve the four public
   names to services IP `172.16.106.53`. Preserve the selected result versus
   activated-VM distinction. The inspected result was `6nxx6yw…json`, services
   toplevel `jds0d7…`, API/database source `5c76e329`, and clean pinned WebUI
   `534caa83`. Read-only guest commands use
   `vpsadmin-devcluster ssh "$slug" services -- <command>`; keep its ordinary
   session/generation/ownership guards. Compare guest `readlink -f
   /run/current-system` with the selected services toplevel.
2. **Services and render.** Through that SSH command, run `nginx -t`,
   `systemctl show vpsadmin-devcluster-webui-credentials.service
   vpsadmin-devcluster-webui-seed.service container@newadmin.service
   -p ActiveState -p SubState -p Result -p ExecMainStatus -p After -p Requires`,
   and `nixos-container run newadmin -- nginx -t`. Check the BFF with
   `nixos-container run newadmin -- systemctl show vpsadmin-webui-bff.service
   -p ActiveState -p SubState -p Result`, and inspect `ss -lnt` for loopback-only
   18082/3001. The seed is a oneshot without RemainAfterExit: inactive/dead with
   a completed successful invocation is valid, not a failure. Confirm rendered
   seed ordering, exact edge Host/forwarding values, OAuth access/error-log
   suppression, CA trust and separate BFF session storage without dumping full
   environment, credential files, service journals or process arguments.
3. **Runtime bundle and seed.** Inspect only owner/mode/size and boolean format
   assertions: bundle mode 0700, exactly three nonsymlink regular files with
   mode 0600, each 65 bytes containing 64 lowercase hex digits plus newline.
   The architect checked
   this existing bundle's shape/format without disclosing values. Inside the
   services VM, use `stat`/quiet `cmp` to verify the runtime files at
   `/run/vpsadmin-newadmin-credentials` match the mounted bundle; never print
   their contents or hashes. The rendered seed requires database setup, base
   seed and credential preparation; `container@newadmin` requires that seed.
   Require successful seed completion and successful OAuth exchange. If DB
   inspection is needed, query only boolean/count/nonsecret policy fields for
   the named React client: one row, NULL default, fixed 1200-second access tokens,
   refresh enabled for 2592000 seconds, exact callback/start origins, and a distinct
   unchanged PHP default. Never SELECT client IDs, secrets, secret hashes or
   token rows into output. The lead's two seed reruns already passed; ordinary
   read-only inspection needs no additional seed rerun.
4. **TLS, public endpoints and CORS.** Use the cluster CA with bounded curl
   timeouts; never `-k`. Check React `/`, a deep link, `/healthz`, `/config.json`
   and PHP `/` using `-o /dev/null -w '%{http_code}\n'`. Add
   `--resolve <host>:443:172.16.106.53` when testing the edge before DNS is ready,
   then repeat through normal DNS. Verify the existing preflight command above;
   print only status and Access-Control-* headers. Public config must point at
   exact newadmin/API/auth/legacy origins and API 7.0. A cross-origin
   `/session.json` request must fail; same-origin unauthenticated access must
   have no token. Filter session JSON to booleans only.
5. **OAuth, refresh and PHP coexistence: completed.** The lead passed real
   `/oauth/login` → auth origin → exact `/oauth/callback`, one-use state
   rejection, authenticated session/API access, BFF restart persistence,
   refresh, logout/revocation and PHP coexistence. Keep no-store/session
   protections and avoid recording a HAR, callback URL/query, cookies or tokens.
   Refresh is automatic in reviewed `bff/server.js:155-187,256-274` when a
   same-origin `/session.json` read reaches access-token expiry; there is no
   separate refresh endpoint. The accepted bounded probe edits only
   `expires_at` in the authenticated disposable server-side test session to a
   truthy expired value, then lets that normal path perform the real refresh.
   Assert token rotation, restored future expiry, unchanged `sessionKey` and
   accepted authenticated API access; report booleans only. It does not alter
   credentials, provider lifetimes or other sessions. The completed probe and
   deletion of its secret temporary files replace the proposed natural-expiry
   wait for this session. Full VM restart and negative credential tests, if
   needed, retain their separately authorized verification scope.

Failure means retain the running cluster, credentials, session state and
compatible API/schema, report the failing gate, and use the previously defined
forward recovery path only when authorized. A source/result selection does not
prove activation; OAuth success does not replace refresh/PHP evidence. No
lifecycle action or additional deployment is authorized by this checklist.

### Internal DNS candidate and publication gate

The lead accepted local preparation of a fourth-repository change necessary
for the approved hostname. **Shared DNS publication is pending exact-target
user approval.** Prepare, check and independently review the candidate before
requesting that approval. The existing aitherdev and user-profile deployment
targets do not include these shared DNS hosts; cluster/profile work continues
independently. This brief authorizes no cluster restart, reset or DNS deployment.

Only `configs/internal-dns/zone.vpsfree.cz.` in the same-session
`vpsfree-cz-configuration` worktree changes: add
`newadmin.aitherdev.int IN CNAME frontend.aitherdev.int.vpsfree.cz.` beside the
existing aitherdev aliases and advance the SOA serial monotonically from the
selected source value `2026092800` (recheck the latest value before editing).
No input, system host code, public zone, OAuth origin or cluster configuration
change is included. `newadmin.vpsfree.cz` in the public zone is the separate
production service and must remain unchanged.

Source ownership at configuration `ee99382c`: the internal zone's line 241
maps `frontend.aitherdev.int` to `172.16.106.53`; lines 244-259 contain the
existing service aliases but no newadmin alias. `configs/internal-dns/default.nix`
lines 11-15 and 26-42 substitute each consumer's FQDN and configure BIND to
serve this zone as master. These are independent local copies, not replicas
that can be assumed to transfer the change from one updated host:

| Exact configuration target | Address | DNS role and source |
| --- | --- | --- |
| `cz.vpsfree/containers/prg/int.ns1` | `172.16.9.90` | Client resolver; `config.nix:11` imports the zone module, `module.nix:3-6,31-35` supplies address and internal-dns/manual-update tags |
| `cz.vpsfree/containers/brq/int.ns1` | `172.19.9.90` | Client resolver; same import and module locations as the Prague ns1 |
| `cz.vpsfree/containers/prg/int.mon1` | `172.16.4.10` | Monitoring's local authoritative copy; `config.nix:11,29` imports the zone and uses localhost DNS; `module.nix:18,34-38` identifies address and all-internal-dns tag |
| `cz.vpsfree/containers/prg/int.mon2` | `172.16.4.18` | Monitoring's local authoritative copy; `config.nix:13,31` imports the zone and uses localhost DNS; `module.nix:18,34-38` identifies address and all-internal-dns tag |

Use these four names for the proposed approval inventory, not an unbounded tag
deployment. Both ns1 hosts are needed for consistent client resolution; the two
monitoring copies need the same record for their local view. The host's
`cluster/cz.vpsfree/machines/aitherdev/config.nix:20-35,149` selects the two ns1
resolvers before `172.16.106.1`. In contrast, extension `test.nix:920-923,985-994,
1186-1197` generates guest hosts and cluster dnsmasq records only. The inspected
services result already contains `host-record=newadmin.aitherdev.int.vpsfree.cz,172.16.106.53`.
That does not publish the name to the host or VPN clients.

Quick candidate checks: require exactly the one alias and increased serial in
the zone diff, no duplicate owner/conflicting record, and `git diff --check`.
Render the zone with each consumer's FQDN replacing `@fqdn@`, then run
`named-checkzone vpsfree.cz <rendered-zone>` using the configuration's Nix
tooling. After committed-change review, use a fresh watcher for builds of the
four exact targets. Prepare selected-result/change evidence for the approval
request; compare against deployed generations so unrelated activation changes
are visible. Dry activation and switch on those shared hosts wait for the
explicit approved target/action set. No successful local check publishes DNS.

After approved publication, query each copy's SOA and the new A/CNAME answer;
for client resolvers use
`dig @172.16.9.90 newadmin.aitherdev.int.vpsfree.cz A +noall +answer`
and repeat at `172.19.9.90`. Check monitoring's local BIND views
through their approved inspection path. Require matching intended serials and
the CNAME resolving to `172.16.106.53`. Then require normal aitherdev
`getent ahostsv4 newadmin.aitherdev.int.vpsfree.cz` and repeat resolution on the
intended VPN/browser client, verifying that client's actual resolver and route
can reach the internal zone and services IP. A direct authoritative query
does not prove client resolver selection; public DNS/DoH is not this private
zone. Do not silently change client DNS or routes.

The lead reported strict-cluster-CA React `/healthz` 200 and PHP `/` 200 using
`--resolve`, loopback-only BFF 3001/private nginx 18082, and API preflight 200
with wildcard noncredentialed CORS and the required token/Content-Type headers.
The completed OAuth, refresh, BFF persistence, seed-rerun and logout evidence is
recorded above. After publication, repeat HTTPS without `--resolve` and confirm
browser login/callback and API reachability from the intended normal host/VPN
client before claiming hostname/browser readiness. A DNS-only publication does
not require repeating the completed refresh, seed or persistence probes. Keep
credentials, tokens and callback queries out of verification output.

The selected zone has one-hour default and negative-cache TTLs. Verify live
SOA/remaining negative TTL if a client still reports no record after all copies
answer correctly; allow expiry or obtain approval for a targeted client/cache
refresh, without restarting/resetting the cluster. On partial publication,
report which copies changed and complete only the approved target set.
Correction/removal after publication uses a forward zone change with a serial
higher than every published value; reverting an old file/generation with a
lower serial is not DNS recovery. Keep the working cluster, OAuth credentials,
BFF state and compatible API/schema intact throughout.

## Compatibility, deployment and recovery

All new portal interfaces are additive; package browser/server assets deploy
together. Old explicit settings/member callers continue to work. Legacy
manifest fields, review scope hashes, committed comparison records, roster
schema, lifecycle journals and cluster identity schemas remain unchanged. The
new snapshot store is ephemeral and unsupported by an older UI; expiry loses
only a disposable review, never repository content. A previous reader ignores
new optional status fields. A page opened before a portal switch can be asked
to reload on unsupported endpoint/expired snapshot; no destructive fallback.

Deploy in dependency order: reviewed/verified dev-workspace feature revision,
extension pin plus cluster changes, then workspace policy/config and extension
pin. Keep exact feature heads recorded and build the complete workspace package
before switching through the stable user-profile command. Do not use system
configuration pins to deploy the portal. Validate required model availability,
package-generation checks and session/cluster ownership before activation.
Prepare and run the separate services-VM update only through the authorized
cluster workflow, preserving the PHP UI and API throughout the supported
update/restart behavior. Readiness of the portal does not prove the new cluster
UI has been booted or logged in successfully.

The current runtime explicitly makes `workspace-host` switches forward-only
and refuses `workspace-host rollback`. Therefore recovery is retrying the same
failed switch when its journal permits, or building a newer compatible package
that reverts the feature behavior. Do not prescribe selecting an older profile.
Data-format compatibility with earlier code remains valuable but is not
authorization to bypass this transition policy. This corrects the plan's
shorthand about restoring the previous portal generation.

For a cluster service failure after publication, the selected result may already
be a complete new build; verify actual VM activation and the partial-update
report separately. Retry the normal build to establish successful rooting and
validation, then recover through the supported services update with a known-good
matching frontend/BFF pair or a new config disabling only the React service.
Retain credentials and BFF session state throughout recovery. Do not reset the
cluster, delete the OAuth client, rotate secrets, or touch another session to
recover the PHP UI.
Keep the compatible selected API/schema when disabling React. Updating an older
API can run its existing upstream migrations; this design introduces none and
does not prove that a prior API/VM generation can read the resulting database.
Do not treat an arbitrary older services generation as a safe schema rollback.

No feature branch enters a default branch without the user's explicit
repository/target integration direction. Leave this session open. The lead
records deployment outcomes and recovery preparation separately from lasting
feature docs. Document behavior in dev-workspace's README/portal guide and
cluster operations in the extension's cluster README; workspace docs own site
domain and model policy. Apply the user-facing-writing workflow to final labels,
errors/help and product-facing prose before committing.

## Acceptance and verification

### Quick checks before independent review

Use each repository's Nix toolchain. The implementer records exact commands and
results; the following are the selection brief, not claims of completed checks.
Do not expand to long suites before the mandatory committed-change review.

1. `dev-workspace`: focused Go tests for `internal/repository`,
   `internal/web`, `internal/teamruntime`, `internal/session` and changed CLI
   adapters; focused browser contracts including
   `repository_review_browser_test.cjs`, `team_settings_browser_test.cjs`, and
   a live-settings race fixture. Run `node --check` on changed browser files and
   review-editor unit tests if its module changes. Use temporary fixture repos.
2. A comparison with more than eight files keeps early editors/content after
   scrolling through the rest. Load all performs bounded requests, expands large
   diffs, shows all completion/errors, handles retries and cancels on navigation.
   Repository HTML refresh and visibility suspension keep retained content.
3. Staged/unstaged fixtures cover one file changed in both layers, untracked
   versus ignored, names with spaces/Unicode/control bytes, rename/delete,
   mode-only, symlink and symlink-directory, binary/over-limit, gitlink, missing
   newline, intent-to-add, conflicted/sparse/split indexes, and concurrent writes.
   Accept safe display or precise unsupported-state error for index extensions;
   never silently produce the wrong comparison. Invalid UTF-8/control paths
   must not collide after JSON encoding or become executable markup.
   Include stat-matched, mismatched and racy tracked files, proving that only
   mismatched/racy tracked candidates are opened. Oversized candidates must
   freeze metadata and any admitted preview within the existing bounds, show
   "content not compared", and report unavailable individual/aggregate line
   totals instead of exact or zero claims. Prove there is no full-file hashing
   or later live read to fill the missing content.
   A fixture with index gitlinks and unrelated ordinary edits must still return
   the ordinary unstaged comparison, with a bounded `unverifiedSubmodules`
   list containing only validated paths and captured index mode/object IDs.
   Assert no submodule traversal/status call, no gitlink `ReviewFile` or
   changed-file/line contribution, and no dirty/changed claim. Verify the
   "working state not inspected" notice also appears for a gitlink-only
   capture, metadata stays frozen after index/submodule changes, admission
   bounds are enforced, and staged/committed gitlink diffs remain unchanged.
4. Verify real index, refs/reflogs, object inventory and working content are
   unchanged after capture/read/error/cancel. Configure hostile external diff,
   textconv/clean filters and fsmonitor in a fixture and prove none execute.
   Prove the hostile clean filter is live with a deterministic disposable-fixture
   control: `git -C <fixture> -c core.fsmonitor=false
   -c core.attributesFile=/dev/null hash-object --path=README README`, without
   `-w` or `--no-filters`. Require the filter marker, remove it, then assert the
   actual snapshot reader's stage/debug plus no-follow stat discovery, capture
   and revalidation leave all clean-filter/fsmonitor/external-diff/textconv
   markers absent. Retain the hostile repository configuration and local
   `.gitattributes` during capture; command-local control overrides must not
   disable the fixture globally. Check forbidden markers after each capture.
   Do not require `ls-files -m`, `diff-files --name-only` or `status --porcelain`
   to run the filter on every fixture: their stat shortcuts can avoid content
   comparison. They remain prohibited in snapshot discovery/revalidation.
   Independently guard both actual `CaptureWorktree` calls with a test-local
   PATH Git wrapper that records and rejects excluded commands before Git runs.
   Require no rejection record and observed safe stage/debug calls after each
   capture; marker absence alone does not prove command exclusion. Use the
   bounded wrapper contract below, without changing the production runner.
   Snapshot reads stay byte-identical after the worktree/index changes. Test
   expiration, admission quotas, active-reader eviction, failed capture cleanup,
   archived/foreign IDs and retargeted worktree/registration denial.

5. Provider fixtures prove current GitHub link/status/workflow behavior,
   unsupported origin denial, local review during GitHub failure, URL escaping,
   archived links and old manifest parsing. Existing durable review IDs must
   still reopen after this change.
6. Settings fixtures reorder a poll around Apply success/failure, change model
   then effort without a write, edit during polling, restore/cancel a draft,
   become active while dirty, switch member conversations, lose the HTTP
   response, and fail roster persistence. Assert exactly one explicit pair is
   submitted, stale reads do not replace it, and errors do not clear the draft.
7. Team fixtures cover each role, aliases/custom roles, solo/smaller retained
   presets and fallback, ambiguous/unavailable catalogs, role switching,
   explicit overrides, absent/both/partial fields in HTTP and CLI, no mutation
   on validation failure, and saved retry settings after a catalog update.
   Workspace catalog checks prove only new Sol defaults changed.
8. `vpsfree-dev-workspace`: focused Ruby command/status fixtures and shell syntax
   checks. Inspect generated Nix and evaluate disabled/enabled/new/local cases,
   both locked WebUI input and optional same-session override, input follows,
   package provenance, listeners, normalized proxy headers, CA trust, credential
   path-only derivations, service ordering and PHP coexistence. No new kernel
   build is acceptable as an incidental effect of these changes.

#### Clean-filter control and command-exclusion evidence

The control clarification comes from the bounded CI investigation of
`TestWorktreeCaptureSkipsUnchangedLargeFilesAndFilters` at generic head
`13383c0`, with implementer-owned test edits present. In 20 fresh disposable
repositories per case using installed Git 2.54.0, filter invocation counts were:

| Working content | `ls-files -m` | `diff-files --name-only` | `status --porcelain` | `hash-object --path=README README` |
| --- | --- | --- | --- | --- |
| Unchanged | 20/20 | 20/20 | 20/20 | 20/20 |
| Same-size edit | 20/20 | 19/20 | 20/20 | 20/20 |
| Different-size edit | 0/20 | 0/20 | 0/20 | 20/20 |

Each hash control left index bytes and object inventory unchanged; stage/debug
reads left the filter marker absent in all 60 cases. These are scratch
observations, not guaranteed invocation rates or a packaged test result.
Git's [`ie_modified`/`ie_match_stat` paths](https://github.com/git/git/blob/v2.54.0/read-cache.c#L358-L461)
can conclude from stat information or enter content comparison depending on
size, mode and racy timestamps. In contrast,
[`hash-object --path`](https://git-scm.com/docs/git-hash-object#Documentation/git-hash-object.txt---path)
explicitly selects path-based conversion without needing an index comparison;
omitting `-w` avoids writing an object. Replace the timing-dependent positive
control loop, not the production reader or its negative safety assertions.
No sleeps, index-stat rewriting, per-command retry-until-marker loop or reduced
filter coverage is required. Keep same-size/racy and oversized-file behavior
tests independent of this filter-liveness control.

Filter liveness and excluded-command absence are separate assertions. A reader
regression that calls a prohibited command on a stat-shortcut path can leave
every hook marker absent. Add a narrow wrapper in the existing Go test:

- Resolve the absolute real Git executable before prepending the wrapper's
  temporary directory to PATH. Scope PATH with `t.Setenv` to a nonparallel
  capture subtest; setup, commits and the `hash-object --path` control remain
  outside it. Keep the hostile repository configuration and attributes active.
- Parse the actual global prefix, skipping `--no-pager`,
  `--no-replace-objects`, and the values paired with `-c`/`-C`. Fail unknown
  prefixes rather than silently missing the subcommand. Match the command
  position, not arbitrary argument substrings or paths.
- Record and reject any `status` or `diff-files`. For `ls-files`, permit only
  the four existing argument forms: `--stage -z`, `--debug -z`, `-v -z`, and
  `--others --exclude-standard -z`. This excludes `-m`, `--modified`, combined
  short flags such as `-mz`, and modified mode mixed with a permitted option.
  Forward the current read-only commands, including the private `diff
  --no-index --no-ext-diff --no-textconv`, with original arguments and exit
  status intact. This is a fixture guard, not a general Git policy parser.
- Write a rejection record before a distinct failing exit (for example 97),
  and assert it is absent after each actual capture even if capture could
  swallow or retry an error. Record permitted commands too; require observed
  stage/debug reads so an unused wrapper cannot pass. Verify representative
  excluded forms are rejected by the wrapper, then clear those self-check
  records before capture. Keep all existing hook-marker checks after both
  captures and do not clear capture violations between assertions.
- Embed safely shell-quoted absolute executable and record paths in the
  generated script. Do not depend on custom environment variables: the main
  runner at `portal/internal/repository/review.go:162-170` retains PATH, while
  the text-diff child at `review_worktree.go:761-764` supplies a restricted
  explicit environment that also retains PATH. No production runner injection
  interface or application change is needed.

A separate disposable wrapper experiment rejected and recorded all six tested
forms (`status --porcelain`, `diff-files --name-only`, and `ls-files` with `-m`,
`--modified`, `-mz`, or `--stage -m -z`); forwarded all four safe index forms;
and forwarded a private no-index diff with the reader's restricted environment
and exit status 1. Quoted paths containing spaces and a single quote worked.
No clean-filter marker appeared during guarded commands. This validates the
wrapper approach, not the still-to-be-implemented Go capture assertion.
The narrow implementation belongs in
`portal/internal/repository/review_worktree_test.go`, reusing existing fixture
helpers. It changes test observability only: snapshot quotas, filter prohibition,
API/storage behavior, compatibility, deployment and recovery remain unchanged.
Nix shell entry was blocked by the sandbox's read-only fetcher-cache SQLite
path; repository toolchain/CI verification remains with the lead and implementer.

### Review and longer checks

The lead supplies the dedicated reviewer the complete committed base-to-head
series, final diffs, this design, trust boundary and migration provenance. Require
an explicit whole-branch history/migration conclusion: there are no schema
migrations here, and obsolete implementation attempts must be consolidated
before readiness. Remote browser clients and guests remain untrusted; the local
workspace operator is the trusted host administrator. Review scope should focus
on ordinary wrong-session/path selection, concurrency, authorization, secret
handling, persistence and recovery, not an already-compromised operator.

After review findings are resolved, launch long/uncertain checks through a fresh
Luna/low watcher per the monitor skill. Appropriate checks are:

- Packaged `nix flake check --print-build-logs` for changed repositories and
  workspace policy/composition, plus full Go/browser suites where not already
  covered. Observe current feature-head CI and diagnose failed attempts before
  rerunning them.
- `nix run .#devcluster-check` for installed provider evaluation, runner loading,
  bridge/local defaults and overrides. Build the exact selected WebUI frontend
  and BFF through the cluster dependency closure; verify matching build metadata
  and package-content/closure contracts. Do not claim build evidence from eval.
- Run a browser check on a packaged candidate: large/many-file load-all and
  retained scrolling, committed deep links, expiry/refresh of uncommitted
  snapshots, and live lead/member settings across background polling, reload,
  reconnect and the next authorized turn. Record memory/responsiveness and the
  accepted native-Find limitation.
- Boot/update only this session's cluster in bridge mode. Verify TLS SAN/trust,
  React root/deep links/assets and build-info, `/healthz`, public configuration,
  unauthenticated/authenticated `/session.json`, actual OAuth callback and one-use
  state with an existing disposable seeded account, logout/revocation, API CORS,
  and the unchanged PHP login/default recovery client. Inspect secret-free
  process environment, private credentials/session permissions and OAuth log
  suppression without recording response tokens or secret contents.
- Restart BFF and services using the same credential bundle and prove sessions
  and the separate client survive. Rebuild from an explicit local WebUI source
  override and prove both package metadata reflect it. Verify missing/invalid
  credential refusal and retained PHP availability in an isolated fixture; do
  not damage a working cluster's credentials merely to test failure behavior.
- Activate the reviewed complete workspace package via its user profile and
  verify portal/session/member/repository/cluster pages. Record portal
  deployment, cluster deployment, login proof and branch readiness separately.

Unexpected local kernel compilation stops the affected verification and goes
back to the lead for the documented cache investigation. A missing live model,
WebUI/API contract, trustworthy source override or OAuth/network proof is a
concrete blocker for that feature's readiness, not a reason to silently broaden
scope or mark the entire initiative complete.

## Addendum: Codex 0.159.2 and exact GPT-6.1 Sol availability

This authorized follow-up supersedes the earlier assumption that no Codex
version change is needed. The implementation edit is confined to the workspace
feature worktree's `flake.lock`. Deploy the existing configuration feature head
to aitherdev separately; no generic runtime, extension, codex-web, configuration
application code, model substitution or account configuration change is in scope.

### Evidence and package ownership

At inspection on 2026-09-30:

| Consumer | Current selection | Required selection |
| --- | --- | --- |
| Workspace at `99e387511cd9d6beac2b9cbb4a7c49306b394ab5` | `vpsfree-dev-workspace` `67bfbbd653694e13e8d5aee53ef0f8e283694bf5` → `dev-workspace` `41c648cd92cb324037778be165e45e17c46bbc75` → lock node `llm-agents` `ddc89534b9a73cd99ff4d33656569ce3be6e6490`; built package reports Codex 0.155.0 | Change only the nested `vpsfree-dev-workspace/dev-workspace/llm-agents` input to `af40d966859ec4075ecc172dbb39e53f474dc5d9`, including its required dependency closure; Codex 0.159.2 |
| Configuration at `ee99382c8c448a15347052a6964030f838cb0381` | Root `llm-agents` input resolves to lock node `llm-agents_2` at `af40d966859ec4075ecc172dbb39e53f474dc5d9`, already updated by generated commit `7ef14716c9da6b85c2edf7750de31ff40fe49c5d` | Deploy this existing head; no new input commit expected |
| Configuration's separate `devWorkspace` input | `ec05cb9f008cc8d6bccfd23e9b15a69d9a66fa40` → its own `llm-agents` node at `ddc89534…` | Leave unchanged for this bounded correction; assess the existing host-contract mismatch below |
| Running system executable | `/run/current-system/sw/bin/codex` reports 0.158.0 | 0.159.2 after the aitherdev system switch |

The lock graph and current 0.155.0/0.158.0 executables were inspected directly.
The lead evaluated and built the existing configuration channel at `af40d966`
as `/nix/store/4mxlhqv9angcqgjw4c067nfpjlxv3d4h-codex-0.159.2`; the older
running system has not deployed that head. A temporary probe called the
existing codex-web `Client.ListModels` against an isolated App Server from that
exact package using the same `/home/aither/.codex` account. It therefore used
the actual client path below (`limit: 100`, `includeHidden: false`, cursor
handling), rather than a separate model-list implementation. The lead's
successful log, `/tmp/portal-model-probe-1592-cgo0.log`, was also read by the
architect: nine models, exactly one matching `gpt-6.1-sol`, `isDefault: true`,
`defaultReasoningEffort: low`, and supported efforts
`low/medium/high/xhigh/max/ultra`. Both required `high` and `xhigh` are present.
The reported catalog default does not replace this workspace's explicit role
efforts. Nine returned models do not constitute a multi-page pagination test.

The first probe failed to build Go because ambient cgo/gcc was unavailable;
the probe passed with `CGO_ENABLED=0`. That first failure was a probe-toolchain
issue, not an App Server or model-availability failure. The earlier isolated
0.158.0 probe did not expose the exact model. This establishes picker-visible
catalog support for the proved 0.159.2 binary/account/client combination, not
universal account availability or a successful deployed turn. No live probe
was repeated by the architect. The lead also reports that the nested workspace
lock has been generated with `af40d966` and its transitive bun2nix/nixpkgs changes;
the implementer inspected the graph and is awaiting this brief before commit.

In configuration, `flake.nix` maps the `llm-agents` channel to the root input;
`cluster/cz.vpsfree/machines/aitherdev/module.nix` selects it, and `config.nix`
lines 15–18 and 247 install that input's Codex as a system package. Its
`devWorkspace` input supplies the host module, not the user-profile application.
The workspace calls extension `lib.mkPackage`, which calls generic
`lib.mkPackage`; generic `flake.nix:36` passes its own llm-agents Codex to
`nix/workspace-portal.nix:260`, installing `libexec/codex`. The host helper
adopts this package binary into the retained active Codex root. Changing only
the system package therefore cannot fix the portal's catalog.

### Catalog and compatibility invariants

Pinned codex-web `codex/client.go:3288-3318` requests `model/list` with
`limit: 100, includeHidden: false`, follows every non-null `nextCursor`, and
rejects missing data, empty cursors and repeated cursors. The portal exposes
that result through `/api/models`; settings validators compare the exact
`.model` string and each requested `supportedReasoningEfforts[].reasoningEffort`.
Require exactly one visible `gpt-6.1-sol` with `high` and `xhigh`; a display name,
upgrade hint, hidden-only entry or similar model is insufficient. Keep saved
rosters unchanged and verify their existing models/efforts still work.

[Official model documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol)
confirms the exact name and high/xhigh support. The
[App Server documentation](https://learn.chatgpt.com/docs/app-server#list-models-modellist)
states that returned models and efforts depend on client and account. Neither
page proves this deployed account's access. Treat the new package's exact
catalog and subsequent successful runtime behavior as separate acceptance gates.

Every Codex version change is a protocol compatibility change. Keep browser,
portal and terminal consumers on the same validated App Server binary. No
workspace state schema changes are proposed; Codex may change its own retained
state, so backward readability by 0.155.0/0.158.0 is not assumed. Do not edit
authentication, force a catalog, disable validation, or rewrite retained roles
to make the probe pass. Preserve credentials, retained roots and journals.

### Pin, verification and deployment sequence

1. In `worktrees/2026-09-30-portal-review-improvements/workspace`, update only
   the nested input with Nix, for example
   `nix flake update vpsfree-dev-workspace/dev-workspace/llm-agents` while it
   resolves to the selected `af40d966…`. Verify the resulting exact revision
   before accepting the lock: a later upstream head is not implicitly approved.
   Review transitive changes, including llm-agents' nixpkgs closure, while
   retaining extension `67bfbbd…`, generic `41c648c…`, codex-web and cluster pins.
   Do not hand-edit hashes or use an unpersisted override as deployment evidence.
   The configuration channel already owns its correct pin; no confctl input
   update is needed. If that premise changes, stop and use the channel procedure.
2. Run whitespace/lock-graph and workspace policy checks. Build the complete
   workspace candidate and run its four flake checks through the authorized
   verification lane. Use a fresh Luna watcher for long/uncertain checks after
   the applicable review gate. Record exact source, store paths and versions;
   earlier 0.155.0 package results do not validate this candidate. Confirm its
   packaged Codex resolves to the proved 0.159.2 store path above.
3. Run the candidate's own
   `bin/workspace-host check-codex --codex <candidate>/libexec/codex/bin/codex`.
   It generates the experimental JSON schema, validates the packaged codex-web
   request corpus, and probes App Server startup. Also retain compatibility with
   the currently active binary for transition preflight. Using the selected
   account and candidate binary, initialize an isolated App Server and request
   every `model/list` page with the exact flags above. Record only model IDs,
   effort options, binary/source identity and pass/fail; never credentials.
   A successful schema/startup check alone does not establish catalog access.
   The recorded `Client.ListModels` probe already supplies isolated catalog
   evidence if the final candidate retains that exact binary, client and
   account configuration; repeat it if those inputs change. The deployed
   portal catalog and live-turn checks remain required after activation.
4. From the clean same-session configuration worktree at `ee99382c…`, enter
   `nix develop`, then build only `cz.vpsfree/machines/aitherdev` with
   `confctl build cz.vpsfree/machines/aitherdev`. Inspect the system closure and
   activation delta; this deploys a complete host configuration, not a single
   executable. Run `confctl deploy cz.vpsfree/machines/aitherdev dry-activate`,
   review affected services, then the authorized
   `confctl deploy cz.vpsfree/machines/aitherdev switch`. Check system Codex
   0.159.2, host proxy/TLS/auth and user-service reachability. Stop at a failed
   build/dry activation. Do not merge a branch or select other hosts.
5. Only after candidate protocol/catalog checks and the host checks pass,
   perform the separate forward user-profile switch from the workspace feature
   source using the exact candidate entry:
   `nix run .#workspace-host -- switch --source "$PWD" --from-candidate`.
   All lifecycle journals, session/cluster ownership and generation
   checks remain mandatory; busy sessions must reach the supported idle boundary.
   Do not force-stop this session or clear journals. Verify registered agent
   configuration/capacity, retained Codex root, running service executable,
   portal and terminal versions, and absence of pending reconciliation.
   Recheck `/api/models` on the actual portal, not merely the isolated process.
6. Test new role defaults and an explicitly authorized live model/effort Apply:
   exact model, high/xhigh availability, refresh-stable draft, successful
   read-back and the next authorized turn. Preserve existing roster selections.
   Then continue the previously required bridge-cluster verification gate:
   successful services activation, legacy PHP availability, new React/BFF
   health, correct origins, separate-client OAuth callback and refresh flow.
   A healthy Codex/catalog or built WebUI package does not establish live cluster
   readiness. No cluster reset, secret rotation or local-mode expansion follows.

### Preflight concerns and recovery

Workspace `bin/check-dev-workspace-deployment:28-35` requires
exact generic runtime equality, so workspace `41c648c…` versus configuration
`ec05cb9…` fails that existing check. This blocks that helper, not confctl
deployment itself: the configuration does not invoke it, and the workspace
flake check exercises it on fixtures rather than these two real checkouts.
Source comparison found no differences under generic `nix/` between those
exact revisions, including the consumed `nix/host-module.nix` and its imported
`nix/host-paths.nix`. The host boundary is unchanged despite unequal complete
runtime revisions. Record the helper as a known failing exact-equality check;
validate site identity, socket/proxy/TLS/auth contracts in the actual host
evaluation, dry activation and live checks. Do not bump configuration
`devWorkspace` or weaken the helper merely to silence this limitation.

Generic `libexec/workspace-host:582-665` uses the initiating helper's package
Codex for registration probes/final marker comparison, while candidate
activation adopts the candidate package Codex. `marker_has_semantics?` compares
the exact binary path. A cross-version normal switch therefore has a source-level
risk of reporting failure after selecting/activating the candidate. This was
not reproduced live. Inspection of the installed package
`/nix/store/8s0kg785hmz72law9psk19y8a2rig7gb-dev-workspace-0.2.0` followed the
outer Nix wrapper into `libexec/.workspace-host-wrapped` and confirmed the same
relevant dispatch/switch/reconciliation logic. Generic `41c648c…` source uses
that logic too; the final lock-only candidate must retain it. The explicit entry,
`nix run .#workspace-host -- switch --source "$PWD" --from-candidate`, is the
planned route: it makes the initiating and activated package identical.

The source proof is:

- Dispatch at `libexec/workspace-host:417-422` enters the candidate path only
  for `switch --from-candidate`. `with_candidate_generation_lock:2656-2664`
  requires a valid installed profile and unchanged profile token under the
  normal exclusive transition lock. The candidate must equal the single
  package built from `--source` and must still be unselected (`603-607`).
- Candidate journal preflight remains mandatory (`607`, `1913-1955`): lifecycle,
  unfinished creation, portal-managed creation, fork/start and agent-registration
  migration records block it. Cluster and runtime-authority checks follow.
  Candidate `check-codex` validates the currently active binary and its own
  target binary; `probe_registration_plans!` tests candidate argv/capacity
  against target Codex before profile selection (`609-618`).
- Quiescing and preselection failure restoration use the selected predecessor's
  session helper (`1877-1910`), preserving its generation authority. Candidate
  activation adopts target Codex, restarts consumers, and checks exact binary
  path plus registration digest/inventory (`1758-1815`). The initiator now
  expects that same target at the final marker check (`655`); no old/new binary
  mismatch is introduced by this route.

Before activation, run the existing disposable Ruby candidate-switch fixtures
in the repository Nix environment:
`ruby test/workspace_host/profile_transition_test.rb -n '/candidate_switch/'`.
They cover exact-source success with a ready expanded team, source mismatch,
missing installed profile, unfinished creation, and predecessor restoration on
prepublication failure. The package's full tests cover the other transition
failure cases. These fixture checks do not replace real target schema/startup,
registration-argv, model/effort and account-state checks; actual selection and
service adoption can only be accepted after the live switch. The architect
inspected these tests and source without running a transition or test suite.
GO for this existing route after all preceding gates pass; otherwise NO-GO
and report the specific failure before considering a runtime code correction.
Do not introduce an environment override or bypass a refusal.
An older archive-recovery helper is
explicitly tied to 0.155.0; unfinished lifecycle work requires its authorized
recovery path, not an opportunistic upgrade or newly initiated archival.

Before profile publication, preserve the working selected profile on failure
and retry the same candidate command after the refusal is resolved. A busy
session may leave a pending target; do not replace or delete it manually.
After publication/adoption, a failure may leave the new profile selected and
reconciliation pending. The candidate flag now deliberately refuses because
its package is selected. Inspect the retained transition evidence, then use
the installed `workspace-host switch --source <same-feature-source>` to retry
from the selected candidate, or build a newer compatible recovery package.
Use ordinary selected-generation reconciliation or session sync only for the
specific recovery state reported by that operation; never call private helpers.
`workspace-host rollback` remains refused. Never point the active Codex root
back to an older binary or assume it can consume newly written account state.
If system deployment needs recovery, assess the previous NixOS generation's
host-module and account-state compatibility separately; a system rollback does
not roll back the user-profile package, and returning to system 0.158.0 would
remove the demonstrated exact-model support. Prefer a corrected forward host
build when those conditions are not proven. Retain compatible API/schema and
WebUI credentials/BFF state during any independent cluster recovery.

The architect performed source/lock/version and supplied-log inspection plus
this design update. The isolated catalog proof and explicitly attributed lead
live evidence above are complete. Earlier package/deployment steps describe
their original gates; current execution status belongs in the lead's session
state. The listed live cluster service/OAuth checks have passed. Shared DNS
publication remains pending approval, followed by normal host/VPN resolution
and browser reachability checks.

## Lead decisions and handoff

The lead accepted the original three-repository edit boundary, forward-only
portal recovery and separate private WebUI backend, then authorized preparation
of the bounded fourth-repository DNS candidate above. Publication to its four
shared consumers remains pending exact-target user approval. The snapshot
quotas above are
concrete initial implementation bounds; material changes go through the lead.
Current inspection found no requirement to edit codex-web or vpsadmin.
The lead's completed API/WebUI/OAuth evidence is recorded in section 6; it does
not supply shared-DNS deployment authority or normal hostname resolution proof.
Local WebUI enablement has the routing blocker described in section 6
and requires a lead decision before expanding network scope. Bridge deployment
is the required supported path. This brief requests no lifecycle action and
creates no application commit.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-30-portal-review-improvements/
