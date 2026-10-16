# Annotation verification baseline

The three companion contract files match the six final KB candidates. The full
191-page checker remains blocked by two pre-existing source/contract differences
outside those candidates; no unrelated pages or contracts were changed.

Baseline contract revision: `ce2c8cd9358c3636e5d39343e595df813a0b197f`.
The original `kb-source` has 114 Czech and 77 English pages. The final corpus
preserves that complete identity set and substitutes exactly the six candidate
files; every other file is byte-identical to the source snapshot.

`networking.host-addresses.add` is expected once and present zero times on both
`cs:navody:vps:ip_adresy` and `en:manuals:vps:ip_addresses`. Running the existing
checker with the original full source and untouched baseline contracts
reproduced exit 1. The final full corpus has precisely the same count failures.
See `kb-annotation-baseline-check.log` and `.status`; baseline contract files and
original-source candidate index are preserved in `kb-annotation-baseline/`.

Independent discovery comparison continued past the checker's early count
abort. Both baseline and final corpora contain 216 discoveries. Each has the
same four issues: two unclassified current IP-address paragraphs and two stale
inventoried variants of those paragraphs. Their texts differ from the recorded
versions and lack the expected host-address tags. No other discovery, text,
paragraph, path or exception-reason mismatch was found. No issue belongs to the
six changed pages.

Both Impermanence candidates have dataset creation count 2, mount count 1,
rescue count 1 and Features count 1. Both User Data candidates retain one tag
for each of their three existing paths. Neither main NixOS candidate has an
annotation. All six page counts match the final companion contract, all paired
tags are nonempty and well formed, and their independent discoveries match.

The comparison ran with the pinned Ruby from the rooted development-shell
profile, without a Nix daemon operation. `kb-annotation-baseline-evidence.json`
contains exact differences and six-page counts. The read-only diagnostic is
`kb-annotation-baseline-audit.rb`; it uses the repository's unchanged canonical
discovery module and reads baseline contracts directly from Git.

To reproduce the scoped and baseline evidence from the contract worktree, run:

```sh
nix develop --profile result/config-imports-dev-shell --command ruby \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-12-streamline-vpsadminos-config-imports/kb-annotation-baseline-audit.rb
```

Static annotations, checker tests and navigation/source fingerprint validation
remain separate lead-owned checks. A full-corpus pass cannot be claimed until
the unrelated IP-address pages and their inventory are reconciled under a
separate scope. This finding does not authorize that reconciliation.
