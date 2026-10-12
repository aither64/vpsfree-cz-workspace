# Current reviewed final heads

The inset Reveal follow-up is independently reviewed with no findings. Full series,
base/head diff inventory and repeated stream dispositions: inset-review-packet.md.
Whole-branch conclusions: inset-review.md. All four primary feature branches are
published; matching rollout-1 refs preserve the previous consumer sources below.

| Repository | Current head |
| --- | --- |
| dev-workspace | 60c679c52c263a0fc7a4b08c5f83a291cfd89191 |
| vpsfree-dev-workspace | 7157c8098dcf60127aa4df823fab82b4185ad22a |
| vpsfree-cz-configuration | e65ef2c4cd179dac2d96cfdfe6d6c6967f08d566 |
| workspace | 86d96b2656c89f37cd4d521fb150ebb123efa89c |

Generic: three coherent functional commits; extension: one; configuration and
workspace: one final selection commit each. No migrations or obsolete final-tree
paths. Workspace feature comparison base is shared local master 64a39659; its
remote merge-base is 0c827576 with three pre-existing coordination ancestors.
No merge approval is present. New browser/package/build and deployment verification
passed at these heads; results are tracked in state.md. Workspace remains based on
the reviewed 64a39659 feature comparison even when later handoff tracking advances
shared master. Required final rebase/checks apply before an approved integration.

## First rollout after narrow review remediation

The reviewer assessed the complete branch series and final diff at the heads
recorded in review.md. Direct range-diff proves the only runtime correction is
the existing rendering assertion changed from footer to toolbar and Release.
Affected quick tests passed. The correction was folded into the owning commit;
no new design or interface change. Matching pins were regenerated and each
stream consolidated to one final commit. No migrations or obsolete history.
The mandatory-review skill's narrow-fix policy applies; no full rerun required.

### dev-workspace

Base: a8934bdac91c64f66aa3cee26b68df3bcb8c2fc0
Head: bc6b841be0bf83ad84f47daa2e0c064f477bdf23

```
1c83d28e767c2ea061c7f49759f5ca2485ec2ae3 portal: align credential reveal and copy icons
bc6b841be0bf83ad84f47daa2e0c064f477bdf23 portal: control retained development clusters from the toolbar
```

### vpsfree-dev-workspace

Base: 3e5dc4681b0343ec236c3f3dfc0d6f725577c376
Head: 7157c8098dcf60127aa4df823fab82b4185ad22a

```
7157c8098dcf60127aa4df823fab82b4185ad22a devcluster: expose retained start and portal control permissions
```

### vpsfree-cz-configuration

Base: decd92fe3926a4a4304c15957b05cc095948f8cc
Head: 4d0ff7cdb4e56f89cf27bb53a433124736f7e410

```
4d0ff7cdb4e56f89cf27bb53a433124736f7e410 inputs: set devWorkspace to bc6b841b
```

### workspace

Base: 0c82757629b48cef93df2c98677c07f5a9ba5059
Head: 7c226d322e39d6a2e7d25ba075332d055b3e6c5b

```
1deacf09fc7b5a305563ea38bef4d897b9f993bd work: plan cluster toolbar and credential controls
7c226d322e39d6a2e7d25ba075332d055b3e6c5b workspace: select cluster toolbar and retained-start controls
```
