# Final workspace mechanical successor

The original independent review and prior mechanical certificate are retained.
The coordinator read and ran the new bounded read-only verifier once (exit0),
independently reconstructing the complete final tree from the fresh tracking-only
base plus the original pin patch. The source session was verified ordinary before
retention. All nontracking source/modes, byte patch, complete lock graph and actual
application/composition derivation JSON are equal. One final pin, no migrations or
obsolete update stream. This satisfies the existing mechanical-review exception;
no substantive source change, reviewer rerun or new deployment is needed.

The deployed old30 commit is preserved but is not literally an ancestor of the
new successor. Integrated lineage must be proved by this exact equivalence plus
fresh remote proof of f174. The already committed shared tracking parent may be
published normally together with the approved pin; no foreign lifecycle action
or tracking-content edit is performed here.

```json
{
  "schema": 1,
  "decision": "accepted",
  "kind": "mechanical_workspace_successor",
  "reviewer": {
    "address": "reviewer0",
    "thread": "01a21312-bbce-7821-afda-65d9e905bc2f",
    "model": "gpt-6.1-sol",
    "effort": "xhigh",
    "originalReport": "review.md",
    "sha256": "83796516f34f5ac765254701a0b22dfc3dd04a2a419f71a2210fb5b09d918f5b"
  },
  "repository": "git@github.com:aither64/vpsfree-cz-workspace.git",
  "target": "refs/heads/master",
  "mapping": {
    "fromBase": "e7b876f69aca4554d52a3ac19ed097263847ad43",
    "from": "30b74dc3278728ab36197e0d2ef2cf76c66cf791",
    "toBase": "97bf6db040d35ac10be0a5a9302ecb5c4c037df7",
    "to": "f1741f4982a3bfef710fc3837f8929b3fa4d8f76",
    "relation": "patch_equivalent"
  },
  "userApproval": {
    "wording": "ok, merge and release aitherdev",
    "scope": "workspace/master (within the previously named three master targets)",
    "retained": "clean equivalent patch, no scope expansion"
  },
  "migrations": [],
  "coordinatorVerification": {
    "command": "python3 /tmp/archive-workspace-refresh-bhjdii1l/verify-readonly.py",
    "exitStatus": 0,
    "completeFreshTreeReconstructed": true,
    "byteIdenticalPatch": true,
    "stablePatchID": "3a3e8dcf13db76da2ba49e602f41c2e616ba76b6",
    "fullLockGraphEqual": true,
    "actualCompleteDerivationsEqualVerifiedDeployment": true,
    "completeDerivationJSONSHA256": "48008632d77f09f41a907a1390e3b333c05afe439b5d57a58c4ba13b8f522eab"
  },
  "application": {
    "appDrv": "/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv",
    "appOut": "/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0",
    "source": "/nix/store/hh81k6nk1r1x0jhi0v8a1l9d53jr0h4n-source"
  },
  "composition": {
    "compositionDrv": "/nix/store/26hx1kp1xlmsklpx2zmz991m6qj3krn7-workspace-pi-runtime-composition-tests.drv",
    "compositionOut": "/nix/store/nxf02z6jccv47rzwzkl5gx3zadq67jya-workspace-pi-runtime-composition-tests"
  },
  "preservedDeployedRef": "refs/heads/2026-11-25-archive-failure-investigation-deployed-workspace-30b74dc3"
}
```
