# Integrated final heads

All four feature heads below are merged into remote master. Integration approval:
user "better, merge it" on 2026-10-12. Final review and history conclusions:
inset-review.md; original inventory: inset-review-packet.md. Pre-merge inventory,
patch equivalence, checks and push evidence: merge-record.md.

| Repository | Integrated feature head |
| --- | --- |
| dev-workspace | 60c679c52c263a0fc7a4b08c5f83a291cfd89191 |
| vpsfree-dev-workspace | 7157c8098dcf60127aa4df823fab82b4185ad22a |
| vpsfree-cz-configuration | e65ef2c4cd179dac2d96cfdfe6d6c6967f08d566 |
| workspace | 0ea2461032ef6be99d0cf88f38090d3ecc38b4dd |

Generic: three coherent functional commits; extension: one; configuration and
workspace: one final selection commit each. No migrations or obsolete final-tree
paths. All final comparisons were captured before integration.

The reviewed/deployed workspace 86d96b26 used shared local base 64a39659. Its
remote pre-merge base was 0c827576, including pre-existing coordination ancestors.
A clean rebase onto handoff tracking ea7d06da yielded integrated head 0ea24610;
range-diff proves the selection patch is identical. Quick tests and the composed
deployment contract passed after that rebase. The runtime/provider heads and
workspace input files are unchanged from the full deployed verification.

The exact deployed workspace source 86d96b26 remains published on rollout-2;
rollout-1 sources remain preserved. The installed aitherdev composition is still
the fully verified runtime 60c679c/extension 7157c80. A tracking-only rebase did
not require another application deployment. Both post-merge CI workflows passed;
exact run/head evidence is in merge-record.md and state.md.

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
