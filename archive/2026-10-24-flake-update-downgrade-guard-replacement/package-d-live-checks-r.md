# Prepared final configuration operations

Prepared only against final local source. Execute only after the affected review
and provider-first/consumer publication; root selects serialized fresh Luna/low
operations. Do not launch alongside C or repeat an existing attempt. Original
7ba/P/Q drivers, manifests, reviews and failed attempts remain unchanged.

| Artifact | SHA-256 |
| --- | --- |
| `package-d-post-review-r.py` | `b993cba5fc6cdf35d5f6435e5b6064922f36a18a520b72af57a071e374bf3835` |
| `package-d-verification-manifest-r.json` | `f89bbd48fe845f288de0d94e83d5c0568481d381e6a57a53d262625a58e1eebb` |
| `provider-runtime-probe-r.sh` | `f8cfba1933e13190dc644613453192dfccd9e873b4d4adb82bd7f814552a16b8` |

Provider: `github:vpsfreecz/confctl/5436d3d7c36d3d5174eab3c44e3578830749d3db#confctl`.
Config heads: vpsFree `28ce92517be0151c0bd52f7ae6e64632474888e9`,
org `949220c108d3c87341457aa96649dd92bad333b6`. Manifest binds exact Git
trees/blobs/workflows/locks, full input graphs, original/transformed shell blocks,
probe and driver. Fresh SSH observations in `package-d-branches-r.json` still point to prior P
feature heads; they are explicitly distinct from these unpublished local heads.

C's successor R module is `package-c-r-post-review.py`; its owned root is
`/tmp/flake-update-guard-2026-10-24-provider-r-1`. Startup must succeed and retain
`startup/confctl-package`. Set D_PROVIDER_RECEIPT to that root's
`startup/receipt.json`; do not reuse P's startup receipt or root. The D driver
checks the literal R head. The D driver requires successful status, exact R,
package output, wrapper hash and packaged Nix path, then retains that same
provider through its own owned indirect root and captures its recursive closure.
It does not treat the earlier 7ba or precommit candidate receipt as final R.

Give each watcher the following setup and only its assigned stage command.
Canonical cwd is `/home/aither/workspace/ai/vpsfree.cz`. Supply GITHUB_TOKEN
privately in the environment; no tracing or environment dump.

```sh
set -euo pipefail
: "${GITHUB_TOKEN:?Provide through the private environment}"
: "${D_R_REVIEW_RECEIPT:?Set the actual completed affected-review report path}"
D_PROVIDER_RECEIPT=/tmp/flake-update-guard-2026-10-24-provider-r-1/startup/receipt.json
D_R_DRIVER=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-flake-update-downgrade-guard-replacement/package-d-post-review-r.py
D_R_ROOT=/tmp/flake-update-guard-d-r-2026-10-24-1
D_R_MANIFEST=f89bbd48fe845f288de0d94e83d5c0568481d381e6a57a53d262625a58e1eebb
```

Each line below is a separate root-assigned operation, not an unattended batch:

```sh
python3 "$D_R_DRIVER" runtime vpsfree-cz-configuration --root "$D_R_ROOT" --review-receipt "$D_R_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_R_MANIFEST"
python3 "$D_R_DRIVER" runtime vpsadminos-org-configuration --root "$D_R_ROOT" --review-receipt "$D_R_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_R_MANIFEST"
python3 "$D_R_DRIVER" project vpsfree-cz-configuration --root "$D_R_ROOT" --review-receipt "$D_R_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_R_MANIFEST"
python3 "$D_R_DRIVER" project vpsadminos-org-configuration --root "$D_R_ROOT" --review-receipt "$D_R_REVIEW_RECEIPT" --provider-receipt "$D_PROVIDER_RECEIPT" --manifest-sha256 "$D_R_MANIFEST"
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
`package-d-r-preflight.log`. No final operation was executed.
All seven final patterns are rerun; older source results remain historical.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-flake-update-downgrade-guard-replacement/)
