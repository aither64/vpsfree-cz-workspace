# Registration assertion correction

The product returned the supported registration plan. The verification helper
incorrectly required `argv == []` after the CLI had added the mandatory reporting
MCP configuration. The corrected pure assertion passes against the original
actual `registration.json`: exit 0 in 0.954 seconds. No source, pins, commits or
live state changed.

`BuildRegistrationPlan` returns an empty native-role argument list, native child
capacity 0 and empty states. The CLI then calls `WithWorkspaceReporting`, adding
five `-c` pairs for `command`, `args`, `required`, `enabled_tools` and
`tools.report_to_lead.approval_mode` under `mcp_servers.team_reporting`. The
corrected assertion requires that exact complete list, including the saved
package path and disposable state/workspace/profile authorities. This excludes
native child/role arguments and foreign, missing, duplicate or changed reporting
overrides. Schema 1, policy 1, capacity 0, empty states and a valid digest remain
required.

This behavior predates the feature. At both upstream B base
`52dcd471186ef874c5c93f4133744195d4815454` and final B
`db25364999aa4bf12b67506662a08e9e464bee33`, `registration.go` has Git blob
`5d950e6d0b7b268abf0957ede4ccf5ff77d92aa0` and its tests have blob
`2cf10ea72e2db953f595974e394aabe83be73616`. Upstream's CLI already calls
`WithWorkspaceReporting`. The portal guide documents direct-thread capacity
separately from the daemon-start reporting server. The existing Go test requires
exactly 10 reporting argv items; the host test rejects an empty reporting plan.

The retained provenance assertion binds all of the following:

- Exact clean C `3de65bbd0e90f0c3b19e0d64ed925158155647a6`, B
  `db25364999aa4bf12b67506662a08e9e464bee33`, and A
  `852e8c51091512bc79ca6c921ef1f5ccc46a9535`.
- Original launcher SHA256
  `3524756528ccaa83a360cca18f6c13cee29b7c942e7369dd4a8c491d2ec1bd4a`
  and unchanged metadata helper SHA256
  `49a3bbc44558ad178fbab008945ba1956ffd1068dda83ac0dd870c1ddbfc9e16`.
- Saved workspace stage receipt: derivation
  `/nix/store/6vf82012b1ljprmznm2jcdizml8g6spx-dev-workspace-0.2.0.drv`
  and output
  `/nix/store/5d43h2q5q7d494l6v718l71lfk0sm5in-dev-workspace-0.2.0`.
- The surviving derivation's output and source
  `/nix/store/l2wg4c2qgg4c8a4nmndh8dpa2bskxkdh-source`, whose NAR hash
  `sha256-YF9+Yd24UK8KbrGcuklUtTW2qSAlVz1TZahRBv9lzyw=` equals final
  workspace B input. That source's own lock pins final A and its exact NAR hash
  `sha256-6dAMMwgGkCJVxUGyckpzyir6ETxpVHvI0w4b00ZQbIc=`. The selected
  extension remains `767dfd587e346168e1443e65ccdb67ce748f3fe3`.
- Unchanged original workspace receipt, saved package path, successful metadata
  log, actual registration JSON and empty registration stderr, with explicit
  SHA256 checks. Original registration SHA256 is
  `7c2aae0c4712878158272a04bc3eda52aa2dc831e3e42cba7b651152cf7f7a36`.

The original script used `set -euo pipefail`, stdin `{"schema":1}`, an empty
environment with `PATH=/empty`, and disposable state/workspace authorities.
It passed workspace, shared and runtime stages plus metadata, completed the CLI
registration, then failed only its pure argv assertion. Its original exit 1 and
915.254-second result remain unchanged. Reuse is based on exact derivation and
input receipts plus the retained actual output, not tree equality alone.

Before the lead's retained-evidence refinement, one bounded metadata reread
stopped in 0.256 seconds because the package output was absent. No registration
or metadata assertion was repeated successfully in that attempt. The original
package and check receipts are preserved. Read-only store queries confirm the
package derivation is valid but its output is not. The pressure-GC journal
explicitly records deletion of that exact output at 2026-10-20 22:38:30 UTC;
see `gc-evidence.log`. This does not invalidate the already produced output.

No realization, build, suite, metadata check or CLI invocation was launched after
the retained-evidence refinement. Restoration is unnecessary for this pure
postcondition. The earlier supplement shell script is superseded and must not be
launched. There is no new GC root or cleanup/lifecycle operation.

Bounded command, from the final workspace worktree:

```text
python3 /tmp/portal-improvements-registration-retained.py
```

`retained-assertions.log` and `retained-assertions-result.txt` contain the pass.
`portal-improvements-post-review-registration.py` is the exact corrected validator;
`portal-improvements-registration-retained.py` adds provenance guards.
`launcher.diff` contains the sole original launcher change. Python AST and shell
syntax checks pass. The existing full launcher was corrected for future use but
was not rerun.
