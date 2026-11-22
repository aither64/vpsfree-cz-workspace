# Read collaboration items from the installed Codex schema

When collecting live delegation evidence from Codex 0.154.0, the installed
ThreadItem variant is `collabAgentToolCall`, not the `collabToolCall` name in
some App Server documentation. Filtering only the latter silently drops spawn
and wait evidence from an otherwise successful notification capture.

Generate schemas with `codex app-server generate-json-schema --experimental
--out DIR` and inspect `v2/ThreadReadResponse.json`. The collaboration item
includes `model`, `reasoningEffort` and `receiverThreadIds`. Retrieve completed
thread history when a live filter omitted these items, but note that namespaced
`collaboration.spawn_agent` events may not be reconstructed there. Inspect the
raw rollout spawn arguments to verify the model, effort and fresh-context
request in that case. Socket notifications may include other threads: filter
exact thread IDs before recording evidence. Keep raw captures private and
commit only curated, credential-free summaries.

Verified against the installed schema during
`work/2026-09-17-luna-monitoring/`; no runtime change is required.
