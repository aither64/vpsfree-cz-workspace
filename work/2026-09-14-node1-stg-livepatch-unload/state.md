---
lifecycle: complete
---

# 2026-09-14-node1-stg-livepatch-unload

## Repositories
Canonical bare clones repos/vpsfree-cz-configuration.git and repos/vpsadminos.git
are being inspected. No project branches or worktrees created.

## Status
Read-only investigation has identified a strong SSH-session correlation for all
three unloads found in September 5–14 logs. The follow-up vpsAdmin timing bug is
also reproduced and a fix is proposed in vpsadmin-kernel-history-diagnosis.md.
Investigation and planning are complete. The user will start implementation in a
different dev-portal session; this initiative owns no implementation work.
The agreed implementation handoff is preserved in handoff.md. This coordination-only
initiative has no registered feature branches, deployments, or remaining checks.
Tracking stays at its current path and runtime stays open pending an explicit
archive request. Started with dev-session start
node1-stg-livepatch-unload --no-codex --no-attach --json. The original process
had no active session. Use this explicitly created slug for subsequent commands.

## Commands run
- Read repository AGENTS.md and livepatch configuration from bare Git refs.
- SSH read-only queries to root@log.int.prg.vpsfree.cz.
- Direct node1.stg.vpsfree.cz SSH refused public-key authentication.
- Queried node log rotations log-20260905 through log-20260914 and current log.
- Queried forwarded runit output in /var/log/remote/localhost/log and
  log-20260914; no live-patches service output matched.
- Matched the SSH authentication fingerprint against public keys in
  vpsfree-cz-configuration data/ssh-keys.nix using SHA256 of the decoded key blob.
  No private keys were read or copied.
- Fetched vpsAdminOS commit c065fa2f8485399737e20e8ef9e44299d0766654 into FETCH_HEAD
  because the configuration pin was initially missing from the local bare clone.
- Read the pinned livepatch module; no code edits, builds, or deployments.
- A direct metrics query from the logger to node1 port 9100 timed out; it did
  not provide evidence about livepatch state.

## Results
All times below are CEST (+02:00). Source: root@log.int.prg.vpsfree.cz,
/var/log/remote/cz.vpsfree/nodes/stg/node1/.

| Root SSH session opened | Unpatch began | Unpatch complete | Reload began | Patching complete |
| --- | --- | --- | --- | --- |
| Sep 13 19:58:28.823806 | 19:58:28.901918 | 19:59:08.371949 | 19:59:21.660908 | 19:59:23.899941 |
| Sep 13 19:59:40.161676 | 19:59:40.247920 | 20:00:20.034938 | 20:00:20.847936 | 20:00:24.200944 |
| Sep 14 03:49:13.269915 | 03:49:13.371936 | 03:49:53.398933 | 03:49:55.346909 | Not found through 04:30:20 |

All three sessions authenticated as root from 172.16.106.12 with fingerprint
SHA256:2jws4aMpQAFeQvmp/PGNAJ14d+S0OSh3NEP6iUpQpv8. Configuration revision
3d9ffa45c7e0388c96434fd3a6127d0a54c0b9ea, data/ssh-keys.nix:34, names this key
`snajpa`, with comment `snajpa@snajpaStation`. This identifies the key, not
necessarily the human who executed the commands.

The delays between session opening and unpatching are 78 ms, 86 ms, and 102 ms.
This repeated timing strongly suggests commands issued through those sessions.
The available syslog entries do not contain the SSH command text, so manual
commands versus an SSH-driven script cannot be distinguished.

Latest event evidence in current log:

```text
03:49:13.268208 sshd-session[37544] Accepted publickey for root from 172.16.106.12 port 48480
03:49:13.269915 sshd-session[37544] session opened for user root
03:49:13.371936 kernel livepatch: 'livepatch_6': starting unpatching transition
03:49:53.398933 kernel livepatch: 'livepatch_6': unpatching complete
03:49:54.562912 kernel livepatch: enabling patch 'livepatch_6'
03:49:55.346909 kernel livepatch: 'livepatch_6': starting patching transition
03:50:00.681691 sshd-session[37544] session closed for user root
03:50:12.869949 kernel livepatch: signaling remaining tasks
```

No later patching-complete message was found through 04:30:20. This is a log
observation, not proof that the current sysfs transition value is 1. Kernel NFS
timeouts for server 172.16.129.26 continue before and after the reload; without
task stacks/current state, they cannot be established as the transition blocker.

Configuration/code findings:

- node1 uses the staging channel and has no host-specific livepatch-disable setting.
- The inspected configuration pins vpsadminosStaging to
  c065fa2f8485399737e20e8ef9e44299d0766654. Its exact deployment on node1 could
  not be verified because node SSH is denied.
- At that pin, os/modules/services/livepatches/default.nix:365–371 runs
  `live-patches load && sleep inf`, has `live-patches unload` as its finish
  hook, and uses `onChange = "ignore"`. An ordinary configuration change is
  therefore not intended to restart this service; an explicit service stop/restart
  can unload the patch, as can invoking the utility directly.
- The unload utility writes 0 to the module's enabled sysfs file (line 210)
  and subsequently attempts rmmod (line 236).
- No livepatch transition messages other than the three cycles above were found
  in the inspected September 5–14 files. Older rotations were not scanned.

Mandatory change review and integration tests are not applicable: investigation
tracking only, with no implementation/configuration changes.

## Investigation limits retained for reference
- User clarified that the concern is vpsAdmin's stale observed-after bound:
  (2026-08-22 17:33:29, 2026-09-13 20:00:36]. This is now reproduced from code;
  see the follow-up diagnosis below.
- Which command or script ran via the snajpa key in the identified sessions?
  Host command auditing or the originating operator's command record would be
  needed to establish that detail.
- Does /sys/kernel/livepatch/livepatch_6/transition still read 1, and which
  tasks have /proc/<pid>/patch_state = 0? Direct node access is needed for this
  follow-up; do not force a transition or modify the running patch as part of
  this read-only investigation.

## Cleanup
User requested cleanup after handing implementation to a different Codex instance.
Inventory found no temporary files, project worktrees, clusters, or build outputs
owned by this initiative. Retain the diagnosis, reproduction, and agreed handoff;
register all three as portal artifacts and commit them with the final investigation
state and durable logging note in one ownership-handoff checkpoint.
Initial coordination commit: 7b00c83. No code, production state, branch refs, or
unrelated workspace changes are modified by cleanup. No archive, delete, or stop
command is run; the existing handoff paths remain valid.
Stable URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-node1-stg-livepatch-unload/

## Follow-up: vpsAdmin kernel-history timestamps

- Read vpsAdmin AGENTS.md, supervisor status ingestion, evidence snapshots,
  record_kernel_evidence.rb, history schema, WebUI rendering, and relevant tests.
- vpsAdmin inspected head / configured vpsadminServices pin:
  791ab3aa89e2f613979da6090b89785c78245db5. Read-only bare clone inspection;
  no vpsAdmin branch/worktree registered or changed.
- Root cause: record_kernel_evidence.rb:97 chooses the last public event's
  observed_before instead of the latest confirmation of that state. Removals
  and release changes use that stale value even with a fresh previous report.
- Introduced in 988ce4a0d1c0bbbe495963c5e8e3ed2190eaba1d on August 7.
- Ran `ruby work/2026-09-14-node1-stg-livepatch-unload/reproduce-kernel-bound.rb`.
  The pinned actual selection logic reproduces the stale August 22 lower bound
  for direct removal, removal after transition, and a release-only change.
  Application control uses the recent observation, confirming the asymmetry.
  Persistence is mocked; this is not a production database replay.
- Proposed fix: persist the latest confirmation time of the stable state,
  retaining it through transitions and unreadable reports. Keep event timestamps
  and immutable snapshots unchanged. Detailed edge cases, regression plan,
  additive migration/rollback contract, and historical repair limits are in
  vpsadmin-kernel-history-diagnosis.md.
- No source edits, new production tests, database writes, pushes, or deployments.
  Mandatory implementation review is not applicable to this diagnostic phase.
