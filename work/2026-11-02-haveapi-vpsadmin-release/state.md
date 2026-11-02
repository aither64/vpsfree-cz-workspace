---
lifecycle: active
---

# HaveAPI 0.32.2 downstream release

## Current phase

Design and upstream publication wait. Identity verified by dev-session current
and both environment markers against the trusted thread binding.

## Phase checklist

- [x] Verify identity, inspect retained roster, authorize peer communication.
- [ ] Architect design and execution package boundaries.
- [ ] Confirm HaveAPI 0.32.2 registry publication.
- [ ] Implement vpsAdmin dependency update; quick checks; independent review.
- [ ] Integrate vpsAdmin to master (no long CI wait).
- [ ] Regenerate Go/Rust/TypeScript clients; verify and review changed clients.
- [ ] Integrate and minor-release/publish clients with code changes.
- [ ] Update configuration vpsadmin channel; verify, review and merge.
- [ ] Verify remote final heads/publications and prepare final handoff.

## Backlog and owners

| Package | Owner | Dependency | Acceptance |
| --- | --- | --- | --- |
| Design/generation/release workflow | architect0 | Repository guidance | design.md with stable package contracts/checks |
| HaveAPI publication | peer release lead | Tagged release workflows | Exact tag/source and registry evidence |
| vpsAdmin update | implementation assignment pending | Design, published 0.32.2 | Focused dependency diff, checks, reviewed master merge |
| Clients | implementation assignments pending | Updated API generation input | Reproducible generation, conditional minor publications |
| Configuration | implementation assignment pending | Integrated vpsAdmin, clients complete | Only intended channel lock changes, verified master merge |
| Review/integration coordination | lead + reviewer0 | Committed deliverables, quick checks | Full history and migration conclusions, remote proof |

## Authority and constraints

Initial user request explicitly directs vpsAdmin master merge, changed-client
merges and minor publications, and configuration channel merge. Rust/TypeScript
actual defaults are main; Go/vpsAdmin/config are master (architect inspection).
No machine deployment or lifecycle action is requested. Do not await long CI.

## Evidence and pending work

Retained roster: architect0 (Astra/xhigh, workspace_write), implementer0–3
(Sol/xhigh, workspace_write), reviewer0 (Sol/xhigh, read_only), observer0.
Architect0 assigned investigation/design. First assignment attempt met a transient
session mutation lock; retry succeeded without changing settings.
Peer reports source 1ef9b204ba45bb261d3334be5c555cc1856b713b and annotated tag
v0.32.2 object 7f8f656ca7655bafaf2cf5e7095573806085a442; not yet published.
Release run 41529223599 prepares artifacts/protected approval. No registry
availability claimed. TypeScript generator targets haveapi-client@0.32.0.

## Handoff and cleanup

No repository worktrees or resource claims created yet. No deployment.
Session remains open. Stable portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-haveapi-vpsadmin-release/
