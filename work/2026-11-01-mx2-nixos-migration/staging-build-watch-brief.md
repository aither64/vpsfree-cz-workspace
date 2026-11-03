# Private staging five-system build utility

This is the first and only operation for this fresh verification utility.
Read /home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/skills/dev-session-monitor/SKILL.md.
Execute only the build below; no edits, diagnosis, retries, remote access,
deployment, approval, nested agents or lifecycle/cleanup actions. Local requested
logs/result files are allowed. Keep ownership until command effects are settled.

Parent verified managed policy from selected/pinned package
/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0:
catalog_digest495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7,
utilities.verification_watcher modelgpt-6-luna/effortlow/lifetimeoperation,
matching native utilityverification_watcher-low.toml and full_access execution
(danger-full-access, approvalnever). Do not invent another readiness gate.

Session2026-11-01-mx2-nixos-migration, workspace/home/aither/workspace/ai/vpsfree.cz.
Command CWD:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-mx2-nixos-migration/vpsfree-cz-configuration.
Verify dev-session current and both environment markers against this binding;
both absent is acceptable with explicit trusted binding, any conflict stops.
Require clean committed HEAD0844881779d62d9a6a86d2bacd61d21565b33932 and lock
SHA256507e781c2fa52da5a389e6eab824efe68baa72b1727de0fc162ea0a5e6b4c098.
Mismatch reports incomplete without repair/execution. Independent final review
staging-review.md clears this exact build batch. No deployment is authorized to
the utility; the machine admission prerequisite is unrelated to local builds.

Run once, exact argv:

```json
["nix","develop","--no-write-lock-file","-c","confctl","build","--yes","cz.vpsfree/containers/{mx2,prg/int.mon1,prg/int.mon2,prg/int.alerts1,prg/int.alerts2}"]
```

Do not rerun the VM check. Supported quoted union inventory already proved exactly
these five targets. No source/input update, shell dependency installation or
other command campaign. Expected build duration about3-10 minutes; report a
concrete overrun, not a generic silence timeout. No intentional kernel change:
if unexpected local Linux kernel compilation starts, cancel only this owned
command through its native handle and report evidence/effects. Otherwise stop on
the command's own result; do not retry. Use cancellable tool handle/native waits
at most60s and bounded log excerpts; parent will not poll the same build log.

Capture complete stdout/stderr to absolute session file staging-build.log;
preserve exact exit status/elapsed and write staging-build-result.md plus
staging-build-status.json (running command identity while active, completed
status afterward). No secrets/environment dumps. Send progress on actual build
milestones/failure/escalation, then return raw result promptly.

After successful native command, inspect only the five corresponding
.confctl/generations current/generation.json and toplevel symlinks, and ordinary
nix path-info registered output/deriver/NAR metadata. Record exact actual paths,
generation timestamps/JSON SHA256, output/deriver/NAR in staging-built-systems.json.
Do not modify generation metadata or relabel predictions as built outputs.
Expected outputs (all under/nix/store):

- mx2:4pc5mic0rp9h5qb2lhgmdh2x8z50pqd2-nixos-system-mx2-26.05.20261026.718f670
- mon1:8wyx524fsyyxpqid9ynrxrhrvn0kga65-nixos-system-mon1-26.05.20261026.718f670
- mon2:085v7hqkq1nc2vc8inrynmyvxa8xk9md-nixos-system-mon2-26.05.20261026.718f670
- alerts1:6qn8kzpgmrs3syxpqiqyvxhn8gvki9wj-nixos-system-alerts1-26.05.20261026.718f670
- alerts2:id1cj8xkg84wscfi30jb4ajdsp18bhxy-nixos-system-alerts2-26.05.20261026.718f670

Exact expected root derivations/table in staging-implementation.md and
staging-final-roots.json. If outputs mismatch, report incomplete provenance with
actual result; do not diagnose, rebuild or change anything. Parent owns acceptance.

Return passed/failed/incomplete, exact head/argv, exit/elapsed, log/artifact paths,
failure excerpt if any, and any still-running command/cancellation/effects. No
cleanup, claim release or session stopping. Preserve evidence and notify parent.
