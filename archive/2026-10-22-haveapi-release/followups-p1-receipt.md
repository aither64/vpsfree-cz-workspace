# P1 registry confirmation and shared Rust packaging receipt

Implementer2, 2026-10-22. Execution follows
[the frozen design and accepted clarifications](release-followups-design.md),
the lead's P1 grant, and the explicit two-file R1 acceptance extension.
Session current, both environment bindings, live workspace-write access and the
exact registered follow-up worktree/branch were verified before edits.

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/haveapi-followups`.
Branch: `2026-10-22-haveapi-release-followups`.
Base and pre-commit head: `b64fb25bea8d8222fb3263b99956c0b61438a859`.
The completed 0.30.0 source/tag/run/artifacts and original dist were not edited.

## Exact eight authored application paths

1. `utils/release/registry_query.rb` (new): read-only registry transport and
   bounded observation. Accepts only constructed HTTPS exact-version endpoints
   on the three official hosts, rejects credentials/redirects/unsupported paths,
   uses no-cache requests and at most one cache-distinct GET after each missing
   or valid incomplete canonical observation. Returns parsed metadata, status
   and bounded allowlisted diagnostic headers. Clock, wall clock, sleeper,
   transport and diagnostic sink are injectable for deterministic tests.
2. `utils/release/publish.rb`: preserves artifact verification, all-destination
   preflight, registry order, one ordinary upload per missing destination, PyPA
   credential/upload ownership, PHP guards and final draft completion. Adds
   strict gem name/version/ruby-platform/hash validation. Python preflight
   retains an invocation-local union only for choosing missing original files;
   confirmation requires one complete validated response. Any response conflict
   remains fatal. Reports visibility regression without bodies and retains
   tag/run URL/original manifest location on unconfirmed errors.
3. `utils/release/spec/registry_query_spec.rb` (new): fake-clock/transport
   deadline, cache, status, transport, header, URL and HTTPS-constructor controls.
   Real registry transport is forbidden in these tests.
4. `utils/release/spec/publish_spec.rb`: fake registry/file fixtures cover
   strict validation, all four gems/order, matching skips, original-only partial
   staging, accepted-but-unconfirmed uploads, shared final deadline, Python
   union regression/reset/conflicts and individual-response confirmation.
5. `utils/release/spec/release_spec.rb`: update the existing registry tests for
   strict metadata and bounded observation; add retained fiddle dependency and
   isolated-smoke invocation assertions. Existing package and PHP test coverage
   remains active.
6. `utils/release/artifacts.rb` (lead-approved R1 extension): require exactly one
   retained Rust runtime fiddle dependency matching the owning source gemspec.
   Existing package file, source-byte and artifact checks are preserved.
7. `utils/release/rust_smoke.rb` (lead-approved R1 extension): pass the retained
   dependency requirement into the existing isolated child, explicitly activate
   it before loading the extracted generator, and require a compatible
   nondefault fiddle gem. No new installation, network, artifact file or source
   fallback was introduced. R1's final declared requirement is `~> 1.1` and
   `>= 1.1.8`, locked to 1.1.8 by implementer3.
8. `doc/agent-instructions/releases.md`: lasting confirmation/recovery behavior,
   Python staging/confirmation distinction and retained fiddle activation.
   Lead directly completed the main prose pass and reviewed visible CLI wording;
   final lead edits are preserved.

`Publisher.new(artifacts, directory)` remains compatible; optional `registry:`
injects the observer for tests. No product API/protocol/schema/version, workflow,
registry order, upload retry loop, mutable journal or credential path was added.

### Registry and shared R1 hunk boundary

Registry-only behavior is in `registry_query.rb`, `publish.rb`, their dedicated
`registry_query_spec.rb`/`publish_spec.rb`, the `existing registry versions`
section of `release_spec.rb`, and the confirmation/recovery paragraphs of
`releases.md`.

The shared R1 acceptance hunks are `artifacts.rb#inspect_rust`'s runtime fiddle
requirement check; `rust_smoke.rb`'s retained requirement argument, activation
and nondefault assertion; `release_spec.rb`'s `Rust generator gem contract`
fixture/dependency/smoke-argument assertions; and the Rust packaging paragraph
in `releases.md`. They add no registry behavior. R1's gemspec/component lock and
generated naming changes remain implementer3-owned and are outside these eight
authored paths. Git owner implementer0 owns any purpose split/index operation.

## Accepted narrow clarifications

- Publisher owns the Python known-file policy. A later 404/partial/transient view
  cannot make a strictly validated file eligible for reupload within preflight.
  A complete union skips upload but does not establish post-upload/final success;
  a withdrawn file expires unconfirmed. State resets on the next invocation.
- Preserve normal `Net::HTTP.new(host, port)` environment-proxy compatibility.
  No actual proxy environment values were read/logged by the implementation or
  tests; publishing credentials are not copied into metadata GETs. Normal proxy
  authentication remains Net::HTTP-owned.
- Retry delay is the maximum of normal positive backoff and a valid Retry-After.
  Zero/past dates cannot cause a busy loop; valid longer delays are honored only
  when the absolute deadline permits. No request/sleep begins after expiry.

Both design owners routed these points through lead acceptance before final
implementation. No unresolved design deviation remains.

## Final quick verification

Implementer0 prepared only the follow-up worktree's `.gems`. The initial
`.gems`-only GEM_PATH omitted selected Ruby's standard rexml/racc gems, so Bundler
stopped before tests. Implementer0 supplied the corrected invocation below.
No install, hook-closure mutation or original/shared writable gem-home use was
performed by implementer2. Nix shell setup may realize its selected tools; no
unexpected kernel build occurred.

Final command, after all logic and accepted clarifications:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c 'set -e
export GEM_HOME="$PWD/.gems" GEM_PATH="$PWD/.gems:$(ruby -e "puts Gem.default_dir")" BUNDLE_GEMFILE="$PWD/Gemfile"
make release-check
make release-test
bundle exec rubocop utils/release/registry_query.rb utils/release/publish.rb utils/release/artifacts.rb utils/release/rust_smoke.rb utils/release/spec/registry_query_spec.rb utils/release/spec/publish_spec.rb utils/release/spec/release_spec.rb
for path in utils/release/registry_query.rb utils/release/publish.rb utils/release/artifacts.rb utils/release/rust_smoke.rb utils/release/spec/registry_query_spec.rb utils/release/spec/publish_spec.rb utils/release/spec/release_spec.rb; do ruby -c "$path"; done'
```

Results: release metadata valid 0.30.0; **170 Ruby examples, 0 failures** in
10.4 seconds; **6 Python tests passed**; **7 Ruby files inspected, no offenses**;
**7 Syntax OK** results. Final tracked and both new-file whitespace checks were
clean. Earlier focused iterations exposed/fixed test-fixture/style issues;
the final complete suite includes all those corrections and the new proxy/
Retry-After/union regressions.

Coverage includes canonical 404/fresh positive, repeated absence/expiry, partial
Python completion, exact identity/platform/digest/malformed metadata, duplicate/
unexpected filenames, all four gems and no npm before Rust confirmation,
no second accepted upload, transient/permanent/TLS/DNS/redirect outcomes,
Retry-After seconds/date/zero/past/malformed/large delays, absolute request and
shared final deadlines, original-only staging and invocation reset. HTTPS
transport tests use a mocked constructor/request and assert total timeout,
normal proxy mode, no cookies/upload Authorization and safe diagnostics.

Existing release unit tests build small disposable package fixtures and exercise
temporary local Git mirrors; they do not publish, access registries or mutate
session refs. No full release build, installed generator smoke, Cargo compile,
listener, real proxy/registry probe, new tag or workflow dispatch was run.

## Exact source yield

All owner2 commands have exited. The exact eight paths above are yielded to
sole Git/index/hooks owner implementer0. Implementer2 explicitly authorizes their
normal hooked staging/commit in this follow-up feature branch, with lead-owned
prose preserved. No Git/index/hook mutation was performed by implementer2 and
no further source edit is planned without a follow-up assignment.

SHA-256 at yield:

```text
0e355749cd3697d061c07295918a45dc98ab0f3304e29a8e3f514cb9bdf7121b  doc/agent-instructions/releases.md
4210742452bbfad2f94717e0277adf6442464ac070a876b46be2e976e04c1df1  utils/release/artifacts.rb
2028d920bacd622faa444fdb7c471e5f4fca606ab4c791253a18475043f960b4  utils/release/publish.rb
7633f1ce0fd38674d0699a0da2df5d5424b6d6972b810062562eac446989131f  utils/release/registry_query.rb
999611fa2e8c3bd5d0702690278e724c19ee4d4ae17b6a930873d220ec7438d5  utils/release/rust_smoke.rb
2afd8ad4cbdf5c52b874dd13eecd63255cef7315427603c9c5c18d5859d9921d  utils/release/spec/publish_spec.rb
4a896e66ed46abac3b9b83987c0e4e6288de7715f68844471b01445393f1bfd9  utils/release/spec/registry_query_spec.rb
fea1d68eba6d6f38514831e176da7690b7f45819f9fc55f7deada48f3bc3ddca  utils/release/spec/release_spec.rb
```

Remaining gates: hooked commit, complete final branch inventory and independent
mandatory review, then separately authorized longer acceptance on that exact
committed head. The shared R1 smoke has only metadata/invocation unit proof so
far; real isolated retained-gem activation remains post-review acceptance.
Lead owns shared state/portal coordination. No master integration, registry
mutation, publication, configuration/deployment, lifecycle or cleanup is implied.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
