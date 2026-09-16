# Architecture and repetition review

## Findings

- **Advisory — protect the complete timeout relationship with a provider-level
  regression check.** In runtime commit `5deb10cd40faf78eaabd4c7e47f5b4e8d5f44ad7`,
  `test/dev_session_test.rb:275` verifies the new 210-second Ruby constant and
  correctly exercises timeout restoration, but supplies the 60-second outer
  scope itself and never checks the Go retirement deadline at
  `portal/cmd/workspace-portal/main.go:287`. The production values are correct
  today. A future increase of the Go deadline above 210 seconds could recreate
  the same premature-kill failure while this regression stays green. Add a
  small check covering the actual ordinary/inner/outer deadline relationship,
  or explicitly retain this as a test gap. A new public timeout configuration
  interface is unnecessary.

No Blocking or Important findings.

## Reviewed scope

- Runtime `eb658d49e6b8182d5fc07ab98bc897c58490baa9` through
  `a65583d45b707eb23feb7d490ba177e8360dfb8d`, including both commits and their
  focused tests and documentation.
- Organization extension `17da396e7fea5d4e31d4af1382da00fe4d140e17` through
  `1a0bc7db6c968bde9cb9ecbd737d8b1b6f28de44`.
- Workspace `f8d6217a8a6e83bd317a7bef166aa650806ca553` through
  `3610be86615b8710b2e1bfe8a53b9771bad15fdf`.
- Local repository instructions, initiative plan/state, session and portal
  guides, existing automatic-archive state owner, lifecycle receipts and
  reconciliation, command runner, browser request and lifecycle helpers,
  extension package constructor and consumer pins.

## Assessment and remaining validation

The generic runtime owns the fix at the existing retirement boundary. Both
archive and deletion reuse that boundary; the existing runner restores its
previous timeout through `ensure`. Stage annotation stays in the component
that owns conversation retirement and preserves wrapped errors. No downstream
implementation or additional state format is introduced.

The failure banner reuses the existing blocker presentation and requires both
the operation and conversation identities. It keeps historical worker evidence
separate from live lifecycle monitoring. The additional refresh loop has a
distinct role and throttle; it delegates running operations to the existing
monitor instead of duplicating its retry state machine.

Consumer discovery through the flakes, package constructor and extension guide
confirms the runtime → organization package → workspace dependency chain. Both
consumer locks select the reviewed runtime. The public package and extension
interfaces and the codex-web pin remain unchanged.

I reviewed the focused test implementations and reported results; I did not
rerun them or start integration tests. The planned real-browser, packaged and
isolated archive acceptance runs remain necessary before rollout. Review
performed directly without subagents, using the requested architecture lane.
