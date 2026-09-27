---
lifecycle: active
---

# 2026-09-27-newadmin-integration

## Status

- Phase: WebUI required BFF frontend bootstrap and audit-record cleanup committed; locked-toolchain quick checks passed and independent checkpoint review is underway.
- Identity verified with `dev-session current` and both environment markers.
- Retained roster: `architect0` (design), `implementer0` (implementation),
  `reviewer0` (independent review). WebUI through W3b is committed on the
  session feature branch at `a91414d`; site configuration remains unchanged.
- Recommendation: adopt incrementally after the documented fixes; no rewrite
  is justified, and replacement of the legacy UI is not yet ready.

## Phase checklist

- [x] Verify session and read applicable workspace procedures.
- [x] Pin primary review source (`fd290b5ec1b22900e704e8cb990c5ba050af2394`).
- [x] Assess architecture, maintainability and tests.
- [x] Verify local checks and map NixOS/proxy/DNS integration.
- [x] Prepare prioritized review document and handoff.
- [x] Assess two-instance HAProxy deployment and record session/failover choices.
- [x] Record the user's single-instance, repository, VPS and domain decisions.
- [x] Inspect replacement upstream handbook and check English/Czech localization.
- [x] Prepare detailed implementation, pinned API/i18n input and deployment plan.
- [x] Commit/push workspace project registration on the session feature branch.
- [x] User adds architect, implementer and reviewer; architect assigned `design.md`.
- [x] Architect completes `design.md` before substantive code changes.
- [x] WebUI W1 repository/tooling baseline committed with locked vpsAdmin input.
- [x] WebUI W2a full catalog integrity and rendered count regression committed.
- [x] WebUI W2b1 coherent workflows, browser provisioning and archive-safe docs audit committed.
- [x] WebUI W2b2 structural debt disposition and narrow UI-string fixture classification committed.
- [x] Record lead acceptance of the exact inherited ledger and pass `ci:quick`.
- [x] W3a BFF public configuration and startup validation committed; 46 BFF tests and quick gate pass.
- [x] W3b required frontend bootstrap and focused compatibility tests committed.
- [x] Locked-toolchain quick gate and production build on the rewritten WebUI head.
- [ ] Independent review of the committed WebUI branch checkpoint (assigned to reviewer0).
- [ ] Complete remaining verification debt: scoped ESLint/format and tooling/E2E type coverage, reassess the jsdom patch, and controlled desktop/mobile browser diagnosis.
- [ ] Application/configuration implementation, independent review and builds.
- [ ] Explicit default-branch integration and user-run deployment.

## Next actions

Architect0 prepared `design.md`; implementer0 completed the WebUI source/tooling,
verification and BFF bootstrap changes through `a91414d`. The branch history
was consolidated without changing its final tree or the W1 source revision
used by the structural ledger. The W6 package/module design is recorded in
`design.md`. Next are independent review, W4 correctness, W5 localization, W6
NixOS packaging and W7 site configuration. Keep the map call unchanged. The
missing external spec is replaced, not a recovery task. Agents may build the
resulting machines; the user performs deployment.

The lead confirmed the canonical origin still advertises no branches, rewrote
only the unpublished feature history, and folded the source-ledger acceptance
follow-up into its parent. The WebUI head is `a91414d`; its final tree
`2a7653a711186a1e587c268d44768de0be11fbfe` is identical to the
pre-rewrite tree. The ledger's baseline source commit `2fad90b` is unchanged.
On this head, the normal Nix shell passed `npm run ci:quick` and `npm run build`.
Focused W3b tests passed in the implementer's cached Node 24 shell; independent
review, browser integration and NixOS builds have not run.

Implementer0 committed durable audit-record wording cleanup as `1949f28`,
limited to `WORK_LOG.md`, `docs/design/VERIFICATION.md` and the ledger's prose
fields. Machine-significant fields for all 43 exceptions compare equal to its
parent. Focused structural/design audits and tests passed; reviewer0 is now
assigned a high-risk general, architecture, scope and compatibility/security
review of base `e7ce3d73` through `1949f28`. No branch has been pushed or
deployed.

## Documentation

- [Detailed implementation plan](implementation-plan.md).
- [Architecture and verification brief](design.md).
- [Operator deployment and secrets runbook](deployment-runbook.md).
- [English/Czech assessment](translation-review.md).
- [Review and NixOS integration proposal](review.md).
- [Verification evidence](verification.md).
- [Initial browser failure inventory](browser-failures.md).
- [Reusable browser setup lesson](../../notes/clankerdev/2026-09-27-local-browser-verification.md).
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-27-newadmin-integration/

## Repositories

- Detached review worktree: `worktrees/2026-09-27-newadmin-integration/clankerdev`.
  Canonical local bare clone: `repos/clankerdev.git`; origin is the user-selected
  `git@github.com:Kerrycek/clankerdev.git`. No feature branch or push.
- Existing vpsAdmin and configuration bare clones fetched for read-only reference.
  Reference heads: vpsAdmin `7045c81b3a5be312eac0d41e8a44f783340abb9f`;
  configuration `1e8dae229fbe4201b5e1f110721f0f63c4b46944`.
- Canonical new clone: `repos/vpsadmin-webui.git`, origin
  `git@github.com:vpsfreecz/vpsadmin-webui.git` (no advertised branches at setup).
  `upstream` retains `git@github.com:Kerrycek/clankerdev.git`. Detached planning
  worktree `worktrees/2026-09-27-newadmin-integration/vpsadmin-webui` uses
  `49c6a51d0b32c4a6d5dd1df426e0bac1d8066115`. It was promoted to the
  `2026-09-27-newadmin-integration` feature branch for implementation. Canonical
  origin has no default branch yet; no default-branch integration is authorized.
  Before edits, lead verified/fetched upstream main at
  `e7ce3d73e799fc60e5933fe23bdb3a979eb4d6b9` and fast-forwarded the clean
  feature branch. The new upstream revision adds the self-contained
  `UI_REDESIGN.md` pointer and doc/audit updates; it removes the old missing-spec
  issue without changing the decision to use the design handbook.
  W1 commit `2fad90b` adds the pinned `vpsadmin` input, Node 24 dev shell,
  localization instruction route, canonical repository identity and source
  handbook/work-log updates. W2 repairs culminate in `c639b32`; W3a public
  runtime configuration/startup validation is `9e2f1f5`; W3b required frontend
  bootstrap is `a91414d`. No site configuration is changed yet.
- Configuration feature worktree:
  `worktrees/2026-09-27-newadmin-integration/vpsfree-cz-configuration`, branch
  `2026-09-27-newadmin-integration`, base `1e8dae229fbe4201b5e1f110721f0f63c4b46944`.
  `dev-session worktree add` created and registered it, then returned nonzero
  because the checkout hook needs gems from its Nix development shell. The
  branch and worktree are clean; future commands must use the declared shell.
- Workspace feature worktree: `worktrees/2026-09-27-newadmin-integration/workspace`;
  branch `2026-09-27-newadmin-integration`, base
  `78585882fc8079bfc11c660f718f9b29931e0f4a`, commit `f12ecd1a`, pushed to origin.
  Only `docs/agent-instructions/projects.md` changed. No declared hook framework
  exists in this workspace; existing instruction tests passed. No tracked Actions
  workflow exists here. Independent review/integration wait for the upcoming
  team. No workspace master integration approval has been given.

## Initial review results (fd290b5e)

- Production Vite build passed; TypeScript and initial lint/i18n/CSP checks passed.
- `ci:check` fails the repository's structural budget (63 files >500 lines vs 53,
  plus per-file cast/growth regressions). This gate is absent from checked CI.
- First `ci:pr` stopped after 130/131 script tests passed because local Chromium
  was missing. The remaining script test passed after browser provisioning.
- All 1,514 Vitest tests and all 36 BFF tests passed. Individually run component,
  docs, overlay, lookup, API-barrel and mutation audits passed. UI-string audit
  reports three test-fixture strings, not missing product translations.
- Desktop PR smoke: 349 passed / 29 failed with the default 32 workers; its
  chained mobile stage was not reached. All five representative failed tests
  passed in a single-worker follow-up. Timing/load sensitivity is supported,
  but the causes of all 29 failures remain unresolved; 24 were not rerun.
- Source-confirmed findings include automatic external registration-address
  geocoding, missing canonical spec, capped network lists and unbounded bootstrap.
- No `.nix` files exist in the UI repository. Report proposes upstream packages/
  module and site-owned proxy, both DNS views, OAuth, monitoring and rollback.
- Applied dev-session-documentation, dev-session-handoff and dev-session-monitor.
  Verification watchers use installed catalog `d540572c722500ac68c240a6f740058484b4a7ea059c9e96ebf674356a92f797`,
  utility `verification_watcher`, GPT-6 Luna/low, one fresh agent per batch.
- Mandatory change review is reserved for subsequent committed implementation;
  this turn reviews existing upstream code and writes investigation records only.
- All three verification watchers completed; no test/build command remains
  running. The detached application worktree is clean. Detailed commands, local
  environment differences and limits are preserved in `verification.md`.

## Material risks and limits

NixOS support and site configuration are not implemented. CI gaps, browser-suite
failures, capped network lists, bootstrap handling and localization defects need
the planned fixes. No live API parity, deployed-version inventory, production
login, NixOS integration or deployment has been certified. The user selected
keeping the map call and a single instance; do not reinstate map remediation or
HA as gates. The new handbook resolves the unavailable external-spec dependency.

## Planning follow-up results (49c6a51d)

- Canonical docs check passed: 16 documents, 66 requirements, 256 routes and
  63 API modules. Initial attempt lacked TypeScript; `npm ci` installed the
  declared dependencies in 8 seconds, then the check passed.
- `audit:i18n` passed with 4,567 keys, but source inspection shows it ignores
  double-quoted keys. Full literal scan: 8,164 unique keys per language, one
  conflicting duplicate per language, no differing key or placeholder sets.
  Found a wrong UI interpolation argument and a stale login terminology test;
  further confirmed terminology/prose findings are in `translation-review.md`.
- Workspace instruction checks passed: 6 tests / 84 assertions. No machine build
  has run for the future configuration; no candidate exists to build yet.
- New requirement: pin vpsAdmin as a WebUI flake input; resolve i18n guidance
  from that source. Site `vpsadminWebui.inputs.vpsadmin.follows` must reference
  `vpsadminServices`, which backs channel `vpsadmin`. The guide's Git blob is
  identical at the inspected service pin and vpsAdmin reference head.

## Architecture decisions for implementation

- Accepted architect0's additive `/config.json` bootstrap proposal. Preserve
  `/config.js` and `/session.json` compatibility; update routing and operator
  checks accordingly. Bound fetches and reject malformed public/session data.
- W3b uses an explicit BFF production build mode; standalone production builds
  require an explicit legacy selection. The BFF session response is authoritative.
  A valid anonymous response clears stored standalone credentials and
  impersonation state. An impersonation token created in BFF mode is usable after
  reload only while its recorded noncredential BFF session fingerprint matches
  the current authenticated session; a fresh login or logout cannot resurrect a
  prior operator's impersonation. Standalone mode retains its existing behavior.
- W3b must use the API token-provider header for bound impersonation; the
  BFF's configured OAuth header is not valid for that provider. BFF logout
  does not revoke a separately issued API impersonation token, and an already
  running tab may retain it until revalidation. Do not claim instantaneous
  cross-tab revocation from the bootstrap fix. Treat this as a preview-use
  limitation and design a follow-up before full cutover readiness.
- For collection pagination, display explicit incomplete state where the pinned
  API's ordering/cursor does not prove lossless traversal; do not claim complete
  totals or silently page by an unsafe cursor.
- Architect0's pinned HaveAPI/API inspection established that `from_id` alone
  does not order results. Lead accepts W4's bounded client behavior and initial
  250-row/20-request/5,000-row, 10-second request/30-second overall budgets:
  traverse only proven ascending host-IP and effective-admin IP routes;
  identify member/interface/history/accounting and other unproven collections
  as partial and gate controls that require complete membership. No backend
  API/schema change is in this tranche; see the matrix and tests in `design.md`.
- The new host needs the `os-staging` channel because its container profile
  resolves `vpsadminos`, even though it runs no local vpsAdmin service.
- Lead accepted architect0's W6 account separation: the new BFF runs as
  `vpsadmin-webui-bff`, because the pinned legacy PHP module already uses
  `vpsadmin-webui`. The service name, Nix option namespace, cookie, secret path
  and `StateDirectory=vpsadmin-webui` remain as planned. No account migration is
  needed because the new service has never been deployed.
- No new default branch, production deployment or existing-interface cutover
  is authorized. GitHub identifies the first pushed branch of an empty repo as
  its default branch, so even a feature-branch push to the empty canonical origin
  would cross the integration gate. Use local flake overrides for candidate
  builds until the user explicitly directs initial default-branch publication.
  Remote-lock site builds then follow the published WebUI revision.
- Read the canonical [vpsAdmin WebUI KB change workflow](https://github.com/vpsfreecz/vpsfree-kb-contracts/blob/master/docs/webui-change-workflow.md)
  for visible-copy impact.
  Its current contract and captures pin the legacy `vpsadmin` WebUI, so they do
  not certify new React preview labels or screenshots. W3b's early failure-copy
  change has no existing documented semantic action identified here. W4/W5
  visible controls need a separate binding/impact assessment before claiming
  documentation parity. No KB staging or production write is authorized or run.
- W1 quick checks reported by implementer: cached Node 24.19.0 `env:check`,
  lint, typecheck, production build and active-docs audit; Nix parse/format,
  lock metadata and whitespace checks. In the lead's normal environment,
  `nix eval` resolved the locked input revision to
  `a65a4dfeb92a59df4a80a737a20bcbf8558793ff` and its store path;
  `nix develop --command node --version` returned v24.21.0; and
  `nix develop --command npm run audit:design-docs` passed (17 documents,
  66 requirements, 256 routes, 63 API modules). These validate source setup,
  not package builds or the new service.
- W2a commit `3f63bbd` replaces the old regex audit with a TypeScript AST
  validator across literal catalogs, detects duplicate keys and unsupported
  constructs, checks en/cs keys/placeholders/plural groups, removes the
  conflicting duplicate and fixes the rendered IP-count argument. Implementer
  reported focused audit, fixture tests, rendered en/cs test and typecheck
  passing. The lead's normal-environment `nix develop --command npm run
  audit:i18n` also passed, reporting 8,164 keys in each language.
- W2b1 commit `a821c8c` adds deterministic source enumeration for the design
  audit, a distinct browser-script bucket, locked Node/npm/Playwright checks,
  and explicit production-build and independent desktop/mobile CI jobs. The
  implementer's fixture/YAML checks passed. In the lead's normal environment,
  `nix develop --command npm run env:locked` passed with Node 24.21.0/npm
  11.19.0 and `nix develop --command npm run audit:design-docs` passed with
  17 documents, 66 requirements, 256 routes and 63 API modules. `ci:quick`
  remains red on inherited structural debt and three UI-string test-fixture
  strings; W2b2 owns those exact findings.
- Architect0's W2b addendum inventories the inherited structural debt at W1:
  892 casts, 63 files over 500 lines and seven over 1,000, with 44 per-file
  violations. The lead accepts a separately reviewed, exact-path/rule/content-
  hash exception ledger for inherited debt only, provided it preserves the
  historical baseline, fails on stale or changed entries and exposes raw
  failures separately. No blanket baseline rewrite or silent suppression is
  accepted. W2b must make CI checks coherent and the design audit safe for
  `.git`-less Nix/archive sources, then supply focused quick-check evidence.
- W2b2 produces a complete machine-readable inventory,
  rejects changed/resolved/stale exceptions, removes three small violations,
  and narrows the UI-string fixture classification. The draft ledger has 43
  exceptions across 41 files. Lead independently compared every listed SHA-256
  with the corresponding file in W1 commit `2fad90b`; all match, and the
  historical baseline is unchanged. Lead accepts this exact inherited ledger
  subject to its source-hash/removal gates. The normal-environment `ci:quick`
  run on the draft W2b2 commit reached the structural
  audit, then failed because the ledger's acceptance marker was still pending
  (44 raw violations, 43 proposed, zero accepted). The accepted ledger and
  rationale correction were consolidated into `c639b32`. The lead's
  `nix develop --command npm run ci:quick` passed after acceptance; its final
  file tree is unchanged by the later history rewrite. Structural output
  records 44 raw violations, 43 exact accepted exceptions, zero unaccepted or
  invalid entries and zero aggregate failures. This does not replace later
  full unit/browser/package and independent review evidence.

## Selected values and remaining operator inputs

- One instance, repo `vpsfreecz/vpsadmin-webui`, public `newadmin.vpsfree.cz`.
- VPS 30431, private 172.16.9.170, hostname `vpsadmin-webui1.int.vpsfree.cz`,
  machine `cz.vpsfree/vpsadmin/int.vpsadmin-webui1`.
- Proposed secret file `/private/vpsadmin-webui.env`: OAuth client ID/secret and
  separate stable session-signing secret. The user supplies these privately.
- Before activation: confirm installed VPS architecture/network/stateVersion,
  effective deployed API revision and OAuth policy/client values. License intent
  still needs confirmation. These do not block the prepared plan.

## Cleanup

Session remains open. Preserve unrelated workspace/index changes. No lifecycle
cleanup is authorized or scheduled.
