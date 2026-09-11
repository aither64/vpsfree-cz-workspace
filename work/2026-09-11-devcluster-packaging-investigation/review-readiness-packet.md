# Review: vpsAdmin SSH readiness follow-up

Implement both-provider packaging repair; deploy user profile and verify start,
update, restart and retained container data. Keep branches unmerged. Full scope,
prior reviews and compatibility decisions are in plan.md/state.md and review-packet.md.

Organization repository: worktrees/2026-09-11-devcluster-packaging-investigation/vpsfree-dev-workspace
Review delta base d2380cbe77f711627ba461ef9359724b6255a5db to head
3d83a8392cd77fb7e92587ed4ea1a5cc665bd3fb (one functional commit with test/docs).
Workspace repository: worktrees/2026-09-11-devcluster-packaging-investigation/workspace,
head 2c81615829910eeb859f83c152e03751f20e08d1; will receive mechanical org pin.
vpsadmin validation-only head 8d0ccafd5b307115ddc4b1f24152ba30ed52e893;
vpsadminos validation-only head 3eaf7b7320754715b38fc629e7f0ce23d13402cd.

Live OS acceptance passed on the reviewed deployed base. vpsAdmin booted all VMs,
but start returned SSH 255 No route to host during automatic node refresh. Runner
shell readiness precedes bridge/sshd readiness. This delta waits before services
seed check and each normal node refresh. It retries only a harmless true probe
on SSH transport exit 255 for 120 seconds; actual remote actions still run once.
The organization owns the helper. Generic stable dispatcher and shared locks,
runner readiness, credentials, config/state/socket/disk contracts are unchanged.
No production changes or coordinated node updates. Generic runtime and all its
package dependencies remain unchanged. No new dependencies or configuration knobs.

Non-goals: password-reset session mutation; broad SSH/lock/runtime redesign;
transactional replacement of forced certificate imports; automatic retry of
remote mutation. Generic dispatcher losing stdin is separately documented and
not part of this repair. Local operator trusted for host administration; guest
and remote-client boundaries remain unchanged. Shell probes preserve real errors.

Quick checks: bash -n, git diff --check pass; actual-command Ruby suite 8 tests,
124 assertions, zero failures/errors/skips. Existing refresh action failure test
verifies action is not retried. Prior base full flake, eight packaged config
smokes/two runner loads and CI passed. New code has not been deployed or used for
live acceptance. Existing deployed-base VMs may be used independently during review.

High risk due to host/node start behavior and deployment. All four lanes required,
gpt-5.6-sol xhigh. Read mandatory-change-review SKILL.md and assigned lane reference,
local AGENTS.md, committed delta and needed context. Perform review directly with
no subagents. Do not edit project files or run live mutations. Return concrete
severity/file/line findings, or no findings and residual test gaps. Save your
report as review-readiness-<lane>.md in this tracking directory.

## Readiness review remediation

General and risk found that ConnectTimeout cannot bound authentication/session stalls.
The follow-up now sets BatchMode=yes and IdentitiesOnly=yes and uses coreutils
timeout with a five second per-attempt bound capped by the remaining 120 second
deadline, plus a one second forced-kill grace. A stalled attempt returns its
non-255 error immediately. Actual remote actions are still never retried.
The probe reuses machine_host/ssh_opts, independently of the public SSH command.
Coreutils was already a runtime dependency; no new configuration/dependency/state
contract. A real hanging SSH stub now proves timeout124, no remote action and lock
release. Full actual-command suite9/130 passes, syntax/diff clean.
Reviewed original 3d83a839 is retained in history by Git but amended into final head:
9e8783d68fdf40de04683e419d4f373bc27e3730

Rerun general, risk and architecture on this narrow change from original readiness
head; scope remains the same bounded readiness behavior. No live use of new code yet.
