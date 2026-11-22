# Count the canonical submitted goal in Codex0.160 rollouts

An acceptance harness reached a real Full-team warmup ready in7.230879s,
then rejected model completion because it counted event_msg/user_message.
The selected0.160 persisted rollout had no such event. It stored one exact
goal as response_item/message with roleuser and input_text content; another
user message held AGENTS/environment context. There was one started/completed
turn, one assistant response and no tool activity.

Use the selected rollout's canonical request representation and distinguish
context from the actual submitted goal. Do not count all user-role records or
both canonical records and event echoes as independent submissions. Preserve
missing/duplicate/unexpected goal refusals and the no-tool/completed-turn gates.
Validate a new harness's real registration, launcher/native/socket and rollout
contracts with a small retained smoke before spending time seeding thousands
of real histories.

The counter correction and remaining measured acceptance are tracked in
`work/2026-10-02-portal-creation-performance/`.
