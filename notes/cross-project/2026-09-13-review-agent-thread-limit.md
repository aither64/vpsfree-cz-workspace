# Fresh review when collaboration threads are exhausted

`collaboration.spawn_agent` can report `agent thread limit reached` after earlier
completed review threads in a long conversation, despite available concurrent
execution slots. Interrupting a completed agent did not free the thread quota.

Use a fresh ephemeral installed Codex CLI review with the mandatory packet and
lane instructions, required model `gpt-5.6-sol`, and `model_reasoning_effort="xhigh"`.
`codex exec --ephemeral --sandbox read-only --model gpt-5.6-sol -c
model_reasoning_effort='"xhigh"' -c approval_policy='"never"'
--output-last-message <artifact> - < <prompt-file>` preserves fresh context and
writes a review artifact. Do not reuse an old reviewer's conclusions or exceed
the concurrent reviewer budget. The CLI header verifies model, effort and sandbox.

Related: work/2026-09-12-portal-file-uploads/plan-decision-review-packet.md.
