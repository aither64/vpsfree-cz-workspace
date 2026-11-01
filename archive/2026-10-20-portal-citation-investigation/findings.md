# Raw citation markers in the workspace portal

The reported response exposes unresolved web-tool citation syntax. The deployed
portal renders ordinary Markdown without interpreting citations or connecting
them to the source metadata retained in the same conversation.

## Confirmed chain

1. The original final response, recorded at 2026-10-20T13:01:36.409Z, already
   contains two citation tokens referring to three source IDs. Its output_text
   annotations array is empty. The portal did not invent these characters.
2. The web lookup used `codex_apps/search_service.web_run` through
   `functions.exec`. App Server retained these as `mcpToolCall` entries. Their
   results include `_meta.raw_messages[].content` records with
   `content_type: sonic_webpage` and explicit `ref_id`, `url`, and `title` fields.
   This metadata survives in the public transcript's tool `details` JSON.
3. In the installed codex-web source, `TranscriptEntry` has no citation/reference
   fields (`codex/client.go:193`). The `agentMessage` case copies `item.text`
   (`:4067`); the `mcpToolCall` case serializes the result as generic details
   (`:4083`). Neither associates source records with the answer.
4. dev-workspace's `presentTranscript` passes each answer's text directly into
   `renderTextMarkdown` (`portal/internal/web/server.go:3657`). That function
   parses Markdown, rewrites local source-file links, renders, and sanitizes
   (`:3678`). The Markdown configuration enables table support (`:473`), with
   no citation extension or reference resolution.
5. The running portal's read-only endpoint returns both tokens verbatim in
   `entry.html`:
   `/codex/conversations/2026-10-19-dynamic-python-api-client/thread/page`.
   The browser assigns that HTML to `element.innerHTML`
   (`portal/internal/web/static/app.js:4275`). There is no later citation pass.

This reproduces the defect on the server before browser display. The markers use
Unicode private-use characters U+E200, U+E202 and U+E201 around `cite` and the
reference IDs. They are application-specific syntax, not Markdown. Neither
Markdown parsing nor HTML sanitization converts them into source links.

## Sources are available

| Referenced ID | URL retained in tool metadata |
| --- | --- |
| `turn489060view0` | https://pypi.org/help/ |
| `turn489060view1` | https://pypi.org/help/ |
| `turn510980view1` | https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/ |

The reference IDs are real results from this turn. A broad claim that the sources
were lost, that `functions.exec` discarded all metadata, or that the model made
up the citations would be incorrect. The missing piece is consumption of that
metadata by the presentation path. Empty final-message annotations also mean
that an implementation handling only output_text annotations would miss this
specific case.

## Verification and identities

The live service executable is
`/nix/store/1i1g6rp8ind51qqayzpww7cn1xp1k1gq-dev-workspace-0.2.0/bin/workspace-portal`.
Its derivation selects source
`/nix/store/gn8az8v3j2yw8mv8cxq6b68zy0jgblgc-source`; that source pins codex-web
`f3633de3903fc85ca829fbb641b44b016ba152be`. Source inspection used the exact
installed files, rather than assuming the local default branch was deployed.

The original thread is `01a155f8-c3b7-7df1-a887-da7b35164c6a`; the final item is
`msg_067291d6b3b993fe016ad76627a3988191b0d20d926e4961cf`.
[Curated evidence](evidence.json) preserves the original message and empty
annotations, the live served entry, relevant tool reference metadata, package
identity and deployed browser asset hash. A focused Python probe asserted:

- Original recorded text equals the live served answer text.
- Both citation tokens survive unchanged in served HTML.
- All three used reference IDs resolve from retained MCP metadata.
- The corresponding source URLs are absent from the rendered HTML.

The normal account-registration and account-publishing Markdown links render
correctly. No new turns were sent to the reported conversation. Full downloaded
page/transcript/browser assets were removed after extracting compact evidence.

One inspection command initially assumed the older `nix derivation show` JSON
layout. The installed Nix wraps derivations under `derivations`; correcting that
reader established the exact source above. This was an inspection-only failure.

## Follow-up implementation boundary

The reusable citation/reference contract belongs in codex-web. Normalize source
records from web-tool results into bounded, explicit reference data and carry
them through history and streaming updates. dev-workspace's Markdown presenter
should consume that data and render recognized citation tokens as readable source
links, retaining the existing sanitizer and URL validation. The generic
codex-web browser UI also needs to consume the shared presentation contract.

Define a readable fallback for unavailable references. Preserve literal markers
inside code and avoid a blanket Unicode/private-use-character removal. A future
verification set should cover this exact MCP metadata shape, multiple references
per token, unknown references, old paged history, streaming partial tokens, code
examples and unsafe source URLs. History loading must retain or recover sources
when a referenced tool item falls outside the current page.

## Historical check

The missing citation support dates back to the portal's first implementation on
2026-09-04. In dev-workspace commit
`5d2f39c18a8854761435a410a66429e553e58697`,
`portal/internal/web/static/app.js:64` creates message elements and assigns answer
text directly with `textContent` at line 76. Markdown rendering was added later
that day in `0eae65c75eadfee3016f3f036d033790c3d7df01`, using plain Goldmark and
sanitization, without citation handling. The current rendering path retains that
limitation.

The reusable-client extraction on September 10 retained plain message text.
The September 12 change titled "render web searches and subagent interactions"
(`fd03a784d1e70c3fc406d3fa60a9120a47529333`) added activity cards; it did not add
answer citation rendering. Searches of the complete, non-shallow local histories
of both repositories found no implementation of citation-token handling or MCP
web-source metadata consumption that was subsequently removed.

This establishes a longstanding missing feature. It does not establish when
Codex first began emitting this token form, whether an upstream behavior change
made it more common, or when it first appeared to a user in a deployed portal.

This is an investigation finding, not an implemented correction. No application,
configuration or deployment changes were made. Findings remain in this
initiative; product documentation does not need to describe an unimplemented fix.
