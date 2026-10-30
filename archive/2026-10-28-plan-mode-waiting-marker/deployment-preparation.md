# Deployment preparation

Implementer1, 2026-10-29. Pins and read-only evaluation only. No package build,
closure copy, claim, activation, default-branch integration or lifecycle action
was performed. Lead owns rollout and approval coordination. Both feature
worktrees are clean and SSH-published; final independent pin/history review passed with no findings. Source review passed; broader checks remain with lead/implementer0.

## Identity and review inventory

`dev-session current` and both environment values matched
`2026-10-28-plan-mode-waiting-marker` /
`/home/aither/workspace/ai/vpsfree.cz`. Read the full required workspace
procedures, configuration AGENTS, configuration provider operations guide,
selected package claim guide and architect's deployment addendum before edits.

All four feature branches use `2026-10-28-plan-mode-waiting-marker` and target
`master`. This package changed only the following two repositories:

| Repository / canonical SSH origin | Base | Final feature head | Complete series |
| --- | --- | --- | --- |
| workspace / `git@github.com:aither64/vpsfree-cz-workspace.git` | shared master `1085b570dc27d7250faa94ae893f9f8ffd04c45c`; remote master `5fc7000f8a5fd1aa1f60c9731cbbb4b8c59a2e13` | `398dc7bab89ee51bcc77d23a5acc52c7e02878c1` | remote base includes initial tracking commit `1085b570d`, then one runtime-pin commit `398dc7bab` |
| vpsfree-cz-configuration / `git@github.com:vpsfreecz/vpsfree-cz-configuration.git` | `584691d9b96ce1555a5787a0a1d999eeb528811f` | `b3b933bf6f9fc9f7f533b3f4e06775defd8879da` | one generated channel update |

Worktrees are under
`worktrees/2026-10-28-plan-mode-waiting-marker/{workspace,vpsfree-cz-configuration}`.
They are registered in portal.yml with honest initial bases. Workspace preserves
sparse omission of work/ and archive/. Shared master was not edited for pins.
Fresh origin fetches and rebases were no-ops. `git ls-remote` proved both exact
published heads and unchanged remote defaults shown above. Comparisons captured
with `dev-session worktree capture-comparison` use the complete remote-base ranges.

No migrations, obsolete approaches, intermediate pin updates or required retained
state boundaries exist in these two ranges. No feature deployment or release
occurred. Publication exposes these exact feature refs for review; retain them.
The source dependency heads are dev-workspace
`5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3` and codex-web
`9d337b70987fdf1dd42a5d8efff31f755a122550`, owned by implementer0.

## Pin changes and quick checks

Inspected `flake.nix` channel mapping and `nix develop -c confctl inputs channel
ls` before mutation. The existing `dev-workspace` channel's `devWorkspace` role
maps to flake input `devWorkspace`. Ran the exact generated update in that shell:

```sh
confctl inputs channel set --commit dev-workspace devWorkspace 5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3
```

Preserved its generated changelog and commit text. Diff: flake.lock only,
7 insertions/deletions. Workspace changed only the direct nested URL in
`inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`, then ran
`nix flake update vpsfree-dev-workspace/dev-workspace`; diff: flake.nix and
flake.lock only, 9 insertions/deletions. No top-level runtime input was added.

Semantic comparison against both exact initial-base locks passed: identical
node keys, root/version and every input edge/follows array. Only `dev-workspace`
and `codex-web` workspace nodes, and `devWorkspace` and `codex-web` configuration
nodes changed. Extension revision/hash, llm-agents, native Codex and all other
locked identities are unchanged. Extension remains
`767dfd587e346168e1443e65ccdb67ce748f3fe3`.

`git diff --check` passed both repositories. Workspace `nixfmt --check flake.nix`
passed using configuration's pinned Nix shell. No hook framework is declared by
workspace. Configuration Overcommit hooks were installed/active before commit;
Nixfmt and commit-msg hooks passed. The expected generated-history line-width
warning was retained without rewriting the generated message.

Configuration worktree creation initially hit a post-checkout hook failure:
ambient Bundler lacked locked gems. Git had already created the exact branch and
checkout, and registration was intact. Entering the documented `nix develop`
installed the worktree's locked gems; `bundle exec overcommit --install` restored
ordinary hook execution. No hook was bypassed, and no shared branch was changed.

The final composed checker passed:

```sh
bin/check-dev-workspace-deployment \
  --workspace-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-plan-mode-waiting-marker/workspace \
  --configuration-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-28-plan-mode-waiting-marker/vpsfree-cz-configuration
```

Result: `deployment contract passed for
vpsfree-cz.workspace.aitherdev.int.vpsfree.cz at
5f4f1c1c52cc009970a2697f5dbc330c0a4dd7a3`.

## Exact sources and complete graph pointers

The complete committed locks preserve every node's locked identity/hash and all
edges/follows, rather than relying on a list of direct dependencies:

- [Workspace graph at exact head](https://github.com/aither64/vpsfree-cz-workspace/blob/398dc7bab89ee51bcc77d23a5acc52c7e02878c1/flake.lock):
  35 nodes, Git blob `99bfd2c5ddd4e27bf57109abab41eec15948f197`.
- [Configuration graph at exact head](https://github.com/vpsfreecz/vpsfree-cz-configuration/blob/b3b933bf6f9fc9f7f533b3f4e06775defd8879da/flake.lock):
  64 nodes, Git blob `6217bad973721936fc4282056f2dedf6a192386e`.

Raw supporting metadata is in logs/workspace-inputs-exact.json,
logs/workspace-inputs-final.json, logs/configuration-inputs-final.json,
logs/workspace-sources.json and logs/configuration-sources.json. Those are
disposable supporting artifacts; the committed locks above retain the graphs.

| Source | Exact store path |
| --- | --- |
| Workspace exact committed Git source | `/nix/store/a0bgavh20yanjjsxxj416fami6xikq4q-source` |
| Sparse-worktree Git metadata source | `/nix/store/3ccam87ljbh4m00yjpz5d0zfm1r8l5x7-source` |
| Workspace path evaluation source | `/nix/store/81m0vmba1kmd9ignm173glsaw72li1dy-source` |
| Configuration committed Git source | `/nix/store/f6kc3n8jkb1wqdplijgw3icx3gxk130l-source` |
| Configuration path evaluation source | `/nix/store/gziggjr6h6sx81m4xg2m00g67117zzvp-source` |
| Runtime | `/nix/store/wdh3nqarvakn0aqs3q4zw479v3lgjr2s-source` |
| codex-web | `/nix/store/4zsm43x32dilp195ai3yg9vcbsk1adbc-source` |
| vpsFree extension | `/nix/store/lfmiclfqmpw7bs99lil6x5f83ba1j070-source` |

Nix reports the sparse workspace as dirty although Git status and logical
`git diff-index HEAD` are clean. Explicit committed `git+file` revision evaluation
and sparse-worktree evaluation produce the same application drv/output below.
No source/index change was made to silence the warning. The exact committed
source path is the shortest way to avoid ambiguity during the later build.

## Read-only system/application comparison

Application drv:
`/nix/store/wxxdwf6ibjnhrfdvv3dx7gf2flhqp3x9-dev-workspace-0.2.0.drv`.
Application output:
`/nix/store/g650vgjpzvyifjmb1j44pc5bby3522z4-dev-workspace-0.2.0`.
Its source is the runtime path above. Selected application observed with
`workspace-host status`:
`/nix/store/d0wikyzpr7qk1w2c2zbqgj97qz1m58qn-dev-workspace-0.2.0`, deriver
`/nix/store/13wf9a0jd1lhrwf6vdf9dvllwyhpapk5-dev-workspace-0.2.0.drv`.

Authoritative ordinary confctl candidate system drv:
`/nix/store/ia5gh8wr85mp6crbgi16nwf7wn66zz80-nixos-system-aitherdev-26.05.20261026.718f670.drv`.
Candidate system output:
`/nix/store/r4rd3qyn52z1bipbln8kdh43mjd2wb1k-nixos-system-aitherdev-26.05.20261026.718f670`.
Auto-rollback drv/output:
`/nix/store/za41c9rsf8k0qv0ay8svf4kc4y2x0q51-auto-rollback.rb.drv` /
`/nix/store/yl9vnin9wlv04cip0sqpkisk80xmccwh-auto-rollback.rb`.
Confctl key: `m_cz_vpsfree_machines_aitherdev_0b1e0938`.

Both `/run/current-system` and `/nix/var/nix/profiles/system` were rechecked and
resolved to
`/nix/store/fczhh0f76j8sy2awv7skrv2rp59vr7lg-nixos-system-aitherdev-26.05.20261026.718f670`.
Its deriver is
`/nix/store/h6vpqnqlrplzavr56k5h00bm5sv9g635-nixos-system-aitherdev-26.05.20261026.718f670.drv`.
Exact base configuration `584691d9` evaluates to that same drv/output, from
`/nix/store/vk3s4902ihgxr50vrxwknf3mq5akiavl-source`. Therefore this pin changes
the actual system output on the observed baseline and system activation is
required before selecting the application. Recheck both links before action.

Ordinary `.#confctl.build.m_cz_vpsfree_machines_aitherdev_0b1e0938.toplevel`
evaluation and an explicit Git input at `b3b933bf` independently agree on this
ia5/r4r identity. The first `builtins.getFlake (toString ./.)` path evaluation
instead returned provisional drv
`/nix/store/jzr4idz432cmmx95xixbqb1ppxl1yx1v-nixos-system-aitherdev-26.05.20261026.718f670.drv`
and output
`/nix/store/287h21qgjmfcnmbbclw20n2shw5y3mia-nixos-system-aitherdev-26.05.20261026.718f670`.
That path source lacks Git revision metadata. Pinned confctl creates
`/etc/confctl/configuration-info.json` only for an input carrying its valid Git
revision. The exact-vs-path etc drv diff proves that the omitted file is the
only difference at that level. Use ordinary confctl from the clean committed
worktree, not the provisional path input. Raw evidence:
logs/system-confctl-identities.json, logs/system-exact-identities.json,
logs/system-source-comparison.json and logs/etc-source-comparison.json.

Bounded immediate-derivation comparison found only etc and activate drv inputs
changed at the system's top level (including in the provisional path comparison). The system build command changes its etc
symlink and activate-script path; kernel, initrd and system-path references are
unchanged. This establishes inequality without building, not a completed
closure-difference or activation verification. Supporting evidence:
logs/system-identities.json, logs/system-base-identities.json,
logs/system-derivations.json and logs/system-derivation-diff.txt preserve the
provisional path comparison; authoritative identity is the ordinary confctl
evaluation above. No full closure comparison was run.

## Proposed post-review watcher batch and lead rollout

These are prepared commands, not execution evidence. Source-suite watcher is
still owned by lead; do not duplicate its suites or exceed utility max_concurrent1.
After review and that batch finish, use one fresh watcher for build preparation:

```sh
# Exact committed application; no source overrides.
nix build /nix/store/a0bgavh20yanjjsxxj416fami6xikq4q-source#default \
  --no-link --print-out-paths

# In the clean configuration feature worktree at b3b933bf.
nix develop -c confctl build cz.vpsfree/machines/aitherdev
nix develop -c confctl generation ls cz.vpsfree/machines/aitherdev
```

Retain confctl generation name, input/source metadata, toplevel and auto_rollback.
Stop unexpected local kernel compilation. After build, compare actual closure:

```sh
nix store diff-closures \
  /nix/store/fczhh0f76j8sy2awv7skrv2rp59vr7lg-nixos-system-aitherdev-26.05.20261026.718f670 \
  /nix/store/r4rd3qyn52z1bipbln8kdh43mjd2wb1k-nixos-system-aitherdev-26.05.20261026.718f670
nix develop -c confctl deploy --generation GENERATION --copy-only cz.vpsfree/machines/aitherdev
```

Build/copy preparation precedes machine ownership. Catalog machine ID is
`vpsfree:aitherdev`; aliases `aitherdev`, `aitherdev.int.vpsfree.cz` and
`cz.vpsfree/machines/aitherdev`; confctl target `172.16.106.40`.
Lead owns later claim, explicit-generation dry-activate/switch, both system-link
checks, then ordinary `workspace-host switch --source` with exact session and
claim environment. Preserve confctl auto-rollback and forward-only application
recovery. No portal application installation in system configuration.

Lead retains [rollout.md](rollout.md), approval, continuity/health and live title
marker verification, complete integrated-lineage proof and machine release.
Separate integration approval remains required. No lifecycle action is implied.
Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-28-plan-mode-waiting-marker/
