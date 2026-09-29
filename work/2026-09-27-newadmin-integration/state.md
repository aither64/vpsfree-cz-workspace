---
lifecycle: active
---

# 2026-09-27-newadmin-integration

## Status

- Phase: the OAuth session identity change is implemented, reviewed, built and published on both development branches. WebUI `534caa83` passes pinned BFF/quick gates, packages, HTTPS VM and GitHub CI. Configuration `a4336908` pins it and passes build-free evaluation, independent review and the exact UI-host build. Ready for the user's controlled deployment and fresh-login acceptance; default-branch integration still awaits explicit approval. The live frontend previously reported WebUI `b86e202d`; the exact active site generation has not been independently established. Earlier optional packaged-browser VM aborts remain a coverage gap, not a proven product defect.
- Identity verified with `dev-session current` and both environment markers.
- Retained roster: `architect0` (design), `implementer0` (implementation),
  `reviewer0` (independent review). The one active WebUI checkout is
  `vpsadmin-webui`, clean on branch `2026-09-27-newadmin-integration` at
  `534caa83a5f97d2b40b4a126886649b14dc9e8d3`. Its earlier history,
  package, module, VM and reconciliation worktrees are retained inactive
  snapshots, not competing candidates. The one active site checkout is
  `vpsfree-cz-configuration`, clean at
  `a433690828a23c13a8ccb3df0c07b9f2d915f0ca` after the generated
  `534caa83` pin and prior CSP, credential-source, missing-probe-series and
  host-only SSH authorization commits; `6586b383` was the last previously recorded deployed
  site revision, but the exact current site generation needs operator confirmation.
  Its newly registered
  reconciliation worktree is inactive and must not be used for edits.
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
- [x] Commit the WebUI repository/tooling baseline with the locked vpsAdmin input.
- [x] Commit full catalog integrity and rendered count regression coverage.
- [x] Commit coherent workflows, browser provisioning and archive-safe docs audit.
- [x] Commit structural debt disposition and narrow UI-string fixture classification.
- [x] Record lead acceptance of the exact inherited ledger and pass `ci:quick`.
- [x] Commit BFF public configuration and startup validation; 46 BFF tests and quick gate pass.
- [x] Commit required frontend bootstrap and focused compatibility tests.
- [x] Locked-toolchain quick gate and production build on the rewritten WebUI head.
- [x] Review WebUI authentication/bootstrap changes in the consolidated whole-branch review.
- [x] Commit the first bounded network-list and DNS lookup unit in the isolated WebUI worktree.
- [x] Verify its locked-toolchain quick gate and production build.
- [x] Rewrite the unpublished introducing commits with descriptive messages and rebase the network-list unit.
- [x] Commit the catalog, BFF error and address-count localization pass.
- [x] Commit dynamic VPS shutdown/poweroff labels and remove two structural exceptions through extraction.
- [x] Finish locked quick gate and production build on localized head `0576063`.
- [x] Reconcile the site configuration brief against confctl, proxy, DNS and monitoring conventions.
- [x] Commit reproducible frontend/BFF Nix packages and build provenance.
- [x] Finish exact package-head flake, quick and production-build checks.
- [x] Review the committed package boundary in the consolidated whole-branch review before package builds.
- [x] Implement and evaluate the reusable NixOS service module in its isolated worktree.
- [x] Implement WebUI Nix packages, module and focused NixOS VM test fixture; evaluate its derivation and flake outputs without building.
- [x] Implement site machine, proxy, DNS and monitoring configuration with an explicit installed-state gate.
- [x] Fold the fresh-container 26.05 setting and final module option contract into the original site branch; evaluate its new-host derivation without building.
- [x] Complete consolidated whole-branch review of the original WebUI and site checkouts.
- [x] Build exact-head WebUI packages and package-content checks.
- [x] Run the full HTTPS VM fixture on the exact committed WebUI head.
- [x] Build the seven affected site machines and inspect rendered nginx, DNS and monitoring configuration.
- [x] Reconcile whole-branch and focused independent review of the committed WebUI changes.
- [x] Remove the obsolete jsdom encoding patch after fresh locked install and direct DOM regressions.
- [x] Add scoped ESLint/format gates with a reviewed adoption inventory and locked root hash.
- [x] Add strict tooling type coverage and align root Node declarations with Node 24.
- [x] Commit the first strict E2E core with explicit deferred-spec inventory and focused fixtures.
- [x] Review the E2E core and verify its focused browser tests.
- [x] Commit strict static contracts for the BFF session queue and pass the locked quick gate.
- [x] Independently review the BFF queue static-contract change.
- [x] Run its full runtime tests and affected package checks.
- [x] Commit two-worker PR browser defaults and retain reports after passing retries.
- [x] Independently review the browser-runner change.
- [x] Run controlled desktop/mobile browser suites and capture failures.
- [x] Repair current browser fixture failures and rerun affected focused groups.
- [ ] Expand E2E/BFF type coverage.
- [x] Pass complete desktop/mobile PR browser suites on the corrected head.
- [ ] Packaged browser smoke through the production BFF/HTTPS VM topology: deferred after unattributed aborts; retain as a coverage gap.
- [x] Application/configuration implementation, independent review and builds.
- [x] Publish both development branches and pin the exact WebUI revision through the configuration channel.
- [x] Finish published-branch GitHub desktop/mobile smoke.
- [x] Diagnose the live console CSP failure and verify the public heatmap origin.
- [x] Add exact frame origins and replace environment secrets with systemd credentials in committed WebUI/site source.
- [x] Complete independent four-lane follow-up and whole-branch review; no Blocking or Important findings.
- [x] Add absent-series coverage for both newadmin public probes and pass its focused Prometheus fixture.
- [x] Review and verify both follow-up branches, then provide operator credential and deployment instructions.
- [x] Authorize Kerry's new deployment key only on the UI host; verify rendered SSH keys and publish the configuration branch.
- [x] Correct OAuth session client IP and WebUI User-Agent; review, test and pin the new WebUI revision.
- [x] Build the pinned host, finish exact-revision CI and publish the configuration development branch.
- [ ] Operator acceptance on the actual VPS, API and browser.
- [ ] Explicit default-branch integration; user reports an initial deployment.

## Next actions

The live frontend previously reported WebUI source `b86e202d` through its
public `build-info.json`. The session identity defect was traced to the BFF's
server-side OAuth token request: the trusted edge supplies the browser IP to
`req.ip`, but the old BFF omitted `Client-IP` and sent Node's default
User-Agent. The accepted `design.md` brief required a validated callback IP
only for code exchange and the fixed `vpsadmin-webui` User-Agent on every
provider token request. `implementer0` committed that BFF/test/docs change at
WebUI `534caa83`. Pinned BFF tests passed 57/57, `ci:quick` passed, all 11
module-eval results are true, and the flake no-build check passed. Exact-head
frontend/BFF packages and package-content checks passed, followed by the
ordinary HTTPS VM in 77 seconds. The first VM attempt was stopped before
testing at a kernel-modules derivation; inspection proved it only assembled
already-substituted inputs and did not compile kernel source. Logs are under
`/tmp/newadmin-oauth-metadata-{quick-gate,flake-eval,packages-vm,vm-retry}/`.

The fallback independent reviewer examined all 21 WebUI feature commits and
the complete diff in four lanes, finding no Blocking or Important issue,
obsolete branch history or migration. One Advisory remains: inherited
`UserSessionsModel` displays the API IP first when both API and client IPs
exist, while details/search include the client IP. The accepted OAuth brief
has no SPA change, so this is a separate presentation follow-up. The same
reviewer examined all 11 site feature commits and final diff after the exact
`534caa83` generated pin at `a4336908`, with no findings, obsolete source
approach or migration. Earlier generated pins are retained because their
revisions were published/deployed. The exact site flake no-build check passed.
The first host build exited at confctl's interactive confirmation without
building. The noninteractive exact-head `confctl build --yes` then passed in
109 seconds, producing generation `2026-09-29--15-33-14` for
`cz.vpsfree/vpsadmin/int.vpsadmin-webui1`; no unexpected kernel compilation
occurred (`/tmp/newadmin-oauth-metadata-site-host-build-retry/`). GitHub CI run
`36575754287` was explicitly dispatched for the WebUI head and all three jobs
passed: required nonbrowser checks, Chromium script regression and production
build (`/tmp/newadmin-oauth-metadata-ci/`). Both development branches are
published at the exact reviewed heads. The user retains deployment ownership.

Before activation, use the site operations guide to verify the existing three
`/private/vpsadmin-webui/` credential files and preserve the signing key, then
run the normal dry-activate and switch against the pinned feature branch. After
activation, verify build-info, health, a fresh OAuth login, a newly created
vpsAdmin session's client IP and exact `vpsadmin-webui` User-Agent, and logout.
Older session records retain their original metadata; do not use one as proof
of the new code exchange. Roll back the paired host/WebUI generation if the
new login fails, retaining the compatible session store and signing secret.

The site feature branch is published at `c95890ec`. Its SSH authorization
commit adds only the new public key in `data/ssh-keys.nix` and binds it to
`kerrycze` on `int.vpsadmin-webui1`. Independent four-lane review found no
Blocking, Important or Advisory findings and confirmed no migration. The
exact target and control-host NixOS system builds passed. In their rendered
root authorized-key files, the old Kerry fingerprint occurs once on each
host; the new fingerprint `SHA256:OealF7ki4iyhmZ5Ogp74K/cP9hsDEgMC6n5YV6j3xeA`
occurs once on the UI host and not on the control host. Both Kerry keys retain
the expected admin identity options. The new key is not active until the user
deploys this generation using existing access. After activation, verify login
with the new key and keep the prior generation available for rollback.

The follow-up review packet covers all 20 WebUI commits from `origin/main` to
`b86e202d` and the eight site commits from `origin/master` to `4ed64fff`,
with no database or persisted-format migration. Retained `reviewer0`
(`gpt-6-sol`, xhigh, read-only) completed the general, architecture, scope and
risk lanes with no Blocking or Important findings. Its two Advisories were
missing absent-series alert coverage for the two public probes and a stale
`docs/design/OPERATIONS.md` pointer. The former is corrected by a ninth site
commit, `fcd5e673`, with its pinned Prometheus 3.12 fixture passing; the latter
is accepted for this deployment because it changes no
runtime or operator guide and a WebUI docs-only SHA change would require a new
pin and rebuild. Revisit the pointer before default-branch integration. The
reported inline-script CSP warning remains unattributed and needs controlled
browser evidence after activation. The initial WebUI `aff1e4b0` and site `6586b383`
revisions were already published and user-reported deployed; preserving those
exact revisions is the reason for separate follow-up commits despite the
branches being unmerged. The removed experimental packaged-browser check is
absent from the current heads.

Exact WebUI `b86e202d` quick evidence: pinned Node 24.21 BFF tests 53/53;
`nix develop --command npm run ci:quick` passed in 88 seconds (log
`/tmp/newadmin-webui-credentials-quick/ci-quick.log`); module-eval returned
11 true results including credential interface and legacy coexistence;
`nix flake check --no-build --impure --no-write-lock-file --option
allow-import-from-derivation false` passed. Exact site `fcd5e673` no-override
flake no-build passed, and the UI-host toplevel derivation evaluated to
`/nix/store/x2b70na319l36cn1nss5dmx20rxhy40x-nixos-system-vpsadmin-webui1-26.05.20260927.cf5e765.drv`.
The generated lock changed only WebUI `rev`, `narHash` and `lastModified`;
root API/Nixpkgs follows are untouched. Site source hooks and both branch
diff checks passed. Exact WebUI frontend/BFF and source/package-content builds
passed, followed by the ordinary NixOS VM in 184 seconds at `b86e202d`.
The pinned site-host build passed at `fcd5e673` in 31 seconds and rendered the
BFF unit with exactly three `/private/vpsadmin-webui/` `LoadCredential` paths,
no `EnvironmentFile`, and `UnsetEnvironment` for retired secret names. The
rendered nginx static CSP contains the exact console and heatmap frame origins,
retains the map origin and original script hash, and leaves console outside
`connect-src`. Both development branches are published at the exact heads.
During publication, `origin/master` of the site repo advanced from `46c6ae81`
to `e47474e4` with unrelated staging/unstable input and Gemfile.lock updates.
The feature branch remains based on its published/deployed baseline; reconcile
that default-branch drift before any later integration, not during this scoped
activation.
The exact WebUI branch [CI run](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/36559880025)
passed on `b86e202d`: required nonbrowser checks, production build and Chromium
script regression. The remaining sequence is the user's credential preparation
and controlled activation, followed by real browser and live API acceptance.

The site now pins WebUI `b86e202d` through a confctl-generated lock commit;
the exact pinned no-build flake check and UI-host derivation evaluation pass.
The WebUI's pinned `ci:quick` and all 53 BFF tests pass; its reusable module
evaluation passes all 11 cases, including removed `environmentFile`, mandatory
credential paths and legacy PHP coexistence. The package, ordinary VM and
pinned site-host builds passed. The separate inline-script CSP warning
does not match the deployed index's allowed inline bootstrap hash, so this
change does not widen `script-src`. The updated credential instructions are in
`deployment-runbook.md` and the site operations guide; no real values are
recorded here.
An unauthenticated read-only HEAD of the live top-level document on 2026-09-29
still returned `frame-src 'self' https://www.openstreetmap.org` without the two
new origins, consistent with this follow-up not yet being deployed. The
separate `https://console.vpsfree.cz/` root returned 404 and does not establish
the tokenized console page's own CSP behavior.

The current published WebUI source is `b86e202d039cbe1aa89f1ad0b7edf58808028a5f`
on `vpsfreecz/vpsadmin-webui` branch `2026-09-27-newadmin-integration`.
The current published site configuration is `c95890ec8b9a8e8b9fa442935e946f7d0a20ffd7`
on the branch of the same name in `vpsfreecz/vpsfree-cz-configuration`.
The user authorized development-branch pushes; neither repository has approval
for feature integration into `main` or `master`. No deployment was run by this
session; the user reports an initial deployment of `newadmin.vpsfree.cz`.
The first `vpsadmin-webui` channel update created only the new lock node/root
edge; an exact-SHA channel set confirmed the revision. The existing
`vpsadminServices` input remains at `a65a4dfeb92a59df4a80a737a20bcbf8558793ff`.
The seven-machine remote-pin build passed in 237 seconds
(`/tmp/newadmin-site-remote-pin-seven-machines/`). Its proxy nginx configuration
is the same Nix store object as the reviewed draft; the rendered backend unit
uses `/private/vpsadmin-webui.env`, `/var/lib/vpsadmin-webui/sessions` and the
private listener. The installed frontend and BFF `build-info.json` files both
record clean source `aff1e4b0`. Both DNS views load at serial `2026092800`, and
the pinned newadmin Prometheus rule check passes. WebUI GitHub CI run
`36491380529` succeeded for the exact published SHA; smoke run `36491390601`
passed with 378 desktop and 303 mobile tests. Independent review found no
new issue in the full 19-commit WebUI and five-commit site histories, no obsolete
unmerged approach, and no migrations. The older entries below retain evidence
from earlier branch heads rather than defining the current deployment candidate.

The retained `reviewer0` (Sol/xhigh, read-only) did not return findings after
repeated session-bound assignments. The mandatory-review fallback used the
installed default team's review-purpose Sol/xhigh policy. It inspected all four
general, architecture, scope and risk lanes for the complete WebUI 13-commit
and site 4-commit histories and cross-project contract. A later targeted rerun
covered the final module/header and VM fixture revisions in general,
architecture and risk lanes. Both reviews found no Blocking or Important issue,
no obsolete unmerged approach or fixup, and **no database or schema migrations**
(the changed `migration_plans.ts` is Czech locale text). The targeted rerun
found no new Advisory issue. Early nginx rejection responses no longer carry
generic server headers, but serve no application content; reachable static and
BFF routes retain their intended headers and BFF-owned OAuth CSP.

The full pinned nonbrowser WebUI suite passed 1,628/1,628 tests at the
pre-package-fix snapshot. The exact clean package head passed the six-output
Nix package/content/module/provenance batch in 63 seconds
(`/tmp/newadmin-webui-package-clean-gate/`). That package patch is unchanged at
final WebUI head `f131a19`. At this exact final head, all ten build-free
module-evaluation assertions and the flake no-build check passed. The full
HTTPS VM test passed in 193 seconds on the clean head
(`/tmp/newadmin-webui-https-vm-clean-gate/`), covering production BFF startup,
weak secrets, OAuth/session flow and restart, routing, MIME, security headers,
private state and legacy-tree preservation. Its prior failures exposed nginx
header-inheritance and synthetic TLS configuration mistakes, plus two test
readiness races; those corrections were folded into their unpublished owning
commits. No local Linux kernel source compilation occurred. Architect0's source
reconciliation found no additional named Nix outputs needed for the planned
BFF and documentation evidence.

The exact site head `eae98bcc` passed a build-free flake check and evaluated
the new host's NixOS 26.05 toplevel derivation against clean WebUI `f131a19`
through the local source override. All seven affected machine toplevels built
in 270 seconds (`/tmp/newadmin-site-seven-machines-clean-gate/`): the new UI
host, Prague proxy, public DNS, two internal DNS hosts and two monitors. The
rendered backend nginx listens on `172.16.9.170:80`, keeps route-owned static
CSP/BFF headers and accepts only the declared private peers. The edge has a
separate HTTP redirect and HTTPS reverse proxy to that host, with normalized
forwarding and newadmin access logging disabled. All three built public/internal
DNS zones load at serial `2026092800` with the intended records. The rendered
monitor configurations contain both HTTPS probes, BFF unit/scrape alerts and
the accepted 14-day certificate rule. No local kernel source was compiled.
Remaining gates are controlled browser and live API/CORS checks, source
publication and channel pin, and operator verification of installed host state,
OAuth secrets and frame origins. These are verification and activation
prerequisites, not confirmed code defects.

The next WebUI change, clean commit `6a7904b`, removes the obsolete jsdom
encoding patch and its shims. A fresh locked `npm ci` followed by direct,
unpatched Vitest passed 279 files/1,628 tests
(`/tmp/newadmin-webui-unpatched-dom-probe/`). Five new direct DOM regressions
cover Czech UTF-8, BOM precedence, Windows-1252, DOMParser and FileReader;
ordinary `npm test` also passed all 1,628 tests without the hook. The
normal-environment `npm run test:scripts` passed all 172 tests
(`/tmp/newadmin-webui-dom-scripts-clean-gate/`); six pre-existing script
fixtures could not run in the implementer's sandbox because loopback or child
process operations returned EPERM there. No runtime dependencies or lockfile
changed for this slice. The architect recorded the remaining lint/type/browser
scope in `design.md`.

The scoped lint/format change is committed at clean WebUI head `229f57a`.
Eight bootstrap, auth, hook and UI files are adopted; 74 other eligible files
remain recorded by exact source hash with an owner and adoption condition.
Changed or newly eligible source cannot remain deferred, including in a
Gitless archive. ESLint checks React Hooks and focused accessibility rules;
Prettier checks the adopted files and new tooling. The root-only development
graph added five exact tool pins and changed the frontend dependency SRI to
`sha256-q4Xy2p/fhQ9PrI2CQJE4vWRe/jObemXdOSGeBgEYwxI=`; the BFF graph and
hash are unchanged. Six focused gate fixtures passed, and the exact clean head
passed locked `npm run ci:quick` in 84 seconds
(`/tmp/newadmin-webui-scoped-quality-quick-retry/`). A first watcher never
started npm because `/usr/bin/time` was absent; its exit 127 is a wrapper
failure, not a check failure. The retained read-only reviewer was assigned but
again returned no report. The previously verified independent standalone
reviewer, using the installed default review-purpose Sol/xhigh policy,
completed general, architecture, scope and risk review of `f131a19..229f57a`:
no Blocking, Important or Advisory finding, and no migrations. Risk was medium
because the root package dependency hash changes while the runtime contract
and BFF graph do not. The reviewer confirmed the patch hook is fully removed,
the adoption gate works in a Gitless archive, and the lock adds only dev
packages without changing existing versions. Exact-head full nonbrowser tests
and x86_64 package checks followed that review. The exact clean-head six-target
Nix batch passed in 76 seconds (`/tmp/newadmin-webui-scoped-quality-package-gate/`):
frontend, BFF, module evaluation, provenance, source contents and installed
package contents. This resolved the optional WASI prefetch uncertainty for the
tested x86_64 build. Exact-head locked `npm run ci:tests` then passed in 53
seconds (`/tmp/newadmin-webui-scoped-quality-tests-gate/`): 279 Vitest files,
1,628 tests and the BFF suite (47 passing) completed with no failure. The next
code slice is tooling/E2E type coverage in the same canonical checkout.

The initial all-E2E strict TypeScript probe exposed 231 diagnostics across 75
files; disabling two useful strict flags still left 90 across 29 files. The
implementer removed the draft config rather than weakening the gate. A narrower
tooling-only commit `16a9018` now checks Vite and Playwright configuration and
all `build/**/*.ts` files with strict no-emit TypeScript. It resolves 23
index-signature env accesses without behavior change and includes compile-only
negative fixtures. Root development declarations now match Node 24
(`@types/node` 24.19.0); the new frontend SRI is
`sha256-1AItkFu1tvJpKjFVbGC/IWky4JPfw+d+XU50egk+/TE=`, while BFF remains
unchanged. The exact clean head passed locked `npm run ci:quick` in 76 seconds
(`/tmp/newadmin-webui-tooling-types-quick-gate/`). The same independent
fallback reviewer completed general, architecture, scope and risk review of
`229f57a..16a9018`, finding no Blocking, Important or Advisory issue and no
migrations. Its exact-head six-target Nix package/content/module batch passed
in about 90 seconds (`/tmp/newadmin-webui-tooling-types-package-gate/`), proving
the refreshed root hash on x86_64. The architect recorded a
staged, zero-error E2E core proposal in `design.md`; the lead accepted its
initial 11-file checked boundary and explicit 228-file deferred inventory.
The corresponding commit `eed0060` is clean and passed exact-head locked
`npm run ci:quick` in 93 seconds
(`/tmp/newadmin-webui-e2e-core-quick-gate/`), reporting 11 checked and 228
deferred E2E files. Browser-free router and negative type/coverage fixtures
passed locally. The separate full strict diagnostic still exits nonzero with
198 diagnostics in 68 files and is not represented as passing coverage. The
same independent reviewer completed all four lanes with no Blocking,
Important or Advisory finding. It independently checked all 228 baseline
hashes against parent source, the import closure and mock behavior, accepted
the distinct immutable-baseline/live-inventory roles, and found no migrations.
The exact clean head then passed locked `npm run ci:tests` in about 70 seconds
(BFF 47/47 and Vitest 279 files/1,628 tests) and a six-output Nix package,
module, provenance and content batch in about 73 seconds. Full evidence and
store paths are under `/tmp/newadmin-webui-e2e-core-tests-package-gate/`.
The Playwright-pinned Chromium 149.0.7827.55 download completed, but its
generic Linux headless executable exited 127 on NixOS before any application
assertion. Repeating the two adopted smoke specs with an explicit Nix-store
headless executable at the same Chromium version passed all three cases with
one worker and no retries in 17.4 seconds
(`/tmp/newadmin-webui-e2e-core-focused-nix-browser-gate/`). This is a mocked
local Vite/legacy-fixture check, not proof of the packaged BFF or live API.
The reusable environment explanation is in
[the Playwright NixOS note](../../notes/vpsadmin-webui/2026-09-28-playwright-nixos-browser.md).
Full E2E typing and broader desktop/mobile browser suites remain.
The first BFF static-contract commit `ec084d4` checks the session queue with
strict CommonJS `checkJs`, a local cookie-signature declaration and negative
compile fixtures. Its pre-edit three-root inventory found 109 diagnostics:
64 in runtime-config, 38 in security and seven in the queue. Runtime-config
imports security; those modules and `server.js` remain explicitly unchecked.
The queue commit changes no production dependency graph or session format. On
its clean exact head, locked `nix develop --command npm run ci:quick` passed in
99.802 seconds, including six BFF type fixtures
(`/tmp/newadmin-webui-bff-queue-quick-gate/`). The retained reviewer0
(Sol/xhigh/read-only) was assigned all four mandatory review lanes because
the checked queue also controls session response release, but did not return
a report; this repeats earlier nonresponse in the session. The installed
default-team review-purpose Sol/xhigh standalone fallback completed all four
lanes. It found no Blocking, Important or Advisory issue: receiver, arguments,
return and release order are preserved; the declaration matches
cookie-signature 1.0.7; the one-commit split and partial-coverage docs are
coherent. There are no migrations in this unit. This incremental review does
not replace final whole-branch review. Full BFF runtime and package checks
then passed: locked `npm run ci:tests` in 69 seconds (279 Vitest files,
1,628 tests, including the BFF suite) and the six-output frontend/BFF package,
content, provenance and module-eval batch in 74 seconds. Evidence is under
`/tmp/newadmin-webui-bff-queue-runtime-package-gate/`. The HTTPS VM fixture
will be rerun with the final application candidate.
The browser-runner commit `ee04abc` fixes two workers in Playwright config and
both PR desktop/mobile commands, while preserving an appended one-worker
diagnostic override. All three browser workflows now upload reports and
retained failed-attempt results on completion, including a green retry; the
existing artifact retention and browser pin remain. A browser-free contract
test checks the pinned CLI parser and workflow conditions. Locked exact-head
`npm run ci:quick` passed in 101.785 seconds
(`/tmp/newadmin-webui-browser-runner-quick-gate/`). Retained reviewer0 did not
return after its all-lane assignment; the installed default-team review-purpose
Sol/xhigh fallback completed all four lanes with no Blocking, Important or
Advisory issue. It confirmed pinned Playwright 1.61.0 retains failed-attempt
traces in separate retry directories, the appended one-worker CLI override and
unchanged artifact retention. Its direct contract test passed 2/2. Actual CI
retry artifacts remain unverified. On clean `ee04abc`, the five representative
historical failures passed with one worker, zero retries and matching NixOS
Chromium 149.0.7827.55 in 37.2 seconds
(`/tmp/newadmin-webui-browser-focused-five-gate/`). The full desktop and
mobile PR selections then ran separately at the new two-worker default with
zero retries, using the same pinned-version NixOS browser. Desktop finished
372/378 in 22.4 minutes; mobile finished 300/303 in 18.5 minutes. Logs,
screenshots, traces and reports are under
`/tmp/newadmin-webui-browser-{desktop,mobile}-pr-gate/`. Six distinct failures
remain: both projects miss a PTR dialog after the fixture supplies only a list
response; both projects have two `page=1` assertions even though the current IP
page intentionally removes unsafe URL cursors; and three desktop forced-stop
task assertions still expect `Stop` where the approved fresh tracking label is
`Poweroff`. All six failed again in one focused desktop run with one worker and
no retries (170 seconds; `/tmp/newadmin-webui-browser-six-repro-gate/`), so
they are deterministic contract mismatches, not load-only observations.
Implementer0 folded the fixture corrections into the unpublished host/IP and
VPS power introducing commits in the original checkout. The later E2E coverage
introducing commit was amended to bind the four corrected deferred specs at its
rewritten source parent; the 11 checked/228 deferred paths and compiler rules
are unchanged. The clean rewritten WebUI head is
`fa35d797095881a016462b0aab22fbfe927e4727`. `git range-diff` maps the
twelve affected commits one-to-one, with only those three introducing patches
changed. Old-final to new-final touches four E2E specs, their coverage
runner/inventories and two owning documents; `src/`, `bff/`, packages, NixOS
module and dependency locks are byte-identical. The four new spec hashes match
both inventories. Cached-toolchain E2E coverage and focused script checks pass.
The exact-head locked `nix develop --command npm run ci:quick` passed in
97.692 seconds (`/tmp/newadmin-webui-browser-rewrite-quick-gate/`). Retained
reviewer0 accepted the four-lane incremental review packet but did not return
a report. The installed default-team review-purpose Sol/xhigh standalone
fallback reviewed general, architecture, scope and risk lanes on the clean
`fa35d79` head and found no Blocking, Important or Advisory issue. It confirmed
the twelve-commit one-to-one history mapping, exact baseline hashes at parent
`dfe86c0`, preserved API/filter/force assertions, and no migrations. The review
did not run a browser. Focused one-worker/no-retry reruns on `fa35d79` passed
five of six desktop and two of three mobile cases in about one minute and 46
seconds respectively (`/tmp/newadmin-webui-browser-rewrite-focused-gate/`).
Both remaining failures are the same IP exact-login case: the fixture expects
an API batch limit of 25, but the admin page requests 250 for its ascending-ID
inventory while URL `limit=25` controls only visible local pagination. Later
assertions in that fixture also expect 50. Read-only source inspection found
its untagged first test still modeled descending keyset behavior and expected
no ascending order, conflicting with the current page. Implementer0 folded a
bounded correction into the unpublished host/IP introducing commit: a 275-row
ascending fixture proves the 250+25 API traversal, cursor on the second API
request, local Next without a new request or URL cursor, exact address filter
and page reset. Four later API-limit expectations now use 250 while URL
display-limit checks remain 25. The later E2E coverage introducing commit
rebinds only this spec hash, baseline digest and rewritten source parent;
11 checked/228 deferred paths and compiler rules remain unchanged. Old-final
`fa35d79` to clean new head `0d9d5791a07d8a02d905ce34f12666b847818492`
differs in six test/documentation/coverage files, with no runtime or site
change. Exact-head locked `ci:quick` passed in 95.96 seconds
(`/tmp/newadmin-webui-ip-fixture-quick-gate/`). The same independent Sol/xhigh
reviewer completed a targeted general/architecture/scope/risk rerun on
`0d9d579` with no Blocking, Important or Advisory finding, confirming the
two amended introducing commits, realistic two-batch mock and 228 valid
deferred hashes. Focused browser runs then passed the changed IP tests on
desktop 2/2 in 40.8 seconds and mobile 1/1 in 28.4 seconds
(`/tmp/newadmin-webui-ip-fixture-focused-browser/`). The full two-worker PR
selections then passed on the same clean head, desktop 378/378 in 21.7 minutes
and mobile 303/303 in 18.3 minutes, with no retries
(`/tmp/newadmin-webui-browser-final-pr-gate/`). All 29 cases in the initial
browser-failure inventory were selected and passed in the desktop suite.
No product defect was established by the observed limit mismatch. A real
passing-retry CI artifact has not been observed. See
[browser-failures.md](browser-failures.md) for the controlled-run details.
Architect0 recorded the separate packaged HTTPS/BFF browser brief in
[design.md](design.md). Implementer0 committed its test-only NixOS VM check at
`b119e7a13ab316ec28efba87d1b721664080c7bf` in the original WebUI checkout.
The one-commit diff has twelve test/build/documentation paths and no product,
module, site or dependency-lock change. Local Python fixture tests, Node/Nix
syntax and format, design audit and diff checks passed. The lead's exact-head
build-free evaluation produced the browser runner and both VM derivations;
all ten module results were true and `nix flake check --no-build` passed with
import-from-derivation forbidden. The browser runner directly selects Node 24,
Playwright core 1.59.1 and a browser farm that links only Chromium headless
shell revision 1217; the ordinary VM derivation has no direct browser input.
Neither the runner nor the new VM check has been realized or executed. The
retained reviewer0 did not return a report after assignment, consistent with
earlier attempts; the installed default team's independent Sol/xhigh fallback
completed all four mandatory-review lanes on `b119e7a`. It found two Important
test gaps: the initial browser runner accepted HTTP 200 failed HaveAPI envelopes while
page containers remain visible, and Retry can pass without a second config
request. An Advisory finding asked the locale flow to switch back to English
through the UI. Implementer0 folded all three assertion fixes into the
unpublished introducing commit, yielding clean `59519f8`. New focused Node
observation tests pass 3/3 under locked Node 24.21; direct Python fixture tests
pass 3/3. The exact amended runner derivation evaluates at
`/nix/store/knbbk5ni979zahyy2sfchs0ap9s1g8q1-webui-browser-smoke.drv`,
and the flake no-build check passes with IFD forbidden, including the amended
browser VM derivation. The same independent reviewer found all three gaps
resolved and no new findings in the affected lanes; the helper is bounded to
this test with focused contract/waiter coverage. A fresh watcher realized the
runner at `/nix/store/0vmwby37znjs583ql7vr15qv89bisfkg-webui-browser-smoke`
in 33.5 seconds. Its recursive closure is 612.2 MiB and contains Node 24,
Playwright core 1.59.1 and only Chromium headless shell revision 1217 among
browser outputs; no Firefox, WebKit, ffmpeg or full Chromium browser appears.
The wrapper records clean frontend/BFF provenance `59519f8`. The first new VM
run failed after 216 seconds before the UI flow: the runner asserted that
`chromium.executablePath()` exists, but Playwright's API reports the default
full-Chromium path while this check deliberately packages only the headless
shell. The selected headless-shell binary exists and reports the expected
147.0.7727.15 version. Implementer0 removed only the false path assertions
and unused import in the unpublished owning commit, yielding clean `1b08cb9`.
The lead confirmed the three-file old/new diff, locked Node syntax and
3/3 observation tests. The second VM run reached the anonymous browser phase
but failed after 240 seconds; its safe log listed a failed `/session.json`
request and a failed `/api/v7.0/system_configs/webui/goresheat_url` request.
The latter is an unconditional public Overview read registered by pinned
vpsAdmin but omitted from the synthetic fixture. Implementer0 added only that
exact route plus allowlisted browser network-failure classes in clean `39f8e4b`.
Normal-environment focused tests pass: 4/4 Node observations and 3/3 Python
API fixtures. The third VM run failed after 195 seconds in the grouped healthy
desktop anonymous-bootstrap step. It reported only `Error`, without a
request-failure, API-response or bootstrap-failure class; its log is
`/tmp/newadmin-webui-browser-vm-third-gate/build.log`. The earlier curl, BFF,
TLS, session and state assertions passed before the browser step. The runner
currently groups navigation, visible overview, config/session reads, required
public API observations, visible statistics and language under one diagnostic
label. Implementer0 added bounded, credential-free labels to distinguish
these assertions. Clean `1fd75ff` contains only these
test diagnostics and documentation changes; the locked four-case observation
suite and exact-head no-build flake check pass. A fresh watcher's fourth attempt
failed before starting Nix because it ran in the parent worktree directory,
which has no flake. The next watcher ran from the verified WebUI checkout; its
fifth attempt reached the healthy desktop browser flow and failed after 229
seconds at `anonymous_vps_stat`. All five required public reads succeeded once
and the Overview was present. Source inspection found two exact visible `0`
values in the VPS card: the main VPS count and the free-IPv4 badge. A strict
locator ambiguity is likely, but not yet proven. That run separately recorded
`/session.json: net::ERR_ABORTED`; implementer0 is determining its timing and
role before any suppression. The full log is
`/tmp/newadmin-webui-browser-vm-fifth-gate/build.log`. The ambiguous selector
is now scoped to StatCard's numeric value in clean `225d7cf`, based on source
proof of the duplicate zero. The session abort remains a failing event; the
runner now records only fixed request stages, response/finished flags and
counts for that path. Exact-head locked observation tests pass 4/4, API fixture
tests pass 3/3. A
first watch attempt stopped before Nix because the lead's Python fixture test
generated one untracked bytecode file; the lead removed only that artifact and
verified a clean checkout. The next watcher passed the exact-head no-build
flake check in 70 seconds and reached the final healthy desktop assertion in
the packaged VM after 273 seconds. The UI login, dashboard, news, language
switching and logout steps completed, but the accumulated error list contained
aborted `/config.json` and `/session.json` requests and one failed
`/api/v7.0/webui_user_settings` request. The missing settings route's
unknown-route response omitted CORS, explaining the likely `ERR_FAILED` cause.
Implementer0 amended the unpublished browser commit to clean `b2825e7` with
the pinned authenticated settings Index response, exact namespace/key filters,
token/CORS checks and a seeded current-user `ui/settings` record. An empty
list would have triggered WebUI's 500 ms default-save PUT, which the read-only
fixture rejects; the seeded record avoids that unintended test path. Focused
Python fixture tests pass 4/4, Node observation tests 4/4 and UI settings tests
5/5 using cached Node 24.19. Architect0 recorded a bounded request-completion
design in `design.md`; implementer0 is adding it without an `ERR_ABORTED`
exception or timeout change. Full prior VM log:
`/tmp/newadmin-webui-browser-vm-seventh-gate/build.log`.
No product failure is established; no timeout or TLS assertion has been
weakened. The review found no production compatibility change, obsolete
iteration or migration.
The packaged-browser introducing commit is now clean at `9a6cc92`. Its
request ledger tracks exact Playwright Request objects, checked response bodies,
terminal completion and document epochs; `requestfailed` remains fatal. Exact
head pinned Node 24.21.0 ledger tests passed 10/10, the Python HaveAPI fixture
passed 4/4, Prettier and the design-doc audit passed, and locked `ci:quick`
passed in 109 seconds (`/tmp/newadmin-webui-request-ledger-quick-gate/`).
Incremental independent review used the installed standalone Sol/xhigh fallback
after retained reviewer0 did not return a report. The general, architecture,
scope and risk lanes found one Important gap: an unexpected API request could
remain pending after the ledger's allowlisted GET drain and escape final
acceptance. They also found an Advisory false-failure possibility for a second
filtered settings-key read, because the response audit expects the seeded row
for every successful settings response. Implementer0 is correcting the Important
issue in the same unpublished introducing commit and examining the bounded
Advisory fix. The browser VM remains on hold; no production behavior or
migration changed in this unit.
The amended clean head is `6fb10e1` over the same parent. Every API request
now enters the exact-Request ledger at issuance; unknown routes and mutations
raise a fixed-class failure immediately and remain subject to terminal drain.
Only exact reviewed provider-origin OPTIONS can succeed with 204. Settings
responses are compared using the fixture's namespace/key filters; only the
completed seeded `ui/settings` GET satisfies the required shell read. Following
architect0's design clarification, each authenticated `/app` document has a
named 1,000 ms browser-context observation after dashboard visibility, the
selected completed settings read and first drain, followed by another drain.
This targets the product's 500 ms save debounce with a scheduling margin;
public/news documents have no such interval. Pinned Node 24.21.0 focused
tests passed 18/18, including a PUT at 750 ms, pending unknown GET/PUT, late
reviewed GET, document change and filter cases; Python fixture tests passed
4/4. The same independent reviewer reassessed all four affected lanes and
found no remaining issue; both prior findings are closed within the bounded
test contract. The exact-head locked `ci:quick` passed in 91 seconds at
`/tmp/newadmin-webui-request-remediation-quick-retry/`. The first watcher
attempt did not run because its wrapper called unavailable `/usr/bin/time`; it
was retried with a fresh watcher and unchanged source. The packaged browser VM
failed on this head after 231 seconds
(`/tmp/newadmin-webui-browser-vm-remediation-gate/build.log:605`). Desktop
reached `anonymous_public_reads` with all five required public API reads
successful and the overview visible, but global request ordinal 2, a session GET
in document epoch 1, started at the `anonymous_overview_visible` stage, received 200 headers and
then failed with `net::ERR_ABORTED`; the body classifier recorded
`session_contract_invalid`. One of two session requests finished. No deliberate
test navigation is evident between that start and failure. The failure remains
fatal; ordinal 2 does not mean it was the second session request. Architect0
and implementer0 investigated its ownership and timing read-only.
Architect0's source review found that two config and two session requests are
expected from application bootstrap plus explicit runner probes. Global request
ordinal 2 could be the bootstrap session request, but ownership remains
unproved. Application bootstrap reads the entire session body before rendering
React; the normal anonymous path has no token refresh or success-path abort.
The runner's old `session_contract_invalid` also covered a failed DevTools body
retrieval and did not prove malformed BFF JSON. The bounded diagnostic design
is in `design.md`. Implementer0 folded a test-only diagnostic into the same
unpublished introducing commit, clean WebUI head `35a8ad8`: explicit probe
Request identity without changing headers, fixed config/session event timeline,
safe runtime/selector booleans and separate retrieval, syntax and schema
failure classes. Request failures remain fatal. Pinned Node 24.21.0 focused
tests passed 22/22 and the Python fixture passed 4/4. The exact-head quick gate
passed in 107 seconds at `/tmp/newadmin-webui-abort-diagnostic-quick-gate/`.
Independent review found one Important diagnostic attribution flaw: the helper
could label a same-path candidate as `runner_probe` before confirming the exact
Playwright Request identity. Implementer0 folded the narrow fix into clean
head `5ae5898`: one predicate supplies both candidate selection and request
wait, and ownership changes only after identity confirmation. Timeout and
mismatch leave candidates unconfirmed and emit fixed classes. The pinned focused
suite passed 25/25, including wrong-origin, wrong-method, child-frame, timeout,
mismatch and hostile-redaction cases. The lead inspected the exact diff as a
narrow review remediation; the diagnostic VM result follows.
That exact-head VM failed after 236 seconds
(`/tmp/newadmin-webui-browser-vm-attribution-gate/build.log:605`). Desktop
reached `login_member_reads`: the dashboard was visible and all required member
API reads succeeded, but a config GET in document epoch 2, global ordinal 12,
started during `login_dashboard_visible`, received 200 headers and then failed
with `net::ERR_ABORTED` and `config_body_retrieval_failed`. All four session
requests finished. At that head, the safe detailed timeline printed only on
anonymous failure, so ownership/event order of the authenticated config
request remained unknown. This neither proves malformed BFF JSON nor justifies
accepting the abort. Architect0 allowed one bounded diagnostic correction and
one more VM run. The same unpublished commit was amended at `4419d48` to print
the existing sanitized config/session timeline on authenticated failure; pinned
focused tests passed 28/28 and the locked `ci:quick` gate passed in 92 seconds
(`/tmp/newadmin-webui-auth-timeline-quick-gate/`). Its single VM rerun failed
after 254 seconds (`/tmp/newadmin-webui-auth-timeline-vm-gate/build.log:605`).
Login document epoch 2 completed config, session and member reads. After the
runner requested a dashboard reload, epoch-3 config request 26 and session
request 27 each received HTTP 200 headers, then `net::ERR_ABORTED` and failed
DevTools body retrieval. Both are main-frame JSON fetches; the diagnostic does
not establish the cancelling actor, malformed BFF JSON or a production contract
failure. The architect's [scope checkpoint](design.md) therefore recommends
deferring this optional automation instead of adding more CDP or exceptions.
The lead accepted that decision. Implementer0 dropped the entire unpublished
top commit `4419d48` by interactive rebase; the original WebUI branch is clean
and byte-identical to its parent `0d9d579`. The prior ordinary HTTPS curl VM,
package/module/site builds and complete desktop/mobile PR browser suites remain
separate passing evidence. They do not certify a browser running the immutable
BFF-mode package through both proxy hops. The failed VM logs and required
manual HTTPS/bootstrap/login/logout checks remain part of the handoff; the
observed abort is an unresolved coverage risk.

The final whole-branch mandatory review covered all 19 WebUI commits and all
four patch-equivalent rebased site commits, across general, architecture,
scope and risk lanes. The retained `reviewer0` (Sol/xhigh/read-only) again did
not return a report after a session-bound assignment; the installed default
team's review-purpose Sol/xhigh role ran as fresh standalone
`/root/final_whole_branch_review`. It found one **Important** issue: the edge
and private backend suppress OAuth access logs but inherit nginx error logs,
which can include `/oauth/callback` query values on proxy failures; the site
runbook overstates the guarantee. It found no other Blocking or Important issue,
no obsolete unmerged approach or fixup-only commit, no unused compatibility
path, and **no database or schema migrations**. The deferred packaged-browser
VM is an activation coverage gap, not evidence of a product defect or a pass.
The architect is designing a bounded logging fix for both nginx hops and the
generated HTTP redirect. The rebased site head still needs affected-machine
builds after that fix.

The new `vpsfreecz/vpsadmin-webui` origin was empty before publication. Kerrycek upstream
advanced seven commits after adopted base `e7ce3d7` to `156a7c0`, changing
the paused issue-runner trust policy and documentation/work-log structure but
not `src/`, BFF, Nix packages/modules, manifests or workflows. Architect0's
[baseline decision](design.md) recommends initializing the new origin's `main`
from the exact adopted base, then publishing the feature branch separately.
This preserves reviewed ancestry while deferring upstream's issue-runner and
per-change log integration as a separate follow-up; the two branches also use
`REQ-067` for different subjects. Never resume the inherited issue runner
without reconciling its later trust policy. The lead accepts this baseline
recommendation. After the user's explicit authorization to push development
branches, exact base `e7ce3d73e799fc60e5933fe23bdb3a979eb4d6b9` was
pushed as the new origin's `main`; `git ls-remote --symref` verified both the
remote default HEAD and `refs/heads/main` at that SHA. No feature content has
entered the default branch. The WebUI feature ref remains local while the OAuth
logging finding is open. The site's `vpsadmin-webui` channel must be pinned
to a published feature revision before deployment; local source overrides are
development evidence only. Before the baseline push, ordinary site `nix eval`
without that override failed with GitHub HTTP 409 because the origin had no
commit; the override-backed check passed but is not a deployable pin.
The user identified VPS 30431 as a newly provisioned NixOS container on
vpsAdminOS and directed use of 26.05. Architect0 compared the shared base/ct
imports and neighboring containers and found no further host setting to add.
Implementer0 folded `system.stateVersion = "26.05"`, removal of the temporary
false assertion and removal of the module's obsolete `stateDirectory` option
into the unpublished site commits in the original checkout. The release channel
alone does not establish the first-installed state version: neighboring hosts
on this same channel retain values from 22.05 to 26.05. The operator will
verify the initial installed release before activation; this check did not
block the development derivation evaluation. Installed
architecture and exact network/SSH identity remain activation checks;
API-returned console/frame origins also remain a deployment gate. The user
performs deployment after review, build and explicit repository integration
decisions. Keep the map call unchanged.

Architect0 prepared and reconciled `design.md`; implementer0 completed the WebUI
source/tooling, verification, BFF bootstrap and first bounded network-list/DNS
unit on the isolated combined branch at `9835d07`. The unpublished history was
rewritten in the commits that introduced temporary internal labels, with no
application-source change. Locked quick checks and production build passed on
the combined head. The first English/Czech localization pass is committed at
`29675db`; power-control labels and the two page extractions are committed at
`0576063`. The layout/lifecycle pages are 747/833 lines, below their 795/862
historical ceilings. Exactly two structural exceptions were removed, with all
41 retained entries unchanged. Focused tests passed 33/33; TypeScript, i18n,
design, structural, UI-string and related architecture audits passed in the
cached Node shell. On exact clean head `05760631352bc37b1b510e781deb5d169c63da1c`,
`nix develop --command npm run ci:quick` passed in 86 seconds and `nix develop
--command npm run build` passed in 24 seconds. Logs and status files are under
`/tmp/newadmin-localized-locked-checks/`; the locale chunk-size warning remains
non-failing. The independent reviewer is assessing the fixed primary snapshot.
The implementer committed WebUI Nix packages/provenance at `3d37236`; the architect's site
configuration brief is accepted with installed-machine facts still open.

The lead realized pinned Nixpkgs `prefetch-npm-deps` 0.1.0 from the WebUI flake
input and checked both unchanged lockfile digests. Separate dependency hashes
are `sha256-qipQBgqu4SMKocavlqdFxFugtB2UYEmgX3fRW+UKdTA=` for the root
lockfile and `sha256-imijdRISN2eVBsYX79YBxl7zKM7Pjq3rixkKXJNDSvw=` for
the BFF lockfile. Both prefetch commands passed; the root prefetch warned that
six packages lack resolved URLs. Logs are under
`/tmp/newadmin-npm-dependency-hashes/`. These hashes do not certify package
builds; the implementer applied them to the new derivations.

The package commit adds separate frontend/BFF derivations, shared full-SHA
provenance, a cleaned source audit, installed-content checks and owning package
documentation. The package-content derivation evaluates with
`allow-import-from-derivation=false`; both package provenance values evaluate
to the same clean full commit. The first evaluation exposed a deprecated
`pkgs.system` reference, which the implementer amended in the introducing
commit. No package output or closure has been built yet. On exact clean head
`3d372365eb6143db75a995386c7ddcc63f490e97`, a fresh watcher ran
`nix flake check --no-build --no-write-lock-file --option
allow-import-from-derivation false` (exit 0, 2.8 seconds),
`nix develop --command npm run ci:quick` (exit 0, 69.9 seconds) and
`nix develop --command npm run build` (exit 0, 21.4 seconds). Logs/status files
are under `/tmp/newadmin-package-quick-checks/`; the build's locale-chunk
warning is non-failing.

The architect's site brief records the metadata-only confctl rediscovery
sequence, clean exact-revision local-source override, proxy and DNS views,
both public probes, BFF unit and certificate alerts, and the seven affected
machine builds. The new VPS's installed architecture, `system.stateVersion`,
boot/network baseline and API-returned frame origins are still unverified.
The lead accepted a 14-day remaining-certificate warning for the new HTTPS
target, with focused alert fixtures and no change to existing target policy.
The new host's metadata, configuration and health-check source were staged
before the root input mapping. Normal-environment `confctl rediscover` then
completed and added exactly one sorted entry for `int.vpsadmin-webui1` to
`cluster/cluster.nix`; `cluster/netbootable.nix` stayed unchanged. An earlier
run before `config.nix` existed could not register the host because pinned
confctl requires both machine files. An earlier draft withheld host evaluation
with an intentional assertion; the user's fresh-container direction superseded
that draft without waiving the before-activation machine inspection.
With a clean exact `51c98bc` WebUI path override, the initial site flake
resolved the new machine key and mapped WebUI Nixpkgs/vpsAdmin inputs to the
intended site inputs. That initial new-host toplevel evaluation stopped at the
deliberate stateVersion assertion; it was not a passing host build. The focused
newadmin Prometheus rule check built and ran successfully (exit 0; 21 seconds),
using the staged rule fixtures. Its log is under
`/tmp/newadmin-site-prom-rules-check/`. The two endpoint-failure alert fixtures
added after that build passed a direct pinned Prometheus 3.12 `promtool test
rules` run against the rendered rules JSON.

Before its upstream rebase, the clean original site branch had four focused commits over
`1e8dae22`: `4387acbe` registers the host and input mapping; `398a2fcf` adds
the edge vhost and both DNS views; `898458e7` adds probes, alerts and fixtures;
`eae98bcc` documents installation and recovery. The 15-file final diff has
559 insertions and two deletions, no local path or `flake.lock` mutation, and
no opaque numbered work labels. The edge and monitoring patches are equivalent
to their pre-rewrite versions. Active Overcommit Nixfmt and commit-message hooks
passed on both amended commits without bypass; both zone views previously
passed `named-checkzone` at serial 2026092800. At that pre-rebase head, the
declared-shell `nixfmt --check` and build-free flake check passed with the
canonical WebUI input override. The machine key remains
`m_cz_vpsfree_vpsadmin_int_vpsadmin_webui1_03e727ba`; its NixOS 26.05 toplevel
derivation evaluates as `/nix/store/6433wpwcnm5cn8ag3vlr2md7i8zb0z8w-nixos-system-vpsadmin-webui1-26.05.20260926.5e2305d.drv`.
These checks do not certify a built or installed machine or a remote-pinned
source. The pinned nginx template shows the forceSSL HTTP redirect server is
separate and inherits http-level logging; rendered nginx inspection remains
for the reviewed machine build.

Site `origin/master` later advanced three commits to `46c6ae81` with Nix input
locks and Geminabox dependencies. The four feature commits were rebased in the
original worktree without conflicts, producing clean head `64dff866` over that
master. `git range-diff` marks every commit patch-equivalent and the complete
15-file feature diff is byte-identical; the feature still does not edit
`flake.lock`. All changed Nix files pass parse/nixfmt and diff checks. The
new upstream input locks passed exact rebased-head `nix flake check --no-build`
with the clean WebUI source override and import-from-derivation forbidden in
29 seconds (`/tmp/newadmin-site-rebased-no-build-gate/`). Machine build evidence
is still needed before publication; earlier seven-machine builds belong to the
pre-rebase input graph.

Architect0's pinned-systemd assessment found that the module's configurable
`stateDirectory` could be set to the legacy `/var/lib/vpsadmin` root. Systemd
260.4 may recursively change ownership of an existing directory before any
`ExecStartPre` safeguard. The lead accepted fixing the new BFF state name to
`vpsadmin-webui`, with no public override or change to the default path,
session format, account or secret. Implementer0 folded this into the unpublished
module-introducing commit; the corrected module is in the original WebUI
checkout at the reviewed `8814479` snapshot and was replayed patch-equivalently
at `f7d37d1`. Architect0 reconciled the design and first-activation
runbook, and the obsolete site option assignment was removed in `4387acbe`.
The committed disposable VM fixture is intended to verify synthetic legacy
state survives BFF start/restart when run after review.
The isolated VM branch now has amended module-introducing head
`58d36b1981cc21959796b21b9301fe11ba9c665f` over package head `3d37236`.
Range-diff maps the one module commit directly; only WORK_LOG, the service
guide, the module and its eval fixture differ from the fixed old snapshot.
Pinned build-free evaluation on the staged amendment passed all ten results,
including rejected override and legacy coexistence. The separate HTTPS VM
fixture is committed at clean head `600748e01caa00d06b32564fec6b2629ccac0c26`.
Its derivation path evaluated successfully with
`nix eval --raw --no-write-lock-file --option allow-import-from-derivation false
.#checks.x86_64-linux.nixos-webui.drvPath`; the exact-head
`nix flake check --no-build --no-write-lock-file --option
allow-import-from-derivation false` passed in 50 seconds
(`/tmp/newadmin-vm-no-build-check/`). Two obsolete pinned-Nixpkgs fixture
options were corrected in its unpublished introducing commit before those
checks passed. Exact-head `module-eval.passthru.results` returned ten true
fields. The prior full-suite failure and its rewritten correction are recorded
below. The VM and package outputs have not been built or run. The old module
worktree remains fixed at `51c98bc` for its existing review packet.
The runbook no longer promises that an immutable rollback retains assets from
another generation; open-tab recovery needs a controlled-reload check.

The first full pinned nonbrowser run on the fixed VM snapshot failed two Czech
assertions in `HostIpLookupInput.test.tsx` because the real lazy catalog had not
loaded before the tests' default assertion deadline. A pinned focused run
reproduced the failure without suite load; preloading the real catalog in the
test passed all ten focused cases at the original timeout. Implementer0 amended
the original unpublished host-IP/DNS commit in a separate registered worktree
and replayed six commits without conflict. `git range-diff` maps all six 1:1;
the old-final versus new-final tree differs only in the test (+2 lines) and
its owning work-log entry (+5 lines). No application source, catalog, lock,
module or site behavior changed. The clean resulting head is
`881447938feb30f32d991692f495811e4d15ac8c`.

On that exact head, the pinned Nix shell passed root and BFF `npm ci`,
`npm run ci:tests` (279 files, 1,628 tests), `npm run ci:quick`, and
`npm run build`; Nix `flake check --no-build --no-write-lock-file --option
allow-import-from-derivation false` and `module-eval.passthru.results` also
passed (all ten assertion fields true). All seven sequential commands exited
zero, and the worktree remained clean. Logs, exact per-command status and
elapsed time are under `/tmp/newadmin-reconcile-locked-gates/`. These are unit,
build and evaluation gates, not package-output or VM runtime evidence.

The package branch remains fixed and clean at `3d37236` for independent review.
Implementer0 committed the reusable NixOS service module on its separate clean
worktree at `51c98bcaedeacdf42e64db43af85d32545d8c476`. The module is
disabled by default, separates its BFF account from the legacy PHP account,
requires a runtime secret-file path, binds the BFF to loopback and nginx to an
explicit private address, and defines peer/forwarding checks and static/BFF
routes. Its fixture imports the actual locked vpsAdmin PHP module to check
coexistence. On the exact module head, pinned Nixpkgs evaluation returned all
nine fixture results true; `nix flake check --no-build --no-write-lock-file
--option allow-import-from-derivation false` passed. Initial locked `ci:quick`
and production-build commands could not start because this isolated worktree
had no `node_modules`; `nix develop --command npm ci` then passed. On the same
exact clean head, `nix develop --command npm run ci:quick` passed in 72.4
seconds and `nix develop --command npm run build` passed in 22.9 seconds.
Logs and status files are under `/tmp/newadmin-module-node-quick-checks/`.
The build retains a non-failing locale chunk-size warning.
Full package/VM builds and site configuration checks still wait for independent
review and implementation. The primary review snapshot remains unchanged.

The canonical WebUI origin still advertises no branches. The rejected late
wording-cleanup commit was folded into the unpublished commits that introduced
the relevant text, leaving six descriptive commits at `38db062`. The BFF and
frontend source trees match the primary review snapshot at `1949f28`
byte-for-byte. All 43 accepted structural-ledger records retain their protected
fields; their content hashes match upstream source `e7ce3d73`, now recorded as
their source revision. No migrations exist. Reviewer0 is assessing that fixed
primary snapshot in general, architecture, scope and compatibility/security
lanes. The primary checkout remains unchanged until the review reports.

Two network-list commits were rebased onto the rewritten history at `9835d07`.
Range-diff confirmed the loader patch unchanged and the page/DNS patch changed
only in its work-log wording; the application source patch is byte-identical.
On that exact combined head, `nix develop --command npm run ci:quick` passed in
85.8 seconds and `nix develop --command npm run build` passed in 34.8 seconds;
logs and status files are under `/tmp/newadmin-rebased-w4-locked-checks/`.
The lead scanned every changed WebUI text file and commit message for opaque
numbered labels and found none. Focused loader fixtures include 250+50 rows
with the same filtered total count on both pages and signal-aware timeout.
The DNS lookup verifies IDs outside its suggestion sample and rejects stale
PTR filter/identity results. The build still warns about language chunks over
500 kB. Browser/live-API checks and independent review remain open. No WebUI
branch has been pushed, merged or deployed.

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
  Repository setup commit `f89a33a` adds the pinned `vpsadmin` input, Node 24 dev shell,
  localization instruction route, canonical repository identity and source
  handbook/work-log updates. Verification repairs culminate in `850d380`; BFF public
  runtime configuration/startup validation is `d0806be`; required frontend
  bootstrap is `38db062`. No site configuration is changed yet.
- Configuration feature worktree:
  `worktrees/2026-09-27-newadmin-integration/vpsfree-cz-configuration`, branch
  `2026-09-27-newadmin-integration`, base `1e8dae229fbe4201b5e1f110721f0f63c4b46944`.
  `dev-session worktree add` created and registered it, then returned nonzero
  because the checkout hook needs gems from its Nix development shell. The
  branch and worktree are clean; future commands must use the declared shell.
- Isolated WebUI correctness worktree:
  `worktrees/2026-09-27-newadmin-integration/vpsadmin-webui-w4`, branch
  `2026-09-27-newadmin-integration-w4`, created clean from the review snapshot
  `1949f28`. It keeps the primary WebUI review worktree fixed at that revision.
  Before integration, reconcile any reviewer fixes into the correctness branch
  and consolidate it into the primary feature branch with a reviewed final diff.
  The first unit covers proven host/effective-admin IP ascending-ID traversal.
  Lead accepted replacing unsupported host `q` with exact `addr` filtering and
  visibly resetting legacy `q` URLs, keeping admin server order `asc`, treating
  suggested-free-IP results as samples, and gating the `user` filter by the
  effective API role. Implementer0 made a loader/tests commit and a page/copy
  integration commit. The affected `HostIpLookupInput` DNS-transfer consumer
  also sends unsupported `q` and has a 100-row eligibility sample; the lead
  asked for a bounded exact-address lookup with the same eligibility filters,
  explicit sample limits and no inferred ineligibility. Commits `7bf1ca9` and
  `9835d07` implement and test this first unit, including authoritative
  direct-ID eligibility checks; all other unordered network collections remain
  later work.
- Isolated WebUI history-rewrite worktree:
  `worktrees/2026-09-27-newadmin-integration/vpsadmin-webui-history`, branch
  `2026-09-27-newadmin-integration-history`, created clean from `1949f28`.
  The amendments are complete at `38db062`. Reviewer0 retains the unchanged
  primary snapshot, and the network-list branch has already been rebased over
  the amended history. The lead will reconcile reviewer findings before final
  consolidation and whole-branch review.
- Isolated WebUI module worktree:
  `worktrees/2026-09-27-newadmin-integration/vpsadmin-webui-module`, branch
  `2026-09-27-newadmin-integration-module`, created clean at package head
  `3d372365eb6143db75a995386c7ddcc63f490e97`. It is registered in
  `portal.yml` and owned by implementer0 for the reusable service module and
  focused Nix evaluation fixtures while reviewer0 assesses the fixed package
  branch.
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
- Frontend bootstrap uses an explicit BFF production build mode; standalone production builds
  require an explicit legacy selection. The BFF session response is authoritative.
  A valid anonymous response clears stored standalone credentials and
  impersonation state. An impersonation token created in BFF mode is usable after
  reload only while its recorded noncredential BFF session fingerprint matches
  the current authenticated session; a fresh login or logout cannot resurrect a
  prior operator's impersonation. Standalone mode retains its existing behavior.
- Bound impersonation must use the API token-provider header; the
  BFF's configured OAuth header is not valid for that provider. BFF logout
  does not revoke a separately issued API impersonation token, and an already
  running tab may retain it until revalidation. Do not claim instantaneous
  cross-tab revocation from the bootstrap fix. Treat this as a preview-use
  limitation and design a follow-up before full cutover readiness.
- For collection pagination, display explicit incomplete state where the pinned
  API's ordering/cursor does not prove lossless traversal; do not claim complete
  totals or silently page by an unsafe cursor.
- The localization pass must distinguish graceful Shutdown/Vypnout from forced
  Poweroff/Vynutit vypnutí in both VPS power controls. Both owner pages have
  exact-hash inherited structural exceptions. The lead chose a focused
  extraction that brings each modified page back to its historical line count
  and removes those exceptions; rehashing modified pages as inherited source
  would invalidate the ledger's provenance. The implementer is preparing this
  as a separate behavior/refactor commit with rendered toggle and payload tests.
- Architect0's pinned HaveAPI/API inspection established that `from_id` alone
  does not order results. Lead accepts bounded client behavior and initial
  250-row/20-request/5,000-row, 10-second request/30-second overall budgets:
  traverse only proven ascending host-IP and effective-admin IP routes;
  identify member/interface/history/accounting and other unproven collections
  as partial and gate controls that require complete membership. No backend
  API/schema change is included; see the matrix and tests in `design.md`.
- The new host needs the `os-staging` channel because its container profile
  resolves `vpsadminos`, even though it runs no local vpsAdmin service.
- Lead accepted architect0's packaging account separation: the new BFF runs as
  `vpsadmin-webui-bff`, because the pinned legacy PHP module already uses
  `vpsadmin-webui`. The service name, Nix option namespace, cookie, secret path
  and `StateDirectory=vpsadmin-webui` remain as planned. No account migration is
  needed because the new service has never been deployed.
- No default-branch feature integration, production deployment or
  existing-interface cutover is authorized. Publication was initially blocked
  while the canonical origin was empty. Main now contains only the adopted
  upstream baseline `e7ce3d7`, and the verified branch-only push published the
  WebUI feature without changing main. The configuration channel now locks that
  published feature revision; final remote-lock site builds passed.
- Read the canonical [vpsAdmin WebUI KB change workflow](https://github.com/vpsfreecz/vpsfree-kb-contracts/blob/master/docs/webui-change-workflow.md)
  for visible-copy impact.
  Its current contract and captures pin the legacy `vpsadmin` WebUI, so they do
  not certify new React preview labels or screenshots. The early bootstrap failure-copy
  change has no existing documented semantic action identified here. Network-list and localization
  visible controls need a separate binding/impact assessment before claiming
  documentation parity. No KB staging or production write is authorized or run.
- Repository setup quick checks reported by implementer: cached Node 24.19.0 `env:check`,
  lint, typecheck, production build and active-docs audit; Nix parse/format,
  lock metadata and whitespace checks. In the lead's normal environment,
  `nix eval` resolved the locked input revision to
  `a65a4dfeb92a59df4a80a737a20bcbf8558793ff` and its store path;
  `nix develop --command node --version` returned v24.21.0; and
  `nix develop --command npm run audit:design-docs` passed (17 documents,
  66 requirements, 256 routes, 63 API modules). These validate source setup,
  not package builds or the new service.
- Catalog integrity commit `3f63bbd` replaces the old regex audit with a TypeScript AST
  validator across literal catalogs, detects duplicate keys and unsupported
  constructs, checks en/cs keys/placeholders/plural groups, removes the
  conflicting duplicate and fixes the rendered IP-count argument. Implementer
  reported focused audit, fixture tests, rendered en/cs test and typecheck
  passing. The lead's normal-environment `nix develop --command npm run
  audit:i18n` also passed, reporting 8,164 keys in each language.
- Verification tooling commit `a821c8c` adds deterministic source enumeration for the design
  audit, a distinct browser-script bucket, locked Node/npm/Playwright checks,
  and explicit production-build and independent desktop/mobile CI jobs. The
  implementer's fixture/YAML checks passed. In the lead's normal environment,
  `nix develop --command npm run env:locked` passed with Node 24.21.0/npm
  11.19.0 and `nix develop --command npm run audit:design-docs` passed with
  17 documents, 66 requirements, 256 routes and 63 API modules. `ci:quick`
  remains red on inherited structural debt and three UI-string test-fixture
  strings; the structural-debt repair owns those exact findings.
- Architect0's verification brief inventories the inherited structural debt at the source baseline:
  892 casts, 63 files over 500 lines and seven over 1,000, with 44 per-file
  violations. The lead accepts a separately reviewed, exact-path/rule/content-
  hash exception ledger for inherited debt only, provided it preserves the
  historical baseline, fails on stale or changed entries and exposes raw
  failures separately. No blanket baseline rewrite or silent suppression is
  accepted. The verification repair must make CI checks coherent and the design audit safe for
  `.git`-less Nix/archive sources, then supply focused quick-check evidence.
- The structural-debt repair produces a complete machine-readable inventory,
  rejects changed/resolved/stale exceptions, removes three small violations,
  and narrows the UI-string fixture classification. The draft ledger has 43
  exceptions across 41 files. Lead independently compared every listed SHA-256
  with the corresponding file in source commit `2fad90b`; all match, and the
  historical baseline is unchanged. Lead accepts this exact inherited ledger
  subject to its source-hash/removal gates. The normal-environment `ci:quick`
  run on the draft structural-ledger commit reached the structural
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
- Candidate `system.stateVersion = "26.05"` per the user's fresh-container
  direction; verify it against the initial installed release before activation.
- Proposed secret file `/private/vpsadmin-webui.env`: OAuth client ID/secret and
  separate stable session-signing secret. The user supplies these privately.
- Before activation: confirm installed VPS architecture/network/stateVersion,
  effective deployed API revision and OAuth policy/client values. License intent
  still needs confirmation. These do not block the prepared plan.

## Cleanup

Session remains open. Preserve unrelated workspace/index changes. No lifecycle
cleanup is authorized or scheduled.
