# Profile deployment observation

- Result: passed; recorded exit status `0`.
- Operation: parent-launched `workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-reboot-recovery-fix/workspace`, claim `2ab59c0b-617e-4b9b-b741-ef3925a063d4`.
- Tested revision: `1deb88301418722ed1aebeaa2bebafd9b2e007d8`.
- Log: `work/2026-10-30-reboot-recovery-fix/profile-deploy.log`; status: `work/2026-10-30-reboot-recovery-fix/profile-deploy.exit`.
- Bounded evidence: log reports “Codex App Server protocol contract is compatible”, “local semantic observation protocol contract passed”, “compatible Codex: 0.165.0”, then the installed generation path `/home/aither/.local/state/dev-workspaces/codex/generations/215` and package `/nix/store/rxn2q52znanqmvjwkdilfj24yrg95jpq-dev-workspace-0.2.0`.
- Timing: first watcher observation at 2026-10-30 22:56:23 UTC found no exit file; exit `0` was present by 22:57:31 UTC. Watcher-observed interval: 68 seconds. Command start time was not available from the supplied status files.
- Execution settings: assignment specified `gpt-6-luna/low`, full access, approval never. This runtime exposed no tool or metadata for independently inspecting the launched model/policy; those settings could not be independently verified here.
- No operation remained running; no cancellation or retry was performed.
