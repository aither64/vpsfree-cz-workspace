# Cgroup v2 shared-user follow-up review

Workspace: `/home/aither/workspace/ai/vpsfree.cz`.
Initiative: `2026-09-05-cgroup-v1-shared-device-fix`.
Plan/state: `work/2026-09-05-cgroup-v1-shared-device-fix/{plan,state}.md`.
Worktrees: `worktrees/2026-09-05-cgroup-v1-shared-device-fix/{vpsadminos,vpsfree-cz-configuration}`.
Read workspace and repository AGENTS.md; do not modify any repository or run VM
integration tests. Perform your assigned review directly, without subagents.

## Commits and scope

- vpsadminos original base: ec7dc42da33cd963fe63d8dde281b0e88fe790c2.
- Original v1 fix: 9fb79eb68ba4f7b9d9a9c6e2e985556a10aa725e, previously reviewed
  by all four lanes with no findings and fully validated locally and in CI.
- New head: 19e7601e1932c25f3b6542d667c6d3f5aea7a20b. The follow-up is one
  independently reviewable test-only commit after the original runtime fix.
- Configuration base: 248e2fc614bb3bc29c0a9c9f910330ade0b3cb80.
- Configuration current head: 72af910e51cc729e65faa4a8507b9e3e0649be8b, the
  existing generated production pin to 9fb79eb68. No tracked changes.
  Development-shell .bin/.bundle artifacts were created during review and
  will be cleaned before handoff.
- After vpsadminos validation and push, the pin will be regenerated with
  confctl and consolidated into one generated input-update commit on its
  retained branch. It is mechanical selection of the reviewed provider, with
  no additional runtime/configuration logic; preserve the generated message.

Review the committed series and current context, focusing on the new v2 test.
Neither retained branch is merged. User requires all pre-merge follow-up in
this initiative on these branches, including the confirmed pin refresh.

## Acceptance criteria

Extend devices-v2 with the same three sibling-isolation scenarios as devices-v1:
local deletion, local chmod rwm to r, and recursive /default deletion. Two
running Alpine containers share one osctl user and promoted char 10:200 TUN.
Persistent /root/test-tun nodes survive policy changes. Read-only/write-only
opens (without I/O) must prove baseline access, target denials and sibling
access, then denial for both under recursive removal. Require explicit
Operation not permitted messages, valid single/multi BPF attachments, unchanged
sibling/parent program names for local changes, restored default programs after
recursive removal, and clean osctl healthcheck after each mutation.

Do not refactor the existing procedural checks or devices-v1. No runtime/API/
state/schema/protocol/Nix module changes, reconciliation, repair command, merge,
deployment, or activation are intended. The original decision not to repair
already damaged running v1 cgroups remains accepted. No shared test framework
interface is changed; ownership stays in the existing vpsadminos VM suite.

## Quick verification

- nix develop --command nixfmt tests/suite/cgroups/devices-v2.nix: passed.
- nix-instantiate --parse on that file: passed.
- Extracted embedded script, nix develop --command ruby -c: Syntax OK.
- git diff --check: passed.
- Reviewed Overcommit configuration and refreshed its configuration signature.
  Mandatory hooks installed; Nixfmt pre-commit and all commit-message hooks
  passed. RuboCop enabled but no Ruby source file was changed.
- No long VM tests have been started for this follow-up, per review ordering.

## Risk and compatibility

Conservatively classify overall initiative high: container device authorization
and tenant isolation plus production revision selection. Follow-up itself is
test-only. Review lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. All reviewers must use gpt-5.6-sol at xhigh.

Old/new nodes remain compatible, with no coordinated update required. The
configuration input keeps the previously accepted staging base and will add
only this test commit. Upstream fetches are being inspected; avoid unrelated
scheduled updates invalidating the accepted base. Full production node builds
remain unavailable because the deployment-only initrd SSH key is absent. No
secrets will be fabricated or copied. Local v1/v2 VM tests and pushed-head CI
must pass; unexpected local kernel builds must be stopped and investigated.

## Rerun packet after first VM result

New amended head: `5e31378ae42f253b4878940e3462f6e40b214fb4`.
Correction diff: `19e7601e..5e31378ae`. Both are still descendants of the original
v1 fix, which remains untouched. No remote push has occurred for the follow-up.

The initial v2 VM run failed after 471.28 seconds. Local deletion and chmod
examples passed. In recursive removal all four read/write opens were denied
with Operation not permitted; only the assertion that testct's BPF program name
returned to its initial default failed (expected `946a3e34004`, actual
`858012c51ba`). Logs show only /default's BPF program replaced on group deletion.

Source inspection: v2 GroupManager#children traverses group.children; v1 also
traverses group.containers. The v2 parent BPF program enforces effective access
without needing to replace the container programs. The test now checks both
container attachment shapes, restored parent program, both effective denials,
and health; it no longer equates descendant program hashes with effective
hierarchical policy. No runtime behavior was changed. Broader restart or future
reconfiguration semantics are outside this bounded immediate-access test.

Re-review general and risk/compatibility lanes at xhigh because the original
expected descendant state was corrected after kernel evidence. Evaluate whether
this correction preserves the requested coverage and is supported by the code.
Architecture and scope lanes are not rerun: no abstraction or scope changed.
All formatting/parsing, extracted Ruby syntax, diff checks, active Nixfmt and
commit-message hooks passed on the amended commit. Do not run VM tests.
