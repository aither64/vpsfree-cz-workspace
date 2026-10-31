# Deployment record

Status: aitherdev system deployment, application activation, live acceptance and
all three integrations passed. The user waived waiting for the final CI repeat;
it remains running remotely, with prior failure evidence recorded in state.md.

## Final selections

Runtime e3315a483f3d3536d492ecbe40f2655449cf630f is selected by workspace
57bd3304b7901d2c942f5f50ecd8897b53bde1ef and configuration
6f6aff9029cd57e1a0f9201356f7fdc9f6480671. All three exact feature heads are
merged into their remote master branches; see integration-proof.json. Both
final pin rebases preserve the reviewed patches. Package and deployment-contract
validation passed. No cluster state conversion or guest reset was performed.

Selected system:
/nix/store/r3c1kcrjmqgq48vjsvkmz3nwkzj6hggy-nixos-system-aitherdev-26.05.20261006.b253099.
Selected application:
/nix/store/b2q12p1725bqrb4nrd6yfjg28hgsggcf-dev-workspace-0.2.0.
The active portal unit is workspace-portal@vpsfree-cz.service.

## Execution

Initial system was98s4gm1i (20261004.0d9e9b8); initial application wash73nvgmd
(runtime4c3ea2e). Host deployment used confctl's exact
cz.vpsfree/machines/aitherdev selector, dry activation first, then switch, from
the guarded feature worktree. The user profile used the stable installed
workspace-host switch command and normal generation, lifecycle and cluster
preflights. Scripts enforced clean tracked source and exact source heads;
profile activation also enforced its previous selected package.

First host deployment at configuration165e465a selected4q2w8x1h, generation
2026-10-06--20-46-15, exit0 in109 seconds. Both system/firewall health checks
passed. Invocation26c5dfb3f8d244eebd1095fa014f5ee8; full host-deploy.log retained.
After the configuration pin's clean rebase onto the separately released WebUI
update, the final build6f6aff90 passed in98 seconds, generation
2026-10-06--22-23-52. Its r3c1kcrj system differed only in the
/etc/confctl/configuration-info.json link; all other direct system references and
package closure versions were identical. Normal final deployment passed, exit0
in about118 seconds, with both health checks passing. Invocation
f4a69b858eb44a3498462bd7a0e40a2b; full host-deploy2.log and exit artifact retained.

Interrupted archives blocked initial profile preflight. The five exact archive
operations explicitly selected by the user were completed through normal
installed executors. The Sep18 retry required temporarily removing two clean
fix-owned worktrees with reused Git admin names, then restoring retained refs.
Three later archives required restoring only state.md modes to their sealed
projection: independent path/byte/mode hashes proved exact equality. No journal
or ownership evidence was deleted or bypassed. Recovery ran under child umask022.
Detailed evidence and reusable diagnoses are linked in state.md.

Profile attemptb47f66e484164201b3fe9ec44aabea50 correctly refused before candidate
selection because the storage lead had an active turn, exit1 after37 seconds.
The ten-minute idle wait never passed. After the user's next "continue" was
interpreted as approval to interrupt that exact turn, the normal portal interrupt
returned ok and the idle check passed. Profile retry
133a32c410be4034a5ac307bcf996cfb activated the expected b2q12p172 package and
completed, exit0 in102 seconds. Full profile-deploy.log and profile-deploy2.log
are retained separately. Warnings for unproven worktrees in other sessions were
left untouched. No conversation was retired or automatically resumed.

## Acceptance and recovery

Repeated safe live verification after application and final system activation
passed: helper schema2 reports running/ready with ten services; portal shows
running/ready with ten services and no status-decode error. Runner identity,
retained disk inode/size identities and every recorded state-file hash match
cluster-before.json. live-verification.json and cluster-after.json contain only
safe projections; raw HTML and helper credentials were never persisted.

The application transition remains forward-only. Recovery uses the supported
stable package-switch commands with the same or a newer compatible package.
Do not select an old decoder or reset retained clusters to bypass a refusal.
Feature/auxiliary refs remain, and only the two clean temporary integration
worktrees were removed. The fix initiative remains open for follow-up.
