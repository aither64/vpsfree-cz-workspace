# OCL-R1 narrow remediation

Baseline `09299a95778807307cb9ca4c66f749de4c3a8f9b`, tree
`a564069618c7763a05fd2b85864156e4af5dfbd2`. Implementer3 retained
Sol/xhigh/workspace_write and verified this session. Product writer is released
back to implementer1; no owned operation remains.

Only three files changed inside `packages/discourse-oauth-log-protection/`:
`lib/oauth_log_protection.rb`, `patches/discourse-oauth-logging.patch`,
`tests/source_fixture.rb`. [Exact diff](final.diff), [diffstat](diffstat.txt),
[all five package hashes](final-source-hashes.json), [effects](effects.json).
The diff is 38 insertions / 25 deletions. Existing source/provider pins, plugin
wiring, shared configuration/docs and generated services update are untouched.
E3 made no Git/index/ref/hook writes.

Both rate-limit URI arguments now call `DiscourseOAuthLogProtection.safe_uri`.
It uses the same `protected_path` classification as environment protection and
logging copies, with the existing single route list and slash normalization.
Unrelated URI values are returned unchanged. No authentication method or
request input is changed.

## Regression and final checks

The enhanced existing fixture loads the exact pinned `Discourse.warn` method
instead of its earlier warning stand-in. Both actual warning branches run for
slashless and trailing-slash callback/failure paths plus a benign unrelated URI.
It checks original request/auth/cache values, unread body, unchanged limiter
result and retained route/category diagnostics.

- **Old product source reproduced the defect**, exit 1:
  [result and exact command](regression-result.json), [stdout](regression.stdout),
  [stderr](regression.stderr), [old patch](pre-fix.patch),
  [old library](pre-fix-library.rb). All four trailing-slash cases emitted public
  sentinel query values to the ordinary logger. In this isolated execution,
  Logster re-sanitized its environment and its stored output did not leak; this
  is preserved as observed, rather than claiming both sinks leaked.
- **Final affected fixture ran once and passed 82 assertions**, exit 0:
  [stdout](source-fixture.stdout), [stderr](source-fixture.stderr),
  [command/results](quick-result.json). Both warning outputs are checked through
  native pinned implementations; unrelated diagnostics remain useful.
- Changed library and fixture syntax pass. Scoped RuboCop reports two files,
  no offenses: [library syntax](syntax-library.stdout),
  [final fixture syntax](syntax-fixture-final.stdout),
  [final lint](rubocop-final.stdout). The first lint attempt found only a
  redundant fixture cop-disable comment; its failure remains in
  [initial results](initial-quick-result.json) and [lint output](rubocop.stdout).
  Removing that comment has no execution effect. Nix parsing was not repeated:
  no Nix source changed. Four patched upstream Ruby files compile inside the
  affected fixture as before.

Declared Ruby is
`/nix/store/3rcm37q1arwggzjxzcnbiz5s8a7c1ppx-ruby-3.4.9/bin/ruby`.
Evidence directory is mode 0700; raw/result files are 0600. Only fixed public
sentinels were used. Original [P3 evidence](../p3-handoff.md) remains its prior
scope, including its earlier failures.

## Limits and handoff

Real pinned Logster Message/Logger/DebugExceptions, DiscourseLogstashLogger,
Discourse.warn and patched owning source execute in the focused fixture.
Rails/Rack/provider/Redis dependencies remain isolated stand-ins. This does not
establish installed Rails boot, real OmniAuth state/CSRF/GitHub behavior or
production absence of disclosure. Those installed checks remain deferred under
the existing post-review release boundary. No network/build/installed test,
production/cluster action or change to parent3922/frozen recovery was performed.
E1 owns normal hooks and folding the narrow remedy into the P3 commit while
preserving the generated pin patch/message. No migrations.
