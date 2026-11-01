# Final committed citation implementation review

Read workspace AGENTS.md and the affected repository instructions. Apply
/home/aither/.codex/skills/mandatory-change-review/SKILL.md and all four lanes:
general, architecture, scope/proportionality and risk/compatibility. Read their
full references. Perform the review yourself; no source edits or nested agents.
Write findings and explicit history/migration conclusions to review.md here.

Request: implement numbered clickable web citations in both browser clients and
prepare matching aitherdev system/profile artifacts, without activation or merge.
User chose numbered links, titles on hover. Preserve raw text, literal code,
sanitization, history paging, tenant/thread isolation, and copied Markdown links.

Review all four committed branches listed in review-inventory.json, their whole
base-to-head series and final diffs (separate *-series.txt / *-review.diff). All
intended code, tests, docs and pins are committed. The original report and metadata
are findings.md and evidence.json; design.md records implementation decisions.

Inherited baseline: running package source was compared by Git blob hash for
every tracked file and exactly matches dev-workspace d68f88aa6ffdf99e6929a29c0d9ad2531a19936a,
which pins codex-web f3633de3903fc85ca829fbb641b44b016ba152be. Preserve its optional
question/provider and archive recovery behavior. Those original feature refs
remain untouched; this branch builds on that supported live boundary. Assess
the inherited series and dependency streams explicitly, including any required
consolidation. New changes have one client functional commit, one runtime pin
commit, one portal functional commit, one workspace pin and one generated
confctl pin. Generated messages are retained. No migrations, schema changes,
Codex upgrade, credentials, deployment execution or master merges.

Owner/public contract: codex-web adds optional UTF-8 citation spans and pending
state, passive async source recovery, shared Markdown/copy and DOM rendering.
Actual consumers are its generic conversation UI and dev-workspace's custom
Markdown presenter. Inspect imports, go.mod and flake pins to verify this.

Quick verification passed: citation Go unit and race tests; all shared Node
browser contracts (74); portal citation/sanitization tests; the server-backed
TestShippedBrowserClientMatchesSessionAPI after adding citations.js to its asset
fixture. Composed workspace/configuration check passes at runtime 2f2966b.
A wrong direct broad portal Node glob required live fixture servers/Playwright;
it was stopped and the supported Go browser harness then passed. No full long
package suite or aitherdev build has started; they follow review.

Documentation: codex-web docs/reference.md owns the optional span/lookup contract;
dev-workspace docs/workspace-portal.md owns visible behavior and links upstream.
The existing configuration operations/workspace-coordination-aitherdev.md remains
the authoritative site procedure. Per-rollout evidence stays in this initiative.

Risk classification high because of public cross-project presentation, untrusted
source URLs and deployment preparation. The local operator is trusted; remote
clients/content are not. Keep URL validation, Markdown sanitizer and authority
checks. No persisted state migration or rollback format change.

Reviewer selection: no retained managed lead/roster; installed schema-6 catalog
default lead_reviewed / review-purpose reviewer = gpt-6-astra, xhigh. This is the
required standalone fallback, not a new team member. Report Blocking, Important
and Advisory findings with evidence. Do not assume the implementation or stated
baseline/history dispositions are correct.
