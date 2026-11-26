# C: React/BFF OAuth theme integration

Owner: implementer2. Final accepted/published source is
`d5aea5ffe1c6171ff4f4e887531d3bcd99538444`, PR335. Whole-branch and affected
review conclusions are accepted; all four final-head CI workflows succeeded.
Standalone immutable packages and the E-composed Node24.22.3 installed-package
check passed. The existing registered fixture now consumes the exact composed
frontend/BFF; source/served-file/startup/health proof is terminal and accepted
for handoff. No production deployment, default integration or release occurred.

Native final-d5 evidence currently covers both desktop mode returns, all three
mobile mode returns, denied optional localStorage, automatic OS changes, and
cancellation. The mobile token-failure attempt did not inject an invalid code:
Playwright interception of the redirected callback missed the first URL in the
redirect chain, so the genuine code succeeded. This is a fixture-only gap. The
corrected token-only runner passed on the actual composed fixture: parent35701,
exit0/11s, two captures, actual provider token rejection400, strict unauthenticated
session and no handoff. Site6, D docs6 and B provider-only coverage follow
sequentially; B now owns only the guarded cosmetic site-branding reload.
Session and registered services stay open. Details and exact next argv are in
[browser preparation](C-browser-preparation.md).

B supplied terminal site-ready receipt `browser-fixture/b-site-branding-result.json`:
cosmetic-only branding JSON switched to the two local HTTPS PNG URLs, mode600,
SHA-256 `02aca70a38f2b8ee66b2d2d69a8deec054c499052094ea8e1481851f33837664`.
Exact provider PID1566923/start230044330/argv remained unchanged around one guarded
SIGUSR1; anonymous TLS API7.0/200 and both PNG hashes passed. No user/client/SSO/
DB/auth/browser action or restart. Parent owns next Csite6, then D; C performed no
readiness retest or live mutation. Site runner8092 and invocation remain unchanged.

## Current final d5 checkpoint

The4f CI run45835305578 failed only the two new AppLayout unit cases, with an
unexpected root OPTIONS request. All379 other files/2609 tests passed; scripts
and BFF had no failure. Production build and Chromium script regression passed;
both4f broad runs subsequently passed and smoke was cancelled. The complete
failed-job log is `browser-fixture/c-final-ci-unit-failure.log`.

Cause: the mocked authenticated user had no timezone. In CI's UTC environment,
SidebarTips legitimately queried its unrelated timezone-tip setting; Amsterdam
and Prague have equivalent offsets, so the local fixture did not take that
branch. Exact UTC prepatch reproduction failed both tests in11.49s with the same
strict unexpected-XHR assertion. The only fix adds
`time_zone: 'Europe/Prague'` to that mocked user. Real shell/settings/theme
providers, denied-storage checks and all strict request assertions remain.

Final source `d5aea5ffe1c6171ff4f4e887531d3bcd99538444`, tree
`31c1bd278a6ad4ba25f7fbcb2954d86efc12e6c4`, is clean and published. Exact4f→d5:
ONLY `src/components/layout/AppLayout.test.tsx`, +1/-1. Runtime, other source,
docs and locks are byte-identical. One logical feature commit remains on base
e311b1c0;39 files,+1132/-153; no migrations or repeated dependency/pin stream.
`c-test-fixture-successor-source.json` and `c-test-fixture-4f-to-successor.diff`
bind the proof; diff SHA-256
`853233cc7bffe3f662116b0e52e88e411943073b45c71231e9670ccc8b187c53`.

UTC, Europe/Prague and Europe/Amsterdam each passed both corrected cases
(11.23s/11.35s/11.59s). Exact-file ESLint/Prettier, staged/final whitespace and
actual Git identities passed. Logs: `/tmp/oauth-theme-c-ci-tz-prepatch.log`,
`...ci-tz-{UTC,Europe_Prague,Europe_Amsterdam}.log`, `...ci-tz-quality.log`,
`...ci-tz-commit.log`. No hook was bypassed. No runtime/type/full-suite rerun was
needed for this test-only correction; no product-documentation change was useful.
Lead independently accepted the exact delta and retained review/history proof.

Fresh SSH lease publication4f→d5, post-push remote/local equality and PR335
headRefOid/target-main equality passed. PR body preserves valid a28 imagery and
verification, records the4f package/fixture and UTC diagnosis, and leaves final
CI/native proof separate. E received exact published d5. Parent's terminal receipt establishes all
four final-head workflows SUCCESS, attempt1: CI45838200511 (workflow369520612),
PR smoke45838200637 (369520616), PR broad45838200492 and push broad45838191336
(369520614). Reuse full unit/script/BFF/quick/audit/production-build/Chromium/
broad/mobile scopes at exact d5; no owner polling, retest or duplicate observer.

Parent final package operation15351 passed136s (14:25:43–14:27:59Z), full
`c-final-package.log`/result. `c-d5-package-provenance.json` binds final clean
metadata, complete graph/results hashes and all six own roots. Frontend:
`/nix/store/w2az5mfz26hldkxd1wdbhivvl8hhcvj8-vpsadmin-webui-frontend-1.0.0`;
BFF: `/nix/store/566bhry30ivx0arsarczlcdd63baiilk-vpsadmin-webui-bff-0.1.0`.
Provenance and module-eval have exact4f drv/output reuse; other four outputs
are new. The4f legacy build is explicitly reused through unchanged runtime/
build/lock inputs, not relabelled as a d5 legacy artifact. No extra build/check.

Final registered fixture update is terminal/accepted: old4f BFF a75ff91f stopped
and retired, PID1945626 ended; new BFF
`8a599f7f-026d-41ea-a41a-a2cf698f2388`/PID2055776 runs the exact final store
server.js. Existing TLS `f4a2e6f3-3c3a-43d8-9607-3320e3439b48`/master1623093
consumes the root-only nginx update (syntax/atomic install/reload exit0). Final
build-info and BFF health are200; served index/JS match the immutable frontend,
CSP is retained, real TLS API/v7.0/200 and both alias PNGs have expected hashes.
Receipts: `c-d5-paired-health.json`, `c-d5-fixture-transition.json`,
`c-d5-services-ready.json`, actual `paired-services.json`. Original a28/4f
service/config/effect/root receipts are retained. No auth/data/branding mutation
occurred in the update.

Parent native81608 passed final-d5 desktop denied-storage dark→light and
system→auto. Its third mobile case timed out on a desktop-only shell selector;
the captured dark Dashboard established responsive runner mismatch. Corrected
ignored runner `c-final-responsive-acceptance.mjs`, SHA-256
`8092e9240b8fdce1bbac1f7faa53e1cc87dc55331efcb5a75489767bac963938`, uses the
existing authenticated mobile navigation button on narrow viewports and keeps
all private/app/theme/prepaint/cookie/session assertions. Parent25106 then passed
all three mobile mode returns and desktop cancellation. Its last token case
failed because callback routing did not rewrite a redirected code; the captured
light authenticated Dashboard and Playwright's first-URL routing contract show
that no failed token exchange was exercised. Logs/captures are preserved under
`c-paired-final-default*` and `captures-c-final{,-responsive}`. No product/input
change or repeated default matrix is justified.

Token-only corrected runner `c-token-rejection-acceptance.mjs`, SHA-256
`9da45155bbaa2edf708f13274fbe325cb3b08fa1fab47ac7e967c983aa7b4cea`, intercepts
the original real provider POST, forwards credentials/CSRF with maxRedirects0,
and changes only the genuine redirect's valid-shaped100hex code. State, other
fields, status and headers/cookies are retained. It requires actual BFF journal
`provider_http_error`/400 after state consumption, strict unauthenticated
three-null session JSON, no cosmetic handoff, initiating dark and retry bit.
Syntax and locked API/source-interface proof passed; no browser execution by
owner. Parent35701 completed this one case exit0/11s,15:16:10–15:16:21Z, with two
captures under `captures-c-token-rejection/default`. Supplied terminal receipt
proves injectioncount1, genuine provider302,100hex shape, unchanged state/other
fields/headers/cookies, callback303, actual provider_http_error400, all-null
session/no handoff, and composed PID2333985/unit1ad binding. Full parent log/result
are `c-paired-token-rejection.log`/result. This closes the negative consumer boundary
without a build/retest/repin. Next B cosmetic site reload→parent site6→D→B.

E's actual composition retains clean d5 source but changes runtime Node24.21.0
to24.22.3. Existing package-content checker under actual composed Node passed
388assets. `c-composed-package-provenance.json` binds source
`/nix/store/dhlcv63g7b2par67ng8z60mkfv1d6x43-source`, frontend
`/nix/store/v66i0ikplfv99gypqyxnqh623dh0kyf8-vpsadmin-webui-frontend-1.0.0`
(drv8n6d2rbb4mi7s46gp6dcix5g0j0ai1gl), BFF
`/nix/store/6585ylpqv5zm24cckf1w2zr1q7yjqyrl-vpsadmin-webui-bff-0.1.0`
(drvq91cghh0x1m70nc715kibk44fhx0clgy), own composed roots and actual Node
`/nix/store/2b13mzd001gzgawnf23d3prlcml2pdb8-nodejs-slim-24.22.3/bin/node`.
No build/eval/full-suite/VM was repeated for this boundary.

Lead released exact plan c725f9.../nginx47c779.... Composed transition is terminal:
standalone8a/PID2055776 registered-stop exit0/retired; new registered BFF
`1ad0f849-30c7-4550-8674-2e82dc8768d1`/PID2333985 runs actual Node2b13+BFF6585
in its matching systemd cgroup. TLSf4a2/master1623093 retained; candidate-t and
root-only atomic nginx reload passed. Actual served build-info/index/entryJS
match composed frontend bytes; BFF health/config200, TLS API7.0/200 and both
PNG alias hashes passed. `c-composed-paired-health.json`,
`c-composed-fixture-transition.json`, `c-composed-services-ready.json` and updated
`paired-services.json` bind identity/effects. Initial list-busy refusal caused
no mutation and was reconciled before proceeding. Standalone d5/4f/a28 manifests,
configs, roots and scoped evidence are retained. No source/auth/provider/DB/user/
SSO/branding change occurred; the short window was returned before the parent
token run. The mixed a28 first roundtrip, standalone-d5 desktop2/mobile3/cancel,
and composed-d5 token receipts keep their actual inputs; no single-input8 claim.

The older sections below retain their original checkpoint scope; this current
source/publication/package/fixture/native summary supersedes pending statements.

## Final review closure and publication

Retained reviewer0 found no Blocking/Important or mutation-permission/runtime
finding in the affected general/architecture/risk review. Advisory C-shell-1
requested only the qualifier “a durable mutation lock” in CONFIGURATION; ordinary
best-effort lock behavior stays unchanged. Lead applied that exact word and
accepted the resulting direct remediation without a reviewer/runtime rerun.

Final head `4f894ffc88870ef17f6982f775bd9460b26f3f7d`, tree
`a7e1ab0049d50fa5877ce3bca0d7d43d5c74d605`, clean. Exact2b3→final delta:
one file, one word, +1/-1. Runtime, tests and all other docs are byte-identical.
`browser-fixture/c-shell-final-source.json` binds this proof and publication;
`c-shell-2b3-to-final.diff` SHA-256 is
`f6b9f05d90e50d349926ca445da745aeda11c3f345e8407a57eb70530954e206`.
Documentation audit, staged/final whitespace and actual commit identities pass
in `/tmp/oauth-theme-c-shell-advisory-commit.log`; no declared hook was bypassed.
The complete final branch remains one logical commit,39 files,+1132/-153 on
base `e311b1c0af0f50fa4c6f6ce83c514c1a866eb042`, with no migrations/update streams.

Fresh SSH fetch reconciled expected remote a28 and unchanged main. Exact
`--force-with-lease=refs/heads/dev/oauth-theme-20261126:a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2`
published the final head. Post-push SSH ls-remote, clean local HEAD and PR335's
fresh headRefOid all equal4f894ffc. PR335 retains its scoped a28 capture gallery
and verification, adds the final correction/review and pending final artifacts/
native limits. E received the exact published revision for its final pin.

One post-publication CI snapshot found attempt1/exact final head in_progress:
CI45835305578 (workflow369520612), PR smoke45835305619 (369520616), PR broad
45835305604 and push broad45835294077 (both369520614). No superseded nonterminal
run existed. No retry/cancellation/duplicate observer was launched. Raw snapshot:
`browser-fixture/c-final-publication-ci.json`. No final CI success is claimed.

Final package script `browser-fixture/c-successor-package.sh`, SHA-256
`9dd8fe1edf3a6be27b92684fe5c8696ce0e61e257b986944d851abd8d179e93f`, was released
to the parent only; owner does not inspect its active logs/results or duplicate
the operation. [Package brief](c-package-brief.md) gives exact argv/input guards,
new/reused output boundaries, roots/provenance and bounds. Prepared, unexecuted
registered-service/remaining-case handoff is in
[browser preparation](C-browser-preparation.md#final-head-fixture-update--prepared-not-executed).
It preserves old roots/evidence, uses the final matched immutable pair, and
keeps provider users/flags/branding `{}` unchanged. No live fixture edit or
new native/browser test has occurred during this preparation/publication.

## Current verification boundary

- All four CI workflows listed below completed SUCCESS, attempt1, exact head
  `a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2`. Required CI includes full unit,
  script/BFF, quick audits/typechecks, production build and browser script tests;
  broad and PR smoke cover desktop/mobile projects. Observation is finished.
- `c-browser-rooted.log`: exit0/75s total, eight dev-source cases passed in24.3s.
  Six implemented desktop/mobile captures and `inventory.json` are retained in
  `browser-fixture/captures-c-only/`; served module/source identity is in
  `browser-fixture/c-preview-source.json`. These use synthetic client fixtures.
- `c-package.log`: exit0/165s. Six frontend/BFF/provenance/source/package/module
  outputs and legacy build passed. Exact graph/results are
  `c-flake-metadata.json` and `c-nix-results.json`; six retained own outlinks and
  immutable metadata receipts are in `browser-fixture/c-package-roots.json` and
  `c-package-provenance.json`. These bind clean source a28c59c6; they do not
  certify its later successor. Frontend output is
  `/nix/store/sgcahc4y5jdigwgrxsxxk24dzlc1papm-vpsadmin-webui-frontend-1.0.0`;
  BFF output is
  `/nix/store/wlbpm7m9ms5ipia2hfhalznkb41yv9nw-vpsadmin-webui-bff-0.1.0`.
- Native default phase: `c-paired-default.log`, parent4584 exit1/42s, terminal.
  `default desktop-light-dark-success` passed actual immutable frontend → BFF →
  vpsAdmin OAuth selection → authenticated return. This case remains evidence
  for unchanged a28 behavior. Second denied-storage case
  `desktop-dark-light-success:return` failed at the user-menu assertion because
  the protected shell hit its error boundary. Remaining six default cases,
  site-logo phase and docs phase did not run. No global pass is claimed.
- Actual pair uses reviewed API `1d3f5bca`, HaveAPI
  `439beea801df3139b7154283a171f53c68295939`, synthetic private credentials,
  registered isolated API/BFF/nginx and rooted Chromium154/nginx1.30.5. Service
  and artifact identities are in `browser-fixture/paired-services.json` and
  `paired-health.json`. B owns unchanged users/flags and branding `{}`. No
  native retry, branding reload or docs window is authorized before corrected
  source acceptance. B services-up34/34 evidence is unaffected.

### Protected-shell optional-storage correction

The failure is after successful authentication. `useLocalMutationLocks` read
the localStorage getter during initial display hydration without a guard;
`AppLayout` then had unguarded legacy pin removal. Background recovery and
storage-event display reads also needed to retain their last known guards when
reads fail. The source correction guards only those display paths and local PIN
cleanup. Durable acquisition, verified writes/removal, record parsing, mutation
dispatch, OAuth sessionStorage, state/PKCE, sessions and cosmetic cookies are
unchanged. Unknown display state grants no mutation permission.

Lead authorized this exact scope and consolidation of the published a28 commit.
Because mutation guard display was outside the earlier source review, the same
reviewer0 must assess affected general/architecture/risk lanes and update the
whole-branch history/migration conclusion before publication. No new abstraction
or protocol/interface is introduced. E was notified that a28 is not the final
pin and must be replaced with the accepted published successor.

Prepatch reproduction uses real AppLayout, settings/theme providers and existing
lock hook test homes. `/tmp/oauth-theme-c-shell-prepatch.log` records four
failing assertions plus the background unhandled rejection at the actual
unprotected reads. After the patch,
`/tmp/oauth-theme-c-shell-focused.log` records37/37 passing cases across six files
in9.12s: real authenticated shell and returned light against dark OS with denied
getter/local-only removeItem; denied getter/getItem rejects durable acquisition
before dispatch; unreadable background/storage-event display keeps corrupt
guards; existing lease/generation/HaveAPI/intent/expired-data cases still pass.
One test-only implicit-this annotation was corrected after the first typecheck;
no runtime assertion was changed.

Exact-file ESLint found four inherited exhaustive-deps errors in layout sources
outside the adopted lint roots. The ESLint API comparison against exact a28
source proves identical rule/severity/messages and no new source findings;
both focused test files lint clean. Receipt:
`/tmp/oauth-theme-c-shell-lint-baseline.log`. No unrelated dependency-array
change or lint suppression was made. New AppLayout test formatting is applied;
final type/documentation/whitespace results and exact successor follow below.

The initial guarded hook exceeded the structural500-line ceiling. Lead approved
moving only the storage-event display reader into existing
`localMutationLockStorage.ts`, with a bounded object-key/lock result or no update.
It is invoked inside the state updater and receives the captured event timestamp.
No acquire/write/reducer/OAuth change, new framework, debt exception or budget
adjustment was made. The hook is now487 physical lines and the helper252.

Final focused suite:40/40 in9.11s across the same six files,
`/tmp/oauth-theme-c-shell-final-focused.log`. The three additional event cases
prove current storage wins over stale event data, other object locks survive,
ordinary deletion updates only its target, and corrupt ordinary/uncertainty
events retain non-acknowledgeable guards and reject durable acquisition.
Structural audit passes with zero new/unaccepted violations or aggregate
failures (`/tmp/oauth-theme-c-shell-final-structural.log`). Documentation and
new-test formatting passed; final type/lint receipts and committed identity are
recorded in the consolidated packet below. No publication, artifact build or
native retry has occurred for the correction.

## Consolidated correction review packet

Current repository/branch/worktree remain the C registration below. Exact base:
`e311b1c0af0f50fa4c6f6ce83c514c1a866eb042`; published predecessor:
`a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2`; local successor:
`2b3e9c7e18d8e6465b364ead4ed9298aafba3b82`; tree:
`3afcf6e08f10ebb27e4cfd509e71c6d34c1568a6`. Checkout/index clean.
Fresh explicit main fetch retained the exact base. SSH branch still points at
a28; the successor has not been published. PR335 remains the owning PR.

Complete final history is ONE logical commit:
`2b3e9c7e18d8e6465b364ead4ed9298aafba3b82 auth: preserve appearance through OAuth login`.
Full base-to-head diff:39 files,1132 insertions/153 deletions. Exact a28-to-head
delta:7 files,295 insertions/42 deletions:

- `src/components/layout/AppLayout.tsx`: catch only optional localStorage legacy
  pin cleanup failures; its sessionStorage behavior is unchanged.
- `src/components/layout/useLocalMutationLocks.ts`: guarded initial display and
  background refresh; last displayed guards survive denied reads; storage-event
  reader invoked in state updater with captured timestamp.
- `src/components/layout/localMutationLockStorage.ts`: only the bounded display
  event reader was moved here; no acquisition, verified persistence, parsing
  reducer, stored format or lease implementation changed.
- `src/components/layout/AppLayout.test.tsx`: real authenticated shell/settings/
  theme providers with denied getter/local-only removal and opposite OS.
- `src/components/layout/useLocalMutationLocks.storageIntegrity.test.tsx`:
  denied optional reads, dispatch refusal, retained guards and valid/corrupt
  storage-event semantics.
- `docs/design/CONFIGURATION.md` and
  `docs/work-log/2026-11-26-oauth-theme.md`: durable display/persistence boundary
  and actual verification limits. Lead directly applied the writing skill and
  released both paths; the known final40-case count and PR335 link were added.

Reproducible review artifacts under ignored `browser-fixture/`:

| Artifact | SHA-256 |
| --- | --- |
| `c-shell-a28-to-successor.diff` | `c5a7028f1db07a7e62a15b21b58c6e861fe65b982ec20ca7484a4f277156c174` |
| `c-shell-base-to-successor.diff` | `44e5661e1b369c0df998522aba9e8c044aee55e2c1999b274d25cad17b993ed5` |
| `c-shell-range-diff.txt` | `08114160e688fcadbe741153ef47ba7ec14f9b4243564f734be330c4e2874643` |

`c-shell-successor-source.json` binds base/old/head/tree, clean state, complete
delta inventory, every changed source hash and the three unchanged lock hashes.
No dependency graph/pin, SDK/API resource, framework, endpoint, theme/session
contract, schema or migration changed. No migrations exist at any branch
checkpoint; none were merged, released, deployed or externally consumed. No
repeated dependency/channel/generated update stream or obsolete fixup commit
remains. Upstream history/authorship is preserved. The earlier published a28 was
consumed only by isolated verification and pending E pin preparation; it was
never integrated, released or production deployed. E has been told to replace
its final pin after accepted successor publication. Local old outputs/receipts
are retained as a28 evidence, never claimed as successor artifact proof.

Final quick receipts, all in the pinned Nix environment:

| Command / scope | Result / log |
| --- | --- |
| `npm test -- src/components/layout/AppLayout.test.tsx src/components/layout/useLocalMutationLocks.storageIntegrity.test.tsx src/components/layout/useLocalMutationLocks.test.tsx src/components/layout/useLocalMutationLocks.webLocks.test.tsx src/components/layout/useLocalMutationLocks.haveapi.test.tsx src/components/layout/useLocalMutationLocks.datasetIntent.test.tsx` |40/40,6 files,9.11s; `/tmp/oauth-theme-c-shell-final-focused.log` |
| `npm run typecheck` |PASS; `/tmp/oauth-theme-c-shell-final-typecheck.log` |
| `npm run audit:structural` |PASS, no new exceptions/budget changes; `/tmp/oauth-theme-c-shell-final-structural.log` |
| Exact-a28 vs current ESLint API comparison |Four inherited source messages identical; moved helper and both tests clean; `/tmp/oauth-theme-c-shell-final-lint.log` |
| `npm run audit:design-docs` |PASS after final count/PR link; `/tmp/oauth-theme-c-shell-final-docs.log` |
| `npx prettier --check src/components/layout/AppLayout.test.tsx` |PASS; `/tmp/oauth-theme-c-shell-format.log`; source unchanged afterward |
| staged/final narrow `git diff --check`, scoped inventory assertion, own Git identities |PASS; `/tmp/oauth-theme-c-shell-commit.log`, source JSON |

No declared hook framework or core.hooksPath exists; automatic Git hooks were
not bypassed. Lead explicitly authorized consolidation of the exact published
a28 feature into this one unpublished successor. There is no new long check or
browser retry; all checks and first native success above retain their original
input scope. Root metadata/build provenance and full CI for this new head remain
unverified until review acceptance/publication and the next bounded batch.

Risk remains high because this touches display of persisted mutation guards.
The same retained reviewer0 Sol/xhigh should assess affected general,
architecture and risk lanes under the lead's assignment, including the approved
third source home and complete final history/no-migration conclusion. No generic
storage layer, new authority or broader behavior was introduced. No production,
default integration, release or session lifecycle action is authorized by this
packet. Shared users/flags/branding `{}` and all fixture services remain intact;
native denied-storage retry and remaining C/site/D cases wait for the final
accepted source/artifact boundary.

The sections below retain earlier source/review/publication checkpoints and
prepared commands as history; the current boundary above supersedes their
pending/never-launched statements.

## Exact source and history

- Repository: `git@github.com:vpsfreecz/vpsadmin-webui.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-oauth-dark-theme/vpsadmin-webui`.
- Branch: `dev/oauth-theme-20261126`; target: `main`.
- Fetched base: `e311b1c0af0f50fa4c6f6ce83c514c1a866eb042`.
- Final local head after C-1: `a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2`.
- Independently reviewed predecessor: `b1f63a5eab2ffbaca239047eceddc2cc98e075d5`.
- Whole series: one logical commit, `auth: preserve appearance through OAuth login`.
- Worktree/index clean after commit. `origin/main` freshly fetched unchanged
  before commit. No rebase, obsolete approach, fixup stream, migration, generated
  dependency update or pin stream remains. Nothing was merged, released, deployed
  or externally consumed. Independent whole-branch history/no-migration conclusion
  was accepted on the reviewed predecessor. The direct C-1 correction is below.

Inspect the complete series and final diff in that worktree:

```sh
git log --reverse --stat e311b1c0af0f50fa4c6f6ce83c514c1a866eb042..a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2
git diff e311b1c0af0f50fa4c6f6ce83c514c1a866eb042...a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2
```

The companion provider contract is HaveAPI `doc/en/oauth-theme.md`, introduced
in `1046a14f2f0485f460b3918098e5bc078a3da758`, present at completed A+D head
`439beea801df3139b7154283a171f53c68295939`. React does not depend on that Ruby
package; actual combined provider acceptance remains later work.

The lead requested the root work-log pointer before final review. The owning
unpublished commit was amended from `a743dc4cbfd6b56b4f827717504e09dd6320b722`
to `b1f63a5eab2ffbaca239047eceddc2cc98e075d5`;
its exact old-to-new delta is only four added lines in `WORK_LOG.md`. The
settled title/link received lead's direct writing approval. The documentation
audit passed again (`/tmp/oauth-theme-c-worklog-docs-audit.log`), scoped staged
and final whitespace checks passed, and the resulting checkout is clean. No
runtime checks were repeated; all runtime/input evidence below is unchanged.

## Changed scope

34 files, 843 insertions / 117 deletions. Complete inventory is the exact
base-to-head `git diff --name-only` above.

| Area | Files / behavior |
| --- | --- |
| Browser transport | `src/lib/auth/oauthTheme.ts`, `oauth2Client.ts`; bounded enum/URL/cookie helper, independent return opt-in, initiating preference alongside existing state, success-only handoff, state storage remains fail-closed |
| UI settings and entry | `src/app/uiSettings{,Model}.ts*`; `PublicLayout`, `AppShell`, `OverviewPage`, OAuth login/callback pages; current preference on entry/retry, guarded optional localStorage, one pending merge into server settings, missing-record semantics, per-mount in-flight effect reuse |
| First paint | `index.html`; read-only handoff before React; guarded optional storage and initiating legacy preference; callback response theme is never read from the URL before authentication |
| BFF | `bff/{oauth-theme,server,oauth-error-page}.js`; selected.initiating allowlisted enums, host-only 120s cosmetic cookie, Secure on HTTPS/Lax/root app path, new/failure clear, initiating error/retry scheme; state consumption and session rotation retained; strict three-field `/session.json` unchanged |
| Packaging/CSP | `packages/bff-runtime-files.json`; add runtime helper. `nixos/modules/webui.nix` and three existing `deploy/` policy/template files; only replace the owning inline bootstrap hash. `scripts/fixtures/lint-coverage.json`; adopt changed OAuth client/helper into existing lint/format gate |
| Checks | Existing OAuth/settings/layout/overview/BFF tests plus `oauthTheme.test.ts`; existing typed `theme_language_bootstrap.spec.ts` gains desktop/mobile screenshot and handoff scenarios |
| Docs | Existing REQ-005, workflow and configuration explanation; dated `docs/work-log/2026-11-26-oauth-theme.md` and compact discoverability link in root `WORK_LOG.md` |

No API resource/action declaration, SDK, token/session response schema, database,
dependency or lock change. No UI framework or endpoint was introduced. Existing
UI forms/feedback and bilingual BFF copy remain in place.

## Inputs and quick checks

All language/tool checks used `nix develop`: Node `24.21.0`, npm `11.19.0`.
The locked vpsAdmin terminology guide and localization procedure were read at
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff`. Lead completed the required direct
writing pass on the four docs and two new existing-style diagnostic messages.

Unchanged input SHA-256 values:

| Input | SHA-256 |
| --- | --- |
| `package-lock.json` | `eee6460485c5aea039721b682839b58d44ce19b7acb3e42f50c59650cd9d429d` |
| `bff/package-lock.json` | `50ffa053cd8b22d78505d10117fa2a42db62f73f6aa0b6de18138cbca9277d5a` |
| `flake.lock` | `6ea5fc4d9d7b43a6c4d6b18a70dc7206f3ba760053513215093b58e24721fa99` |

Inline bootstrap CSP hash:
`sha256-GsLiqeMVCzP8bNzzGixyR67nIkrZ+XnSTAT8QzB3MAo=`.

Root and BFF `npm ci --no-audit` succeeded (12s/1s); no graph edits. Repository
hook framework search found none declared and `core.hooksPath` is unset. Own
author/committer identity was verified in the actual pinned commit context;
no hook was bypassed. Scoped staged `git diff --check` passed before commit.

| Check | Result / disposable log |
| --- | --- |
| `npm test -- src/lib/auth/oauthTheme.test.ts src/lib/auth/oauth2Client.test.ts src/pages/oauth/OAuthPages.test.tsx src/app/uiSettings.test.tsx src/app/uiSettingsModel.test.ts src/components/layout/PublicLayout.test.tsx src/pages/public/OverviewPage.test.tsx` | 74 passed, 7 files, 14.08s; `/tmp/oauth-theme-c-focused.log` |
| Final callback tests after 3 additional cases | `npm test -- src/pages/oauth/OAuthPages.test.tsx`: 9 passed, 4.47s; `/tmp/oauth-theme-c-final-callback-e2e-types.log` |
| Final missing-record/denied-storage cases | `npm test -- src/app/uiSettings.test.tsx -t 'does not create a missing record for unchanged login'`: 4 passed, 14 skipped, 7.09s; `/tmp/oauth-theme-c-final-absent.log`. Combined distinct focused coverage: 79 cases |
| `npm run test:bff` | 63 passed, 4.75s; `/tmp/oauth-theme-c-final-bff.log` |
| `npm run typecheck`, `typecheck:tooling`, `typecheck:e2e:core`, `typecheck:bff:core` | Passed; root/tooling in `/tmp/oauth-theme-c-remaining-quick.log`, final E2E in callback log above; BFF core passed 6 compile fixtures and intentionally covers the existing queue/signature contract, not server/pages |
| `npm run env:locked`, `lint:tailwind`, `lint:patterns`, `lint:scoped`, `format:check` | Passed; 47 adopted ESLint files / 84 format files; `/tmp/oauth-theme-c-final-docs-quality.log`, `...remaining-quick.log`, `...audits.log` |
| `audit:design-docs`, `audit:i18n`, `audit:i18n-structure`, `audit:csp`, `audit:pages`, `audit:structural`, `audit:component-contracts`, `audit:active-docs`, `audit:overlays`, `audit:lookup-primitives`, `audit:api-barrel-imports`, `audit:ui-strings:check`, `audit:mutations:check` | All passed through component commands equivalent to `ci:quick`; no blanket rerun needed. Logs: `/tmp/oauth-theme-c-audits.log`, `...remaining-quick.log`, `...extra-audits.log` (structural pass followed by initial CSP failure), `...csp-package.log` (corrected CSP + remaining checks), `...final-docs-quality.log` |
| `node --test scripts/check-package-source.test.mjs scripts/check-package-contents.test.mjs scripts/csp-policy.test.mjs` | 17 passed; `/tmp/oauth-theme-c-csp-package.log` |
| `nix-instantiate --parse nixos/modules/webui.nix`, final `git diff --check` | Passed |

Corrections during implementation: initial settings tests waited inside an act
before hydration completed; corrected to await idle before the debounce.
The head-script VM fixture uses the checkout file directly. Adding a cosmetic
cookie exposed old BFF fixtures assuming the first Set-Cookie was the session;
they now select actual `webui_next_sess` by name, preserving their auth assertions.
The CSP audit required the inseparable policy hash refresh above. All affected
checks passed after correction; no unresolved failure remains.

## Documentation placement

| Topic → reader/class | Authoritative path | Evidence / applicability |
| --- | --- | --- |
| Provider wire extension → maintainers/reference | HaveAPI `doc/en/oauth-theme.md` | Exact companion revision above; React links the owning source rather than duplicating provider internals |
| React preference persistence → contributors/reference | `docs/design/CONFIGURATION.md#oauth-theme-handoff` | Cookie, settings merge, missing-record and rollback semantics match implementation/tests |
| Login interaction → product/contributor workflow | `docs/design/WORKFLOWS.md`, REQ-005 in `REQUIREMENTS.md` | Success and failure behavior, unchanged account fields and optional storage documented |
| Current implementation → maintainers/historical work log | `docs/work-log/2026-11-26-oauth-theme.md` | Prepared vs reviewed/merged/deployed kept distinct; browser/package limits explicit |
| Exact check/rollout evidence → session | This file, existing session state | No individual rollout/test report added to lasting feature reference |

## Final review and C-1 direct remediation

Lead reported the retained Sol/xhigh review complete across all four lanes:
no Blocking findings, one Important C-1. Whole-branch history, no migrations,
absence of repeated update streams and documentation placement were accepted at
`b1f63a5eab2ffbaca239047eceddc2cc98e075d5`. No additional interface/design concern
was reported. Lead authorized narrow direct remediation under review step9,
without automatic whole-review confirmation or blanket unchanged checks.

C-1: the head prepainted the legacy initiating preference, but React's settings
initializer used only localStorage/success cookie and reset to system while the
exchange was pending. The provider now reads the bounded login request enum only
on its exact configured login path, or the existing fresh pending-state preference
only on its exact callback path. The successful cookie remains highest priority.
No unvalidated callback response query theme, authentication bypass, new storage
format, endpoint or framework is added. Existing documentation already describes
this contract and needs no semantic change.

The owning unpublished commit was consolidated to
`a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2`. Exact remediation range:
`b1f63a5eab2ffbaca239047eceddc2cc98e075d5..a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2`.
Only `src/app/uiSettings.tsx` and its existing test change:107 insertions,
2 deletions. Complete narrow diff: `/tmp/oauth-theme-c1-remediation.diff`, or
`git diff b1f63a5eab2ffbaca239047eceddc2cc98e075d5 a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2`.

Targeted check evidence on the correction:

- `nix develop -c npm test -- src/app/uiSettings.test.tsx`:27/27 passed,
  15.02s, `/tmp/oauth-theme-c1-focused.log`. Uses real settings/theme providers,
  opposite OS preference and denied localStorage during a deferred actual legacy
  token exchange and failure; direct basename light/dark/auto entry plus OS change;
  invalid/missing pending, duplicate login input and unrelated path rejection.
- Root typecheck, exact-file ESLint and Prettier passed:
  `nix develop -c bash -c 'npm run typecheck && npx eslint src/app/uiSettings.tsx && npx prettier --check src/app/uiSettings.tsx && git diff --check'`;
  `/tmp/oauth-theme-c1-types-quality.log`.
- Own Git identities, scoped staged whitespace and final narrow diff whitespace
  passed; amendment retained one logical feature commit. Checkout/index clean.
- No long checks, publication, source packaging or deployment. Previous unchanged
  quick checks/locks/CSP proof remain applicable. Final distinct focused cases
  combine previous79 with the9 new C-1 cases; the27-case settings rerun includes
  all18 earlier settings cases.

## Remaining work and prepared commands

Lead accepted C-1 after inspecting the exact source/test diff and supplied
27-case/type/lint evidence. Source is frozen at the accepted successor above.
SSH publication and the repository-required focused PR are complete:

- Branch `refs/heads/dev/oauth-theme-20261126` on
  `git@github.com:vpsfreecz/vpsadmin-webui.git`.
- Fresh `git ls-remote` equals local/PR head exactly:
  `a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2`; checkout remains clean.
- Fresh fetched `origin/main` remains base
  `e311b1c0af0f50fa4c6f6ce83c514c1a866eb042`.
- [PR335](https://github.com/vpsfreecz/vpsadmin-webui/pull/335), target main,
  OPEN. Includes REQ-005, actual scoped evidence and remaining browser/package
  gaps. Screenshots follow actual browser verification.
- E was notified of the exact published revision for normal channel pinning.
- No merge, deployment or release. Source did not change during publication.

CI run identities were read once after publication/PR creation. All had
attempt1, exact head `a28c59c6ee5e62bf27f4858b266ea2e5ef5f62f2`, in_progress and
no conclusion at that read:

| Workflow / event | Workflow ID | Run ID |
| --- | --- | --- |
| Playwright smoke / pull_request | 369520616 | 45819880644 |
| CI / pull_request | 369520612 | 45819880490 |
| Playwright broad smoke / pull_request | 369520614 | 45819880434 |
| Playwright broad smoke / push | 369520614 | 45819815700 |

Lead received exact workflow/run/attempt/head receipt and owns observation.
C started no duplicate CI watcher and performed no polling/retry/cancellation.
Both broad runs have the current head; no superseded-head run was identified.

Long checks below have not run. Use the lead's fresh verification watcher/monitor
policy. Do not repeat unchanged passing quick checks. These commands run from
the C worktree with the unchanged exact locks above:

```sh
nix develop -c npm test
nix develop -c npm run test:scripts
nix develop -c npm run build
nix develop -c npm run build:legacy
nix build --no-link --print-out-paths .#frontend .#bff .#checks.x86_64-linux.provenance .#checks.x86_64-linux.source-contents .#checks.x86_64-linux.package-contents .#checks.x86_64-linux.module-eval
```

Full unit/scripts/builds: expected a few minutes, stop for a failed command and
return evidence to owner for diagnosis. Script suite includes 17 already-proven
package/CSP fixtures; the full command is the repository's standard broader
script acceptance, not a replacement for their focused receipt. Nix outputs:
expected several minutes/cache dependent; no VM/kernel is selected. Stop and
escalate an unexpected kernel build or uncertain process outcome.

For the narrow browser fixture, register one actual Vite preview server on a
free port (example 5186); then invoke the wrapper directly without its self-start
environment. Lead owns the later exact command/operation IDs and service launch:

```sh
dev-session service run 2026-11-26-oauth-dark-theme --as-is --name c-theme-preview --cwd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-26-oauth-dark-theme/vpsadmin-webui -- nix develop -c npm run dev -- --host 127.0.0.1 --port 5186
env -u E2E_START_SERVER E2E_BASE_URL=http://127.0.0.1:5186 nix develop -c node scripts/playwright.mjs test e2e/specs/public/theme_language_bootstrap.spec.ts --project=chromium --project=mobile-chrome --workers=1 --retries=0
```

Expected under 3 minutes after browser setup; stop on test/setup failure. The
fixture uses synthetic HaveAPI responses, exercises handoff with denied storage,
pauses before application-module evaluation to assert head-script paint, checks
one-shot consumption and auto OS response, and writes implemented desktop/mobile
screenshots under ignored `e2e/test-results`. No production credentials or API
objects are involved. It does not certify the real provider UI or a deployed API.

Representative combined provider/BFF browser roundtrip and actual OAuth form
screens require B's rendered templates plus isolated credentials/provider setup;
lead coordinates B/C after review. Real deployment is not claimed. No temporary
service or resource claim has been created by C so far.

Stable session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-26-oauth-dark-theme/


## Bounded CI coverage snapshot after publication

At the lead-requested next snapshot, all four workflows were still in progress,
attempt1 and accepted head a28c59c6; no terminal workflow failure. CI45819880490
had these completed passing scopes:

- Production build job139909085845, success at12:28:59Z: locked-toolchain check
  and `npm run build`. No duplicate local plain production build is planned.
- Chromium script regression job139909086477, success at12:29:30Z:
  `npm run test:scripts:browser` using Playwright-managed Chromium. Reuse this
  passing script-browser receipt.
- Required nonbrowser job139909086274: both production dependency audits and
  `ci:quick` passed; full unit/script/BFF step was in progress since12:29:49Z.
  Do not launch duplicate local full suites while that required source is active.

The workflow contains no Nix immutable package/provenance/source-content/module
check and no legacy production build. Smallest uncovered package batch remains
those exact Nix outputs plus `npm run build:legacy`. Actual C-only browser
source/scheme/screens and paired provider/docs are independent uncovered scopes.
See C-browser-preparation.md and ignored c-preview-source.json for the registered
preview/current-source import identity and ready eight-case fixture command.
C started no polling loop or duplicate CI observer.


## C-only launch failure and rooted environment correction

The first eight-case browser operation failed at browser launch, exit1 after16s;
no application assertions or screenshots ran. `c-browser.log` preserves the
full failure. Lead confirmed outer44187/underlying47461 and utility effects fully
quiescent. The registered Vite preview remains available, source a28c59c6 unchanged.

Minimum diagnosis compared the original successful14.8s setup receipt with current
store state: the entire expected Chromium7d79... output directory is absent and
`nix path-info` reports it invalid; nginx mff9... still exists with bin/nginx.
The setup used --no-link, retained no GC root and logged no executable-version
probe. The unrooted output disappeared, consistent with GC; no separate GC event
receipt was inspected. This is not a basename-only discrepancy or product defect.

Lead accepted one identical locked-output re-realization with ignored/untracked
session outlinks `browser-fixture/nix-chromium` and `nix-nginx`, retained through
all C/B/D browser verification. Exact fail-fast batch is
`browser-fixture/c-rooted-browser.sh`, SHA-256
`acec2a2f54cfe4ba766944fbc33588809052b416c1cc641ca0e5f9a8465cb97d`;
mode700, bash syntax passed, not launched by owner. It verifies accepted head/clean,
realizes exact locked outputs, verifies resolved output paths, -x, actual version
and `nix-store --query --roots`, then runs the same eight cases with the stable
outlink executable. Root receipts go to chromium-roots.txt/nginx-roots.txt;
recommended real full log c-browser-rooted.log. First setup/test error stops, no
adjustments/retry inside. Definitive version/root/browser outcome awaits that one
fresh lead utility receipt. No global policy/cache hack, source change, service
replacement or lifecycle cleanup is authorized/implied. D was notified not to use
the disappeared unretained path before the rooted receipt.


## Native mobile selector correction

Operation81608 ended exit1/46s (14:34:02–14:34:48Z); all contexts/processes ended.
Actual denied-storage desktop dark→light and desktop system→auto passed, including
strict mode/cookie/session assertions. The next mobile light→dark capture shows
its rendered dark member Dashboard and Navigation header. The desktop nickname
control is intentionally hidden below768px while its mobile drawer is closed;
waiting for that visible desktop control was a runner mismatch. No ErrorBoundary,
product/auth/input defect or rebuild/re-pin requirement was found. The failed
mobile case's later mode/cookie/session assertions remain unexecuted.

Lead accepted only a viewport-specific authenticated-shell selector and remaining
case selection. Frozen `browser-fixture/c-final-responsive-acceptance.mjs` SHA-256
`8092e9240b8fdce1bbac1f7faa53e1cc87dc55331efcb5a75489767bac963938` waits for
AppSidebar/MobileNavigationTrigger `shell.mobile-nav-button` on mobile and
AppHeaderMenus `shell.user-menu-button` on desktop. Existing private/app,
prepaint/mode/cleared-handoff/cookie/session checks are unchanged. Syntax and
bounded actual source-marker mapping passed. No owner auth/test was run.
`c-final-responsive-runner.json` lists exact source/scopes/default5/site6.

Next default5 is mobile3 plus desktop cancel/mobile token failure, preserving the
completed desktop2 and all original inventories/captures. Parent command uses the
same Node/Chromium/manifest/env/cwd, new runner and separate output
`captures-c-final-responsive`, full log `c-paired-final-default-remaining.log`.
Site6 uses that corrected runner later. Source/services/provider/users/flags/SSO/
branding{} remain unchanged and frozen; parent alone launches/observes native runs.
