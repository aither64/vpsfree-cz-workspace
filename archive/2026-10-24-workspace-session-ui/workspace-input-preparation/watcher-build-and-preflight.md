# Workspace candidate preparation receipt

Prepared by implementer0 for the lead's watcher; no candidate build, service
probe, machine claim or activation was launched by this package owner.

## Exact committed inputs

- Workspace repository: `git@github.com:aither64/vpsfree-cz-workspace.git`,
  default `master`, feature `2026-10-24-workspace-session-ui`.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/workspace`.
- Base `df1944a2004282d5eb988323e25c9c3010791b8d`; final
  `cbaa7d949eb4e9061cda7ff896dc6d97f2e0c2aa`; final tree
  `01c2fd8a84cedaed51d75823582b917935df9e69`.
- One mechanical commit: `deps: select session controls runtime`.
  Complete series is in [workspace-history.txt](workspace-history.txt) and final
  diff in [workspace-final.diff](workspace-final.diff). Only `flake.nix` and
  `flake.lock` change, 5 additions/5 deletions. No obsolete update commits,
  supported intermediate boundary, application change or migration is introduced.
  No migration was merged, released, deployed or externally consumed by this
  one-commit update; the candidate has not been deployed by implementer0.
- Required rebase maps reviewed old
  `b1b86b2b8a075666ccdef7f9d254047be972508a..e1c216981117c6049818a57157f0c4b6d8ad65f0`
  to `df1944a2004282d5eb988323e25c9c3010791b8d..cbaa7d949eb4e9061cda7ff896dc6d97f2e0c2aa`.
  [rebase-range-diff.txt](rebase-range-diff.txt) and stable patch IDs prove the
  sole pin patch unchanged; the complete old/new feature diffs are byte-identical.
  Full `flake.nix` and `flake.lock` bytes also match the reviewed old head.
  Original history/diff/preparation receipts remain in the `reviewed-old-*`
  artifacts. New base adds unrelated existing KB records, preserved in the
  feature's source tree; shared root was not edited by this rebase.
- Direct nested runtime `10bb047513c82d1310e8fcaa797e8772f948dd8a` →
  `9293e314e6028d71a57595073117b51bdc53c8ff`, new NAR
  `sha256-BWZF/vmlVNqRBFBqcobQmR8oEOz0MJHBYYOKOobY6BY=`.
- Extension remains `767dfd587e346168e1443e65ccdb67ce748f3fe3`, NAR
  `sha256-om/+qNfQw6y74gjdzXfVG5AbHOQGysMefFZiqR92KP4=`.
  codex-web remains `872c7ad3962f9fa9b17358244e27f3e3fac59fc5`;
  llm-agents remains `e85b99217baf13a38fc887b31338b1833f1159c0`.
- Matching configuration head at check time:
  `eac2877469a3b626f4c0d81f301f9320dae564cb`, same-session
  `vpsfree-cz-configuration` worktree. Its lock is retained as
  [configuration-final.lock.json](configuration-final.lock.json). That owner
  reports confctl's effective Home Manager input agrees with deployed metadata;
  do not infer the effective input from an unrelated root node.

Complete composed flake graphs are preserved in
[workspace-old.lock.json](workspace-old.lock.json),
[workspace-new.lock.json](workspace-new.lock.json), and the actual selected
composition's [selected-composition.lock.json](selected-composition.lock.json).
[semantic-input-check.json](semantic-input-check.json) proves all nodes other
than `dev-workspace`, all follows paths and all runtime dependencies unchanged.
No top-level runtime input, extension lock or deduplication was introduced.

Quick evidence: Nix-shell deployment-contract tests passed 4 runs/19 assertions;
the real cross-repository checker passed at the exact runtime above and canonical
portal hostname/aliases. `nix-instantiate --parse flake.nix` and whitespace checks
passed. No declared hook framework or `core.hooksPath`; ordinary Nix-shell commit
used no bypass. An accidental Ruby parser invocation on `flake.nix` failed because
it was the wrong language; the proper Nix parser passed. No source repair followed.

## Live preparation snapshot (refresh before activation)

Selected profile `~/.local/state/dev-workspaces/profile` → `profile-187-link` →
`/nix/store/8ph05i3nps8xi1jfs450b16aysc16nvg-dev-workspace-0.2.0`; deriver
`/nix/store/idaz4jqnjy572qi03shxa26bkjlrgpq9-dev-workspace-0.2.0.drv`.
Its complete recursive derivation/input-source graph is retained in
[selected-profile-derivations.json](selected-profile-derivations.json).
Runtime source `/nix/store/r2pxv5h275gk9njy59rbk4ydsjy38hx4-source`;
composition source `/nix/store/3g4dbw0nzyvc01gfbr08x35slccqnf0v-source`.

Both live system and system profile resolve to
`/nix/store/n6b9dmmaw83zx80paglrisy0w5rwnfw8-nixos-system-aitherdev-26.05.20261021.da6dc0e`.
Full deployed configuration/input metadata is retained as
[current-system-configuration.json](current-system-configuration.json) and
[current-system-inputs.json](current-system-inputs.json).

The native active package is
`/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0`.
At inspection `workspace-codex@vpsfree-cz.service` MainPID was `3387667`, with
`/proc/3387667/exe` resolving to that package's
`libexec/codex/bin/codex`. The immutable
[live-launch-marker.json](live-launch-marker.json) retains its actual launch
package `s4fbv3hya8l09jh4a67rd4brdkwx4piz-dev-workspace-0.2.0`, reporting argv,
policy 1, digest and required native child capacity 0. Catalog capacity is a
separate field; never replace the launch marker's capacity with a catalog total.
[live-registration-inventory.json](live-registration-inventory.json) is separate
selection inventory. [live-runtime-contract.json](live-runtime-contract.json)
retains the selected package contract. Do not edit these live files.

## Watcher-ready composed build

After the lead records the applicable final review disposition, launch a fresh
verification watcher with the existing monitor skill and this exact command:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/workspace-input-preparation/build-workspace-candidate.sh
```

The script guards exact head/clean source and preserves candidate flake metadata,
output path, deriver, full recursive derivation/input graph and output dependency
closure. It calls the required composed build:

```sh
nix build --no-link --print-out-paths --print-build-logs .#packages.x86_64-linux.default
```

It performs no activation. Stop/report unexpected kernel builds. Do not overwrite
an existing candidate receipt after partial failure: inspect it and reconcile
before a lead-authorized retry. The configuration owner/lead captures the exact
system generation, system toplevel/deriver and full effective source/input graph
separately; compare both graphs to these selected/candidate receipts.

## Candidate versus live preflight recipe

Use the exact built output from `candidate-output-paths.txt`. These checks remain
prepared, not executed. A mismatch returns to the lead before ownership/activation;
do not bypass checks, choose a system-Codex override, restart a daemon, or change
a provider to make the candidate fit.

1. Resolve `candidate/libexec/codex/bin/codex` and the active native package's
   `bin/codex` using `readlink -f`. Require the exact same immutable executable
   path as the launch marker's `launch.codex_path`. Also compare the candidate's
   underlying `libexec/codex/libexec/codex/bin/codex` with the freshly observed
   `/proc/MAINPID/exe`: canonical path, SHA-256 and bytes (`cmp`) must agree.
   Record the native package manifest/resources/helpers and their derivations
   from the composed closure. Version, source revision or standalone product
   output equality is insufficient. Require no `DEV_WORKSPACES_SYSTEM_CODEX`
   override. Preserve native PID/proc argv as pre/post evidence without dumping
   process environment.
2. Read the candidate, selected package and actual launch package's
   `share/workspace-portal/runtime-contract.json`. Require live-switch policy 1,
   reporting policy 1 and unchanged compatible authority/session/provider/
   recovery/cluster/tracking contracts. Compare `claim-contract.json`,
   `repository-claim-contract.json`, `coordination-contract.json`,
   `integration-contract.json`, `coordination.json`, `integration.json` and
   `extensions.json` with the selected package. Package paths in catalogs may
   differ; inspect semantic commands/provider identities and exact source graph,
   never accept an unexplained behavior change as path churn.
3. Capture candidate registration without selecting it through its public,
   read-only helper, matching ordinary host invocation:

   ```sh
   printf '%s\n' '{"schema":1}' | "$candidate/bin/workspace-portal" agent-teams registration \
     --package-root "$candidate" \
     --state-root /home/aither/.local/state/dev-workspaces \
     --workspace /home/aither/workspace/ai/vpsfree.cz \
     --host-profile /home/aither/.local/state/dev-workspaces/profile
   ```

   Save complete output under this receipt directory. Compare `policy` and
   `required_native_child_threads` with the fresh launch marker; compare actual
   argv. The only allowed live argv difference under reporting policy 1 is the
   package-dependent reporting executable path. Both complete invocations must
   validate as the same workspace/state-root/profile, `team-mcp`, required=true,
   enabled tool exactly `report_to_lead`, approval mode `approve`. No other args
   may change. Preserve launch provenance; inventory may describe the new package.
4. Compare selected/candidate `agent-teams.json` catalog digest, capacity, native
   configs and role policy, then compare retained registration-state identities
   without editing saved roster settings. Validate extension catalog provider
   IDs/helper contracts and runtime cluster schema 1/transition policy 3/tracking
   bounds against the selected package and retained cluster identity. Use public
   read-only inspection; no lifecycle commands, cluster create/access/reset or
   private transition helpers. If checks require more than bounded reads, the
   lead assigns the exact verification scope.
5. Refresh exact system/profile/source/native/marker identities before the lead's
   ordinary claim-bound switch. The ordinary switch repeats authoritative
   generation, ownership, registration and transition checks under its locks;
   this recipe does not substitute for those checks or authorize activation.

No default integration is approved. Physical deployment alias mapping is
`vpsfree:aitherdev` / `aitherdev` / `aitherdev.int.vpsfree.cz` /
`cz.vpsfree/machines/aitherdev`, target `172.16.106.40`. The lead owns claims,
system-before-profile activation, effect verification and eventual release after
complete approved integrated lineage. No session lifecycle action is authorized.
