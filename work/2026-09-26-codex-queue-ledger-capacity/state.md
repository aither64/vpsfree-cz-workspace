---
lifecycle: active
---

# Codex submission-ledger capacity

Initial tracking was committed as `173de66`. The exact session has started at
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-26-codex-queue-ledger-capacity/>.
Ready, awaiting merge approval. The complete implementation and package pin
chain are committed and pushed; mandatory full-change review found one issue,
now remediated. All four full Nix checks and exact-head CI passed. The
user-profile workspace package is deployed, and the storage-session team
assignment smoke test passed. The shared
checkout has extensive unrelated changes; stage only this initiative's owned
paths.

## Next actions

1. Obtain explicit repository/target approval before integrating either this
   initiative or the older Team-settings feature branches. Do not merge merely
   because this deployment passed.
2. Preserve the live schema-3 ledger. Older 1 MiB binaries cannot read it
   after future growth beyond that bound; recover with this or a newer fixed
   package, never by truncating or deleting the active file.

## Worktrees and team

- `worktrees/2026-09-26-codex-queue-ledger-capacity/codex-web`: new branch
  from `01e7579`.
- `worktrees/2026-09-26-codex-queue-ledger-capacity/dev-workspace`: new branch
  from deployed Team-settings head `9e97536`.
- `worktrees/2026-09-26-codex-queue-ledger-capacity/vpsfree-dev-workspace`:
  new branch from `1a022c2`.
- `worktrees/2026-09-26-codex-queue-ledger-capacity/workspace`: new branch
  from `ff0cc0a`.
- The retained `delegated` roster has ready `architect0` (design,
  workspace-write), `implementer0` (implementation, workspace-write), and
  `reviewer0` (review, read-only), all Sol/xhigh. A direct assignment would
  use the failing ledger path while it is nearly full, so bounded native
  Sol/xhigh implementation subagents are handling the two independent source
  areas until that path is repaired. The retained reviewer cannot receive a
  pre-deployment assignment through the full ledger. Mandatory review will
  therefore use the installed catalog's fresh standalone Sol/xhigh reviewer
  fallback before long tests and deployment.

## Baseline

- Generic `dev-workspace` pins `codex-web` `01e75798654b` in `flake.nix` and
  `portal/go.mod`; the installed user-profile package is
  `/nix/store/rvnahc2nfixg7v2brzm04v6cfri2ibaz-dev-workspace-0.2.0`.
- Prior Team-settings heads are unmerged: generic `9e97536`, extension
  `1a022c2`, workspace `ff0cc0a`. New downstream branches will stack on them
  to preserve currently deployed behavior without changing those initiatives.
- The active ledger was 1,048,127 bytes. Only aggregate counts and sizes were
  inspected; no messages, IDs, digests, or raw JSON were output.

## Committed feature heads and quick verification

- `codex-web` `e92dd887c888d5a9f50c70febc714f875cb44378`:
  16 MiB bound, selective accepted-send options compaction, retired-thread
  cleanup, tests/reference. Focused and full `CGO_ENABLED=0 go test ./...`
  passed. Pushed to the initiative branch.
- Generic `dev-workspace` `3b570f0a8b75d809a2753177590158e9dc4639f1`:
  team runtime and lifecycle commit `df36807`, exact codex-web Go/Nix/vendor
  pin commit `b7f457a`, review remediation `3b570f0`. Focused teamruntime
  tests, portal command compile check, and `nix flake check --no-build`
  passed. Pushed.
- `vpsfree-dev-workspace` `47d9d93cc2373f010a3e6963f76b1cb57bbc1240`:
  exact generic pin; `nix flake check --no-build` passed. Pushed.
- Workspace `179ee440d693f2f6481bfa89bef2dff7b00bfee7`:
  exact extension pin; `nix flake check --no-build` passed. Pushed.
- The normal generic `nix develop` bootstrap failed while Go and Nix pins were
  temporarily inconsistent. The dependency sum was generated with Nix Go
  1.25, and a fresh Luna/low watcher obtained the vendor hash via the
  documented fake-hash build. The expected hash-discovery failure is logged
  at `/tmp/queue-ledger-workspace-portal.JG9JwF/build.log`.
- Review packet: `work/2026-09-26-codex-queue-ledger-capacity/review-packet.md`.
  Overall risk High; general, architecture, scope, and risk lanes. The ready
  retained reviewer could not be assigned before deployment because the
  installed ledger was full, so the installed catalog's fresh standalone
  Sol/xhigh reviewer performed the complete review. It found one Blocking
  risk: an already-archived member could bypass the unresolved-attempt gate
  before new cleanup erased retry markers. The generic implementer is adding
  a narrow fail-closed gate and regression test before long checks. No other
  distinct finding was reported; exact pins, commit split, and deleted-fresh
  member proof were accepted. The generic remediation `3b570f0` now refuses
  ordinary cleanup for archived and already-terminal members while their
  submission attempts remain unresolved; it adds four regression paths and
  passed focused checks. The deliberate forced-retirement path still permits
  discard. A narrow direct remediation does not require a full review rerun
  under the review skill. The resolved check and cleanup are separate ledger
  transactions, but team operations are serialized by the runtime lock and
  retired member threads do not receive ordinary new team assignments.

## Final verification and rollout

- A fresh Luna/low watcher ran `nix flake check --print-build-logs` at all four
  final heads. All passed: codex-web, generic runtime, extension, and workspace.
  Logs: `/tmp/ledger-final-package-checks/{codex-web,dev-workspace,vpsfree-dev-workspace,workspace}.log`.
- Exact-head GitHub Actions `Check` passed: codex-web run `36240362601`,
  generic runtime run `36241479372`, and extension run `36241554760`.
  The workspace branch has no matching GitHub Actions workflow.
- The first `workspace-host switch --source <workspace worktree>` failed after
  its unrooted Nix output disappeared between preflight and `nix-env --set`.
  The previous profile and portal remained active; its auto-archive timer was
  restored. A dedicated Luna/low watcher built the exact package path
  `/nix/store/h2xr6mb86jykzilm9qg0l941hbgd4dfq-dev-workspace-0.2.0`
  (`/tmp/ledger-deployment-package-build.log`), and an explicit temporary
  out-link held it during the retry. The second switch succeeded. The profile
  now roots that package, the temporary out-link was removed, and the portal
  service and auto-archive timer are active. The switch emitted warnings about
  unrelated legacy worktree registration; no affected worktree was changed.
- `dev-session team assign 2026-09-23-storage-redesign --as-is --to reviewer0`
  accepted one harmless smoke-test message. A read-only Codex transcript check
  counted exactly one matching user-message entry and one completed reply.
  Repeating the same client message ID returned the identical turn receipt;
  the transcript still contained exactly one matching message. No ledger
  contents were output. The ledger changed from 1,048,127 bytes (mode 0600)
  to 363,418 bytes (mode 0600) through bounded accepted-team compaction.
- The public portal returned 401 to an unauthenticated curl request, as
  expected; local `workspace-portal@vpsfree-cz.service` is active. This shell
  lacks the internal CA, so certificate-verified curl could not assess the
  portal directly. The command-level assignment and transcript check verify
  the repaired workflow without browser authentication.
- The temporary package-build failure and retry lesson is recorded at
  `notes/dev-workspace/2026-09-26-unrooted-switch-output.md`. Lasting
  compaction and cleanup semantics are in the owning codex-web and generic
  dev-workspace documentation. No default-branch feature integration or
  configuration pin change was performed.
