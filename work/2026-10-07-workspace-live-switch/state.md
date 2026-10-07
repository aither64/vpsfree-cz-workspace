---
lifecycle: active
---

# Live workspace switching

Current phase: deployed, merged and handed off; CI continues without waiting.
Implementation, quick checks, independent review, packaged contracts, exact
native recovery, final builds and CI passed. Approved scope is recorded
in [plan.md](plan.md); detailed brief is [design.md](design.md).

## Phase checklist

- [x] Investigation and scope decisions.
- [x] Dedicated threadless initiative created and ownership recorded.
- [x] Implementation and documentation.
- [x] Quick checks, commits, final branch inventory and independent review.
- [x] Packaged and exact-binary integration checks; CI.
- [x] Matching aitherdev host/application deployment and live-switch proof.
- [x] All three approved master targets integrated at exact final heads.
- [x] Final handoff; user explicitly excluded waiting for master CI.

## Authorization and ownership

User approved implementation, one initial idle cutover, aitherdev deployment,
and integration of dev-workspace, workspace and vpsfree-cz-configuration into
master. No archive/delete/branch deletion was requested. This initiative was
created by this conversation with no Codex thread or retained team. Existing
shared changes are unrelated and must be preserved.

## Current evidence and next action

`dev-session current` initially refused because no current session existed;
both DEV_SESSION identity environment variables were absent. Creation returned
slug 2026-10-07-workspace-live-switch and threadId null.

No implementation, review, deployment or integration work remains. Master CI
continues in GitHub; the user explicitly directed "no waiting for CI". No further
CI observation is scheduled here. Lifecycle remains active while that external
run is incomplete; the session and feature refs remain available for follow-up.

Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-07-workspace-live-switch/

## Implementation and quick verification

Lead implementation is complete for the runtime restart decision and stable
member-report profile routing. All existing host guards and payload schemas
remain; livePackageSwitchPolicy 1 is additive. Focused verification passed:
126 Ruby host tests (1018 assertions), 3 report-binding tests (18 assertions),
Go cmd/workspace-portal, internal/teamruntime, internal/agentteams and
internal/web. The explicitly tagged exact-native integration fixture compiles;
execution follows independent committed-deliverable review.

The configuration worktree was created from origin/master 23412037590f after
entering its existing configuration Nix environment from that checkout's cwd.
Calling nix develop against that path from the shared root failed because the
configuration tools shell expects ./Gemfile. No application or profile mutation
resulted.

Runtime and both downstream pins are committed and published.
See [review packet](review-packet.md) and [rollout](rollout.md).

## Review phase

Implementation, publication, downstream pins and quick checks complete.
Independent high-risk four-lane review requested; see review-packet.md.
No deployment or integration tests started yet.

## Final review result

Standalone /root/final_review (installed gpt-6-astra/xhigh review policy)
completed general, architecture, scope and risk lanes on runtime 89bf6794,
workspace 1856956e, configuration 2a3a56da. No Blocking/product findings.
One Important test finding: command approval kind must be `command` per pinned
codex-web, rather than `commandApproval`. Narrow expectation correction is
compiled, inspected and folded into the owning unmerged runtime commit.
No review rerun required under the skill's narrow-fix rule.

Reviewer explicitly concluded coherent whole-branch history, no obsolete
approaches or compatibility paths, and no migrations. Residual checks:
packaged/native tests and real profile/systemd switch evidence, including
report delivery. Deployment and integration remain pending.

## Final reviewed correction and selected heads

Narrow approval-kind fix inspected and compiled, no product patch change.
Runtime final head f5d5ecf7f519d526d60c2d9f75c2b2e921c5cbc6.
Workspace pin commit 2008dd61; configuration generated pin d713f5d6.
Both generated selection streams consolidated to one commit. Deployment
contract passes again with unchanged extension/siblings.

Superseded runtime CI run 37664183677 cancellation was attempted after
force-push and refused with HTTP 403 (token cannot cancel Actions runs).
No other branch's workflow was targeted. Reviewed predecessor CI 37662407771
was successful; final-revision evidence is still required.
Fresh /root/runtime_checks watcher gpt-6-luna/low owns packaged runtime and
exact-native tests under installed utility digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd,
native config dw_024841fba072af1d79bd78026612eaeca055acfa31ecc89f.

Final runtime CI 37664227075 succeeded on f5d5ecf7. The fast lane evaluated
all checks and built the package/focused checks (12 minutes); host VM lane is
not triggered for feature pushes. The local watcher remains responsible for
packaged and exact-native completion.

## Packaged checks and native fixture diagnosis

Packaged f5d5ecf7 runtime built successfully. Flake evaluation, Codex package,
host package and catalog contracts passed. The packaged suite passed 126 tests
with 988 assertions (3 skips); the contract suite passed 401 tests with 5408
assertions (12 skips). Logs are retained locally under logs/.

The native fixture needed corrections to its setup: explicit empty environment
maps, an initial raw turn/start to seed a new thread's saved rollout, and HTTP
426 for WebSocket probes to select the mock provider's HTTP fallback. The last
matches the existing native naming fixture. These are fixture-only corrections;
the reviewed production patch is unchanged. Active lead/member turns, native
queue retry identity and exactly-once report retry now pass. Approval request
replay passes, but browser response needs matching command-item evidence; the
next diagnostic run records native thread/items/list. No product restart was
performed, no unrelated session was accessed or interrupted.

Native thread/items/list confirmed the pending command item is unavailable;
browser response refused without weakening the authority check. Fixture-only
terminal JSON-RPC fallback and before/after authority evidence received a
general/risk followup review from the same gpt-6-astra/xhigh reviewer at
bf40b54d. One Important finding: idle includes failed/interrupted turns and
cannot prove success. The narrow correction asserts the original turns completed
their synthetic responses and the exact command item produced synthetic-approved.
The Advisory request to compare authority before and after reconnect was also
implemented. Quick tagged compilation and focused inspection passed; no full
review rerun is required. This proves native protocol recovery, not actual
terminal UI or complete retained MCP delivery; real deployment remains separate.

## Final revisions and native acceptance

- Runtime: 5b17c6965228f1d7bbce45817294b54894f737ef.
- Workspace: 2e61afb70112599dd7d5ab98905260d7d06a2197.
- Configuration: 16c19f3c3210f0d03bff5b9db0ca04404acc1fb9.

All three feature branches are published and each retains one coherent commit.
Only the workspace's nested runtime lock node changed; extension, sibling nodes
and follows remained fixed. Configuration changed only devWorkspace's locked
revision/hash/time. Confctl hooks passed and its generated message was retained.
The final cross-project deployment contract passed at runtime 5b17c696.

Fresh /root/native_recovery_check gpt-6-luna/low passed the isolated native test
on 5b17c696: preserved native PID 826336; active lead/member turns, queue/report
retry identity and exactly-once delivery, command/question replay and completed
original turns. Command authority was false before and after reconnect; native
terminal fallback executed the exact original command and synthetic-approved
output. Question authority remained true. Native binary 0.160.0 SHA256
d46bd2016f2a24e263a168237fbe50e32aae009ea2c209b0227fb90a61799f04.

Fresh /root/downstream_verification gpt-6-luna/low owns workspace evaluation,
package/deployment-contract build, aitherdev configuration build and exact
runtime CI run 37670751875. Installed utility digest/settings remain unchanged.
All superseded feature CI runs completed successfully; none remains to cancel.

Workspace evaluation and final package/deployment-contract build passed. Selected
application output is /nix/store/wfrg7ybg5qf0xvz4gcyy1apl64rr0asf-dev-workspace-0.2.0.
The watcher stopped before aitherdev evaluation at confctl's confirmation prompt
(EOF on noninteractive stdin), leaving deployment and final CI unattempted.
No configuration failure or host mutation occurred. `confctl build --help`
confirms --yes for the authorized build; fresh verification will use that flag
and preserve the initial prompt-failure log. Deployment already uses its own
documented --yes and --no-interactive options.

## Final packaging correction

Aitherdev built successfully at configuration 16c19f3c (generation
2026-10-07--21-11-49). CI 37670751875 failed before package tests: the tagged
fixture's new wsjson import expanded vendoring, while Nix retained the existing
fixed-output hash. The failed logs were collected and inspected. Remove that
unnecessary package import and encode/decode the same JSON messages through the
existing websocket/encoding-json APIs. This is a narrow test correction;
production behavior, dependency versions and the declared vendor hash remain
unchanged. Tagged compilation, gofmt and diff checks passed.

Final published heads now supersede the previous selection:
- Runtime c51ba3c0ca0d41d237ef71c56accd564beb70a33.
- Workspace 8163ff2e57dcd0a33458184d6a3091e50d93efd6.
- Configuration 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3.

Each branch is still one coherent commit. Current master targets were fetched;
both downstream branches were already based on their latest targets. Confctl
hooks and final matching deployment contract passed. Fresh /root/final_builds_ci
gpt-6-luna/low owns the vendor-content check, native fixture, final composed
package/configuration builds and exact CI 37673057916. No deployment yet.

Final /root/final_builds_ci operation passed all assigned checks (exit 0,
about 12 minutes). Fresh vendor contents match the original declared hash;
native recovery passed again at c51ba3c0. Final composed package and deployment
contract, aitherdev configuration build and CI 37673057916 all passed.

## Deployment and live continuity

Host deployment passed dry activation, switch and both confctl health checks.
The host-only change preserved all four user-service process identities.
Application bootstrap completed normally (exit 0) with the approved initial
Codex restart. The subsequent compatible switch passed (exit 0, 18.5 seconds):
Codex PID 1204139 and tmux PID 435397 and their invocation IDs were preserved;
all 291 terminal pane PIDs were unchanged. Portal and router restarted. The
immutable launch marker was unchanged, and the selected package publishes
livePackageSwitchPolicy 1. The native binary remains 0.160.0.

Registration for this workspace actually requires capacity 0 with empty argv;
the installed catalog utility policy is separate from this launch capacity.
No real-host busy-turn probe was created: active-turn recovery is covered by
the isolated exact-native fixture and busy-switch behavior by host tests.
See [rollout](rollout.md) for actual system/application paths and limits.

All three default targets were fetched again without advancement. Each feature
is one clean commit. Exact base/head comparisons were saved through dev-session
before integration; no final rebase or additional production edit was needed.

## Exact master integration

All three approved masters fast-forwarded and were pushed over SSH:
- dev-workspace: c51ba3c0ca0d41d237ef71c56accd564beb70a33.
- workspace: 8163ff2e57dcd0a33458184d6a3091e50d93efd6.
- vpsfree-cz-configuration: 7e744b49ef90ba39d13b0f82a10a1f4c161c75f3.

Independent repositories used fresh detached target worktrees; those temporary
targets were removed normally after pushes. Workspace integrated from shared
master with an empty index; unrelated changes were preserved. Feature refs and
initiative worktrees remain. Fresh fetches proved all exact feature heads are
ancestors of their remote masters. Direct portal Unix-socket /healthz returned
ok. Fresh /root/master_host_ci Luna/low watcher owns master run 37676621854,
including the host VM activation/renewal/rollback lane. Feature CI 37673057916
already passed. The user then explicitly directed "no waiting for CI"; the
observer was told to stop without cancelling the GitHub run. The master run was
in progress at handoff and is not reported as passed. The deployed behavior is
verified by local/package/native checks and real service/pane continuity.

## Handoff

All authorized implementation, independent review, deployment and exact master
integration are complete. No blockers remain for using the deployed feature.
Native executable, launch policy/argv/capacity changes still take the guarded
idle restart path. Existing lifecycle, ownership and forward-recovery guards
remain intact. Real-host busy turns and full native terminal/MCP UI delivery
were not probed; the bounded fixture and dispatcher/host checks cover those
contracts to the limits recorded above. CI status is intentionally unawaited.

Feature documentation was reconciled in generic docs/workspace-portal.md and
docs/codex-package.md. Exact rollout evidence is in [rollout.md](rollout.md);
reusable fixture and configuration-shell lessons are in the two owned notes.
The portal manifest retains the three repositories and useful artifacts. No
archive, delete, session stop or feature-ref removal was performed.
