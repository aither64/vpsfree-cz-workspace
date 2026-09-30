# Portal review improvements: design and verification brief

Status: completed implementation brief. The lead accepted the repository,
forward-only recovery and separate WebUI backend boundaries. This document
records design, not implementation or deployment evidence.
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

The lead owns plan/state/portal artifacts and implementation assignments; the
implementer owns application changes. This architect edits only this document
and any separately assigned coordination prototype. A consequential departure
from these boundaries goes through the lead. No vpsAdmin API/schema, PHP product
behavior, generated clients, Terraform provider, node protocol, production host,
KB content, or vpsAdminOS change is required. No coordinated node upgrade is
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
legacy services. In a disposable API fixture, seed twice and assert one stable
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
suppression and credential failure in isolated fixtures. A live cluster probe
and authenticated flow remain required before readiness.

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

For a cluster service failure, retain previous successful VM build/result and
the new credential/session state. Recover through the supported services update
with a known-good matching frontend/BFF pair or a new config disabling only the
React service, while retaining its state for later recovery. Confirm the runner's
partial-update report before repeating. Do not reset the cluster, delete the
OAuth client, rotate secrets, or touch another session to recover the PHP UI.
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
   Preserve the clean-filter regression proof: in a disposable fixture, use
   `ls-files -m`, `diff-files --name-only` and `status --porcelain` as positive
   controls for the hostile filter despite disabled global attributes and
   fsmonitor. Then assert the actual snapshot reader's stage/debug plus
   no-follow stat discovery, capture and revalidation never execute it.
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

## Lead decisions and handoff

The lead accepted the three-repository edit boundary, forward-only portal
recovery and separate private WebUI backend. The snapshot quotas above are
concrete initial implementation bounds; material changes go through the lead.
Current inspection found no requirement to edit codex-web or vpsadmin.
Remaining verification uncertainties are real App Server read-after-update
behavior and the live selected API/WebUI flow. Source proof establishes the
CORS/OAuth contracts; enabled packaged smoke coverage still needs the compatible
API input. Local WebUI enablement has the routing blocker described in section 6
and requires a lead decision before expanding network scope. Bridge deployment
is the required supported path. This brief requests no lifecycle action and
creates no application commit.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-30-portal-review-improvements/
