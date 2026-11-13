# Package I implementation evidence

Ready for lead acceptance and independent final review at 2026-11-13 21:15 UTC.
Implementer0 owns the complete configuration package; lead owns plan/state,
review invocation, post-review build and approved integration. User clarified
configuration-only scope: no node access, live checks or deployment are required.

## Exact deliverable and publication

- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-oomd-restart-thresholds/vpsfree-cz-configuration`.
- Branch: `2026-11-13-oomd-restart-thresholds`, registered with `dev-session worktree add`.
- Base: `1a948a872f84bdb4643926b357cf15534de1d313` (fresh `origin/master`).
- Head: `08d68a85f24a95b70b2d806f995f04b236e4d89a`.
- Complete series: one commit, `cluster: lower oomd restart thresholds on node25.prg`.
- Complete diffstat: `cluster/cz.vpsfree/nodes/prg/node25/config.nix | 5 +++++`.
- Diff adds ordinary module settings `restart_hits = 4` and
  `load_multiplier = 1.5`; inherited `verbose = true` and all other guards,
  defaults and inputs remain unchanged. No `mkForce`, daemon or shared edit.
- Pre-push fetch and post-push `git ls-remote` both identified master at the
  exact base above; `git merge-base --is-ancestor origin/master HEAD` passed.
  Remote feature ref equals the exact head. Worktree/index are clean.
- [Publication log](push.log). No pull request required or created. GitHub
  Actions lists no runs for this head/branch; the sole repository workflow is
  scheduled/manual input maintenance, with no push trigger.

## Quick checks and hooks

All run against the delivered source in its pinned `nix develop` environment:

- `nix-instantiate --parse cluster/cz.vpsfree/nodes/prg/node25/config.nix`: passed.
- `nixfmt --check cluster/cz.vpsfree/nodes/prg/node25/config.nix`: passed.
- `git diff --check`: passed; final full base-to-head diff check also passed.
- Existing executable Overcommit hooks verified active; version 0.76.0.
  Actual commit ran Nixfmt and commit-message hooks successfully. TextWidth
  gave one nonfatal body-line warning above its 72-column preference; all lines
  satisfy the documented 80-column limit. [Commit log](commit.log).
- `git diff --exit-code BASE HEAD -- flake.nix flake.lock`: passed.
- [Quick-check log](quick-checks.log), [shell-preparation log](shell-prep.log).

Worktree creation initially exited 78 because its ambient post-checkout hook
could not find locked gems. Inspection confirmed the correctly created branch,
clean checkout and completed manifest registration. The documented
`nix develop -c true` preparation installed the normal local bundle and passed
under a fresh Luna/low native watcher in 49 seconds. Subsequent hooks ran in
that pinned shell; no hook was disabled or bypassed. No command remains running.

## Inputs, history and documentation provenance

The initial design inspected configuration `d0674cc68ed2cb1c71606caa50fe31227ea3521a`.
Fresh master included only subsequent lock changes to vpsadminosProduction and
vpsadminProduction. Architect0 rechecked the relevant new daemon/module contracts
and updated [design.md](design.md); no configuration pin is changed by I.

[input-metadata.json](input-metadata.json) records the final exact source and
complete 64-node locked input graph. Final source is
`/nix/store/ir33sf6icaly26xsphp65apfrx2f6s85-source`, NAR hash
`sha256-lx9kCXFEu7gkP/Dn1kJ5nnKjU20ykZvc+pk4lJWTMzk=`.
`flake.lock` SHA-256 is `d6a45cb62482eb2f321d551595325da1b44b1095284abe2acf6f4af57f487877`.
[node25-inputs.json](node25-inputs.json) records confctl's actual production-role
mapping and store paths:

| Input | Revision | Source path |
| --- | --- | --- |
| confctl | `ff5e017780a35fb97b549db2a51b570193867c3b` | Pinned in the complete graph |
| nixpkgsProduction | `ac588ef1c914865dad517b337ea0eb9694a4021c` | `/nix/store/7sa2x9c9566lfxkaxs36n3z4yayl5cy4-source` |
| vpsadminosProduction | `c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62` | `/nix/store/yb3qniksa7pklfiy7fzqb3avxxldhh3d-source` |
| vpsadminProduction | `2d0946c4e699aa61092228d8a7cb275477ee46d0` | `/nix/store/m5x5i02kjrrvpn2pp5xmzykwxwcwz7k9-source` |

There are no migrations, generated clients, protocol/state-format changes,
dependency-update streams or transitional compatibility paths. The sole commit
is the complete intended patch; only its message was amended before publication.
Nothing was merged, released or deployed by implementer0. No obsolete commits
remain in the branch range and no history consolidation is needed.

Existing settings need no new repository reference/runbook documentation. Readers
are the node operator and future maintainers; the accepted design holds the
site-specific rationale, compatibility and future operator recovery context.
This evidence belongs in session tracking, per configuration repository policy.

## Lead-owned post-review validation

Lead accepted architect's sequencing clarification: pinned confctl does not
export its evaluated module configuration. Do not reconstruct private evaluator
arguments. Quick checks above precede independent review; exact merged JSON is
checked through the actual required build afterward. No full-node build has run.

- CWD: the exact worktree above, at the exact final head.
- Build argv: `["nix", "develop", "-c", "confctl", "build", "cz.vpsfree/nodes/prg/node25"]`.
- Use a fresh monitored operation; retain exact command, exit, input and output
  receipts. Stop and diagnose unexpected local kernel compilation.
- Evaluated metadata confirms node25 `buildAttribute` is
  `["system", "build", "toplevel"]`; confctl key is
  `m_cz_vpsfree_nodes_prg_node25_5e1cc944`.
- After successful build, identify its exact system store path from the build
  receipt (or `nix eval --impure --raw '.#confctl.build.m_cz_vpsfree_nodes_prg_node25_5e1cc944.toplevel.outPath'`
  at this same unchanged head). Read
  `<system>/etc/runit/services/osctl-oomd/run` and the store JSON named by its
  `--config` argument. Require precisely
  `{"load_multiplier":1.5,"restart_hits":4,"verbose":true}`. Preserve both
  exact paths, contents and the assertion result in the build/review evidence.
  This reads generated artifacts without executing the service.

No machine/repository claim or lifecycle action was taken. Session remains open.
Lead owns the user's later integration approval and its recording.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-oomd-restart-thresholds/

## Package P: integration preparation

Ready for lead acceptance after I was accepted. Capacity reconfirmed; package P
prepared only a disposable detached checkout and its normal hook environment.

- Target: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-oomd-restart-thresholds/vpsfree-cz-configuration-merge`.
- Freshly fetched base and detached target HEAD:
  `1a948a872f84bdb4643926b357cf15534de1d313`. Working tree/index are clean.
- Feature remains clean at `08d68a85f24a95b70b2d806f995f04b236e4d89a`.
- Saved shell profile:
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-13-oomd-restart-thresholds/merge-dev-shell`,
  resolving to `/nix/store/6krdzayrv18d8y4m2rh65jjxdvnpbcf0-nix-shell-env`.
- Launch from the original feature worktree. Its proven `.gems` and `.bundle`
  supply hooks for `git -C <target>`; target and feature Gemfile, Gemfile.lock,
  flake.nix, flake.lock and .overcommit.yml are identical. No bundle copying or
  symlinks inside the target are needed. `bundle check` passed.
- Common executable pre-commit/post-merge/pre-push hooks are active, with no
  core.hooksPath override. Overcommit 0.76.0 post-checkout completed successfully
  during creation. Standard `bundle exec overcommit --sign` completed from the
  target using the proven shell/bundle; no hooks were replaced or bypassed.
- [Creation log](merge-target-prep.log), [environment/trust log](merge-environment.log).

Prepared command argv for the lead, **not executed** here. CWD for both is the
original feature worktree; enter this prepared environment before the lead's
short claim section where practical. The lead must still perform its fresh
target/feature/review checks and claim workflow.

```sh
nix develop /home/aither/workspace/ai/vpsfree.cz/work/2026-11-13-oomd-restart-thresholds/merge-dev-shell -c git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-oomd-restart-thresholds/vpsfree-cz-configuration-merge merge --ff-only 08d68a85f24a95b70b2d806f995f04b236e4d89a
nix develop /home/aither/workspace/ai/vpsfree.cz/work/2026-11-13-oomd-restart-thresholds/merge-dev-shell -c git -C /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-13-oomd-restart-thresholds/vpsfree-cz-configuration-merge push origin HEAD:refs/heads/master
```

Exact environment dependencies are `GEM_HOME=<feature>/.gems/ruby/3.4.0`,
`BUNDLE_PATH=<feature>/.gems`, `BUNDLE_APP_CONFIG=<feature>/.bundle`, and PATH
provided by the saved pinned shell. Preserve the feature worktree/bundle and
shell profile until integration finishes. The target is not registered as a new
feature or final-head obligation. No merge, push, default-branch mutation, claim,
test, node build or cleanup was performed in P. All owned commands completed.

## Package V: focused canonical JSON verification

Lead accepted P and released V after the required full-node build was attempted
unsuccessfully. Source remains exact reviewed head
`08d68a85f24a95b70b2d806f995f04b236e4d89a`, with clean index/worktree and the
unchanged input graph above. V passed its focused configuration assertion.

Canonical first projection, CWD the original feature worktree:

```sh
timeout --foreground 55s nix develop /home/aither/workspace/ai/vpsfree.cz/work/2026-11-13-oomd-restart-thresholds/merge-dev-shell -c nix eval --json --impure --no-write-lock-file --no-update-lock-file --apply 'x: builtins.filter (p: builtins.match ".*-etc[.]drv" p != null) (builtins.attrNames (builtins.getContext x))' '.#confctl.build.m_cz_vpsfree_nodes_prg_node25_5e1cc944.toplevel.activationScript'
```

Fresh Luna/low native watcher ran this once, exit 0 in approximately 13 seconds,
under the explicit first-projection deadline. [Captured stdout](oomd-projection.json)
contains the ordinary shell-readiness banner followed by the one-element JSON
array; [stderr](oomd-projection.log) is empty. It yielded exactly one etc drv.

Direct graph inspection used these exact read-only argv, each exit 0:

```sh
nix derivation show /nix/store/1vaqc8lp512dxm3s6h8637rkm98zdl1n-etc.drv
nix derivation show /nix/store/zigk4rk1fmfsn8yrk19jvzf8nif0if48-sv-osctl-oomd-run.drv
nix derivation show /nix/store/qm4n2dlld168534ajiwdwdxnc2n5cfb3-osctl-oomd-config.json.drv
```

The first drv has exactly one direct `sv-osctl-oomd-run.drv` input (the second
path); that service drv has exactly one direct `osctl-oomd-config.json.drv` input
(the third path). Installed Nix emits derivation JSON schema version 4:
`derivations` keys and `inputs.drvs` edges are store basenames, and this JSON
leaf's actual generated value is in `structuredAttrs.value`. This is the real
`formats.json` serialization from the canonical confctl node output. No private
module evaluator or replacement module arguments were constructed.

Read-only parser probes initially expected stdout without the shell banner and
the older derivation JSON shape; those parsers exited 1 without inspecting
settings or causing mutations. Adapted only to the observed banner/schema;
the canonical projection was not rerun. Full unrelated derivations and activation
scripts were never printed. Only matching edges and this leaf's value were shown.

Parsed leaf content is exactly:

```json
{"load_multiplier": 1.5, "restart_hits": 4, "verbose": true}
```

Assertions passed for exact key/value equality and float/integer/boolean types.
[oomd-graph.json](oomd-graph.json) retains the exact chain, output identity and
assertion; [oomd-settings.json](oomd-settings.json) retains the parsed leaf value.
The JSON output identity is
`/nix/store/vp9ybgilck71psx049hspq1xn1mi9c2n-osctl-oomd-config.json`; V did not
realize it or execute its service. The serialized value proves intended merged
configuration, including inherited verbose; it does not prove a built/running
system or daemon behavior.

The required corrected full-node command
`nix develop -c confctl build --yes cz.vpsfree/nodes/prg/node25` remains failed
(exit 1 after 32.621 seconds) because
`/secrets/nodes/initrd/ssh_host_ed25519_key` is unavailable. See the lead's
[build log](node25-build-yes.log) and state. V neither supplied a secret nor
retried/overrode that build, and must not be reported as full-node build success.
No source/commit/push/merge/claim/deployment/lifecycle changes were made. All
owned commands, cells and utility work completed. Lead owns acceptance of this
bounded coverage and integration with the full-build limitation explicit.
