# Final three verification checks

- Result: passed; batch exit status 0.
- Tested head: `a8ea3132e7efe601aaa8965afe648459b3dab5c5` (tree `9a596258d912ca2075c36ded30d11b3984c656ae`).
- Batch elapsed time: 29.61 seconds.
- Checks: 3 passed, 0 failed, 0 unrun.

| Check | Command | Exit | Elapsed | Log |
| --- | --- | ---: | ---: | --- |
| 06-python-package | `nix develop .#client-python --command bash -euo pipefail -c 'cd clients/python; uv run --locked python utils/package_smoke.py'` | 0 | 2.516 s | `06-python-package.log` |
| 07-release-check | `nix develop . --command bash -euo pipefail -c 'make release-check'` | 0 | 17.493 s | `07-release-check.log` |
| 08-release-test | `nix develop . --command bash -euo pipefail -c 'make release-test'` | 0 | 4.525 s | `08-release-test.log` |

No owned operation remains running. Per-check statuses and aggregate status are retained in this directory.
