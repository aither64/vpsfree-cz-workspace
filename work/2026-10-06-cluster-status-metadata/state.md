---
lifecycle: active
---

# Cluster status metadata fix

Phase: implementation preparation. Live defect reproduced; no application or
deployment changes yet. Next: create owned worktrees and implement the decoder.

## Phase checklist

- [x] Investigate helper, decoder, current runtime, and live portal.
- [x] Agree existing-card scope and deployment/integration authorization.
- [ ] Implement, document, and complete focused checks.
- [ ] Commit and independently review the complete branch.
- [ ] Verify composed pins, package checks, and CI.
- [ ] Deploy aitherdev and workspace user profile; verify the live card.
- [ ] Merge exact verified feature heads into remote master branches.

## Ownership and scope

`dev-session current` reported no session and both session environment variables
were absent. Created this separate initiative with the supported
`dev-session start ... --as-is --no-codex --no-attach --json` command; no roster
or second conversation was invented. Lead owns design and application edits;
catalog-policy standalone review and fresh utility watchers will be used.
The small decoder unit uses this lead-owned plan as its bounded design brief.
Preserve all unrelated shared-master/index changes and the storage session.

## Evidence

Installed runtime source: 4c3ea2eb3b82b572e86f23ec7f9e53a0f1dc6a0c.
Selected extension: 0ff827df13e82dfab4b536ff29979280f264e8f5.
Helper status exited zero: schema 2, running, ready true, storage topology,
bridge network, ten services, four commands. WebUI source is worktree revision
aa2f60b89df65d2f987be48784ed42bab7010833, clean. Maintenance version 2 is
released/pending false/copied true/active true. Only safe projections were
printed; credentials were never logged.
Read-only portal request reproduced unknown field webuiSource. Decoder also
lacks maintenance, so both metadata objects must be accepted together.

## Integration and deployment approval

User: "you can deploy aitherdev using vpsfree-cz-configuration and merge the fix
into the default branches when it is verified." Accepted plan identifies
dev-workspace/master, coordination workspace/master, and
vpsfree-cz-configuration/master. No separate approval remains for that scope.
Deployment only selects cz.vpsfree/machines/aitherdev and the workspace user
profile. No cluster reset or guest mutation is authorized or needed.
