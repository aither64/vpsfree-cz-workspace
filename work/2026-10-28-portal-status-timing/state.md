---
lifecycle: active
---

# Current status

- Phase: final implementation and independent-review preparation.
- Done: private native-home runtime, Codex 0.165 compatibility, published runtime,
  configuration and workspace pins, independent portal sign-in, seven migration
  fixtures and composed deployment-contract check.
- Remaining: independent review, longer native/package checks, final builds,
  coordinated system deployment, detached migration and live acceptance/retry.
- Risks: both backends must become idle; migration preserves an original backup.
  No live service has been changed and no message has been resent.
- Next: review the committed branches and one-time operational source.

See [design.md](design.md) for the implementation and verification brief.
All feature branches are `2026-10-28-portal-status-timing`, under the same
`worktrees/<slug>/` group: dev-workspace, codex-web, vpsfree-cz-configuration,
and workspace. The configuration checkout hook initially lacked ambient Ruby
gems; registration exists, so repair within its Nix shell without recreating it.

Detailed evidence and the exact retry identity are in [diagnosis.md](diagnosis.md).
The user's October 29 clarification resolves the interface question: stock CLI
need not access portal threads; existing portal tmux clients provide terminal
access. No deployment has been made. A connection-scoped
unsubscribe of the idle confctl thread returned
`notSubscribed`, confirming it cannot release another connection's ownership.

Latest read-only checks: system stock CLI is 0.165.0; workspace service remains
0.164.0. Their processes held 14 and 47 thread-writer locks respectively. Both
reported thread locks still belonged to the managed stock daemon. Both target
threads were idle when subsequently queried. The event that first opened them
in that daemon is not proven; do not claim the user manually opened them there.
The runtime currently derives its Codex home from inherited CODEX_HOME or
~/.codex; its tmux clients already use the workspace's explicit remote socket.

Application changes are in progress; live services have not been changed. No retained team was created; team list
reports no lead thread for this tracking-only shell initiative. The shared index
was empty and shared master matched origin/master before the initial checkpoint.
Unrelated workspace changes are preserved.

## Evidence

- `workspace-host status`: selected package
  `/nix/store/7wqvb8wdy58x94nh24k0kqnagqldfhvi-dev-workspace-0.2.0`.
- Autostart thread: `01a163b4-e2c6-7081-b9cb-e7a0e78eab4b`.
- Confctl thread: `01a14bb2-e3ad-7922-a5c9-bc1d07d5cbb8`.
- Portal Unix socket reads avoid the ambient curl trust-store mismatch with the
  internal CA; no credentials are needed for this local operator endpoint.
- User explicitly permits retrying `yes go ahead` after repair.

## Phase checklist

- [x] Initial investigation and scope.
- [x] Root cause established and implementation design accepted.
- [ ] Runtime isolation, upgrade and migration implementation.
- [ ] Applicable checks and independent review.
- [ ] Deployment and live acceptance.
- [ ] Authorized original message retry verified.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-portal-status-timing/

## Implementation checkpoint (October 29)

- codex-web published head: ba8dfdd27daa7ab3f4350f7a2627984b6b7f84cf.
  Strict 0.163 and prompted 0.164 contracts remain; 0.165 adds a native fixture,
  upgrade fixture and exact source provenance. Full 0.165 catalog adds only Terra;
  derived Luna remains 62680 bytes with the existing digest.
- Exact 0.165 native SHA-256: 647b0157e6472a793e0a0bd45bc44ef8ade673b6d8f3db4118260acda4976652.
  The llm-agents package keeps its daemon Nix-store patch and chatgpt recursion
  limit insertion. Upstream adds native state migration 62 (attached parent).
  Both 0.164/0.165 source trees have temporary initiative-owned indirect GC roots.
- dev-workspace private home propagation and native storage launch identity are
  committed and published at 8c597b6f5c3b10ca8d9193f2da7ef4cc3a4b21a5.
  Naming/package prerequisites select 0.165. The fresh vendor derivation passed.
- Quick evidence: codex-web full Go unit suite, tagged version-probe tests,
  exact binary schema/client corpus and all 55 config restrictions passed.
  Runtime local protocol and focused naming tests passed. Initial host suite had
  two stale-home assertions and five long Unix socket path failures. Corrected
  assertions and TMPDIR=/tmp: focused 23 tests/742 assertions passed. Use the
  aggregator test/workspace_host_test.rb; individual shard files omit fixtures.
- Configuration worktree registration is complete. Overcommit installed through
  nix develop; no hook bypass used. Workspace feature worktree is also registered.
- Fresh independent ChatGPT login completed in the private portal home; credentials
  were not copied or printed. Existing stock login remains untouched.
- Initial read-only inventory: 7074 native rows, 507 registered/retained roots and
  members, 2723 portal-owned threads including dependencies, 4351 stock rows,
  no shared ancestor dependencies and no missing portal rollout. A missing
  historical test member is explicitly state=removed and excluded by the same
  retained-member rule as runtime; preserve its old native row in stock.
  Portal rollouts total about 13.27 billion bytes. Inventory still needs recovery
  and archived prompt references before final cutover. Current free space ~98 GiB.
- One-time inventory code/JSON and schema fixtures are untracked operational
  artifacts. Preserve the final reviewed migration source in Markdown or another
  durable permitted location before execution; do not rely on untracked archive
  retention. No migration, deployment, live resend or master merge has occurred.

Recovery/archived-prompt references increased explicit inventory seeds to 660;
the closure remains 2723 portal and 4351 stock threads, with no missing owned
rows/rollouts or shared dependencies. Completed provider snapshots contain eight
historical original rollout paths; they are evidence, not active recovery state.
Active provider state currently says applied. Recheck final transition readiness.

Fresh vendor derivation jndaqzn3gqjpcis944g8q36dgcrj4jcx produced
sha256-XEvzpQbsCzcHzhTdqghrjhGmiqna25MPU2b/wGJekqA=; runtime now uses that hash.
The discovery build failed as expected against a fake hash. Final build remains.
Configuration functional edit selects a private copy of the portal codex-lb token;
stock codex-ds continues using its stock key path.

## Final implementation evidence

- Runtime: 8c597b6f5c3b10ca8d9193f2da7ef4cc3a4b21a5 (published).
- Configuration: dcb5982fd4325d57cda79693fa4da27c7a955413 (published).
- Workspace composition: 5deaee4fcf6692f617e346aa84ab3f95f52c3bfd (published).
- Full runtime Go unit suite passed; focused native-client tests passed (2 tests,
  12 assertions). Earlier unrelated host socket-path fixture failures were fixed
  by TMPDIR=/tmp; corrected home expectations passed the focused host batch.
- Final composition check passes and preserves extension
  767dfd587e346168e1443e65ccdb67ce748f3fe3. System llm-agents was already the
  frozen 91ff550f revision, so its channel command made no redundant commit.
- Seven synthetic migration tests passed in about three seconds: exact schema
  and history preservation, untouched source, unknown stock records, missing
  portal history, low space, unknown schemas, atomic exchange recovery preserving
  new writes, wrong directory identity and live open-file exclusion (some cases
  share a test). Root /proc inspection uses existing SSH access to 172.16.106.40;
  ambient sudo needs a password and is not used by the operation.
- Latest inventory: 7075 indexed, 661 seeds, 2724 portal, 4351 stock; no missing
  portal history or shared dependencies. Existing missing stock rollouts stay
  unchanged. Portal rollouts total 13,275,356,461 bytes. Free disk is
  97,049,088,000 bytes (90.4 GiB); repeat capacity admission after final builds.
- Four portal shell snapshots contain old-home entries only in PATH. They do
  not set CODEX_HOME/SQLite storage; retain snapshot bytes and native history.
- One-time source, recovery behavior and deployment preparation are preserved
  in [rollout.md](rollout.md). It is not installed by any project package.
- Current session has no retained lead/team. The installed catalog digest is
  495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7.
  Mandatory review fallback is delegated/reviewer: gpt-6.1-sol, xhigh,
  read-only review instructions, effective full-access execution. No roster changes.
