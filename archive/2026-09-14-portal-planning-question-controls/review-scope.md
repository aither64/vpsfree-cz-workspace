# Scope and proportionality review

Reviewed the committed ranges:

- `dev-workspace` `e9ed544bf66ba8be07b4fca27aede6e6fd1bfe0a..df21f2ea8fe27efdb2cb8c0330fa31acd0f3a933`
- `vpsfree-dev-workspace` `916223fce1c5b7b78578ca8a16aaaa472c68b08c..89a03581b13056fa83114e592f2e2993e6a87887`
- `workspace` `f523eddf3e1d1cdebf445992318247030e11c7f3..1e01e557cac5527666d5b1e35fa52fadcdbb81af`

Lane: scope and proportionality. Reviewer model/effort: `gpt-5.6-sol` / `xhigh`.

## Findings

No Blocking, Important, or Advisory findings.

## Proportionality assessment

The implementation is a proportionate realization of the accepted question UI and deployment plan:

- `portal/internal/web/static/app.js:80-138` replaces the old plan-only visibility helper with one private controller for the three views that compete for the same composer area. Its state is limited to completed-plan visibility, rendered answerable questions, the existing composer, and the existing Interrupt element. This is the smallest credible shared owner because plan rendering and pending rendering refresh independently; separate visibility writes would recreate the reported race. Focus identity/selection preservation and the response-settlement restoration at `app.js:2311-2329` directly implement the explicit draft/focus requirement rather than adding a general focus framework.
- The request ID and button names at `app.js:2385-2406` are local DOM identity hooks needed to preserve focus across the portal's existing full pending-card replacement. Interrupt is moved, rather than duplicated, into the first rendered answerable question header. The priority order at `app.js:87-118` remains question, completed-plan decision, composer, while terminal-only, errored, unavailable, and ordinary approval cards never acquire the `question-approval` marker.
- `portal/internal/web/static/style.css:241-243` adds only the accepted question-header layout. Removing the former `max-height: 600px` compact-composer rules is appropriate cleanup because the composer is now absent whenever those question-specific rules would apply; retaining them would be obsolete maintenance surface.
- The 201-line Playwright scenario plus its 76-line Go host are substantial but bounded to browser-owned acceptance behavior: DOM replacement, focus and selection, one relocated Interrupt control, failed/reconnected responses, retained draft/upload state, plan precedence, and the requested viewport geometry. It reuses the real test server, template, CSP, TLS, event stream, and upload handler and adds no product endpoint or reusable test framework. `PORTAL_BROWSER_TEST=1` keeps Chromium and Playwright out of routine Go checks, which is a proportionate dependency boundary for this focused regression.
- The two consumer commits are pin-only. `vpsfree-dev-workspace` changes only the `dev-workspace` source revision and its lock metadata. `workspace` changes only the `vpsfree-dev-workspace` source revision plus the expected transitive `dev-workspace` lock node. Site configuration, the shared provider pin, and unrelated inputs remain unchanged. This is the minimum pin chain needed for the authorized assembled-package deployment.

## Residual test gaps

- The browser regression exercises Nix-packaged Chromium only. It does not establish behavior in other browser engines.
- Thread and pending API snapshots are controlled at the browser request layer, so live Codex App Server delivery is not exercised. This is proportionate because the provider, request schema, validation, and answer encoding are unchanged, while the real host renderer and transport handlers are exercised.
- The regression is deliberately opt-in and therefore detects regressions only when the explicit browser check is run. The recorded successful run covers the accepted behavior; packaged checks and deployed smoke verification remain the appropriate post-review steps.
