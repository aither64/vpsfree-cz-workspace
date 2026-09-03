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
- The fourth mandatory review examined workspace
  `d269a6ca57b46ac0a2c86279ce76120eb0948f3d` and configuration
  `7b7d3489ab6a079b04a48a2f4a645ed8dfa9c354`. All four lanes finished before
  remediation began. The fixes are committed and pushed at workspace
  `58e9b099420c96f594c943c31397b5f133918c6f` and configuration
  `1509f7f8c7fd01fc77f3f9d0d53616f5af514a14`. No long configuration build or
  deployment has started.
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
  `go vet` pass.
- The remediation was folded into the owning workspace commits and force-pushed
  at `6119ef8dbb99fae4bc930f853a02fdb4b3c4e6ee`. The reconciled branch contains
  the preserved concurrent-session guard from the shared checkout.
- `confctl inputs channel set --commit` regenerated the configuration pin from
  the new workspace revision. The rewritten configuration branch was
  force-pushed at `6b07356e04347830cc02385f96f1ce28667bfee3` with one generated pin commit,
  followed by the aitherdev and DNS commits.
- A first `confctl inputs channel set --commit` attempt used an incorrectly
  expanded abbreviated SHA and failed with a GitHub 404 before changing the
  lock file. Re-running it with the exact output of `git rev-parse HEAD`
  succeeded. The reusable lesson is in
  `notes/vpsfree-cz-configuration/2026-09-03-confctl-pin-full-revision.md`.
- Post-commit quick checks pass: Go tests, Go race tests, `go vet`, JavaScript
  syntax checking through Nix, both Ruby suites, `nix flake check --no-build`,
  and `named-checkzone` at serial `2026090300`.
- The pinned Nix package builds as
  `/nix/store/kfz4ziqbhxr1pzif482sbr0byzdmlrbb-workspace-portal-0.1.0`, and its
  three packaged commands start or print their expected usage/version.
- Temporary `.bin/` and `.bundle/` files created by the configuration hook were
  inspected and removed. Both feature worktrees now have clean tracked and
  untracked status.

## Second mandatory review

- All four fresh lanes completed against workspace `6119ef8` and configuration
  `6b07356e`, using `gpt-5.6-sol` at `max` effort.
- Blocking findings cover the non-idempotent `thread/start` result boundary,
  missing session identity in browser-created Codex turns, incomplete
  `request_user_input` and command-approval controls, missing browser
  subscriptions for terminal-originated events, same-origin active artifacts,
  approvals without their matching thread items, a TCP backend reachable from
  the shared-network LXC, and a firewall rule that also admitted the aitherdev
  LAN.
- Important findings cover connection-generation races, invisible unsupported
  App Server requests, divergent manifest timestamp validation, stale GitHub
  default-branch comparisons, closed-session controls, a known Goldmark XSS,
  stale plan text, and DNS rollback state inferred from Git instead of the
  running DNS systems.
- The current remediation journals browser creation before other initiative
  state, reconciles threads by their unique `work/<slug>` cwd, injects the
  session environment into the thread, resumes watched threads after App Server
  reconnects, binds writes and approval responses to one connection generation,
  rejects and surfaces unsupported requests, and requires server-fetched
  matching items before approvals become actionable.
- The portal backend now uses a host runtime Unix socket shared only with nginx.
  The firewall admits HTTPS only from WireGuard. Curated artifacts use a
  passive extension allowlist, attachment disposition, and sandboxed CSP.
  Goldmark is updated to 1.7.17.
- Shared valid and invalid manifest fixtures now cover goal digests and strict
  RFC3339 finalization timestamps in both Ruby and Go. The deployment runbook
  captures independent running system paths and live DNS answers for both DNS
  servers.
- Quick remediation checks currently pass: 90 `dev-session` tests with 784
  assertions, 4 PKI tests with 33 assertions, all Go tests, Go vet, JavaScript
  syntax validation, and `nix flake check --no-build`.

## Review rerun checkpoint

- The final remediation was folded into the four owning workspace commits and
  force-pushed at `d9260fa562392ce9443af970be826efd4b074a9d`.
- `confctl inputs channel set --commit` regenerated the configuration pin for
  that exact workspace revision. The host and DNS commits were replayed after
  the generated input commit, the Go dependency vendor hash was updated, and
  the configuration branch was force-pushed at
  `bc4f31de0f7175c7aedb4dfea0fbe7e347e2d3d9`.
- The pinned portal package builds successfully. `named-checkzone` loads serial
  `2026090300`, `nix flake check --no-build --show-trace` passes, and repository
  hooks pass in the configuration development shell.
- GitHub reports no workflow runs for either feature branch. There are no
  superseded runs to cancel.
- All four review lanes apply because this remains a high-risk change affecting
  authentication, a host security boundary, a cross-project protocol adapter,
  deployment, and rollback. The rerun uses `gpt-5.6-sol` at `max` effort.

## Third mandatory review

- General, architecture, scope, and risk lanes completed against workspace
  `d9260fa562392ce9443af970be826efd4b074a9d` and configuration
  `bc4f31de0f7175c7aedb4dfea0fbe7e347e2d3d9`. Every lane used
  `gpt-5.6-sol` at `max` effort.
- Blocking findings cover repository-controlled Git configuration executing on
  the host, incomplete crash recovery around manifest/tmux/HTTP boundaries,
  writable `creating` sessions, permission approvals without matching thread
  items, one stale thread breaking all reconnects, divergent Ruby/Go manifest
  contracts, nginx-unreadable TLS keys, unsupported insecure TCP serving, and
  a commit split that does not keep portal and PKI documentation with their
  owning changes.
- Important findings cover archived comparison identity, the reserved
  `workspace` worktree name, untyped transcript rendering, passive-page
  coupling to Codex availability, unsafe PKI output and symlink paths, exact
  reviewed revisions and durable rollback captures in the runbook, an HTTP
  hostname sink plus HSTS, and a stale configuration commit message.
- Advisory findings include clearing the proxied Authorization header, aligning
  exact goal-size accounting, avoiding event streams on closed pages, and
  removing or documenting smaller stale metadata and commit-boundary details.
- No long integration build may start until Blocking findings are fixed and
  Important findings are fixed or explicitly decided. Remediation changes the
  persistence, protocol, and host-security designs, so affected lanes require a
  fresh rerun.

## Open questions

- Third-review remediation is committed, tested, repinned, and ready for a
  fresh mandatory review. Long `confctl build` validation follows only after
  the affected review lanes pass.
- Live ChatGPT macOS/mobile discovery remains an optional deployment smoke test
  because it depends on the installed clients. The VPN portal is the supported
  browser path regardless of native discovery.

## Fourth mandatory review

- The general, architecture/repetition, scope/proportionality, and
  risk/compatibility lanes completed against workspace `d269a6ca` and
  configuration `7b7d3489`, using `gpt-5.6-sol` at `max` effort.
- Blocking findings covered browser-triggered host Git configuration, missing
  experimental App Server negotiation, terminal-only permissions being denied,
  non-atomic tracking writes, Ruby/Go manifest divergence, worktree registry
  recovery, incomplete final comparison evidence, and the portal inheriting
  nginx secret access.
- Important findings covered active/archive cache identity, a stale unsubscribe
  race, midnight retry identity, duplicate browser submissions, service child
  lifecycle, mixed helper revisions, weak password provisioning, and executable
  deployment assertions.
- Advisories covered backend HSTS ownership, stale data fields, reconnect and
  response feedback, PKI passphrase custody, protocol-pin coupling, native
  ChatGPT wording, and checked DNS evidence capture.
- Decision: the local journal guarantees atomic local files and replay of a
  completed result. Codex App Server does not provide caller idempotency for
  `thread/start` or `turn/start`, so an acceptance-boundary timeout remains
  ambiguous. The portal performs bounded single-candidate reconciliation and
  refuses conflicts; it does not claim exactly-once remote creation.

## Fourth-review remediation checkpoint

- Removed top-level Git history inspection from browser creation and added a
  hostile `core.fsmonitor` regression. Tracking creation and goal seeding now
  use fsynced temporary files with atomic link or rename publication.
- Worktree creation resolves one base commit, persists its registry before Git,
  recovers a validated partial worktree, and refuses finalization unless every
  physical worktree is registered and every archived comparison has both commit
  IDs.
- Ruby and Go reject the same explicit tags, empty constrained values, legacy
  YAML boolean spellings, and malformed RFC 3339 timestamps through shared
  fixtures.
- The App Server handshake enables its experimental API. Permission approvals
  remain visible but unanswered for the terminal, and unsubscribe/resubscribe
  transitions are serialized. Browser controls disable during submissions and
  reconnects refresh both transcript and pending state.
- Browser retries retain a server-rendered date in the posted full slug.
  Repository caching includes manifest time and closed/archive identity, and
  closed sessions use immutable comparisons immediately.
- The configuration uses a dedicated nginx socket-sharing group. Browser tmux
  sessions and App Server use separate systemd units; the web service drains
  creation handlers and returns to full cgroup cleanup. A Nix assertion ties the
  packaged Codex version to the portal protocol pin.
- The operator guide now provisions bcrypt credentials atomically, checks DNS
  capture failures, asserts missing and wrong-password responses, verifies
  process groups and secret separation, requires the live helper revision, and
  includes a non-WireGuard probe.
- Current quick checks: 94 `dev-session` tests with 833 assertions, all portal
  Go tests, JavaScript syntax, Ruby syntax, `git diff --check`, Nix formatting,
  and `nix flake check --no-build --show-trace` pass. The ambient Go command
  lacked a C compiler, so Go verification runs through a Nix shell with GCC.
- Final quick checks at the rewritten head pass with 95 `dev-session` tests and
  837 assertions, 5 PKI tests and 44 assertions, all Go tests and race tests,
  Go vet, JavaScript and Ruby syntax, Nix formatting, and no-build flake checks.
- The exact pinned package builds as
  `/nix/store/9d4v7106fxhrw3mym77h61dky34clqn5-workspace-portal-0.1.0`; all three
  packaged commands start or print their expected version or usage.
- A `confctl inputs channel set --commit` attempt used an unverified expanded
  workspace SHA and failed with GitHub HTTP 404 before committing. The command
  was rerun with `git rev-parse HEAD`, producing the single generated pin commit
  `7eb542fb96235fd01659fb12accf86eade6be28a`.
- The workspace and configuration branches were force-pushed with exact leases.
  GitHub reports no Actions runs for either branch, so there were no superseded
  runs to cancel.
- The fifth mandatory review must rerun all four high-risk lanes against these
  final heads before the deferred `confctl build` commands begin.

## Third-review remediation checkpoint

- The portal no longer executes Git while rendering active or archived
  sessions. Repository links come only from the strict manifest contract, and
  archived comparisons use the recorded initial and final commit IDs.
- Browser creation writes a complete `creating` manifest before external work,
  blocks interaction until the initial request has been sent, identifies
  incomplete tmux sessions through their creation environment, kills the whole
  helper process group on timeout, separates JSON output from diagnostics, and
  retains a `ready` journal for exact response replay.
- Permission approval requests are rejected with a terminal-only explanation.
  Transcript events are normalized into portal-owned data types. Reconnects
  resume each watched thread independently, and the final browser subscriber
  sends `thread/unsubscribe`.
- Ruby and Go enforce the same manifest fields and scalar types. Shared fixtures
  cover aliases, duplicate keys, explicit nulls, multiple documents, and
  invalid nested values.
- The PKI helper rejects existing export directories, Git or symlinked private
  paths, and installs nginx keys as `root:nginx` mode `0640` beneath traversable
  mode `0750` directories.
- The portal has no TCP or insecure serving mode and does not contact Codex at
  startup. Nginx owns HTTPS, redirects the exact hostname from HTTP, sends HSTS
  on all responses, clears the upstream Authorization header, and remains
  limited to WireGuard clients.
- Workspace history now separates the portal, PKI, shared-session integration,
  workspace branch policy, concurrent-session safety rule, and operator guide
  into independently reviewable commits.
- Quick verification passes: 91 `dev-session` tests with 800 assertions, 5 PKI
  tests with 44 assertions, all Go tests, Go race tests, Go vet, JavaScript
  syntax checking, `nix flake check --no-build`, and internal zone validation
  at serial `2026090300`.
- The pinned Nix package builds as
  `/nix/store/jmk7fwrrwwjyskigk7lrs1p29q54m1x9-workspace-portal-0.1.0`.
- Workspace revision `d269a6ca57b46ac0a2c86279ce76120eb0948f3d`
  and configuration revision
  `7b7d3489ab6a079b04a48a2f4a645ed8dfa9c354` are pushed and frozen for the
  fourth mandatory review. GitHub reports no workflow runs for either branch.
- An ambient configuration push failed because its mandatory hook gems were not
  installed outside the Nix shell. The same force-with-lease push passed through
  the repository's Nix development shell without bypassing hooks.

## Cleanup

- Keep the tmux session and configuration worktree until implementation,
  review, and deployment handoff are complete.
- Do not finalize until no review, CI, merge, user deployment handoff, or local
  cleanup remains.
