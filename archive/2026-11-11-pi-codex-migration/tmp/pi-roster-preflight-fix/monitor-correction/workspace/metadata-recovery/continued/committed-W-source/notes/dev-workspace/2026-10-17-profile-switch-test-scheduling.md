# Profile-switch fixture scheduling and host provider isolation

During 2026-10-17-team-delegation, final runtime CI 39044502588 failed in the
unchanged TestPortalMutationRejectsProfileSwitchWhileWaiting/successful case.
It expected a superseded-generation error but received the creation handler's
"Workspace runtime is changing. Retry shortly." response. The handler waits
at most 200 ms for the transition lock; the fixture holds the lock, waits 10 ms,
rewrites the profile symlink and unlocks. Scheduling delay can consume the
deadline before the generation check. This failure does not by itself show
that superseded-generation rejection was bypassed.

Inspect the failed logs before retrying. The exact final runtime packaged suite
passed locally, and 100 focused repetitions (200 scenarios) passed in 5.690
seconds. The CI result remains failed; local success is separate evidence.
The available GitHub token refused rerun, so no remote rerun was performed.

For source-checkout web tests on this configured host, set
DEV_WORKSPACES_CODEX_PROVIDERS to an absent fixture-owned path when the fixture
does not define a workspace name. Otherwise the deployed /etc provider catalog
can be loaded during newTestServer setup and fail with
"invalid workspace provider state identity" before the test runs. Use the
repository's Nix environment and explicit `go test -mod=readonly`.

Evidence and exact revisions:
work/2026-10-17-team-delegation/verification.md.
