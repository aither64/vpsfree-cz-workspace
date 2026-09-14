# General review: bounded CI remediation

No Blocking, Important, or Advisory findings.

Reviewed directly with gpt-6-astra / xhigh under the mandatory-change-review
skill and General lane. Scope is the two runtime commits from
`63cbc32173f73da313e4f11c9c2214884f6161d5` through
`cdcaafa0333cd7aa1f48e6eedc3424ca5d447b13`, organization pin delta
`3f602aef0662b23eef9f7aa2f4c5a76e20e943bd` to
`6f59c3017b6da91bd5745a35a934be265b8330f1`, and workspace pin delta
`c986868b94ef67c9ecf9a65b814f1f18793dadee` to
`5bd3d8b409dfa466438777a2e31aad6202a62c6a`. The completed presentation review
was not repeated.

The commit split is appropriate: `615444b` retains Git failure diagnostics and
adds its regression and failure reporting; `cdcaafa` isolates background
maintenance in the pagination fixture. Downstream changes remain consolidated
in the existing dependency commits. Their exact runtime and organization pins
agree across flake declarations and lockfiles, with no unrelated dependency
movement in the specified delta.

In `portal/internal/repository/review.go:169`, stderr is copied only onto the
existing `exec.ExitError` after the established output-limit and context-error
branches. The existing 8192-byte stderr bound remains in force. Exit type, exit
code, and `Error()` stay unchanged; HTTP review errors continue through the
existing generic error mapping. No new response, retry, repository configuration,
or persistence behavior is introduced.

The pagination fixture configures only its own temporary repository before
creating the additional commits. This matches the existing bulk-rename fixture
and leaves its page-boundary/count assertions intact. The diagnostic regression
checks both retained stderr and the unchanged public error text. Commit messages
describe the final behavior and rationale and follow the repository conventions.

Read the review packets, initiative plan/state, applicable local instructions,
commit diffs/history, fixture creation and Git helpers, and HTTP error handling.
The runtime worktree is clean and the reviewed diff passes `git diff --check`.
Independent focused verification passed in the repository Nix environment:

```sh
nix shell --inputs-from . nixpkgs#go nixpkgs#gcc -c bash -c 'cd portal && go test ./internal/repository -run "^(TestReviewGitFailureRetainsDiagnostic|TestReviewTotalMatchesFullHistoryAcrossPageBoundaries)$" -count=1'
```

Result: PASS, 1.491s. No long integration tests were run for this review.

Residual limits: the reported intermittent object-read failure is consistent
with maintenance interference but does not establish the underlying Git cause.
Fixture isolation and passing repetitions do not prove concurrent maintenance
safe in production. This change appropriately makes no such claim and retains
production behavior. Current-head downstream CI/package validation remains the
coordinator's next verification step.
