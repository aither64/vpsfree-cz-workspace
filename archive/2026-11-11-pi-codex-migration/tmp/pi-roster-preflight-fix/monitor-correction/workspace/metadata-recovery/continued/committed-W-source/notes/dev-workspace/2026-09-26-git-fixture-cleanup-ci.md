# Temporary Git-fixture cleanup error in a Nix package check

In `work/2026-09-26-codex-queue-ledger-capacity/`, the extension repository's
first `master` CI run of `nix flake check --print-build-logs` failed while
running inherited generic dev-workspace tests. The error came from
`DevSessionTest#test_session_closing_rejects_ambiguous_or_missing_tracking`:
`Dir.mktmpdir` cleanup called `FileUtils.remove_entry`, which raised
`Errno::ENOENT` for a path under the fixture's `.git/objects/`. The report had
336 runs, 3,484 assertions, zero assertion failures, and one cleanup error.
The extension commit changed only its generic-runtime flake pin; this test
helper was unchanged.

Run [36249774435, attempt 1](https://github.com/vpsfreecz/dev-workspace/actions/runs/36249774435/attempts/1)
contains the failure. After inspecting that log and the helper, the same-head
[attempt 2](https://github.com/vpsfreecz/dev-workspace/actions/runs/36249774435/attempts/2)
passed both the flake check and `devcluster-check`. The exact feature-branch
CI and local full check had also passed. A concurrent change to loose Git
objects during recursive cleanup is plausible, but the runner log does not
identify a competing process; the cause is not proven. A green rerun is
verification for this integration, not evidence that the cleanup race cannot
recur. If it does recur, instrument fixture subprocess completion and Git
maintenance behavior before changing the assertion or ignoring cleanup errors.
