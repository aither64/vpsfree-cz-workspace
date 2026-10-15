---
lifecycle: active
---

# Aitherdev disk retention

Phase: setup and design. Implementation, review, deployment and cleanup pending.

## Phase checklist

- [x] Investigate disk usage and agree retention policies.
- [x] Create an initiative without a duplicate Codex conversation.
- [ ] Commit initial plan/state and create isolated project worktrees.
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
