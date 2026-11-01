# C0311 minimal postreview plan — released; execution recorded separately

Lead accepted the affected final review with no findings and released both
checks plus conditional own-ref publication. The commands and limits below
remain the accepted plan; actual results and original failures are separate receipts.
Exact candidate `e468ca48406bde1bd99cc42a05e1832fb42162f4`, base
`9113caa0915b2908373ecd616f8f752e779ed4c9`, tree
`13db539707ae88c8635e194ca04f3e36c6e3d76a`, clean registered
`vpsadmin-webui-0311` / `dev/vpsadmin-haveapi-0311`.

Two sequential batches use existing repository/Nix commands. Fresh identity,
head/clean/tested-hash/lock and capacity checks precede them. No repeated quick
gate, dependency install, focused tests, browser, SDK or baseline campaign.
Root0.31.1 and current main BFF installs/audits are already complete; BFF package
inputs are its unchanged security manifest/lock/hash from911, not old C31.

Use CPU60–63/nice5, Nix maxjobs1/cores2 and explicit
`/run/current-system/sw/bin/bash`, login false. A0 owns the utility slot now;
use the released visible parent fallback if it remains busy, preserving each
handle/full log/exit/elapsed with blocking waits at most50s. Do not start another
watcher or wait for capacity. If lead releases a free slot instead, resolve a
fresh retained Luna/low watcher through the monitor skill; do not reuse one.

## Batch 1: required aggregate and normal production build

Run from the own0311 worktree under its pinned toolchain:

```sh
taskset -c 60-63 nice -n 5 nix develop \
  --profile <C0311-records>/toolchain-profile \
  -c bash -ec 'npm run ci:tests; npm run build'
```

With bash `-e`, build executes only after the aggregate passes. The package's
declared `ci:tests` is `npm run test:scripts && npm run test:bff && npm test`.
This unavoidably repeats the quick BFF57 inside the ordinary required aggregate;
do not add another manual script/BFF/unit invocation. Repository guidance calls
for full unit/build verification, and the fresh119-path product/BFF baseline
changes inputs since the old C31 full-unit run. Run this aggregate once after
review rather than claim its old full result for the new source. The generic
library's version-only delta alone does not justify another campaign.

Expected8–15minutes, depending on contention; this is an estimate, not a timeout.
Capture full log/status/time and actual test counts. Check the resulting normal
`dist/build-info.json` is exact e468, dirty false. Do not alter or rebuild in
legacy mode; the normal build compiles required BFF bootstrap.

## Batch 2: exact normal Nix package/check outputs

Only after Batch1 passes:

```sh
taskset -c 60-63 nice -n 5 nix build --max-jobs 1 --cores 2 \
  --print-build-logs --json --out-link <C0311-records>/nix-result \
  .#frontend .#bff \
  .#checks.x86_64-linux.provenance \
  .#checks.x86_64-linux.source-contents \
  .#checks.x86_64-linux.package-contents
```

Expected1–5minutes if the ordinary pinned dependencies substitute. No VM/kernel
output is selected. The normal persistent out-links retain all five actual
outputs immediately after success; retain the existing source/toolchain roots
as well. Do not deploy missing paths or treat historical paths as new outputs.

Record the JSON build results, each actual derivation/output, frontend/BFF
metadata, NAR/reference identities, full locked flake metadata, complete
recursive derivation/input graph (`nix derivation show --recursive` for actual
derivations), recursive output closure (`nix path-info --json --recursive`), and
registered normal root map. Verify both package metadata files agree at exact
e468/dirty false; source/provenance/contents checks bind this current package.
Retain roots for later lead/E3 use without switching any live path.

## Stop and reconcile

On a real failure, stop at that batch, retain original logs/artifacts and report
diagnosis before retry or source repair. Stop only an owned unexpected actual
kernel compilation under the workspace procedure; modules/initrd activity alone
is not kernel compilation. No generic quiet timeout or foreign-process control.
If source/lock/head/input identity differs, stop before dependent execution.
Resource contention is a wait, not failure; keep updates/waits interruptible.

After success, recheck exact source/head/clean/locks/hashes, owned command effects
and roots. No automatic browser repeat: old3/6+5/6 and separate paired expiry
passes remain historical, with no synthetic6/6/cause/preexisting claim. New actual
deployed TLS/BFF/login acceptance belongs to lead/E3 after remaining A gates.

Own new-ref publication requires lead's postreview/check release and fresh
canonical main/own-ref/SSH/hook/clean boundaries. If released and checks pass,
publish only exact e468 to `refs/heads/dev/vpsadmin-haveapi-0311` by one explicit
no-force refspec; independently verify remote, capture comparison and perform
bounded exact-head CI trigger discovery. No dispatch or CI wait, PR74/PR63
rewrite, default merge, source move, runtime/provider/cluster/lifecycle action.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/
