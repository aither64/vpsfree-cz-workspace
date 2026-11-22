# Activity recorder test directories

`NewActivityRecorder` requires its directory to have mode 0700. Passing the
framework-created `t.TempDir()` itself failed that check in the local Nix Go
test environment. Use `filepath.Join(t.TempDir(), "activity")` so the recorder
creates and owns the private child directory. Keep the production permission
check intact.

Verified by the recorder-setup error release test with three race repetitions.
Related initiative: `work/2026-09-12-portal-review-experience/`.
