# vpsAdmin feature published for review/testing

2026-10-26. Lead accepted the architect's dependency-advance disposition and
explicitly released publication of the unchanged reviewed head, without rebase.
The earlier stopped-publication receipt and all evidence remain unchanged.

Published branch:
https://github.com/vpsfreecz/vpsadmin/tree/2026-10-24-vpsadmin-haveapi-upgrade

Exact published head: `70a2ed54b98d0c2f359a9cc4484452a257a9807b`.
Original reviewed base: `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5`.
Freshly assessed remote master: `898e2881e8230d24fb06baee1c58737ae55e0009`.

The single normal SSH push used root `nix develop`, plain Git and exact refspec
`70a2ed54b98d0c2f359a9cc4484452a257a9807b:refs/heads/2026-10-24-vpsadmin-haveapi-upgrade`.
It exited 0 and created the absent feature branch. No force flag, hook bypass,
outer bundle exec, PR, claim or manual workflow dispatch was used. Declared
executable hook identities matched preflight; no hook intervention was needed.
`push.log` and `push.exit` retain its result. An independent SSH ls-remote then
proved the exact feature head and unchanged master/default identity.

Before and after publication, local head/index/worktree and API effective
ignored lock, packaged lock and flake hashes equal the earlier reviewed inputs.
Normal root Nix shell entry prepared its root hook bundle; it did not change the
active API runtime lock. All owned Git/network command handles finished, without
uncertain mutation or retry. Git publication ownership returned to lead; the
parent retains CI observation only.

This branch is **published for review/testing; integration refresh pending**.
Its reviewed two-commit series and no-migration conclusion remain unchanged.
The assessed master adds separate Faraday/Guzzle runtime dependency changes in
four generated files. Those changes are deferred to separately authorized
integration preparation and affected verification. Publication does not claim
fast-forward compatibility, merge readiness or integration approval. No default,
OS ref, source, deployment, cluster or lifecycle action was performed.

Nine automatic exact-head Actions runs were observed initially queued/in
progress, with 35 check runs. `actions-initial.json`, `checks-initial.json` and
`status-initial.json` retain IDs/statuses. There was no manual dispatch; pending
is not a pass. The lead authorized visible parent monitoring while A occupies
the sole watcher slot; no additional watcher was started. Final CI status and
any failure evidence will be appended after bounded exact-run observation.

## API CI outcome

Eight of nine automatic workflows have succeeded. API run 40336542902,
attempt 1, completed successfully with all 26 topic jobs plus the topic-coverage
aggregate. All 26 native result/environment artifacts are retained under
ci-api-results. Each mode reports 4,725 examples and zero failures or
outside-example errors; full has eight pending examples, core has 404.
api-native-summary.json records per-mode topics, totals and environment identity.

CI used Ruby 3.4.12, Bundler 2.6.9 and RSpec 3.13.6. All 13 full topics share
effective lock SHA256
`b84937ac47bad0e42a176ec8538b2e320c6ad378e294cf71461ef06a4044dbe5`;
all 13 core topics share
`82ef7568786da20099a700f9c2bcdc6bac14cfd4d57cfa4258f228154335fe58`.
Representative full/core resolved-lock logs explicitly show all four HaveAPI
gems at 0.30.2 and Faraday 2.15.1. These are CI's own effective resolutions,
separate from both the local runtime lock and committed packaged lock; no local
test result is relabelled and no packaged-closure equivalence is claimed.

The other seven successful workflows are Webui PHPUnit, API Migration Specs,
Download Mounter Specs, Console Router Specs, RuboCop, Client Specs and i18n
health. Only integration CI run 40336542935 remains active. Pending integration
is not a pass. ci-progress.jsonl retains bounded observations; no workflow was
manually dispatched or rerun.

## Final milestone CI handoff

Lead ended the old integration observation contract at this milestone. The
final bounded read confirms vpsAdmin integration run 40336542935, attempt 1,
exact old published head `70a2ed54b98d0c2f359a9cc4484452a257a9807b`, is still
in progress. Its sole selected-test job remains active with no failure or
conclusion reported. Native limits are 720 minutes for tests and 780 minutes
for the workflow; elapsed time is not treated as a failure and no wait for
those limits remains assigned.

The separately requested F source-fix Check run 40379808743, attempt 1, exact
`ab9346b0c4b942fccd0da6af760401fad3a55bd1`, completed successfully; its sole
flake job is successful. Raw final responses and query exit receipts are
final-handoff-old70a.json and final-handoff-f-ab934.json; final-ci-handoff.json
records the stopped observation and absence of local operations.

Both queries completed without errors. No failure diagnostics were needed;
no retry, dispatch, cancellation or source/ref/lock change occurred. No local
polling, query, wait or background operation remains. New successor CI discovery
belongs to implementer0 and was not queried here. This packet's publication
and original-input results do not claim overall CI success or current successor
merge readiness. Any later integration refresh/verification stays with its
separately assigned owner and receipts.
