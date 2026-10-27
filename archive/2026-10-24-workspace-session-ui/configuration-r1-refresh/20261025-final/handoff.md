# Corrected-client configuration consumer

Committed and quick-checked; feature publication is held for the parent's
mechanical-transfer assessment. Build, copy and activation have not run.

- Repository: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
- Feature/worktree: `2026-10-24-workspace-session-ui`,
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/vpsfree-cz-configuration`
- Fresh default/base: `b167cd4388a5c94ff3f978df85b6800fafd1b8af`
- Reviewed published head: `06351ae9dc3611d0ef5b298f5b6e5cafb4b79d4d`
- Final head: `508ab4684c1c22e0f8d386353e6fcf87ce2dce63`
- Final tree: `1ce2c2c25688aa9c6e82556502959538188089bb`
- Runtime: published `5eb5bff620a302239179edb4736f0c2196d58437`, NAR
  `sha256-sL80sBPH/24+d1sefwY0uSIXE9c7ejpK0w3s7tWsvqo=`.

Normal `confctl inputs channel set --commit dev-workspace devWorkspace` generated
one final lock-only commit. Its changelog and hook output remain unmodified in
[confctl-set.log](confctl-set.log): Nixfmt and commit-message hooks passed, with
the expected generated full-SHA width advisories. No hook was bypassed. The
channel/role/root mapping remains `dev-workspace → devWorkspace → devWorkspace`.

The [complete series](final.series.txt) has one commit and the
[whole diff](final-base-to-head.diff) changes only flake.lock,14 insertions and13
deletions. From reviewed063, only devWorkspace and its codex-web lock nodes
change. From fresh b167, the expected four runtime-owned nodes differ:
devWorkspace, codex-web, llm-agents and nixpkgs_3. Node inventory, root mapping,
all input edges/follows and every unrelated node remain unchanged. No config,
provider, application system pin, native source policy or documentation edits
are included.

[Mechanical transfer](mechanical-transfer.json),
[complete mode/blob inventory](final-mode-blob-inventory.json),
[reviewed-to-final diff](reviewed-to-final.diff),
[old/new range-diff](reviewed-to-final.range-diff.txt) and
[full source/input graph](final-input-graph.json) bind the result. All paths and
modes outside flake.lock equal reviewed063. The old pin was replaced, not replayed:
the final branch has one runtime input stream and no obsolete intermediate
pin/fixup. Reviewed063 remains in the local ref
`refs/session-evidence/2026-10-24-workspace-session-ui/reviewed-063`, verified
bundle and full old range. Earlier eac/source/rollout provenance remains in the
[original preparation](../../configuration-consumer-resumed/20261025-final/preparation-handoff.md).
All merged b167 inputs, source and retention docs are literal ancestors/preserved.

There are **no migrations** in this mechanical consumer. Runtime and underlying
shared-client R1 are separate review scopes; the client repair is substantive
and has its own affected review. No whole-branch/client equivalence or native
state-compatibility acceptance is inferred from this input transfer.

## Effective source and quick checks

The final [actual confctl build plan](final-build-plan.json) is structural
evaluation only. Its system EA, Home Manager and nixpkgs source paths equal the
reviewed063 and freshb167 plans; only the runtime source advances to dq5417.
All role source NARs match their actual root-resolved lock nodes. System native
still resolves through root llm-agents_2/EAea188; runtime separately owns the same
frozen EA. The existing Home Manager c47 metadata versus actual root e286 lookup
discrepancy is unchanged and explained in the prior preparation. No speculative
metadata/pin correction was made.

Channel mapping, Nix parse, both full-range whitespace checks, semantic lock
comparison, effective source/NAR checks, metadata-lock equality, clean state and
prepared runner Bash/embedded-Python syntax passed. Exact aitherdev config.nix
still hashes to e728c6c268efd7bac76cac32649eab24683ff64e6a51ee16bca59f02f4fc76f5,
so owner3's whole-profile static DeepSeek receipt remains reusable; no duplicate
schema/native/provider execution was run. Owner0 receives this exact committed
head for its independent matching-workspace checker.

The command-wrapper sequencing was reconciled: the confctl Nix wrapper started
before the prior empty-suffix rebase wrapper's completion had been fully
collected. Both settled successfully; the generated commit's exact parent is
b167 and confctl observed baseline runtime963 before its update. No ref/source
conflict or uncertain effect remains. See
[reconciliation](operation-reconciliation.json).

## Prepared build/copy recipe

After the parent accepts mechanical transfer and releases builds, a fresh Luna
watcher may run exactly:

```sh
test -f /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/configuration-r1-refresh/20261025-final/prepare-aitherdev.sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/configuration-r1-refresh/20261025-final/prepare-aitherdev.sh
```

[Recipe guards](build-recipe-guards.json) bind the exact508 head and5eb runtime.
The recipe checks session/clean source, uses ordinary confctl, captures the actual
generation, system output/deriver and retained root, full recursive derivation and
input graphs, then performs copy-only for that exact generation. It has only been
parsed, never executed. There is no activation, claim, reboot or lifecycle action.
Stop/report unexpected local kernel compilation; do not diagnose or retry in the
watcher. Parent owns both build release and the ordinary source/output acceptance.

After actual build/copy/output review, native/state/idle prerequisites and an
authoritative lead-held vpsfree:aitherdev claim, the parent's separate activation
commands from this exact worktree's Nix shell are:

```sh
UI_CONFIG_GENERATION=$(cat /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/configuration-r1-refresh/20261025-final/generation-name.txt)
confctl deploy --generation "$UI_CONFIG_GENERATION" cz.vpsfree/machines/aitherdev dry-activate
# Inspect the entire result before this separate command:
confctl deploy --generation "$UI_CONFIG_GENERATION" cz.vpsfree/machines/aitherdev switch
```

Relative to b167 the source is only a runtime channel update. Relative to the
live host, merged EA native/retention/upstream changes can also apply; actual
dry output must establish service effects. Do not assume metadata-only change
or unchanged native processes. Preserve health checks/auto-rollback, idle guards,
old roots/state and original recovery journals. System precedes dependent user
profile selection through the ordinary coordinated procedure. No downgrade
safety or live mixed-writer support is claimed.

Publication still needs parent assessment followed by fresh SSH masterb167 and
exact own-feature063 lease preflight. Only the dated feature may be pushed;
stop/report drift. No default integration, claim, live probe, activation, build,
native/provider invocation or session lifecycle action occurred. No operation
remains running; source is frozen at this completed package.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
