# Final review: stable systemd unit links

Reviewed clean runtime head `ea650c34c56eeb16ce0cfd330e5e9cb1b25c46be`, complete range `7ceb6b943c7fa6e6db2b42b1fc2d9732c6413e03..ea650c34c56eeb16ce0cfd330e5e9cb1b25c46be`, the new host commit, and the browser changes since accepted `901cff7db8f816cad12d8bbc2b39fa477fbd786a`. The supplied full diff and latest-commit artifact exactly match Git output. Complete-range whitespace checking passed.

Same independent standalone reviewer `/root/creation_final_review`, retained catalog `gpt-6-astra` / `xhigh`. Session identity and both environment markers match; the verified live roster is null. All four mandatory review references and applicable workspace/runtime guidance were applied. Previous accepted runtime conclusions remain applicable outside this delta. Source remained read-only; no nested agents, long checks, deployment, or lifecycle actions were performed.

## Findings

- **Blocking:** none.
- **Important:** none.
- **Advisory:** none.

## Affected-lane conclusions

**General.** The new `refresh_systemd_instance_links` handles the reported collected-package failure directly. It derives eligible unit/template names from the selected package, examines existing direct and wants/requires symlinks, and compares their textual targets against the matching template in a dev-workspace store path. It does not require the predecessor package to exist. Direct aliases are redirected through the stable profile; enablement links use the local template. The suffix handling covers the shipped service/timer families, and the existing atomic symlink helper performs replacement. A repeated pass leaves the resulting stable links intact.

The new pass skips regular instance files, custom targets, masked instances, and unit families absent from the selected package. It creates no missing instance or enablement link and issues no service start/enable command. Existing activation policy remains responsible for service actions. The narrow documentation addition describes this repair in the owning profile-state guide.

**Architecture.** Link installation is the correct generic host owner. The implementation reuses the package's shipped unit inventory and existing atomic replacement, without a parallel hard-coded unit registry or downstream repair script. `activate_candidate` invokes link installation after profile selection, and the selected candidate's `_activate` invokes it again before `configure_user_services` performs daemon reload. Therefore the repair also executes when an older package initiated the switch. The new helper does not depend on the initiator knowing the new behavior.

**Scope.** The live evidence records precisely the stale provider instance and wants links this code recognizes. Repairing existing package-owned links is proportionate to that failure. No provider operation, session lifecycle, custom-unit management, or additional worker activation was added. The trusted local operator boundary is respected without speculative physical-path defenses.

**Risk and compatibility.** The textual match is limited to a same-template target under a dev-workspace store package. Filesystem errors propagate through existing activation recovery, and a partial pass can be repeated. The selected profile remains the activation authority; this change neither rolls back a selected generation nor changes transition ownership. The repaired links are ordinary systemd links that older packages can follow. No journal, registry, authority, provider, native binary, protocol, or dependency format changes occur. Older code lacks the new repair guarantee; normal recovery remains the existing forward package-switch procedure.

## Browser correction and verification

The owning sixth commit now opens the settings dialog, selects the effort, clicks Save while awaiting the actual root-session POST, checks the response, and waits for the dialog to close. The route `/api/sessions/${record.slug}/settings` agrees with the root `conversationPath` override in `portal/internal/web/static/app.js`. The native-effective `xhigh` poll remains in place. This corrects the test interaction and route expectation; it does not weaken settings verification or alter product behavior.

The focused host tests exercise dangling instance/wants/requires links, service and timer templates, stable selected-template resolution, idempotence, regular/custom instance preservation, unrelated families, and absence of new service commands or disabled instances. The packet reports 4 tests / 78 assertions passing, the two new tests passing 56 assertions, and an expected failure when the refresh method alone is disabled. I inspected those tests and the production call paths; I did not rerun them.

The packaged VM seeds the exact dangling provider alias and enablement pattern before normal registration, then checks systemd load/enabled/start/active behavior and final template resolution before the existing browser/native suite. This is useful coverage of real systemd behavior, but it has not yet run at this reviewed head. The earlier failed browser assertion and partial VM results are not full acceptance evidence. Syntax/Nix and quick results reported by the packet do not replace the pending packaged run.

## Complete history, consolidation, and migrations

The final complete branch has seven coherent units:

1. `98ae6b38b2830b612f68d3d5a84f96c1d7caf5ca` — provider-aware creation journal reading.
2. `bc29fab704f1cff34f2435710585d063e0419d87` — packaged usable-creation acceptance and CI.
3. `95cc08dbbeaafcc264a9af0e452b832b16d68e82` — all-provider retirement discovery.
4. `11620fc9793083a8ba2a8ac25cc4cf7357c3c489` — terminal preparation retry refusal.
5. `814568f3a28ae916ef193fd0be129a9f28fe1ffd` — HTTP readiness after fixture restart.
6. `c5f86eefd3c45bf3a28e757ce38626177a713091` — complete fork settings preservation and its corrected regression coverage.
7. `ea650c34c56eeb16ce0cfd330e5e9cb1b25c46be` — stable systemd link repair with owning tests/docs.

The independent host behavior belongs in its separate seventh commit. The browser interaction/route correction is folded into its owning sixth unit. There is no obsolete partial fork implementation or test-fix chain in the final series. Exact deployed 95 and published 814 sources remain ancestors. The replaced reviewed 901 runtime and tested 360 runtime remain available under their `refs/session-evidence/2026-10-19-session-creation-end-to-end/` refs; the inspected change from 901 to the replacement sixth unit is confined to the browser test. This preserves consumer and verification provenance without retaining superseded feature commits.

**No migrations** exist anywhere in the complete range: no database conversion, journal-version transition, or intermediate schema lineage. **No repeated runtime dependency/input/pin streams** exist. No additional history consolidation is required for this runtime series.

The previously reviewed workspace `3dfe7bc7c9400a082d9bbecc1ddd180b03ac2541` and configuration `0c6ec0a11323a580a3b07b7e208fdf5c666b308b` still each contain one consolidated 901 selection. Their earlier no-migration/consolidation conclusions remain valid for those heads, but they are superseded candidates and do not select this host fix. Final matching pins and their complete-history acceptance remain outstanding.

No review finding prevents authorized long verification of this source. Full positive packaged/CI acceptance, the old-reader negative control, final consumer selections and preparation, exact deployment/live acceptance, and conditional integration/release remain with the parent. This report does not declare final merge readiness.
