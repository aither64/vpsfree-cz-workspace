# API performance expansion: acceptance blocked

Superseded readiness decision: [final acceptance](api-performance-acceptance.md)
records the independently audited, user-authorized repeat pass. This historical
blocked checkpoint and its original measurements remain unchanged below.

Historical intermediate update, 2026-10-25: the user authorized exactly one additional hosted
quick run with the same38/399 pair, workloads and thresholds. D collects the new
evidence; C independently audits; acceptance remains pending assessment of both
separate outcomes. The earlier diagnostic-limit/no-new-run checkpoint below is
retained and superseded only for this single explicit repeat.

Published HaveAPI head `38ecca75edaf797d048fb36c6a50ea7e05eb50a9`, tree
`c6cf3c6809ab52b3b2fba57c117139c7bcff6a37`, remains clean and unmerged.
Target/master is `39909094649b1d14a23f00615775ca7136acf4fd`; fixed weekly
reference `b85ec364057f536940d689b09e612512ffffaf82` remains in the lineage.

Implementation, independent whole-branch review and inspected narrow fixes are
complete. Exact final local verification passed 541 server examples, 147 Rust
examples and both documentation asset checks. Hosted server Ruby 3.2/3.3/3.4
each passed 541 examples; all ordinary triggered workflows passed. Release did
not trigger. No merge, deployment or release occurred.

The required quick run [40187916872](https://github.com/vpsfreecz/haveapi/actions/runs/40187916872)
remains **blocking inconclusive**, exit 2. SQLite includes32/depth2 has 7/9
passing pairs on both clocks, below required8; regression agreement is0.
The other11 cases pass, allocations/counters/output/source proofs all validate.
Independent full [quick audit](phase2-c-hosted-quick-analysis.md) confirms the
report. Whole job276s is within600s. Faster candidate median and sub20% observed
slowdowns do not override the agreement rule.

Weekly [40187949233](https://github.com/vpsfreecz/haveapi/actions/runs/40187949233)
passes all32 cases against the fixed reference. Independent full
[weekly audit](phase2-c-hosted-weekly-analysis.md) validates41workers,
170,152output/counter records,1,312raw/typed bodies and every classification.
Whole job1278s is within1800s. This does not replace quick acceptance.
[Final hosted observation](api-performance-hosted/38ecca75edaf797d048fb36c6a50ea7e05eb50a9/final-hosted-observation.md)
links immutable metadata, logs, archives, checksums and retention proof.

A bounded local diagnostic completed once, exit0/28.135934s: six processes,
18batches,288requests. All response/counter/runtime/source/input checks pass.
Same-source batch CPU variation is not explained by measured GC time; observed
waiting/faults do not support a dominant pure-wait mechanism. No concrete
application/environment remedy or original-host cause is established.
[Diagnostic analysis](sqlite-timing-diagnostic-v2-analysis.md) and structured
receipt SHA256 `43c47b98ec16f742c90d1a47e737d70911a951e26c886a43ac1d049258237ae7`
retain the evidence. Architect independently recomputed raw totals/telemetry and
agrees with stopping at this evidence limit.

The diagnostic used a different host, isolated case history, explicit exact
io-console activation and outside-timer telemetry. It cannot transfer causes or
timing to the hosted run. Earlier strict graph refusal and zero-request graph
preflight are preserved. The preflight exposed unexpected Nix build attempts;
v2 used existing executables directly and invoked no Nix command. Watcher
preexecution refusals are retained separately from the one actual v2 execution.
All children were reaped and both evidenced process groups independently drained.
No operation or utility slot remains owned. No full local paired campaign ran.

No unchanged required-campaign rerun, waiver, threshold/reference/budget change,
optimization or further measurement is authorized. Further progress requires a
separately scoped targeted host investigation or an explicit acceptance-policy
decision. The branch is not ready for integration. Session, worktree and branches
remain open; no lifecycle action or cleanup is scheduled.

Live fork PR/default-push/Sunday events remain unexercised. Resolver tests cover
selection semantics. Synthetic Rack/SQLite measurements establish no production,
vpsAdmin or network latency result. Hidden input-copy omission and exact archive
reconstruction are explicit in both hosted audits.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/
