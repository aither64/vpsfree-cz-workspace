# Disable automatic maintenance in large disposable Git fixtures

The 1001-file modified-rename regression initially passed its assertions but
failed Go TempDir cleanup with `directory not empty` in the disposable bare
repository. Git background maintenance can race removal after bulk object writes.
Configure `gc.auto=0` and `maintenance.auto=false` in that test repository before
creating the bulk history. This leaves production Git configuration unchanged.

Initiative: work/2026-09-12-portal-review-experience. The original failure was a
test-fixture cleanup race; rerun after the explicit maintenance settings verifies
the regression and cleanup together. It passed in 1.164 seconds.
