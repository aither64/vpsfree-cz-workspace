# Verification result

Final runtime ced8e76ec73fbc4809ac30af60903874590b82f6; workspace 65926d048fc110b5c55b6eef793d5caa71c857f1; configuration b2c39068b062f82c7842eb02ad6eec223c185ba6. All three feature branches are published and clean, with no default-branch integration or activation.

| Check | Result | Evidence |
| --- | --- | --- |
| Focused Ruby integration | 32 runs / 158 assertions passed | review-remediation.md |
| Lifecycle admission | 4 runs / 13 assertions passed | review-remediation.md |
| Schema-1/schema-2 GC focus | 3 runs / 16 assertions passed | review-remediation.md |
| Browser coordination contracts | 13 tests passed | review-remediation.md |
| Go package capability metadata | Passed | review-packet.md |
| Full runtime package and host contract | Passed | runtime-final-package.log/status |
| Real user-manager fixture | 1 run / 5 assertions passed | systemd-final.log/status |
| Rooted final runtime rebuild | Passed, exact same source | runtime-package-rooted.log/status |
| Native notification acceptance | Passed, actual Codex 0.163.0 with local synthetic provider | native-notification-final.log/status |
| Notification protocol | Passed | notification-protocol.log/status |
| Composed workspace application, deployment contract and instructions | Passed | workspace-package.log/status |
| aitherdev exact configuration build | Passed | aitherdev-build.log/status |
| Final lock composition | Passed; one runtime node changed per consumer | final-pin-proof.json |
| Runtime CI | Success, run 38961125758 at final runtime SHA | runtime-final-ci.json |

CI: https://github.com/aither64/dev-workspace/actions/runs/38961125758

## Native acceptance scope

native-notification-check.go is a session-owned evidence program, compiled in the runtime's Nix environment and run against the exact built generic package. It uses an allowlisted private HOME/CODEX_HOME, a local synthetic Responses SSE provider and two disposable native threads. No real credentials, network model calls or live session state are involved. It proves that idle threads make no provider requests, the built coordination helper wakes each once while retaining gpt-5.5/high, and retries after helper/native App Server restart reconcile the original message identities. Four synthetic provider requests total: two initial materialization turns and two notification turns. Both threads, provider and App Server are stopped and disposable data removed by the program. Generated evidence binary was removed; source retained.

This does not prove a full live system/profile deployment, live reservation contention or production generation handover. The user-manager test exercises actual systemd scheduling/restart but uses a fixture worker, fake native receipts and stubbed tracking publication. The real built notification helper and native server are covered separately. Live end-to-end acceptance requires managed session startup recovery and coordinated activation.

## Retained build outputs

- Generic runtime: /nix/store/3vzmicdbbvbrimsksv451x4xryi4lnqq-dev-workspace-0.2.0, rooted by session-local runtime-package link.
- Composed workspace application: /nix/store/0h1n61gsw2xcwv0xn6imkldc9gsbazyp-dev-workspace-0.2.0, rooted by workspace-package link (additional result links retain checks).
- Aitherdev: /nix/store/bwknpx1hj6b7lbg2j3r5kbks4j5pqsgz-nixos-system-aitherdev-26.05.20261015.26f4107, confctl generation 2026-10-16--22-29-04 under the configuration worktree's .confctl/generations/cz.vpsfree:machines:aitherdev/.

No local kernel compilation occurred. No verification operation remains running.

## Diagnosed failures and monitoring

Original package checks already passed before GC collected the unrooted result; repeated exact build retains an explicit result root. Original systemd failure was a fixture observation race, corrected to await event publication rather than the earlier finalizing phase. Original native fixture omitted required client_version; the real helper correctly refused it, and the corrected fixture derives that field from the exact native --version. Original confctl attempt used an unsupported global --yes; help confirms build --yes, and the corrected build passed. Original failure logs remain retained. See review-remediation.md for dispositions.

Fresh gpt-6-luna/low verification utilities launched and monitored initial and final runtime batches. Fresh delegation became unavailable for the remaining batch; the lead reported the dev-session-monitor fallback and used bounded parent observation. Superseded CI cancellation was attempted for exact old run 38960251749 and refused HTTP403 by GitHub token permissions. Final successful run was untouched.
