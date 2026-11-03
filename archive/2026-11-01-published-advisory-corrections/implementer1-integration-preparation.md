# Historical integration preparation handoff

The lead subsequently integrated all three exact heads and released their claims.
See [actual outcome](implementer1.md) and [postintegration proof](implementer1-postintegration.json).
Prepared targets are retained; commands below describe the preparation/handoff, not
an instruction to repeat completed integration.

User explicitly authorized merging the prepared five-repository set. The lead
owns actual claims, merge/push critical sections, their restricted observer and
remote integration proof. This packet prepares three repositories only. No claim,
merge, default push, cleanup, deployment, preview or session lifecycle command was
run by implementer1. API/KB source, Git and preparation stay with implementer0.

Session/current/env verified for2026-11-01-published-advisory-corrections and
/home/aither/workspace/ai/vpsfree.cz. Current local AGENTS, Git, commit/hooks and
monitor procedures read; relevant workspace coordination procedure/selected guide
consulted. Defaults and feature heads were checked over canonical SSH, then the
exact default refs fetched without movement. All features clean/local=remote,
all defaults ancestors of final heads. No source/input change or rebase needed.
AGENTS/Overcommit/Gemfile/lock bytes match between each target base and feature.

## Prepared detached targets

Preparation started2026-11-03T13:25:03.101196+00:00, completed2026-11-03T13:27:36.296915+00:00,153.2seconds, exit0. Parent owns
prepare.py and all worktree/Nix/hook commands; one fresh Luna/low utility only
observed independent log/status. Both are terminal. The utility summary's wording
'both targets' is imprecise; preparation.json records and parent verified all3.

### vpsadmin-webui

- Prepared target: `/tmp/2026-11-01-published-advisory-corrections-integration-implementer1/vpsadmin-webui`.
- Detached base: `63d484fc070dbee633d32624de545e834d483701`; target tree `2b6d3b14e670cbf86c5e833d414e9eb4eaae6ace`.
- Exact feature: `1c8478bceb3943645ec06ccde895ee4b0985873f` on `dev/published-advisory-corrections`.
- Default target: `refs/heads/main`.
- Common Git: `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin-webui.git`.
- Canonical origin: `git@github.com:vpsfreecz/vpsadmin-webui.git`.
- Feature checkout remains `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-published-advisory-corrections/vpsadmin-webui`, unchanged/clean.
- Target is clean/index clean/detached. No local default branch checkout changed.

Enter the target's declared environment **before** acquiring its repository
claim. This reruns ordinary shell initialization against already installed
target-local dependencies; do not do environment installation inside ownership.
The lead can launch its own critical driver from that shell. These Git commands
are supplied for the lead and have NOT been executed:

```sh
cd /tmp/2026-11-01-published-advisory-corrections-integration-implementer1/vpsadmin-webui
nix develop
# Lead acquires/verifies this repository's one claim after environment readiness.
# Fresh guards: exact feature, detached target HEAD/base, clean index/worktree,
# current SSH remote default still equals the prepared base.
git merge --ff-only 1c8478bceb3943645ec06ccde895ee4b0985873f
# Inspect actual merge/hook output even if Git's status is zero.
git push origin HEAD:refs/heads/main
git ls-remote origin refs/heads/main
# Lead proves exact final remote head and releases this claim immediately.
```

### security-advisories

- Prepared target: `/tmp/2026-11-01-published-advisory-corrections-integration-implementer1/security-advisories`.
- Detached base: `7b6c71807e3c5a41f585fd1d9563e151ada71244`; target tree `4300c751c4a65408a11b9e20871322a85b3b6926`.
- Exact feature: `0b771120bb2a878c012512b685208124c2b4263b` on `2026-11-01-published-advisory-corrections`.
- Default target: `refs/heads/2026-07-13-security-advisory-automation`.
- Common Git: `/home/aither/workspace/ai/vpsfree.cz/repos/security-advisories.git`.
- Canonical origin: `git@github.com:vpsfreecz/security-advisories.git`.
- Feature checkout remains `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-published-advisory-corrections/security-advisories`, unchanged/clean.
- Target is clean/index clean/detached. No local default branch checkout changed.

Enter the target's declared environment **before** acquiring its repository
claim. This reruns ordinary shell initialization against already installed
target-local dependencies; do not do environment installation inside ownership.
The lead can launch its own critical driver from that shell. These Git commands
are supplied for the lead and have NOT been executed:

```sh
cd /tmp/2026-11-01-published-advisory-corrections-integration-implementer1/security-advisories
nix develop
# Lead acquires/verifies this repository's one claim after environment readiness.
# Fresh guards: exact feature, detached target HEAD/base, clean index/worktree,
# current SSH remote default still equals the prepared base.
git merge --ff-only 0b771120bb2a878c012512b685208124c2b4263b
# Inspect actual merge/hook output even if Git's status is zero.
git push origin HEAD:refs/heads/2026-07-13-security-advisory-automation
git ls-remote origin refs/heads/2026-07-13-security-advisory-automation
# Lead proves exact final remote head and releases this claim immediately.
```

### vpsfree-cz-configuration

- Prepared target: `/tmp/2026-11-01-published-advisory-corrections-integration-implementer1/vpsfree-cz-configuration`.
- Detached base: `0d71dd289feeb1ea2686f9c7cf0f93728baf9bd2`; target tree `aaca9dee228ab122267e8b52ffd05f729db3de80`.
- Exact feature: `c4107822060e9e34b24a83950d618c9f28a7722b` on `2026-11-01-published-advisory-corrections`.
- Default target: `refs/heads/master`.
- Common Git: `/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git`.
- Canonical origin: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
- Feature checkout remains `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-published-advisory-corrections/vpsfree-cz-configuration`, unchanged/clean.
- Target is clean/index clean/detached. No local default branch checkout changed.

Enter the target's declared environment **before** acquiring its repository
claim. This reruns ordinary shell initialization against already installed
target-local dependencies; do not do environment installation inside ownership.
The lead can launch its own critical driver from that shell. These Git commands
are supplied for the lead and have NOT been executed:

```sh
cd /tmp/2026-11-01-published-advisory-corrections-integration-implementer1/vpsfree-cz-configuration
nix develop
# Lead acquires/verifies this repository's one claim after environment readiness.
# Fresh guards: exact feature, detached target HEAD/base, clean index/worktree,
# current SSH remote default still equals the prepared base.
git merge --ff-only c4107822060e9e34b24a83950d618c9f28a7722b
# Inspect actual merge/hook output even if Git's status is zero.
git push origin HEAD:refs/heads/master
git ls-remote origin refs/heads/master
# Lead proves exact final remote head and releases this claim immediately.
```

## Environment and hook expectations

- Modern: pinned Node24.21.0/npm11.19.0 and normal Nix Git available. No declared
  Git-hook framework, no install/sign bypass; no npm install, test or build needed
  for this Git-only preparation. PR122 is already ready at exact1c847. Workspace
  Git requires local FF plus direct SSH main push despite the PR. Check normal
  PR merge auto-close only AFTER the lead integrates; do not use GitHub Merge.
- Client: target's declared Nix shell installed its locked Ruby bundle, Ruby3.4.9.
  `bundle check`, `bundle exec overcommit --install` and `--sign` all passed.
  `.overcommit.yml` enables PreCommit RuboCop; builtin configuration signature
  updated normally. No custom plugin files or extra trust framework introduced.
  Target default is the automation branch, not master (bare master was unborn).
- Config: declared pinned confctl tools shell, Ruby3.4.9, target-local locked gems.
  Same normal bundle/Overcommit installation/signature passed. PreCommit Nixfmt
  and RuboCop remain enabled. Generated feature message/history retained; no
  new commit is created by the FF. No confctl pin update/deploy during integration.
- Valid configured author/committer in all target environments remains
  Jakub Skokan <jakub.skokan@havefun.cz>. No identity change was made.
- Native target Git executables observed for client/config:
  /nix/store/k3wl6cg7q50zkx47af3msmg1yrg1f203-git-2.54.0/bin/git and
  /nix/store/b1wn5clix1mz4vpfih7x9cnj9qfh7c6h-git-2.54.0/bin/git, respectively.
  Invoke through each prepared target's ordinary Nix shell so bundle variables
  and PATH remain correct. Do not copy a feature's GEM_HOME to the target.

The actual FF/post-merge hooks still run in the lead's critical section. Git can
exit zero after a post-merge hook failure: inspect output before pushing. On
baseline movement or a hook intervention, stop/reconcile effects, release the
known-safe claim and repair outside ownership. Do not hold a repository while
waiting for CI, review, operator input or bookkeeping. Acquire one repository
at a time; no machine claim needed. Never force push a default.

## Evidence and boundaries

Private raw preparation.json/log/exit/observer evidence and exact command argv:
/tmp/2026-11-01-published-advisory-corrections-integration-implementer1/.
Sanitized source/target mappings are in this receipt. Feature refs, portal
comparisons, full reviews/no-migration conclusions and exact prior validation
remain unchanged; no new code or verification campaign. No claims held here.
No default integration result or PR auto-close is claimed before the lead runs it.
All own commands terminal. Implementer0 took the newly free utility slot for its
API/KB environment preparation after this batch; no overlapping utility.
State/handoff/portal remain lead-owned and untouched.

Stable portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-01-published-advisory-corrections/
