# Native Responses HTTP fallback in isolated verification

Codex0.160.0 builtin OpenAI uses provider supports_websockets and session fallback
state. Retired features.responses_websockets[_v2] do not select HTTP transport.
An SSE-only mock returning404 to genuine upgrades produces repeated WebSocket
GETs and no inference POST, even with valid private API-key auth and reachable
firewall-permitted provider endpoint.

Pinned core/src/client.rs handles426 by its supported fallback. For a fixture
that deliberately covers HTTP/SSE, refuse only valid GET /v1/responses WebSocket
upgrades with426. Keep plain GET404 and malformed/unrelated refusal. Require
actual decoded POSTs, full original model/tool/instruction evidence and record
the observed upgrade plus POST. Neither endpoint reachability nor426 is proof
of inference. Keep original provider/model capabilities and normal serving
transport unchanged.

This design covers native HTTP/SSE dispatch, questions, cancellation, teardown
and persistence when their actual checks pass. It does not prove successful WS
framing, reconnect/continuation caching or hostile WS delivery. A positive live
model naming call is a separate serving-path gate, not the complete hostile
WebSocket matrix. Full WS mocking needs a concrete additional requirement.

In work/2026-10-03-automatic-session-slugs, architect accepted this correction
and focused14top-level groups passed. Native proof and later live model call
were still pending at the fixture-review checkpoint; do not infer a release pass
from this design note. See verification.md for execution results.
