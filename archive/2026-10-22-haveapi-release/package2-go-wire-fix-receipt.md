# Go documentation request-envelope correction receipt

Implementer2, 2026-10-22. Direct lead-owned small correction following
[the wire diagnosis](package2-go-wire-diagnosis.md). Current session/environment
and saved workspace-write access were verified before the work. Source base is
`3fb91caf783eaeacf49bf3647b8409d536339d71`; its failed actual run remains in
`go-final-verification.log`, `.exit` and `-result.json` (196.15 seconds, exit 1).

## Exact two-path source package

- `clients/go/spec/documentation_acceptance.rb`: extract the existing 16-case
  expected table into harness-only `self.expected_cases`, used by both the
  actual runner and focused native check. Expect the established `_meta: {}`
  envelope for `object` and `hostile`; add the same exact body expectation to
  `basic_call`, `token_call` and `oauth2_call`, which invoke the same action and
  sample. Metadata-free `empty`/`omitted` still expect only `widget: {}`. The
  actual private verifier and its strict whole-body equality are unchanged.
- `clients/go/spec/documentation_wire_check.rb` (new): standalone pure Ruby
  check calls the actual private verifier through an allocated harness object
  and an in-memory request queue. It does not call harness initialization, SDK
  generation, a compiler or a listener. A literal captured object body and the
  hostile/empty/omitted fixtures supply positive controls against the shared
  expected table. Mutations are deep copies and must fail at the body assertion.

All 16 existing cases were assessed in the diagnosis. The only proven mismatch
is the metadata envelope of the shared action; unrelated route/query/output/state
assertions and all product code remain unchanged. No arbitrary metadata is
stripped or normalized. No new request values/defaults were invented.

Lead directly inspected and accepted the exact two-path source/test change,
applied the main writing workflow, and accepted the inline comment unchanged.
No product documentation update is useful for this test-only correction; the
owning inline comment explains why these exact expected bodies contain metadata.

## Final quick verification

Final invocation passed after moving the new singleton method above the
instance-method `private` boundary to resolve the first RuboCop finding:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c 'set -e
BUNDLE_GEMFILE="$PWD/clients/go/spec/documentation.Gemfile" bundle exec ruby clients/go/spec/documentation_wire_check.rb
ruby -c clients/go/spec/documentation_acceptance.rb
ruby -c clients/go/spec/documentation_wire_check.rb
BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile" bundle exec rubocop clients/go/spec/documentation_acceptance.rb clients/go/spec/documentation_wire_check.rb'
```

Results:

- **7 accepted bodies:** object, three authenticated calls, hostile input,
  explicit empty input and omitted input.
- **52 rejected mutations:** nonempty/null/missing metadata, extra top-level or
  `unused` input keys, altered false/zero/null, missing supplied fields, and
  accidental metadata/input namespace omission on metadata-free actions.
- Both Ruby syntax checks: **Syntax OK**.
- RuboCop: **2 files inspected, no offenses detected**.
- Tracked `git diff --check` and new-file `git diff --no-index --check` produced
  no whitespace errors; final diff is limited to this two-path package.

The check uses the existing dedicated optional-generator bundle explicitly.
It performs no automatic dependency installation or skip and does not alter
ordinary standalone server dependencies. Initial root-shell entry fetched and
realized existing selected Nix tools; the final rerun completed without further
setup output. No Go compilation, listener, package-artifact build/install or
actual acceptance retry was run. All owner2 commands have exited.

## Yield and remaining gate

Source ownership of these exact two application paths is yielded to sole Git
owner implementer0. Implementer2 explicitly authorizes implementer0 to stage,
hook-commit and fold them into the existing Go owning purpose, preserving the
22-purpose series and final Version commit. No Git/index/hook mutation was
performed by implementer2. There is no active owner2 source/setup operation and
no further source edit is planned without a new assignment.

SHA-256 at yield:

```text
e7b00cea79eda9454f4b3bd45ebf4571cebcda7c418e5a501f60722eff140324  clients/go/spec/documentation_acceptance.rb
2f46589e99a712801710a0c8f5f46f25d98cfb9375db45b46cc2cf2c7d1e5946  clients/go/spec/documentation_wire_check.rb
```

Remaining: hooked commit/fold and same-reviewer affected final review (general,
architecture and scope), then separately authorized actual Go rendered acceptance.
These quick controls establish assertion fidelity, not full generated-client
execution success. Existing artifacts, prior logs, Rust inputs/results, unrelated
untracked files and session lifecycle remain untouched. Lead owns shared tracking.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
