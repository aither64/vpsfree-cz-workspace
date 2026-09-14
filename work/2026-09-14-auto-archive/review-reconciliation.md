# Review reconciliation

High risk: automatic lifecycle transitions, private persisted state and user-profile deployment. All four required lanes ran with gpt-5.6-sol and xhigh; original reviewed heads and lane reports are retained alongside the packet.

| Finding | Lanes | Decision and verification |
| --- | --- | --- |
| Blocking: unknown observations age candidates | Architecture, risk | Reset marker on failure; next healthy observation starts a fresh interval. Scanner regression covers 24/168/336-hour tiers. |
| Important: reused slug inherits hold/results | General, architecture, risk | Bind complete observation/control record to current conversation identity; status and hold also rebind. Real delete/recreate tests cover held/unheld predecessors, hold before first scan, and same-identity reset. |
| Important: scan JSON contains subprocess output | Architecture, risk, scope duplicate | Route both runner and subprocess operational output to stderr. Non-dry CLI test archives a disposable session and parses exactly one JSON response. |
| Important: old initiator cannot clean candidate timers | Risk | Candidate enables timer after core activation and performs failure cleanup itself, including partial enable. Tests model old wildcard linking, configuration failure and partial timer enable. |
| Important: timer stop bypasses recovery | Risk | Stop inside rollback/unregister recovery scope; timer errors are collected while clients are restored. Explicit failure tests pass for both commands. |
| Important: revival removes journal before sidecar reset | Scope | Reset under final creation/session locks before journal finalization. Corrupt-sidecar test retains runtime_started journal, repairs state and retries successfully with hold preserved. |

All findings fixed. General's positive merged-tier coverage gap is closed by an actual successful seven-day archive which retains the branch and removes the clean worktree. No additional scope drift or consumer pin mismatch found. Changes are direct remediations within the reviewed design; no public schema, archive authority or accepted policy expanded, so no reviewer rerun is required by the skill. Fixes are folded into the owning worker commit; portal remains a separate commit. Final generic head: c33238eeeb3d527a2d30d88aef2e7bd935066136.

Focused results: automatic and archive tests 26/579; revival corrupt-sidecar test 1/17; host tests 77/485; pure retention tests 8/33. Previously passed Go/browser contract tests are unchanged. Packaged and live checks follow this gate.

The read-only deployed browser check found that the Keep open label lacked
the existing `checkbox` CSS class, causing a full-width input. The portal
commit now reuses that class (final runtime 83136101866eb42d9e079f47191308c0549ac9e7).
This is a one-line style correction with no contract or behavior change; no
new review lane is warranted. Final package/browser checks follow.
