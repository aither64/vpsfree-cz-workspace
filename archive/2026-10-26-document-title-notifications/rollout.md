# Document title notification rollout

Prepared rollout; no activation yet. Exact source, input and artifact identities
will be recorded as each phase completes. Session remains open after release.

## Authorization and targets

User requested aitherdev deployment through vpsfree-cz-configuration, then merging
and release after verification, and subsequently said "Implement the plan."
The accepted plan names dev-workspace, workspace and vpsfree-cz-configuration
`refs/heads/master`. Machine release means the exact session-owned claim only.

| Repository | Canonical SSH remote | Target |
| --- | --- | --- |
| dev-workspace | git@github.com:aither64/dev-workspace.git | refs/heads/master |
| workspace | git@github.com:aither64/vpsfree-cz-workspace.git | refs/heads/master |
| vpsfree-cz-configuration | git@github.com:vpsfreecz/vpsfree-cz-configuration.git | refs/heads/master |

Machine ID `vpsfree:aitherdev`; aliases `aitherdev.int.vpsfree.cz` and
`cz.vpsfree/machines/aitherdev`; confctl selector
`cz.vpsfree/machines/aitherdev`. Workspace application is installed in the user
profile, separately from the configuration-selected host module.

## Predecessor observation

Observed 2026-10-26 during preparation:

- Host: `aitherdev`.
- Live `/run/current-system` and system profile both resolve to
  `/nix/store/7za3la15ys7kq68sggbq6psvjqvqwrf7-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
- Selected user package:
  `/nix/store/vq113xqpwhz09sc7myd9zciyqvn1lsvv-dev-workspace-0.2.0`.
- Runtime source: `/nix/store/xzh3s2660hw9p1klfh26ck93l9msjy3w-source`;
  relevant source parity with `7e6d7c9cdb3388ab7abc720c034c15c21afbd686`.
- `workspace-portal@vpsfree-cz.service` active, PID 2017250.
- Profile Codex is package-owned, active Codex uses
  `/home/aither/.local/state/dev-workspaces/codex/current/bin/codex`.
- Authoritative session coordination status: no owned claims/jobs/reservations.

These observations do not reserve the machine or certify the later candidate.

## Preparation and gates

1. Runtime fix and consumer pins; exact source/input graph and complete branch
   inventory; quick checks and hooks.
2. Independent final review, including no migrations and pin consolidation.
3. Required package/VM/browser checks; configuration build and matching application
   closure; deployment-contract check; prepare copies before activation ownership.
4. Acquire aitherdev, inspect exact claim, dry-activate/system switch, profile
   switch with exact session and claim identity; reconcile any uncertain effects.
5. Verify exact live store paths, served assets, portal health, conversation
   continuity and background marker/focused-clearing behavior.
6. Integrate approved targets with individual short repository claims, hooks and
   SSH remote proof. Preserve independent review/equivalence evidence if rebased.
7. Verify deployed feature lineage integrated, inspect exact machine claim,
   release it and verify its state. No session lifecycle action.

## Candidate and verification

Feature worktree group:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-26-document-title-notifications/`.

| Repository | Initial exact base | Final head |
| --- | --- | --- |
| dev-workspace | 7e6d7c9cdb3388ab7abc720c034c15c21afbd686 | ef85bd0ae50714dbce51ba5807c0234875212a53 |
| workspace | c00fa4b3b36b41666d4c9210b6ae730bc83e27a4 | 6521561ff57caf84b7ddfa62eee59c7c47d62590 |
| vpsfree-cz-configuration | 880a6253f8d6cc1368e633f936b174792e86bff7 | c6fa188bfe10bf8acbe728ce8197b77e46705975 |

Workspace final reviewed base is `978a2f280185f3ae114c2db13130f13e6976b159`.
Old review candidate `c00fa4b3..3b5050c81` was refreshed to
`978a2f280..6521561ff` before review/deployment. Range-diff has exactly one '=';
all inherited base changes are tracking under work/archive. Complete filtered
source manifest, lock blobs and evaluated application derivation are unchanged.
No old candidate was deployed. Final review independently assesses this lineage.

Complete source/input graphs are reproducible from the exact commits' `flake.nix`
and `flake.lock`: workspace lock blob
`af685e9b581f2a415d5be9a9cdef14defa91d6ce`, flake blob
`e1d31175d575375072c9d35275428f02f998fbec`; configuration lock blob
`fd3baabc1a50b1156215e58033267d6226205379`, flake blob
`0dec4d0b2a649f2a47def3e29d0e6bad52070181`. Sorted compact JSON graph SHA-256:
workspace `189526100edc695a9067c3ff49dc34d35b11e3532ced4d30a6fb4053cf5b8ef2`,
configuration `a762ed5fb6ba52552642f614c5a9761327ce2a9dbd820cbb6af1fd19f9d579e3`.
Both select runtime `ef85bd0ae50714dbce51ba5807c0234875212a53` with
`sha256-yPBaMwSpf1354Q/qiZcgJq/C3EMxsuqtNZ69qYH45PI=`. Only that node differs
from each baseline. No schema/migration or native dependency changes.

Evaluated composed application derivation:
`/nix/store/bl252g0xdkh3hzskapcpf9xml5ixmf3q-dev-workspace-0.2.0.drv`.
Its direct Codex dependency equals the predecessor's:
`/nix/store/zgxck45jn2z9yf70rk6d794pdn6mq3ca-codex-package-0.163.0.drv`.
Host assembled Codex evaluation also remains byte-identical to the live
0.164.0 path/derivation recorded below. Build success/artifact still pending.

Baseline input identities to retain: extension
`767dfd587e346168e1443e65ccdb67ce748f3fe3`
(`sha256-om/+qNfQw6y74gjdzXfVG5AbHOQGysMefFZiqR92KP4=`), codex-web
`8b60554bc10c2a6bcbf9732a8b77ad959c317036`, llm-agents
`e85b99217baf13a38fc887b31338b1833f1159c0`. Both consumers initially select runtime
`7e6d7c9cdb3388ab7abc720c034c15c21afbd686`.

System Codex is intentionally separate from profile Codex. Configuration's
top-level llm-agents is `ea188d2f072e0ec8d5b71245e228803672801a22`
(`sha256-a4mZGtaldWR0DIsFbLgj9DI/5lVGbKDgQ6tbb2vWPfo=`), while the runtime's
nested llm-agents identity above remains frozen. At preparation, configuration
evaluation and the live system both select Codex 0.164.0,
`/nix/store/mdwhg24inrayrhh2q9hvcrcp1m0crz50-codex-package-0.164.0`, derivation
`/nix/store/vji6zpqs2w725wcyqd9hy6a50w6v272q-codex-package-0.164.0.drv`.
Its derivation is in the current system graph. Configuration nixpkgsStable remains
`da6dc0e7b26060f2f71ce3ef7088fb56ee44fa36`. Profile Codex resolves to
`/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex`.
This rollout does not change either selected Codex version.

Configuration uses pinned confctl revision
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`, package
`/nix/store/j5wxvlxdnsh2gyc6wbjx8xxfllqp4zmv-confctl`. Channel `dev-workspace`,
role/input `devWorkspace`; update through the channel, preserving generated
message and hooks. Pinned commands inspected, not run yet:

```sh
confctl build --yes cz.vpsfree/machines/aitherdev
confctl deploy --yes --generation GEN --copy-only cz.vpsfree/machines/aitherdev
confctl deploy --yes --generation GEN cz.vpsfree/machines/aitherdev dry-activate
confctl deploy --yes --generation GEN cz.vpsfree/machines/aitherdev switch
```

`GEN` must be the exact built candidate generation. Deployment flags do not
authorize rebuilding from a changed worktree or rebooting. Health checks remain
enabled. Application activation uses ordinary `workspace-host switch --source`
with the prepared workspace feature path, exact session environment and held
`DEV_WORKSPACE_CLAIM_ID`.

Final focused runtime suite: 75 tests passed in 8.5 seconds; changed JavaScript
syntax, targeted Firefox fixture readiness/journal checks and whitespace passed.
Consumer lock comparison, deployment contract, Ruby contract 4 tests/19 assertions,
format checks and required hooks passed. See final review packet for exact ranges
and commands. Independent review and longer verification were pending at this checkpoint; subsequent results follow.

Independent final review subsequently passed with no findings; see
[final-review.md](final-review.md). Review independently confirmed the exact
ranges, whole-branch history, rebase equivalence and no migrations.

Runtime GitHub Actions run
https://github.com/aither64/dev-workspace/actions/runs/40391274276 completed
successfully at exact head `ef85bd0ae50714dbce51ba5807c0234875212a53`: `fast`,
`creation` and `archive` all success; feature-branch `host` job skipped. This is
the required packaged/creation/archive verification, not a host activation result.
Local composed checks/build, configuration build and native Firefox acceptance
remain in progress under fresh Luna/low verification utility.

Authenticated HTTPS preflight of this exact session route and the title asset
returned HTTP 200 through the configured CA. BatchMode root SSH to
`172.16.106.40` works. Local `sudo -n` has no cached credential; deployment uses
confctl/root SSH. Portal credential stayed solely in process memory and was not
printed or written. Predecessor title asset SHA-256
`7de4d0ff72a6666aa3a1be0ee73a61fa4533f7cbcfba7804f06b91931e77fcd0`.

## Activation, integration and release

Not started. Failure or uncertainty retains the machine claim until effects and
integrated deployed lineage are reconciled. Recovery uses a compatible corrected
successor and preserves private runtime/event state.

Prepared detached integration targets under the owning worktree group:
`dev-workspace-merge` at `7e6d7c9cdb3388ab7abc720c034c15c21afbd686`, and
`vpsfree-cz-configuration-merge` at
`880a6253f8d6cc1368e633f936b174792e86bff7`, both clean at preparation. Configuration
target hooks were prepared in the pinned shell; identical Gemfile/lock permitted
an ignored `.gems` link to the same-session feature environment. Overcommit
signature, post-checkout and post-merge hooks ran successfully. These targets
still require fresh authoritative remote/cleanliness checks under their claims.

Shared workspace integration must preserve all unrelated dirty paths and the
index. Prepared master `978a2f280185f3ae114c2db13130f13e6976b159`; feature descends
from it, flake files clean and no staged entries at preparation. Acquire the
workspace repository claim first, then nonblocking `.git/dev-session-tracking.lock`.
If busy, release ownership and retry later. No claim has been acquired yet.

## Initial longer verification checkpoint

Configuration build passed at original config head c6fa188b: generation
`2026-10-26--21-11-12`, derivation
`/nix/store/0y7arfd02l3yrw7h2gbk2z0yca3zjw7d-nixos-system-aitherdev-26.05.20261021.da6dc0e.drv`,
output `/nix/store/8z0anan65y46412nbk95flhdb57glm61-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
Not deployed. Original runtime CI fast/creation/archive passed as recorded above.

Native Firefox ReadBudget passed; Tabs passed new background title/discard
transitions, then failed existing durable-original-retry step. Failed log
`verification/firefox.log` establishes exactly one DOM submit but two HTTP
attempts/native mock dispatches/journal entries, no unknown receipt. Implementer0
traced zero-byte connection close after upstream acceptance allowing transparent
Firefox HTTP replay, plus a fixture Send implementation without native
idempotency. Accepted bounded fix changes only that fixture: reconcile before
dispatch, append/fsync journal once, inject a truncated non-success gateway
response after actual acceptance, verify unknown recovery and repeated original
identity through real handler. Truncated 2xx would be insufficient because the
pinned browser client accepts 2xx despite JSON parse failure; use 502 to model
an uncertain gateway response. Product behavior and durable acceptance
assertions remain unchanged. Preserve this evidence; no blind rerun accepted.

Source changes are folded into the unmerged runtime correction; both consumer
pins will consolidate to the final replacement head. Original reviewed ranges,
source graphs and undeployed build results remain historical evidence, not proof
for refreshed artifacts. Affected review and verification are required.

## Refreshed final candidates (not deployed)

| Repository | Final base | Replacement final head |
| --- | --- | --- |
| dev-workspace | 7e6d7c9cdb3388ab7abc720c034c15c21afbd686 | d2099c62656bc2a36c306918a92832ba1e1a0cc0 |
| workspace | 978a2f280185f3ae114c2db13130f13e6976b159 | e3b44a8b59c656e0ecec0bd692ad7f72963f7e61 |
| vpsfree-cz-configuration | 880a6253f8d6cc1368e633f936b174792e86bff7 | 514e6a06ef72c3c2b4c50a592ff58b3d6fcd7cd2 |

Original ranges/heads and failed-run evidence above are retained. Runtime
ef85->d209 changes only `firefox_tabs_test.go` (+99/-7) and commit explanation;
all production controller, assets, browser runner and prose are unchanged.
Both consumers consolidate the replacement into one final pin each from the
original accepted base; no superseded pin history is retained. New pins are
not patch-equivalent to old revisions, but no old candidate was deployed.

Runtime selection is now `d2099c62656bc2a36c306918a92832ba1e1a0cc0`,
`sha256-kQkKnjQVSYZw3ZDNan8EakG7HS29wIbHGZ14B7Xq5vA=`. New complete graph
identities: workspace lock `fc043cc6829bdd35d020719d9ef82d02a1a1a2f8`, flake
`36d9473ed7c0aa2b5f8efcbfccd23ed8ee3c3b8c`, graph SHA-256
`e0036e4a7217e8633d701279e1f7f03a3ec0be0dd9c10398f91c8c5214a64482`;
configuration lock `d1933449b7264273a05aa25c59b0a34aab7087db`, unchanged flake
`0dec4d0b2a649f2a47def3e29d0e6bad52070181`, graph SHA-256
`1af2521240337460f2cd2e60e07ec151477d8ba9179973d724cc423b861a862c`.
Both semantic node/edge comparisons and composed deployment contract passed.
Only runtime node differs from original reviewed graph; all sibling identities,
follows and distinct system/profile Codex dependencies remain unchanged.

New application drv `/nix/store/wvbhwr6zl16rd51yfpmjf31vwjl368b5-dev-workspace-0.2.0.drv`,
expected output `/nix/store/ch3lnb3cd89xkqrnb0va3yizq3sq71x1-dev-workspace-0.2.0`.
Evaluation only at this checkpoint; new build/activation still pending.
Quick Go fixture tests 3/3 passed (0.499s), config hooks passed, all three feature
refs published over SSH with bound leases and fresh exact-head proof.

Affected independent final review uses the same reviewer and
[affected-review-packet.md](affected-review-packet.md). Refreshed verification
commands in `verification-brief.md` retain original logs and target new heads.

Affected review subsequently PASS with no findings; see
[affected-final-review.md](affected-final-review.md). Native refreshed Firefox
acceptance passed both Tabs (110.63 seconds) and ReadBudget (25.86 seconds), total
136.543 seconds at exact runtime d2099c62. This includes background title updates,
focused clearing, native discard/restoration, hidden heavy-read limits and the
unchanged original durable-retry assertions. Failure diagnosis and fixture
correction are preserved above; success is not used in place of diagnosis.

Refreshed configuration build passed at exact 514e6a06, generation
`2026-10-26--21-29-03`, system derivation
`/nix/store/67x1qh521xdnmrm0xdnzvhvzwlrv131k-nixos-system-aitherdev-26.05.20261021.da6dc0e.drv`,
actual built output `/nix/store/avqrck9bjnxmqli5qlmcbnk76ziijvfv-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
The exact generation.json and nix-store --query --outputs agree on that output;
its sw/bin/codex resolves to the unchanged mdwhg24...0.164.0 package.
Logs under `verification-refreshed/{configuration,runtime}.log`. Not yet deployed;
composed application and exact-head CI checks remain in progress.

Prepared system copy via pinned `confctl deploy --yes --generation
2026-10-26--21-29-03 --copy-only cz.vpsfree/machines/aitherdev` exited0. No
activation or machine claim yet. Existing generation's partial role metadata
reports nested llm-agents e85; the same discrepancy exists in both original and
refreshed generation.json. Complete committed lock graph and actual system
sw/bin/codex prove the unchanged top-level ea188/0.164.0 selection; metadata is
not used as a complete input-graph authority. No unrelated metadata change made.

## Activation underway

Refreshed batch all exit0: composed application flake/default checks, exact
configuration generation build, native Firefox Tabs/ReadBudget and CI40394771174
fast/creation/archive. Current exact default application build/deriver agree:
/nix/store/ch3lnb3cd89xkqrnb0va3yizq3sq71x1-dev-workspace-0.2.0 from
/nix/store/wvbhwr6zl16rd51yfpmjf31vwjl368b5-dev-workspace-0.2.0.drv.

Acquired machine claim1667fb9f-cf93-467a-91b2-c9f8e9aef81f, owner
05463215-9651-4f41-8989-5f6a2d3bfae9, at2026-10-26T20:40:13Z. Exact held
state/session/resource rechecked immediately before lead's activation driver.
Source heads verified clean/exact before driver: config514e6a06, workspacee3b44a8b.
Driver logs/status in deployment/. Dry-activate exited0 (22.82s); system switch
and then user-profile switch are next stages. All effects must be reconciled
before release; no repository merge claim is held during activation.

## Verified deployment, integration and release

Lead activation driver completed all stages with exit0: dry activation22.82s,
system switch37.87s, user-profile switch65.32s. No unfinished command effects.
Live /run/current-system and /nix/var/nix/profiles/system both resolve to
/nix/store/avqrck9bjnxmqli5qlmcbnk76ziijvfv-nixos-system-aitherdev-26.05.20261021.da6dc0e.
Selected profile resolves to
/nix/store/ch3lnb3cd89xkqrnb0va3yizq3sq71x1-dev-workspace-0.2.0.
System and profile remain at their separately frozen Codex0.164.0/0.163.0.

Authenticated HTTPS live checks passed using configured CA: own session page,
attention and team stats all HTTP200; attention fresh with retained root thread
01a179a6-3faa-7223-b930-82156d51516d. Router, portal and Codex user services active.
Served session loads session-attention.js?v=3; response bytes equal exact reviewed
source, SHA256b8902bfe4c5e50d5c1cf88bbb484d24af168cedd231fb16e3c48d6c24190e87d.
Native Firefox tests on those same shipped-source bytes proved hidden ✓/?,
focused clearing, hidden heavy-read limits and durable retry; no live native
question was fabricated to exercise title state. Existing open pages need reload.
No credential was printed, saved in this record or included in artifacts.

Fast-forward merges with normal hooks/SSH push/fresh remote equality proof:
- dev-workspace/master=d2099c62656bc2a36c306918a92832ba1e1a0cc0; repository
  claim25e3bb4d-44aa-48b7-8e24-ab1052203cb0 released20:44:37UTC.
- vpsfree-cz-configuration/master=514e6a06ef72c3c2b4c50a592ff58b3d6fcd7cd2;
  claimea8600ff-09f1-4283-b46d-15bdfb1e1ef7 released20:45:27UTC.
- workspace/master=e3b44a8b59c656e0ecec0bd692ad7f72963f7e61; claim
  5b439f73-ba7b-4403-bcb2-aefa5599112c queued briefly, held notice verified against
  authoritative status; acquired nonblocking tracking lock then fast-forwarded
  shared master, pushed all inherited tracking history and feature, verified
  exact remote, released20:46:31UTC. Unrelated dirt/index preserved.

Fresh remote equality and Git ancestor proof for all exact deployed/final heads
was repeated immediately before machine release; complete deployed feature
lineage integrated without any nonancestor replacement. Deployment driver state
terminal, live paths exact, claim1667fb9f... held by exact owner05463215... rechecked.
Normal machine release succeeded20:47:17UTC and authoritative state confirmed
released. All repository claims released; no owned jobs/reservations remain.
Compact raw proofs: deployment/{status,live-verification,integrated-lineage}.json.

Automatically triggered master CI40398311740 at exact runtimed2099c62 remains
under fresh Luna/low watcher, separate from released machine. Deployment and
feature CI had already passed; master host-only job result remains pending.
Session is open; no archive/delete/stop/lifecycle helper/cleanup action performed.

## Final verification and completion

Master CI https://github.com/aither64/dev-workspace/actions/runs/40398311740
at exactd2099c62656bc2a36c306918a92832ba1e1a0cc0 completed success; fast, host,
archive and creation all success. Fresh standalone Luna/low watcher verified
actual danger-full-access/never launch and retained utility policy; gh watch
exit0, no failures or retries/cancellations, all watcher operations terminal.
Final report/details under verification-refreshed/master-ci-{report.md,final.json,log}.

No remaining owned work or resources. Exact final feature heads integrated and
verified, state.md lifecycle complete. This is a tracking state only: session
remains open; no archive/delete/stop/finalization/private lifecycle helper or
worktree cleanup. User should reload existing tabs for assetv3. Browser throttling
remains the documented background-update limit.
