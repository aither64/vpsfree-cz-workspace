# Generic sysctl v2 monitor batch — approved, not launched

Affected final review is accepted and SSH publication is verified at
`895870606179f0c1170ad92a5fdc49eb2d6d1bbf`. No VM rerun has yet launched.
The only source change from v1 is explicit boot/test-shell readiness before the
separate service-check deadline. Prior failed attempt is retained in
[the failure note](generic-sysctl-focused-failure.md), not treated as a sysctl
application result.

After publication, existing utility `/root/generic_sysctl_88486_watch` owns
stale CI `39759039117` at exact `88486d43f7d47917b6ab796163abf8cd1f0be94a`.
Ask that owner to preserve first failures/logs/artifacts and cancel only if the
run is still queued/running at that exact old head. Obtain terminal/exit and
no-active-operation receipt before a new watcher. No duplicate observer.

Resolve retained utility policy at launch: fresh context, `gpt-6-luna`/`low`,
max concurrent one; retained digest
`ffaf9deb97720995ad1d662badae7645eba1fede5068eef529c9024efa7e7376`, matching
native `verification_watcher-low.toml`. Installed `full_access` requires
`danger-full-access`/`never`; verify actual launch binding and record native
identity. Follow `/home/aither/.codex/skills/dev-session-monitor/SKILL.md`.

## Fresh watcher assignment

- Canonical cwd:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-20-kernel-check/vpsadminos`.
- Verify current/session env `2026-10-20-kernel-check`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`, clean exact head `895870606179f0c1170ad92a5fdc49eb2d6d1bbf`.
- Existing automatic exact-new-head CI ID: `39764186292`; no RSpec appeared at
  discovery. RSpec only if automatic. Observe exact IDs/head; never start or
  rerun workflows.
- Start **once immediately** after binding, without a new full OS/cache-job
  prerequisite: `./test-runner.sh test system/sysctl`.
- Kernel `/nix/store/4k5kg0x1msvl4kffpr2g7cidpnwbnkhk-linux-6.12.113/bzImage`
  and initrd `/nix/store/i23y4g1swaix7mxqj9s8l1xjaaxiiwj6-initrd/initrd` are
  identical to the first native attempt and locally valid. See
  [bounded identity proof](generic-sysctl-v2-guest-identity.log). Full-closure
  equality is not claimed. Stop/escalate any unexpected local Linux kernel
  build, preserving exact derivation/cache evidence; no retry or workaround.
- Send parent a **timestamped start message immediately before launching**,
  including head, command and owned handle when available. Send completion or
  escalation immediately with end time/elapsed/exit and native artifact path.
  Clearly distinguish boot/test-shell readiness failure from a completed guest
  service check. Retain full native console/shell/service/runner evidence.
- Full focused log:
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-20-kernel-check/generic-sysctl-focused-vm-895870606.log`.
  Preserve actual exit status and native test-runner output directory. No
  pipeline may hide status. No arbitrary quiet-output timeout.
- Continue existing exact-head CI observation independently; focused completion
  is reported without waiting for the broad pipeline. Retain full available
  failure logs/artifacts and report material phase changes with observation
  timestamps. Do not cancel current-head CI.
- No source/tracking edits, diagnosis, retry, nested agents, deploy, merge,
  pins, host sysctl write or session lifecycle action. Do not clean first-failure
  evidence. Parent owns interpretation and subsequent decisions.

Return pass/fail/incomplete, revision/command/run IDs, start/end/elapsed/exit,
full evidence paths, bounded first error and every still-owned active operation.
