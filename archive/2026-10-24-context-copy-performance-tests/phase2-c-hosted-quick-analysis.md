# Final hosted quick: blocking inconclusive

Run [40187916872](https://github.com/vpsfreecz/haveapi/actions/runs/40187916872),
attempt1, exact candidate `38ecca75edaf797d048fb36c6a50ea7e05eb50a9` versus
whole-feature base `39909094649b1d14a23f00615775ca7136acf4fd`. Independent raw
recomputation agrees with runner exit2: **11 cases pass; SQLite includes32/depth2
is inconclusive on both wall and CPU,7/9 passing pairs,0/9 regression pairs.**
Required agreement remains8/9. This is blocking and no pass/replay/rerun replaces it.

Verified artifact12597346593 SHA256
`c1caa0319afec7d7591e854c1f0ab60ee5fa530a63d2a951bd7a29a7ee9316d7`.
[Structured analysis](phase2-c-hosted-quick-40187916872-analysis.json) binds all
case arithmetic/source/input evidence and [SQLite stages](phase2-c-hosted-quick-sqlite-diagnosis.json).
[Read-only audit script](phase2-c-audit-hosted.py) makes no requests and invokes
no Comparator replay; its Ruby helper only verifies canonical byte digests.
Original artifacts and reports remain unchanged. Local campaign attempts are0.

## Why two pairs are unresolved

Pilot9.990850ms selects16 operations/batch; both revisions retain that count,
two warmups,3AA/9AB and alternating AB/BA plus workload order. Wall AA differences
in magnitude are0.853391/0.164296/0.728095ms, so noiseN=0.853391ms, exceeding
5% of the9.033552ms baseline median(0.451678ms). CPU N=0.854488ms.
For passing agreement the excessE=C-B-max(20%B,0.20ms) must be strictly below-N.

Pair indices below are zero-based; times are per operation in milliseconds.

| Pair | Order | B | C | Change | T | E | Passing-margin shortfall |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | C/B, reverse | 9.033552 | 10.149243 | 12.351% | 1.806710 | -0.691020 | 0.162371 |
| 8 | B/C, forward | 8.329052 | 9.746075 | 17.013% | 1.665810 | -0.248787 | 0.604604 |

CPU passing shortfalls are0.164923/0.605630ms respectively. Both observed
slowdowns remain below20%; all9 excess values are below+N, so no pair supports a
regression classification. The candidate wall median8.964497ms is about0.76%
faster than baseline, but a median cannot override the agreement gate. Pair5
lies within the observed self-noise allowance; pair8 remains unresolved even
against the5% baseline floor. Removing the maximum AA observation, discarding
pairs or changing the noise allowance would change the accepted policy.

Both troublesome orders occur, so there is no single ordering defect. All24
AA/AB measurements allocate exactly11265.0625 objects/request and retain every
3-query/65-authorization/1-execution record. Maximum absolute wall/CPU difference
is4.601microseconds/request; simple I/O waiting or descheduling alone is not
supported. The candidate pair5 second warmup is9.981593ms/request versus baseline
9.219652ms, while pair8 second warmup is8.904969 versus8.393330ms; stages do not
identify one cause. Reverse SQLite build is roughly96-105ms versus11-16ms
forward, outside timing and symmetric across sources. It does not explain the
measured discrepancy. GC count/time, CPU frequency and scheduling telemetry were
not recorded, so CPU throughput variation and measured GC/CPU work cannot be
separated retrospectively.

## Complete validation and limits

All12 case/dimension keys and all25 workers including pilot match. Actual worker
arrays confirm forward/reverse order; pair roles, same selected counts and two
warmups match. The audit checks25,956 outputs and per-operation counters,
300 stored raw/typed-canonical bodies, raw bytes/SHA, canonical digests, duplicate
key rejection, scalar types, array order, HTTP/envelope identity and strict
cross-operation/revision parity. Wall/CPU noise,excess,agreements,classifications,
allocation medians,growth and fixed ceilings independently reproduce every report
field. Every allocation gate passes, including SQLite11265.0625 below14102.

Both full source tars and tracked tree/blob/SHA256 graphs match Git:772 baseline
files and793 candidate files. Representative and complete loaded-source hashes,
neutral harness/fixtures,budget57b8d472...,matched dependency declarations,
resolved root/server locks,84 loaded third-party gems,Ruby3.4.11/ABI3.4.0,
executable,Nix graph and fixed test/locale/timezone/JIT policy validate. Reference
calibrationSHA d31d9261... matches every reference allocation/counter budget.
The only production base-to-head edits are documentation Context and Rust
normalization; no ActiveRecord/SQLite runtime edit exists. Prior documentation
work can affect process heap state, but these observations establish no causal
SQLite correction or source regression.

One separate retained copy,inputs/.ruby-version,is omitted by the artifact
uploader's default hidden-file filter. Its exact bytes are present independently
in BOTH Git-verified source archives and match input-sha256.json at
33bdaf9e2d6bcbde2e4e613e865e403f8fe21fc621078d34c30b0bdc7f68d903.
The receipt explicitly records this omission and exact reconstruction; it is
not a silent dependency/input substitution. All lock copies are retained.

Performance job121152535735 completed in276s including setup and upload, within
600s; paired wrapper step198s, upload4s. All workers and evidence completed;
performance and aggregate correctly fail on exit2. No timeout, new benchmark,
policy adjustment, source/Git/install mutation or local campaign occurred.

No specific environment/harness remediation is established by these data, and
there is no justified blind rerun. Keep exit2 blocking. Architect's separate
six-worker telemetry probe is design-only pending lead authorization; a new-host
diagnostic cannot identify the original host's cause or substitute for quick.
Weekly final-head artifact analysis remains separate and pending D collection.
