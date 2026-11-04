# Final typed-tail verification

- Result: passed (exit status 0).
- Revision: `a9e2049f5f3445691e4025bca496e342443494f2`.
- Command: the supplied `nix develop ... --command bash -e -c` invocation running `typecheck`, `typecheck:tooling`, `typecheck:e2e:core`, and `typecheck:bff:core`, once.
- Elapsed: approximately 74 seconds.
- Full stdout/stderr: `w-final-typed-tail.log`.

Evidence: all four npm scripts completed; E2E type coverage reported 100 checked and 182 deferred; BFF type tests reported 6 passed and 0 failed. Nix printed a dirty Git tree warning.
