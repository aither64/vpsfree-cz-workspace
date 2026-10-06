# Mandatory review packet: dev-workspace

## Review assignment

- Reviewer: retained `reviewer0`, GPT-6 Sol, xhigh, read-only.
- Risk: high. The branch changes live conversation rendering and durable-send
  reconciliation, automatic archive locking and final eligibility checks, and
  the packaged Codex web dependency.
- Lanes: general, architecture and repetition, scope and proportionality, and
  risk and compatibility.
- Canonical procedure: `~/.codex/skills/mandatory-change-review/SKILL.md` and all
  four lane references.

## Repository and history

- Repository: `worktrees/2026-09-29-portal-performance/dev-workspace`.
- Feature branch: `2026-09-29-portal-performance`.
- Initial base: `3b570f0a8b75d809a2753177590158e9dc4639f1`.
- Review head: `9db7bc844a0332b7e00d21536c3bebf835928ece`.
- Complete base-to-head series:
  1. `7afe780f929773727693184c0c302f5340d61b2b` — `flake: select paged Codex conversation client`
  2. `38cc1220092d58ae0bcdb1f6a4a377a818fad6d7` — `portal: page large conversations incrementally`
  3. `9e25870d143f28c2e37763a5e6fd526dad1c9df5` — `session: observe automatic archives without exclusive locks`
  4. `9b54f7b46cd37fdd36679e619616ebd995f43be6` — `portal: preserve legacy transcript view on refresh`
  5. `67246cf25a40ad5029121b75c99f24434bf86d36` — `portal: track output across sliding legacy windows`
  6. `87430b813cb0e0017e844711e60f4b34a7c32513` — `portal: pin corrected codex-web history module`
  7. `9d48fc795de12f7725b0995d336c323c474c25e0` — `nix: validate the selected codex-web module pin`
  8. `9db7bc844a0332b7e00d21536c3bebf835928ece` — `nix: require the exact codex-web pseudo-version`
- The worktree is clean. No `dev-workspace` commit is pushed or deployed. There are no database,
  state-format, or other migrations.

## Upstream dependency

- The reviewed and pushed Codex web feature head is
  `d210d3f7cc93981d0ab163b1fcf0718f9587f47e` on its feature branch.
- Its pre-push high-risk review resolved all Blocking and Important findings;
  see `review-codex-web.md` and `review-codex-web-result.md`.
- Nix source metadata, Go pseudo-version and checksums, and Go vendor hash now
  identify exact revision `d210d3f7`. The package asserts that the Go module
  revision matches the Nix input. Fake-hash discovery produced final vendor hash
  `sha256-XCmaphXVXVvhnV3oU1UnreAw01qEoyBGB1bbb8Y9dSg=`.

## Intended portal behavior

- Request the newest transcript page first and render it without waiting for
  complete history, queue reconciliation, pending prompts, or rollout metadata.
- Reuse the shared Codex web page reader, stable entry keys, and history model;
  do not duplicate cursor/gap/reset rules in the portal.
- Offer **Load older**, preserve loaded nodes and scroll position, repair missed
  ranges and active-turn updates, and reject stale in-flight repair responses.
- Preserve strict fallback: only a missing route or explicit paging capability
  response may use legacy `/thread`; authorization, malformed, timeout, cursor,
  and server errors fail closed.
- Reconcile pending requests, queue state, activity, and transcript on
  independent bounded lanes with retained last-known UI and retry behavior.
- Acknowledge durable sends against the complete retained transcript and
  coalesce a follow-up pass when another page arrives during an in-flight batch.
- Reduce idle activity polling while preserving focus, visibility, active-turn,
  and stale-status recovery.

## Intended archive behavior

- Passive automatic-archive observation uses a shared global transition lock
  and shared per-session observation lock. It does not claim mutation authority.
- A single bounded `workspace-portal thread observe` call obtains trusted thread
  identity, cwd, updated time, idle state, and blockers instead of repeatedly
  scanning Codex state through separate processes and RPCs.
- Known active, pending, queued, or unresolved states become ordinary blockers;
  malformed or unknown observation failures fail closed.
- The worker upgrades to exclusive transition and session locks only for an
  actual archive candidate. Under those locks it rechecks root activity, team
  members, registered worktrees and exact branch heads, hold, and policy before
  writing the lifecycle journal.
- Sidecar storage locks are not held across Codex RPCs, Git inspection, or
  content hashing. Lock order must remain transition, session, then short
  sidecar operations.

## Acceptance criteria

- Large conversations render a useful newest page without full-rollout latency;
  older history, filtering, disclosure state, composer actions, pending prompts,
  queue controls, and durable receipts remain correct.
- Mixed old/new Codex web and portal versions fail safely through the documented
  optional paging contract.
- Passive scans no longer block unrelated portal reads or session commands on
  an exclusive transition lock; real archive mutations remain serialized and
  race-safe.
- The live deployment later meets p95 at most 2 seconds with zero failures for
  30 normal loads and 30 loads overlapping a dry-run scan. Metadata expiry and
  rebuild CPU are a separate live gate.

## Compatibility, deployment, and recovery

- No persisted schema or journal format changes. Existing sidecars remain
  readable and existing lifecycle recovery/journal rules are preserved.
- The page endpoint is optional; legacy `/thread` remains available. Exact pins
  prevent packaging a portal against a different helper contract.
- Shared locks are compatible with existing exclusive lifecycle commands;
  actual mutation still requires the exclusive lock marker.
- Deployment is from the workspace user-profile package after downstream pin
  propagation, review, and builds. No vpsFree.cz system configuration pin is
  changed.
- Profile rollback is intentionally unsupported for the current forward-only
  team-registration state. Recovery requires a newer package preserving current
  readers and site composition while disabling or correcting the feature.

## Explicit non-goals

- Do not merge default branches, change system configuration, identify unrelated
  historical lock holders, alter archive policy, or archive/delete this session.
- Do not remove the legacy thread route, change Codex protocol writes, expose
  conversation content in diagnostics, or relax lifecycle final rechecks.

## Verification evidence

- Portal JavaScript syntax checks pass for the application, browser contract,
  shared paging contract, and live paging harness.
- Portal shared-pagination and browser unit contracts pass against the local
  corrected Codex web asset at `d210d3f7`.
- Focused Codex web regressions pass for stale responses after both paged and
  legacy full replacements. Focused portal regressions pass for preserving
  disclosure and scroll state when a new portal script refreshes through an
  older Codex web asset, including a recent-turn window sliding from turns
  1–20 to 2–21. Added or updated entries signal new output; removal alone does
  not.
- `go test ./portal/...` passes all portal packages; the web package completed in
  34.338 seconds and the workspace Codex package in 5.185 seconds.
- Ruby syntax checks pass for both lifecycle executables.
- `ruby -Itest test/dev_session_test.rb -n '/automatic|retirement_uses_its_own_deadline/'`
  passes 19 runs and 415 assertions. A prior direct single-file invocation was
  invalid because it bypassed the aggregate loader that defines shared fixtures;
  it is not a product failure.
- Nix flake metadata evaluates with the committed lock file; vendor-hash
  discovery failed only with the expected fake-hash mismatch and supplied the
  installed exact hash.
- `git diff --check` passes.
- The parsed module-pin contract accepts the exact required version, rejects a
  commented coincidence, and rejects wildcard and version-specific replacements
  of `codex-web` while allowing unrelated replacements.
- On the currently deployed old package, the 21:01 CEST scheduled scan held the
  transition path until 21:04:53. A reviewer assignment waited more than 45
  seconds and completed only after that scan exited, directly reproducing the
  contention this branch removes.

## Reviewer deliverable

Start with findings ordered by Blocking, Important, then Advisory, with file,
line, and commit references where possible. Explicitly assess shared/exclusive
lock ordering and mutation authority, final archive race checks, combined
observation fail-closed behavior, portal cursor/reset races, retained receipt
acknowledgement, activity/pending/queue lane isolation, mixed-version behavior,
exact dependency coherence, cross-project helper reuse, commit scope, user copy,
and missing tests. If there are no findings, say so clearly and list residual
risks and verification gaps. This is pre-push review; final complete-history and
migration readiness review comes after the whole pin chain and live acceptance.
