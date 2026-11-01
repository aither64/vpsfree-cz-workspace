# Final branch inventory

## dev-workspace

Base: `356f6a9930bb8b0749079069038c67695404e825`. Head: `00952377f152ae600dc6723f239c1a36fe6aaf3d`.

```text
00952377f152ae600dc6723f239c1a36fe6aaf3d portal: retain Codex mode during metadata refreshes
```

Final diff: [dev-workspace-final.diff](dev-workspace-final.diff).

## workspace

Base: `306e805d7d0ab4b2236aaa1dbd0fb174b81bb05d`. Head: `6bdc2a60f9b1c116c3dff2675efc8be1c5a09cf3`.

```text
6bdc2a60f9b1c116c3dff2675efc8be1c5a09cf3 workspace: select stable Codex mode refresh
```

Final diff: [workspace-final.diff](workspace-final.diff).

## vpsfree-cz-configuration

Base: `b18412bfdbec545312469f581f2991bcf6c237d5`. Head: `f644b39a0f05b096a26c9f3df270d07483604937`.

```text
f644b39a0f05b096a26c9f3df270d07483604937 inputs: set devWorkspace to 00952377
```

Final diff: [vpsfree-cz-configuration-final.diff](vpsfree-cz-configuration-final.diff).

No migrations. No obsolete approaches or intermediate pin commits remain.
The runtime behavior, its browser regression and guide are one logical fix.
Each composition consumer has one separate final pin commit. Earlier unpublished
configuration pins were replaced by a single confctl-generated base-to-final
update; none was merged, released, deployed, or externally consumed.
The runtime was amended once to make fake-clock sync hints deterministic;
its superseded source was never deployed or merged.
