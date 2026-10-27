# Aitherdev configuration preparation

Prepared and published; no build, copy, claim or activation was performed.

- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- Branch: `2026-10-24-workspace-session-ui`
- Base: `d12a77374b18e15fe7600f95307114e2e1882828`
- Head: `eac2877469a3b626f4c0d81f301f9320dae564cb`
- Tree: `34a8813548ad7d870c2892c14bc8e45625232b2c`
- Matching workspace composition: `e1c216981117c6049818a57157f0c4b6d8ad65f0`

The complete branch has one generated input commit. Its complete diff is
`whole.diff.patch`: only `flake.lock`, 3 additions and 3 removals. Channel
`dev-workspace`, role `devWorkspace`, selects the root `devWorkspace` input.
Only its locked revision, NAR hash and timestamp changed, from `10bb0475` to
reviewed/tested `9293e314e6028d71a57595073117b51bdc53c8ff`. Every other lock node,
original input and follows relationship is identical. No application, system
package, provider or native selection was changed. The extension is owned by the
matching workspace composition and remains `767dfd58`; llm-agents remains
`e85b99217baf13a38fc887b31338b1833f1159c0`.

No migrations were added or rewritten, and none from this branch has been merged,
released, deployed or externally consumed. There is one pin stream, no repeated
updates, intermediate selections, obsolete approaches or fixup commits. Standalone
mechanical-content review disposition belongs to the lead; this inventory does
not substitute for that decision or grant integration approval.

`channel-set.log` preserves successful Nixfmt and commit-message hook output and
the unmodified generated changelog. Its TextWidth advisory is expected for the
generated full-SHA log range. No hook was bypassed. The initial post-checkout
failure was a missing ambient Gem bundle; the repository Nix shell installed its
pinned gems, then Overcommit installation/signing and the commit succeeded.
Sequential ordinary `dev-session` retries registered the worktree after session
lock contention, without bypassing the lock.

Quick checks passed: exactly three intended semantic lock values; all effective
metadata siblings unchanged; actual pristine-base/final build-plan input paths
unchanged except devWorkspace; final metadata lock graph equals `flake.lock`;
full diff whitespace; runner Bash syntax and embedded Python syntax. The workspace
owner independently reported the cross-repository deployment checker PASS against
these exact committed locks. No routine pin documentation change is needed in the
configuration repository; existing operational guidance remains applicable.

## Home Manager discrepancy

Pinned confctl `mk-confctl-outputs.nix:248` constructs input paths from the actual
root-resolved `inputs.<name>.outPath`. Its `mkRoleInfo` instead indexes
`lock.nodes.<inputName>` without following `lock.nodes.root.inputs`.
`confctl-home-manager-lookup-source.txt` preserves the relevant source.

Thus the role's metadata reports transitive node `home-manager` / `c47b2cc6`,
while the actual root input maps to `home-manager_2` / `e28654b7`. The pristine
`d12a7737` build plan and final committed build plan both select
`/nix/store/qh7n70gsg3rmvyn5zi1x1vhnwbrnm5wx-source`; its NAR hash is
`sha256-wnV9ttf4fPWNonBIQmvlrSlNpQYgx5HgWWd007mwIFA=`, matching `e28654b7`.
Their other input paths are also identical. The deployed clean configuration
receipt identifies `d12a7737`, and its input metadata repeats the same lookup.
That metadata alone cannot prove a different live Home Manager selection.
No speculative pin repair was made. Preserve the actual source graph when
building and compare the resulting system plan before activation.

## Watcher preparation command

After the lead's mechanical-pin/review gate, a fresh verification watcher may run:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/configuration-preparation/prepare-aitherdev.sh
```

The runner asserts exact clean configuration head and session identity, enters its
pinned Nix shell, builds only `cz.vpsfree/machines/aitherdev`, captures its actual
generation JSON/name, system output/deriver, complete recursive derivation graph,
runtime closure and flake source/input graph, then performs copy-only for that
exact generation. It has no dry-activate, switch, reboot, claim or lifecycle action.
The watcher must stop/report an unexpected local kernel build and must not diagnose,
retry or change source. Preserve configured health checks and auto-rollback.

## Parent activation commands

Only after successful preparation, acceptance inspection and an authoritative
held claim for physical machine `vpsfree:aitherdev`, the lead can enter the exact
configuration worktree and its Nix shell, read the captured generation, and run:

```sh
UI_CONFIG_GENERATION=$(cat /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/configuration-preparation/generation-name.txt)
confctl deploy --generation "$UI_CONFIG_GENERATION" cz.vpsfree/machines/aitherdev dry-activate
# Inspect the complete result before the separate ordinary switch:
confctl deploy --generation "$UI_CONFIG_GENERATION" cz.vpsfree/machines/aitherdev switch
```

The source range changes portal content, not host modules or native inputs. Expect
configuration/input metadata changes; require the actual dry activation to confirm
service effects. Unexpected native-daemon, system-Codex, provider or guest changes
return to the lead before switching. Do not disable auto-rollback, bypass health
checks or reboot. Bind both live system and system profile to the captured output
and inspect configuration/input metadata before the dependent workspace profile
switch in the architect's brief. A partial or uncertain switch retains its
original recovery obligation and machine hold.

The lead owns profile preparation/activation and deployed-effect checks, machine
retention, final CI and any later integration request. Default integration is not
approved. The configuration preparation Git/edit window is released after the
final clean-state report.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>
