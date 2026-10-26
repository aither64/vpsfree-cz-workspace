# Package C: deterministic documentation regressions

Implementer2 completed the three assigned files; no application boundary change
or design deviation was needed:

- `servers/ruby/spec/client_examples/context_performance_spec.rb`
- `servers/ruby/spec/documentation/performance_spec.rb`
- `servers/ruby/test_support/documentation_performance_fixture.rb`

Committed as `de799b595d04e880d092b3e5ef47bce2f4587130`. Git window relinquished
with an empty index; concurrent package D files remain untouched. Normal
HaveapiI18n and RuboCop pre-commit hooks and commit-msg hooks passed. Commit-msg
TextWidth emitted nonblocking warnings for body lines over its optional 72-column
limit; every line complies with the workspace's 80-column maximum. The first
pre-commit attempt found `index.zero?` in the spec; the equivalent `index == 0`
owned-line fix passed the ordinary retry. No hook bypass was used.

The shared fixture loads HaveAPI from the caller's load path so the same fixture
can exercise baseline sources. It creates independent modules and mounted servers
without modifying a registered API. Dynamic renderers need no generator. The
optional Rust mode registers crate `documentation_performance_client`; D owns its
benchmark smoke check. Dimensions count ordinary resources/actions/public samples
and extra string parameters. Fixed coverage adds one admin-only action on the
first resource, one privileged sample per ordinary action, and the common
Custom/scalar/admin-field parameter set.

## Quick checks

Prepared environment, with dependency installation skipped only:

```sh
HAVEAPI_RELEASE_TOOLS_ONLY=1 nix develop -c bash -lc 'cd servers/ruby && bundle exec rspec spec/client_examples/context_performance_spec.rb spec/documentation/performance_spec.rb spec/documentation/auth_filtering_spec.rb spec/client_examples/profile_mount_spec.rb && bundle exec rubocop spec/client_examples/context_performance_spec.rb spec/documentation/performance_spec.rb test_support/documentation_performance_fixture.rb'
```

Passed: 19 examples, 0 failures, seed 62985; 1.94 seconds examples / 1.22 seconds
load. RuboCop: three files, no offenses. Subsequent source changes added the
observed allocation calibration in a comment and the equivalent numeric style
fix required by the root hook.

Real renderers run underneath context-capture wrappers. Three consecutive
admin/member/admin requests return 200, render the normal dynamic client variants
and samples, share one owned description within each request, and own different
descriptions between requests. HTML and captured descriptions/actions/samples
exclude the denied action, field, default and sample markers for members; admin
content returns on the third request. Original request-help values and mutability
are preserved.

## Allocation calibration and baseline proof

Runtime: CRuby 3.4.11, x86_64-linux. Description sizes: 8 and 128 resources. Both
parents and both derivation paths are warmed before measurement; each measurement
contains 40 derivations, takes the minimum of three batches, and includes neither
expectations nor fixture construction. No GC disabling or wall-clock gate.

| Algorithm/path | 8 resources | 128 resources |
| --- | ---: | ---: |
| Candidate, profile replacement | 200 | 200 |
| Candidate, small sample replacement | 560 | 560 |
| Original, profile replacement | 12,560 | 151,760 |
| Original, small sample replacement | 12,560 | 151,760 |

The fixed allowance is 32 additional objects per derivation, or 1,280 per batch.
Observed candidate growth is zero; original growth is 139,200. Independent field
and description identity assertions prevent allocation slack from accepting a
whole-description copy. An explicit `with(description:)` still requires a copy.
Ruby 3.2/3.3 and CI Ruby 3.4 observations remain for the lead's published-head CI
inspection; this local calibration establishes only the runtime listed above.

Raw counts: [package-c-allocation-calibration.json](package-c-allocation-calibration.json).

The isolated baseline run loaded only the exact Context file from HaveAPI
`39909094649b1d14a23f00615775ca7136acf4fd` with read-only `git show`, replacing
the constant in that subprocess. Candidate source and worktrees were untouched.
The two new spec files then produced three failures out of three examples in
1.97 seconds: unchanged-field identity, allocation-size growth, and shared
description identity in a real HTML request. Allocation failure was 151,760
against a maximum 13,840. Raw RSpec evidence:
[package-c-baseline.json](package-c-baseline.json).

The first ad hoc baseline command omitted `require 'rspec'` before `spec_helper`
and stopped with `NameError` before examples ran; the corrected isolated command
produced the evidence above. This was harness setup, not a test result.

No long suites, publication, merges, deployment or lifecycle actions
were performed by this package. Lead owns review,
long verification and branch readiness. Permanent contributor documentation is
package D; the comments beside the allocation check retain the specific test
rationale.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/>.
