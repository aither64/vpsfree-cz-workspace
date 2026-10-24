# A/B derivation receipt recovery

RELEASED by lead after the composed build watcher exited with successful checks/builds and a separate collector setup failure;
one retained-policy utility at a time. Fresh gpt-6-luna/low with installed full
access, danger-full-access and approval never. Exact native utility config and
catalog are those in composed-build-watcher-packet.md. No nested agents.

Verify session binding and read workspace AGENTS, verification procedure,
dev-session-monitor skill, and implementer1-ab-receipt-diagnosis.md fully.
Sources are frozen A c1f415ad5602c23e6443cced73cb59267a796f05/tree
7e3523236dc4500b68a008398305b2290beabcc8 and B
d819ad044ef7fcc7bb4a111dc7676fe251383249/tree
6f1f05da60b09743d3716eb1a0adf794b90cf5a3 in the ordinary session worktrees.
Require clean source and unchanged locks before and after operation.

Use a fresh private RUN under verification-build/ab-receipt-recovery-d819.
Once only, execute the two exact source-based offline recursive derivation
commands in the diagnosis, from each source's root, with eval-cache=false and
allow-import-from-derivation=false and both lock update/write forbidden. Set
NEW_RECEIPT=RUN. Capture stdout/stderr/exit/elapsed independently. Stop first
failure; no fallback input fetch, build/realization, retry or source repair.

Compare reconstructed root drv/output paths with all17 original pairs in
verification-build/ab-d819ad04/selected-derivations-and-outputs.tsv and original
successful build-*-results.json. Every pair must match exactly. Retain complete
recursive input derivations, check closure completeness, and prove all13 Ruby
shard selector identities appear under the aggregate using the final source
and original selector outputs. Record selector->drv->output maps for all2A/28B
checks from the reconstructed graphs, with any absence explicit. Re-evaluation
is metadata reconstruction, not a new test success or preserved output proof.

For each originally recorded output still valid, collect read-only
nix path-info --json --recursive exact_output once. Missing output paths are
historical limitations: record absence; never realize, substitute or build them.
No cache lookup, network retrieval or successful test repetition. Recover any
available Ruby shard output manifest only through existing output files/paths;
do not claim the empty aggregate marker is a copied manifest. Existing successful
aggregate log already proves complete unique suite coverage.

Capture current platform via nix eval --impure --raw --expr builtins.currentSystem
and Nix version as supplementary metadata, distinguishing the original failed
pure platform query. No tests, build, CI, source/Git mutation, claim, copy,
activation, deployment, GC, cleanup or lifecycle actions. Writes limited to RUN.

Return passed/failed/incomplete for METADATA RECOVERY, exact exits/root matches,
graph and13shard inventory, complete evidence paths, available output closure
receipts and still-missing output limitation. Parent owns acceptance and preserves
all original successful test/failed receipt evidence.
