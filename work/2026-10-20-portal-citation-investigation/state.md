---
lifecycle: active
---

# Portal citation investigation

Phase: implementation authorized on 2026-10-20. Investigation complete. The deployed Markdown presenter does not resolve
web-tool citation tokens. All three source references are available in retained
MCP metadata, but codex-web exposes them only as tool details and dev-workspace
renders answer text without consuming them.

See [findings](findings.md) and [curated evidence](evidence.json). No application
fix or deployment was requested or performed. No project branches or worktrees
are owned, and there are no merge obligations. The session remains open for
follow-up; no archive action is authorized.

- [x] Identify the reported session and original response read-only.
- [x] Trace deployed rendering and citation data through the client.
- [x] Reproduce and record root cause and recommended correction.
- [x] Prepare findings and evidence for handoff.

Initial evidence: the original final response was recorded at
2026-10-20T13:01:36Z in thread 01a155f8-c3b7-7df1-a887-da7b35164c6a.
Its raw output_text includes the reported citation markers and annotations: [].
The web-search tool was invoked through functions.exec, rather than native
webSearch transcript items.

Verification: live read-only thread/page request plus exact installed source and
browser asset inspection; a focused Python probe confirmed text equality,
unmodified tokens in HTML, all source IDs resolvable, and missing rendered links.
No automatic independent review is triggered by investigation findings/evidence.
No product documentation changes are useful before implementation.

Next action: a follow-up fix can add a shared citation/reference contract in
codex-web and consume it in the portal's Markdown presenter. No current blockers
prevent the requested root-cause conclusion.

Follow-up historical check: citation rendering was already absent from the first
portal implementation on September 4 (`5d2f39c`), its Markdown addition that day
(`0eae65c`), and the September 10 reusable-client extraction. Complete local
histories show no removed citation implementation. The September 12 web-search
UI work added activity cards only. When Codex first emitted this citation form
or first exposed the gap in a deployed conversation remains undated.

## Implementation authorization

User: "Implement the plan." Scope includes both citation consumers, shared
normalization/history resolution, reviewed feature branches and prepared
aitherdev system/profile artifacts. Live activation and master integration are
not authorized. The current conversation created this initiative earlier;
explicit paired environment identity resolves current to this same slug.
There is no managed lead or retained roster (team list refuses with no valid
lead); implementation stays with the parent and final review uses the installed
catalog fallback. No team is created or reconfigured.

- [ ] Shared client, source resolver, parser and browser view
- [ ] Portal Markdown integration and copied links
- [ ] Quick checks, committed source and independent review
- [ ] Package/CI verification and deployment pins
- [ ] Aitherdev system/profile build and retained preparation

