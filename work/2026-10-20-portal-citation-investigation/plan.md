# Portal citation investigation

Investigate raw citation markers shown in the Codex response linked to the
2026-10-19-dynamic-python-api-client session. This is a diagnosis request;
application fixes, deployment and integration are outside the current task.

Affected components: dev-workspace portal rendering, codex-web transcript
normalization, and the recorded Codex/tool response. Inspect the other session's
transcript read-only; preserve its records, worktrees and runtime ownership.

Trace the original final message and web-search references, inspect the exact
deployed renderer and its source, and reproduce the behavior with a focused
offline check. Distinguish missing citation metadata upstream from handling in
the shared client and portal. Record evidence and the appropriate fix location.

Readers: the operator and developers implementing the follow-up. Keep findings
and reproduction evidence in this initiative; no product documentation changes
are planned for investigation alone.

Compatibility: no production or persistent-format changes. A future fix must
consider stored history, streaming responses, unresolved references and safe URL
handling. It must preserve prose, code samples and Markdown sanitization.

Verification: inspect the retained transcript and deployed asset identities;
run only small local rendering probes, without sending new conversation turns.
