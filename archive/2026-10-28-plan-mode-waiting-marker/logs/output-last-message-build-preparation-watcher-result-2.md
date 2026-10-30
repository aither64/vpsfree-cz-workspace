# Build preparation watcher result 2

Result: **passed**. No deployment, copy, activation, or switch was performed.

- Application command: `nix build 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-plan-mode-waiting-marker/workspace?rev=398dc7bab89ee51bcc77d23a5acc52c7e02878c1#default' --no-link --print-out-paths --print-build-logs`
  - Tested HEAD: `398dc7bab89ee51bcc77d23a5acc52c7e02878c1`
  - Exit: 0; elapsed: 730 seconds
  - Output: `/nix/store/g650vgjpzvyifjmb1j44pc5bby3522z4-dev-workspace-0.2.0` (expected)
  - Log: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-plan-mode-waiting-marker/logs/composed-app-build-2.log`
  - Bounded evidence: package integration tests included 48 runs/317 assertions, zero failures/errors; another group had 131 runs/1883 assertions, zero failures/errors and 3 skips. Go checks completed; Nix reported `checkPhase completed` and produced the expected output. There is a warning about inability to create PATH aliases under `/build`.
- Configuration command: `nix develop -c confctl build --yes cz.vpsfree/machines/aitherdev`
  - Tested HEAD: `b3b933bf6f9fc9f7f533b3f4e06775defd8879da`
  - Exit: 0; elapsed: 115 seconds
  - Derivation/output matched expected: `/nix/store/ia5gh8wr85mp6crbgi16nwf7wn66zz80-nixos-system-aitherdev-26.05.20261026.718f670.drv` -> `/nix/store/r4rd3qyn52z1bipbln8kdh43mjd2wb1k-nixos-system-aitherdev-26.05.20261026.718f670`
  - Generation: `2026-10-29--19-25-31`; listing reports presence/current `build`, kernel `6.18.57`, and pinned component versions. Metadata: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-plan-mode-waiting-marker/vpsfree-cz-configuration/.confctl/generations/cz.vpsfree:machines:aitherdev/2026-10-29--19-25-31/generation.json`; its `toplevel` is the expected output and `auto_rollback` is `/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb`.
  - Log: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-plan-mode-waiting-marker/logs/configuration-system-build-2.log`; generation listing log: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-plan-mode-waiting-marker/logs/configuration-generation-list-2.log`.

Progress JSON: `/home/aither/workspace/ai/vpsfree.cz/work/2026-10-28-plan-mode-waiting-marker/logs/build-preparation-progress-2.json`.
