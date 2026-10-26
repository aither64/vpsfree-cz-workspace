# Master push performance diagnosis

Both failed original runs returned **2, inconclusive timing**, with no regression,
input, response, lineage or allocation error. No source defect identified from
the retained evidence. No source/index/ref edits or test/build runs were made.

| Run | Exact comparison | Result |
| --- | --- | --- |
| Master push `40214200383`, attempt 1 | `38ecca75edaf797d048fb36c6a50ea7e05eb50a9` → `1741a25e1df45f06f9966942d5c34a97967ebb3e` | 11 pass; `docs.html_resources(size=8)` inconclusive |
| Feature `40213477525`, attempt 1 | Same exact comparison | All 12 pass |
| Prior master `40204639542`, attempt 1 | `39909094649b1d14a23f00615775ca7136acf4fd` → `38ecca75edaf797d048fb36c6a50ea7e05eb50a9` | 11 pass; `docs.options(size=8)` inconclusive |

Current failed/master and passing/feature runs have identical harness, fixtures,
budget, input/environment identities and loaded-source digests. Baseline
selection is not the cause. Recorded hosted CPU models differ (EPYC 9V45 vs
EPYC 7763), so these are separate measurement environments.

The current failure's third baseline/self wall pair is **77.913044 vs
116.864923 ms/request**, selecting 38.951879 ms as the maximum observed noise.
CPU time reports the same difference. Actual baseline/candidate medians are
81.894015 vs 82.460104 ms, equal allocations162119, and safe-side margins range
7.94–21.32 ms. None clears the observed noise: pass0/9, regression0/9. Prior
master OPTIONS likewise has a noisy baseline/self pair1.134318 vs1.350695 ms,
with near-identical actual medians1.088675 vs1.087575 ms and pass4/9. Passing
feature HTML noise was5.642673 ms and pass9/9.

The classifier correctly returns inconclusive under its documented fail-closed
rule. Retained evidence establishes unstable baseline/self measurement, but does
not establish its physical cause (for example CPU behavior or GC). It does not
prove a performance regression. Budgets/reference/classification are unchanged.

Original status/logs/artifacts are preserved under `ci-RUN-status.json`,
`ci-RUN.log` and `ci-RUN-artifacts/performance-RUN-1/`. Artifact downloads briefly
used a relative path under the master worktree; all owned downloaded directories
were moved to session evidence and the empty temporary parents removed. Master
checkout is clean; no application/index/ref content changed.

Lead authorized one diagnosed rerun of **only40214200383**. Preserve original
attempt1 and record the fresh attempt separately. Any repeated inconclusive or
regression blocks acceptance and returns to diagnosis; no automatic retry or
budget relaxation.

User then replaced fine hosted timing with a coarse regression requirement.
Only owned attempt2 was cancelled through the native workflow command while
active. Final attempt2 conclusion **cancelled**, observed and retained with its
jobs/log/available artifact under `master-performance-rerun-attempt-2/`.
Watcher finished; no handles remain. Original attempt1 is still inconclusive,
not erased or accepted. No second retry or source change occurred here.
