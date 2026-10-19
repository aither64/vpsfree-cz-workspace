# Prepared rollout

Status: not executed. No default-branch integration or activation approval has
been given. Independent review, its fixes and all verification are complete;
ready, awaiting merge approval.

Candidate runtime: 5d59adbcdba420e5f127333097348ba1860c970d.
Workspace composition: 541d7f9ab937579b903e1f4d886ce6bc487f2bf4.
Configuration: 265ed92ddf52570fa5414c7a4642b22229b3884a.

Build the composed workspace's default package with a
session-owned output root, using a fresh installed-policy verification watcher.
This workspace exports `default` and `vpsfree-dev-workspace`; it does not export
`dev-workspace`. Run the disposable native-profile exercise from the runtime's
Nix environment, retaining compact results. All three feature branches are
published. Inspect applicable CI for the exact final runtime head.

Before activation, prepare the exact aitherdev system artifact and application
profile through native coordination. Read the installed coordination/integration
guides and the configuration's aitherdev operations guide. Resolve this session's
threadless native ownership through supported commands. Current session startup
was --no-codex, so it has no managed conversation. Supported initialization may
require stopping and restarting only this empty runtime, as described in
notes/dev-workspace/2026-10-16-threadless-start-and-configuration-hooks.md.
Include that exact lifecycle action in the final rollout approval request:
ordinary completion does not authorize a session stop. Do not edit authority
metadata. A resource owned by another session must be awaited through the
coordinator.

A read-only coordinator status check during preparation found no active local or
foreign machine reservations. This is an observation, not a reservation or a
guarantee of later availability; activation must still pass native admission.

Required user direction is integration of dev-workspace, workspace and
vpsfree-cz-configuration into their respective master branches, plus activation
of the matching aitherdev system and workspace user profile. Record the exact
direction and scope before submitting any mutation. Deployment remains separate
from integration approval.

Activation order is matching system module then composed application profile,
under the same aitherdev reservation. Keep the reservation until deployment
verification and exact integration proofs are complete. Workspace selection is
forward-only; recover a failed admitted transition under its original attempt.

After activation, inspect collector dry-run output and the scheduled service's
results. Verify live references remain, complete scratch is removed, profile
selection stays unchanged, and the selected generation plus predecessor remain.
Measure available filesystem space and Nix root changes; ordinary host Nix GC
owns store deletion. Do not claim bytes freed merely from released references.
Keep compact journals, feature refs and this session's records.

## Built final artifacts

All checks passed for the exact candidates above. See verification.md and
final-artifacts.json. Application package m72n1y584cafyzi09na546ll751hwnpl;
matching system bd52dj1ba0sai0bd2w2qmhjnmzxg1p8p, confctl generation
2026-10-19--10-43-01. Native coordination preparation and admission follow the
explicitly authorized empty-runtime initialization. No reboot is requested.
This record describes prepared operations; none has been activated.
