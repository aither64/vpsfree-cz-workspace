# Successful 37 batch receipt capture

Historical successful commands/statuses/source identities and log SHA256s are
preserved in [receipt.json](receipt.json). This capture grants no new acceptance
or reuse claim. Only the passed collection, client-flake and package logs were
read; failed creation logs were not opened.

| Passed check | Exit | Seconds |
| --- | --- | --- |
| Collection probe | 0 | 23.396 |
| A6e469 flake | 0 | 60.488 |
| B37 package | 0 | 1396.193 |

Exact committed A tree is `b1737d05f35c391baca39296833d4dbe0e1e6d82`;
B37 tree is `149b827753359c9ea9f140895b77dbac2f630f31`. These come from immutable
local Git objects named by the original batch receipt, independently of mutable
B worktree HEAD. Original commands and original batch result are retained.

The main check/package derivations and outputs are unavailable locally. Twenty
of22 logged drv paths are absent; their cause of absence is not established.
Do not regenerate them under this package. In particular, full input receipts
for A’s successful default/generic checks and B’s successful package cannot be
certified from this capture. The collection log records no Nix check drv/output.

Two logged manifest derivations remain. Their full local recursive derivation
JSONv4 contains924 derivations. Original local ATerm drv files are archived;
the complete input/output identity index and available local NAR/registration
metadata for218 source/output paths are retained. Another872 paths are absent.
This supplemental manifest closure does not replace the missing successful
check/package closures.

Raw derivation JSON/ATerm environments are private local artifacts (0700 parent,
0600 raw files), not printed here or copied to product repositories. See
[artifact hashes](manifest.json), [local capture](proof/local-input-capture.json),
[missing drv inventory](proof/log-derivations.json), and
[committed source proof](proof/committed-source-identities.json).

No source/pins/refs changed. No evaluation, fetch/network, build/test, CI query,
rerun, runtime-private-data inspection, claim/deployment/merge or lifecycle action
was performed. Main owns later exact derivation/full-input comparisons and any
missing-evidence or build choice; equal trees or patches are insufficient.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-workspace-session-naming/>.
