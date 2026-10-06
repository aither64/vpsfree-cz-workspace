# Session policy application rollout

Status: deployed and verified; all three reviewed feature heads merged into
remote master. The original archive blocker was recovered with failure evidence
preserved. The first attempt below is historical.

Deploy the reviewed application from
`worktrees/2026-10-04-session-modes-review-timing/workspace` at
`9f016bf8685a5098fe24892cf9a539c031856eb9`. It pins organization extension
`e1bb5cf3ad37c5ef31445a68ab85f53db2858777` and runtime
`6a972b9ab01077611b2c60e0fc726c185e050315`.

Preflight observed selected profile:
`/nix/store/cfrf8mjcww7lks1ylqzgfay5920ab029-dev-workspace-0.2.0`.
Active Codex root:
`/nix/store/a29lfsrdnbkijw5iabpmxghkqf46jk2p-codex-package-0.160.0`.
Registered workspace is the canonical `/home/aither/workspace/ai/vpsfree.cz`.
Expected candidate:
`/nix/store/nl29dilg1awgqxmim73d04pizsp5px3j-dev-workspace-0.2.0`, output of
the exact final workspace source derivation. The literal deployment launcher
is prepared at `/tmp/session-modes-deploy-workspace.sh`; bash syntax passed.

After final verification, the parent launches the stable
`workspace-host switch --source <absolute workspace feature path>` in a named
transient user service. The launcher supplies a complete literal PATH, exact
session identity, source-head/clean-tree and selected-profile guards, complete
log and an atomic exit-status file. A fresh utility observes that exact unit;
it does not relaunch or deploy. The package command owns lifecycle-journal,
cluster-schema/generation compatibility and serialized transition preflights.
Do not bypass refusal or reset another session's state. Recovery uses a
corrected same/newer forward package, not an older profile.

Verify selected package, service health, installed skill text and catalog
totals/design ownership/prompts after switch. Compare the saved roster and
creation snapshot before/after without creating or reconfiguring live teams.
Canonical workspace source rules remain on the feature branch until explicitly
authorized integration. Correct new-session developer prompts are packaged.

No system configuration deployment is needed. If host changes are later found
necessary, their owner is vpsfree-cz-configuration's confctl
`cz.vpsfree/machines/aitherdev` target, channel dev-workspace/role devWorkspace;
that would be a separate scope decision. Default-branch integration and recovery of the exact archive were separately
authorized by the final user instruction recorded below.

## First execution

The parent launched `workspace-session-modes-review-timing-deploy.service`
(invocation `d046e2aa70a249cc82974f4dce9febd2`). Its guarded switch exited 1
after 2 seconds at the lifecycle preflight, reporting unfinished archive
`vpsfree-cz/2026-10-03-api-specs-optimization`. Unit Result=exit-code,
ExecMainStatus=1 and atomic `deployment.exit=1` agree. The selected profile
remains the preflight package above. No activation or post-switch checks ran.
See [deployment result](deployment-result.json) and [log](deployment.log).

The other session's owner must finish that archive, or the user must explicitly
direct recovery of that exact operation. Do not bypass it or treat this failed
switch as permission to change foreign session state. Preserve failed evidence;
later retry uses a new unit/log/status identity and fresh utility observer.

## Successful recovery, deployment and integration

The user authorized recovering the exact pending archive and merging the affected
default branches without waiting for CI. [Recovery](archive-recovery.md) preserves
the journal, original failed portal receipt, retained-team retirement ordering
defect, CLI missing-home failure, and final matching-command success. The archive
implementation remains a later task; the journal was completed normally.

A new guarded switch used invocation `f0e8606d273d4106b24bb7f3b8dde0a6`, exited
0 at 2026-10-04T18:04:27Z, and selected the exact reviewed candidate above.
The utility could not observe the user service from its environment; the parent
visibly took over the same operation and confirmed atomic completion without
retrying. [Final deployment result](deployment-retry-result.json).

[Installed verification](post-switch-verification.json) confirms new defaults,
review policy, unchanged retained roster/creation records, active services and
portal health. New sessions receive the corrected prompts; existing snapshots
retain their settings. Runtime, extension and workspace remote master all contain
their exact tested feature heads. [Integration](integration.json). Automatic
post-merge CI is left unattended per user direction. The session stays open.
