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


## Source implementation checkpoint

Shared client a204708d32c12bfe547c5c8bbbcf1b4396490bcb and portal runtime
2f2966bf518b84490e310304d28214ffcbe24f9a are published on the initiative feature
branch. The runtime includes the exact deployed d68f88a baseline, identified
by comparing every tracked file to the installed source. Its client baseline
f3633de retains optional questions. These inherited refs remain untouched.

Quick checks passed: citation Go tests, citation race tests, all 74 shared browser
contracts, portal citation/sanitization tests, and the server-backed shipped
browser contract after adding the new asset to its fixture dependency list.
The broad portal Node glob was a wrong harness invocation: it requires
Playwright and running fixture server URLs. Its surviving process was stopped;
focused server-backed Go tests are authoritative. An initial direct Go executable
call lacked the Nix compiler PATH; rerunning in the dev shell resolved it.
Configuration checkout's post-checkout hook initially lacked Bundler gems. The
verification utility installed its 40 ignored local gems through the config Nix
shell; Overcommit hooks are installed and registration now succeeds.

Pins in workspace/configuration are being generated. Independent review and long
package checks remain pending. No activation or reservation has been requested.

## Deployment ownership handoff preparation

The coordinator requires an exact retained native conversation before it can
seal preparations. This initiative was created as tracking-only during diagnosis.
Initialize its first retained conversation through the supported dev-session
creation flow, with no team preset and an acknowledgement-only initial request.
The external supervising conversation keeps implementation responsibility; the
new retained lead supplies native ownership for supervised preparation. It must
not edit code, run checks or activate anything without explicit handoff.
This is a genuine runtime ownership handoff checkpoint, allowed by the tracking
cadence; it does not grant any integration/deployment approval.

Current heads: codex-web a204708d32c12bfe547c5c8bbbcf1b4396490bcb; dev-workspace
2f2966bf518b84490e310304d28214ffcbe24f9a; workspace
c0187a433a95c4c42b4baa6e3cd872be468fca84; configuration
34249ae7a131c03aad8e8af6a3e68e19a24042a0. Composed deployment contract passed,
with only runtime/client lock nodes changed and the extension preserved.
Standalone final reviewer citation_review uses catalog gpt-6-astra/xhigh across
general, architecture, scope and risk lanes. Review is running; long checks and
artifact builds remain gated on its result.
