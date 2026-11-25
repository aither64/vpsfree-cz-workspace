# Final small prerequisite batch

Fresh installed watcher Luna/low/full_access; catalog f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d from package22x45q9snm46qw95c1zjsbavifv9fki9-dev-workspace-0.2.0, native utility dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569. Read monitor/repo guidance. Confirm dev-session current from EXACT trackingdir /home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy (not workspace root), both env absent matches binding.

Cwd for both commands: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin
Frozen source: compare `git diff --binary c02f56e1c45d6dfeb4f5fbfbee486ee584ef1460` (includes staged+unstaged; bare `git diff` is NOT source identity) against preserved nov13-localization-working.diff. Original basec02f56e1, current HEAD2a1f44119730650ec89c1fc22cf4c9fdef766f0a treef4a9d5b18805b23f8c22a493ce4b2f74b508f161 (normal commits complete; source unchanged) plus same full deltaSHAf4ebdc0309d77d44a25b87bc90d6c51408c0c55e4d20f7ff3b7929df4ccdc703.
Run these two literal argv sequentially, exactly once each, STOP on first nonzero. No trailingdot/extraoperands.

```json
[
  "env",
  "VPSADMIN_PLUGINS=none",
  "nix",
  "develop",
  ".#api",
  "--command",
  "bundle",
  "exec",
  "rspec",
  "spec/migrations/20261030180000_add_incident_escalation_spec.rb",
  "--seed",
  "50834",
  "--fail-fast",
  "--format",
  "documentation",
  "--format",
  "json",
  "--out",
  "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/nov13-migration.json"
]
```
```json
[
  "env",
  "VPSADMIN_PLUGINS=all",
  "nix",
  "develop",
  ".#api",
  "--command",
  "bundle",
  "exec",
  "rspec",
  "--options",
  "/dev/null",
  "../tools/api-schema-export/safety_spec.rb",
  "../tools/api-schema-export/snapshot_spec.rb",
  "--seed",
  "50834",
  "--fail-fast",
  "--format",
  "documentation",
  "--format",
  "json",
  "--out",
  "/home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/nov13-exporter-safety.json"
]
```

REQUIRED: redirect complete stdout+stderr from command1 to nov13-migration.log and command2 to nov13-exporter-safety.log; record actual native exits in matching .exit files. Use shell native redirection and explicit saved exit, not piping without pipefail. These logs are in trackingdir. Record start/end/elapsed and parse each native RSpecJSON. Existing source may not be edited, no diagnostics/retry/sourcegeneration, no dependencies beyond declared small API shell, no guest/image/CI/lifecycle. Expected minutes; no elapsed-only kill. Escalate actual unexpected owned kernelbuild. Finish/join native sessions before reporting.
