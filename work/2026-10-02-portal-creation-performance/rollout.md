# Portal creation performance rollout

Status: final sources/pins reviewed and published; corrected application and host
builds/checks passed, with both outputs retained. Five isolated Full-team creations
at the original candidate passed: median6.401349s, max6.500734s. Corrected real
root-loss and partial-team fault acceptance passed. Host dry-activate and switch
passed for the exact generation; both normal host health checks passed. The
application user-profile switch refused an unrelated active session and waits
for normal idle proof. Full-package canary remains pending.

User request "Implement the plan" authorizes the accepted aitherdev rollout.
Feature branches remain unmerged; deployment does not authorize master integration.

## Exact current candidates

| Component | Revision |
| --- | --- |
| SDK | 4c170393a96ed0a6ac2e43488d073f6fcab36132 |
| Generic runtime | 924c0ec28c41dd8b56aaf17f2212b302ca614899 |
| Site extension | 8f8d8ecf5031c40d3e4a4ee2e9425721fc035800 |
| Workspace source | 1b670e0329c80b5ed266f6edb92ac2096134677c |
| aitherdev configuration | 3d26ec396ceb935a233bdda3079618821d099b3e |

Application: /nix/store/xl9mvbb5j19anfbx6qj3lrw8k7a9vnz2-dev-workspace-0.2.0.
Compiled Go provider SHA256:
ac2bf71e98d1bafb4357bbf0bb7b7d1140f0bb4a1a903147cff67790284e9c4c.
Codex launcher/native, runtime contract and Full catalog match the retained old
candidate. New corrected-candidate-root retains this output; old candidate-root
continues to retain0klh7 for measured evidence and the private fixture.

Host generation:2026-10-02--23-26-29.
Toplevel:/nix/store/4wa4aiamhn1cm63j7gsaiqdqfn0f9ign-nixos-system-aitherdev-26.05.20261001.4feb8eb.
Config generation metadata selects exact runtime924c0ec and unchanged
llm-agents/nixpkgs/home-manager. New corrected-host-candidate-root retains it;
old host-candidate-root retainsjpv50 for historical provenance.

SDK CI37024785401, corrected runtime CI37063660861 and corrected extension
CI37064115624 passed exact heads. Source whole-branch reviews and consumer
supplement found no findings, no obsolete history and no migrations. Relevant
reports are linked from state.md; consumer locks and deployment contract match.

## Ordered operations and current result

1. Completed host dry-activate for exact generation above using the declared config
   Nix shell, local aither login, --yes/--no-interactive and normal health checks.
2. Completed separately reviewed fresh root-loss/member-loss fault cases through
   the supported corrected-provider boundary. Preserve old unavailable-root
   receipt/journal, original result, services, claims and five measurements.
3. Completed deployment of the same exact host generation with confctl switch.
   Preserve tool health checks and automatic rollback; no configuration merge.
4. Application activation attempted through installed /home/aither/bin/workspace-host switch
   --source absolute owned workspace worktree. Respect all transition ownership,
   generation, activity and journal refusals; do not interrupt other sessions.
   The idle gate refused storage-redesign's active turn. Old9g8 remains selected;
   preserve the failed log/status and retry the ordinary switch when idle.
5. Verify selected package, active services and retained36 roots/owned3 members.
   Run one actual-history Full-team portal canary, with readiness and first model
   response measured separately; one goal, no tools, detailed progress.
6. Reconcile evidence/docs and retain feature branches active awaiting explicit
   integration approval. Do not archive/delete/stop sessions or remove claims.

The parent initiates deployment; fresh catalog Luna utilities only observe its
long waits. Each long check/build has a fresh watcher. Full logs and identity
snapshots stay private; only nonsecret curated evidence belongs here.

Host switch completed on 2026-10-02 around 22:07 UTC, wrapper exit0. Parent
verified `/run/current-system` resolves to the exact toplevel above. Confctl's
systemd and firewall checks both passed (2 passed, 0 failed). Full host log is
`.confctl/logs/2026-10-03--00-06-31-confctl-deploy.log` in the configuration
worktree; its local date differs from UTC. No unexpected kernel build occurred.

The application switch exited1 at 22:08:22 UTC, before package selection. Its
normal idle check reported storage-redesign thread
`01a0d230-6068-71d2-9768-4928682cdccf` has an in-progress turn. Parent's read-only
observation confirmed active status; existing package9g8 remained selected.
Supported pre-selection recovery restores earlier quiesced terminals. The
pending update and original failed profile-switch.log/status remain; no journal
or busy session is cleared. A fresh utility watches only the reported activity;
the stable switch must recheck all activity on retry. A separate guarded wrapper
retains the next run as profile-switch-idle.log/status.

Read-only observation from 22:12:18 through 22:22:32 UTC never found idle status.
The observation window ended incomplete, without changing that session. No
watcher or deployment remains running. Final blocked-rollout health/retention
check passed: all36 prior roots and owned3 members remained exact, four user
workspace services and nginx were active, host4wa remained selected and old
application9g8 remained selected. Activation and the single live canary are
prepared, unexecuted next steps. This record does not claim production portal
latency for the corrected package.

## Execution evidence and historical provenance

Corrected application build/flake checks passed in the related final batch,
including Go/Ruby/package and workspace contract/catalog checks. A Git author
identity diagnostic in a fixture did not cause suite failure. Original aggregate
exit1 was host GC-root retention, not application failure. Root/identity JSON
were verified directly by the parent, correcting the watcher's missing-identity
summary.

Host output first built through rootSSH/sudo, but RubyEtc.getlogin selectedroot
(loginuid0 despite effectiveuid1000), so confctl refused root GC-directory
creation. Repeating only the host step in the normal uid/loginuid1000 local Nix
shell succeeded69s and reported the same generation. Parent retention script
counted the current symlink as duplicate; finite directory correction retained
the existing output without rebuilding. Failed logs/generation remain evidence.
No root permissions or loginuid were changed. No kernel build occurred.

Original source8ae46f9/extension4f817322/workspace461bedfb/config4123d883 and
candidate0klh7 produced the successful warm-up7.230879s and all five timings.
[verification-measurements.md](verification-measurements.md) owns those exact
numbers and model offsets. The lost JSON fault then failed retry2 through an
unsupported resume of a loaded unmaterialized root. [recovery-design.md](recovery-design.md)
records the corrected source behavior and strict uncertainty boundary.
[Root observation](root-observation.md) now confirms that root is unavailable;
its old prepared continuation stays unexecuted. A new exact fresh fault case
supplies corrected acceptance without changing or replacing that old receipt.

Original setup/schema/native/socket/goal-counter failures and all consumed claims
are retained privately, with curated review/preparation records linked from state.
Historical original host output was once absent; normal rebuild reproduced it
and retained a GC root. Removal cause is unknown. None of these historical
build operations activated the host or user profile.

Pre-activation snapshots retain36 root IDs and the owned Full roster. Four user
workspace services and nginx were active. Final Full preset equals the retained
preset. Post-activation and single canary wrappers are prepared, not executed.

## Software recovery

No persisted schema/migration or Codex/catalog/provider change is introduced.
Old SDK callers omit the optional listing flag. Recover application faults via
an advancing package generation that reverts the change; do not select an older
profile generation. Resume the same supported switch after interruption, and
preserve conversation/team/receipt/submission identities. Never delete a pending
journal or repair uncertain root evidence to unblock a transition.

Host dry-activate completed exit0, resolving exact generation2026-10-02--23-26-29
at runtime924c0ec2. Noninteractive output omitted service-plan/health detail, so
the observer initially marked that detail incomplete. Parent inspected confctl's
owning control flow: it performs activation and raises on a false activation
result; no skip/copy-only option was supplied. Parent accepted command success
without inferring real activation or health evidence from that dry run. The
subsequent real host switch and two successful health checks supply that evidence.
