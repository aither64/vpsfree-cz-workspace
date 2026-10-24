# Three browser fixture alignment candidates

Candidate only, derived from committed B `d617ef3968280e9955da85e2d7464a47030e7087`.
No B source, index, refs or failed evidence was changed. No syntax check, test,
browser, probe, build or CI wait was run. Parent must transfer the explicit
three-file source boundary before application.

`receipt-selectors.patch` changes one optional-question selector and two recovery
display selectors to the shipped accessible name **Dismiss message**, with exact
matching. The ×, accepted delivery, transcript confirmation, storage failure,
saved attempt identity, attachments, successful dismissal and reload assertions
are unchanged. The label was changed by the owning delivery recovery group
`cee4cca1`; keep these selector corrections with that group if practical.

`scoped-limits-mock.patch` matches only the exact `/api/codex-limits` pathname,
including its query. The separate `/api/codex-limits/reset` mutation interceptor
and all credit/reset/layout/upload assertions are unchanged. A boolean is set
after the mock fulfills a read with `session=example`; the normal bounded
Playwright `expect.poll` must observe it before the credit-summary assertions.
There is no provider mock or timeout change. Group this preexisting fixture
repair with implementer0's model-mock correction after serialized integration.

`candidate-manifest.json` binds both patches and the three exact base/candidate
file contents. Construction checks verified replacement counts and that undoing
only the proposed changes reconstructs each original file byte for byte. This is
candidate construction evidence, not test execution or acceptance.

The retained failure is `../followup-browser-final/run/B-full-browser.log`, with
`run/result.json` and `watcher/result.md` in the same packet. These artifacts and
the earlier passing notification evidence remain unchanged.

After authorized application, syntax-check exactly the three changed CJS files
in B's Nix environment before committing. Parent direct diff/checks use the
accepted mandatory-review narrow-follow-up disposition; expanded contract or
source changes return to the lead. Parent's fresh Luna utility then runs the
three actual targeted fixtures under the existing pinned Playwright/browser,
absent-provider and review-assets overlay environment, bound to the new head:

```sh
nix develop --no-update-lock-file -c go -C portal test -mod=readonly \
  -overlay /tmp/portal-followup-browser-assets-overlay.json ./internal/web \
  -run '^TestQuestionBrowser$/(optional_questions_browser_test[.]cjs|recovery_display_browser_test[.]cjs|usability_browser_test[.]cjs)$' \
  -count=1 -timeout=10m -v
```

No product, API, cache, persistence, protocol or migration change is proposed.
Later fixture stages remain unverified until this run. Do not overwrite or
replay the original exact-d617 guard as evidence for a changed source head.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-dev-workspace-portal-improvements/
