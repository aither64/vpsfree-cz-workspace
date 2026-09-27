# Review verification evidence

Target: `Kerrycek/clankerdev` commit
`fd290b5ec1b22900e704e8cb990c5ba050af2394`, detached checkout under this session's
worktree group. No tracked application files changed.

## Environment and first batch

No repository Nix environment is defined. Checks used
`nix shell nixpkgs#nodejs_22 -c bash`, resolving Node `v22.23.2` and npm `10.9.8`.
The upstream CI pins npm `9.9.4`; these local checks are not an exact reproduction
of that runner image. The source revision and lockfiles were unchanged.

| Command | Result | Duration / evidence |
| --- | --- | --- |
| `npm ci --include=dev --no-audit --no-fund` | Pass | 10 seconds |
| `npm ci --omit=dev --no-audit --no-fund --prefix bff` | Pass | 2 seconds |
| `npm run ci:pr` | Incomplete suite, command exit 1 | 74 seconds; lint, i18n parity, CSP hash and TypeScript passed; 130/131 script tests passed; the remaining test could not launch absent Chromium. BFF/Vitest were not reached by this command. |
| `npm run build` | Pass | 20 seconds; Vite build, warning for locale chunks above 500 kB |
| `npm run ci:check` | Fail, exit 1 | 6 seconds; stops at structural audit before its remaining checks |

`ci:check` failure summary:

- Files above 500 lines: 63 versus the recorded limit of 53.
- New casts in `src/lib/api/systemConfig.test.ts`; increased casts in
  `payments.test.ts` and `ResourcePackageDetailPage.tsx`.
- Eight listed components crossed 500 lines; `LocationsPage.tsx` crossed 1,000.
- Previously large components grew, including `VpsLayout.tsx` and
  `VpsNetworkPage.tsx`.
- Current audit totals: 892 `as any`, 63 files above 500 lines, seven above 1,000.
  The totals include test casts, unlike the source-only count in the review.

The missing-browser test is
`scripts/live-vps-certification-browser-proxy.test.mjs:35`. It uses real Chromium
against loopback HTTP stubs and is safe to run locally; it does not execute the
live VPS certification operation. Its source accepts a system-browser override.
The second batch explicitly provisioned Chromium and reran only this failed
script test, then ran the BFF/Vitest/audits not reached by the earlier aggregate
commands and the mocked PR browser smoke.

First-batch full logs and command exit records:
`/tmp/newadmin-review-checks/{versions.txt,status.tsv,npm-ci.log,bff-npm-ci.log,ci-pr.log,build.log,ci-check.log}`.
These temporary logs are diagnostic detail; this document preserves the useful
results independently of their retention.

## Remaining verification

The second batch used `nix shell nixpkgs#nodejs_22 nixpkgs#chromium -c bash` with
`E2E_CHROMIUM_EXECUTABLE_PATH` set to the Nix Chromium binary and
`E2E_RECORD_ARTIFACTS=0`. Browser error-context files were still generated; some
specifications explicitly captured screenshots. These used mock data.

| Command | Result |
| --- | --- |
| `node --test scripts/live-vps-certification-browser-proxy.test.mjs` | Pass: 1/1; confirms the initial script-test failure was missing browser provisioning |
| `npm run test:bff` | Pass: 36/36 |
| `npm test` | Pass: 270 files, 1,514 tests; about 31 seconds |
| `npm run audit:component-contracts` | Pass |
| `npm run audit:active-docs` | Pass: 1,321 files scanned, despite missing canonical-spec target; it checks terminology rather than link existence |
| `npm run audit:overlays` | Pass |
| `npm run audit:lookup-primitives` | Pass |
| `npm run audit:api-barrel-imports` | Pass |
| `npm run audit:mutations:check` | Pass: 219 calls, no warnings; source audit, not live mutation execution |
| `npm run audit:ui-strings:check` | Fail: three strings, all in test fixtures |
| `npm run e2e:pr` | Exit 1: desktop Chromium stage, 349 passed / 29 failed, 378 tests using the default 32 workers, 6.5 minutes. The chained mobile stage did not run. |

UI-string findings are `MainContentAccessibility.test.tsx:11` (label) and
`VpsLookupInput.test.tsx:287,295` (placeholder/text). These do not demonstrate
missing product translations. Exclude/annotate test fixtures appropriately in the
audit before making it an enforced release gate.

Full logs and individual `.exit` files are in
`/tmp/newadmin-review-remaining/`. The [initial browser failure inventory](browser-failures.md)
preserves every failed test name and assertion; full error contexts remain in
the checkout's ignored `e2e/test-results/` directory.

### Browser failure investigation

The lead inspected failure logs, test source and captured page trees before
selecting further verification. Early failures such as cluster DNS resolvers and
VPS map mode showed a rendered shell with a lazy route still at `Loading…`.
Other failures reached data-rendered pages but asserted incorrect pagination or
Back/Forward state. The first run's 32-worker default made concurrency/load a
plausible confounding factor; it was not taken as an established root cause.

Five representative failed tests were then run once with `--workers=1`, retaining
traces on failure and using a separate output directory. **All five passed:**

- `e2e/specs/admin/cluster_dns_resolvers_smoke.spec.ts:36`
- `e2e/specs/admin/vps_map_mode.spec.ts:24`
- `e2e/specs/app/dns_zones_keyset_pagination.spec.ts:68`
- `e2e/specs/app/user_namespace_filter_contract.spec.ts:271`
- `e2e/specs/app/user_namespace_filter_contract.spec.ts:450`

Command inside the Node/Chromium Nix shell, from the application checkout:

```sh
E2E_START_SERVER=1 E2E_RECORD_ARTIFACTS=0 \
  E2E_CHROMIUM_EXECUTABLE_PATH="$(command -v chromium)" \
  node scripts/playwright.mjs test \
  e2e/specs/admin/cluster_dns_resolvers_smoke.spec.ts:36 \
  e2e/specs/admin/vps_map_mode.spec.ts:24 \
  e2e/specs/app/dns_zones_keyset_pagination.spec.ts:68 \
  e2e/specs/app/user_namespace_filter_contract.spec.ts:271 \
  e2e/specs/app/user_namespace_filter_contract.spec.ts:450 \
  --project=chromium --workers=1 --trace=retain-on-failure --reporter=line \
  --output=/tmp/newadmin-review-focused/results
```

Tools: Chromium `153.0.8010.52`, Node `v22.23.2`, npm `10.9.8`. Exit 0,
42 seconds elapsed (39.4 seconds reported by Playwright). Evidence:
`/tmp/newadmin-review-focused/run.log`, `status.txt` and results metadata.
No failure trace was produced because all selected tests passed.

This supports a concurrency/load-sensitive test or application timing problem.
It does **not** prove that all 29 failures have that cause, make the full PR
suite green, or validate the skipped mobile stage. Before adoption, bound worker
counts, gather failing request/console/timing evidence and run the agreed release
suite in a controlled environment. Do not interpret the initial run as 29 proven
product defects, or accept the focused pass as a substitute for that work.

## Limits

No npm advisory audit result is claimed: installs intentionally disabled audit,
and no production-dependency vulnerability inventory was performed. No production
login, live mutations, DNS updates, server changes, Nix package build, NixOS VM
integration, deployed-version inventory or full browser suite was performed.
A build and mocked tests do not establish feature parity or deployment readiness.

All three verification watchers completed their owned operations; no test/build
command remains running. The application checkout is clean after verification.

This was an assessment of existing upstream code, not independent review of new
implementation commits. Apply mandatory change review to the subsequent fixes
and integration branches before their long integration tests.

## Implementation-planning follow-up

Source `49c6a51d0b32c4a6d5dd1df426e0bac1d8066115` is a separate clean detached
checkout backed by the new canonical bare clone. The first source revision's
unit/build/browser results above do not certify it.

- `nix shell nixpkgs#nodejs_22 -c node scripts/audit-i18n.mjs --fail`: pass,
  4,567 recognized keys per language. Its single-quote-only regex is incomplete.
- Both-quote literal inventory of all `src/i18n/locales/{en,cs}/**/*.ts`:
  8,165 definitions / 8,164 unique keys in each language, matching key and
  interpolation-variable sets, one conflicting duplicate per language.
  This lexical scan is supporting evidence, not a full parser or prose review.
- `audit-design-docs.mjs` initially reached inventory generation but failed for
  absent `typescript`. After `npm ci --include=dev --no-audit --no-fund` (8 seconds),
  it passed: 16 documents, 66 requirements, 256 routes and 63 API modules. No
  generated inventory write was requested. Node was 22.23.2.
- `nix shell nixpkgs#ruby -c ruby test/agent_instructions_test.rb` in the workspace
  feature checkout: 6 tests, 84 assertions, no failures/errors/skips.
- Application checkouts remained clean. No machine configuration build, NixOS VM
  test, production activation or OAuth client creation occurred during planning.
- The workspace project-map commit `f12ecd1a` has only four added lines. It is
  pushed on the session feature branch and awaits the upcoming team's independent
  review and explicit integration direction; it is not claimed ready/merged.

## Implementation W1 source and toolchain checkpoint

The WebUI session branch was fast-forwarded to freshly checked upstream
`e7ce3d73e799fc60e5933fe23bdb3a979eb4d6b9` before W1. Implementer0 committed
the repository/toolchain/instruction baseline as `2fad90b`. Its WORK_LOG records
passes for `env:check`, lint, typecheck, production build and active-docs audit
on cached Node 24.19.0, plus Nix syntax/format, lock metadata and whitespace
checks. Its restricted shell could not reach the Nix daemon or run the stricter
design-doc audit's Git subprocess; those are environment gaps, not skipped gates.

From the lead's normal environment on `2fad90b`:

- `nix eval --raw --impure --expr '(builtins.getFlake (toString ./.)).inputs.vpsadmin.rev'`
  returned `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`.
- Evaluating the input's `outPath` returned
  `/nix/store/030czw9xwvihmw4l24p97d5r2xxd71vi-source`, containing the
  intended i18n guide and localization procedure.
- `nix develop --command node --version` returned `v24.21.0` after binary-cache
  substitution; no kernel build was started.
- `nix develop --command npm run audit:design-docs` passed: 17 documents,
  66 unique requirements, 256 routes and 63 API modules.

No Nix frontend/BFF package or machine configuration exists at this W1 checkpoint.
The earlier `49c6a51d` or `fd290b5e` test totals do not certify the current
candidate, and W1 quick checks do not certify runtime integration.

## W2a and W2b1 implementation checks

W2a commit `3f63bbd` adds a TypeScript parser-based catalog audit and rendered
English/Czech IP-count regression. Its focused fixtures and typecheck passed in
the implementer's cached Node 24 shell. The lead's normal-environment
`nix develop --command npm run audit:i18n` passed and counted 8,164 keys in each
language, including previously skipped double-quoted keys.

W2b1 commit `a821c8c` makes the design audit source-form independent, separates
the Chromium script test, aligns locked tool versions and prepares CI jobs.
Implementer-reported archive/checkout fixtures, wrapper/version/bucket tests
and YAML parsing passed. From the lead's normal Nix environment on that commit:

- `nix develop --command npm run env:locked` passed with Node 24.21.0/npm
  11.19.0. This closes the implementer's sandbox-only inability to enter the
  Nix development shell.
- `nix develop --command npm run audit:design-docs` passed: 17 documents,
  66 requirements, 256 routes and 63 API modules.

`ci:quick` is not yet green: the inherited structural budget reports 892 casts
and 63 files over 500 lines against an unchanged 1,156/53 baseline, plus
per-file violations; the UI-string audit also sees three strings in two test
fixtures. W2b2 owns the exact debt ledger and narrow fixture classification.
The production build job, browser script, desktop/mobile PR suites and GitHub CI
are prepared but not yet executed on the current candidate. The canonical new
repository is empty, so no remote CI run is possible without the separately
required initial publication decision.

W2b2 was consolidated as `c639b32`, including the lead's acceptance of the
exact inherited debt ledger. The lead compared all 43
exception hashes against the corresponding files at W1 commit `2fad90b`; all
matched, across 41 paths, with no duplicate path/rule entries. The historical
baseline remains unchanged. The first normal-environment `ci:quick` stopped at
the intentional pending-acceptance marker, before later audits ran. After the
marker was committed, `nix develop --command npm run ci:quick` passed end to
end on the equivalent pre-rewrite file tree in about 52 seconds. Its structural report retains 44 raw
violations, accepts the 43 exact inherited per-file entries, and has zero
unaccepted/invalid entries or aggregate failures. Lint, 8,164-key catalog audit,
design/CSP/architecture audits, UI-string/mutation audits and typecheck passed.
No long browser or package test is inferred from this quick gate.

## W3a committed BFF verification

Implementer0 committed BFF production configuration validation and the public
`/config.json` contract as `9e2f1f575a33b15780218a16519ba0383c339a38`
after the message-only history rewrite.
The feature worktree was clean at this head. From the lead's normal Nix
environment on that exact commit:

- `nix develop --command npm run test:bff`: 46/46 passed, including JSON/JS
  public-config parity, fail-closed production settings, provider-error
  redaction, OAuth state and refresh/logout concurrency.
- `nix develop --command npm run ci:quick`: passed end to end with locked Node
  24.21.0/npm 11.19.0, 8,164 keys in each catalog, 43 accepted inherited
  structural exceptions and no unaccepted/invalid or aggregate failures;
  lint, documentation, source audits and TypeScript checks also passed.

W3a has not undergone independent review or a long browser/NixOS integration
test. The frontend bootstrap is recorded below; W4/W5 correctness/localization
and W6/W7 NixOS and site configuration remain pending. These quick checks do
not certify the proposed production deployment.

## W3b committed frontend bootstrap

Implementer0 committed the required production BFF bootstrap as
`a91414ded48332b23e1fafffae01d50024de0335`. Its focused Vitest selection
passed 80 tests across six files; typecheck, lint (1,633 files), the i18n,
design, structural, UI-string and mutation audits passed in the implementer's
cached Node 24 shell. The structural report kept 44 raw violations, 43 accepted
and zero unaccepted or invalid ledger entries. No browser or integration suite
was run. The lead rewrote only local unpublished commit messages and folded the
acceptance follow-up into its parent; the final tree remained
`2a7653a711186a1e587c268d44768de0be11fbfe` across the rewrite. The pinned
W1 source revision stayed `2fad90b0d3cdc629d81b4d2ed3656e67b17f4fa3`.
Normal Nix-shell checks on the rewritten head passed:

- `nix develop --command npm run ci:quick`: exit 0 in 90 seconds; all audits
  and TypeScript checks completed. Full log:
  `/tmp/newadmin-w3b-locked-checks/ci-quick.log`.
- `nix develop --command npm run build`: exit 0 in 35 seconds, with the Vite
  bundle built in 19.97 seconds. A non-failing large-chunk warning remains.
  Full log: `/tmp/newadmin-w3b-locked-checks/build.log`.

The fresh Luna/low watcher reported no unexpected kernel build and no remaining
operation. The tracked WebUI worktree was clean at the checked head.

The subsequent prose-only commit `1949f28689e944554a5dee970ce281a7181b1b73`
replaces internal work-package labels in the work log, verification guide and
structural ledger rationales. The lead compared the JSON before and after this
commit with prose fields removed: the remaining machine-significant structure
is identical for all 43 exceptions. Implementer0's cached Node 24.19 checks
passed: `audit:structural` (44 raw, 43 accepted, zero unaccepted/invalid or
aggregate failures), `audit:design-docs` (17 docs, 67 requirements, 256 routes,
63 API modules), focused structural/design script test files, and diff check.
The normal Nix quick/build result above applies to the parent `a91414d`, whose
application files are unchanged by this commit. No long integration test is
inferred from these results.
