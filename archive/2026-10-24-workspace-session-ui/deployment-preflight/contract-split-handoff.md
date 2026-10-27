# Resumed contract-checker handoff

Bounded implementation of the accepted `design.md` section **Contract-check
owner: selected package versus immutable native launch**. Only evidence files in
this directory changed. No product/configuration/Git mutation, candidate preflight,
build, claim, deployment, lifecycle action or other-session inspection occurred.

The original failed checker is preserved verbatim as
`compare-before-contract-split.py`, SHA-256
`75bea2e2c35f3bfc3ba9233a985157e49a48d1a309ac7c41299d4cf104616b35`.
`contract-split-original.json` binds that copy to the original watcher failure.
The old capture, failed log and historical diagnosis remain unchanged.

## Reviewable change

`contract-split.diff` is the complete original-to-current checker diff.
`compare.py` now requires complete, type-preserving selected-to-candidate
application/state JSON equality, including SQLite, archive, provider/retry and
unknown future fields. It does not default absent fields or filter unknown ones.

Separate pure helpers validate exact native launcher/executable/hash, supported
live-switch/reporting policy in all three packages, launch/registration policy1,
actual native child capacity0 and fully validated reporting argv. Complete
captured/current native argv must agree; only the existing validated reporting
executable package path may differ between launch and proposed registration.
The actual `cmp` check and fresh native/profile/marker/inventory guards remain.
Catalog capacity is not used as native launch capacity.

Raw selected/launch/candidate runtime contracts and immutable launch marker are
written to a fresh `*-raw-contracts.json` sidecar before compatibility assertions,
and retained in the successful comparison too. A failed comparison does not erase
that raw sidecar. Existing catalog/extension/machine/role comparisons were not
expanded or refactored. Source/profile/claim/cluster and ordinary host transition
checks retain their ownership; this script authorizes no activation.

The old post comparison's hardcoded9293 runtime was replaced by an explicit
runtime head argument from the future exact built receipt. No old package/output
or cached8ph baseline may be replayed. The lead supplies fresh candidate/system/
configuration/runtime identities after the current review/build gate.

## Quick evidence

`contract-split-fixtures.json` preserves raw current48011 application contract,
older immutable launch contract/marker and the previously captured native argv.
Only the proposed package/negative changes in tests are synthetic. No native
process, registration helper or candidate command is launched by these checks.

Command: `python3 -B helper_contract_checks.py`. Six tests with table variants
passed, exit0, in0.013s; full output is `contract-split-quick-checks.log`.

- Same native plus older launch succeeds while full selected SQLite1/policy1/
  archive3 capabilities remain intact.
- Loss of each selected SQLite/archive/provider/retry capability fails.
- Unknown field addition, archive/store downgrade and boolean-vs-integer contract
  mutation fail.
- Changed native launcher/executable/hash, changed complete argv/reporting
  workspace authority, capacity8/false, policy2/true and missing live-switch or
  reporting support fail.

Python AST syntax checks passed. Original-copy SHA-256 verification passed.
`contract-split-sha256.json` binds all reviewable code, fixtures, diff and quick
results. Final checker SHA-256:
`303a4ef53f1bfaa8a9a62afc209bc1528fdf906c2949267e0c265238dffb0aec`.

## Future fresh watcher commands

These are prepared commands, not executed preflight. Wait for the parent's exact
new reviewed/built output signal. Use new receipt names. No oldnz0 output.

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/capture.py \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/pre-resumed-candidate.json
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/compare.py \
  candidate /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/candidate-resumed-comparison.json \
  NEW_CANDIDATE_OUTPUT /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/pre-resumed-candidate.json
```

Parent delegates the uncertain-duration comparison to a fresh verification
watcher. Reconcile any raw sidecar from a failed run and choose a new output name
for a later authorized attempt. Refresh baseline again if live identities change.
No ownership change is implied; activation requires this session's own held
machine claim and ordinary host checks.

After authorized activation, capture `post-resumed-activation.json` and run:

```sh
python3 -B /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/compare.py \
  post /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/post-resumed-comparison.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/pre-resumed-candidate.json \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/deployment-preflight/post-resumed-activation.json \
  NEW_CANDIDATE_OUTPUT NEW_SYSTEM_TOPLEVEL NEW_CONFIGURATION_HEAD NEW_RUNTIME_HEAD
```

Scripts are frozen after this handoff pending parent results. Naming inference
limits and authenticated safe capture behavior remain as previously recorded.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>
