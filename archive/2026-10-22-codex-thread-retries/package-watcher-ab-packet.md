# Full A/B package verification

RELEASED after review-run3.md passed no findings and native4 passed all required
cases on exact A c1f/B d819. Fresh operation-only Luna/low watcher, not a roster
member. Read ~/.codex/skills/dev-session-monitor/SKILL.md; retained catalog
840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa selects
gpt-6-luna/low and utility dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12.
Installed execution_access full_access: danger-full-access/approval never.
Matching behavior TOML is under selected package
/nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml.

Trusted session2026-10-22-codex-thread-retries/workspace
/home/aither/workspace/ai/vpsfree.cz. Verify current exact and optional markers
both absent or both exact. Read workspace AGENTS/verification procedure and A/B
AGENTS, verification-build-brief.md (full check selectors/receipts/escalation).
This exact packet overrides historical candidate labels in that brief.

A=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/codex-web
B=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace
RUN=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/verification-build/ab-d819ad04
Use fresh private RUN; no overwriting/retry. Verify clean source exact A
c1f415ad5602c23e6443cced73cb59267a796f05/tree7e3523236dc4500b68a008398305b2290beabcc8
and B d819ad044ef7fcc7bb4a111dc7676fe251383249/tree6f1f05da60b09743d3716eb1a0adf794b90cf5a3.
C/W owner may edit ONLY their separate worktrees; A/B frozen.

Authorized related batch, each command ONCE, no retries/repairs/diagnosis:

1. Record heads/trees/clean status, Nix version/system, /dev/kvm read/write,
   disk availability. Host KVM accessible; last free108GiB. Copy A/B flake.lock
   as full semantic input graph artifacts. Run nix flake metadata --json
   --no-write-lock-file A and B, capture full outputs. From each respective
   root run nix flake check --no-build --no-write-lock-file --print-build-logs.
   Record exact check selector->drvPath/outPath maps using:
   nix eval --json --no-write-lock-file SOURCE#checks.x86_64-linux --apply
   'checks: builtins.mapAttrs (_: drv: { inherit (drv) drvPath outPath; }) checks'
   Compare actual declared names with verification-build-brief.md; stop/report
   any mismatch instead of silently omitting/expanding selectors.
2. cwd A:
   nix build --no-link --no-write-lock-file --print-build-logs --json
   .#checks.x86_64-linux.default .#checks.x86_64-linux.generic-source
3. cwd B:
   nix build --no-link --no-write-lock-file --print-build-logs --json
   .#checks.x86_64-linux.ruby-verification
4. cwd B:
   nix build --no-link --no-write-lock-file --print-build-logs --json
   .#checks.x86_64-linux.package .#checks.x86_64-linux.codex-package
   .#checks.x86_64-linux.ruby-source-filter .#checks.x86_64-linux.host-module
   .#checks.x86_64-linux.host-auth-benchmark .#checks.x86_64-linux.host-package-contract
   .#checks.x86_64-linux.extension-catalog .#checks.x86_64-linux.agent-team-catalog
   .#checks.x86_64-linux.user-namespace .#checks.x86_64-linux.generic-source
5. cwd B:
   nix build --no-link --no-write-lock-file --print-build-logs --json
   .#checks.x86_64-linux.host-module-idempotency
   .#checks.x86_64-linux.session-recovery-boot
6. cwd B:
   nix build --no-link --no-write-lock-file --print-build-logs --json
   .#checks.x86_64-linux.session-archive-lifecycle
7. cwd B:
   nix build --no-link --no-write-lock-file --print-build-logs --json
   .#checks.x86_64-linux.session-creation

Keep each full stdout/stderr/exit/elapsed separate; don't mask exit with pipeline.
Capture nix derivation show --recursive for selected drv paths and
nix path-info --json --recursive for successful output store paths. Preserve
Ruby aggregate manifest proving all13 shards exactly once and relevant successful
output receipts. No duplicate default/package aliases or native tests. Use Nix
cache naturally; no tree-only reuse claims. Each failed build stops batch/report
without rerun; retain raw logs/partial outputs. No source edits or CI wait.

Unexpected local Linux kernel compilation requires stop/escalation: cancel ONLY
the owned build process, retain logs and drv, do not diagnose/repair or kill
foreign process. No kernel/cache exception has been granted. Disk exhaustion or
unsafe fixture access escalates; no cleanup/GC. No generic quiet timeout. Report
milestone progress and retain owned command handle through completion/escalation.

No app/session state edits, diagnosis, retries, nested agents, source/refs,
claim/copy/deploy/integration/lifecycle. Only RUN artifacts allowed. Return
passed/failed/incomplete, exact command exits/elapsed/revisions, selector coverage,
drv/input/output/graph receipts, bounded failures and still-running status.
Parent resumes decisions automatically.
