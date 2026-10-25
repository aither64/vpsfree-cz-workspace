# Go documentation query correction receipt

Implementer2, 2026-10-22. Direct bounded lead brief, based on
[the query diagnosis](package2-go-query-diagnosis.md). Session/environment and
saved workspace-write access matched before work. Source base:
`ee67d27419c48d27a01c83a29114adf9a82062ba`.

## Exact two-path package

- `clients/go/spec/documentation_acceptance.rb`: correct only the expected
  `widget[enabled]` string from `"false"` to the SDK's established `"0"`.
  Nullable input remains `widget[name] == ""`, integer zero remains
  `widget[count] == "0"`, and unselected fields remain absent. Strict full
  parsed-query-hash equality is unchanged. Capture WEBrick's existing
  request-owned `query_string`; on query mismatch, print expected and actual
  parsed query plus raw query. This deterministic fixture diagnostic includes
  no bodies, auth headers or tokens and adds no product tracing.
- `clients/go/spec/documentation_wire_check.rb`: extend the existing native
  checker through real in-memory `WEBrick::HTTPRequest -> serve -> verify`.
  One exact query passes; eight mutations must fail with useful parsed/raw
  diagnostics. They cover the false string, true value, wrong integer, wrong
  nullable value, each missing field, and one extra field. Existing seven body
  positives and 52 body negatives remain intact.

Lead directly accepted the exact source/test diff, inline boolean comment and
controlled-fixture diagnostic after applying the main writing workflow. No
product documentation change is needed for this test-only expectation fix.
No generator, renderer, runtime, SDK/schema/default, dependency or other product
input changed. The ordinary optional-generator dependency boundary is retained.

## Evidence and quick checks

The prior actual run compiled all 16 rendered programs and passed the executed
object/empty/omitted/list/failure/association cases before the opaque query error.
Its actual raw query was not retained. That run's artifacts/logs remain untouched.

The separate listener-free diagnosis probe exited 0. Actual WEBrick capture of
the constructed template-established numeric-boolean query was
`{"widget[count]":"0","widget[enabled]":"0","widget[name]":""}`. The actual
verifier rejected the old expectation and accepted only the corrected one.
Constructed operation/state, three auth-call and hostile-body fixture controls
also passed actual `serve`/`verify`. Source inspection found no further proven
mismatch in those remaining seams. None of these controls claims actual Go
execution or recovery of the failed run's wire capture.

Focused command:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c \
  'BUNDLE_GEMFILE="$PWD/clients/go/spec/documentation.Gemfile" bundle exec ruby \
    clients/go/spec/documentation_wire_check.rb'
```

Result: **7 accepted bodies / 52 rejected body mutations; 1 accepted query /
8 rejected query mutations**. The checker uses the existing dedicated bundle
explicitly; it does not install, skip, generate, compile or start a listener.

Final syntax/style/whitespace invocation passed after formatting-only blank-line
corrections requested by RuboCop:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -c 'set -e
ruby -c clients/go/spec/documentation_acceptance.rb
ruby -c clients/go/spec/documentation_wire_check.rb
BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile" bundle exec rubocop clients/go/spec/documentation_acceptance.rb clients/go/spec/documentation_wire_check.rb'
git diff --check -- clients/go/spec/documentation_acceptance.rb clients/go/spec/documentation_wire_check.rb
```

Both syntax checks returned **Syntax OK**; RuboCop reported **2 files inspected,
no offenses detected**; whitespace was clean. The final diff was inspected and
contains only the exact expectation, fixture-only diagnostic/capture and pure
checker changes above. No behavior changed after the successful focused run.
All owner2 command sessions have exited; no compiler, listener, install or full
Go acceptance retry was invoked.

## Source yield and remaining gate

The exact two application paths are yielded to sole Git owner implementer0.
Implementer2 explicitly authorizes their stage, hooked commit and fold into the
existing Go owning purpose, retaining the 22-purpose series and final Version
commit. No owner2 Git/index/hook mutation was performed. There is no active
owner2 source/setup command and no further source edit is planned without a new
assignment. Lead retains shared tracking ownership.

SHA-256 at yield:

```text
c6a9521990dfe7d4b07b46097ec99588f4529d008789ed7f66973e82cf6e3453  clients/go/spec/documentation_acceptance.rb
05fa6dc66a006174202e038f6d4851bfce37ecc09aef619606550168225ee13f  clients/go/spec/documentation_wire_check.rb
```

Remaining: hooked commit/fold, same-reviewer affected final review, and separately
authorized actual Go execution. Full Go acceptance is still pending. Preserve
all earlier logs/artifacts and exact product inputs; no integration, publication,
deployment or lifecycle action is implied.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
