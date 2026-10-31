# Downstream preparation and verification

Owner: implementer1. Updated 2026-10-31. Status: both consumers committed,
published and clean, ready for affected final independent review with runtime
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79`. Quick checks passed; the unrelated
preexisting optional workspace formatter difference was accepted by the lead
and left unchanged. Review and longer verification remain lead-coordinated.
No builds, copies, deployments, merges or resource claims were performed here.

Session identity was verified with `dev-session current` from this session's
directory, matching the trusted thread binding. Both environment markers were
absent. The live roster confirms implementer1 has workspace-write access.

## Scope and baselines

Own both downstream branches, their Git operations, generated pins, hooks,
quick checks and follow-up fixes. Preserve the direct nested runtime override,
extension, native/Codex versions and unrelated inputs. Keep one final logical
runtime-pin update per consumer. Lead owns tracking, final review coordination,
longer verification, machine ownership, activation and integration.

| Repository | Feature worktree | Final base | Published final head |
| --- | --- | --- | --- |
| workspace | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-codex-profile-generations/workspace` | `c83620f63200da8274efbbaebfc985f35d4b9e1d` | `7a0a8fd1317c9dc17b79a99c1a27e182ac988ab1` |
| vpsfree-cz-configuration | `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-codex-profile-generations/vpsfree-cz-configuration` | `e34f08314b6db1ac38facc2386b79111daee864f` | `2e1d9e957a5c11fda47bdea8f12dffbafa8064ee` |

Both use branch `2026-10-27-codex-profile-generations` and were registered through
`dev-session worktree add`. Both were clean after preparation. During the
lead-granted shared Git window, workspace fetch showed shared master ahead of
remote master `019ea536593cbf27abde9ec157a24ce126fbb655` by one inherited commit,
with zero divergence. The workspace feature starts at shared master as directed;
configuration starts at freshly fetched `origin/master`. The shared Git window
has been returned to the lead.

Both effective runtime locks initially select
`6f54d0c7fdb974705c120b3c1ef5372f5897d544`. Workspace extension selection is
`767dfd587e346168e1443e65ccdb67ce748f3fe3`. Configuration's `dev-workspace` channel
maps role `devWorkspace` to flake input `devWorkspace`. Its pinned confctl is
`7bee58a52372b95c2198ce3f2a719807a3c2c66b`.

Both final locks select runtime `c2182254d29c4175c3e9fe4267e5a92dd1da6b79`,
`narHash = sha256-k6d90hicmnStL/tT6AeBLbYBQ5U7O/pmUls1zGYwsMg=`,
`lastModified = 1793457903`. No native/Codex version or extension update occurred.

## Final inventory, checks and rebase evidence

Each owned final range in the table contains one commit and one final logical
runtime-pin stream. Workspace commit `7a0a8fd1`,
`inputs: select runtime without redundant Codex history`, changes only the nested
URL in `flake.nix` and generated `flake.lock` (5 insertions/5 deletions).
Configuration commit `2e1d9e95`, `inputs: set devWorkspace to c2182254`, changes
only generated `flake.lock` (3 insertions/3 deletions). Its generated changelog
and commit message were preserved. There are no superseded pin updates,
intermediate consumers, obsolete approaches or compatibility paths to retain.
There are **no migrations** in either consumer branch, hence no consumer
migration merge/release/deployment/external-use provenance. Runtime collector
migration behavior belongs to the separate runtime change and combined review.

Quick evidence:

- Before/after semantic lock comparisons passed: only each intended runtime node
  changed; workspace additionally updated its exact nested original revision.
  Extension revision/content hash, all other nodes, follows, siblings and runtime
  input mappings stayed identical. Full runtime locked records match.
- With workspace-pinned tools from
  `nix shell --inputs-from . nixpkgs#ruby nixpkgs#nixfmt --max-jobs 0 -c ...`,
  `ruby test/deployment_contract_test.rb` passed **4 runs, 19 assertions,
  0 failures/errors/skips**. The actual composed deployment contract passed at
  the final runtime SHA. Complete owned-range `git diff --check` passed.
- Configuration Overcommit installation/signing and generated commit hooks
  passed. Only accepted generated-message text-width warnings were emitted.
  No hooks were bypassed. SSH publication succeeded; `git ls-remote` proved
  both exact final heads. Both worktrees had empty `git status --porcelain=v1`.

Configuration's tools-shell GEM_PATH initially hid Minitest. Running the workspace
test in its own pinned Nix shell resolved this environment issue (Ruby 3.4.9).
No assertion failed. Optional whole-file `nixfmt --check flake.nix` with pinned
nixfmt 1.4.0 exposed preexisting formatting at the untouched storage-retention
`nativeBuildInputs = [ pkgs.ruby pkgs.git ];` list. Reproduction on the original
base's `git show HEAD:flake.nix` failed identically; formatter preview only expands
that unrelated list. Lead explicitly accepted leaving it unchanged. Workspace
declares no mandatory formatter hook. No further optional checks were run.

The workspace original range was
`a1b404fab578b71454f11760e6d0a8097b0e179f..0f7e91687dd21d0db74b3339c6cd97d0da7f9d10`.
Lead required a rebase onto shared master after it advanced to
`5d508b850ebd7c3720e9772ebc9ab431e6dea012`. The additional commit only changes
tracking/archive paths; diffstat was inspected without reading another session's
contents. Lead confirmed inherited shared commits `a1b404fa` and `5d508b850`
are tracking-only. The new range is
`5d508b850ebd7c3720e9772ebc9ab431e6dea012..6fa6c0f218f5ee2d887f1669bec86cfec6959a91`.

For that earlier tracking-only rebase,
`git range-diff OLD_BASE..OLD_HEAD NEW_BASE..NEW_HEAD` reports the sole commit
as `=`. Old/new owned patches are byte-identical (`cmp`); stable patch IDs are
both `60935391672888d5a8e09bb1c51f587c8e11fe9f`. `flake.nix` blob stayed
`09ac8eabee8b62d3fc5ef9502faaf4c7f9e13458`; `flake.lock` blob stayed
`a6d9ad4fdf1ce162cc2ed50f3f8515ab01177764`. The relevant real deployment contract
and new-range whitespace check passed after rebase. Publication used an exact
`--force-with-lease=refs/heads/2026-10-27-codex-profile-generations:0f7e91687dd21d0db74b3339c6cd97d0da7f9d10`;
fresh `ls-remote` confirms `6fa6c0f2`. GitHub Actions exact-branch run list was
empty, so no superseded runs required cancellation. Configuration stayed at its
original published head. No deployment preceded the rebase, and shared default
and shared index were untouched.

Routine pins need no separate product documentation change. The accepted design,
selected runtime guide and runtime-owned documentation explain the behavior;
this artifact retains consumer and rollout-specific evidence.

## Refresh onto current extension and instruction baseline

Shared and freshly fetched remote master advanced to
`c83620f63200da8274efbbaebfc985f35d4b9e1d`. It selects extension
`e4e7e95ed39bf514b33f8f8ae61ba9868de060ae`, content hash
`sha256-5tnBT6j5LzwkYTffhWQ7mWpDkWMisxbCpFpbtDOjBlc=`, and includes accepted
source/writing instruction changes. Current AGENTS, applicable procedures and
changed documentation routing were reread. Their changes remain in the feature
base unchanged; this package authors no instruction or extension update.

Refreshed range:
`c83620f63200da8274efbbaebfc985f35d4b9e1d..7a0a8fd1317c9dc17b79a99c1a27e182ac988ab1`.
Immediately preceding reviewed range:
`5d508b850ebd7c3720e9772ebc9ab431e6dea012..6fa6c0f218f5ee2d887f1669bec86cfec6959a91`.
Only adjacent `flake.nix` URLs conflicted: preserve the new extension URL and apply
the original exact runtime URL. Lead explicitly accepted that routine resolution.
The lock auto-merged only the intended runtime node; repeating the required nested
`nix flake update vpsfree-dev-workspace/dev-workspace` made no additional change.

The final tree was independently reconstructed from current base: `flake.nix`
equals its base with only the same runtime URL replacement, and the entire lock
equals its base with only the original runtime-node replacement. Every other
source path matches current base; all extension identities, siblings, follows
paths and runtime dependencies remain unchanged. Old/new semantic pin deltas
match exactly. Range-diff shows only the adjacent extension context change;
stable patch IDs therefore differ (`60935391672888d5a8e09bb1c51f587c8e11fe9f`
versus `169b5a41df5a7a6faa052e68f6f4e55207f3ddf9`). This is semantic
equivalence of the pin delta, not byte-identical complete compositions or equal
patch IDs. Full old/new base/head lock graphs and source hashes are retained in
`downstream-refresh-inputs.json`; the prior receipt remains `rollout-inputs.json`.

Refreshed quick checks passed: 4 tests/19 assertions, actual two-consumer
deployment contract at `c2182254`, semantic reconstruction and complete-range
whitespace. No declared workspace hooks or framework appeared; none was
bypassed. Exact leased force-push expected old head `6fa6c0f2`; fresh remote
feature proof confirms `7a0a8fd1`, and Git status is clean. Exact-branch CI list
was empty, so no superseded runs needed cancellation. Still one final pin stream,
no migrations and no session-deployed old workspace head. Runtime and
configuration heads/pins remain unchanged. No activation, merge or claim occurred.

After affected final review, a fresh verification watcher should run from the
refreshed workspace feature worktree:

```sh
nix build .#packages.x86_64-linux.default .#checks.x86_64-linux.deployment-contract \
  --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-codex-profile-generations/prepared-application-refreshed \
  --print-build-logs --print-out-paths
```

No build was started here. Evaluated refreshed application derivation:
`/nix/store/2jvhgyq2ilxa4cprlswc7fwh93b3snpx-dev-workspace-0.2.0.drv`, expected
output `/nix/store/0q7rc75dh4mjrxpb37m1hchfwcbmpa7a-dev-workspace-0.2.0`.
Refreshed deployment-contract derivation:
`/nix/store/3wlzx7rciz57afhq5i2r9vr85z1bqrir-dev-workspace-deployment-contract-tests.drv`,
expected output `/nix/store/nlp2zb1g3z4jwvzsgfi6nn76065138ys-dev-workspace-deployment-contract-tests`.
Both differ from previously successful `79a03hkjv2lwdc3ziikyy11khhxq7j5v`
application and `nzzm2dkh2zi08iac3jzd1y2gj8ag5wsb` contract derivations; the old
application/contract build receipt does not validate the new composition.

Runtime and configuration full lock graphs still exactly match their original
receipt hashes (`fa808c04beeaf2ea5d6dfb4b76b1bd6ff1a166e298771de3756a646a5294a955`
and `1e5f7e9af62ffa70e3f94e4a0d63f2ba5f36760e1ffe499c201aacf247e05e5e`).
New workspace lock hash is
`68485a53a69556716c28df31dc3d72679446c569f09b8b21bd13d05029772ec6`.
Current configuration toplevel evaluation yields the same derivation as retained
prepared output `/nix/store/4wpwzqrb3c51bbibwzqavjlc6qjcpiv0-nixos-system-aitherdev-26.05.20261026.718f670`:
`/nix/store/42a2ii9r9s7h0969gwdxjzhgiasl4jcr-nixos-system-aitherdev-26.05.20261026.718f670.drv`.
That exact system generation remains reusable under the unchanged source/input
receipt; this does not authorize activation. Current runtime evaluations also
match all original successful check derivations:

| Runtime check | Exact unchanged derivation |
| --- | --- |
| ruby-workspace_host-0 | `/nix/store/d843bz4b8q1ddyv8rdy8w94yjfhkzn4p-dev-workspace-workspace_host-0-of-1.drv` |
| ruby-coordination_gc-0 | `/nix/store/f5mw0zn7qi7l914pld2b684d4ppc5q94-dev-workspace-coordination_gc-0-of-1.drv` |
| ruby-workspace_coordination-0 | `/nix/store/bczndbjg4dbbr70wpvrh120qh98n715k-dev-workspace-workspace_coordination-0-of-2.drv` |
| ruby-workspace_coordination-1 | `/nix/store/00rn61cxgmsiiraxnw086yvcrg9bzjpp-dev-workspace-workspace_coordination-1-of-2.drv` |
| session-creation | `/nix/store/2sma25j1bh8862lwrij0zpcwhk44sj7p-vm-test-run-dev-workspace-session-creation.drv` |

The four Ruby derivations match `verification-batch-1.log` and its passed step 1
receipt. The VM derivation matches `creation-ci-reuse.json`, which binds the
successful exact CI test and driver; the intentionally canceled local duplicate
remains canceled. Unchanged complete runtime graph/head and equal check
derivations support reuse of that successful runtime evidence. No runtime check,
VM or system build was rerun during this refresh; only Nix identity evaluation
and the affected quick workspace checks ran.

## Environment and hooks

Workspace declares no hook framework and has no common pre-commit/post-checkout
hooks. Configuration has installed executable Overcommit hooks and declares
Nixfmt/RuboCop. Its development shell uses Ruby 3.4 and bootstraps worktree-local
`.gems`, `.bin` and Bundler configuration. Before the first configuration commit,
from its writable worktree:

```sh
nix develop -c bundle exec overcommit --install
# Inspect declared configuration/custom hooks before accepting their signatures.
nix develop -c bundle exec overcommit --sign
```

Run hook-sensitive Git commands in that same repository's Nix environment.
Do not disable hooks. Configuration's hook dependency bootstrap, installation and
signing have now completed. No Nix package build was needed for source preparation.

Preparation encountered a known setup edge: entering its tools-mode flake shell
from the shared workspace fails because CWD has no Gemfile. Using the read-only
Nix source as CWD then cannot create local gems. The inherited post-checkout hook
failed for missing gems after Git had already created the feature branch and
worktree. Exact HEAD and clean status were checked; retrying ordinary native
registration reused that worktree and succeeded. No command remains running.
Use the actual writable configuration worktree for subsequent shell commands.

The obsolete coordination operations document observed in stale bare master is
already absent from the fresh configuration base. Use the selected runtime's
`workspace-host coordination guide` and accepted design brief.

## Pinning and quick checks

Use the lead-supplied exact runtime SHA. In the workspace feature worktree, edit
only `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`, then run:

```sh
nix flake update vpsfree-dev-workspace/dev-workspace
```

In the configuration feature worktree:

```sh
nix develop -c confctl inputs channel set --commit dev-workspace devWorkspace EXACT_RUNTIME_SHA
```

Preserve confctl's generated commit message. Before final review, inspect
semantic before/after input graphs, extension revision/content hash, siblings and
follows paths, allowing only the intended runtime identity update and necessary
transitive changes. Run `git diff --check`, declared hooks, the existing
`test/deployment_contract_test.rb` with Nix-provided Ruby, and the real composed
contract:

```sh
bin/check-dev-workspace-deployment --workspace-root "$W" --configuration-root "$C"
```

Here `W` and `C` are the full worktree paths above. Commit and publish exact
feature heads after fresh-target checks/rebase as appropriate. Inventory each
complete base-to-head series and final diff, identify its single generated pin
stream, and explicitly report that these consumer changes contain no migrations.
Routine channel pins need no separate product documentation change.

## Prepared post-review build and activation commands

These commands were checked against pinned confctl source and the workspace
flake; they have **not been executed**. Run longer verification through the
lead's fresh verification watcher, after combined independent final review.
Build from final committed sources; confctl embeds the configuration revision.

From `W`, prepare the application output:

```sh
nix build .#packages.x86_64-linux.default \
  --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-codex-profile-generations/prepared-application \
  --print-out-paths
```

`packages.x86_64-linux.vpsfree-dev-workspace` is an alias of the same package.
Available workspace check attributes are
`checks.x86_64-linux.{deployment-contract,tracking-source,agent-instructions,agent-team-policy,storage-retention,cluster-provider-composition}`;
the lead selects applicable longer verification.

From `C`, build and retain a confctl generation:

```sh
nix develop -c confctl build --yes cz.vpsfree/machines/aitherdev
GEN=$(readlink .confctl/generations/cz.vpsfree:machines:aitherdev/current)
nix develop -c confctl generation ls --local cz.vpsfree/machines/aitherdev
nix develop -c confctl deploy --yes --generation "$GEN" --copy-only cz.vpsfree/machines/aitherdev
```

Confctl builds
`confctl.build.m_cz_vpsfree_machines_aitherdev_0b1e0938.toplevel` and
`confctl.build.m_cz_vpsfree_machines_aitherdev_0b1e0938.autoRollback`.
Retain the exact generation name, `generation.json`, toplevel and auto-rollback
paths in the rollout record. `--generation "$GEN"` reuses that prepared generation
instead of rebuilding; `--copy-only` returns before activation. `current` is also
supported, but the exact name avoids later selector changes. A naked Nix build
does not create the corresponding confctl generation metadata.

Only the lead, under the held `vpsfree:aitherdev` machine claim, runs from `C`:

```sh
nix develop -c confctl deploy --yes --generation "$GEN" cz.vpsfree/machines/aitherdev dry-activate
nix develop -c confctl deploy --yes --generation "$GEN" cz.vpsfree/machines/aitherdev switch
```

Preserve configured auto-rollback; do not pass `--disable-auto-rollback` or
`--reboot`. Deploy checks/copies the closure again; there is no skip-copy flag.
Generation reuse prevents another build. Confctl activates the system and then
publishes its profile separately: verify both `/run/current-system` and
`/nix/var/nix/profiles/system`. `--dry-activate-first` can combine dry activation
with switch, but the accepted sequence uses the two explicit commands above.

After system verification, only the lead, under that same held machine claim:

```sh
env DEV_SESSION_SLUG=2026-10-27-codex-profile-generations \
  DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
  DEV_WORKSPACE_CLAIM_ID=HELD_CLAIM_UUID \
  workspace-host switch --source "$W"
```

Ordinary workspace-host owns package compatibility, activation journals and
forward recovery. Application selection remains in the user profile. Preserve
exact committed sources, complete input graphs, store outputs and live verification
in the rollout record. Machine release and approved integration remain lead-owned.

Command evidence: pinned confctl `lib/confctl/cli/app.rb`,
`lib/confctl/cli/cluster.rb`, `lib/confctl/nix_flake.rb`,
`lib/confctl/generation/{build,build_list}.rb`, and
`nix/flake/{mk-config-devshell,mk-confctl-outputs}.nix`.

## Configuration integration target preparation

Prepared outside claims after a fresh fetch; configuration `origin/master`
remained `e34f08314b6db1ac38facc2386b79111daee864f`. Detached target:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-codex-profile-generations/merge-vpsfree-cz-configuration`.
Its exact HEAD is that remote base and `git status --porcelain=v1` is empty.
The target is an ancestor of feature `2e1d9e957a5c11fda47bdea8f12dffbafa8064ee`.
Both published feature heads remain untouched.

Read target AGENTS, hook configuration and custom Nixfmt code. Configuration,
custom hooks, Gemfile, Gemfile.lock and flake.nix are identical across target
and feature. From the writable target, setup completed with:

```sh
nix develop --max-jobs 0 -c bundle exec overcommit --install
nix develop --max-jobs 0 -c bash -c 'set -e
bundle exec overcommit --sign
bundle exec overcommit --sign pre-commit
bundle exec overcommit --list-hooks'
```

Target-local `.gems`/`.bin` bootstrap completed. Configuration signature is
trusted; no plugin signature changes were needed. Nixfmt/RuboCop are enabled,
and pre-commit, commit-msg, post-checkout, post-merge and pre-push hooks are
executable. Setup/listing did not run checks, tests or package builds; no hooks
were bypassed. No merge, push, shared-default/index mutation or claim was made.

Only the lead, after approval/preparation and fresh target/feature/ref/clean
checks under the repository claim, may run from this target:

```sh
nix develop --max-jobs 0 -c git merge --ff-only 2e1d9e957a5c11fda47bdea8f12dffbafa8064ee
nix develop --max-jobs 0 -c git push origin HEAD:refs/heads/master
git ls-remote origin refs/heads/master
```

Inspect ordinary hook results and remote proof, then release repository ownership
before records or CI. Leave this target available for the lead's integration.

## Pre-rollout live state supplied by lead

Read-only lead refresh; downstream implementer made no live changes:

- System/profile:
  `/nix/store/hsci7shrxm3a5gy642jzhp7yd54adgni-nixos-system-aitherdev-26.05.20261026.718f670`.
- Application:
  `/nix/store/413w4bai6br4c2vq08gx9diq55iasvqk-dev-workspace-0.2.0`.
- Selected Codex:
  `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0`.
- Numeric history links: 168.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-codex-profile-generations/
