# Downstream composition inventory

Runtime source remains the independently reviewed e3315a483f3d3536d492ecbe40f2655449cf630f.

## Coordination workspace

Feature head a296f66f39f3ec04c19bab9cb4e8933a341fa5f4, parent/base
8dfb2bf8fb249d9fb348cfee55ba255b0bd58f10. One dependency-selection commit,
two files, five additions/five deletions. The feature was fast-forwarded/rebased
onto current shared master before editing. Only the nested runtime node changed;
the extension node, all siblings/follows and site configuration are unchanged.
No obsolete history or migrations. Further shared-master tracking-only movement
may require a patch-equivalent rebase before integration.

Final rebase onto shared master f8b7271d produced ef529ec8bfb85e8c2d939ef69bdac2204fefdfc7.
`git range-diff 8dfb2bf8..a296f66f master..HEAD` reports the sole pin commit
unchanged (`=`). The new base adds archive tracking and the separately owned
repository-PR instruction change. The relevant agent-instructions check passed
on the rebased source. Rebuilding its default output returned the exact same
composed package b2q12p1725bqrb4nrd6yfjg28hgsggcf already fully checked.
Runtime, extension, configuration pin and package contracts are unchanged.
Published the rebased feature ref with an exact old-head lease; original merge
approval and independent pin review still apply to the identical patch.

## vpsfree-cz-configuration

Feature head165e465ae5be6ad1706e0528d537011616d20efb, parent/base
cde8451718d75929c931db63626b48f7de92fc4f. One generated dependency-pin commit,
flake.lock only, three additions/three deletions. Confctl's existing dev-workspace
channel/devWorkspace role owns this pin. Only that lock node changed; semantic
checks passed. Overcommit Nixfmt and commit hooks passed; the generated message
has the expected >72-character TextWidth warning and is preserved by procedure.
No obsolete history or migrations, host module/options changes, or other targets.

These two updates are mechanical dependency selection and exempt from automatic
substantive review. The final cross-project history/composition inventory is
provided to the same independent reviewer to conclude downstream readiness.
Package checks and the single-host build/deployment still follow.
