# Final independent component review

Reviewer report received 2026-11-26 through report_to_lead; persisted by lead
because the retained reviewer remains read-only. Reviewer0 verified current
session, live purpose review, saved gpt-6.1-sol/xhigh/read_only; no overrides,
fallback or nested reviewer. High risk; all general, architecture/repetition,
scope/proportionality and risk/compatibility lane references read and applied.
No source writes, publication, integration/deployment, services or long tests by
reviewer. Source/diff/history/docs and targeted read-only diagnostics were used.

## Findings

No Blocking findings. One Important finding C-1; no findings in HaveAPI A+D.

### Important C-1: initiating legacy theme lost during authentication

Reviewed C commit: `b1f63a5eab2ffbaca239047eceddc2cc98e075d5`.
Primary `src/app/uiSettings.tsx:108–115`; supporting `index.html:25–53`,
`src/app/theme.tsx:45–58`, `src/pages/oauth/OAuthCallbackPage.tsx:23,33–50`,
`src/pages/oauth/OAuthLoginPage.tsx:25–42`, `src/routes/RouteProvidersLayout.tsx:41–43`.

For a legacy PKCE flow with denied optional localStorage, a valid pending
sessionStorage dark preference, light OS and unfinished token exchange: head
prepaint is dark, but settings initialization sees only local/default or
successful handoff, so initializes system. ThemeProvider removes explicit dark
and progress appears light. Error catch restores dark only later, success
restores after hard navigation. Direct/retry request theme has the same ownership
gap when React renders a login error. This violates the accepted continuity and
denied-storage contract, not optional hardening.

Required correction: initialize React settings for those legacy pages with the
bounded initiating preference, without consuming response query theme before
authentication. Regression must use actual settings/theme providers, denied
localStorage, opposite OS and deferred exchange; cover direct query/error too.
Current mocked page tests and completed-cookie prepaint tests do not cover the
transition. Source-proven; reviewer launched no integration test.

Lead accepted finding and returned it to implementer2. Agreed minimal fix reuses
existing path-scoped query/pending enum reader; cookie remains highest priority,
callback URL returned theme is ignored. Implement after final report; focused
checks + consolidated amended head. Mandatory-review step9 permits direct
source/result verification of this narrow correction without automatic repeat
review. New design/interface changes would require affected lanes.

## HaveAPI conclusion

Base `4c126e3b0ed259b2be18a241a0c4c716046eb816`; final
`439beea801df3139b7154283a171f53c68295939`; base verified as merge base,
checkout/index clean. Entire series reviewed:

1. `1046a14f2f0485f460b3918098e5bc078a3da758`: provider extension/owning contract.
2. `439beea801df3139b7154283a171f53c68295939`: docs consumer/tests/explanation.

Logical split and messages; no obsolete unmerged approaches, fixup streams,
abandoned shims, repeated dependency/channel/input/lock/generated update streams.
No migrations or transitional lineage. No release, deployment, merge or external
consumption claimed or contradicted. Independent component result: no findings;
may proceed to lead acceptance/publication/long checks, not whole-initiative
readiness or merge/deploy authorization.

Default hook empty; complete success GET/SSO+POST only; errors unchanged. Exact
single theme key/enum accepted per response while Rack owns code/state/mode and
verified redirect. Sibling API override inspected as representative consumer
only, not completed B acceptance. Docs retains strict unknown/duplicate query
rejection, pending/state validation and successful exchange; old pending shape
accepted, auth-cookie fields/purposes unchanged. Error/retry initiating theme and
bounded destination retained. Script merges only theme, preserves examples and
clears mount cookie independently of static prefix. Failure layout reuses
existing palette/translations.

Docs placement/preservation explicitly sound: README links owning oauth-theme.md;
existing documentation-ui/oauth articles explain reader/client/operator behavior,
storage, HTTPS/auth/revoke and pending-cookie rollback retry. Useful without
session; existing guidance preserved, valid relative source links. Individual
results/environment failure in session with reusable note. No fidelity gap.

Remaining gaps: full suites/performance/native browser/paired provider acceptance,
exact source0.32.0 consumer packaging/shipped docs/assets/effective Gemfile-lock-
runtime identity vs current published0.32.2. B owns actual package proof; no gem
release or package pass implied by this review.

## React/BFF conclusion

Base `e311b1c0af0f50fa4c6f6ce83c514c1a866eb042`; final
`b1f63a5eab2ffbaca239047eceddc2cc98e075d5`; base verified merge base,
checkout/index clean. One logical feature commit includes required CSP/runtime
manifest support and final root work-log pointer. No obsolete history/fixups,
unused alternatives, abandoned shims or repeated update streams. No migrations;
no transitional lineage, release/deploy/external-consumption/merge claimed.
C-1 needs correction/explicit decision before long integration; no other findings.

BFF emits handoff only after state consumption+exchange/session rotation;
invalid/array enum falls back, new/failure clears. Bounded selected.initiating,
120s host-only/Lax/Secure HTTPS; session JSON unchanged. Legacy state storage
remains required; optional storage guard waives no PKCE/state validation.
StrictMode promise reuse stays per mount. Existing record merges only selected
theme and preserves snapshot/unrelated fields; missing record distinguishes
known selected/initiating difference; pending survives failed read. Subject to
C-1 before legacy initialization.

Independent diagnostic recomputed CSP hash
`GsLiqeMVCzP8bNzzGixyR67nIkrZ+XnSTAT8QzB3MAo=`. All four policy/template changes
are exactly hash replacement; no unrelated policy change. Three locks byte-
identical. Runtime manifest includes helper. Boundary enum glue across BFF,
browser and head realms is proportionate, no general preference framework needed.

Docs placement/preservation explicitly sound: root README→existing handbook,
configuration owns cookie/settings/rollback, workflows/REQ005 interaction and
acceptance, root work log→dated entry. HaveAPI owns wire contract. Existing
instructions preserved, no private-context dependence; preparation/testing/
review/merge/deploy distinguished. Continuity prose needs C-1 correction; counts
are not browser/deployment proof. External master link depends eventual ordinary
provider integration, controlled by downstream review.

Owner scoped quick evidence credible, not rerun by reviewer: focused tests,
BFF63, type/audit/format, package/CSP17. Full suites/builds/Nix/native screenshots
and paired acceptance remain later. No production behavior certified.

## Scope and next boundary

Reviewer found scope proportional to user goal: HaveAPI14 files +444/-22 and
C34 files +737/-116 mostly feature tests/docs/bootstrap CSP. No service/framework,
SDK/endpoint/broad refactor/speculative compatibility layer. Available milestone
chronology supports progress, overlapping member clocks were not summed.

Return C-1 to owner and apply narrow-fix rule. HaveAPI clean component conclusion
unblocks publication. Completed B/E still need whole-branch final reviews; E's
actual final source graph needs explicit cross-project/history/no-migrations
conclusion, reusing unchanged upstream review evidence. No global readiness yet.
