# Saved workspace f520 index disposition

The saved evidence supports a separate validation/consolidation **without another
Nix update**. The original UPDATE remains exit1; this is neither a rewrite of
that result nor execution authorization. Only saved files were examined after
the required current/envpair/own ready Astra/xhigh/workspace_write roster32 check.
No live repository, index, tool, store, guard, Nix or peer inspection ran.

## Exact index proof

Inputs are `workspace-consumer-f520-execution-preparation-v1/effects-v1/update/`
`before.index` and `after.index`. The retained decoder SHA256
`45ebb02044891dfb65a873454d275c950a1ac6ed29407bbe3f09608f21686914`
was read and applied in memory to those saved bytes only, without imports that
write caches. Both indexes are version2/count57420 with valid SHA-1 trailers.

| Field | Before | After |
| --- | --- | --- |
| Raw bytes | 10548090 | 10548067 |
| Raw SHA256 | `7b2e831c8b9ddfde0b9c3e91a8b685a566067bcbaf2c608270c3a22edbee2ff4` | `9ac6197c84526dee2c9e6dcde9dfbb796b13a3fd410376a6059502b092ec2d03` |
| TREE payload bytes | 295018 | 294995 |
| TREE root | count57420, children9, tree898b7215fe4f8011089ffc2b237333a3ab8fe5e2 | count-1, children9, no cached tree ID |
| Valid trailer SHA1 | `ed8a3e8f0c0afea31ae0f8406e280b163039c81a` | `7f421dec2107a7ec26831801e37f34d00c0d926a` |

Exact byte-region comparison, offsets zero-based/half-open:

- Header `[0,12)` and entire entry region `[12,10253044)` are byte-identical.
  All57420 decoded paths, object IDs, modes, stages, flags/extended flags and
  all ten stat-cache fields match. Entry-region SHA256 is
  `9aa26e471a2b1154e8d6811774192033bd675f219ea7116017f8716ec8438999`.
- TREE is the sole extension. Its header `[10253044,10253052)` changes only its
  payload length. The root record shrinks from29 to6 bytes: count57420 becomes
  -1 and its20-byte cached tree ID is omitted; child count9 remains unchanged.
- The remaining294989 TREE payload bytes are identical after that23-byte shift:
  before `[10253081,10548070)`, after `[10253058,10548047)`. All5948 child nodes
  match; SHA256 `2a1d236705216ddfd13a1be28c939873c747fd4504d2715c6869362c7555408f`.
- Only the length/root record and correctly recomputed trailing checksum differ.
  Before decoding equals saved PREPARE after-index inventory; after decoding
  and semantic flags equal both saved UPDATE snapshots.

This proves derived TREE-root invalidation only for **this exact pair**. The
historical `workspace-consumer-c31-index-continuation-v1/parent-index-byte-equivalence-v1.json`
describes the same pattern for6cc→c823, but was not used as a blanket exemption.
No writer or cause is attributed from timing.

## Generated inputs and bounded continuation

Saved `021-scopedUpdate/command.json` records the sole scoped Nix update exit0
in51.121811s. All39 saved command receipts record joined/empty groups, no signals.
The aggregate failed in65.592097s on raw-index equality. Preserve summary SHA256
`dc6de08282bd22e3c06307329a426a1506d637964af534d1bcebabe892cc7747` and command
SHA256 `37c8544eb908e4c547a736f4c0964b711e564ce11af91e0411442a90132fa93a` unchanged.

Saved generated lock JSON equals the complete expected35-node JSON. Only the
dev-workspace node changes: locked revision/NAR/time and original revision;
its inputs, every other node and top-level graph fields remain unchanged.
Saved flake.nix equals the prepared URL candidate and is unchanged by UPDATE.
The saved620-file manifest has the same path set and all modes as its original;
only the two owned files change blob/size/hash. Their saved bytes match the
manifest's blob/hash records. Exact generated SHA256 values are:

- flake.nix: `57a0812ae8c29a21bd772b0e1752f2a39cd7d1577b77a6fc90b6443d61676c3e`
- flake.lock: `392ea143231c416968142a78b6084369ac18f60c4b053410e93e1e62df96f932`

Saved postflight records unchanged HEAD0c/tree898b, own feature/preservation
refs and branch. These are historical observations, not current-state claims.
Parent may bind this exact index equivalence and generated pair into the existing
no-Nix validation/consolidation route, with fresh ordinary preconditions at its
separate release. Keep the original baseline expectations; add this specific
accepted post-update pair rather than globally refreshing them. Still-unrun
diff/whitespace, current source/index/ref/remote/tool checks and normal hooks
remain required before the two-file consolidation. Unexpected further drift
stops. No index restore, reset, new framework, source change or Nix repeat is
needed to address this failure. No design amendment is required; session stays open.
