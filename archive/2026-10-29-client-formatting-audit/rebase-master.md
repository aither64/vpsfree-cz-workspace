# Rebase onto updated HaveAPI master

User direction: “haveapi master moved, so rebase onto it”. Implementer2 received
exclusive team source/Git ownership for this bounded replay. Integration into
master and publication were not authorized or performed.

Repository: `git@github.com:vpsfreecz/haveapi.git`.
Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-29-client-formatting-audit/haveapi`.
Branch: `2026-10-29-client-formatting-audit`.
Session/current/environment and saved workspace_write settings were verified.

## Exact lineage and ranges

- Old base: `ae46cf27a9afb6558d386c293cec7231dd6c423d`.
- Old feature head: `d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038` (also remote feature at lead's pre-task fetch).
- Fetched target master/new base: `c79645e0d43885c26cdc4129cbac96fdd5a13b07`.
- New feature head: `7edb003dd5d5a058b3308510bb8a5f60387ad654`.
- New feature tree: `ed397888e12edcd0ec81fc0ac078e593f78ea0b0`.
- Old owned range: `ae46cf27a9afb6558d386c293cec7231dd6c423d..d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038`.
- New owned range: `c79645e0d43885c26cdc4129cbac96fdd5a13b07..7edb003dd5d5a058b3308510bb8a5f60387ad654`.
- Both ranges contain exactly ten logical formatting commits. The inherited
  documentation redesign is already in master and was not replayed or duplicated.
- Merge-base proofs establish old base is an ancestor of new master and new
  master is the exact parent-line base of the new ten-commit feature range.

New upstream commits above the inherited base:

```text
ddf836fbb33ec6f920c3edfd9a4a53c2c2eb494b docs: escape generated CLI and curl arguments
a3f522e509faaf9da34d9e87c7f7e9246c76bd6c clients/ruby: escape CLI help example arguments
aee093cd3387c261570067e58b7f1e16029e3619 docs: make CLI and curl response transcripts inert
c79645e0d43885c26cdc4129cbac96fdd5a13b07 servers/ruby: expect normalized shell option names
```

## Complete resulting ten-commit series

```text
173edf81a7ed32b736153bc0fda4a2966e4994f9 clients/js: normalize authored source with Prettier defaults
a7209152fda6a32fd5ba175410a8f42653450a69 clients/js: enforce shared Prettier defaults for authored source
3ac5ef632edd0090f07e4b2a223ab31ac5026db9 ci: cover Ruby tooling inputs in RuboCop triggers
e5769f47f19558975ebb41054eb8843f031cca1a clients/go: cover formatting failures and canonical output
717d6272daee3073d00798a50a24ace3ad57150b clients/php: apply canonical source formatting
125c7723b2dba683f60eae26829e5c5f9889d2a0 clients/php: enforce style and PHP 8.0 syntax
74679a6b2d8eeb95cf4d0b092543499c3f412c58 clients/typescript: format generated clients with Prettier
8e482036546fdc8234c2621e3a8512c7fd6e4052 release: verify formatted TypeScript generator packages
108d8f0fc4bdf864c01b14b551aac1f9e8417552 clients: align formatting tools and contributor checks
7edb003dd5d5a058b3308510bb8a5f60387ad654 clients/rust: verify fixture formatting and failures
```

## Equivalence and independent reconstruction

All ten patches compare equal in the full range-diff below. The complete binary
feature patch old-base..old-head is byte-for-byte identical to the complete
binary feature patch new-base..new-head. Its SHA-256 is:

```text
fbdcf10b77ce1852047b4d46491e47decab7858d85d38b422265ab3128515124
```

The eight upstream changed paths below are disjoint from all 128 owned
formatting changed paths (set intersection empty). No conflict resolution or
source adaptation was required.

```text
clients/ruby/lib/haveapi/cli/example_formatter.rb
clients/ruby/spec/cli_example_formatter_spec.rb
doc/client-examples.md
servers/ruby/lib/haveapi/client_examples/curl.rb
servers/ruby/lib/haveapi/client_examples/ruby_cli.rb
servers/ruby/spec/client_examples/assets/documentation_test.cjs
servers/ruby/spec/client_examples/shell_spec.rb
servers/ruby/spec/documentation/client_examples_spec.rb
```

Lead independently reconstructed the expected tree before receiving this new
head: a separate temporary GIT_INDEX_FILE read the old feature tree, applied the
binary old-base..new-master delta, and wrote a tree without touching the real
index/worktree. Expected and actual trees match `ed397888e12edcd0ec81fc0ac078e593f78ea0b0`. Exact receipt:
[rebase-tree-proof.json](rebase-tree-proof.json).

## Full range-diff

`git range-diff --no-color ae46cf27a9afb6558d386c293cec7231dd6c423d..d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038 c79645e0d43885c26cdc4129cbac96fdd5a13b07..7edb003dd5d5a058b3308510bb8a5f60387ad654`:

```text
 1:  5aa2de00 =  1:  173edf81 clients/js: normalize authored source with Prettier defaults
 2:  058e9315 =  2:  a7209152 clients/js: enforce shared Prettier defaults for authored source
 3:  26f578ce =  3:  3ac5ef63 ci: cover Ruby tooling inputs in RuboCop triggers
 4:  8bd66938 =  4:  e5769f47 clients/go: cover formatting failures and canonical output
 5:  05082918 =  5:  717d6272 clients/php: apply canonical source formatting
 6:  08e8716d =  6:  125c7723 clients/php: enforce style and PHP 8.0 syntax
 7:  31f2a081 =  7:  74679a6b clients/typescript: format generated clients with Prettier
 8:  5e871ab4 =  8:  8e482036 release: verify formatted TypeScript generator packages
 9:  86e32916 =  9:  108d8f0f clients: align formatting tools and contributor checks
10:  d6c2748a = 10:  7edb003d clients/rust: verify fixture formatting and failures
```

## Native hooks and command effects

Ordinary `git rebase --onto c79645e0d43885c26cdc4129cbac96fdd5a13b07 ae46cf27a9afb6558d386c293cec7231dd6c423d` replayed only the feature's
ten commits. Hooks/signature verification stayed enabled. Three native refusals
were handled without bypass: stale config signature before rebase (HEAD/index
unchanged); historical baseline config at first replayed commit; restoration of
reviewed shared-tooling config at commit nine. At each stop actual HEAD/index
were inspected and config/plugins compared byte-exact to their trusted owning
commit. Plugins were read, ordinary `overcommit --sign` updated signatures, and
ordinary retry or `git rebase --continue` completed. No source conflicts,
manual source resolutions, reset, clean, stash, disabled hooks or foreign
worktree operations occurred.

## Bounded quick verification on the new head

Prepared root Nix environment, `HAVEAPI_RELEASE_TOOLS_ONLY=1`:

- `make check-format`: pass. RuboCop inspected 427 files without offenses;
  Prettier, PHP-CS-Fixer dry-run, Ruff (41 formatted files), Cargo fmt all passed.
  PHP-CS-Fixer printed its existing root-composer metadata warning; exit 0,
  no files reported for changes.
- `make release-check`: metadata and prepared inputs both valid at 0.31.0.
- `make doc`: copied shared docs as required for focused server specs.
- `BUNDLE_GEMFILE="$PWD/clients/ruby/Gemfile" bundle exec rspec
  clients/ruby/spec/cli_example_formatter_spec.rb`: 3 examples, 0 failures,
  0.065 seconds. This pure entrypoint does not load the client server helper.
- `BUNDLE_GEMFILE="$PWD/servers/ruby/Gemfile" bundle exec rspec
  -Iservers/ruby/spec servers/ruby/spec/client_examples/shell_spec.rb`:
  13 examples, 0 failures, 0.933 seconds, seed 27212.
- `git diff --check`: passed. Final project index/worktree clean.

No full CI, full suite, long integration, installation or source fix was added.
The Nix shell substituted already-declared packages during entry; no package
pins or lockfiles changed.

## Migration and review implications

No migrations. No owned schema/migration files changed; manifest-format-1
compatibility and all accepted formatting behavior remain unchanged. All ten
owned patches are equivalent, and the only new final-tree content is the
four upstream CLI/shell-documentation fixes. The lead owns proportional review
of the changed baseline interaction and history. Unchanged mechanical lanes
need no full repeat; this receipt is evidence, not independent review approval.

## Retained refs and handoff

```text
refs/review/2026-10-29-client-formatting-audit/before-master-rebase d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038
refs/review/2026-10-29-client-formatting-audit/rebased-onto-c79645e0 7edb003dd5d5a058b3308510bb8a5f60387ad654
```

No refs deleted. No push, default-branch integration, deployment, publication or
session lifecycle action. Rebase/check commands completed with clean project
index/worktree. Exclusive team ownership is released to the lead after this
receipt; force-with-lease publication and CI remain the lead's next steps.
