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
- The latest completed mandatory review examined workspace `b345dfed` and
  configuration `6c6d627b`. All four lanes finished before remediation began.
  The fixes are committed and pushed at workspace
  `39d5e3d6d1fb31e56416cb67d9383a279b45d840` and configuration
  `38dca2988818477739438fcdef069ecb6ab406c2`. Fresh review is pending; no long
  configuration build or deployment has started.
- The top-level checkout already contained unrelated changes, including a
  modification to `AGENTS.md`; it remains preserved outside this initiative's
  patch. The feature no longer contains that hunk. If its owner has not
  committed it before integration, preserve it as an exact path-only patch,
  reverse that patch briefly with an empty index, fast-forward, reapply it, and
  verify that the resulting `AGENTS.md` diff is byte-for-byte identical.

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
- The earlier desktop SSH experiment established App Server connectivity but
  did not prove that the existing tmux client used the supervised portal
  socket. Its manifest is intentionally read-only until that session is stopped
  and restarted after deployment with recorded endpoint and version provenance.
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

## Fifth mandatory review

- The general, architecture/repetition, scope/proportionality, and
  risk/compatibility lanes completed against workspace
  `58e9b099420c96f594c943c31397b5f133918c6f`, configuration
  `1509f7f8c7fd01fc77f3f9d0d53616f5af514a14`, and tracking `dd92765`.
- Blocking findings cover incorrect nested `thread/items/list` decoding,
  hard-coupling passive pages to Codex, stale nginx process credentials after
  first deployment, unsynchronized work/manifest/archive lifecycle, missing
  canonical repository identity, and a workspace branch that cannot pass its
  fast-forward-only integration gate without rebasing and repinning.
- Important findings cover goal-sentinel retry corruption, permissive Ruby
  RFC3339 normalization, bulk removal without immutable-head capture,
  half-retrofitted unshared tmux sessions, false App Server unit ownership,
  workspace-pin churn killing tmux sessions, stop-time interruption of creation
  helpers, and archive entries without finalization evidence.
- Advisories cover duplicated protocol-pin ownership, status chronology based
  only on manifest mtime, and refusing a pre-existing unowned tmux namespace.
- Decision: fix every Blocking and Important finding before long builds. Make
  Codex CLI's managed daemon the single daemon authority, keep it a soft/lazy
  dependency of passive pages, use main-process-first systemd shutdown for web
  request draining, decouple the tmux keeper from workspace pin changes, and
  require nginx to restart with the new supplementary group. Rebase the
  workspace feature branch onto current shared `master`, then regenerate the
  configuration pin and all exact revision gates.
- No code changed and no long configuration build ran while the fifth review
  lanes were active.

## Fifth-review remediation in progress

- After committing this checkpoint, the workspace feature branch was rebased
  onto shared `master` at `4264e32`, so it can be integrated by fast-forward.
  Its final remediation head is pushed at
  `72e21da1a52b2c2fb07b8730002e598e9efd82c9`.
- The configuration branch is pushed at
  `eb1b3aa27e1eff1f6c42549b47e1c922b11ac4f0`. Commit `bf9ae6e1` changes service
  ownership and shutdown behavior; generated commit `eb1b3aa2` pins workspace
  `72e21da1` through `confctl` without editing `flake.lock` manually.
- The portal decodes nested App Server thread-item entries, reads its protocol
  version from source metadata, treats anchored `state.md` lifecycle as the
  interaction authority, rejects malformed archives, and uses finalization
  timestamps for archived chronology.
- `dev-session` now persists canonical project identity, verifies it during
  cleanup/finalization, snapshots heads during bulk cleanup, strictly validates
  RFC3339 calendar/time components, reconciles exact tracking skeletons, and
  refuses to retrofit a running unshared terminal session.
- NixOS now leaves the detached App Server under Codex CLI ownership, decouples
  the tmux keeper from workspace-pin changes, refuses a pre-existing tmux
  socket, drains portal helpers with `KillMode=mixed`, and restarts nginx so
  live processes acquire the proxy group.
- Quick verification passes with 99 `dev-session` tests and 891 assertions,
  5 PKI tests and 44 assertions, all Go tests and Go vet, Ruby/JavaScript syntax,
  formatting, diff checks, and `nix flake check --no-build --show-trace`.
- Exact-head Go race tests also pass. The pinned portal package builds as
  `/nix/store/y1i4bhk4iaig5f73lnjyi9p4mkqvy1hj-workspace-portal-0.1.0`.
- GitHub reports no Actions runs for either rewritten feature head, so there
  are no current or superseded branch runs to inspect or cancel.
- The fifth-review findings require one final review rerun against the new exact
  heads before long `confctl build` validation begins.

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

## Sixth mandatory review and remediation

- General, architecture/repetition, scope/proportionality, and
  risk/compatibility reviews completed against frozen workspace `72e21da1` and
  configuration `eb1b3aa2`. No files changed until all four reports finished.
- Blocking findings were an invalid persisted schema-1 manifest, an App Server
  launcher that requires an absent standalone Codex installation, tmux attach
  commands split between `/tmp` and the shell's `TMUX_TMPDIR`, and shared
  `master` advancing beyond the reviewed workspace base.
- Important findings require one reproducible configuration pin, remediation
  folded into owning commits, per-session tmux provenance, and unambiguous
  top-level workspace integration instructions. Advisories cover bounded
  in-memory registries, hostname duplication, recent-turn limits, rollback of
  live tmux sessions, and leaf-key custody.
- The tracked manifest now includes canonical project identities and the exact
  live default tmux socket. Both the Ruby and Go readers validate it. New
  manifests persist their resolved socket path, and the UI suppresses attach
  commands when that provenance is unavailable.
- The replacement design runs the pinned `codex app-server` directly in its
  own systemd service and cgroup. The portal has only a soft dependency and
  continues serving status while Codex is unavailable. Terminal and browser
  helpers use the same explicit App Server socket.
- Browser tmux sessions use an absolute `/run` socket, independent of
  `TMUX_TMPDIR`. A real tmux regression exercises creation and attachment while
  the environment points elsewhere.
- Production CA and source leaf keys are now kept in a root-only state
  directory. The runbook validates all manifests and renders the real
  initiative page before DNS publication, and refuses rollback while
  browser-created sessions remain.
- Workspace history is rewritten into five owning commits based on shared
  `master` at `a9a0f55`. The clean branch is pushed at
  `b345dfed561d09bc3621d49e2c5e60fcccfae92c`. The unrelated concurrent-session
  identity hunk is not part of the feature, and the portal handoff rule belongs
  to the session-sharing commit.
- Configuration history is rewritten into four reproducible commits: channel
  declaration, one generated exact input pin, complete aitherdev hosting, and
  DNS last. The clean branch is pushed at
  `6c6d627ba844d10a32209542417952377988573d`; generated commit `bda43117`
  pins workspace `b345dfed` with its `confctl` message unchanged.
- Quick checks pass with 105 `dev-session` tests and 921 assertions, 6 PKI
  tests and 48 assertions, all Go tests and race tests, Go vet, Ruby and
  JavaScript syntax checks, the handoff-skill validator, both manifest readers
  against the live initiative, `nix flake check --no-build`, and internal DNS
  zone validation.
- The exact pinned portal package builds as
  `/nix/store/aq9w3fham0l42y2jlw1zlfc0kr3h7674-workspace-portal-0.1.0`.
  Its portal, `dev-session`, and PKI entry points run, and both packaged
  manifest validators accept the live initiative.
- GitHub reports no Actions runs for either rewritten feature head, so there
  are no current or superseded runs to inspect or cancel.
- The remediation makes Ruby and Go reject the same schema/timestamp drift,
  adds a shared lifecycle corpus, resolves tmux sockets from each manifest for
  normal lifecycle commands, and binds browser interactivity to matching
  thread, App Server socket, and Codex client-version provenance.
- Root PKI commands now use the immutable flake package, the helper verifies
  state ownership, public export is atomic in a root-owned directory, and both
  host rollback paths stop and drain the portal before inspecting journals and
  dedicated tmux sessions.
- The Nix package now runs every Go package test and includes the shared
  fixtures. Its build log confirms the command, Codex, repository, session, and
  web suites all ran.
- Next steps are fresh review of these exact heads and, only after it passes,
  the long configuration builds.

## Seventh mandatory review and remediation

- All four lanes finished against workspace `b345dfed` and configuration
  `6c6d627b` before remediation began. The review was not clean.
- The blocking architecture finding was that LXC-writable `portal.yml` data
  could authorize a browser thread or select a host tmux socket. Mutable
  controls now require a uid-private host record under
  `/run/vpsfree-workspace-authority`, a matching live tmux identity, the
  configured App Server socket and Codex version, and an App Server thread cwd
  equal to the canonical `work/<slug>` path. Workspace manifests remain
  passive status metadata.
- The blocking deployment findings were a fail-open rollback snippet,
  workspace-owned shell data later sourced into privileged rollback commands,
  and privileged helpers/builds selected from mutable worktrees. A tested
  `workspace-portal-rollout` helper now stores strict JSON in a root-owned
  directory, drains and validates before switching, and restarts the portal on
  any failed pre-switch check. The runbook builds an exact commit, attests its
  store path and NAR hash, and runs each `confctl` build/deploy from a fresh
  detached checkout of that revision.
- All supported terminal and browser sessions now use the dedicated absolute
  tmux socket in the deployed environment. Session mutations share a host-only
  lifecycle gate; rollback takes it exclusively before checking that runtime
  authority is empty and only the keeper remains. This closes terminal
  creation races between drain validation and the generation switch.
- Cross-server tmux attachment now nests an attachment instead of issuing an
  invalid `switch-client`. The helper verifies the exact configured Codex
  executable and its reported version before publishing provenance. Socket
  selection happens inside the per-slug lock and rejects explicit mismatches.
- Ruby and Go validators now agree on plan/state presence, bounded reads,
  lifecycle placement and finalization, and duplicate identities. PKI commands
  consistently validate private directory ownership, exact modes, and symlink
  ancestry before reading or exporting.
- The runbook checks both firewall ports from a routed non-WireGuard source,
  requires a positive connectivity control, and corroborates the result with
  firewall rules and counters. DNS and host rollback paths come only from the
  root-owned structured capture.
- An exact package build then exposed a nondeterministic App Server reconnect
  test timeout. Repeated execution showed that a delayed watcher from the old
  connection could send `thread/resume` before the replacement connection's
  `initialized` notification. Normal RPCs are now gated on a ready generation;
  the reconnect regression passes 100 consecutive iterations and surfaces
  server protocol errors without waiting for the global Go test timeout.
- A race-enabled process-group test once reported a surviving child. Repeated
  isolated runs killed the process group correctly; the assertion now records
  the descendant's Linux start time and process group so PID reuse or group
  drift is distinguished from a real survivor. Five race-enabled full-suite
  iterations pass after that instrumentation.
- Quick verification passes: 109 `dev-session` tests with 943 assertions, 6
  PKI tests with 56 assertions, 2 rollout tests with 15 assertions, 20 full Go
  suite iterations, five race-enabled full Go suite iterations, Go vet,
  JavaScript syntax, configuration hooks, `nix flake check --no-build`, and
  internal zone validation at serial `2026090300`.
- Workspace `39d5e3d6d1fb31e56416cb67d9383a279b45d840` is clean and pushed.
  Configuration `38dca2988818477739438fcdef069ecb6ab406c2` is clean and pushed
  with four commits: channel declaration, one generated pin to the exact
  workspace revision, complete aitherdev hosting, and DNS last.
- The exact pinned package builds as
  `/nix/store/idswhbb99ifdygk578hm5dy0cgp8bj6y-workspace-portal-0.1.0` with
  NAR hash `sha256-Qehg8negveuC2slGDSQG/TyJVLqcl7hGCYkjRBBmWzU=`. Its build
  runs all five Go packages plus the packaged Ruby session, PKI, and rollback
  suites.
- The current deployment runbook has SHA-256
  `1a4d1655eaa13b34772bdbe34c7c885187a09cebfa7ee4d9c27b29cdd9aff926` before
  this state update; recompute it for the frozen review packet because exact
  revision substitutions and runbook hardening are still uncommitted tracking
  changes in the shared top-level checkout.

## Eighth mandatory review and remediation

- All four review lanes completed against workspace `39d5e3d6` and
  configuration `38dca298` before files changed. The reports were not clean:
  they identified five general blocking findings, three architecture blocking
  findings, one scope blocking finding, and two risk blocking findings.
- Browser creation now publishes only a non-interactive `creating` authority
  before the initial turn. Tracking, tmux, and the complete Codex environment
  exist before that turn begins; the journal, manifest, and private authority
  advance to `ready` only after the turn is accepted or reconciled.
- Browser and terminal mutations now serialize on stable host-only lock files
  rather than LXC-writable workspace inodes. Ruby, Go, and the rollout helper
  validate the same runtime-authority JSON corpus.
- Persisted Codex provenance permits a verified read-only transcript for a
  stopped, completed, or archived initiative. Only a matching live `ready`
  authority enables events or mutations, and index rendering no longer blocks
  on serial App Server verification.
- New thread environments include the authority directory, dedicated tmux
  socket, exact Codex executable, App Server socket, and Codex version. Stop,
  remove, finalize, stale recovery, and rollback verify that relevant App
  Server turns are idle before destroying runtime state.
- Rollback now drains the portal, takes the exclusive host lifecycle gate,
  validates journals and authority entries, scans all workspace App Server
  threads for activity, stops the App Server, and only then changes generation.
  Every failure before a successful switch attempts to restart both services.
- The deployment runbook uses the exact attested package rather than building a
  mutable worktree for privileged helpers, verifies the immediate predecessor
  immediately before each host deployment, and describes the firewall rule as
  the exact allowed source subnet.
- Workspace history was rebuilt as six focused commits on current shared
  `master`. The branch is clean and force-pushed at
  `f2c408567ef71568c970d0472ac4e46c049156ee`.
- Configuration history was rebuilt as four commits. Generated commit
  `365db8fb` pins the exact workspace head through `confctl`; complete
  aitherdev hosting is in `566af982` and DNS remains last. The branch is clean
  and force-pushed at `543a985ef7ee858b05bac78f49851710f692c98e`.
- Quick checks pass with 113 `dev-session` tests and 956 assertions, 6 PKI
  tests and 56 assertions, 7 rollout tests and 54 assertions, all Go tests and
  race tests, Go vet, Ruby and JavaScript syntax, configuration hooks,
  `nix flake check --no-build --show-trace`, and internal zone validation at
  serial `2026090300`.
- The first exact package build exposed a fixture lookup based on
  `runtime.Caller`, whose path is trimmed by the Nix Go builder. The test now
  uses its stable package working directory; the exact pinned package builds as
  `/nix/store/c42ncdgyia44yf25p0qa9mm3nvfg9xs2-workspace-portal-0.1.0`
  with NAR hash
  `sha256-/8NGuYZyaLEcTXonBy7FT7zAHlSgW4R0Z9ECiDe92ZE=`.
- GitHub reports no Actions runs for either force-pushed feature head, so there
  are no superseded runs to cancel. The frozen deployment runbook has SHA-256
  `e1def2787424c5b0fb870c6e2721b05cdda5d558759dbd9e0876abf72c651a7c`.
- The mandatory review must now be rerun against these exact heads before long
  `confctl build` validation begins.

## Cleanup

- Keep the tmux session and configuration worktree until implementation,
  review, and deployment handoff are complete.
- Do not finalize until no review, CI, merge, user deployment handoff, or local
  cleanup remains.
