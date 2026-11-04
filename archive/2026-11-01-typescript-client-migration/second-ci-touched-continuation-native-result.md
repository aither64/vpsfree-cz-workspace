# Second CI touched continuation: native result

- Result: failed; exit status 1.
- Tested revision: `129bf840dda84a71c006b875a8afb6301cf53a89`.
- Operation: `second-ci-touched-continuation-observed`; PID 2328145, start ticks 23459655, PGID/SID 2328145; execution handle 89487.
- Elapsed: 115.406 seconds.
- Native counts: 15 passed, 1 failed, 1 interrupted, 161 did not run (178 total).
- Bounded failure evidence: `security_advisories_admin.spec.ts:125` failed after a 90,000 ms test timeout; `locator.selectOption` waited for `getByTestId('admin.security_advisories.nodes.editor.state')` at line 262. The next snapshot export case was interrupted when maxfail stopped the run. Playwright also reported one error not part of any test.
- Durable observer receipt: `second-ci-touched-continuation-observed-state.json` and `second-ci-touched-continuation-observed-exit.json`.
- Log: `second-ci-touched-continuation-observed.log`.
- Browser artifacts: `browser-second-ci-touched-continuation/report/index.html` and `browser-second-ci-touched-continuation/results/` (failure screenshot, video, trace, and error context are retained there).
- Remaining uncertainty: 161 selected cases did not run; native WebKit is covered by CI, not this local operation. No cause was determined.
