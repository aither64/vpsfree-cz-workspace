Result: failed (exit 1)
Tested revision: 475b97df6c833de7d89d9d61a186a9dee3043938
Command: nix develop --command bash -e -c 'npm run typecheck:e2e:core; npm exec --no -- prettier --check scripts/fixtures/e2e-type-coverage.json tsconfig.e2e.json'
Elapsed: 15.7 seconds
Evidence: E2E type coverage passed (102 checked, 180 deferred); Prettier check flagged tsconfig.e2e.json formatting. The shell stopped on that first nonzero exit.
Full output: webui-advisory-e2e-types-fixed.log
Still-running owned process: none
