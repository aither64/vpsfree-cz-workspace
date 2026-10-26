Comparison implementation: `bdb034436e0dffbc39537a481442c3a2880cea9c`.
Source is clean and frozen for review. Complete retained replay has not run.

`performance-replay-stages.rb` is a session-only diagnostic preload for the
unchanged supported `make performance-compare` command. The controlled smoke
passed: `validation-stage-smoke-accepted.log` and
`validation-stage-smoke-stages.json`. No sample/report schema or validation
semantics are changed by instrumentation.

After independent review, use the existing prepared top-level Nix shell and
gem paths. Clear inherited Bundler/RUBYOPT/RUBYLIB state as in the normal runner
preparation, then set these session-only variables from `haveapi-master`:

```sh
session=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-haveapi-backport-release
export HAVEAPI_STAGE_SOURCE_ROOT="$PWD"
export HAVEAPI_STAGE_INPUT="$session/batching-hosted-be520ed8ea8a82b4d1cb719a4066460f110bcf83/40221259354-artifacts/performance-40221259354-1/results/samples.json"
export HAVEAPI_STAGE_OUTPUT="$session/postreview-bdb03443-retained-replay"
export HAVEAPI_STAGE_RECEIPT="$session/postreview-bdb03443-retained-replay-stages.json"
RUBYOPT="-r$session/performance-replay-stages.rb" make performance-compare \
  PERFORMANCE_ARGS="--input $HAVEAPI_STAGE_INPUT --budgets servers/ruby/benchmarks/performance_budgets.json --output $HAVEAPI_STAGE_OUTPUT"
```

The output and receipt paths above are prepared names, not executed artifacts;
use a new directory. The preload activates the existing shared JSON bootstrap.
It records input read/parse, comparison, report serialization/write, Ruby peak
RSS, exit status, original input bytes/hash and original source identities.
Its `total_elapsed_seconds` starts after loading the shared helper at preload
initialization; the fresh watcher/execution wrapper must also retain complete
command wall time and exact exit. Record the implementation head separately
from the original samples' `b85`/`be520` source IDs; never relabel those originals.

The original weekly run remains cancelled/failed with no final report. Bounded
subset acceptance is not a weekly performance pass. Full replay must precede
the next hosted campaign, and meaningful final-head quick/weekly receipts remain
required. Existing native JSON checks, locks and complete unchanged external
graphs are in `json-preparation-locks.json`; no resolution/install is needed.
