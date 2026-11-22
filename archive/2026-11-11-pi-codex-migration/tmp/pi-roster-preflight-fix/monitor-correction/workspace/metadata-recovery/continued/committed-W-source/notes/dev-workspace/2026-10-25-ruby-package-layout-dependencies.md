# Ruby command dependencies in package-layout fixtures

When a command gains a `require_relative`, update both the actual package and
any tests that build a minimal package layout. In the archive-preparation work,
`workspace-host`'s lazy archive-recovery loader passed in the source layout but
failed in its packaged fixture with `cannot load ... workspace-archive-check`.
The Nix package already installed the new module; the fixture's explicit copy
and symlink lists omitted it.

Keep those lists aligned with the shipped wrapper's requirements. Verify with
`nix develop --command ruby test/workspace_host_test.rb -n test_workspace_host_loads_dev_session_only_for_archive_recovery`, then run packaged Ruby checks.
The focused corrected fixture passed (1 test, 3 assertions). The original
packaged failure was retained before rerunning; it did not exercise the VM.

Related initiative: `work/2026-10-25-archive-unmanaged-files-investigation/`.

Native acceptance also found a separate command-boundary gap: the new identity
service supported a missing team roster, but the CLI's final JSON loader did not
include the new command in its existing root-only allowance. Service unit tests
passed; a plain native session in the VM exposed the final loader error. Keep
service behavior and command result handling aligned, and exercise the complete
shipped command for new lifecycle helpers.
