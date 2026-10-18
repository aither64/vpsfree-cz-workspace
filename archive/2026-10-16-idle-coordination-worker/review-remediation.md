# Review remediation

## Important: garbage collector journal compatibility

Reviewer identified Collector#mark_live retaining a schema-1-only decoder. Replaced it with the owning Store.integration_journals reader so validation and supported versions have one owner. Kept schema-1 test fixtures valid with their retained journal IDs. Added retention/collection evidence for active and completed schema-2 journals. Focused GC checks passed: 3 runs, 16 assertions, including retention during schema-2 work and collection after completion. This is a narrow extension of the existing supported journal reader, with no new format or ownership policy.

No long integration tests have started. Independent report received; no Blocking findings, three Important and one Advisory, all addressed. Runtime and consumer feature pins will be consolidated to the final corrected head before readiness.

## Pause admission ordering and displayed pause state

Lead inspection found that pause publication could race an in-progress claim: the marker was written outside the ledger mutex, allowing a pause acknowledgment before a claim transaction committed. Publish the marker under the existing ledger transaction. Already admitted claims settle before acknowledgment; later claims see the pause. Added a concurrent barrier regression check. Also corrected paused/held run descriptions so they do not say that continuation is running. These are narrow corrections of the specified pause contract and existing display.

## Important: distinguish contention from command failures

Admission.acquire now raises the internal AdmissionBusy subtype (still Error and CLI code 75). Background continuation waits only for that subtype or explicit suspension/fencing/pause state. Engine.capture retains its CLI exit contract, while failed commands now persist needs_attention and one notice. A failing external command regression verifies code 75 does not trigger automatic retries. Real flock contention verifies quiet waiting.

## Important: normalize host preparation errors

The owning coordination_prepare callback normalizes DevWorkspaceHost::Error into a bounded WorkspaceCoordination::Error. A regression exercises the real callback with failed prepare_profile validation and proves one attempt, persisted actionable reason and one notice.

## Advisory: complete generation identity

Extracted Engine.current_generation? from the existing guard, used by both current_generation! and background handover. Tests cover changed package and replacement profile symlink selecting the same package with a different token. Both hand off without jobs or outbox messages.

## Verification and review disposition

All remediations remain within the reviewed design, public contract and ownership boundaries. These narrow requested fixes, plus the pause ordering correction and truthful paused display, do not require a reviewer rerun under mandatory-change-review steps 9-10. They are folded into the owning unmerged runtime commit. No database migrations, no intermediate deployed journal formats, no expanded compatibility paths.

Quick checks after fixes: integration 32 runs / 158 assertions; admission 4 / 13; GC integration/background 3 / 16; browser 13 tests. All passed. Runtime final committed head ced31b5 replaces 4fd9128d; consumer pin streams will each be consolidated to that final revision. Long verification is now permitted.

## Systemd acceptance observation race

Package and host-package contract build passed at ced31b5f. The real user-manager fixture failed at test/background_integration_systemd_test.rb:63: journal phase finalizing was visible before the completion outbox transaction (expected one, observed zero). Inspection of Integration#complete confirms that it intentionally saves finalizing before export and native notice publication. The fixture must wait for the specific durable receipt, not infer it from an earlier phase write. It now waits for finalizing plus the completion event, and treats activating/deactivating units as still running before redispatch. Product behavior unchanged. This is a narrow test correction after diagnosed failure; no blind rerun or new reviewed boundary. Original failing log retained as systemd-check.log.

## Final package/systemd result and native fixture diagnosis

At final runtime ced8e76e, systemd acceptance passed (1 run / 5 assertions), and package plus host-package-contract passed. Exact runtime artifact is /nix/store/3vzmicdbbvbrimsksv451x4xryi4lnqq-dev-workspace-0.2.0. No product change followed these passing checks.

The isolated native evidence program reached the packaged helper, which correctly refused its test manifest with incomplete Codex provenance. Manifest validation requires client_version together with socket and thread ID. The fixture now reads exact native --version (0.163.0) and includes client_version. This fixes session-local test data only. Original failed log native-notification.log retained; corrected run uses native-notification-final.log. Full live coordination remains untested until managed owner recovery.

## Verification environment corrections

Fresh watcher delegation became unavailable after two completed utility batches; parent reported the skill-authorized visible fallback and uses bounded blocking observation. The unrooted runtime artifact was collected between checks. Rebuilding the same final source/derivation with a retained out-link protects subsequent native verification and rollback preparation. Source unchanged.

The planned configuration command placed --yes globally; pinned confctl returned status 64 before building. `confctl help build` confirms --yes is a build command option. Corrected command: `nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev`. Original CLI failure retained in aitherdev-build-invalid-options.log/status, corrected run in aitherdev-build.log/status. No activation was attempted.
