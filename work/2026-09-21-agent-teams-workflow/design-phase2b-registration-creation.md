# Phase 2B registration and creation design

## Scope and implementation order

Phase 2B activates managed policy only for new sessions and plan-to-new-session
creation. It owns startup registration, immutable package retention, initial
state publication and the first real turn.

Implementation is split into three generic commits so every intermediate
revision remains coherent:

1. dormant Go contracts and commands: binding resolution, retained publication
   and registration planning;
2. host registration and package-transition integration, still without a UI or
   accepted managed creation path; and
3. portal/CLI creation, recovery, evidence and UI activation after registration
   support exists.

`codex-web` needs no Phase 2B change. Organization and site repositories receive
exact dependency-pin updates only after the generic implementation is reviewed
and its packaged suite passes.

Phase 2B does not implement ordinary managed sends, team transitions, member
observation or lifecycle release/adoption. Managed-source forks, explicit team
selection on forks, and managed archive/revive/delete/auto-archive fail closed
until Phase 2D. Ordinary finish and handoff remain unchanged. These temporary
blockers must not be deployed without the later lifecycle slice.

## Ownership

Generic `dev-workspace` owns all behavior:

- `portal/internal/agentteams/`: creation binding/resolver, initial-state and
  turn-option construction, registration plan, Nix retainer and retained store
  creation;
- `portal/cmd/workspace-portal/main.go`: bounded helper commands for creation
  resolution/publication, registration and transition preflight;
- `portal/internal/web/`, templates and browser assets: server-owned catalog
  page data, team selection and lead overrides;
- `libexec/dev-session` and `libexec/workspace-host`: strict schema-2 lifecycle
  transport, startup argv and profile-transition reconciliation;
- runtime contract, Nix package wiring, focused tests and user documentation.

`vpsfree-dev-workspace` owns only the exact generic pin. The site workspace owns
only the exact extension pin and its existing subjective catalog. Neither layer
duplicates resolver or lifecycle policy.

## Creation binding

`CreationBinding` schema 1 is exact:

```text
schema catalog selection initial_turn_policy
```

`catalog` is the exact Phase 2A `CatalogPin`, `selection` is the existing
schema-1 `Selection` at revision 1, and `initial_turn_policy` is exactly 1. Go
serializes canonical compact JSON into a bounded, self-checking opaque token:
`v1.<base64url-no-pad>.<lower-sha256>`, at most 32 KiB. Ruby validates token
syntax, size, digest equality and transport equality but never decodes policy.

Resolver inputs preserve presence:

- with `teamConfig = null`, omitted team/digest resolves to unmanaged; any
  explicit team or digest is rejected;
- for a managed catalog, omitted team resolves the installed default exactly
  once; explicit empty team or missing digest is rejected;
- explicit selection requires the displayed catalog digest and a known team;
- nonempty model/effort form values become lead-only overrides; empty values
  are absence, not an empty override;
- effort must be allowed by the selected `team_lead`, and the effective
  model/effort must exist in the live model inventory; inactive alternatives
  are not validated for creation.

The token contains no workspace, slug or thread identity. Publication supplies
the canonical workspace, slug, completed-removal digest, 64-hex creation/tmux
identity and actual root thread ID. It creates state revision 1 and selection
revision 1 with nil pending/dispatch and nonnil empty member/history arrays.

Managed initial-turn options are always reconstructed from the published state
and pinned catalog. They contain the exact effective model/effort and one
`application` context source named `dev-workspace.agent-team`. Its deterministic
value is at most 4 KiB and contains only schema 1, catalog/team/team digest,
selection revision, lead role and a reminder that staffing policy does not grant
source-change permission. Caller options are never trusted after publication.

## Package retention and atomic publication

The production retainer executes exact argv:

```text
nix-store --add-root ROOT --indirect --realise PACKAGE
```

The installed Nix 2.34.8 accepts `--indirect`; `--realise` documentation confirms
the `--add-root` symlink contract. The package wrapper supplies Nix on `PATH` (or
an explicit immutable binary) and tests inject the command runner.

The root parent is the existing private mode-0700
`Store.rootsDirectory`. No component may be a symlink. The derived indirect root
must be the expected symlink and resolve exactly to the canonical package output.
A wrong target, regular file or wrong namespace fails. Release unlinks only the
exact derived root and fsyncs the parent.

`Store.CreateRetained(ctx, state, retainer)` runs below the existing per-slug
lock:

1. validate state and identity;
2. if exact state already exists, idempotently retain and succeed;
3. reject any differing state without releasing its root;
4. retain the package first, then atomically replace state;
5. on ordinary write failure, release before unlocking and return combined
   errors.

A crash after retain but before rename may leave an operation-owned root. The
still-present creation journal makes the same token retry retain/publish
idempotently and prevents lifecycle cleanup. A lost publication response is
reconciled only by exact state identity, pin and selection equality.

## Strict lifecycle records

Creation request schema 2 adds presence-aware `team` and `catalogDigest`.
Existing `model` and `effort` are deliberate managed lead overrides only.

Managed creation receipt schema 2 stores the opaque binding and its digest.
Schema-1 receipts remain exact, readable and unmanaged. Request, journal,
receipt and evidence decoders branch strictly by schema; unknown fields are not
accepted by weakening a shared decoder.

Public CLI adds `dev-session start ... --team TEAM`. Private portal transport
uses `--team-binding TOKEN`, mutually exclusive with `--team`. Direct CLI
creation asks packaged Go to resolve the installed default or explicit team,
uses returned effective model/effort operationally, and otherwise treats the
token as opaque. Explicit team selection on an existing, preserved or revived
session fails until adoption exists.

Schema-2 request, `.creation.json` journal and completion evidence carry the
exact binding/digest while retaining current goal, `run_codex`, model, effort,
state and tmux semantics. Publication validates journal effective settings
against the binding. Ready journals may drop tmux identity as today because
state and evidence retain it.

Schema-2 creation proof verifies token digest, evidence thread/creation/catalog
identity, ready manifest and initial goal, plus matching managed state identity
and pin. It must not require the current selection to remain the initial team
after future Phase 2C transitions.

The portal resolves and freezes the binding before accepting a receipt. An exact
request retry returns its earlier receipt/binding even after an installed package
change. A new stale digest returns 409 with refresh guidance; explicit empty or
unknown input returns 400. Resolver failure precedes any worktree/thread effect.

## Ordered creation and recovery

1. Portal or direct CLI resolves the token and effective lead. An accepted
   receipt owns all retries.
2. Under existing transition plus creation/slug locks, Ruby writes strict
   schema-2 request and journal binding before destination effects.
3. Existing recovery creates or reuses the exact root thread with binding-derived
   lead settings, reconciles tmux, and writes creating manifest/runtime authority.
4. After final thread ID, tmux identity and successful slug sync, but before the
   initial turn, Go revalidates the token and identity, retains the pinned
   package, and publishes state.
5. Ruby durably records the existing `initial_goal_attempted` boundary, releases
   the slug lock, and invokes managed `thread ensure-initial`. That path loads
   state by workspace/root/slug/creation/thread identity and calls
   `EnsureInitialMessageWithOptions`; Ruby supplies no managed options.
6. Ruby reacquires/revalidates the exact session, marks goal sent/ready, finishes
   journal/authority and writes schema-2 evidence.

Recovery is fail closed:

- before retain: ordinary journal recovery;
- root retained without state: the same journal/token validates the root and
  publishes state;
- state published but response lost: exact state is success, mismatch is fatal;
- state exists before durable attempt: retry may send once;
- attempt bit exists but the thread remains unmaterialized: do not resend, report
  an explicit recovery blocker because the native initial-turn API has no
  durable request identity;
- exact materialized goal: finish without a second turn;
- different materialized goal: hard conflict.

## Portal behavior

Server page data adds managed status, exact catalog digest, default team and
sorted neutral team rows containing name, description and compact role summary.
Generic UI never embeds site team names or models.

New-session and plan-to-new-session forms show a Starting team selector and
hidden exact digest. The default is preselected. Copy explains that specialists
start on demand and team choice is not edit authorization. Existing model/effort
controls move under an Advanced lead override disclosure; untouched controls
submit empty and are not filled with team defaults.

Managed plan creation does not inherit source model/effort as hidden overrides;
the selected lead is authoritative. Unmanaged behavior retains existing source
model handling. Team, digest and overrides stay in the existing session-storage
draft after validation/stale errors. `teamConfig = null` shows unmanaged status
and retains current model/effort flow. Fork UI exposes no team selector, and
server enforcement is mandatory.

## Startup registration

The registration plan includes the current installed managed catalog and every
retained pinned catalog from active, archived and creation-in-progress state.
Each state is validated against `LoadPinned`, manifest/removal/thread identity
and its GC root. All role variants are registered for later switching; utilities
and Luna are never registered.

Bounds are enforced statically where possible and again over the aggregate plan:

- child capacity 1..64;
- at most 512 managed states;
- at most 64 distinct catalog pins;
- at most 512 unique native role names; and
- total exact config argv payload, including terminating NULs, at most 256 KiB.

For each sorted role, emit two argv entries:

```text
-c
agents.<name>.config_file=<TOML-quoted absolute immutable path>
```

Then emit `-c` and the maximum required
`agents.max_concurrent_threads_per_session=<children>`. Capacity counts children;
Codex accounts for the root separately.

The same generated name from multiple package outputs is deduplicated when its
native identity and exact TOML bytes match; choose a deterministic path. The same
name with different identity or bytes is rejected. Semantic plan digest covers
name, config-content digest and capacity, not the chosen absolute package path.

`workspace-host run-codex` asks packaged Go for JSON argv, writes an owned
mode-0600 runtime marker containing the semantic plan digest, and execs
`active_codex`, config pairs and `app-server --listen` without shell
interpolation or global configuration changes.

Codex reconciliation compares both binary and per-workspace registration-plan
digest. A changed catalog must quiesce/restart consumers even when the binary is
unchanged. The pending reconciliation record is versioned and contains both.
Managed creation compares desired digest with the actual launch marker and
returns 503 while restart is deferred. Unmanaged use remains available. A state
from the current catalog adds no new registration because that catalog was
already included.

## Forward package changes and one-time migration

Aitherdev is the sole deployment and advances forward. There is no
`transition-preflight` compatibility API, old-target capability matrix or
mixed-generation rollback path. Before a package change, quiesce and refuse any
open creation, lifecycle or migration journal. Run the candidate package's
strict registration helper against current durable state and verified roots,
switch the profile, and restart App Server consumers whenever the binary or
semantic registration digest changed. Future schema changes require explicit
offline forward migration.

Existing idle sessions are migrated only after managed ordinary-send support
exists, so migration is not deployed with Phase 2B alone. Under a mode-0600
atomic journal, preserve each materialized session's worktree, slug and root
conversation/thread ID; assign the installed default team with unmodified lead
defaults and no inferred overrides; retain the current package and publish
revision-1 state. Reuse a trusted tmux identity or journal a new 64-hex session
generation. Tracking-only sessions receive no fake state. Stop portal/App Server
while migrating, rerun partial work idempotently, build one final registration
plan, restart once, and verify thread readability without sending inference.

## Verification and rollout

Focused checks before mandatory review:

- Go: `internal/agentteams`, `internal/web`, `cmd/workspace-portal`;
- Ruby: `test/dev_session_test.rb`, `test/workspace_host_test.rb`;
- Node syntax and focused creation browser contracts;
- fake retainer/Nix runner and fake App Server argv/first-turn capture only; no
  paid inference.

The generic implementation is committed in the three coherent slices above,
then reviewed by the retained independent Sol/xhigh reviewer across all
applicable lanes. Every test/build wait uses a fresh Luna/low watcher.

After review, run the generic packaged Nix suite, update and verify the
organization pin, then update and verify the site pin. Deployment order is
generic exact head, organization exact pin, site exact pin, then the aitherdev
user-profile switch. Current-state/root validation runs before activation;
registration reconciliation quiesces/restarts App Server consumers; automated no-inference
smoke covers selector rendering, stale rejection, first-turn protocol fields and
forward-migration recovery. Any real-inference smoke is a separate conscious
step.
