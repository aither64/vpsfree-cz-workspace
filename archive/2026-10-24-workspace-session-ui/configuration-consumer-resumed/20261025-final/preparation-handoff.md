# Refreshed configuration consumer preparation

Committed, quick-checked and feature-published; build, copy, activation and actual
native/provider acceptance have not been launched. The
[publication receipt](publication-receipt.json) proves the exact fresh-ref
preflight, lease publication and unchanged default.

- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- Feature: `2026-10-24-workspace-session-ui`
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/vpsfree-cz-configuration`
- Fresh default/base: `b167cd4388a5c94ff3f978df85b6800fafd1b8af`
- Head: `06351ae9dc3611d0ef5b298f5b6e5cafb4b79d4d`
- Tree: `06cbb2f13ca6cb605846ea528b9b657947e60103`
- Selected runtime: `b24164822fd33c330a6e5511e4d1580ab6590224`,
  NAR `sha256-QgmgJ9X7LQRVbht2WyOySwO9Hd81cdRfX+AAgjXUEd8=`.

The complete [series](whole.series.txt) contains one unmodified generated
`confctl inputs channel set --commit dev-workspace devWorkspace` commit.
The [whole diff](whole.diff.patch) changes only flake.lock,14 insertions and13
deletions. The channel/role/root input mapping is `dev-workspace → devWorkspace →
devWorkspace`. No application pin, provider behavior, configuration code or
documentation was changed. Existing operational guidance remains applicable;
routine pins need no configuration documentation commit.

## Source and input preservation

Fresh b167 includes six upstream commits since the old d12 base, including
retention documentation, system llm-agents EA and related merged inputs.
[Upstream history](fresh-upstream-history.txt) and
[upstream diff](fresh-upstream.diff) are retained in full. All are literal
ancestors of the refreshed feature. The old eac candidate was not replayed.
Its [diff](old-configuration.diff), [history](old-configuration-history.txt),
[verified bundle](preserved-eac.bundle) and
[old/new range-diff](old-new.range-diff.txt) preserve provenance. A raw-SHA-range
bundle command initially refused; the ordinary named-ref bundle was verified.
The old object remained reachable and no source content was lost.

[Semantic check](semantic-input-check.json) proves the node inventory, every
input edge/follows relationship, root mapping and all unrelated nodes unchanged.
Only four expected nodes change: devWorkspace, its codex-web, its llm-agents and
that native input's nixpkgs_3. The full before/after recursive graph is
[final-input-graph.json](final-input-graph.json), with the actual source paths
from the [baseline](baseline-build-plan.json) and
[final](final-build-plan.json) confctl build plans. This is structural evaluation,
not a system build. The final metadata lock graph equals the committed lock.

System root llm-agents resolves to **llm-agents_2/EAea188**, unchanged from b167.
The runtime's distinct llm-agents node advances from e85 to the same frozen EA.
Both select0.164 under the governing runtime contract; source inputs and native
identities are in the [runtime packet](../../naming-runtime-takeover/final-runtime-packet.md).
Root nixpkgsStable and Home Manager are unchanged. Compared with the older
deployed e85 package, system tools do advance to0.164; this package makes no
blanket claim that native execution is unchanged or live-compatible.

There are **no migrations** in this mechanical consumer diff and no repeated
input stream or obsolete pin commit in the final one-commit range. No final-head
deployment occurred. Existing runtime SQLite and native-state compatibility
obligations remain in combined final review and postreview acceptance; absence
of a consumer migration does not waive them. See
[history/migration inventory](history-migration.json).

## Effective input metadata discrepancy

Pinned confctl7bee58 constructs actual role source paths through resolved
`inputs.<name>.outPath`, but `mkRoleInfo` directly indexes `lock.nodes.<name>`
without following root.inputs. The exact
[source excerpt/hash](confctl-role-lookup-source.txt) and source-path NAR checks
are retained.

Home Manager metadata therefore reports transitive c47 while the actual root
selection remains home-manager_2/e28654b7 and source
`/nix/store/qh7n70gsg3rmvyn5zi1x1vhnwbrnm5wx-source`, NAR
`sha256-wnV9ttf4fPWNonBIQmvlrSlNpQYgx5HgWWd007mwIFA=`.
The same issue makes baseline llm-agents metadata report runtime-nested e85,
although its actual system root source is already EA at
`/nix/store/dyw4sx7rn0bhj9kyb3s1r58vsmh9vwj8-source`.
Final metadata happens to report EA after the runtime's distinct input advances.
Baseline and final **actual paths** for system native, Home Manager and nixpkgs
are identical. Only the runtime path changes. No speculative pin correction or
confctl source change was made.

## Quick checks and evidence reuse

Normal Nix-shell Overcommit installation/signing completed. The actual generated
commit ran Nixfmt and commit-message hooks successfully; generated full-SHA
changelog width advisories remain untouched. No hook was bypassed. See
[commit log](confctl-set.log) and [hook receipt](hook-receipt.json).
Channel mapping, Nix parse, full-range whitespace, lock semantics, input paths,
metadata equality, clean tree, runner Bash and embedded Python syntax passed.

The entire aitherdev config.nix SHA256 remains
`e728c6c268efd7bac76cac32649eab24683ff64e6a51ee16bca59f02f4fc76f5`.
Thus owner3's complete managed DeepSeek profile static schema validation is reused
at the same b167 source bytes; no duplicate validation/provider probe was run.
Its nine-string-leaf/static-only scope remains explicit in
[reuse receipt](static-profile-reuse.json). Actual assembled-wrapper identity and
isolated strict-config provider execution are pending output/review gates.
Owner0 independently checks the matching workspace composition against this
exact committed configuration; its receipt is supplied to the lead separately.

## Prepared watcher command

After combined final review and the parent's build release, a fresh Luna watcher
may run this exact file, without discovery or a guessed runner path:

```sh
test -f /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/configuration-consumer-resumed/20261025-final/prepare-aitherdev.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/configuration-consumer-resumed/20261025-final/prepare-aitherdev.sh
```

The prepared runner checks identity and the exact clean committed head, enters
its normal Nix shell, builds only cz.vpsfree/machines/aitherdev, verifies the
returned generation against the final actual input plan, captures generation,
system output/deriver, a retained output root, complete recursive derivations,
runtime closure and recursive source/input graph. It then uses copy-only for
that exact generation. It contains no claim, activation, reboot or lifecycle
action. The watcher must stop/report an unexpected local kernel build without
diagnosing or retrying. This runner has only been parsed, never executed.

## Parent activation preparation

Only after final review, successful build/copy/output inspection, ordinary
new-native idle gates and an authoritative lead-held claim for vpsfree:aitherdev,
enter the exact committed configuration's Nix shell and run:

```sh
UI_CONFIG_GENERATION=$(cat /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/configuration-consumer-resumed/20261025-final/generation-name.txt)
confctl deploy --generation "$UI_CONFIG_GENERATION" cz.vpsfree/machines/aitherdev dry-activate
# Inspect the whole dry result before this separate command:
confctl deploy --generation "$UI_CONFIG_GENERATION" cz.vpsfree/machines/aitherdev switch
```

The source diff to b167 is only the runtime channel, but activation relative to
the live host can also include merged EA system tools, retention and other
upstream changes. Require the actual dry output to identify service effects;
do not assume unchanged native processes or a metadata-only activation. Preserve
health checks and auto-rollback. Unexpected effects return to the lead before
switching. Activate the verified system before the dependent user-profile
package, through the ordinary coordinated procedure; preserve the idle gate,
old roots/state and original journals. A partial/uncertain operation keeps its
original recovery obligations. There is no downgrade-safety claim.

No default integration, machine ownership, deployment or session lifecycle
action is authorized by this preparation. The source Git window is released
after the publication/clean-state receipt; the session stays open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
