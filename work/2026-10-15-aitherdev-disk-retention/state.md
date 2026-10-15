---
lifecycle: active
---

# Aitherdev disk retention

Phase: implementation. Host cleanup and runtime collector are implemented;
focused checks pass. Review, deployment and cleanup remain pending.

## Phase checklist

- [x] Investigate disk usage and agree retention policies.
- [x] Create an initiative without a duplicate Codex conversation.
- [x] Commit initial plan/state and create isolated project worktrees.
- [ ] Implement and locally check configuration and runtime collection.
- [ ] Commit complete deliverables and obtain independent final review.
- [ ] Run longer verification and the aitherdev build.
- [ ] Deploy, apply reviewed cleanup and verify reclaimed space.

User authorization: "Implement the plan" and "you can deploy aitherdev using
vpsfree-cz-configuration on your own". No default-branch integration approval.

Initial inventory: old VM disks 245.7 GiB (out of scope), Nix store 222 GiB,
/tmp 113.1 GiB, private KB campaigns 64.5 GiB, coordination sources 34.9 GiB.
Implementation setup found / at 96%, with 42 GiB available. Pressure GC cannot
collect live roots. The ad hoc g7 KB campaign has a retained runner/two guests;
exact shutdown proof must precede its manual cleanup.

Extensive unrelated shared-workspace changes exist; preserve them and stage
only this initiative's records. No user data has been removed. Registration
returned this exact new slug and a stable URL. Explicit matching environment
identity verifies current. Team list reports no valid lead Codex thread because
creation used --no-codex; no retained roster can be selected. Use ordinary lead
work plus installed catalog standalone review and utility monitoring policies.

Repositories, branches and tested revisions will follow registration. No schema
migrations are planned. Immutable coordination records remain intact; additive
retention metadata must preserve old/new package operation.

Next: commit setup, register worktrees, record the design and implement.


## Management ownership handoff

A native deployment requires a managed root thread. Initial --no-codex creation
was adequate for tracking but cannot admit new coordinator work. Initialize the
ordinary managed root with a bounded management-only initial request; the
initiating conversation continues implementation. The first attempt correctly
refused because repository registrations had changed portal.yml after its
committed baseline. This consolidated checkpoint is the genuine ownership
handoff exception to normal tracking cadence, needed before conversation creation.

Configuration checkout initially failed its normal post-checkout hook because
its new worktree had no local bundle. Entering its pinned nix develop environment
installed the declared dependencies; native worktree registration retry succeeded.
Hooks remain enabled and were installed/signed through Overcommit.

Host tests: 10 passed (0 failures). Runtime GC tests: 13 passed, 51 assertions
(0 failures). The collector preserves queued/recovery references and compact
metadata, expires unused preparations, and retries interrupted Git removal.
Existing preparations release their guard before building; new code retains the
shared generation guard and detects old in-flight native preparations before GC.

Read-only SSH root access to the declared aitherdev target succeeded. Deployment
is authorized; native coordinator ownership and existing reservations still apply.
