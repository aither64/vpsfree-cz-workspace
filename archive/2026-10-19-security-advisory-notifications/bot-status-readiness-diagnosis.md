# Existing status example readiness diagnosis

Exact failed source263ddbc0b541b5df2d025a73f1759d33db3f30b2. Lead-owned local run
exited1 after622.04s. First public-status example timed out30.02s; all other seven
examples succeeded, including corrected hourly summary, overlap/count, routing and
minimum interval assertions. Preserve this evidence independently of any retry.
Full failed tree/config/VM logs archived as
[bot-local-failed-263ddbc.tar.gz](bot-local-failed-263ddbc.tar.gz).
Original runtime-final-watcher-report.md, bot-runtime-final.log/.exit retained.

## Concrete failure condition

The failed example's last IRC lines contain `No outage reported`, followed by
`Status unknown, unable to reach vpsAdmin API`. The latter is emitted by unchanged
Cluster#cmd_status only when that plugin's own api_setup? is false. Each Api
consumer owns its own client/setup and15s retry. Setup waits for OutageReports
readiness after a4s sleep; that does not establish independent Cluster readiness.
The first !status was issued before Cluster setup completed and never reissued,
so its later readiness could not produce the expected result for the consumed
command. This is a concrete fixture readiness race, not digest code evidence.
Neither Cluster nor shared Api source differs from feature base.

The initial setup exception/network detail cannot be determined from retained
logs: the old firstexample captured IRC timeout context but no service journal.
Do not claim a specific network failure or accept a later green run as its cause.
No new app behavior is needed to handle the asynchronous readiness response.

## Pinned runner scope

Pinned TestRunner::Cli::App offers testScript path/metadata filters only;
ExampleConfiguration only default_order, ExampleGroup evaluates each non-skipped
example. There is no supported per-example selector. `--filter` cannot select
this first example. Do not invent an exact targeted command or monkeypatch the
runner. Lead asked to stop investigation of unsupported debug/selector paths.

## Proposed narrow fix

[bot-status-readiness.diff](bot-status-readiness.diff) changes only existing first
example: total120s deadline, normal IRC !status, wait up to15s/remaining for either
the exact existing not-ready response or original concrete node-count response.
Only explicit not-ready responses trigger a2s pause and another command. Silence,
unmatched output or API/IRC errors still fail with the existing helper's timeout;
they are not swallowed or generalized into retries. Deadline expiry raises the
named Cluster setup timeout. Outage/digest examples and app/API code unchanged.
No source/runtime/queue bypass, no new public boundary or retry framework.

Lead accepted the diagnosis/scope and will directly inspect proposed diff before
amendment/publication. Exact source verification/provenance for seven successful
examples remains in the preserved original run. No new long check has been run.

Current exact-head CI observation: Integration39323728183 queued;
RSpec39323728164 completed/success. No CI rerun/dispatch or uncertain wait.


Lead directly inspected/accepted exact readiness diff and released consolidation.
Selected quick batch PASS: full150/0, RuboCop63 clean, Nix parse/format,
extracted Ruby syntax, diff--check. Mandatory amendment hooks passed. Published
final94ac4eb5a7caf0456fff7df86a44cae198463276 as sole feature commit above
unchanged basee9c60b0, using explicit force-with-lease protecting263ddbc. Source
worktree clean. No application/prose/migration/dependency changes.
Old queued263ddbc Integration39323728183 status preserved before cancellation;
new exact-final verification remains assigned through lead.

Superseded263ddbc Integration39323728183 confirmed completed/cancelled after new
publication (ci-263ddbc-after-cancel.json); completed old RSpec remains success.
New exact94ac4eb Integration39325998761 queued, RSpec39325998769 in_progress
at handoff, left active for lead monitoring. No manual dispatch or local long run.
