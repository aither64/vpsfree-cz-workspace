# Refreshed development demo — 2026-11-18

Package `82e99ce8` is delivered for lead acceptance. The refreshed cluster is running/ready, applied pending is null, and the session remains open. Both isolated fixture VPSes are physically stopped by the demonstrated enforcement. All owned command handles are terminal/joined; intentional runner719334 and the services/node1 guests remain running.

The local result is 20 unique source events, 24 reports, 20 saved evaluations, four completed/sent actions, two successful physical Stop chains and 24 delivered incident messages. Mailpit contains41 messages:24 incident and17 `user_new_login`. Every incident message has plain and HTML bodies. No event, create or reset was replayed for mail or UI recovery.

[Completion](completion.json) binds the [artifact manifest](artifacts.json). Exact result IDs and source/system/input paths are in [result-identities.json](result-identities.json); command, utility-item and effects accounting is in [native-effects.json](native-effects.json). [UI acceptance](ui-acceptance.json) binds the retained route/media evidence. Final read-only health snapshot: [final-health.json](final-health.json), sampled 2026-11-18T08:09:19.834568+00:00.

## Reviewed source and actual running inputs

All seven final source worktrees are clean. No source/Git edit, fetch, pin or registration was performed in this execution package.

| Project | Head | Tree |
| --- | --- | --- |
| vpsadmin | `0117035f22a465c2b3d78f02df05bc828775afab` | `90b3f6101cf089124b77cfe3f0209870a2e986db` |
| vpsadmin-webui | `b1fb37b0de3af6ef2f6f9e5f4f73ea0296b19c89` | `7f62ae155b397e22614c0ffc10c36451a1ec99c6` |
| vpsfree-notification-templates | `125f132a4c45ea8e8dbf6c392c7ca5f96e15a508` | `092c3638f123f1c275f6c48132bd58d344f9a1a4` |
| vpsfree-cz-configuration | `1efed32a70a91e8705be2ceeb6b7dac4ad19e10c` | `457391d83177a8ab7a5276078c2ba8ef15b4d6f5` |
| vpsadmin-go-client | `bd0d1d2f548c128f4fbc8657679450b7f998e181` | `91f32aa03288066271f8ed9f79045260d1c57573` |
| vpsadmin-rust-client | `e34ef441468b3e7579719ceb68d1b0b2cce8d101` | `49af7ad097d468d8b1717ddac1ef5a5557fe46fd` |
| vpsadmin-typescript-client | `3cb7cf838a607bbafab207307e11626e57cdec8c` | `a227d98471882fb49bf2464df1dfdea05202cda4` |

No OS worktree was selected. The provider used existing local `origin/staging` `ccd51ed38ebffa2e744f7f8847668bc2e3413378`, tree `489255fcbda37685a63b5878dffb183219e4bd00`, without fetching. Literal SDK/export/KB generation remains backend5aa1. Retained alerts PASS is actuald304; final PHP PASS is actual011. Their graphs/checks are not relabelled as this demo's graph.

The actual config is `/nix/store/127hdsydqcmz5ydnsqhkavzxcszk61rz-os-test-vpsadmin-devcluster-2026-10-30-oomd-abuse-policy.json`, SHA256 `94779292b6abdf9c8a46bba28fc59e4d035bae3255231c8a1c0f36ffa2f1e436`. The complete captured input graph has6707 derivations/869 source inputs; the actual runtime graph has1831 store paths. [Host-runner provenance](host-runner-provenance.json) binds six runtime roots and1841 recursive store paths. Raw graphs and applied config are restricted private artifacts bound by path/hash.

Actual systems are services `z7k5zs6489722y9y6rr9ib0yn379ngqd`, node `zv0wss6qmc5s1ip995ycf66nb5b61pr1`, and React container `df906mwmzw03887wrl2pv5a4zqnfmv63`; full paths are in [activated-react-paths.json](activated-react-paths.json) and [result-identities.json](result-identities.json). Actual backend common source retains2996 reviewed tracked files:2986 byte-equal,10 ordinary shebang substitutions with identical remaining bytes. Ignored/generated payload is inventoried separately and not asserted reviewed.

Root resolved the historical React metadata hold after the architect's [packaging recommendation](../../design.md#actual-react-package-provenance--demo-acceptance-recommendation-2026-11-18). Actual frontend `0fb7nng36g9820s28zhnfgklxsyrqp31` and BFF `jrcw5s6bqc9pnkyqay2lkg48gf1x6fwd` are accepted as externally source-bound DEVELOPMENT outputs. All2835 retained cleaned-source blobs match reviewedb1fb. Effective nginx root and the active BFF process script/executable bind those exact outputs. Embedded `unknown / dirty=true / source=unavailable` and UI “Version unavailable” remain literal. This does not claim a clean release, equality with standalone package outputs, or transferred whole-package checks.

## Reset, activation and capture prerequisites

The one authorized public reset was consumed at06:41:58UTC. Reset/init/start exited0; start wrapper89743 and fresh Luna18202 joined at07:01:09UTC after19m11s. [start-terminal.json](start-terminal.json) and [start-evidence.json](start-evidence.json) are immutable historical snapshots, including their then-active metadata hold. No second reset, separate stop, private lifecycle helper, rebuild or downgrade occurred.

Fresh boundary observations were170173456384B free disk,57770332160B available RAM and37839179776B free shm. Shared use was counted once.100GiB incremental disk+20GiB floor,48GiB RAM,20GiB shm and one Nix job/core were allowances, not measured peaks or quotas. No unexpected local kernel compilation was observed.

The cluster remains single/bridge, DNS disabled, React/Mailpit enabled, no storage profile. Only the preserved intended regular config was restored; no old disk, DB or applied envelope was restored. Private credential/config files remain restricted, ignored and untracked. Credentials are available only through the existing portal Accounts/secret channel.

Ordinary notification reconciliation loaded exact templates125f. All five incident families×CS/EN×subject/plain/HTML give30 matching DB fields (normal parser subject chomp). Exact declaration1efe digest `f3b4549ab502d40fe8bb72de6f4a22e1d9ec4dfdf8aa692ff5e25003a3df5e78` is installed as regular component-owned0440 files at the actual API/supervisor/database configDirectories. Normal component restarts are active; independent package loads and subsequent running supervisor saved evaluations prove the same digest, soleoomd declaration5/10, no selector and unsuppressed default. [Activation log](activate-public.log), [migration proof](migration-predecessor-proof.json) and capture config/endpoint proofs retain the details.

Exactly one migration20261030180000 follows20261006120000; obsolete20261115120000 is absent. Nodectld sends only to capture SMTP127.0.0.1:1025; Mailpit listens there and on HTTP127.0.0.1:8025. Authenticated PHP/React/API/Mailpit readiness passed.

## Fixture and event result

Both ordinary API creates used1CPU/1GiB RAM/4GiB disk/no IP. Create chains1/2 completed. Before any source event, node state proved both running and physical quota4294967296B each. Cached `is_running=NULL` is retained literally; physical state and completed chains supplement the strict policy/resource/permission/zero-event baseline. Baseline counts were0/0, current declared limits5/10, shared permissiontrue, null overrides, demo global modeenforce.

| Identity | CS | EN |
| --- | --- | --- |
| Owner / VPS | 2 /1 | 3 /2 |
| Hostname | incident-final-cs | incident-final-en |
| First ordinary report / MailLog | 1 /7 | 2 /8 |
| Warning notice / trigger / action | 7 /6 /1 | 12 /11 /2 |
| Warning MailLog | 12 | 17 |
| Stop notice / trigger / action | 23 /17 /3 | 24 /22 /4 |
| Real Stop chain / physical transaction | 29 /45 | 35 /51 |
| Stopped MailLog / SMTP transaction | 33 /53 | 34 /54 |
| Final node state | stopped | stopped |

The saved20-tuple plan predates publication; stdout and exact guest files are parsed-tuple equal. [Publisher coverage](publisher-coverage.json) proves20 unique attempt markers,20 confirmations and exact plan/source-report key equality across ranges1–1,2–5,6–10, each once. These are qualifying synthetic oomd events, not claims of actual memory abuse. First ordinary mail was inspected before further events; warning mail before events6–10. Queue/sending/sent states were retained until authoritative completed/sent state. All24 SMTP transactions are done/status1. Four summary actions are completed/sent; physical Stop handle1002 transactions45/51 are done/status1 and independent node state is stopped. Stop contributors are bounded5shown/10total. Saved first evaluations remain unchanged through later counts10/5 and10/10.

## Authenticated views and mail

[ui-acceptance.json](ui-acceptance.json) records24 baseline views,8 warning owner views and40 unique final own views across PHP/packaged React/admin/CSowner/ENowner. Actual threshold links point to Incidents; current limits/counts, saved ordinary history and source links were inspected. Admin controls and owner read-only views were retained. Four foreign-report denials prove owner isolation: PHP CS/EN object-not-found and settled React CS/EN pages, with backend404 responses and no foreign hostname. Two-policy UI behavior remains within owner4's separate accepted fixture; no second policy was introduced here.

All six selected ordinary/warning/stopped messages in both languages were inspected in actual Mailpit HTML frames and Text tabs, including screenshots and full rendered text/footers. Current selected message IDs are in [mailpit-selected.json](mailpit-selected.json). Final41-message total includes17 incidental login messages separately; no mail was removed.

## Preserved failures, corrections and limits

| Evidence | Exact reconciliation |
| --- | --- |
| Original42925 create exit1;32113 effects read exit1/noJSON | Retained. Corrected deployed-cwd43580 read proved zero admitted VPS/chains/events before continuation; preparation effects were retained. |
| Guarded create13816 exit0 | Actual packaged Ruby offline87596 control proved own filename consumption and unchanged forwarded argv with no HTTP. Only the two planned creates then ran once. |
| Utility12870 CLIexit0 but INCOMPLETE | Did not observe the fresh command or inspect artifacts. Visible active-parent fallback binds13816 exit0/join, exact command/log/time and actual effects; no watcherPASS claimed. |
| Cached-running guard35900 failed | No cache write or monitor investigation. Node-running+completed chains and strict unchanged policy/resource/zero-event checks accepted by root. |
| Local stopped-mail selector63205 exit1 | Corrected expected5shown/10total using the same captured raw snapshot; no mail/event mutation or refetch. |
| Final browser81860 exit1 / observer68291 FAILED | Actual CS foreign denial retained; local regex omitted “objekt nebyl nalezen”.15 own views retained. |
| Resume61089 exit1 / observer5866 INCOMPLETE |20 more own views and PHP EN denial retained; React Loading was provisional. |
| Tail62980 exit0 / observer33751 PASS | Only remaining5 own views,2 settled React denials and six Mailpit renders executed. |
| Graph parser/host query corrections | Older Nix JSON-shape failure retained and corrected from same raw graph. Initial host query diagnostic was not retained; this explicit evidence gap remains in host-runner provenance. |

Original preparation8c15355a and manifest47a40b9d remain exact; all24 bound preparation artifacts still hash-match. Earlier ee/d26/d304 runs, original demo/media/failures and uncertainty outside this reset remain literal. No current local result resolves those historical fences. Root owns final backend hosted CI; this packet makes no hosted final-success claim. Canonical KB media/runtime remains parked. No production/default integration, registry release, staging, cleanup or session lifecycle action occurred.

This package adds execution evidence only; no application documentation/source change is needed. Root retains state.md and final acceptance. Capacity is available after this delivery, with no next execution package started.

## Browse the running demo

- [PHP CS Incidents](https://webui.aitherdev.int.vpsfree.cz/?page=adminvps&action=incidents&veid=1)
- [React CS Incidents](https://newadmin.aitherdev.int.vpsfree.cz/app/vps/1/incidents)
- [React EN Incidents](https://newadmin.aitherdev.int.vpsfree.cz/app/vps/2/incidents)
- [CS stopped email](https://mailpit.aitherdev.int.vpsfree.cz/view/6UorASrljwGRvw9thJP6sp)
- [EN stopped email](https://mailpit.aitherdev.int.vpsfree.cz/view/4XTwanzfVtc0sIDu7a5Un6)
- [Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)
