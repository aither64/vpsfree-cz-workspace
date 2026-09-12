# Plan creation goal normalization review

Review only the committed goal normalization delta and its recovery consumers.
The user-approved portal features have passed the required general, architecture,
scope and risk reviews and are deployed as profile28. Prior reports and decisions
remain in review-reconciliation.md. This is a targeted general/risk rerun for a
real browser acceptance finding, not a new review of the entire initiative.

Initiative: 2026-09-12-portal-review-experience. Plan and state are under
/home/aither/workspace/ai/vpsfree.cz/work/2026-09-12-portal-review-experience/.
Runtime worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace.
Read its AGENTS.md. The local operator is trusted; preserve remote-client
validation, ordinary concurrency, request identity, partial recovery and rollback.

## Finding and acceptance criteria

A real completed Plan-mode response has a trailing newline. The portal froze
the derived implementation goal with that newline, but the existing Ruby CLI
read_goal uses String#strip before binding, journal creation, initial submission
and completion evidence. The CLI successfully created the intended session and
completed its initial turn; the portal rejected its goal hash and shadowed it
with a failed receipt. Three of four bounded fixture threads are allocated.

The fix must align submitted goal identity with the CLI's actual strip behavior
(space, tab, LF, VT, FF, CR and NUL, not all Unicode whitespace). The captured
PlanText, PlanTurnID and PlanSHA256 must remain exact. It must recover the
already-frozen raw goal from the deployed version using ordinary reads/retry,
strictly matching all other binding/evidence/manifest identities, without
manually rewriting fixture state, allocating another thread or sending the
initial plan again. Content changes beyond this existing normalization must
still fail proof. No canonical state schema, CLI behavior, source plan digest,
Codex protocol, dependency, host configuration or user-visible feature changes.

Runtime owns this portal/CLI interface. Only portal creation invokes the private
CLI receipt flags. codex-web remains83770217d63f2c206689d2c569e1c81950544504.
The organization and consuming workspace only update immutable runtime pins.
Their current deployed heads are2e0cae05f79f68c1e7bbbd1fb5b2ec857963f0e6 and
abd0cbd932c17196f8f973d8b1b3be0af97a7eee, respectively. Those pin changes will
follow the exact reviewed runtime revision; no independent logic changes.

Risk is HIGH because this compares persisted cross-process request identity
and must recover a deployed receipt. Fresh standalone general and risk reviewers
use gpt-5.6-sol/xhigh. Architecture/scope remain satisfied: a bounded normalizer
within the existing goal identity contract adds no abstraction or wider scope.
A separate functional fix commit is appropriate because profile28 already runs
the prior revision and its frozen receipts are a supported compatibility case.

Review directly without edits, Git mutations, tests or nested agents. Report
concrete findings ordered Blocking/Important/Advisory with file/line and commit
evidence, or clearly state no findings and remaining test gaps.

## Committed delta and quick checks

Runtime range:
`f5d587823368e530c5d9f52a17e1befed9fd54e1..d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2`.
One scoped functional commit changes creation.go and creation_test.go.
The runtime worktree is clean. Provider and consumer heads above are unchanged
at review launch; consuming pin refreshes are mechanical.

From runtime portal using Nix Go/GCC/Ruby/Git:
`GOWORK=off GOFLAGS=-mod=mod go test -race ./internal/web -run
"TestCreationGoalNormalization|TestCreationReconcilesDeployed|TestCreationWorkerPersistsSuccess"
-count=1` passed in 1.912 s. Broader creation/fork/plan race coverage passed in
32.353 s with `-run "TestCreation|TestSessionCreation|TestForkSessionInvokes|TestImplementPlan"`.
The parity test executes actual Ruby read_goal. The old receipt regression
reloads failed state, validates strict canonical binding/evidence, rejects
changed internal content and durably readies the same receipt/attempt via GET,
preserving raw Goal and the entire Request without invoking the CLI.

Long real acceptance is paused until review completes, then resumes the same
retained fixture on the new package. The portal's failed receipt, canonical
session, CLI binding and evidence have not been manually edited.


Mechanical consumer updates completed during review:
organization2e0cae05f79f68c1e7bbbd1fb5b2ec857963f0e6..a30de6c62d2bcd1ff41ee48018c595140c6d4042;
workspaceabd0cbd932c17196f8f973d8b1b3be0af97a7eee..9edf553f03b94b69ac96bb4d986eddccd3fa90b5.
Both commits change only flake.nix/flake.lock to select the exact runtime above.
All four feature worktrees are clean and contain their explicitly fetched
origin/master. Runtime and organization exact-head CI runs are34702185008 and
34702231264; no superseded runs remain active.
