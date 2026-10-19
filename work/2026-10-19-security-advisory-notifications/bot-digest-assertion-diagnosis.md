# Digest assertion failure diagnosis

Failed revision `a5d1dfe565526c3532183d756c592a26e7270675`.
Lead's local retry failed exit1 after566.22s, example8 after70.86s. Examples1–7
passed. Entire failure tree preserved distinctly in
[bot-local-failed-a5d1dfe.tar.gz](bot-local-failed-a5d1dfe.tar.gz), including config.
Existing runtime-watcher-report.md and bot-runtime-retry.log/.exit retained.

Registration and bootstrap now succeeded. Local irc-shell.log shows successful
service start/readiness and bootstrap snapshot file. services-shell.log shows
both new advisories and both updates. The exact expected digest wait and >=60s
assertion passed; the sole failure is final `expected:1 got:5` count assertion.

The fixture counted every digbot PRIVMSG as a summary. UrlMarker is always
loaded, and the original individual bot emits four standalone advisory links
(two new/two updated). Each causes an unrelated digbot URL-marker reply. A short
mocked-HTTP handler probe exercises the real UrlMarker#channel for four advisory
links, then adds the expected summary and applies the old/new classifiers:

```text
Actual UrlMarker handler on four advisory links: 4 unrelated replies
Old all-bot-message count: 5; corrected digest count: 1
```

This probe confirms the classification cause without a VM rerun. It does not
claim to recover the lost full IRC transcript; fixture error previously rescued
StandardError only, while RSpec assertion errors inherit Exception directly.
The proposed diagnostic clause now explicitly catches
`RSpec::Expectations::ExpectationNotMetError` as the pinned test framework does.

Only `tests/suite/vpsadmin-events.nix` changes: collect all bot lines, select
summary lines by the existing ` in vpsAdmin: ` message category, retain exact
payload/count/interval assertions, and check absence of individual advisory
headings across ALL bot lines. Preserve last30 IRC transcript lines and existing
last120 service journal lines for both standard and assertion failures.
No application, timing, server limit, plugin, public contract or prose change.

Lead directly inspected accepted narrow diff
[bot-digest-assertion.diff](bot-digest-assertion.diff) (+6/-4), released amendment
and publication, and requires no affected-lane/full review rerun for this fixture
repair. Quick verification all PASS:150 examples, RuboCop63 files, Nix parse and
format, extracted Ruby syntax and git diff--check. Short real-handler probe PASS.
No long rerun or hook setup by implementer0.

Before corrected publication, CI on a5d1dfe observed:
Integration Tests39321329088 queued; RSpec39321328974 completed/success.
Only the superseded queued integration may be cancelled after new publication;
completed failure/success evidence remains intact. New exact-head verification
will be owned by lead's fresh watcher.


Corrected head263ddbc0b541b5df2d025a73f1759d33db3f30b2 published as the sole
feature commit above unchanged e9c60b0. All mandatory hooks passed; source worktree
clean. Exact lease protected olda5d1dfe. Its queued integration status was saved in
ci-a5d1dfe-before-cancel.json before cancellation after corrected publication.
New exact-head CI and runtime retry remain lead-owned.

Olda5 integration39321329088 cancellation confirmed completed/cancelled in
ci-a5d1dfe-after-cancel.json; no current-head run cancelled. New exact263ddbc
Integration Tests39323728183 queued; RSpec39323728164 in_progress at handoff.
