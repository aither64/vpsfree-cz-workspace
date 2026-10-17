# Final verification

The exact published heads are recorded in final-heads.json. Independent review
and the two verified remediations are recorded in review-report.md and
review-remediation.md. No feature head has been integrated or deployed.

## Passing checks

- Focused runtime Go and Ruby regressions, including repeated-role creation,
  retained retries/forks, numbered additions, schema-4 digest compatibility,
  and exact creation-journal size limits. See review-remediation.md and
  quick-final.log for the commands and assertions.
- Workspace instruction checks: 9 tests, 152 assertions.
- Workspace final-head `nix flake check --print-build-logs --keep-going`:
  exit 0, 331.4 seconds. See packaged-results.json and workspace-packaged.log.
- Runtime final-head `nix flake check --print-build-logs --keep-going`:
  exit 0, 833.8 seconds, including both host VM checks. See packaged-results.json
  and runtime-packaged.log. Recovery polling printed transient assertions while
  the fixture converged; both VM checks completed and the aggregate result was
  "all checks passed!". No unexpected local kernel build was observed.
- Configuration final-head
  `nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev`:
  exit 0, 171.6 seconds, generation 2026-10-17--17-29-48.
  See aitherdev-final-result.json. The preceding attempt stopped at confirmation
  with EOF; it did not start a system build.
- Final paired workspace/configuration runtime pin consistency check passed.
- Candidate compiled `workspace-portal team-preset` produced architect0,
  implementer0, implementer1 and reviewer0 with the intended saved settings;
  candidate reads of the preceding schema-4 catalog matched the preceding
  binary's selection. See compiled-preset-smoke.json. This does not prove live
  new-session creation or assignment.

## CI investigation

Final runtime CI run 39044502588 failed:
https://github.com/aither64/dev-workspace/actions/runs/39044502588

The failure is in the unchanged
TestPortalMutationRejectsProfileSwitchWhileWaiting/successful test. It expected
a superseded-generation error but received the creation handler's 200 ms
transition-lock deadline error. The fixture holds that lock while it waits
10 ms, rewrites the profile symlink and releases it; scheduling delay can exceed
the handler's deadline. Neither that test nor the admission deadline was changed
by this branch. The test file's last change is 8fbc931. All other reported Go
packages passed in the failed job. Full failure evidence is retained in
runtime-final-ci-failure.log.

A focused local diagnostic passed 100 repetitions (200 scenarios) in 5.690
seconds with DEV_WORKSPACES_CODEX_PROVIDERS pointing to an absent session-owned
fixture path. See profile-switch-diagnostic-final.log. The first diagnostic
omitted that existing host-fixture isolation and failed during fixture setup;
it did not exercise the CI failure. No source was changed for these diagnostics.
The available GitHub token refused a failed-job rerun with
"Resource not accessible by personal access token". No credentials were changed.
The earlier reviewed head's green CI is not final-head CI evidence.

## Outstanding checks

Live new Full-team creation and independent assignment to both implementers
remain pending after guarded deployment.
