# Lifecycle reliability rollout

Status: prepared source is independently reviewed; packaged verification and
exact deployment builds are running. System/profile activation is not yet run.

Sources: branch-inventory.json. Runtime6ab3b48, workspace4b22d04f,
configuration9e90ff6e. Both consumers select same runtime; extension unchanged.
All development changes remain on feature branches. No master integration
approval exists. Final review: final-review.md, all four lanes, accepted.

Original affected owner6a0351a8 held aitherdev reservation1ce9be0f. Stable
finish succeeded at revision5 using exact integrated heads, existing independent
rebase acceptance and fresh live identity proofs. Receipt:
original-reservation-finish.json. This releases the old hold before corrective
deployment without editing ledger or bypassing ownership.

Verification and preparation: verify-prepare.py started exact runtime package
and archive lifecycle VM plus concurrent machine/profile preparation. Results
and stdout/logs use packaged.*, machine-prepare.*, profile-prepare.* names.
Derivations: verification-derivations.json. Preparation builds/copies outside
mutation claims. Final tests include shared session lock contention and portal
restart within one worker invocation; complete reservation release and predecessor
sidecar retry use packaged Ruby regressions.

Activation plan: activate.py binds exact independently reviewed prepared
snapshots, actual user deployment direction, new session reservation, and
system-before-profile dependency. Workers perform adapter dry activation and
configured no-reboot switch; profile selection uses ordinary prepared activation.
No direct confctl bypass. On uncertain outcome preserve original attempt and
recover through ordinary reconcile; do not replay deployment or force release.
Profile selection is forward-only; prior selected package and source/artifacts
remain recorded in ordinary coordinator history.

Acceptance after selection: compare live /run/current-system and system profile
with prepared machine artifact; compare selected application profile with prepared
candidate. Verify portal and service health and conversation continuity. Retry
original saved archive via authenticated portal API (same receipt and journal ID,
next attempt), observe complete local closure and settled journal/sidecar. Preserve
archive recovery and branches. Verify original reservation remains released and
new initiative remains active holding its own review reservation until user merge
or archive direction.

Original archive before rollout: original-archive-before.json, failed attempt1,
receipt ed5897f17bbb3424f6e6647c0d83dd6c953112280cb0718210e1ee70f46b41ac,
operation a0feaf8be13b427703b17170a8b80d971fe91f2130aae488652809e598152ac1.
