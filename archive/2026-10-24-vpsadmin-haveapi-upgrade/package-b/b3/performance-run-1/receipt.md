# B3 consumer performance and isolation acceptance

Passed one assigned post-review run on 2026-10-26. No retry. Command and
acceptance exits are both 0. Source head is
`70a2ed54b98d0c2f359a9cc4484452a257a9807b`; all four actual loaded HaveAPI gems are
released 0.30.2 and canonical Context/Rust adapter hashes, absolute paths,
effective/packaged locks, Ruby and complete Nix inputs match the B3 pre-review
receipt. `installed-identity.json` retains that proof and eight ownership checks.

Fresh retained-policy Luna/low watcher owned the sole assigned session utility
slot, exact prepared command and fresh evidence directory. The existing committed
ordered full-page regression completed: **1 example, 0 failures, 0 pending**,
seed 23906, 44.39s example time and 13.94s load, about 60s total command elapsed.
API 7.0 mounted with all six plugins (monitoring, newslog, outage_reports,
payments, requests, webui), 151 ordinary resources, 519 actions and 17 samples.
The private structural API/model was not used as request authorization.

| Role/locale | Prior instrumented wall | Current instrumented wall/CPU | Warm uninstrumented wall/CPU |
| --- | ---: | ---: | ---: |
| administrator/en | 102.376s | 5.280s / 5.245s | 4.936s / 4.923s |
| member/cs | 49.716s | 3.491s / 3.480s | 2.533s / 2.522s |
| anonymous/en | 139.036s | 4.759s / 4.755s | 4.231s / 4.224s |

All warm requests meet the proposed <=5s target. The first instrumented admin
request is above 5s and is reported as measured; the target is for the separate
warm uninstrumented requests, not every instrumented request. Instrumented wall
reductions versus the same-shape baseline are 19.4x, 14.2x and 29.2x. Context
counts remain 639/484/639 but their measured time fell to 1.236/0.396/1.609s;
renderer counts remain 294/224/294 with 0.279/0.166/0.281s. Context/renderer
counters overlap, so these times are not summed. Timings precede CGI/matchers.

All six responses are HTTP 200. Admin/member/anonymous ordering and exact locale
headers en/cs/en are recorded and observed translated resource text is checked.
The unchanged regression confirms admin action/sample and restricted node-field
filtering for the member after an admin request, preserved init/auth/action
programs and no private-model/path leakage. Each warm full raw body is byte-equal
to its corresponding instrumented role body, after all observer wrappers were
removed. There is no response cache, role-result reuse or hidden output
normalization in the application or harness.

Strict output comparison passed at every stable role/client/kind/resource/action/
auth/sample-occurrence identity: **174 panels = 168 complete programs + six
explicit Go limitations**, unchanged. All 17 action samples remain present.
The only allowed byte changes are the exact approved first-line Rust
Git-to-registry comments, in 116 Rust programs. Go programs and every limitation
reason are unchanged; no source or body differences were silently discarded.
New rows retain sample SHA256; the original baseline lacked sample hashes, so
historical sample identity relies on unique panel coordinates and occurrence
order, not an invented digest. The mapping of old unlabelled timing rows to
roles comes from original committed spec order, not elapsed time.

Host observations before/after every request report 64 logical CPUs, load average
about 6.5–6.9 and reported CPU pressure averages 0.00. Wall and process CPU are
close for these requests. This is observed capacity/contention evidence, not a
claim that the shared host was globally idle. No foreign process was controlled.
A/C session batches stayed stopped during the assigned operation.

All original baseline hashes remain unchanged. `comparison.json` has pass=true,
no failures and 116 explicitly allowed comment changes. Exact raw pages,
programs, timings, host observations, RSpec JSON/log and command exit receipts
remain in this directory. `operation-reconciliation.json` records no remaining
owned Ruby/database process; watcher reported its operation complete. Worktree
and index remain clean, no repository source/Git/provider mutation occurred,
and the utility slot was returned to lead promptly.

This result supplies the requested consumer timing/output/isolation proof;
**R1 closure is the lead/reviewer's decision**, not set by this package. Required
packaged services-up, full/core suites, external SDK compilation and other
integration gates remain separate. No SDK compiler, VM, deployment, publication,
merge or lifecycle operation was executed by this run.
