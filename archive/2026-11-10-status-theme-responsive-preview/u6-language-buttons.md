# U6 language buttons

Owner implementer2; direct lead brief for this bounded edit. Capacity/identity,
environment and live saved Sol/xhigh/workspace_write verified. Scope is only
two native language links replacing the select, preserving server SwitchLinks
URLs, current-language state and progressive navigation. No new strings, custom
keyboard handlers, dependency, API, persisted state or migration.

Seven owned files: `templates/{index_header,layout}.tmpl`,
`public/{status.css,theme.js}`, `ui_routes_test.go`, `app_routes_test.go`,
`docs/reference/appearance.md`. Language controls use one always-present pair of
`.language-option` anchors in a labelled `.language-options` group. Both JS and
no-JS use them. Current link has `aria-current=true` and a selected border.
Removed the obsolete select/fallback CSS and three JS wiring lines. Gear/theme
radios, titles, hit areas, first paint/storage/history/dismissal remain unchanged.
CSS URL v5, JS URL v4. Lead applied the user-facing writing skill and supplied
the exact final language/progressive-enhancement wording before commit.

Quick checks passed in the repository Nix shell: focused route batch 0.616s,
normal `go test ./...` 10.885s, preview-tagged tests 14.882s, `make i18n-health`.
Node JS syntax and diff whitespace checks pass. Route assertions cover two
native links across EN/CS shells, selected state, entity/group page2/scenario
queries and the documented About-to-overview exception.

Lead reordered the exclusive index window to U6 first. Amended owning UI commit
`2d448fd21e8ea5ec3b2a1322bb170d35617470ce` into
`c1125948c53c0a36dbf695459221844702408365`, retaining preview parent
`63d34fe341f759455d81e262ffc38fccad8c3cb5`. Only seven owned paths were staged;
Lefthook gofmt/i18n passed (0.44s). All seven file SHA256 values matched before
and after hooks. Index empty, owned paths clean, U5's four unstaged flake/lock/
workflow/tests-README paths preserved. Index window explicitly released to lead
and U5; no push, service or browser mutation. No obsolete language-select followup
commit or migration was added. Lead owns full branch history review.

Disposable final browser preparation: `browser-language-buttons.cjs`, SHA256
`a48b2c7bafa38b57fda78803abf24a32d49ce5be3e33974fd56d732367455620`.
Node `--check` passes. Invocation after final combined review/candidate release:

```bash
/nix/store/lnfxdsvvm1srsa9kk94s7jqw06yq1h2d-nodejs-24.18.0/bin/node \
  /home/aither/workspace/ai/vpsfree.cz/work/2026-11-10-status-theme-responsive-preview/browser-language-buttons.cjs \
  "$U6_REVIEWED_BASE_URL" "$U6_NEW_RESULTS_DIR" "$U6_FINAL_HEAD"
```

New output directory required. Two captures at 320px: real EN/CS native clicks,
entity page2/scenario query and theme preservation, keyboard Tab/Enter, current
state, no-JS navigation and About exception, side-by-side button/panel geometry.
No preview is contacted before release. Prior unaffected passing browser evidence
is retained. Package remains executing through final review/browser and necessary
fixes; no next package accepted.

## Requested local-preview usability check

The user explicitly requested refreshing the UI preview. Lead released the
known-quick focused browser check before independent source review, against
registered immutable candidate `http://127.0.0.1:18086`, combined head
`c4e11ec3f933de75f782b95bb3034ca31e3034d5` (UI source c112594). Exact prepared
script ran once, 2026-11-10 16:54:54–16:54:58 UTC, authoritative exit 0. Both
groups passed; two PNGs. Evidence: `browser-language-buttons-c4e11ec/results.json`
and PNGs, adjacent `browser-language-buttons-c4e11ec.log` with full output/exit.

Real EN→CS and CS→EN clicks preserve entity kind/ID, probe_page=2, scenario=mixed
and Dark preference. Selected aria-current/border, side-by-side 44px targets,
320px panel containment/no overflow, Tab/Enter activation, native no-JS links and
About-to-overview exception pass. Errors/console/network arrays empty. Dark 320px
open-panel capture was visually inspected: both language buttons fit and the
current choice is clear. No harness correction, rerun or source/service edit.
Browser closed and runner finished. Lead notified for requested 4567 refresh.

This is local-preview usability evidence, not independent review approval.
Committed source review remains a separate lead-owned prerequisite before long
integration checks. Package remains current through review/follow-up acceptance.
