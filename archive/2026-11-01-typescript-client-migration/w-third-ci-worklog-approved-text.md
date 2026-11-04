## Third browser CI repair

Core CI [41480946099](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41480946099)
passed all three jobs on `9d9617c0`. Browser run
[41480945591](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41480945591)
recorded 52 failing headings across 11 additional specs: 23 Chromium, 22 mobile
Chrome and 7 mobile WebKit. WebKit completed with 267 passed, 7 failed and 2
skipped. The Chrome jobs ended as cancelled with incomplete totals; the retained
evidence does not establish their cancellation cause. None of these 11 paths
belongs to the earlier 30- or 27-spec repairs.

The leaf fixtures now use declared collection and resource namespaces, partial
references, selected-template Show responses and canonical mutation envelopes.
The lifetime Start response includes the required `vps` object beside its
existing action-state receipt. The network case checks the dialog's static
parent interface, the fresh host read before each explicit retry and the exact
assignment, owner, PTR and toggle payloads. Production guards and eligibility
rules are unchanged; intended rejection, uncertain-outcome, role, count and
no-replay assertions remain.

Member transaction fixtures model the API's restricted output. Existing admin
cases retain the privileged diagnostics, long payload and geometry checks using
canonical JSON-string payloads. Two existing My-view layout cases use explicit
admin identities and titles. The independent final review on `11cf6019` found
one Important mismatch: three assertions still expected quoted JSON fragments
although the payload reader renders semantic keys and values. The direct remedy
in `2ad8f717` checks those values within their Input/Output regions; fixtures,
roles, titles, error/rollback text and viewport checks are unchanged. Focused
whole-file strict typing, lint and direct review reconciliation passed. No
findings remain open. The complete history retains one generated-client input
stream and has no database, schema or persisted-format migrations.

All 11 edited specs are fully adopted. Only the user-data editor and VPS access
specs needed new whole-file adoption, bringing coverage to 136 checked and 146
deferred. The original baseline, sourceRevision, surviving deferrals and compiler
options are unchanged. The combined strict gate passed on `11cf6019` with zero
diagnostics; the later assertion-only remedy has its own focused checked-byte
evidence and does not relabel that earlier execution.

Both local attempts used `2ad8f717`, two workers, no retries, a first-failure stop
and the existing 900-second limit:

| Selection | Native result |
| --- | --- |
| 126 cases, three projects | 1 timed out during WebKit page setup, 1 interrupted, 124 unrun; exit 1 after 101.261 seconds |
| 118 Chromium/mobile Chrome cases | 118 passed; exit 0 after 548.809 seconds |

In the failed WebKit case, browser launch and context creation completed, but
the built-in `newPage` call timed out before the test body or app requests. The
specific local startup mechanism remains unresolved. The continuation selected
the exact 118 unrun Chrome identities: 59 Chromium and 59 mobile Chrome across
the same 11 files. Every case passed on retry 0 without errors; no earlier pass
was reused. Only project selection and artifact paths changed. All eight WebKit
identities remain pending unchanged native final-head CI; this is not a claim
that all 126 cases passed. The failed attempt and its original observations are
preserved. Post-run inspection found none of the recorded owned processes,
groups/sessions, operation-era worktree processes or listener 5187; the older
unrelated shell was preserved.

At this checkpoint, native WebKit, the broader final-head CI matrix and exact
final-head Nix derivation/provenance checks remain pending. Earlier API,
local-client cycle and Nix results keep their actual input scope. The user keeps
the released-client transition pending; a compatible published dependency is
still required before merge.
