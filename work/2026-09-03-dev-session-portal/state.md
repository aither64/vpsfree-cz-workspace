---
lifecycle: active
---

# 2026-09-03-dev-session-portal

## Repositories

- Coordination workspace: branch `2026-09-03-dev-session-portal` in
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/workspace`
- `vpsfree-cz-configuration`: branch `2026-09-03-dev-session-portal` in
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-03-dev-session-portal/vpsfree-cz-configuration`

## Status

- Portal service, `dev-session` integration, PKI helper, tests, documentation,
  handoff skill, and workspace branch policy are implemented on the dedicated
  workspace feature branch.
- Current Codex thread registered as
  `01a0678c-baae-7600-bcf6-9a0cb6c83232` and named after the initiative.
- Configuration worktree created from `origin/master` at
  `57d7c12a2da78d334d338a0e56dd7438376a6973`.
- Workspace changes are committed and pushed on
  `2026-09-03-dev-session-portal` through `2c9112da`. At the user's direction,
  published `master` was force-reset from `ada6db0` to its pre-initiative
  commit `0d2802f`; no portal implementation remains on `master`.
- Configuration changes are committed and pushed on
  `2026-09-03-dev-session-portal` through `2ba6673d`. The branch has four
  commits on top of current `origin/master`.
- The top-level checkout already contained unrelated changes, including a
  modification to `AGENTS.md`; it remains preserved outside this initiative's
  staged patch.

## Commands run

- `bin/dev-session current`
- `bin/dev-session start dev-session-portal --no-attach --no-codex`
- Read-only inspection of the workspace, Codex CLI/App Server interfaces, and
  current aitherdev/internal-DNS configuration.
- `ruby test/dev_session_test.rb`
- `ruby test/workspace_pki_test.rb`
- `CGO_ENABLED=0 go test ./...`
- `CGO_ENABLED=0 go vet ./...`
- `workspace-portal thread create` and `thread set-name` against the live Unix
  App Server socket.
- Skill validation through a Nix Python environment with PyYAML.
- `confctl inputs channel update --commit workspace-tools vpsfree-workspace`
- `confctl inputs channel set --commit workspace-tools vpsfree-workspace d45b5e914434a93859b039f057b4b84750a4c5fa`
- Nix build of `packages/workspace-portal` from the pinned flake input.
- `named-checkzone vpsfree.cz /dev/stdin` with the internal DNS placeholder
  expanded for `ns1.int.prg.vpsfree.cz`.
- Created and pushed the workspace feature branch and its dedicated worktree,
  then force-reset `master` to `0d2802f` as explicitly requested.
- Cancelled the first mandatory-review run because its review packet became
  stale when the workspace history and worktree layout changed.
- Rebased the workspace feature branch onto the tracking-only `master`, dropped
  duplicate tracking commits, and force-pushed the rewritten feature history.
- `confctl inputs channel set --commit workspace-tools vpsfree-workspace 6371e9cad7dec81791a5eb3bf6290aef632dce0d`
- `confctl inputs channel set --commit workspace-tools vpsfree-workspace 2c9112daa50f74dab50ab8983323d040d246f62e`
- Rewrote the unmerged workspace branch into separate portal, final PKI,
  shared-session, and workspace-policy commits.
- Regenerated the final workspace input pin with `confctl` from the clean input
  commit, then rewrote the unmerged configuration branch so it contains one
  generated input update instead of three successive revisions.
- Split aitherdev hosting and internal DNS into separate configuration commits
  because they have distinct deployment and rollback steps.
- Re-ran both Ruby suites, all Go tests, `go vet`, the handoff-skill
  validator, `git diff --check`, and `nix flake check --no-build` after the
  workspace history rewrite.
- Built `packages/workspace-portal` from the final pinned workspace revision
  with Nix; output:
  `/nix/store/h05r1jlqydflyrn36xgd2g49m8fj8505-workspace-portal-0.1.0`.

## Results

- Active slug: `2026-09-03-dev-session-portal`
- Managed tmux session created as `$36`.
- User confirmed the portal hostname, custom-CA HTTPS, browser-created empty
  sessions with an initial Codex turn, encrypted CA custody on aitherdev, and
  user-owned deployment of aitherdev and both internal DNS servers.
- After the initial mandatory review completed, the user changed the hostname
  to `vpsfree-cz-workspace.aitherdev.int.vpsfree.cz` so future workspaces can
  use distinct names.
- `dev-session` suite: 83 tests and 700 assertions passed.
- PKI suite: 2 tests and 25 assertions passed, including encrypted-key,
  renewal, hostname, chain, permission, and git-worktree refusal checks.
- Portal Go tests and `go vet` passed.
- The `dev-session-handoff` skill passes the skill creator validator.
- The current ChatGPT desktop SSH session uses the same Unix App Server socket
  that the portal adapter successfully connected to.
- The pinned Nix package builds and its packaged portal, `dev-session`, and PKI
  commands start successfully.
- Internal zone validation passes with serial `2026090300`.
- `nix flake check --no-build --show-trace` passes.
- No GitHub Actions runs are configured for the pushed configuration feature
  branch.
- Workspace `master` and `origin/master` were both reset to `0d2802f`; the
  complete implementation is retained on the pushed workspace feature branch.
  Tracking-only commits now follow that pre-initiative revision on `master`
  without carrying the implementation.

## Mandatory change review

- Overall risk: high, because the feature introduces authentication, local-CA
  secrets, a local Codex control protocol, host process behavior, TLS,
  firewall, DNS, deployment ordering, and rollback behavior.
- Reviewed workspace `2c9112da` and configuration `2ba6673d` with
  `gpt-5.6-sol` at `max` effort in the general, architecture/repetition,
  scope/proportionality, and risk/compatibility lanes.
- Blocking findings: workspace self-worktrees could not be finalized; artifact
  reads followed ancestor symlinks and raced path replacement; approval prompts
  hid granted authority and accepted unoffered decisions; App Server messages
  over 32 KiB disconnected the client; serial GitHub enrichment could hide all
  local page content during an outage.
- Important findings: incomplete App Server handshake/resolution/reconnect and
  response-claim lifecycle; non-retry-safe partial session creation; unbounded
  full-history refreshes; divergent manifest identity validation; unsafe PKI
  pair replacement; overbroad `KillMode=process`; incomplete deployment and
  rollback probes; policy reconciliation with the preserved user change; and a
  disproportionate bespoke authentication subsystem.
- Advisory findings cover explicit repository probe failures, authoritative
  default-branch metadata, no-store responses, proxy-aware throttling, unused
  interfaces, and pinned PKI invocation in the runbook.
- Decisions: retain and fully support the workspace feature-branch policy
  because the user explicitly requires it; replace application-owned password
  sessions with nginx basic authentication while retaining strict mutation
  origin checks; address all Blocking and Important findings before long
  builds; apply low-cost advisory fixes in the same remediation; rerun every
  review lane because authentication and protocol remediation change design
  boundaries.

## Review remediation checkpoint

- All four initial reviews finished before the hostname was changed. The
  implementation and runbook now use only
  `vpsfree-cz-workspace.aitherdev.int.vpsfree.cz`; the shorter name is not kept
  as an alias.
- The workspace feature branch now supports the reserved
  `worktrees/<slug>/workspace` worktree through creation, manifest recording,
  final commit capture, non-force removal, and finalization. A regression test
  exercises the full lifecycle against a real non-bare top-level repository.
- Browser session creation records a `creating` manifest before external work,
  persists the thread ID before best-effort naming, checks the thread's first
  turn before retrying the initial request, and marks the session `ready` only
  after tmux setup. This makes retries converge without duplicate threads or
  initial turns.
- Portal artifact and tracking reads use already-open file descriptors beneath
  a no-symlink `openat2` boundary, enforce size limits before reading, and
  reject duplicate active/archive identities and manifest/directory mismatches.
- The Codex adapter completes the initialize handshake, rejects protocol
  version skew, accepts 64 MiB frames, limits browser history to 20 recent
  turns, removes resolved prompts, tags connection generations, claims each
  response once, and coalesces browser refresh events.
- Approval controls show the complete request and matching thread item. The
  application accepts only the string decisions offered by the App Server or
  defined by the exact file-change and permission response protocols.
- GitHub enrichment is concurrent under one five-second page budget. Local Git
  probe failures are shown as unavailable instead of clean.
- Authentication moved from the Go application to nginx Basic Authentication.
  Every application mutation still requires the exact HTTPS origin, and all
  application responses use `Cache-Control: no-store`.
- CA and server certificate helpers publish versioned certificate/key pairs
  through an atomic `current` symlink. Root-only installation copies and
  verifies a complete pair before switching nginx. Previous pair directories
  remain available for rollback.
- The runbook now covers root-owned Basic Authentication and TLS preparation,
  pre-DNS HTTPS and authentication probes, exact rollback capture, partial DNS
  deployment recovery, one-hour DNS cache handling, pinned renewal tooling,
  and Codex daemon restart/version checks.
- Quick checks after remediation: `dev-session` has 87 tests and 740
  assertions passing; PKI has 4 tests and 33 assertions passing; Go tests and
  `go vet` pass. The Go race suite and JavaScript syntax check still need their
  Nix-provided compilers/runtimes before the remediation commits are written.

## Open questions

- Mandatory change review must be restarted after quick checks; the long
  `confctl build` validation follows review.
- Live ChatGPT macOS/mobile discovery remains an optional deployment smoke test
  because it depends on the installed clients. The VPN portal is the supported
  browser path regardless of native discovery.

## Cleanup

- Keep the tmux session and configuration worktree until implementation,
  review, and deployment handoff are complete.
- Do not finalize until no review, CI, merge, user deployment handoff, or local
  cleanup remains.
