# Mechanical final pin review reuse

The original independent review remains in [review.md](review.md).
The coordinator read the bounded complete-tree verifier, then ran it once to
satisfy the changed-head reconstruction requirement. It reconstructed each
fresh default plus only the final runtime selection and proved unchanged reviewed
locks, file sets/modes, one final update per stream and no migrations. G separately
proved exact immutable application/composition derivation and full-input equality.
This meets mandatory-change-review’s mechanical-refresh exception; no new
substantive behavior or lane rerun is introduced. No tests were rerun for tree
equality. E executes the already-reviewed immutable derivations once.

```json
{
  "schema": 1,
  "decision": "accepted",
  "kind": "mechanical_final_pin_refresh",
  "reviewer": {
    "address": "reviewer0",
    "thread": "01a21312-bbce-7821-afda-65d9e905bc2f",
    "model": "gpt-6.1-sol",
    "effort": "xhigh",
    "originalReport": "review.md",
    "reportSHA256": "83796516f34f5ac765254701a0b22dfc3dd04a2a419f71a2210fb5b09d918f5b"
  },
  "repositories": [
    {
      "name": "workspace",
      "oldBase": "d43347c1fd4f9ff9dfdf5c19f6cccb9531bbd639",
      "oldHead": "18275679109c2adda4084af1ea7474e21be98b4e",
      "base": "e7b876f69aca4554d52a3ac19ed097263847ad43",
      "head": "30b74dc3278728ab36197e0d2ef2cf76c66cf791",
      "changedPaths": [
        "flake.lock",
        "flake.nix"
      ],
      "completeFreshTreeReconstructed": true,
      "reviewedFinalLockEqual": true,
      "singleConsolidatedSelectionCommit": true,
      "lockSHA256": "f411b1b56173b128a85d4c18a17869d12d9eca4add6ba1b2a843ab8b6c426919",
      "target": "refs/heads/master",
      "migrationInventory": []
    },
    {
      "name": "vpsfree-cz-configuration",
      "oldBase": "d5055ec0b2ea22de976f6703208f5526c3e185ca",
      "oldHead": "6f6cb452e17ca663114a07013a0402ef85a7fee3",
      "base": "9bdb0c68b47ceebde450fcdf018727b382cacc09",
      "head": "fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81",
      "changedPaths": [
        "flake.lock"
      ],
      "completeFreshTreeReconstructed": true,
      "reviewedFinalLockEqual": true,
      "singleConsolidatedSelectionCommit": true,
      "lockSHA256": "8f3738f6c1f9a583fc4692cb0f67de4a9db7e46dbccb896bcdb021d09546b0f3",
      "target": "refs/heads/master",
      "migrationInventory": []
    }
  ],
  "runtime": "f6d60bf87002fb1896599f35f0284743c16d7e6f",
  "coordinatorVerification": {
    "command": "python3 work/2026-11-25-archive-failure-investigation/verify-g-pins.py",
    "result": "passed",
    "exitStatus": 0,
    "completeFreshTreesIndependentlyReconstructed": true,
    "reviewedFinalLocksEqual": true,
    "singleFinalUpdatePerStream": true
  },
  "artifactReuse": {
    "applicationDerivation": "/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv",
    "applicationOutput": "/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0",
    "compositionDerivationPrefix": "26hx1kp1xlmsklpx2zmz991m6qj3krn7",
    "compositionOutputPrefix": "nxf02z6jccv47rzwzkl5gx3zadq67jya",
    "exactDerivationsAndCompleteInputsEqual": true,
    "source": "G immutable old/new evaluation and full graph receipt; E results pending"
  },
  "migrations": [],
  "authority": "No integration, lifecycle or additional deployment authorization granted."
}
```
