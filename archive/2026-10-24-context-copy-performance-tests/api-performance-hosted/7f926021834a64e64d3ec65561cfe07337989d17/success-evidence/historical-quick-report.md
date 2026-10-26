# Historical7f hosted quick evidence

Scope is exactly `7f926021834a64e64d3ec65561cfe07337989d17`, not final38 CI.
Both first-attempt artifact archives match GitHub's API SHA256, exact run/head/
branch/event/attempt bindings and30day expiry. Fullrun/jobs/logs/rawarchives,
source exports, samples/reports/inputs/locks/runtime and independent structural
inspection receipts retained in the two run-ID directories.

| Run | Baseline | Archive SHA256 | Paired step | Whole comparison job | Hard limit |
| --- | --- | --- | --- | --- | --- |
| push40186965799 | 39909094649b1d14a23f00615775ca7136acf4fd | bbe31b1c46e18a188a8ee1b8a2106bcd7d0299d2c5279a36c80ef88546011c9b | 240s | 308s | 600s |
| manualquick40187122638 | b85ec364057f536940d689b09e612512ffffaf82 | a1de17d206952d9234bd78969a20609c0edb4bfb5162f1e142015d333056b6f3 | 171s | 240s | 600s |

The paired step includes wrapper source/input/documentation preparation and
runner work; it is not pure request latency. Whole-job times include hosted
setup and artifact upload. Worker-process wall sums222.036s/157.602s are retained
as diagnostics. No production-latency claim. Actual gate logs explicitly record
`PERFORMANCE_RESULT: success` and `PERFORMANCE_OUTCOME: compared` in both runs;
no-work step skipped, selection relevanttrue, runnerexit0 and reportstatuspass.

Both complete reports/samples contain the exact12quick IDs/dimensions, each
3AA+9AB pairs, correct alternating source/workload order,2warmups and25unique
process observations (pilot+6AA+18AB). No hidden no-work or partial report.
Report raw components match samples. Every recorded body is retained, raw digest/
byte length and parsed canonical typed value/digest recomputed. Every output and
operation/counter record was inspected:48,840push and43,440manual. Exact calibrated
query/authorization/execution counters match each case's budget.

Manual strict raw parity holds throughout. Push raw differences occur only for
`docs.options,size8`:340paired records reference3raw variants of23,423bytes;
all share canonical digest
`f028aba0d88f97e7aef9cca3227eae7709b9bc1f66755c056b736753464cb2a1`.
Independent reconstruction proves all keys/types/scalars/arrays/nested key order
match; only `/response/resources` map insertion order changes. Existingversion1
map-order contract applies; original bytes/digests remain, no source or artifact
normalization. All HTML and other paired raw digests match.
[Order proof and three raw bodies](docs-options-order-proof/proof.json).

Both runs match calibration Ruby3.4.11/x86_64-linux/ABI3.4.0, executable
`/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`,84loaded
third-party gem versions/platforms, manifests and exact root/server resolved
locks. All25worker policy/environment/input/fixture graphs and loaded-source
hashes match their selected verified source graph. Source tar SHA256 and every
772/777baseline and793candidate tracked-file hash independently match receipts.
All3scenario fixture hashes equal calibration. Neutral executed runner/comparator
hashes differ from the original calibration snapshot and are explicitly recorded
in structural-inspection.json; no claim of identical calibration harness bytes.
C owns review of that accepted calibration lineage and independent statistics.
Within each run the same executed neutral harness is used for both revisions.

All12reported case classifications are pass, but D did not recompute/accept
numeric statistics. C owns that assessment. This verifies actual historical
quick orchestration/composition and retained contracts; it does not replace
final38 pushquick/manualweekly first-attempt results or waive any blocked result.

D's first evidence-inspector attempt assumed .ruby-version was duplicated under
inputs; it is retained in candidate-source.tar/fulltrackedgraph. Inspector fixed
and receipt preserved in inspection-attempt1-error.txt. No benchmark/check rerun,
source edit or additional timing operation occurred.
