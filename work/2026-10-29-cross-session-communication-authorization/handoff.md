# Cross-session authorization handoff

Ready, awaiting explicit integration approval for dev-workspace/master.

## Result

The generic dev-workspace branch implements trusted registry authorization
context separately from peer text. One explicit approval in either exact
session authorizes deliberate messages both ways without receiving-chat
reapproval. Fresh policy/tool guidance resolves legacy ambiguous deliveries
through the registry. Pair/thread/incarnation, revocation, held delivery,
saved submission identity and message-only scope remain enforced.

Native verification also identified and fixed production activity composition:
communication reads fresh activity through the existing portal observer and
read gates, retaining the operational client for metadata/send/reconciliation.
UI cache/stale success cannot authorize delivery. No codex-web or global
recorder, public API, schema, migration, dependency or scheduler change.

## Published source

- Repository: git@github.com:aither64/dev-workspace.git; target master.
- Feature branch: 2026-10-29-cross-session-communication-authorization.
- Base: 08f3dbb92bc8585929edee85a824d44dfb3b0846.
- Final head: 4155d0099d03028b43d5f08d225a88156cb4155a; exact SSH remote verified.
- Final series: A ed16c606, B b0279514, C 4155d009. Obsolete fixture iterations
  and fixups consolidated; no migrations or repeated update streams.
- [Compare](https://github.com/aither64/dev-workspace/compare/master...2026-10-29-cross-session-communication-authorization).

## Evidence

Original and affected independent final reviews completed all four applicable
lanes using retained reviewer0, codex-lb Sol/xhigh, with no findings. Original
and affected reports preserve exact reviewed ranges. The final tagged-only
fixture repair from a6c0e10f to4155d009 received direct narrow-fix inspection,
architect source confirmation and short red/green proof. Production is identical
to the affected reviewed tree. Consolidation retained exact source trees and
patch equivalence. See [final review](review-report-production.md),
[original review](review-report.md), [followups](review-followup.md),
[design](design.md), and owner [A](implementation-a.md),
[B](implementation-b.md), [C](implementation-c.md) evidence.

Focused communication, policy/MCP, web/activity/cache/admission and transcript
checks pass. Full exact-pinned native verification passes both idle and steer
on final 4155d009 through the actual portal constructor/observer/background
worker, native MCP and App Server: trusted developer context reaches both
leads, one grant remains, exact active turn is steered, reverse reply succeeds
without local allow, and recipient settings remain retained. Go 12.043s,
wall 17.9s, exit0; [result](verification/native-final-result.md).
Native pin: /nix/store/idil0dg5623qarasafiqsjfc3s2bm2a9-codex-package-0.165.0/bin/codex.
The Responses endpoint is synthetic; a checked host-selection adapter substitutes
for the unchanged Ruby wrapper. This proves protocol/policy inputs and runtime
behavior, not arbitrary model judgment. Packaged Ruby checks close that wrapper
boundary separately.

[CI 40975812804](https://github.com/aither64/dev-workspace/actions/runs/40975812804)
PASSED on exact 4155d009: fast packaged/focused checks, archive and creation
succeeded; host skipped as expected for a feature push. Completed 00:08:21Z,
elapsed 17m 52s. Fast logs confirm complete workspacecodex passes across packaged
variants (39.829-44.654s) and Ruby shard coverage, including dev_session_test.rb
500 tests / 4 shards. This closes the earlier 45s broad-package timeout obligation;
that partial local attempt itself is still recorded as timed out. See
[CI result](verification/ci-result.md). All owned local CI observers have exited.

Final fresh fetch and SSH proof confirm origin/master remains08f3dbb9, remote
feature head remains4155d009 and source tree 9b80c67e2f800c3354776404711c458b02c0881e
is clean. The portal captured this exact base/head comparison. No required work
remains before handoff; user approval is the next integration prerequisite.

## Operator boundary

No default-branch integration, deployment, production mutation, incident-private
access or session archival/deletion/stop occurred. The installed runtime is
unchanged; feature readiness does not establish deployed usability. Integration
into dev-workspace/master requires separate explicit approval. Deployment is a
separate decision and must follow the current selected package's coordination
and rollout procedures with disposable-session verification. Preserve schema-1
saved options/envelopes; do not refresh an already-prepared tuple to add context.
Legacy messages use current registry authority rather than duplicate approval.

The session remains active and open. Current phase, completed checks and
next action: [state](state.md).

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-29-cross-session-communication-authorization/)
