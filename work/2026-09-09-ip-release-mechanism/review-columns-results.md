# Compact campaign-list columns review

Reviewed vpsAdmin `58a9b71eae255fb2c5547b8be4c41d968ab4dc22` to
`b76affa12f6f8664ce01d329183dc66cb35ab8a7` and KB contracts
`2e5cb3b078ff99805fbc42075ed45a05b576a8f2` to
`c4c4ba469becafde34ea058c4333106725b41678`. Notification templates are unchanged.

Low-risk presentation change; general and architecture lanes were required.
Both fresh reviewers used gpt-6-astra with xhigh effort and no delegation.
General ran through collaboration; architecture used a fresh read-only ephemeral
Codex process after the retained-thread limit prevented another collaboration
agent. Scope and risk lanes were not triggered: no abstraction, API, state,
security, deployment or compatibility contract changed.

Both lanes reported no Blocking, Important or Advisory findings. They confirmed
the existing API counters, normal table helpers, escaped header tooltips,
right-aligned numeric values (including zero), seven-column empty/pagination
rows, unchanged member/detail presentation and the compiled Czech labels.
The API and six prerequisite commits retain their exact hashes, while the ninth
fixture commit retains its patch. KB changes only refresh the exact vpsAdmin
revision; other lockfile nodes are unchanged.

The three repeated tooltip descriptions match the detail view exactly and do
not duplicate count or eligibility logic. No shared helper or other scope
expansion is needed. No remediation or review rerun was required.

Residual verification at review completion: final-head browser integration and
live bilingual empty/paginated list, unchanged details and member checks were
pending. The existing browser fixture has equal total/release counts; live
fixtures with different values will also check the mapping against details.

Live verification subsequently passed in English and Czech: three short
headers and tooltips, numeric/right-aligned values matching the unchanged detail
summary, seven-column empty rows, one-row pagination with navigation and the
unchanged two-column member list. The original administrator language was
restored. No campaign records or fixtures were changed, and no screenshots were
generated. Only the WebUI PHP worker pool was reloaded; the API and cluster
services were not restarted. Log: /tmp/ip-release-columns-live.log.

Final-head hosted PHPUnit, translation health, RuboCop, KB Check and KB managed
runtime have passed. API Specs also passed all 26 topic jobs and coverage.
The selected integration run remains in progress at this checkpoint; catalog
changes select the broader WebUI suite as well as networking/DNS.

At the 18:13 UTC handoff, [the integration workflow](https://github.com/vpsfreecz/vpsadmin/actions/runs/35126167637)
was still running. Its final result and the checked-in browser scenario remain
pending; the focused live bilingual checks above have passed. The current-head
workflow was left running.
