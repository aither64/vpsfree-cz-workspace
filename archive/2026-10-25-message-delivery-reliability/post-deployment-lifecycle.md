# Selected-package lifecycle acceptance

Fresh standalone utility `01a1733e-4bd4-7241-9c66-98d93fff6bbb`, verified
gpt-6-luna/low, full access, approval never, ran this after deployment.
No live session lifecycle action occurred.

**Result: passed** — exit status `0`; the owned build has finished.

- **Revision:** `9634151b9836311c331a58880fbb4c46133fd98f`
- **Profile:** `/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0`
- **Test:** `session-archive-lifecycle` VM check, from the exact command you supplied.
- **Elapsed:** approximately 18 minutes 39 seconds (the VM test reports 884.77 seconds).
- **Evidence:** complete log at `/tmp/message-delivery-reliability-2026-10-25/selected-archive.log`; exact exit status at `/tmp/message-delivery-reliability-2026-10-25/selected-archive.exit`.
- **Output:** `/nix/store/99113yqjh101fkzc17yjmd1ry082zhp8-vm-test-run-dev-workspace-session-archive-lifecycle`
- **Failure excerpt:** none; the VM test script and cleanup completed successfully.
- **Still running:** none.

The test uses the existing reviewed VM script and the exact installed package:

```nix
let
  runtime = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/dev-workspace?ref=refs/heads/2026-10-25-message-delivery-reliability&rev=9634151b9836311c331a58880fbb4c46133fd98f";
  pkgs = import runtime.inputs.nixpkgs { system = "x86_64-linux"; };
in
import (runtime.outPath + "/nix/tests/session-archive-lifecycle.nix") {
  inherit pkgs;
  self = runtime;
  devWorkspace = builtins.storePath "/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0";
}
```

The full VM script and cleanup completed successfully. No owned operation
remains running. The output root can be removed after acceptance; exact source,
package and output identity remain recorded above.
