# Final composed checks and artifact builds

RELEASED 2026-10-22 after all six A/B build batches, both no-build checks and selector inventories passed. A/B supplemental graph receipt inspection failed on invalid old store paths; implementer1 owns read-only diagnosis separately, with no test rerun. This batch does not reuse those absent outputs and must preserve its own complete roots and receipts. Activation remains gated on evidence reconciliation. This utility owns one related operation batch;
no copy, activation, claim, merge, lifecycle or service action is included.

Fresh gpt-6-luna/low verification watcher under dev-session-monitor skill;
retained catalog840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa,
utility dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12, matching behavior
TOML in selected4cn1hh88xdpql5jp9pyrnf5fvnqsc829 package. Actual execution
must be danger-full-access, approval never. No nested agents or role changes.
Verify exact session2026-10-22-codex-thread-retries/workspace
/home/aither/workspace/ai/vpsfree.cz via current and both optional markers.

Read workspace AGENTS and required verification/deployment routes, W/C AGENTS,
verification-build-brief.md and confctl-generation-receipts.md fully. The latter
binds exact pinned confctl7bee58a5 commands and generation identity. Guidance
missing/mismatched means stop, never substitute a guessed command.

Frozen sources:
W=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/workspace
C=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/vpsfree-cz-configuration
Whead ebf6ab35c7754f9ac2e5474959259fdcef24a7c8,
tree e46dfa5027a2e34cc083e6d41da78f7c60106d3e,
source NARsha256-SfwiR8s4bntwC599gAeuwlaZMHV8Mx59xv/6lP/yPig=.
Chead81d0e68c52762d3804e00e4c4ef99a421bafc05f,
tree27b3b4425c9104269b5909a5d935eb94c6c954df,
source NARsha256-CLmAqgX1jRsrvGT9N6JPTHFm4Atabo/megfN/NKpb+U=.
Both select B d819ad044ef7fcc7bb4a111dc7676fe251383249 and
A c1f415ad5602c23e6443cced73cb59267a796f05; extension767dfd58 preserved.
Full graph/history/tree reconstruction receipts: final-pin-inspection-d819.json,
c-d819-mechanical-review-reuse.json and c-repin-d819ad04.json. Independent source
review passed, native4 passed. This is final exact-source verification, not reuse
of stale C/W derivations. Source must be clean at start and end.

RUN=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/verification-build/composed-81d0e68c
MACHINE=cz.vpsfree/machines/aitherdev
Create private fresh RUN, retain every full command/CWD/env/exit/elapsed/log.
Stop/report at first failure without retry/diagnosis/repair. No quiet timeout.
Unexpected local Linux kernel compilation: stop ONLY owned build and escalate;
no exception granted. Do not delete/GC data to fix disk pressure.

Authorized commands, each once:

1. Record exact heads/trees/status, full lock graphs, Nix/system and space.
   Capture nix flake metadata --json --no-write-lock-file for W/C, check maps
   via nix eval SOURCE#checks.x86_64-linux --json --no-write-lock-file --apply
   'checks: builtins.mapAttrs (_: drv: { inherit (drv) drvPath outPath; }) checks'.
   Verify names against four W/eight C names below, report coverage mismatch.
   At each respective root run nix flake check --no-build --no-write-lock-file
   --print-build-logs.
2. cwd W, run final deployment contract using its declared shell:
   nix develop "$W" -c bin/check-dev-workspace-deployment --workspace-root "$W"
   --configuration-root "$C". An exact final source quick receipt with command,
   source and result may be retained rather than repeating the same source test;
   inspect c-repin-d819ad04.json and report whether reusable. Do not assume reuse
   of a Nix check derivation from a plain Ruby quickcheck.
3. cwd W:
   nix build --no-link --no-write-lock-file --print-build-logs --json
   .#checks.x86_64-linux.deployment-contract
   .#checks.x86_64-linux.agent-instructions
   .#checks.x86_64-linux.agent-team-policy
   .#checks.x86_64-linux.cluster-provider-composition
4. cwd C:
   nix build --no-link --no-write-lock-file --print-build-logs --json
   .#checks.x86_64-linux.nix-store-cleanup
   .#checks.x86_64-linux.alert-recipients
   .#checks.x86_64-linux.infra-monitoring-rules
   .#checks.x86_64-linux.infra-monitoring-config
   .#checks.x86_64-linux.vpsf-status-prometheus-rules
   .#checks.x86_64-linux.vps-autostart-prometheus-rules
   .#checks.x86_64-linux.process-count-prometheus-rules
   .#checks.x86_64-linux.newadmin-prometheus-rules
5. cwd W, exact composed application output, preserve out-link:
   nix build --no-write-lock-file --print-build-logs --json
   --out-link "$RUN/workspace-package" "$W#packages.x86_64-linux.default"
   This is the same derivation as W's vpsfree-dev-workspace alias; no duplicate
   alias build. If prior check realized it, request output receipt/cache reuse.
6. cwd C explicitly (nix develop does NOT change cwd):
   CONFCTL_TTY=0 nix develop "$C" -c confctl --color never build --yes "$MACHINE"
   Only after exit0 take the exact emitted 'Built generations:' name for this
   machine. May reuse matching older generation; do not choose latest/current,
   clock time, directory order or numeric offset. Then execute the exact local
   generation listing and Ruby receipt collection from
   confctl-generation-receipts.md, with RUN/GENERATION_DIR literal selected values.
   Require embedded clean C revision81d0e68c, inputs_info equality and runtime
   d819. Retain generation.json, links, toplevel and rollback closures, complete
   metadata and hashes. No status without --generation (it builds).

For selected checks and application/system outputs preserve selector->drvPath/
outPath, nix derivation show --recursive and nix path-info --json --recursive
receipts, full source/input graphs, successful cached/substituted results and
exact output identities. Native/version unchanged; no native or real-provider
requests. Do not rerun A/B checks. C/W sources/Git remain frozen; confctl's own
ignored local generation metadata is expected, not a source change to fix.

No copy-only command, activation, remote status/health, provider switch, profile
selection, claim/release, integration, lifecycle, broad process stop or cleanup.
Do not edit generation receipts or source to silence mismatches. Parent owns
all deployment commands and decisions. Return passed/failed/incomplete, exact
case/check coverage/exits/elapsed, profile package store path, exact system
generation/toplevel/rollback path, all receipts, bounded failures and any running
owned process. Write result.md under RUN only; keep full failed evidence.
