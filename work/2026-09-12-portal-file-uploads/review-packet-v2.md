# Remediation review packet

Read review-packet.md for the full requested outcome, acceptance criteria,
consumer graph, initial bases, non-goals and deployment topology. Read
review-reconciliation.md for the first-round findings and explicit decisions.
This is a focused rerun after the queue completion fix introduced a new optional
public contract and changed lifecycle validation. Review the remediation and
its interactions, not a rubber stamp of earlier conclusions.

Risk: high (durable recovery, public API, deletion and rollback); xhigh effort.
Selected rerun lanes: architecture/repetition and risk/compatibility.
All intended changes are committed. Quick checks pass; integration is not started.

Current exact heads:

- codex-web: 39abf28707ac3417bfc1b1a26361d52f4f21e26d
- dev-workspace: 32760301b56dc490a12874edf854ae84d5bc89f5
- vpsfree-dev-workspace: f0761fbbc75a44d6470b248df62bec4878cfbebc
- workspace: f27c721bbd7ad5b3404d12112ae08b651e559827
- vpsfree-cz-configuration: 3f4375a33ef350ad008ec2e40b40ca332a32ab91

Public change since initial review: QueueDeletionCompleter is an optional
conversation client interface. The concrete codex.Client retains its unchanged
schema-3 deletion intent through provider completion. Queue GET may complete
only already absent entries; it cannot perform App Server deletion. Lifecycle
validation reports unresolved deletion intents instead of auto-clearing them.
Clients without completion support fail before attachment queue deletion.

Direct runtime fixes are the creation lock/receipt reconciliation, conflict
release, prepared replay validation, catalog compaction and recovery headroom,
exact deletion proof, and centralized private workspace namespace. Runtime
history is now four functional commits: pin, storage, portal input, CLI lifecycle.
The rewrite preserved the final tree exactly. The workspace feature is rebased
onto current shared master 56b9b7236f6f16f127461ef0f878b295b34e1ca7; those
additional coordination commits are outside the feature review range.

No Codex version or App Server protocol request shape changes. Provider and
consumer pins all select 39abf287 and runtime 32760301 through both the workspace
profile and aitherdev configuration. No default branch integration is authorized.

Validation: codex-web full Go and four Node tests; runtime full Go at the exact
pinned module; Ruby removal/fork 69 tests/622 assertions; measured Nix vendor hash.
Codex-web current-head CI 34720476635 passed. Other current-head CI is monitored.
Provider regression tests include persistence failure before and after completion,
restart, queue refresh, and a started-message reconciliation race. Store tests
include both capacity bounds, accepted receipt protection, expiry/replay, exact
owner deletion, conflicts, and a creation/deletion interleave.

Accepted rollback boundary is documented in README and plan: finish queue
deletions before rollback. An older package may clear an existing receipt without
updating upload metadata; roll-forward then retains those bytes until explicit
owner-session deletion. This does not lose bytes or weaken authorization.

Write findings to review-v2-architecture.md or review-v2-risk.md in this directory.
Do not edit implementation files or delegate. Cite exact heads and useful lines.
