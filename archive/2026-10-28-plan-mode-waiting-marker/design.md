# Plan mode waiting marker: bounded design

Architect0, 2026-10-29. Investigation and design only; no application edits or
runtime reproduction performed. Lead accepted the existing-recorder direction;
implementation assignment, tracking commits and publication remain with lead.

## Scope and root cause

Restore the existing `?` document-title attention marker for an unseen blocking
Plan-mode `request_user_input`. Preserve focused-visit acknowledgement, optional
questions, approval handling, completion markers and reservation prefixes.

Inspected canonical cached `origin/master` revisions (not stale bare `HEAD`):

- codex-web: `f6f4a187509b3bebfc81585c535be856eaab0d04`.
- dev-workspace: `cc0d452a0653a112c8a013492c1734d9554bb909`, which pins that
  codex-web revision. Lead must fetch/check the actual feature bases before work.

The broken path is established directly by code:

1. `dev-workspace/portal/internal/web/activity.go:76` constructs the activity
   client with `ObserverOnly: true` and an `ActivityRecorder`.
2. `codex-web/codex/client.go:1327–1343` records native requests for activity,
   then broadcasts and discards them for observer clients before `admitPrompt`.
   Thus activity can correctly report `waiting` / `userInput`, but the observer
   has no interactive `Prompts()`. Tests explicitly require this separation:
   `TestObserverNeverAnswersSupportedOrUnsupportedRequests` and
   `TestObserverListQueueStaysReadOnly`.
3. `dev-workspace/portal/internal/web/attention.go:223` nevertheless obtains
   request identity from that observer's `Prompts()`. Its empty list prevents
   the input attention event.
4. `static/session-attention.js` already renders an unseen input event as `?`
   from `/api/sessions/<slug>/attention`. It intentionally acknowledges an
   observed event on a visible, focused visit. `static/app.js`'s waiting dot is
   a separate display and is not the missing document-title boundary.

The notification test currently substitutes an observer fixture that returns
interactive prompts, masking the production mismatch. Correcting the shared
attention source also restores its existing notification behavior; no new
notification controls or delivery policy are needed.

## Interface and smallest fix

Reuse `ActivityRecorder`'s existing bounded `activityObservation.Requests` map.
It already tracks native request IDs, turn IDs, blocking/category information,
resolution, terminal cleanup and connection coverage. Add optional native
`itemId` and `method` fields to `activityRequest`; copy these scalar identities
from the already consumed request message. Do not retain the request body.

Add `ActivitySnapshot.BlockingRequests` (`blockingRequests,omitempty`), containing
identity-only entries with `TurnID`, `ItemID`, `Method` and `Kind` (`userInput` or
`approval`). The enclosing snapshot supplies `ThreadID`. Populate it from the
same durable, connected current observation used for `CurrentState` and
`WaitReason`; use stable ordering. Export only supported blocking requests with
complete identity for the current in-progress turn and a classified waiting
state. No tokens, question text, answers, commands or response authority.

Change `observeAttention` to consume that snapshot projection, preserving its
existing freshness, exact-thread, eligibility and wait-reason gates. Keep the
event key exactly `attentionDigest(thread, turn, item, method)` and the current
kind mapping and reduction rules. Remove its `Prompts()` interface dependency.
The browser title renderer and acknowledgement store require no production edit.

An unextended snapshot cannot suffice: `waitReason` identifies a category, while
`stateSinceMs` and turn identity cannot reliably distinguish successive or
concurrent native requests. Synthesizing identities would break acknowledgement
and deduplication. Native request notifications already enter the recorder, so
there is no reason for a second registry, a new observer API or an interactive
client dependency. Exposing interactive prompts would violate observer policy.

## One complete implementer package

One implementer owns these dependent changes serially:

- **codex-web:** `codex/activity.go`, `codex/activity_recording.go`,
  `codex/activity_snapshot.go`; focused cases in `codex/activity_test.go` and
  `codex/activity_storage_test.go`; extend the existing real observer transport
  test as needed. Document the additive projection and checkpoint compatibility
  in the activity section of `docs/reference.md`.
- **dev-workspace:** `portal/internal/web/attention.go`, regression cases in
  `attention_test.go` / `notifications_test.go`, and a concise explanation in
  `docs/browser-notifications.md` of the passive identity source. Use the
  existing `attention_browser_test.cjs` harness for input, acknowledgement and
  resolution; add a focused transition case only where coverage is missing.
- After the codex-web feature commit is published under lead coordination,
  update its exact pin in dev-workspace `flake.nix`, generated `flake.lock`,
  `portal/go.mod`, `portal/go.sum`, and `nix/workspace-portal.nix`'s `vendorHash`.
  Preserve unrelated dependencies. No Codex release, extension, configuration
  or coordination-workspace feature change belongs in this package.

## Invariants and compatibility

- `ObserverOnly` never answers, rejects unsupported requests, auto-resolves,
  creates response tokens, applies settings or retains interactive prompts.
- Resolution by any client, completed/failed/interrupted turns, disconnect,
  stale coverage and reconnect must not expose obsolete request identities.
  Reuse recorder cleanup and generation checks; do not reconstruct pending
  requests from transcript text or restore old connection authority.
- Acknowledgement clears the marker without answering. A distinct subsequent
  request has a distinct event; repeated observations do not re-alert. Optional
  input, sleep, team waits, unknown activity and terminal failures do not become
  input or successful-completion events.
- Keep existing request-count and checkpoint-byte bounds. Missing identity
  means no projected request, never an invented key or invalid old checkpoint.
- No database migration or version bump. The two optional checkpoint fields
  are additive within schema 1; existing `json.Unmarshal` readers ignore them.
  New readers accept old records with absent fields and retain timing totals.
  Old writers may drop identity fields without corrupting timing state. Native
  replay/fresh observation restores identity on the current connection.
- The HTTP activity addition is optional and compatible with old browser code.
  New portal source requires the pinned new codex-web library at build time;
  old portal code remains source-compatible with the library. Attention events,
  IndexedDB, notifications, session manifests, native RPCs and Codex versions
  keep their existing formats. No coordinated fleet or node upgrade.

## Acceptance and verification

Required regression: a real passive client receives a native blocking Plan
question and produces the identity-bearing activity snapshot while `Prompts()`
stays empty and no response is written. Feed that contract through the portal
attention reducer/API to an unseen input event; the existing browser harness
must render `?`, clear it on acknowledgement/resolution, and preserve `R`.
Do not rely solely on a fixture that manufactures answerable observer prompts.

Cover omitted `isBlocking` (defaults to blocking), explicit false, approvals,
duplicate observation, a second question in the same turn, resolution,
terminal cleanup, disconnect/reconnect, missing historical identity and stale
snapshots. Check old/new schema-1 decoding and absence of prompt text in stored
records. Reuse existing cases instead of duplicating unaffected behavior.

Quick commands, using each repository's Nix environment:

- codex-web: `go test ./codex -run 'Test(Activity|Observer)'`.
  Its flake has no dev shell; use its pinned toolchain/package environment.
- dev-workspace, from `portal/`:
  `go test -mod=readonly ./internal/web -run 'Test(Attention|Notifications)'`;
  `node --test internal/web/attention_browser_test.cjs`.
- Check formatting, `git diff --check`, coherent exact dependency pins, and
  applicable declared hooks. Record commands, exact tested heads and results.

After quick checks and committed-deliverable independent review, run each
repository's `nix flake check --print-build-logs` and applicable branch CI.
Long/uncertain checks use a fresh verification watcher. A full live deployment
or broad new browser system is unnecessary to establish this bounded contract.
Any later authorized deployment should verify one background-tab Plan question,
answer/continuation and focus acknowledgement against the actual paired package.

## Deployment and recovery

No deployment or integration is authorized here. Delivery is two reviewed
feature branches with the downstream pin selecting the exact upstream head.
If later authorized, build the paired dev-workspace package before its ordinary
coordinated user-profile activation; no system configuration change is implied.
Follow the selected package's coordination guide and preserve conversation
continuity. The package switch is forward-only: recover using a compatible
successor package, not a profile rollback. The additive metadata needs no state
repair or discard; reverting the behavior in a successor restores the old
missing-marker limitation without changing conversation or timing data.

## Deployment addendum: aitherdev

The user subsequently said, "aitherdev can be deployed using
vpsfree-cz-configuration". Lead is preparing that rollout after review/checks;
integration remains a separate approval. This addendum supersedes the earlier
no-deployment scope statement without changing the implemented source design.
Exact actions, heads, outputs and ownership belong in [rollout.md](rollout.md).

Authoritative sources read: workspace deployment procedure and coordination
guide; full selected `workspace-host coordination guide`; configuration
`AGENTS.md`, `docs/operations/codex-providers-aitherdev.md`,
`codex-deepseek-aitherdev.md` and `aitherdev-disk-retention.md`; configuration
channel/host wiring and the pinned confctl command reference. This is a portal
fix, not a Codex/provider upgrade, so provider-switch and model-request upgrade
checks do not enter scope.

### Composition and implementer1 package

Investigated configuration `origin/master` is
`584691d9b96ce1555a5787a0a1d999eeb528811f`; workspace HEAD is
`1085b570dc27d7250faa94ae893f9f8ffd04c45c`. Recheck actual fetched bases.
Both currently select generic runtime `cc0d452a0653a112c8a013492c1734d9554bb909`.
The workspace extension is `767dfd587e346168e1443e65ccdb67ce748f3fe3`.
The source-review candidate runtime is
`5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3`, containing codex-web
`9d337b70987fdf1dd42a5d8efff31f755a122550`; use the final reviewed published
runtime if review changes it, and consolidate intermediate pin updates.

Implementer1 owns only two dedicated session feature worktrees:

1. `vpsfree-cz-configuration`: inspect `confctl inputs channel ls`, then run
   `confctl inputs channel set --commit dev-workspace devWorkspace RUNTIME_SHA`
   in its Nix development shell. The role maps to flake input `devWorkspace`.
   Keep generated commit text and lock changes; no host-definition edits.
2. `workspace`: change only the direct nested runtime URL under
   `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` in `flake.nix`, then
   generate the lock with `nix flake update vpsfree-dev-workspace/dev-workspace`.
   Preserve the extension revision/content hash, follows paths, native Codex,
   llm-agents and unrelated inputs. No extension-source change or new runtime
   input. Shared master is not an implementation checkout.

The workspace composes the extension, site configuration, team policy and
coordination catalog into the user-profile package. Configuration imports the
runtime's `nixosModules.host` and uses its Codex packaging helper; it does not
install the portal application. `cluster/cz.vpsfree/machines/aitherdev/module.nix`
selects the channel and targets `172.16.106.40`.

Before commit/publication, perform semantic input-graph inspection, formatting,
`git diff --check`, declared hooks and the composed checker:

```sh
bin/check-dev-workspace-deployment \
  --workspace-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-plan-mode-waiting-marker/workspace \
  --configuration-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-plan-mode-waiting-marker/vpsfree-cz-configuration
```

Retain complete resolved input identities, exact bases/final heads and any
read-only derivation comparison. Source branches remain under their ongoing
independent review; pin preparation cannot certify that review. This assignment
permits quick checks, commits/publication and read-only comparison, not builds,
claims or activation. Return the two clean heads and checker evidence to lead.

### Lead-owned build, comparison and activation

After applicable review gates, a fresh verification watcher builds the exact
committed composed workspace package with `nix build .#default --no-link
--print-out-paths`, and configuration with
`nix develop -c confctl build cz.vpsfree/machines/aitherdev`. Preserve the package
output and confctl generation name, `toplevel`, `auto_rollback` and input metadata.
These builds and supported closure copies precede machine ownership. Stop an
unexpected local kernel build under the workspace verification procedure.

Read-only comparisons after preparation:

```sh
readlink -f /run/current-system
readlink -f /nix/var/nix/profiles/system
nix develop -c confctl generation ls cz.vpsfree/machines/aitherdev
nix store diff-closures CURRENT_SYSTEM CANDIDATE_SYSTEM
workspace-host status
```

During design, both live and persisted system links resolved to
`/nix/store/fczhh0f76j8sy2awv7skrv2rp59vr7lg-nixos-system-aitherdev-26.05.20261026.718f670`.
This is an observation, not an activation precondition valid indefinitely.
Recheck both immediately before action. The operations guide explicitly permits
application-only activation: if the candidate system output equals both current
links, record that proof and omit system activation. Do not infer equality from
version strings or a small source diff. Otherwise inspect the system difference
and use the reviewed configuration path first.

The selected package at design time is
`/nix/store/d0wikyzpr7qk1w2c2zbqgj97qz1m58qn-dev-workspace-0.2.0`.
Its catalog maps `aitherdev`, `aitherdev.int.vpsfree.cz` and
`cz.vpsfree/machines/aitherdev` to the one machine `vpsfree:aitherdev`, which is
also `profileMachine`. Acquire one machine-only claim near activation; a waiting
claim owns nothing. Inspect authoritative status for the exact session/claim
before acting. No repository claim is needed for preparation or deployment.

If system activation is required, pin the prepared generation explicitly:

```sh
confctl deploy --generation GENERATION --copy-only cz.vpsfree/machines/aitherdev
confctl deploy --generation GENERATION cz.vpsfree/machines/aitherdev dry-activate
confctl deploy --generation GENERATION cz.vpsfree/machines/aitherdev switch
```

Copy can precede the claim; dry activation and switch require it. Run through
the configuration Nix shell, preserve configured auto-rollback, and do not reboot.
Verify both system links and health before the dependent profile selection.
The ordinary selected command owns profile compatibility and recovery:

```sh
DEV_SESSION_SLUG=2026-10-28-plan-mode-waiting-marker \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
DEV_WORKSPACE_CLAIM_ID=CLAIM_UUID \
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-plan-mode-waiting-marker/workspace
```

Reconcile any unfinished transition before retry; never force a daemon restart
around a refusal. Verify selected package path, portal health and conversation
continuity, then the requested background-tab blocking question marker,
answer/resolution and focused acknowledgement. Use disposable authorized test
state for synthetic activity; do not modify another session to manufacture it.

### Recovery, evidence and release

Preserve system generations, package/Codex roots and private journals. A failed
or uncertain activation keeps ownership while its actual effects are reconciled;
compare both system links because live activation can precede failed profile
publication. Keep configured system auto-rollback. Workspace package recovery
is forward-only through the original supported retry or a compatible successor;
do not delete state or roll the application profile backward.

Record the full workspace/configuration/runtime/codex-web source and input graph,
exact deployed system/profile paths, canonical remotes/targets and machine alias
mapping in rollout.md. Integration approval must separately cover each affected
repository/target. Once deployment/effects are verified and complete deployed
feature lineage is proven integrated in approved remote defaults, promptly
release the exact session-owned machine claim and verify its released state.
Missing integration evidence keeps the machine held. Rebased nonancestor heads
need independently reviewed equivalence and migration evidence; a substantive
successor requires a new verified deployment. Release grants no lifecycle
permission; retain this session open.
