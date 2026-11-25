---
lifecycle: archived
---

# Archive failure fix: merged, deployed and aitherdev released

Complete. Root cause fixed, reviewed, tested and deployed. All three registered
exact final heads are in their remote master branches. Aitherdev claim released
and its authoritative released state verified. No blockers or remaining work.
This conversation/session remains open; no archive, delete or stop was requested.
The original failed archive was not retried.

## Phases

- [x] Diagnosis/design and committed implementation
- [x] Quick checks and independent final review (no findings)
- [x] Four-target verification, including isolated archive-lifecycle VM
- [x] Profile-only deployment and passive usability verification
- [x] User-approved master integration and fresh remote proof
- [x] Verified aitherdev release; post-merge CI green

## Final integrated heads

| Repository / remote target | Exact final head |
| --- | --- |
| aither64/dev-workspace / master | f6d60bf87002fb1896599f35f0284743c16d7e6f |
| aither64/vpsfree-cz-workspace / master | f1741f4982a3bfef710fc3837f8929b3fa4d8f76 |
| vpsfreecz/vpsfree-cz-configuration / master | fdcb0a2c3f6413224a8e32b4b887eaf2ca8ecf81 |

User approval: current conversation message, exact wording
"ok, merge and release aitherdev", accepting the previously named three master
targets and release. Approval retained through a clean mechanically equivalent
workspace pin refresh. No feature refs were deleted; original deployed30 retained.

## Cause, checks and documentation

Browser preparation duplicated the native-monitor proof already returned quiescent
by CLI archive-check and exhausted its shared30-second deadline. Fix consumes the
fresh typed result within the same admission after cancellation check. Missing
proof/blocked/quiesceable owner/join/recheck paths and fresh executor validation
remain intact; no cache, timeout increase, schema or authority change.

[design.md](design.md), [core-evidence.md](core-evidence.md),
[review.md](review.md) (Sol/xhigh, HIGH/all lanes, no findings),
[mechanical-refresh-review.md](mechanical-refresh-review.md) and
[workspace-final-refresh-review.md](workspace-final-refresh-review.md) own rationale,
full cleaned histories, no-migration and documentation preservation conclusions.
Maintained behavior explanation is in runtime docs/session-archive-recovery.md;
no supported recovery path was removed.

[verification-evidence.md](verification-evidence.md) binds all final inputs,
derivers/outputs/NARs and one successful four-target batch,30m45s. No retry or
unexpected kernel build. Exact derivation/full-input equality validates reuse
at the final workspace successor. Post-merge CI run45651730877, exactf6, completed
SUCCESS: https://github.com/aither64/dev-workspace/actions/runs/45651730877 .

## Deployment and release

[rollout.md](rollout.md) is the authoritative final receipt: exact full source/input
graphs, actual deployed/final heads and equivalence, all canonical remotes/targets,
store paths, fresh remote/effect checks, user approval and release evidence.
[deployment-evidence.md](deployment-evidence.md) and
[deployment-verification.md](deployment-verification.md) retain preparation and
verified profile/health/native/session/naming-availability evidence.

Selected application remains
`/nix/store/apjaqip0xj9cy297z2wmb8hmfqn2c8x1-dev-workspace-0.2.0`, deriver
`/nix/store/m9pdsbnrrlwkyhp87d3cic5am7c10rbs-dev-workspace-0.2.0.drv`.
System and system-profile remain exactk79; no system selection was performed.
Native process and its pinned2rq executable were preserved; services active,
health200, original activation0 and all command effects settled.

Deployed workspace30 is not literally merged: finalf174 is an independently
reconstructed patch-equivalent successor with identical complete application/
composition derivations and full inputs, with original review/ranges/migrations
preserved. All final registered exact heads themselves are remotely integrated.

Own machine claim51ed48c0-8052-4e9b-ad36-399562a20020, ownerb6290bcd-8006-434c-a1c8-8c3140699c31,
exact typed config/aitherdev binding, was read authoritatively held after fresh
live and five-remote equality checks, then released at2026-11-25T16:29:11Z.
Authoritative released/revision2 verified. All own repository claims are released;
no owned queued claim/job/reservation or uncertain effect remains. A later
deployment needs fresh machine ownership. No lifecycle cleanup was performed.

No next operator action is required. Historical investigation checkpoints are in
[progress-history.md](progress-history.md) and integration checkpoints in
[integration-history.md](integration-history.md). Initial tracking checkpoint172c14576;
subsequent session records maintained locally under ordinary tracking cadence.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/
