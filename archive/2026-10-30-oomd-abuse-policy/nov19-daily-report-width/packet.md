# Daily-report width change

The EN HTML admin daily report now fills the available email window with 12px outer horizontal margins and 12px card-cell padding. Only `templates/daily_report/email/en.html.erb` changed: the 640px outer-card maximum was removed and the cell's horizontal padding reduced from 24px to 12px. All content, links, inner-table styles and every other template are unchanged.

- Repository/worktree: `worktrees/2026-10-30-oomd-abuse-policy/vpsfree-notification-templates`
- Accepted parent: `1ba7169bf64c61cff8802af33279260c0f81bfc8`, tree `1ef951adf31f8f0be18972c567c9995426d868c9`
- Final head: `535b46920382b80b4d733871ccbdc9d242f0eeef`, tree `8e0cd09138e04c7948c7f7497f89f48efed19334`
- Historical recorded base: `2cfd218d9152888feea4109f064459078ea9f76e`
- Create-only preservation ref: `refs/preserve/2026-10-30-oomd-abuse-policy/daily-report-width-base-1ba7169b` → exact accepted parent.

The normal focused commit completed with exit0. The repository declares no hook framework, core.hooksPath is unset, and its hooks directory contains only sample hooks; no hook bypass was used. Clean source/index and committed-blob equality to the rendered input are recorded in [commit-receipt.json](commit-receipt.json). No source edits, rebases, folds, pushes or other Git mutations followed it.

## Rendered examples

| Viewport | Before card | Final card | Final content | Document | Dense tables needing contained scroll |
| --- | --- | --- | --- | --- | --- |
| 1280px | 640px | 1256px | 1226px | 1280px | 0/40 |
| 390px | 366px | 366px | 336px | 390px | 33/40 |

The card starts at x=12 and content at x=27 in both final viewports. All rightmost table cells remain reachable after contained horizontal scrolling, including the narrow view. No document horizontal overflow or network requests occurred. Screenshots are local synthetic previews, not mail-client/SMTP delivery evidence.

- [Complete rendered dense report](renders/daily-report-dense-after.html)
- [Desktop screenshot, 1280×1000](renders/daily-report-1280.png)
- [Narrow screenshot, 390×1000](renders/daily-report-390.png)
- [Missing-optional-data/sparse report](renders/daily-report-sparse-after.html)
- [Full dimensions and per-table accessibility](visual-result.json)

Both complete rendered text outputs were read, and both screenshots visually inspected. Dense and sparse baseline/final DOM text, link targets, IDs and all table-cell contents match exactly. No wording was changed; the writing rule's protected content was preserved.

## Quick verification and input scope

`python3 nov19-daily-report-width/run-checks.py` ran four synchronous commands from the normal site checkout, stop-first-failure; all exited0 in a 4.868s native invocation. Exact argv/timestamps are in [check-results.json](check-results.json):

1. The repository's declared `notification-template-check` implementation from its unchanged locked backend `9fc0648accd414246d6422e67106ae7217486020`, exported through canonical Git objects, checked77templates/393files. The old packaged checker output was absent from the store; using the identical locked source avoided any Nix evaluation/build or dependency change.
2. The unchanged real `MailTemplateTranslation::TemplateBuilder` and `TimeZones` retained in the accepted older-preview source snapshot rendered only two daily fixtures (dense/sparse), before and after. Exact helper/fixture source hashes and actual loaded Ruby/gem versions/paths are in [render-result.json](render-result.json). The fixture-loader prefix stops before the old multi-template driver; it never invokes that batch, MIME, SMTP, API boot or DB.
3. The established Playwright/Chromium local HTML route checked both viewports/fixtures and created only two screenshot examples. Node24.21.0, Chromium156.0.8078.79; all network requests blocked, zero attempted.
4. `git diff --check` passed.

Ruby3.4.9 came from the retained Nix store interpreter; already-present API gem files supplied ActiveSupport8.1.4.1 and TZInfo2.0.6. Ruby/Bundler variables were sanitized explicitly. This is a pure source/render verification using compatible existing tools, not a newly evaluated whole Nix shell or flake build. No renderer/product tests or generic layout abstraction were added for the reversible two-line layout change.

## History and review handoff

[change.patch](change.patch) is the entire new delta. [full-series.txt](full-series.txt) and [full-base-to-head.patch](full-base-to-head.patch) retain the complete recorded-base range: three accepted owning purposes (incident mails, writing guidance, older-template styling) plus this deliberately separate daily width correction. Prior accepted history/evidence/refs remain literal. No migration/schema, dependency/pin or payload change exists; no repeated dependency stream was introduced. Further split/consolidation is lead-owned and explicitly deferred by this allocation.

This is a low-risk, localized layout correction with no persisted-state or delivery-contract change. It is ready for root acceptance and mandatory independent review allocation; review and publication are pending. General review plus any applicable architecture/repetition lane can use this packet and the exact two-line diff. Root retains review selection and final whole-branch readiness.

No product documentation update is useful for this visual-only change. Individual verification evidence belongs here; existing repository AGENTS is unchanged. This packet is the implementer evidence addendum for the lead-owned plan/state, with no change to the frozen mail/demo/KB packets. No Nix build/integration, runtime/SMTP/Mailpit, backend edit, CI read, KB/media/capacity/default/registry or lifecycle action occurred.

All owned effects are terminal; see [effects.json](effects.json). The short source/index window and capacity are returned on delivery, retaining concrete daily-mail review-fix ownership. Session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
