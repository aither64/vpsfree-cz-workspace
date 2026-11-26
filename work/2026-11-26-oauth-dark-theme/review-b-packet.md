# Final vpsAdmin OAuth/branding repository review

Completed B component: all intended source/tests/docs/dependency changes committed,
quick checks+hooks passed, own checkout/index clean, publication withheld until
final review because push starts long CI. Review entire range, not last patch.
Use same independent reviewer0 saved purpose review gpt-6.1-sol/xhigh/read_only,
no overrides/fallback/nested reviewers. High risk; all four mandatory lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Read mandatory-change-review skill/each lane reference and applicable workspace/
repository AGENTS/routed procedures in full. Preserve read-only; report full
findings/conclusions to lead, who persists report.

## Scope, source and history

User goal/implementation approval, including explicit removal of core.logo_url
fallback, is in plan.md/state.md; accepted interfaces/design in design.md. No
integration/deployment/release approval. User wants compact light/dark/auto login
controls, status-inspired dark palette, declarative site light/dark logos,
bundled generic fallback, React/docs roundtrip, no PHP exchange.

Worktree: worktrees/2026-11-26-oauth-dark-theme/vpsadmin
branch: 2026-11-26-oauth-dark-theme, target master
Base: 1bf7c120beaf21f7fd30f4b75441d4b835bc57af
Final: 1d3f5bcae05f3d44ca9ad22011721202c48c0124
Fresh fetch origin/master unchanged; base is merge base, own tree clean.
Whole series ONE commit: api: add OAuth appearance and declarative branding.
43 files, +764/-99. Complete file/series/diff inventory via git log BASE..HEAD,
git diff --name-only BASE..HEAD, git diff BASE..HEAD. Owner receipt in this packet
is authoritative; vpsadmin-evidence.md is being reconciled from prior draft to
that receipt without delaying review. Missing extra evidence returns to owner,
do not rebuild it. No migrations/schema changes/intermediate/repeated pins,
obsolete approaches or released/deployed/externally consumed B heads. One final
HaveAPI pin stream439beea8. Commit combines feature with minimum compatible
source/runtime/profile packaging; owner says inseparable supported artifact,
review that rationale independently under general/scope lanes.

## Inventory and ownership

B owner implementer0 owns entire source/tests/instructions/docs/metadata/checks/
commits/diagnosis/fixes; lead only authorized settled prose windows. Grouped files:
auth Appearance+5assets; OAuth2Config+ERB; PasswordRecovery controller+ERB;
WebAuthnRegister controller+ERB; SysConfig+testseed; catalogEN/CS; appearance,
callback/OAuth/recovery/registration/profile specs; API Gemfile+api.rb explicit
profiles; flake/overlay; API3package wrappers/common/Gemfile/lock/gemset and
fixed HaveAPI source; gem-update task; exporter Gemfile/safety/spec; Node spec;
docs README/OAuth/client examples/schema export. No consent/task UI. WebAuthn
registration only shares new brand resolver; no new theme integration there.

Scheme→declarative common→bundled inlineSVG, no sysconfig reads/registry/old seed;
dormant rows ignored without deletion migration. Same-origin recovery preserves
appearance, external authorization_start_uri unchanged, fresh-browser auto.
Normalized scalar theme + independent return bit, explicit success callback
only incl SSO; state/PKCE/redirect/token/CSRF untouched. All forms/errors stay
existing flow. Shared logo origins enter existing recovery CSP for both schemes.

## Exact dependency graph and maintained boundary

Owning HaveAPI reviewed/published head439beea801df3139b7154283a171f53c68295939,
actual source/runtime version0.32.0. Raw archive NAR
sha256-xH9KW4Y0XXWNhhczkJmn+Rf/dhPpei0fBS+8xg334uc=.
Remote fetched/prepared source
/nix/store/9z3ipzfdpa7k87jp7pa92x4xghwaz61w-vpsadmin-haveapi-source-0.32.0/servers/ruby.
Same prepared source for dev path+API source-gem override: same-source make doc,
archive-safe full file list (no Git index). Deterministic service Gemfile requires
actual source0.32.0 with no hostenv conditional; normal registry minimum~>0.32.2
remains on ordinary Gemfile path. Existing metadata normalization helper reused.
API package metadata only source server0.32.0 plus x86_64-linux platform, no
unrelated version updates. flake.lock blob e53d2b042cbe8b874e593b49ac6e09cfc315e3ce
unchanged. Actual runtime/client/Go/Rust/TS remain published0.32.2. Three profiles
explicitly FIX generator_version0.32.2 using existing supported HaveAPI interface,
strict configured-vs-actual guard intact (no dynamic expectations/source relabel).
DB-free real-env registration proved all three versions/source paths, then real
mounted/render examples passed. Same-version profile assumption changed for
this actual pinned combination, explicitly documented and must be reviewed.

Exporter rejects inherited VPSADMIN_HAVEAPI_PATH before conditional tooling
Gemfile evaluation, keeps isolated registry0.32.2 bundle; related safety tests
passed. Server source versus publishedv0.32.2 bounded comparison: only version/
dependency text and docs-label CSS remain before feature; fixes patch-equivalent,
not literal ancestry. No new version/release or generator source closure.

Actual HaveAPI A+D conclusions can be reused from review-component.md (all four
lanes clean439beea8); C original b1f63a5e reviewed plus narrow C-1 direct accepted
successora28c59c6, PR335. Final E still awaits published B, will pin B/C through
real confctl and get complete final branch/cross-project graph review. B does
not gain whole-initiative readiness or merge approval from this component review.

## Quick evidence, corrections and remaining checks

Owner authoritative completion report:
- Catalog generation+health passed; Node3/3, semantic text contrast minimum5.85.
- First107RSpec:105pass+2stale markup assertions (locale html opening/passkey
  DOMContentLoaded). Precise expectations fixed; no weakened auth assertions.
- Next source setup0examples failed real profile-version coupling; corrected
  explicit supported profile pins, not mismatch guard bypass. Actual DB-free
  three-profile source/version registration passed before behavior recheck.
- b-runtime-check.log/result terminal exit0/139s:7auth (both prior failures+
  5actual hook/SSO/optout/invalid/cancel route),5mounted/renderprofile,
  15isolated exporter examples all0fail. Lead targeted log confirms old names
  at721/722 and summaries7/5/15. No repeat needed.
- Touched Ruby lint/root-format and Nixfmt pass. Commit hooks44838 exit0:
  MigrationSpecs/Nixfmt/WebuiI18n/RuboCop/APIi18n all passed; commit-message hooks
  pass with72-col advisory only, required<=80. Failed first commit79998 formatting
  reconciled HEAD unchanged, one equivalent safety-helper formatting fix rechecked,
  no remaining mutation uncertainty. All tooling quiescent at delivery.
- Existing CI path coverage packages/**/nixos/**/flake/API roots and
  authentication/** covers new runtime; route/helper specs fit foundation/
  platform-config exactly in BOTH full/core topic matrices. No partition change.

Declared API assessment from complete final diff: no resources/actions/routes/
param types/defaults/choices/API/protocol version change. SystemConfig uses
free-string category/name+genericvalue, removed registered row is observable
behavior not enum/schema change. Explicit profile policy not resource metadata.
OAuth cosmetic field is cross-project auth extension, reviewed as such, not
SDK action schema. No schema export/client regeneration launched. Independently
assess this source conclusion; uncertainty should target specific declarations.

Long checks unrun: actual consumed immutable API source-gem artifact graph/
installed bundle+all5gem paths/Gemfile/file manifests, services-up packaged routes,
full/core API-spec modes (publication matrices or smallest necessary local
coverage), combined native login/docs/React browser. Prepared owner commands:
b-build-after-review.sh and b-package-check.rb (syntax pass), then existing
./test-runner.sh test services-up. Do not run during final review. B owner
retains their preparation/execution/failures; lead retains mutation drivers and
visible parent monitoring fallback for long checks. No duplicate upstream generic
gem extraction (HaveAPI full server1054CI already passes incl gem proof).

## Documentation and KB inventory

Reference branding/theme/recovery/rollback→developers/operators:
docs/oauth-appearance.md linked by docs/README.md.
Independent fixed generator policy+packaged docs→contributors/operators:
docs/api-client-examples.md. Old released-gem heading anchor preserved.
Isolated schema export/source-env refusal→tool users:
docs/api-schema-export.md. User EN/CS labels and all settled prose had direct
lead writing/terminology pass. Wire semantics authoritative HaveAPI
/doc/en/oauth-theme.md; no duplicate provider authority. Individual failures/
exact receipts in session only. No production deployment claimed by docs.

KB cached exactc064b4fe87d66486c5eb8f43cb278a464d8574ab bounded capture/scenario/
page/navigation query found only PHP session.login IDs, no OAuth/recovery capture
binding. PHP unchanged, no production KB writes. Record applicability limits,
not blanket external-doc certification. All intended docs included in commit.

## Required report

Findings ordered Blocking/Important/Advisory with concrete line+commit and
consequence. Explicit complete-range obsolete-history/no-migrations/repeated-pin
conclusion, supporting runtime/package split rationale, supported path/profile/
old-new compatibility, documentation placement/preservation and remaining
verification gaps. Retain same reviewer; no source edits/nested agents/long
tests/publish/merge/deploy. Report_to_lead full report; lead persists read-only
reviewer artifact as review-b.md. Direct narrow fixes use mandatory step9;
new contract/design requires affected lanes. Final E review still must bind actual
B/C/A+D heads/input graph and cross-project compatibility/lineage, no merge
readiness until all required checks final.
