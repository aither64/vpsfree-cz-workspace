# Citation presentation and source recovery

The parent owns design and implementation; no retained roster exists. Preserve
the deployed optional-question behavior: exact source comparison identifies
dev-workspace d68f88aa6ffdf99e6929a29c0d9ad2531a19936a and codex-web f3633de.
Their existing feature refs remain untouched. The new client branch includes
that deployed boundary; the runtime branch starts from the deployed source and
contains current origin/master. Review inherited supported commits explicitly.

Expose optional CitationSpan values on assistant transcript entries, with UTF-8
byte offsets, validated numbered HTTP(S) destinations, and a pending flag.
Keep Text unchanged. A shared Go parser uses Goldmark's code-node source ranges
to avoid interpreting literal examples. Shared Markdown substitution consumes
those spans before the portal's existing parser/sanitizer; the generic browser
uses DOM anchors and the same spans. Copy substitutes ordinary Markdown links.
This avoids a separate browser token grammar and a second HTML trust boundary.

Resolution consumes earlier MCP metadata in the returned page immediately.
Missing references get a per-message asynchronous lookup using the passive
history reader: descend through turn pages until the target turn, skip items
after the target message, then inspect preceding items and earlier turns.
Only requested references are retained. Workers yield after bounded pages;
request refreshes continue their saved cursor. Cache keys include thread identity,
connection generation and rollout file lineage; append-only growth is allowed,
replacement/truncation invalidates. No new durable state or native protocol.
Caches and worker concurrency are bounded; Client.Close cancels workers.

Both browsers retry loaded pages with pending citations via their original
request cursor and merge matching rows without discarding scroll/history.
Unknown sources eventually show [source unavailable]; active partial tokens are
hidden. No source resolution is performed for user messages or artifacts.

Quick checks cover parser, metadata extraction, source lookup continuation,
Unicode spans, copying, browser pagination and sanitized portal rendering.
Final source/history review precedes long suites/builds. Pin the reviewed client
in the runtime; match that runtime in workspace and configuration, validate locks,
and prepare exact committed aitherdev system/profile artifacts. Preserve all
schemas, source messages, execution policy, extension pins and Codex version.
No activation, merge, reboot or reservation is part of preparation. Recovery
notes retain old system identities/profile token and eventual ordered jobs.
