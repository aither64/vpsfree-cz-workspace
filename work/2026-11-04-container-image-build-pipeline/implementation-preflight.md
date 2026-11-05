# P0: implementation preflight

Observed 2026-11-05, approximately 19:28–19:34 UTC, by `implementer1`.
P0 complete for acceptance; **production activation and privileged runner execution
remain blocked on the unverified facts below**. Fixture core/HTTP/pipeline work
can proceed. No source edits, tests, builds, CI, deployments, credential changes,
claims, branches, commits or session lifecycle actions were performed.

## Identity, source and boundaries

- `dev-session current` returned `2026-11-04-container-image-build-pipeline`;
  both environment identity values matched the bound slug and workspace.
- Saved roster: implementer1, `gpt-6.1-sol` / xhigh / workspace_write. Current
  peers architect0, implementer0, implementer2 and implementer3 verified.
- Authoritative [design](design.md) and [plan](plan.md) read. Workspace AGENTS,
  applicable session/documentation/project/Git/verification/team guidance reused;
  deployment, coordination and commit/hook procedures read for this phase.
- Installed `workspace-host coordination guide` read: selected package
  `/nix/store/zmyllqw6x1cxk8vhwliy7r11ykd19cz9-dev-workspace-0.2.0`.
  No ownership claim is needed or taken for these read-only metadata checks.
- Org own worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-04-container-image-build-pipeline/vpsadminos-org-configuration`
  was clean on feature branch `2026-11-04-container-image-build-pipeline`,
  exact base/head **C=`ca96c95a1fee04793468785d8323a759615b2b4e`**.
  C has no tracked AGENTS/README/docs; commands inferred from flake/manifests.
- Other fixed evidence sources: vpsadminos
  **V=`2951a632c4254a44747a8da326e3dde897eaa0e2`**, builder configuration
  **B=`f4069909b55fbed907cb658f350ec6a59f97e05a`**. No fresh remote ref claim.
- Only this assigned evidence file is written; prior peer/session work preserved.

## Observed local development capacity, not runner capacity

Local `hostname -f`: `aitherdev.int.vpsfree.cz`. `nproc`: **64**.
`free -m`: **96,537 MiB** total, **76,367 MiB** available at observation, no swap.
`df -h` for workspace and `/tmp`: common root `/dev/vda1`, **984G** total,
**789G** used, **145G** available, **85%** used. These are transient local values;
no I/O benchmark, recursive size scan or allocation was performed.

`/dev/kvm`: mode **0666**, root:kvm, current user read/write access true. This
is a permission observation, not a successful nested-VM launch. Ambient PATH has
Nix/Go/Bundler; gcc, sqlite3, virtiofsd and qemu-system-x86_64 are absent. They
must come from declared Nix dependencies, not assumed ambient tools. Root cgroup
v2 `memory.max`/`cpu.max` paths were absent; no capacity claim follows from that.
This workstation is not established as a configured GitHub runner or image VPS.

## Configured runners and trust prerequisites

C `configs/gh-runner.nix:71` registers one persistent runner service per host at
`https://github.com/vpsfreecz`, group **vpsAdminOS runners**, user/group
`github-runner`. Credential file path is referenced at `:73`; no contents read.
`:87` disables private devices/users and namespace/syscall restrictions needed
for KVM/virtiofsd. `:110` assigns a 65,536-ID subordinate UID range.
`:40–64` configures Nix GC coordination every ten minutes with a random delay;
this is not image-run scratch/quota management or proof of actual free space.

| Configured machine selector | SSH alias | Primary address |
| --- | --- | --- |
| `org.vpsadminos/int.gh-runner1` | `gh-runner1.int.vpsadminos.org` | `172.16.4.21` |
| `org.vpsadminos/int.gh-runner2` | `gh-runner2.int.vpsadminos.org` | `172.16.4.22` |
| `org.vpsadminos/int.gh-runner3` | `gh-runner3.int.vpsadminos.org` | `172.16.4.25` |
| `org.vpsadminos/int.gh-runner4` | `gh-runner4.int.vpsadminos.org` | `172.16.4.31` |

Source: each C `cluster/org.vpsadminos/int.gh-runnerN/{module,config}.nix`.
V `.github/workflows/image-scripts.yml:7–28` includes dispatch/push/PR triggers;
`:33` and `:103` choose generic `self-hosted`. Those source declarations do not
prove external repository/workflow/ref admission, fork protections, runner-group
restrictions or secret availability. Before privileged execution, verify trusted
revision admission and publisher-secret separation outside worker/build jobs.
Do not execute editable/untrusted workflow code on these persistent runners.
Actual runner CPU/RAM/free disk/KVM accessibility/virtiofsd packages remain unknown.

## Bounded live metadata attempts and exact failures

All attempted SSH commands used `-T`, `BatchMode=yes`, `ConnectTimeout=5`,
`ConnectionAttempts=1`, `StrictHostKeyChecking=yes`, `UpdateHostKeys=no` and root
login. Commands only requested hostname/current-system/version, targeted disk
metadata/catalog summary and specific systemd/runner facts. **All five attempts
exited 255 before remote commands ran: zero remote commands executed.**

| Exact target | Result |
| --- | --- |
| `images.int.vpsadminos.org` | No ED25519 host key known for this alias; strict host-key verification failed |
| `gh-runner1.int.vpsadminos.org` | Permission denied (publickey,password,keyboard-interactive) |
| `proxy.vpsadminos.org` | No ED25519 host key known for this alias; strict host-key verification failed |
| `gh-runner2.int.vpsadminos.org` | Permission denied (publickey,password,keyboard-interactive) |
| `172.16.106.5` | No ED25519 host key known for this exact target; strict host-key verification failed |

No trust bypass, key acceptance, credential search, host scan, remote writer or
service change followed. Runner3/4 were not probed after these access failures.
A legitimate trusted access path is required only for dependent runtime preflight;
no user question or implementation stall is needed now.

## Images/proxy/adoption prerequisites

C `cluster/org.vpsadminos/int.images/module.nix:3` names selector
`org.vpsadminos/int.images`, alias `images.int.vpsadminos.org`, address
`172.16.4.15`, NixOS container profile. Current filesystem/free/used space,
file/catalog counts, actual formats/aliases/hashes, path ownership/modes,
SQLite/file durability properties and active system revision **were not observed**.
No numerical production upload/run/storage budget can be justified yet.

C images `config.nix:21–43` allows proxy HTTP and serves `/srv/images` through
nginx/fancyindex. C proxy `config.nix:79–104` terminates HTTPS and proxies this
host; `proxy/module.nix:16` declares IPv4 `37.205.14.58` and `:22` IPv6
`2a03:3b40:fe:48::1`. Effective socket peer, generated headers, HTTP reachability
and bypass routes remain unverified; explicit trusted forwarding belongs in P2.
No HTTP requests or server/mount launches were made during P0.

C `environments/base.nix:48` authorizes root admin+builder keys, with no dedicated
producer/publisher restricted roles shown. Do not repurpose those unrestricted
keys as a verified role boundary. P2 prepares role-specific forced commands,
no forwarding/PTY, separate service sockets and explicit deployment-supplied keys;
actual credential provisioning/admission stays an activation prerequisite.

B `cluster/cz.vpsfree/machines/build/config.nix:106–135` configures the legacy
weekly VM builder and post-run `rsync -av --delete` to images `/srv/images`.
Its exact selector is `cz.vpsfree/machines/build`, host alias `build.vpsfree.cz`,
configured target `172.16.106.5`. The active timer/job/rsync status and any manual
native writers are unknown. Before adoption, exclude every mutator, capture one
coherent catalog/files/hash/alias inventory, and verify portable recovery export.
A static C/B source revision does not prove its active deployment revision.

## Limits and next package release

Production worker count, CPU/RAM/scratch allocation, max upload bytes, incoming/run
quotas, reserved public headroom, leases/TTL and private access-log retention
remain **unset and activation-blocking**. Implement explicit configurable finite
limits and fail closed when required production values are missing; fixture tests
can provide their own small bounds. Do not promote workstation capacity or legacy
24GiB/16CPU/60G builder sizing into a runner allocation or a measured speedup.

Before shadow work, measure chosen runners and image storage through a trusted
access path; before activation, reconcile writer exclusion and exact import/export
proof. These findings block those operations, not P1/P2/P3 disposable fixtures.

Org `Gemfile:3` declares Overcommit and `.overcommit.yml:3` enables Nixfmt. Canonical
pre-commit/commit-msg hooks exist and are executable; ambient Overcommit is absent
and the lead reported setup trouble. P0 makes no hook changes. Resolve the actual
Nix/Bundler hook environment before later commits; never bypass required hooks.

P1's stable reader contract is owned by implementer2 in
[types.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-04-container-image-build-pipeline/vpsadminos/osctl-repo-server/types.go).
P2 should consume that definition, keep disjoint HTTP/dashboard/log files, and
return main/type wiring requests to P1. No duplicate copied interface is introduced
here. P2 starts only after lead accepts P0 and releases it; capacity is available
for that package after acceptance. No migration/history/source-head change in P0.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-04-container-image-build-pipeline/)
