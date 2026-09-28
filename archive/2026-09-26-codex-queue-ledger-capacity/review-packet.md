# Submission-ledger capacity review packet

Review the complete committed cross-project change for general, architecture,
scope/proportionality, and risk/compatibility concerns. Risk is **High**:
private persisted retry state, destructive per-thread cleanup, a new public Go
client API, package deployment order, and inability of older readers to load
files over 1 MiB. Do not edit files. Report findings ordered by severity with
file/line and commit references, or explicitly state none.

## Outcome and boundaries

`dev-session team assign` must work without deleting/truncating the active
ledger. The fixed client must read/write a bounded 16 MiB schema-3 ledger,
compact only accepted team-send original options while preserving retry
identity, and clear member attempts only after proven thread retirement.
Preserve atomic replacement, private permissions, and lock serialization.

Non-goals: App Server protocol changes, schema migration, browser-send
compaction, clearing active/uncertain attempts, automatic default-branch
integration, configuration master changes, and support for rolling back to an
older binary after the ledger grows beyond 1 MiB. The workspace host package
transition is already forward-only; an older binary cannot read such a file.

The active ledger was 1,048,127 bytes before implementation. Private aggregate
inspection found 1,193 accepted `team:` sends and no pending sends; about
680 KiB was stored original turn options. No contents or identities were
printed, and the live ledger was not changed.

## Initiative and revisions

- Slug: `2026-09-26-codex-queue-ledger-capacity`.
- Plan/state: `work/2026-09-26-codex-queue-ledger-capacity/{plan,state}.md`.
- `codex-web`: worktree `worktrees/<slug>/codex-web`, base
  `01e75798654b5c56535646dea687468a358408fb`, head
  `e92dd887c888d5a9f50c70febc714f875cb44378`. One focused client
  behavior/test/reference commit; tests and docs describe that behavior.
- Generic `dev-workspace`: worktree `worktrees/<slug>/dev-workspace`, base
  `9e97536842bb3d21f9955494ad96ed7016a446f2`, head
  `b7f457a90ac9751bf7c7a4486541f8d7b2ec5a51`. Code/docs/tests commit
  `df36807`, separate Go/Nix module and vendor-hash pin commit `b7f457a`.
- `vpsfree-dev-workspace`: worktree `worktrees/<slug>/vpsfree-dev-workspace`,
  base `1a022c213ff38819c1b96531fb727fdc83ab0483`, head
  `e9bb8b5cb7a6d19c6fde71b0bb0e925f6eeff4ed`. Exact generic pin only.
- Workspace: worktree `worktrees/<slug>/workspace`, base
  `ff0cc0ab4755d1b900b362e1eae5b5249c73718d`, head
  `2be7eee0d4d98a0f2a9bf994b0942fc9cb85917f`. Exact extension pin only.

Downstream bases are the deployed, unmerged Team-settings feature heads to
avoid regressing their functionality. This is a stacked new initiative, not
permission to merge the earlier or new work. Canonical provider is
`aither64/codex-web`: its new APIs are
`CompactAcceptedSendOptions(contextPrefix string) error` and
`ClearRetiredThreadAttempts(threadID string) error`. The demonstrated consumer
is generic `aither64/dev-workspace` teamruntime; it pins the provider in both
`portal/go.mod` and `flake.nix`, with Nix verifying the match. The vpsFree
extension and workspace then pin the generic package in one direction. Other
codex-web consumers are not changed; review whether the public API contract
and non-team preservation are safe for them.

## Evidence and documentation

- `codex-web`: focused ledger tests and `CGO_ENABLED=0 go test ./...` passed.
- Generic: focused teamruntime tests and portal command compile check passed
  with Nix Go 1.25. `nix flake check --no-build` passed after the exact pin.
- Extension and workspace: each `nix flake check --no-build` passed. All
  committed diffs passed `git diff --check`.
- Long package checks and live deployment have **not** begun; review precedes
  them. A Luna watcher derived the real vendor hash from an expected fake-hash
  mismatch, not a successful package build.
- Lasting contracts are documented in `codex-web/docs/reference.md` and
  generic `dev-workspace/docs/workspace-portal.md`; exact rollout decisions
  and evidence belong in this initiative's plan/state.

Reviewer selection: ready `reviewer0` is saved Sol/xhigh/read-only but cannot
be assigned through the installed ledger at its current size. Per the
mandatory review skill, use one fresh standalone reviewer from the installed
default development team's `reviewer` role (Sol/xhigh/read-only). No reviewer
authored these changes. The selected reviewer must read the skill and all four
lane references directly and perform the review without nested agents.

## Review result and final follow-up heads

The standalone Sol/xhigh reviewer completed all four lanes. It found one
Blocking retirement-retry path: an already-archived member could skip the
unresolved-attempt gate and have its submission markers cleared. Generic
`dev-workspace` commit `3b570f0a8b75d809a2753177590158e9dc4639f1`
adds a fail-closed check for ordinary retirement, including already-terminal
members; focused tests cover refusal, resolution, and same-ID retry. The
deliberate forced-retirement discard behavior remains separate. This is a
direct, narrow remediation, so the review procedure does not require rerunning
the entire review. No other distinct finding was reported.

The final generic head is `3b570f0a8b75d809a2753177590158e9dc4639f1`;
the extension pin head is `47d9d93cc2373f010a3e6963f76b1cb57bbc1240`;
the workspace pin head is `179ee440d693f2f6481bfa89bef2dff7b00bfee7`.
They are pushed to their feature branches. The original revision list above
records the exact pre-review packet reviewed, not the final follow-up heads.
