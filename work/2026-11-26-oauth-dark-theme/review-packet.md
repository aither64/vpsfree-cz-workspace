# OAuth appearance — completed component final review

Review owner: reviewer0, retained gpt-6.1-sol / xhigh, read-only, session verified.
Risk: high (OAuth response handling, callback/pending state, settings persistence,
client/server extension and mixed-version behavior). Apply general,
architecture/repetition, scope/proportionality and risk/compatibility lanes from
mandatory-change-review. Read that skill and each selected reference in full.

## Scope and acceptance

User requested OAuth light/dark/auto compact controls, status-like dark palette,
reusable dark logo, declarative production logos and a vpsAdmin default, React
and HaveAPI docs theme preservation on entry/return, no PHP integration. User
accepted implementation with explicit removal of core.logo_url fallback.
[Design](design.md) is the accepted brief; [plan](plan.md)/[state](state.md) retain
scope/phase/approvals. No merge, deploy or package release is authorized.

This final review is of COMPLETE HaveAPI A+D and React/BFF C repository
branches, not partial commits or advisory early review. Their intended changes
are committed and quick checks pass. Publishing either branch triggers long
CI, so final component review must precede publication. B (API) needs the exact
reachable HaveAPI source to finish its packaging pin; E (configuration) needs
reachable final B/C heads for real confctl pins. Those downstream completed
branches receive their own final reviews, with E's final cross-project graph
assessment reusing unchanged upstream reviews. No readiness for the full
initiative is claimed until every final branch/head is covered.

## Reviewed ranges and evidence

| Repository / worktree | Base | Final head | Series |
| --- | --- | --- | --- |
| haveapi at worktrees/2026-11-26-oauth-dark-theme/haveapi | 4c126e3b0ed259b2be18a241a0c4c716046eb816 | 439beea801df3139b7154283a171f53c68295939 | 1046a14f2f0485f460b3918098e5bc078a3da758 provider+contract; 439beea801df3139b7154283a171f53c68295939 docs consumer+tests/docs |
| vpsadmin-webui at worktrees/2026-11-26-oauth-dark-theme/vpsadmin-webui | e311b1c0af0f50fa4c6f6ce83c514c1a866eb042 | b1f63a5eab2ffbaca239047eceddc2cc98e075d5 | b1f63a5eab2ffbaca239047eceddc2cc98e075d5 one logical feature commit with inseparable CSP/runtime-manifest support |

Inspect each entire `git log BASE..HEAD` and `git diff BASE..HEAD`, not only
latest commit. Owner inventories: [HaveAPI evidence](haveapi-evidence.md) and
[C evidence](C-evidence.md). They own exact files, commands/results, source/lock
identities, docs routing and remaining checks. Both ranges have no migrations,
no obsolete alternate approach, no repeated dependency/pin/generated stream,
no release/deployment/external consumption. Check these claims independently.

HaveAPI changes the Config success-response extension and same-source docs
consumer, keeping only explicit bounded theme extra fields. Its two commits
separate reusable provider contract from docs adoption. Current actual source
VERSION/runtime are 0.32.0; no version bump or gem publication. API currently
packages published0.32.2 and B is explicitly preparing exact final source0.32.0
using existing source-gem machinery with honest effective Gemfile/runtime.
Same-source asset/docs packaging and actual consumer assembly remain B-owned
post-review evidence, not a claimed HaveAPI package pass here.

C changes entry/retry URLs, validated BFF+legacy return, selected+initiating
handoff, prepaint/settings merge, optional storage guards and tests/docs. Required
bootstrap CSP hashes and new BFF helper runtime allowlist accompany the feature.
No SDK/dependency lock/API declaration or session.json shape change is intended.
Inspect the initial-vs-selected distinction and no-record settings behavior.

## Interfaces, consumers and limits

Owning theme contract: HaveAPI doc/en/oauth-theme.md and Config hook
`authorization_response_params(sinatra_params:, oauth2_request:, auth_result:)`.
Consumers: same-source HaveAPI docs, vpsAdmin OAuth override in B (sibling
worktree is representative in-progress context only), C BFF+legacy browser.
Existing subclasses inherit empty result. Actual C paths/imports/manifests and
B packaging must define discovered consumers; do not rely only on this list.

Request preference is light|dark|auto, separately theme_return=1. Only success
returns chosen theme; clients consume it after normal state + exchange
validation. Error/cancel/replay retains initiating theme. Auto remains a mode.
Never alter OAuth state, redirect URI validation, PKCE, CSRF, scopes or token
fields. Old clients receive no extra callback without opt-in; new client/old
provider retains initial preference. HaveAPI docs accepts old pending shapes;
rollback may require retry of a new in-flight pending cookie. React BFF/session
JSON remains strict and unchanged; handoff has only selected+initiating enums,
120s, host-only/Secure HTTPS/Lax, no auth authority. Failed callbacks cannot
apply returned theme. Storage denial must preserve appearance without weakening
legacy state-storage requirements. Check all of these against source.

Non-goals: PHP theme interconnection, new consent UI, generic preference service,
shared-domain cookies, extra endpoint, SDK/schema generation, new framework,
production access/deployment and new release. Keep review proportional; defects
within supported paths remain actionable.

## Verification and documentation

Both owners supply exact quick checks and known failures/corrections. HaveAPI
focused provider/docs combined 128 examples pass; final D105 pass, JS controls
and touched RuboCop/hooks pass. C latest focused tests, BFF63, CSP/package17 and
all applicable quick type/audit/format checks pass; detailed evidence identifies
overlapping reruns accurately. Long full suites, native browser/screenshots,
packages and real paired provider/client flow remain after review. No production
or deployed acceptance is claimed. Required later checks stay owner work.

Main-agent writing skill passes completed on affected EN prose and diagnostics;
no C locale keys changed. HaveAPI wrapper reuses existing translations. Article
contract lives in HaveAPI; downstream explanation links to it. Relevant docs
routing/fidelity inventory is in owner evidence. Inspect discoverability,
placement, compatibility/recovery fidelity and prepared-vs-tested claims.

## Required report

Write review-component.md in this session and report to lead. Give findings by
severity with source/commit references and concrete consequence; explicit
whole-branch history/no-migrations/repeated-stream and documentation placement
conclusions for each range. State actual saved model/effort, reviewed heads,
lanes, residual gaps and whether changes remain within user scope. Do not edit
application source, run long tests, publish, deploy or spawn nested reviewers.
Return missing evidence/gaps rather than reconstructing author evidence.
