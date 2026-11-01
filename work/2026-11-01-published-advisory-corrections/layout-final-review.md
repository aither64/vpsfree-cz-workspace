# Affected legacy node-form layout final review

No Blocking, Important or Advisory finding was established. The committed scoped layout correction is appropriate for the observed pointer-interception failure. The held strict KB check and real legacy advisory retry may proceed; their outcomes remain unverified by this review.

## Identity, scope and method

Reviewer0, retained independent review-purpose/read_only member, native thread 01a19801-1fc5-70e3-ba37-8c0952a89392; saved gpt-6.1-sol/xhigh on codex-lb, no override/fallback or substantive authorship. dev-session current printed 2026-11-01-published-advisory-corrections from its tracking directory; both session environment variables were absent, consistent with the trusted binding.

Used mandatory-change-review and the applicable general/history, architecture/repetition, scope/proportionality and risk/compatibility guidance, reusing unchanged current-context reads. Overall package risk remains High; this affected delta is bounded layout and browser-verification compatibility. Read layout-review.md and legacy-layout.md in full, inspected actual diff/form helper/template/CSS/callers/regression and retained synthetic scripts, measurements and PNG. No broad repetition of unaffected API/client/modern review.

No source/session writes, tests, builds, fetches, remote mutations, nested agents, production requests, integration/deployment or lifecycle actions. Text returned for the lead to persist as layout-final-review.md.

## Exact committed ranges

vpsadmin, target master:
097226b22edf8b59f80b5dfaa55265e9d0cac633..
49f5a29e5a7d85559d06d31496acb5c08895bcda.

Complete series:
1. 9415cf2855a3f9caef6ab68dc7df8405ed9f3ef8 — API correction/lifecycle commit, exact unchanged object.
2. 49f5a29e5a7d85559d06d31496acb5c08895bcda — legacy advisory management, with layout fix folded into B.

Actual merge base/local HEAD match and worktree/index are clean. Full inventory is 25 paths, +1957/-149; affected comparison is:
006454821ee35b291def4bfafee19cd0553bc7b2..
49f5a29e5a7d85559d06d31496acb5c08895bcda.

Independent Git inspection confirms exactly three changed files, +12/-1:

- webui/forms/security_advisory.forms.php
- webui/public/template/css/main.css
- tests/playwright/webui/specs/security-advisories.spec.cjs

KB, target master:
ce2c8cd9358c3636e5d39343e595df813a0b197f..
5276b64b9cab0d29bc14968730eccf88c230059d.

Complete series: one commit 5276b64b9cab0d29bc14968730eccf88c230059d, Pin KB contracts to expanded advisory management. Actual merge base/HEAD match and worktree/index are clean. Full delta remains five pin files, +8/-8.

## Implementation and acceptance assessment

The native prior-run call log establishes the concrete failure: node_101_add was visible, enabled and stable, but the aside helpbox Edit link intercepted its pointer. Its 11 passed / 1 failed / 6 not-run result is partial evidence. Guest trace/screenshot absence after teardown is recorded honestly; I did not infer visual guest state or full acceptance from those missing artifacts.

The PHP change uses the existing form_create third argument to give only security_advisory_node_form() the name security_advisory_nodes. The actual helper escapes/emits that name and retains its default CSRF behavior. The actual template places CSRF and hidden fields, table and submission inside the resulting form. Existing node JavaScript binds forms/fields by selectors rather than generic_form name; inspection found no conflicting named-form behavior.

The CSS adds only max-width:100% and overflow-x:auto on this exact form name. Its block remains within the fixed content column while its wide auto-layout table scrolls natively instead of painting under the sidebar. The selector does not affect embedded advisory creation, unrelated forms, the sidebar, global table sizing or inputs. No field name, column, input size, guard, membership semantics, payload or backend/API/auth/mail behavior changes.

The existing membership regression adds the named-form and content-bound checks and keeps ordinary check(), subsequent status editing and normal form submission. There is no forced click, hidden sidebar, increased viewport/deadline or input-size reduction. The bounds assertion alone would not establish overflow containment; the retained normal checkbox interaction is the meaningful regression against the actual pointer interception.

The synthetic PHP render uses the actual production form/XTemplate and main/scheme CSS with explicit fake API objects. The temporary Playwright script removes only the new CSS rule for its before measurement, then restores it and invokes ordinary check() without forcing or manual scrolling. The receipt shows an 805px form against a 970px table; natural checkbox interaction scrolls 165px, putting table right at 884.92px within content right 885px. The checked state, size-14 input and publication/revision guards are asserted. I visually inspected legacy-node-layout.png: Actions/Add is inside the content area and the synthetic sidebar remains visible.

This is useful implemented-layout evidence, not real backend validation. It supports the small native overflow fix without justifying a broader table/framework redesign, new UI abstraction or additional screenshot campaign. Existing table/form ownership is preserved.

## Source/input and evidence reuse boundaries

Independent blob/mode graph comparison confirms A is the exact same parent object, and the entire API and tests/runner subtrees equal 006454. The three paths above are the sole successor delta. The complete range-diff shows only those additions folded into B, with no hidden API or unrelated source change.

Final source tree is 0ac9a9144e394a8c963db71a49d059e48ebec23c. Saved final metadata binds it to /nix/store/x2vqnk03hgzbl6qfch00czzm4jsk5a64-source; changed-path store bytes equal their committed blobs. The full locked input graph equals the prior graph. Saved final API-shell derivation JSON is byte-equal to the original verified derivation, SHA256 30d5a1bd662c539f4e091713b4d9ab2ab35b32095622d2c350cab8690de2bd2d.

That supports retaining earlier API evidence at its actual source/derivation/environment boundary. It does not reuse a failed browser attempt as a passed final-layout run. Client 0b771120 and modern 1c8478bc are unchanged/outside this affected scope, with their earlier evidence retained separately.

For KB, independent full lock/source comparison proves only the selected vpsadmin lock node changes; other nodes, root follows and selected-node input edges remain equal. All five locations agree on 49f5a29e5a7d85559d06d31496acb5c08895bcda, narHash sha256-76qu5evtuath+AJrp1PXDavMSxf/vzXxBpuGq7q7Jmc=. Explicit OS remains 6bdf458fd9105379860234ff33d352e55844f08f. Source pin files are byte-equal after revision substitution, preserving capture/page provenance/content/assets. No advisory binding/content/capture has been fabricated.

## Whole-branch history and migration conclusions

The refreshed API retains two logical commits: A unchanged, and the bounded B layout/regression correction consolidated into the owning WebUI commit. No obsolete implementation approach, transitional compatibility path or redundant fixup commit remains in the complete series. No repeated dependency/input stream exists in this feature range.

The KB has one logical vpsadmin pin stream consolidated in one final commit. No repeated superseded pin commit remains, and no supported boundary requires retaining intermediate updates. Prior tested/reviewed heads remain evidence refs; no deployed or default history was rewritten.

NO MIGRATIONS in either complete reviewed range. This successor adds no migration/schema/seed/persisted format or migration version with merge/release/deployment/external-use provenance to preserve.

## Residual checks

Owner quick PHP syntax/formatter, JS syntax, diff checks and mandatory amendment hooks are recorded; I assessed their scope and inspected evidence rather than rerunning them. Synthetic normal-click geometry/image is not real VM/API acceptance.

The final exact KB pin still needs its strict check, followed on success by the real legacy advisory script on 49f5. That retry must establish operator interaction plus the remaining membership/lifecycle flows using ordinary actions. Preserve any new failure and its actual coverage; previous 11/1/6 evidence cannot certify the six unrun cases. No need to repeat unchanged long API/client/modern suites solely for this layout delta.

Session remains open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
