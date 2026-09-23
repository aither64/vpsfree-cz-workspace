# Review packet: team lead delegation

## Outcome and boundaries

The root lead should discover its session's live direct-team roster at each new
substantive work item, delegate nontrivial design and separable implementation
to ready retained members, and integrate reports. Solo and small dependent work
stay with the lead. Existing idle roots gain this policy; active turns are not
interrupted. Review and Luna/low verification remain governed by their existing
skills. No new bus, roster format, UI, or automatic work assignment is intended.

The user chose default delegation for a full team, not mandatory fan-out for
every request. Do not merge feature content to a default branch without a
separate explicit approval. This initiative uses a no-Codex tracking session,
so it has no eligible retained reviewer.

## Repositories, commits, and ownership

- `codex-web`: base `d542e767310d9d7b32460691a54829371b88e3b2`, head
  `01e75798654b5c56535646dea687468a358408fb`; worktree
  `worktrees/2026-09-23-team-lead-delegation/codex-web`. Its public Go client
  owns `ReconcileThreadInstructionsWithPolicy`, retaining the old method.
- `dev-workspace`: base `ec8cb4211111d9734bfef5e4fe5c1f06c8372934`,
  head `1b836baf85e8486e0455ce2a70f9c4423328ac22`; worktree
  `worktrees/2026-09-23-team-lead-delegation/dev-workspace`. The portal is the
  discovered consumer. Its `portal/go.mod`, `flake.nix`, `flake.lock`, and Nix
  vendor hash pin the above provider head. The pin belongs with the consumer
  behavior because its new API cannot compile against the prior pin.
- `workspace`: base `ede06b6221c76ef7ba084d9376ff2134ad622469`, head
  `8fe84327f656f1112b860a26b1e1ebd42bccc8ff`; worktree
  `worktrees/2026-09-23-team-lead-delegation/workspace`. This site-specific
  instruction reinforces the generic root policy for CLI attachment.

The coordination plan and status are in
`work/2026-09-23-team-lead-delegation/{plan,state}.md`. The commit split is
provider API, generic consumer plus inseparable pin/package changes, and
site-specific instructions.

## Design and compatibility

The generic root developer policy is applied on root create and fork and on
portal reconciliation. It names no member address or model; the lead reads the
current same-session roster. Member policies and model/effort settings are
untouched. Existing roots are reconciled only when idle, with bounded attempts
and current thread-identity checks while the portal runs. Archived roots are
reconciled on revival. The existing lifecycle
instruction remains combined with the lead policy. No persisted state, schema,
API wire format, or roster migration changes. New `dev-workspace` requires the
new `codex-web` revision at build time; deployment is one user-profile package
switch. Older profile generations still read the unchanged session state.

Documentation changed: `codex-web/docs/reference.md`,
`dev-workspace/docs/dev-sessions.md`, and workspace `AGENTS.md`. The former two
are the durable public-interface and session-behavior homes. No separate
operator upgrade guide is needed for an additive instruction and API change.

## Verification and review assignment

Risk: **High** because a cross-project public client contract and persistent
root-thread instructions affect active sessions, CLI/portal consistency, and
deployment behavior. Review all four lanes: general, architecture/repetition,
scope/proportionality, and risk/compatibility.

Quick checks: `codex-web` focused `go test ./codex -run
TestReconcileThreadInstructions -count=1` passed in its Nix shell with
`GOFLAGS=-mod=mod`; `dev-workspace` focused tests for root settings and portal
reconciliation passed with the new pinned module. `nix build --no-link
--print-build-logs .#workspace-portal` passed after refreshing the Nix vendor
hash; its package check phase ran the Go and Ruby suites with no failures.
After review remediation, focused portal reconciliation tests passed again.
The initial vendor-mode and stale-hash failures were tooling/pin setup and
are recorded in the initiative state.

Reviewer: fresh standalone installed default development reviewer, because
this tracking session has no root Codex thread or roster. Installed catalog
`bc7e3a3cc3af152879ee5b4e29fdd8a20bf1cfc2a10dcdf122c1e94a69e3743b`
selects `gpt-6-sol`/`xhigh`, role `reviewer`, read-only, native variant
`dw_aedcfbb1a3dc69f0aebc22073bb4abbd78ac1803dd2d0f57` with behavior
digest `3ac7c9377651e2298f3d3cf8ae28b35a3763c5bd9d426f4aacd840a04139b6b4`.

The reviewer should read the mandatory-change-review skill, all four selected
lane references, this packet, and the affected repositories' `AGENTS.md`
files. Review the committed series directly; do not edit, deploy, or launch
nested agents. Return concrete findings ordered by severity and lane, or say
clearly that none were found and name residual risks/test gaps.

## Review remediation

The first review found one Important risk issue: a stalled reconciliation
request could block later roots indefinitely. It also noted stale thread IDs
on retry. The consumer commit was amended to give each request a 10-second
deadline and refresh the current manifest identity before retries. Focused
tests cover both behaviors. Revisit only general and risk lanes for this new
retry behavior; the provider API, architecture and scope boundaries are
unchanged.
