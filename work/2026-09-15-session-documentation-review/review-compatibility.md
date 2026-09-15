# Risk and compatibility review

## Findings

No Blocking, Important, or Advisory findings in the committed series.

Reviewed directly with `gpt-6-astra` / `xhigh`, using the mandatory review skill
and its risk lane. The local operator is trusted within the runtime and
workspace integration boundary; this does not relax remote-client, managed
project, or guest protections.

## Reviewed revisions

| Repository | Base | Head | Commits inspected |
| --- | --- | --- | --- |
| dev-workspace | `227bcfc1b989407582d3b022f8b388ac29972c16` | `9a1b16464e45d722110b448a79315a0f3ce134aa` | `b485d5d`, `9a1b164` |
| vpsfree-dev-workspace | `08d691cfd239260ce5bf7c269a44a49ce8de41e7` | `c6afe2905506fba0b8e372e0436b570f5597f8bd` | `dbf7a9b`, `c6afe29` |
| workspace | `d4382e7143b88e95bf093c8508c2867ff35160a1` | `7353127dc22275f24f1f92e5782fb34840dd0e49` | `9e7f55c`, `7353127` |

All three worktrees were clean and at the packet's heads when checked.

## Compatibility and safety assessment

- **Creation and retries:** runtime `libexec/dev-session:3632` (`9a1b164`)
  recognizes exact current or predecessor empty/already-seeded content. It
  preserves predecessor layout and refuses edited drafts. Plan and state can
  recover independently after an interruption. The request digest, creation
  journal, locking, and tmux identity checks remain in the existing startup
  path at `libexec/dev-session:663` and `:2424`.
- **Restart, revival, and rollback:** the added headings preserve all existing
  required markers and anchored lifecycle front matter
  (`libexec/dev-session:6687`, `:6729`). Existing tracking takes the preserving
  path at `:2027`; retained/revived requests bypass seeding at `:768`. Unfinished
  forks retain their exact-template checks at `:2098`, while current creation,
  fork, and start journals continue blocking profile changes through
  `libexec/workspace-host:1277`. No schema or state migration is introduced.
- **Catalog and link ownership:** `nix/workspace-portal.nix:58` (`b485d5d`)
  includes the core skill in the existing schema-1 catalog and explicitly
  rejects an extension collision. Distinct extension entries are preserved.
  Existing activation and rollback use the selected catalog, with removal
  limited to recognized managed links (`libexec/workspace-host:742`, `:849`);
  ordinary authored files are not deleted. Existing non-symlink destinations
  are refused at `:1875`.
- **Consumers and deployment:** extension `flake.nix:6` (`c6afe29`) pins the
  reviewed runtime, and workspace `flake.nix:6` (`7353127`) pins that extension;
  both lockfiles agree. The extension's existing skill enumeration and
  `lib.mkPackage` composition consume the core addition without duplicating
  it. No host module, Codex version, portal protocol, cluster contract, or
  configuration repository changes accompany these pins. Deployment remains a
  user-profile switch with the preceding generation retained.
- **Operational guidance:** the generic skill and guide distinguish supported
  behavior, versioned instructions, inferred rationale, and prepared versus
  executed operations. Extension handoff guidance at
  `skills/dev-session-handoff/SKILL.md:15` (`dbf7a9b`) preserves lifecycle
  authorization. Workspace `AGENTS.md:414` (`9e7f55c`) retains publication
  workflows and explicitly separates writing procedures from executing them.

## Independent focused verification

Executed with the installed Nix-profile Ruby in the runtime worktree:

- Session goal seeding, predecessor retry, exact fork recovery, malformed
  partial tracking, and revived-thread recovery: **7 tests, 74 assertions,
  zero failures/errors/skips**.
- Managed skill-link reconciliation, unfinished creation/fork/start gates,
  completed and legacy creation journals, and malformed-journal rejection:
  **7 tests, 35 assertions, zero failures/errors/skips**.

Also inspected the repository rules, plan/state, verification artifact,
individual commit boundaries, existing retained-tracking tests, packaging
interfaces, and activation/rollback implementation.

## Residual risks and test gaps

- Full Nix package/catalog builds, final-head CI, and live deployment checks
  remain for the coordinating agent after review. The added catalog check was
  inspected but was not built during this lane.
- Link rollback was exercised in the existing isolated fixture, not by switching
  the live host or launching the actual predecessor package. Preservation of
  completed records across generations was assessed from the unchanged
  validators and existing restart/revival paths.
- Automatic skill discovery and the quality of future model-authored
  documentation need the planned fresh-session check; catalog presence and
  editorial scenarios alone do not establish that behavior.
