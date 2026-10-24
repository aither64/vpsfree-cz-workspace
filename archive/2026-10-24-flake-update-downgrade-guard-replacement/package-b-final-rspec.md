# Prepared final exported RSpec operation

Prepared only. Run through one fresh root-assigned Luna/low watcher after the
complete affected review passes and provider P is published. No command here
has been executed. Original 195-example evidence is historical; this operation
builds final P's existing exported check once, including the two new package
regressions, rather than duplicating a direct source-suite invocation.

Frozen [package-b-final-rspec.sh](package-b-final-rspec.sh) SHA-256:
`bb04e99d3cd9c3f155ffa2d5e7ec6ff59304113bc64f0cf88283fe79b4576247`.
Canonical cwd: `/home/aither/workspace/ai/vpsfree.cz`.

```sh
set -euo pipefail
: "${B_FINAL_REVIEW_RECEIPT:?Set the actual completed affected-review report path}"
export B_FINAL_ROOT=/tmp/flake-update-guard-b-final-rspec-2026-10-24-1
export B_FINAL_REVIEW_RECEIPT
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-b-final-rspec.sh
```

The exact check build is:

```sh
nix build github:vpsfreecz/confctl/bdaed19e901237e05bd0a779f368e76cb311143f#checks.x86_64-linux.rspec \
  --out-link "$B_FINAL_ROOT/rspec" --json --print-build-logs
```

The flake check already sets `src = self` and `CONFCTL_BIN` to that source's
actual confctl package. The script verifies metadata revision P, compares
metadata/archive store paths, captures complete input source graphs and recursive
derivations, and roots every archived source under its owned output directory.
It separately retains the actual provider output and closure. The check output
has its own root, build JSON, exact derivation path/log and closure receipt.
The log must report 197 examples, zero failures and no pending cases; missing
or different coverage is evidence requiring diagnosis. This is not a retry or
inference from the earlier 195-example suite.

`status.json` binds review-report hash, exact P, final phase and raw exit status.
Metadata is checked for raw token values before writing; no complete environment
or credentials are printed. The script refuses an existing output directory and
performs no cleanup, publication, merge, VM, machine or lifecycle operation.
Retain the provider/check/source roots and all logs. Root chooses a distinct
attempt after diagnosing any failure.

Watcher must read the monitor skill and applicable guidance, verify session
identity and explicit full-access utility policy, and own the exact process
group/log/status. Interrupt that owned group on an unexpected local Linux kernel
build and escalate; no kernel workaround, quiet-build timeout, diagnosis, edits,
retry, acceptance or nested watcher. Return status, elapsed time, source/check
identity, receipt paths, bounded failure excerpt and any unfinished process.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
