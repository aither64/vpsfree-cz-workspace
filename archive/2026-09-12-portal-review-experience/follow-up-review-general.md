# Follow-up mandatory review: general lane

## Review identity

- Lane: general
- Risk: high
- Reviewer model and effort: `gpt-5.6-sol`, `xhigh`
- Review packet: `follow-up-review-packet.md`
- Reviewed commits:
  - `codex-web` `83770217d63f2c206689d2c569e1c81950544504..de83e9c72dec6cb5ff8ec13d5b0b21ed60148117`
  - `dev-workspace` `d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2..ebc0e4a71b01e81d0d90a29b0ca7385a61b1bdd1`
  - `vpsfree-dev-workspace` `a30de6c62d2bcd1ff41ee48018c595140c6d4042..534d0f2c5530bbbbf36d8254d282a9945cef9bfc`
  - `workspace` `5dbe312b1edf6a4454c4e86ec06f68baa3b5f4b4..77ca31a5e3e5e4f44c907b34b0f30bd99aec6980`

The review covered the complete commit series, repository-local `AGENTS.md`
files, plan and state, native Git parsing and limits, HTTP routes, descriptor
persistence, caching and batching, browser route/state handling, CodeMirror and
Shiki integration, focused tests, documentation, and downstream pins. No
production code was edited and no long integration test was run.

## Findings

### Blocking: independently reviewable behavior is bundled and dependency ordering leaves an intermediate live UI broken

Commit: `dev-workspace` `b924a157043b7c3535cccde514d63fad52cbffdb`,
with related ordering in `5bc5f02128ba5045596c463ba4ef54b3cc753c05`
and `a10fcb658c72213d263f0f48649c49188e2688ab`.

Files and representative final-tree lines:

- `portal/internal/session/worktrees.go:83-103` and
  `portal/internal/web/server.go:606-614`: shared discovery caching and Git
  process admission used by the index and session details.
- `portal/internal/web/repository_review_cache.go:13-147`: independent immutable
  LRU/coalescing implementation.
- `portal/internal/web/repository_comparisons.go:121-250`: independent schema-1
  durable descriptor and scope implementation.
- `portal/internal/web/repository_review_batch.go:12-136`: independent batch API
  and bounded worker implementation.
- `portal/internal/web/static/app.js:149-155`, `617`, `1382-1386`, and `1651`:
  query-aware tabs, provider-helper wiring, and waiting copy are carried by the
  accepted-steer commit.
- `portal/internal/web/static/repository-review.js:198` and `318`: the UI starts
  calling the batch history and file endpoints in `a10fcb6`, before `b924a15`
  adds those endpoints.

The discovery cache is also consumed outside repository-review snapshots, and
durable descriptors do not require either the batch endpoints or response LRU.
These changes can be reviewed, tested, reverted, and ordered independently, so
the packet's shared-lifetime rationale does not establish inseparability.
Moreover, the `a10fcb6` tree serves a Repository tab whose initial history call
uses an endpoint that does not yet exist. Its mocked component test cannot catch
that intermediate deployment regression.

Rewrite the unmerged runtime series so the final design is introduced in
focused dependency order. Separate receipt lifecycle behavior; repository tab,
URL and shared-helper wiring; discovery/process admission; immutable caching;
durable descriptor restore; and batch/preview APIs unless a concrete dependency
makes a narrower grouping indivisible. Put backend and packaged editor contracts
before the UI that requires them. This is Blocking under the general-lane rule
that independently reviewable behavior bundled without a convincing rationale
must be corrected before long integration.

### Important: the eight-editor resource bound is not enforced

Commit: `dev-workspace` `a10fcb658c72213d263f0f48649c49188e2688ab`,
reinforced by the worker assumption in
`5eeed4e3759c37050d9bab3719c1af4e9a67906c`.

Files: `portal/internal/web/static/repository-review.js:229-240` and
`portal/review-ui/highlight-client.js:1-4`.

`trimEditors` stops only once the retained count reaches eight, but it skips
every record within the viewport plus a 700-pixel margin. With many short diffs
or a tall viewport, all nearby records can be skipped and more than eight
editors/content records remain mounted. Before trimming, the inline preview and
two four-file batches can also mount nine records concurrently. The highlighter
queue explicitly sizes `MAX_PENDING` for one warmup plus two sides of eight
mounted files, so the mismatch can retain more source and DOM than promised and
reject syntax jobs as unavailable.

Evict deterministically to at most eight retained editor/content records while
protecting the selected or currently rendered record, invalidate any in-flight
render that is evicted, and trim before mounting another editor. Add an actual
browser regression with a tall viewport and many short files that asserts the
mount count and successful highlighting.

### Advisory: full-file navigation can serialize the unavailable version

Commit: `dev-workspace` `a10fcb658c72213d263f0f48649c49188e2688ab`.

File: `portal/internal/web/static/repository-review.js:243-250` and `434-452`.

File-list navigation spreads the existing route. When a reader moves from a
Before full-file view to an added file, the UI correctly falls back to the new
blob through `fullFileVersion`, but the URL still says `version=old`. The
opposite occurs when moving from After to a deletion. Cold load happens to make
the same fallback, but the durable URL no longer names the version displayed.

Normalize the route version through `fullFileVersion` whenever the selected
file changes in full-file mode. Cover added/deleted cross-navigation and the
resulting copied URL.

### Advisory: the committed-range whitespace check contradicts the packet

Commit: `dev-workspace` `5eeed4e3759c37050d9bab3719c1af4e9a67906c`.

File: `portal/review-ui/syntax.NOTICE:8101-8113`, `10111`, `11737`, and `12610`.

`git diff --check d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2..ebc0e4a71b01e81d0d90a29b0ca7385a61b1bdd1`
reports trailing whitespace in the committed notice, despite the packet saying
the source diff is clean. A worktree-only `git diff --check` on a clean checkout
does not verify committed changes. Remove non-semantic trailing whitespace
without changing license text, or document a generated-notice exception and
correct the verification record.

## Residual risks and test gaps

- The packet deliberately defers the full Nix package/VM, full-handler browser,
  and live-browser tests until review reconciliation. They remain necessary
  because the retained Chromium component test mocks the bounded API data while
  the Go tests exercise the real handler separately.
- The browser acceptance covers durable cold links, line navigation, branch
  movement and Back/Forward with fixtures. It does not yet exercise the same UI
  against a restarted real portal and canonical repository in one test.
- The broader downstream devcluster CI was still running during this review;
  automatically triggered CI is feedback rather than a substitute for the
  deferred integration checks.
- Rewriting the commit series and changing editor admission introduce a new
  reviewed history and resource-control behavior. Rerun the general lane on the
  resulting exact heads; rerun any specialist lane whose owned boundary changes.

Apart from the findings above, inspection found no additional concrete defect
in exact-object and issued-file validation, native Git message/raw/numstat
parsing, cache coalescing and cancellation, descriptor scope and rollback
isolation, copy-control behavior, or syntax-token projection.
