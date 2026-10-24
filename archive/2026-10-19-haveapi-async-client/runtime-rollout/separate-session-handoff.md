# Shared runtime rollout handoff

Prepared for an ordinary deployment session with its own identity, branches and
worktrees. The user explicitly approved creating that separate session after the lead
asked “May I start a separate deployment session using the prepared handoff?”
and the user answered “yes”. This does not transfer the parent session identity. Keep the HaveAPI development
session and WebUI PR #74 open.

## Approved outcome

The user approved merging the HaveAPI client into master, keeping WebUI open,
then answered “yes” to integrating the coordinator fix into dev-workspace/master
and updating the shared runtime before finishing HaveAPI. The coordinator fix
is now integrated. Shared runtime activation has not run. No lifecycle, npm/tag
release, WebUI merge, or unrelated default-branch integration is approved.

## Completed source and verification

- dev-workspace/master contains `dce4784fe0069b061dd76cdf689e2099b4b0e66d`,
  tree `5dc33558cc877c26573b9489aab13eb2e4c1ac89`. The only production change
  resolves Ruby through the entered repository Nix shell, preserving hooks and
  coordinator contracts. Independent reviewer0 (Sol/xhigh/read_only) accepted
  all four lanes with no findings. One coherent commit; no migrations or pins.
- Packaged coordinator checks: both exported shards, 54 unique tests and
  384 assertions, no failures/skips; complete aggregate coverage verified.
  Exact-head remote Check `39322472651` succeeded.
- Isolated real environment proof passed: coordinator host Ruby3.4.9/API3.4.0,
  HaveAPI shell Ruby3.3.10/API3.3.0 with Bundler4.0.23, Overcommit0.73 and all
  four native gems loaded. All588 committed files, original5native libraries
  and original/copied generated lock unchanged. This is environment evidence,
  not an admitted coordinator job. Failed setup attempts remain preserved.
- Exact review and check receipts: `premerge/coordinator-correction/` in the
  source session. Coordinator merge receipt: `runtime-rollout/core-status-final.json`,
  job `ae5e02ec-7485-46be-a01e-59f70c9b725d`, verified applied dce4784.

## Preservation and normal rollout

The selected package at preparation time is
`/nix/store/ad0s75irvrbj6pz6qk1zf7v9sy4l1qyp-dev-workspace-0.2.0`. Its generic
source matches published `6ab3b48f57981f4358094b47cac1ba724c458396`, including
two deployed lifecycle commits beyond the fix's original09a4079 base. Do not
replace that runtime with dce4784 alone: doing so drops deployed behavior.
Recheck the then-selected package and completed deployment frontier, and use a
published runtime containing both the fix and all preserved behavior. Prefer
the owners' normal canonical integration; do not integrate their unrelated
features or edit their branches/worktrees under this handoff.

Read the current workspace procedures, selected `workspace-host coordination guide`,
operations/integration guides, and configuration's
`docs/operations/workspace-coordination-aitherdev.md`. Use new session-owned
canonical-name worktrees. Update only the direct nested generic runtime URL and
generated workspace lock, plus matching configuration `dev-workspace` /
`devWorkspace` channel via confctl. Preserve extension and sibling inputs.
Run composition validation, required review/history gates and exact-final builds
outside claims. Normal activation order is system switch then dependent profile
activation, without reboot, under one approved aitherdev reservation. Respect
foreign review ownership and FIFO order, including the queued browser rollout.
No private helper, store/ledger edit, direct activation, forced release or retry
of ambiguous effects. Configuration/workspace default integration needs explicit
repository/target approval; do not infer it from deployment approval.

## Why separate deployment ownership

The current HaveAPI session also owns intentionally open WebUI registrations.
Reserve freezes every registration; normal finish requires all exact feature
heads integrated and resolves each through the immutable catalog. Those WebUI
names lack catalog entries, and merging their head would violate “keep PR open”.
No supported profile-only path avoids reservation ownership. Do not unregister,
archive, alter the catalog or hold the shared machine indefinitely to hide that
constraint. A separate ordinary rollout session must own only its real deployment
obligations and prove their normal release path before admission.

## Resume HaveAPI after deployment

HaveAPI feature `2026-10-19-haveapi-async-client` is published at
`19c20c90cc957d4225ece50a92e190855f252710`, based on
`c58704a08451a231fdf6c6123437133422af46dc`, tree
`0ef10a638118397c07f537b6a33159ec2ee21fe1`. All five exact-head workflows
passed, and final affected review accepted the full branch/history/no migrations.
The whole client subtree and tar bytes equal the prior reviewed candidate.
After legitimate corrected runtime selection, notify the original HaveAPI lead
with exact package/system/profile/receipt identities. That lead rechecks current
HaveAPI target and submits the authorized fast-forward merge through the
coordinator. No HaveAPI merge job has yet been admitted.

WebUI PR https://github.com/vpsfreecz/vpsadmin-webui/pull/74 remains open at
`5dd2333b9af230d4a81c8f772cbbb08d39b14913`; leave it unchanged. Do not archive
or close the original session. Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-haveapi-async-client/

## Ownership accepted and startup delivered

User approval was executed through ordinary `dev-session start --new --no-attach`
with the complete startup task, without team/model overrides or a parent fork.
New session: `2026-10-19-haveapi-runtime-rollout`, thread `01a15609-ff8b-7912-be54-6ef503996476`.
Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-haveapi-runtime-rollout/
Creation succeeded; the CLI reported restarting its terminal client after an
App Server disconnect. No runtime activation is claimed by session creation.
