# Final branch inventory

## dev-workspace

Base: `356f6a9930bb8b0749079069038c67695404e825`. Head: `a8934bdac91c64f66aa3cee26b68df3bcb8c2fc0`.

```text
a8934bdac91c64f66aa3cee26b68df3bcb8c2fc0 portal: retain Codex mode during metadata refreshes
```

Final diff: [dev-workspace-final.diff](dev-workspace-final.diff).

## workspace

Base: `306e805d7d0ab4b2236aaa1dbd0fb174b81bb05d`. Head: `45aba9bf798b8b3b880eb018dad9bb627edb4cf5`.

```text
45aba9bf798b8b3b880eb018dad9bb627edb4cf5 workspace: select stable Codex mode refresh
```

Final diff: [workspace-final.diff](workspace-final.diff).

## vpsfree-cz-configuration

Base: `b18412bfdbec545312469f581f2991bcf6c237d5`. Head: `3faee82a80b815e3be0542d30b3ea9f535193aa8`.

```text
3faee82a80b815e3be0542d30b3ea9f535193aa8 inputs: set devWorkspace to a8934bda
```

Final diff: [vpsfree-cz-configuration-final.diff](vpsfree-cz-configuration-final.diff).

No migrations. One focused commit per repository; no obsolete approaches or intermediate pins remain. Final review inspected the preceding complete series (reviewed-branch-inventory.md). Final heads incorporate the requested narrow stale-plan fix and synchronized regression, including the corrected fixture sequence, with matching regenerated consumer pins. Superseded source was never merged, released or deployed.
