# A/B supplemental verification-receipt diagnosis

Exact session binding verified; both environment markers absent. A remains
c1f415ad5602c23e6443cced73cb59267a796f05/tree7e3523236dc4500b68a008398305b2290beabcc8;
B remains d819ad044ef7fcc7bb4a111dc7676fe251383249/tree6f1f05da60b09743d3716eb1a0adf794b90cf5a3,
clean. Source/ref freeze preserved. Diagnosis used completed artifacts and bounded
read-only store/GC queries, with no tests, builds, realization, GC, CI, process or
service mutations. Original receipts were not modified.

## Finding

All six build batches exited0, and both non-building flake checks exited0.
Existing evidence binds successful execution to exact source/input selections and
17 top-level derivation/output pairs. It does not contain the requested complete
recursive derivation or output-reference/NAR inventories. Supplemental collection
stopped at the FIRST A derivation, with empty JSON files and exit1; B graphs were
never reached. This is a receipt gap, not a failed test.

The two named A paths are both physically absent and invalid now:

- /nix/store/243hfgwrjhhqs1az79zlgii3ng6f1rk3-codex-web-checks-0.0.0.drv
- /nix/store/ja5y7gpgby3gljmgd5g235w4707kps92-codex-web-checks-0.0.0

The generic-source A derivation/output are also absent. Across all17 recorded
entries,7derivations and4outputs remain valid;10derivations and13outputs are
absent/invalid. [Exact validity snapshot](implementer1-ab-receipt-validity.json)
records every path. The surviving outputs are B session-creation, ruby-source-filter,
host-module and ruby-verification. The Ruby aggregate output is intentionally an
empty marker file (nix/ruby-checks.nix93–96), not a standalone copied shard manifest.
Its successful build log and dependency identities remain relevant evidence.

Available GC evidence does not establish causality: system nix-gc service/timer
inactive with no recorded start/trigger timestamps; bounded system/user service
journal and daemon GC-filtered journal since18:00UTC returned no entries. Current
client settings min-free0, keep-derivations=true, keep-outputs=false describe this
client now, not all historical daemon or external actions. No exact deletion
record was found. Do not label the loss 'caused by GC' from absence alone.

## Evidence still available

Under verification-build/ab-d819ad04:

- 00-inventory.txt binds exact clean heads/trees and Nix2.34.9; metadata-A/B.log
  and preserved A/B-flake.lock bind source NARs and full locked flake input graph.
- eval-checks-A/B.log bind selectors to outputs (2A/28B, including13Ruby shards).
  These are output-only maps, despite the packet requesting drvPath+outPath.
- Six successful build-*-results.json files and selected-derivations-and-outputs.tsv
  retain17exact top-level drvPath/output pairs. Separate .status files show exit0
  and elapsed seconds A50.884, B Ruby294.295, package242.069, VMcore694.532,
  archive885.895, creation1975.311. Flake evaluation exits0 at1.355s/41.003s.
- build-A.log names the exact .drv, runs checkPhase, reports browser92/92pass and
  reaches fixup of the exact recorded output; final JSON matches build-A-results.
  The successful result is historically bound even though its marker output is gone.
- receipt-1 and output-info retain exact path-not-valid stderr/status and empty
  JSON. Repeating those same store-path-only queries cannot recreate missing DRVs.

## Minimal recovery plan (NOT EXECUTED; lead decides)

A source-based derivation query can reinstantiate missing .drv metadata and emit
its recursive graph WITHOUT realizing check outputs. Force evaluation rather than
reuse an eval-cache root pointing at deleted dependencies; disable import-from-
derivation so any implicit build request fails closed. Use the same frozen Git
worktrees and lockfiles, with no input/lock changes. Save fresh receipt artifacts,
never overwrite receipt-1. This can succeed only if required source inputs are
available; missing inputs/IFD or changed root identities must stop, not trigger a
fallback build.

Proposed first exact command (new artifact directory chosen/created by lead):

```sh
A=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/codex-web
nix derivation show --recursive --offline --no-update-lock-file --no-write-lock-file \
  --option eval-cache false --option allow-import-from-derivation false \
  "$A#checks.x86_64-linux.default" "$A#checks.x86_64-linux.generic-source" \
  > "$NEW_RECEIPT/A-recursive-derivations.json"
```

Immediately compare both root drvPath and output paths to the ORIGINAL successful
build-A-results.json. Require exact243hfg.../ja5y7... and6zfz.../dvxk... matches.
Then the same command form for B's15 selected roots:

```sh
B=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace
nix derivation show --recursive --offline --no-update-lock-file --no-write-lock-file \
  --option eval-cache false --option allow-import-from-derivation false \
  "$B#checks.x86_64-linux.ruby-verification" "$B#checks.x86_64-linux.package" \
  "$B#checks.x86_64-linux.codex-package" "$B#checks.x86_64-linux.ruby-source-filter" \
  "$B#checks.x86_64-linux.host-module" "$B#checks.x86_64-linux.host-auth-benchmark" \
  "$B#checks.x86_64-linux.host-package-contract" "$B#checks.x86_64-linux.extension-catalog" \
  "$B#checks.x86_64-linux.agent-team-catalog" "$B#checks.x86_64-linux.user-namespace" \
  "$B#checks.x86_64-linux.generic-source" "$B#checks.x86_64-linux.host-module-idempotency" \
  "$B#checks.x86_64-linux.session-recovery-boot" "$B#checks.x86_64-linux.session-archive-lifecycle" \
  "$B#checks.x86_64-linux.session-creation" > "$NEW_RECEIPT/B-recursive-derivations.json"
```

Require every reconstructed root/output pair to match original successful JSON,
recursive input-derivation closure completeness, and all13Ruby shard identities
through the aggregate graph. Source inspection and Nix help support this plan;
no source evaluation/reinstantiation was run during diagnosis. If duration is
uncertain, lead should assign a fresh bounded receipt-only utility, not a build.

A recovered derivation graph proves build instructions/input identities; it does
NOT recreate absent output bytes, output NAR hashes or runtime reference closures.
For the4surviving outputs, ordinary nix path-info --json --recursive can capture
current output receipts without realizing anything. For absent outputs, complete
output NAR/reference evidence cannot be recovered from a normal input-addressed
.drv alone. A separately authorized read-only cache metadata lookup might supply
it if such outputs were published; availability is unproved. Otherwise lead must
explicitly retain this historical evidence limitation or authorize a distinct
artifact recovery later. No successful test should be rerun merely to repair a
missing graph receipt, and no new reconstruction is a replacement test pass.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-codex-thread-retries/
