# Bounded CI remediation: Architecture review

No Blocking, Important, or Advisory findings.

Reviewed directly using mandatory-change-review's Architecture lane, with
gpt-6-astra / xhigh. No nested agents or long tests were used. Scope is the two
runtime CI remediation commits and corresponding downstream pin changes; the
completed presentation review is unchanged.

Reviewed revisions:

- dev-workspace: `63cbc32173f73da313e4f11c9c2214884f6161d5` →
  `cdcaafa0333cd7aa1f48e6eedc3424ca5d447b13`, including the separate
  `615444bb2f5d93f14ca772d9520cdec4b024eef4` diagnostic commit.
- vpsfree-dev-workspace: `3f602aef0662b23eef9f7aa2f4c5a76e20e943bd` →
  `6f59c3017b6da91bd5745a35a934be265b8330f1`.
- workspace: `c986868b94ef67c9ecf9a65b814f1f18793dadee` →
  `5bd3d8b409dfa466438777a2e31aad6202a62c6a`.

The diagnostic belongs in the existing `ReviewReader.git` execution boundary
(`portal/internal/repository/review.go:170`). It copies already bounded stderr
onto the existing `exec.ExitError`, after the established output-limit and
cancellation checks. It adds neither another error abstraction nor a retry
policy. Existing exit-code consumers, including comparison ancestry checks,
keep the same error type and behavior. The HTTP adapter still maps failures to
its existing messages, and the existing logger formats the error with `%v`.

Fixture maintenance settings remain explicit in the pagination test
(`portal/internal/repository/review_summary_test.go:17`). They affect the
temporary repository created by `newRepositoryFixture`, without changing the
production Git command or general fixture defaults. The two configuration
lines shared with the bulk-rename test are small, readable setup; extracting a
new abstraction would not improve ownership for this bounded change. The
pagination assertions and real Git reads remain intact.

Consumer inspection confirms the organization package still calls the runtime's
`lib.mkPackage`, and the workspace still consumes the organization's
`lib.mkPackage`. Both downstream diffs contain only `flake.nix` and `flake.lock`
pin updates. Their direct and transitive runtime revisions agree on `cdcaafa`.
There is no new provider, state, packaging, or migration interface to adopt.

Residual limits: the recorded intermittent failure and maintenance trace are
consistent with a maintenance race, but do not establish its upstream cause.
Disabling maintenance isolates the pagination contract; it does not validate
production Git behavior during concurrent maintenance. The new diagnostic test
checks retained stderr and unchanged public error text, while existing tests
cover output limits and deadlines. I inspected those tests and the packet's
reported passing checks; I did not rerun the suites. `git diff --check` passed
for the runtime review range, and the three reviewed worktrees were clean.
