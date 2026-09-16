Current follow-up pin: vpsAdmin `58a9b71eae255fb2c5547b8be4c41d968ab4dc22`,
KB `2e5cb3b078ff99805fbc42075ed45a05b576a8f2`. Full `bin/check` passed.
Campaign header selection, admin counts and member sidebar/history refinements
have no bindings to existing managed pages or capture concepts. Existing
navigation intent and documentation IDs remain unchanged; no page edits or
screenshots are needed. `docs/ip-release.md` describes the current API/UI
behavior and deployment order. The consumer now declares the existing
`6bdf458` OS pin explicitly so API pin refreshes preserve its runtime.
Hosted Check and Managed page runtime are in progress.

Final test-fixture pin: vpsAdmin `46acba869d319726126e8d9337e9d53fcea7aa6d`,
KB `d76608007bf20710c16058ad7f1fe6b9d81fd4c9`. Full `bin/check` passed.
Only tests differ from the deployed be21 runtime; existing pages, controls and
images remain valid. No screenshots were generated. Hosted Check35003281480
and Managed runtime35003281177 both passed on d7660800.

Selection/member-view refinement pin: vpsAdmin `be21bc8b9e4101ca6b35654ad6f52147dea87213`,
KB `bce530f8af8778ddc77fae9b89510f50225d4a5d`. Full bin/check passes. Existing
managed pages, controls and images remain valid; no screenshots are generated.
OS runtime pin remains 6bdf458. The campaign feature documentation is maintained
in vpsAdmin docs/ip-release.md, including filters and member response boundaries.

Previous checkpoints follow.

Final removal-correction pin: vpsAdmin `a75bb80d5d4ce76e95c766199bc35e798fab956e`,
KB `7222baa580476ce7f9c5c02deabece2744d92f9b`. Full bin/check passed. No page,
control or image changes were needed; the OS runtime pin remains 6bdf458.

Current exact-pin update: vpsAdmin `5e15045a67278569ef45fb5a2246291ff510887e`,
KB `46279da7f53a3f2620d263696422fd7fb828b1b6`. Full bin/check passed again
with the narrow review fixes: no existing page or control drift. The preserved
catalog images were validated, not regenerated. No screenshot deliverables.

# Documentation impact assessment

Current vpsAdmin: `43530927dc814780e8b641fd5e5ce846bd9f4b79`.
Current KB contract: `2dfe4c7c3ba8e1e9675647eb100cf39e7a42ec3c`.
The complete local `nix develop -c bin/check` passed for the unified campaign UI,
including 45 controls/36 paths and the managed-page and image inventory checks.
Existing pages, controls and crops do not change. No KB page/media publication or
new screenshot generation is needed. The user explicitly wants live UI review
without screenshot deliverables. The API pin is updated and OS runtime remains
6bdf458. Canonical docs/ip-release.md explains navigation, bulk action atomicity,
actor privacy, closure, and additive rollout; its index link moved to the new
upstream docs/README.md.

## Previous assessments

Current vpsAdmin revision: `aa9ac1e3af0acde65e15fd2c9758d1613689fed0`.
Current contract revision: `243b15895e7a0f7b13eb63b96c348df309e2e2e5`.
Both are published on the initiative feature branches.

The full local contract and hosted Check pass. There is no existing page,
control or screenshot drift: 45 controls, 36 paths, 35 capture concepts,
94 annotation bindings, 4 managed pages/8 variants, 60 tests/194 assertions,
and 60 screenshot concepts/120 PNGs. No KB page or media publication is needed.
The managed runtime workflow is queued; state.md tracks its result.

The new campaign pages sit outside the existing screenshot crops. Current
networking controls retain their meaning. The final page-local form reset fixes
campaign form boundaries without changing shared rendering or managed pages.
The vpsAdminOS runtime stays pinned at 6bdf458. The lockfile update changes only
the exact vpsAdmin revision.

## Earlier assessments

Affected vpsAdmin revision: 871fa3dae787678ceea7f36ba5cbec139c93e5ee.
Contract repository: worktrees/2026-09-09-ip-release-mechanism/vpsfree-kb-contracts
at head 87bc0fbcb267292a30867d7a5f90eee92552fc10 (base81d6d7d).

The final documentation contract check against the exact pushed feature revision passes:
44 controls, 35 paths, 35 capture concepts and 3 semantic selectors. No existing
label, route or landmark fingerprint drift is reported.

The new navigation links appear in the Cluster and routable-address sidebars.
Existing networking screenshots capture #content-in or individual VPS forms;
sidebars are outside those crops (webui/template/template.html). The existing
address list, assignment forms and reverse-DNS forms retain their controls and
content. The new campaign page has new semantic IDs and a dedicated browser test.
No existing KB instruction or screenshot concept changes meaning.

The exact revision is pinned in the flake input, captures.json, navigation.yml
and pages.yml. Full bin/check passed: 92 annotation bindings / 9 exceptions,
4 managed pages / 8 variants / 12 tests / 21 executable samples, 60 regression
tests / 194 assertions, and the 60-concept / 120-PNG inventory.

The existing disown/removal form now displays pending/failure guidance only when
its asynchronous cleanup has not succeeded. Existing documented normal-flow
controls and screenshot crops retain their meaning and appearance. No reported
page or capture requires regeneration.

The KB runtime remains at its already documented vpsAdminOS 6bdf458f revision,
now explicitly overridden in the vpsAdmin input. This prevents an incidental
nested-lock reset to the provider's older embedded runtime. No platform version
or runtime action change is made.

No production page/media write or new documentation release is needed.

Follow-up check on 2026-09-10 includes reminder controls, the planned-date label,
deleted-user display and permanent-exclusion status in the new IP release
screens. No existing managed navigation path or screenshot crop covers these
screens. Full bin/check passed again with the same counts and no drift.
The final pin includes a DNS integration-test endpoint correction; API and WebUI
component trees remain identical to 473b5c62a. The managed-page runtime passed
on that product tree, and bin/check passed again at the final exact revision.

The later feccc0073 commit only corrects CLI response handling in vpsAdmin's
networking Playwright spec. KB does not consume that spec; its API, WebUI and
shared runtime inputs remain byte-identical. The exact 871fa3dae product pin
therefore remains the documentation revision without another metadata update.

Hosted Check 34470210306 and Managed page runtime 34470210256 both passed on
final contract head 87bc0fbcb.

The later email-only wording follow-up removes a sentence in built-in/overlay
notifications and updates an existing render expectation. It changes no WebUI
labels, routes, controls or screenshots; no new KB pin or runtime check is
needed for this copy deletion.

The final follow-up omits the exemption paragraph entirely when opt-outs are
disabled. Only notification prose/its ERB branch and an existing render
assertion change; the WebUI documentation contract is still unaffected.

Rebuilt-series follow-up (2026-09-15): pinned exact vpsAdmin
4d53fa1573bf5d0ba8de5d896153e4ca21dcfb5a on current KB base 8789cc1.
The complete bin/check passes and reports no control/page/screenshot drift.
All 60 concepts and 120 PNG variants remain valid. The lockfile changes only
the vpsAdmin node; its inherited vpsAdminOS 6bdf458 runtime pin is retained
with the Nix override-input update workflow. No page publication is needed.

Final form/rebase check (2026-09-15): exact pin
`aa9ac1e3af0acde65e15fd2c9758d1613689fed0` passes full bin/check with the same
45 controls, 94 bindings, 4 pages/8 variants, 60 tests/194 assertions and
60 concepts/120 PNGs. The form-context reset is confined to new campaign pages
outside existing screenshot crops. Upstream's doc/ to docs/ rename and PHPUnit
update do not change any managed page or capture. No content regeneration or
publication is required.
