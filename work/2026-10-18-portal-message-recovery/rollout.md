# Aitherdev rollout

## Prepared behavior

Portal source: d3de362f5d8fa86bbf0c4865b0766eb614cf4e2b. Workspace:
5ab415afbe766a16267b7ebd5c0646eecfb310e3. Configuration:
e9dddabf713ab6ee4b4ef24b969ebd68932346dd. Both consumers select the same runtime;
the final deployment composition contract passed. Independent final review and
its direct timestamp-node remediation are complete. Source Go, existing paging,
and the new Chromium/Firefox recovery/display tests passed. Runtime package,
composed workspace and final source CI passed. The initial aitherdev invocation
stopped at confctl's confirmation prompt with EOF before starting the build.
The parent inspected that log and confctl build --help, then selected its
documented --yes option. The corrected exact aitherdev build passed in 113.58s
under fresh Luna/low watcher 01a150f2-9187-7b80-b9b4-237e8195726a. Built confctl
generation: 2026-10-18--23-38-03. No kernel build or other verification operation
remains. All activation and integration remain pending.

## Authorization

Initial user: “aitherdev can be deployed using vpsfree-cz-configuration. when
deployed and verified, you can merge it.” Follow-up scope selection explicitly
approved dev-workspace/master, vpsfree-cz-configuration/master and workspace/master
after successful deployment verification. No reboot, session closure, archive
or deletion was requested. Stopping the owned shell and enabling native coordination were explicitly
approved by the user’s “yes” on 2026-10-19. Normal stop removed the runtime; its
trailing empty-thread recovery error is recorded in state.md. Native startup is next.

## Ordering and recovery

Prepare and build exact committed source, workspace and configuration revisions.
Verify matching nested runtime/channel locks and deployment contract. Use the
selected coordinator to reserve vpsfree:aitherdev; currently another session
holds deployed_review ownership. Do not bypass that reservation. System
activation/dry-activation precedes user-profile activation. Application remains
in the user profile, never installed by the system configuration.

Verify current-system/profile identities, package/source composition, portal
access, reported UI behaviors and Codex/tmux continuity. Then submit authorized
fast-forward merge jobs with exact reviewed/equivalent ranges and retain feature
refs. Finish reservation only with exact final integration and explicit
deployment/review completion evidence. Profile recovery is forward-only through
the admitted attempt or reviewed successor. Ambiguous effects require original
operation reconciliation, never blind replay or forced release.

## Evidence

- branch-inventory.json: original reviewed exact ranges;
  verified-branch-inventory.json: final remediated branches and diff checksums.
- review-report.md, review-remediation.md, reviewer-native-policy.json.
- source-shorttmp-verification.json: successful full Go suite and paging result
  within the browser batch; source-browser-firefox-verification.json: successful
  final Chromium/Firefox recovery/display regression. Earlier failed fixture
  attempts and host-isolation failure evidence remain retained.
- build-source-heads.json and build-verification.json: exact package/host build
  identities and incremental results. build-watcher-final.txt proves completion
  of that batch when present.
- build-aitherdev-noninteractive-verification.json and
  aitherdev-build-watcher-final.txt record the successful corrected host-build operation. The original prompt failure is retained separately.
- Source CI run 39167591341 passed at final d3de362; ci-current-result.json and
  ci-current-status.json bind the successful run and job results.
- Activation jobs, live checks and integration proofs do not yet exist.
