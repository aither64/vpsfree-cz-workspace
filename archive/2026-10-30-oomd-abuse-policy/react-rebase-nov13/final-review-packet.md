# React generated-SDK rebase: final affected-review packet

Status: complete committed local package, source frozen for lead-coordinated
independent affected review. Not published; PR115 still points at9e7dd95d.
No merge, deployment, registry release or lifecycle action is authorized.

## Request and acceptance

User requested rebasing the incident escalation packages onto current defaults,
plus ordinary osctl-oomd incident report localization to recipient language.
React preserves the accepted selected-type UI; ordinary report text is stored by
the backend and needs no new client fields or React localization behavior.

Use main's generated SDK/request policy and capability/output narrowing. Preserve
selected-type omission on initial reads, server-calculated counts/effective limits,
per-type nullable administrator settings, shared stop exemption/action/cooldown,
old-API hiding, latest-search reference, flushSync and canonical pagination reset.
No arbitrary rule editor, extra navigation, copied SDK, casts, any, raw transport,
provider change, BFF change or second production rule.

Session plan/state/design/implementation-contract.md and sdk-requirements.md are
under work/2026-10-30-oomd-abuse-policy. Architect's Generated choices clarification
(2026-11-14) preserves primitive kind/required/nullable validation in the retained
SDK; the server owns registered choices. Unknown strings follow normal errors.

## Repository, complete range and history

Only vpsadmin-webui is owned here; canonical worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-webui
Branch dev/oomd-abuse-policy; existing PR115 targets main.

- Fresh SSH default/main:88ac13b89d6421c914cd57e18153de1fee6fc7b7.
- Final local head:5ffdb67df9d31de8a2de0952c73b92c9a234b424.
- Final tree:20e4583fe57fd2d02505b23614cac653290e5993; worktree/index clean.
- Actual remote feature lease:9e7dd95d67a3b33b88674a3d436775e0bb820504.
- Old reviewed base40653dffed4561dd6086716fd506a7223d3631d7/head9e7dd95d retained
  at dev/incident-escalation-before-nov13-9e7dd95d; original review/failures remain.

Complete series:

1. c255afdbe8f8563b08b2234f4873ec307d478bcb — verified SDK dependency/provenance,
   ordinary npm lock/Nix frontend hash and dependency reference docs.
2. 2202f08049fa254b6d3f029544c8c67b3834798a — selected incident UI, API integration,
   feature contracts, approved EN/CS copy, actual-library wire/render/filter tests.
3. 5ffdb67df9d31de8a2de0952c73b92c9a234b424 — historical synthetic captures,
   capture-only scroll reset and truthful worklog/evidence, including this rebase.

Dependency input precedes its consumer; historical media remains separate from
runtime. Follow-up source/test fixes were folded into the owning application
commit. Only one final SDK input update exists, with no obsolete local-file input,
React TGZ, superseded OOM-prefixed feature stream, fixup or shim in final history.
No migrations exist in this repository: none merged, released, deployed or consumed.
There is no React database/persisted format change. Backend migration provenance
is separately owned by owner0; this packet makes no backend migration claim.

The rebase had substantive conflicts in API_CONTRACTS, REQUIREMENTS, vps.ts,
VpsListPage, VpsLayout and VpsListMobile. Main transport, toolbar/create action,
partial generated relations, disk-risk badges and independent docs were preserved.
This is not patch-equivalent to the old branch. Full final diff, original/final
range-diff and first-resolution adapter diffs are in this artifact directory.
Tree equality across final consolidation is recorded in after-consolidation.json;
final-input-equivalence.json binds checked runtime hashes and historical media.

## Dependency and public boundary

API source7919441ccb8e9587ad0afc84674b074ca9c5a880, raw schema
f919dcebf8ce5453dce6b0eb09e718f72664b5137443bb8e2064ff6452470ca7.
SDK packed source6a5227c156aeef89447abb1f2e68988cecb735f4, immutable artifact
commit6a6ca3613ce947a1393597d5ddcbc78294f6b12d. Exact341450-byte archive SHA256
fee3800140869c1f721c5a07eda3e438d1a347690dc89aa5f8379a9efc1663bf.

URL:
https://raw.githubusercontent.com/vpsfreecz/vpsadmin-typescript-client/6a6ca3613ce947a1393597d5ddcbc78294f6b12d/development-artifacts/incident-escalation-sdk.tgz

Npm integrity sha512-CyHADzgOATfImrb71IBAQiZ37QBbZ4ZSaObiOzhDZ6dZi5IVMZhW0iY7BF4bT0mzoZk8BXx/i7eybfa8GiqZlQ==.
HaveAPI generator1ef9b204ba45bb261d3334be5c555cc1856b713b/version0.32.2;
consumer runtime remains haveapi-client0.32.0. Candidate package version0.4.0
is not registry publication. Lead independently reviewed source and certified
artifact support, and owner1 verified published HTTPS200+sameSHA.

Manifest, npm-generated lock and development provenance agree. Only the two SDK
lock records changed; BFF lock/hash and all other dependency records are unchanged.
All1364 installed SDK files equal the verified archive. Standard prefetch passed;
frontend npmDepsHash sha256-Q1gWCIYoWlM0eiagOEcIDNBTRvocm5urw64AkCLBlTc=.
No custom fetch/install pipeline or private/sibling path is used in hosted source.
A published registry SDK with these members and corresponding manifest/lock/
provenance/hash remains mandatory BEFORE WebUI merge. This is development only.

Provider ownership: backend defines selectors/settings/summaries and authorization;
the generated SDK owns paths/primitive validation/types/serialization; HaveAPI owns
XHR/decoding; WebUI owns request policy, output narrowing, receipts and presentation.
The changed consumer is src/lib/api/vps.ts and its list/detail/settings views.
Related Go/Rust synchronization and site/legacy UI are owned by other packages.

## Quick evidence and failures

Nix-pinned root tools only; no BFF install, local full suite, frontend build,
browser, server, image, guest or old services-root was created/restored.
Root install for quick verification was a new necessary allocation, not a reversal
of the historical cleanup receipt:313561088 ->316416000 allocated bytes (+2854912).

- docs:inventory:266 routes/74API modules, no inventory delta.
- audit:i18n:8356 matching EN/CS keys; structure pass.
- npm run typecheck + npm test -- <seven files below>:exit0/72.712s,
  seven files/88 tests through actual installed SDK and controlled XHR.
- typecheck:e2e:core, lint, format:check, audit:design-docs, audit:structural,
  audit:component-contracts, audit:ui-strings:check, audit:mutations:check:
  exit0/39.518s. Structural20 accepted/0unaccepted, no new exception; mutation226.
- HTTPS prefetch-npm-deps package-lock.json:exit0/7.596s, final hash above.
  Six existing bundled WASI optional packages lack resolved URLs; no full x86_64
  dependency/build success is inferred from prefetch alone.
- nix build .#checks.x86_64-linux.source-contents --no-link:exit0/4.250s.
  Final clean source resolves the SAME successful derivation:
  /nix/store/gi2gzck9amk337wkhb4i5kxrriqrhmbk-vpsadmin-webui-source-contents.drv
- Final audit:design-docs:exit0/5.277s,285 docs/76requirements; git diff --check pass.

Seven files:
src/lib/api/vps.incident.test.ts
src/lib/api/vps.blocking.test.ts
src/lib/api/sdk.wire.test.ts
src/pages/app/vps/vpsIncidentEscalation.test.ts
src/pages/app/vps/VpsIncident.test.tsx
src/pages/app/vps/VpsIncidentFilters.test.tsx
src/pages/app/vps/useVpsListSmartFilters.test.tsx

Source hashes match the actual tested source; URL/lock/hash/docs changes followed
without runtime/test changes. Tests cover omitted selectors, null resets/false,
generated primitive/null no-send validation, server refusal of unknown strings,
synthetic test-only second type, admin/owner/fallback rendering and receipt guards.
Existing rapid-filter/external-Back/pagination regression stays intact.

Preserved failures: initial typecheck exit2 (three nullable output assumptions;
tests not run), fixed by truthful type predicate + existing VPS label fallback;
local file:packages Nix prefetch failed because it resolved file:///packages.
Replaced by SDK-owned immutable HTTPS input. No failed result is relabeled passed.
Logs: quick-types-wire.log, quick-types-wire-fixed.log, quick-audits.log,
https-npm-deps-prefetch.log, source-contents.log, final-docs.log and watcher receipts.

Normal Nix Git identity verified Jakub Skokan <jakub.skokan@havefun.cz>.
No declared hook framework/core.hooksPath was found; no hook bypass used.
No operation-owned command/tool session remains running.

## Documentation routing and evidence limits

| Topic | Reader/class | Authoritative repository path | Evidence |
| --- | --- | --- | --- |
| Selected incident fields and receipts | API adapter maintainer/reference | docs/design/API_CONTRACTS.md | actual SDK wire/receipt tests, backend-owned contract |
| Product scope/permissions | UI maintainer/reference | REQUIREMENTS.md REQ-051, WORKFLOWS.md, EVIDENCE_MATRIX.md | rendered/filter tests and retained accepted copy |
| SDK source/choices/release prerequisite | Contributor/reference | HAVEAPI_CLIENT.md + packages/vpsadmin-typescript-client-development.json | exact artifact/schema/generator +1364file check |
| Standard cache/hash/source boundary | Packager/reference | PACKAGING.md, packages/frontend.nix | prefetch0, exact source-contents derivation0; full build pending |
| Rebase/check/failure/capture chronology | Reviewer/individual execution | docs/work-log/2026-10-30-incident-escalation.md | raw session receipts linked here |
| Original implemented appearance | Reviewer/historical fixture evidence | screenshot README +fourPNGs | byte-identical to9e7, never current real backend certification |

Handbook entry points already link SDK/packaging/requirements/worklog. Retained
historical published SDK provenance is labeled baseline, not current selection.
KB ownership/workflow remains unchanged; no product copy or new visible flow was
introduced by this rebase, and no production KB changes/captures are performed.

All four synthetic images and their README equal original9e7 bytes. They show
accepted old implementation, not proof of current main's integration/rendering.
Historical initial10pass/1fail/1notrun, intermediate1pass/1fail, affected2+oldAPI1
and desktop recapture1 remain scoped to their exact old sources. Earlier9e7 hosted
CI/smoke successes do not certify this candidate. No browser/build repeat is
requested before affected independent review or while capacity holds apply.

## Requested affected review and next gate

Overall HIGH risk for cross-project API/SDK and mixed-version administrator write
semantics; preserved authorization is still a review concern. Request all four
lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Lead owns assignment to retained reviewer0 with saved Sol/xhigh/read_only; no
replacement reviewer or model override requested. Require explicit complete-series,
obsolete-stream, documentation placement/preservation and NO MIGRATIONS conclusions.
Inspect substantive SDK conflict resolution plus preserved feature invariants;
existing unrelated main implementation is outside this package.

After source clearance: fresh SSH default and actual remote lease, appropriate
rebase only if necessary, one feature publication/update existing PR115 with actual
source/dependency/media limits; capture-comparison; observe automatic exact-head
CI/smoke via fresh catalog Luna/low utility, no duplicate manual dispatch/local
full suite. A new substantive conflict returns through lead. No merge/deploy.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
