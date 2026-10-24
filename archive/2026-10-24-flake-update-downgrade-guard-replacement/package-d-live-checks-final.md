# Prepared final configuration operations

Prepared only against final local source. Execute only after the affected review
and provider-first/consumer publication; root selects serialized fresh Luna/low
operations. Do not launch alongside C or repeat an existing attempt. Original
7ba drivers/manifests/review/failed attempts remain unchanged.

| Artifact | SHA-256 |
| --- | --- |
| `package-d-post-review-final.py` | `b77afa62c1d70d7f17d0aeee71b5da313d94d90576a26fb184762046187d8d71` |
| `package-d-verification-manifest-final.json` | `4bbac7e990b115719a773b65403383bc2183a361daee16a5454d6f3ba2411c06` |
| `provider-runtime-probe-final.sh` | `6b4e603e92b61311d5ed41358f0d1314a7698afc20015038fb4868a0e30cb464` |

Provider: `github:vpsfreecz/confctl/bdaed19e901237e05bd0a779f368e76cb311143f#confctl`.
Config heads: vpsFree `7b0609cf41fc9fe54b6d09129246ff100fb4197a`,
org `4352f16fb967e3b9da829972c9799157badd0494`. Manifest binds exact Git
trees/blobs/workflows/locks, full input graphs, original/transformed shell blocks,
probe and driver. Historical prior remote observations in
`package-d-branches-final.json` are explicitly distinct from local heads.

C's final startup owns
`/tmp/flake-update-guard-2026-10-24-final-provider-1/startup/confctl-package`.
After that operation succeeds, set D_PROVIDER_RECEIPT to its actual
`startup/receipt.json`. The D driver requires successful status, exact P,
package output, wrapper hash and packaged Nix path, then retains that same
provider through its own owned indirect root and captures its recursive closure.
It does not treat the earlier 7ba or precommit candidate receipt as final P.

Give each watcher the following setup and only its assigned stage command.
Canonical cwd is `/home/aither/workspace/ai/vpsfree.cz`. Supply GITHUB_TOKEN
privately in the environment; no tracing or environment dump.

```sh
set -euo pipefail
: "${GITHUB_TOKEN:?Provide through the private environment}"
: "${D_FINAL_REVIEW_RECEIPT:?Set the actual completed affected-review report path}"
: "${D_PROVIDER_RECEIPT:?Set the successful final-P C startup receipt path}"
D_FINAL_DRIVER=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-d-post-review-final.py
D_FINAL_ROOT=/tmp/flake-update-guard-d-final-2026-10-24-1
D_FINAL_MANIFEST=4bbac7e990b115719a773b65403383bc2183a361daee16a5454d6f3ba2411c06
```

Each line below is a separate root-assigned operation, not an unattended batch:

```sh
python3 "$D_FINAL_DRIVER" runtime vpsfree-cz-configuration --root "$D_FINAL_ROOT" --review-receipt "$D_FINAL_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_FINAL_MANIFEST"
python3 "$D_FINAL_DRIVER" runtime vpsadminos-org-configuration --root "$D_FINAL_ROOT" --review-receipt "$D_FINAL_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_FINAL_MANIFEST"
python3 "$D_FINAL_DRIVER" project vpsfree-cz-configuration --root "$D_FINAL_ROOT" --review-receipt "$D_FINAL_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_FINAL_MANIFEST"
python3 "$D_FINAL_DRIVER" project vpsadminos-org-configuration --root "$D_FINAL_ROOT" --review-receipt "$D_FINAL_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_FINAL_MANIFEST"
```

Each stage creates a fresh exact-head SSH clone in its owned directory and
disables push. Runtime stages use actual old config shells and the pinned inner
provider, preserving all Ruby/Bundler variables; vpsFree probes `nixpkgsStable`,
org `nixpkgs`, both with settings/channel outputs. Actual binary/hash/bundled Nix
must equal the verified final provider artifact. C's final IRC stage separately
exercises its real inherited RUBYOPT/Bundler environment and hooks; no harness
clearing is applied to any supported invocation.

Project stages execute all actual workflow shell bodies, retaining channel
selectors, llm-agents condition/post-check, dependency/tests and ordinary commits.
The manifest records exactly three removed lines per workflow: its final push
and two hosted-runner sudo GC-root mkdir/chown lines. Read-only user ownership,
directory and write/search preflight must pass again before those setup omissions;
there is no sudo shim or privileged host preparation. Hosted checkout/installer/
cache differences are explicitly recorded. Every other shell byte is retained.

The workflow's own original baseline copy executes before added Nix/dependency
evidence preparation. Each successful baseline/final stage captures metadata,
archive and complete recursive source closure, roots all archived sources, and
retains the exact old dev-shell output plus recursive derivation/runtime closure.
Final-worktree source receipts are labeled as such; committed final lock graph
and HEAD snapshot are recorded separately. The retained final workflow check
validates `git show HEAD:flake.lock` against the original external baseline.
No push or remote ref mutation is part of verification.

Known guard rejection 3 remains a nonzero `policy_rejection`; unknown evidence
remains an `evidence_error`. Fixture, workflow and runtime errors remain distinct
failures requiring parent diagnosis. Step snapshots do not claim whole-job
rollback; earlier accepted commits may remain. Raw token output is redacted and
fails. Unexpected local kernel builds interrupt only the owned group and
escalate 125, including a reported build observed at command exit. No automatic
retry, quiet timeout or cleanup. Return receipts/status/log paths and unfinished
identities to root. Root owns acceptance and B/D diagnosis.

Preparation-only Python compile, JSON/hash assertions and Bash syntax for all
12 workflow bodies plus probe/full-RSpec scripts passed; see
`package-final-verification-preflight.log`. No final operation was executed.
All seven final patterns are rerun; older source results remain historical.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
