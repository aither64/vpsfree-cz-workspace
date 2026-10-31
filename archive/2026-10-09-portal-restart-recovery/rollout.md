# Aitherdev rollout: portal restart recovery

Status: executed and verified. Ready for use, awaiting merge approval. User authorized deployment through
vpsfree-cz-configuration and explicitly excluded rebooting aitherdev.
Default branches remain unchanged.

## Selected revisions

| Component | Revision |
| --- | --- |
| codex-web | c9878454f07da244c103b8a79340b92b6d5bf052 |
| dev-workspace | 97ea4c56f4984c5d8e574735e09a205c6a648f59 |
| workspace composition | 4f4060ab3425c8eecc4614c261f28ee359b611e0 |
| configuration | f715299ccd019a3f282dfbd969231223f3479e3b |
| unchanged vpsFree extension | 0ff827df13e82dfab4b536ff29979280f264e8f5 |

## Baseline

Host boot ID: `0104034e-3a15-4772-aa62-aac7ee4ff6ef`.
System: `/nix/store/g7grfapc1lky4p94r37yhf8y2rj5vn20-nixos-system-aitherdev-26.05.20261008.7c8764b`.
Application profile: `/nix/store/za0yzb4j1ahkdgnbciix3plfzsyhcwrr-dev-workspace-0.2.0`.
User lingering: yes. All workspace services enabled and running.
Native Codex remains 0.160.0.

Before deployment, Codex PID was 1204139 and tmux PID 435397. Portal/router
PIDs were 3762055/3761994. The profile's live switch policy should preserve
Codex and tmux while replacing the portal and router. Verify actual behavior
and unchanged host boot ID after both deployment operations.

## Executed sequence

1. Resolve independent review findings and pass final-head checks, including
   native cold recovery and disposable VM boot. The VM test may reboot only
   its private VM.
2. Build aitherdev configuration from the initiative feature checkout:
   `nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev`.
3. Deploy that checkout with normal guarded dry activation and health checks:
   `nix develop --command confctl deploy --yes --no-interactive --dry-activate-first --no-reboot cz.vpsfree/machines/aitherdev switch`.
4. Switch the application through the stable user-profile command:
   `/home/aither/bin/workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-09-portal-restart-recovery/workspace`.
5. Verify profile/package contracts, service health, stable initiative URL,
   exact native process preservation and host boot ID. Record results here.

Long builds/checks are owned by a fresh verification utility. The main agent
owns deployment invocation and interpretation. Never restart Codex/tmux or
mutate another session as a smoke test. Runtime recovery tests use private
fixtures rather than the occupied workspace.

## Recovery

Before profile selection, a refusal leaves the existing package selected.
After selection, retain the forward target and retry the same reviewed switch
if reconciliation fails. Normal downgrade is refused once durable recovery
or receipt state exists; use a compatible forward correction. Native roots,
rollouts, queues and goals stay retained. Generic supported instructions are
in dev-workspace/docs/workspace-portal.md; this file records only this rollout.

## Executed actions and verification

Pre-deployment checks passed: private native restart fixture, final generic and
composed packaged suites, standard final-source recovery boot VM, host-module
idempotency VM, all seven browser subtests, aitherdev configuration build and
exact final runtime CI 37999200234 at 97ea4c56. The complete local batch exited 0.
Library CI 37995107833 passed at c9878454. Review findings were resolved and
focused checks passed before the long checks.

Configuration deployed at f715299c using the sequence above, exit 0 after 1m43s.
Confctl used build generation 2026-10-10--00-53-47; normal dry activation and
live switch with --no-reboot succeeded. SystemState=running and firewall active;
2 health checks passed, 0 failed. Selected system:
/nix/store/kxscawff631f111i9blaiwbjpvv9h9g6-nixos-system-aitherdev-26.05.20261008.7c8764b.
Wrapper evidence: /tmp/portal-recovery-config-deploy.log.

The stable workspace-host switch selected composition 4f4060ab successfully,
exit 0. Actual application profile:
/nix/store/wgbyyyivgza0i1y4wpk8d0hn8c0pd8fj-dev-workspace-0.2.0.
Wrapper evidence: /tmp/portal-recovery-profile-deploy.log.
The application declares sessionRecoveryPolicy 1 and livePackageSwitchPolicy 1;
its native Codex link is the unchanged
/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0/bin/codex.

Post-deployment quick checks passed:

- Host boot ID is unchanged: 0104034e-3a15-4772-aa62-aac7ee4ff6ef.
- Native Codex PID 1204139 and tmux PID 435397 are unchanged.
- Portal/router refreshed to PIDs 1415774/1415614.
- Codex, tmux, portal and router user units are enabled and active.
- User lingering remains yes.
- Unix portal healthz returns {"ok":true}; owned session page returns HTTP 200.
- Public HTTPS portal validates with the installed CA and returns expected
  unauthenticated HTTP 401.
- Deployment pin contract passes for runtime 97ea4c56.

Stable URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-09-portal-restart-recovery/.

No aitherdev reboot, native/tmux restart, default-branch integration, session
archive/delete or other session smoke mutation was performed. Reboot coverage
comes from the disposable VM; native recovery and browser/CLI boundaries have
separate fixtures. The accepted absence of one integrated native portal/CLI
restart test remains documented in review.md. All feature branches are retained,
ready and awaiting explicit merge approval.
