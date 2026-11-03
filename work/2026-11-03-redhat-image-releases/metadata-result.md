# Source-identity package result

Committed by implementer0 as `1a637e9eac4311adba2b08d60dfa7a17d07bcb52`
(`test-runner: preserve captured source identity`). Tree:
`49b8a7879e6b363349ae70808c4cdecc996e578e`.
Parent is channel commit `52fba5ee5aac2e171375a780d3860a86e71e5d65`.
All four image commits and that channel commit are preserved unchanged. The
worktree and index are clean. No push, merge, VM/image test or CI action was run.

## Delivered behavior

- Existing path snapshot selection and GC-root lifetime are unchanged.
  RepositorySource captures a matching original Git root/commit before resolution,
  then compares the immutable snapshot through a private temporary index.
  Included ignored/untracked content affects dirty state; the caller index is
  unchanged. Unknown or enclosing-parent identity is not presented as clean Git.
- One `source_info` record is scoped through `TEST_RUNNER_SOURCE_INFO` and the
  previous environment is restored on success or exception. Metadata remains
  bound to the snapshot even when live HEAD/files move.
- `os/lib/source-version.nix` shares the previous flake revision/dirty/suffix
  defaults between ordinary OS construction and test OS construction.
  Matching snapshot metadata is accepted only for the provider's own source;
  an external caller cannot relabel a pinned vpsAdminOS provider. Explicit
  overrides, packaged fallback, optional legacy framework behavior and existing
  nixpkgs identity rules remain supported. Native direct evaluation forwards
  the full available framework.
- Focused regressions and the existing framework integration documentation were
  updated. No schema/migration, configuration pin, channel assertion or workflow
  changes. No design deviation or new identity registry/harness.

## Focused verification

Ruby check passed: 42 examples, 0 failures, approximately 36 seconds:

```sh
nix develop .#test-runner --command env \
  RUBYLIB=/nix/store/givmi31xrbr231gxnry1xc2ggb5s4imf-libosctl-native-local/lib \
  bundle exec rspec -I test-runner/spec \
  test-runner/spec/test_runner/repository_source_spec.rb \
  test-runner/spec/test_runner/cli/command_spec.rb \
  test-runner/spec/test_runner/prebuild_nix_spec.rb
```

The existing native extension uses Ruby 3.4.11 and unchanged libosctl sources.
Set RUBYLIB **after** `nix develop --command`; the shell replaces an outer value.
The same environment can prefix the required local-code image-test command.
Log: `/tmp/redhat-source-identity-checks-ready.log`, SHA-256
`2bab76f72c4f603fd17054eaf4e9e84db67350c7809f5d6fbd66d926c6ab16fa`.
That batch's later Nix fixture failed because it attempted a read-only toplevel
assignment; the fixture was corrected to inspect existing derivation passthru.
The Ruby sources did not change after their passing run.

Both corrected Nix evaluations passed, without building a system or kernel:

```sh
nix eval --impure --raw --file tests/source-version-eval.nix
nix eval --impure --raw --file tests/channel-revision-eval.nix
```

Times were 17 and 32 seconds. The first covers shared version rules, matching
and different providers, normal/dirty native metadata, unknown/packaged fallback,
explicit overrides and the real test constructor with and without the optional
module. The second preserves the channel owner's known/null regression.
Log: `/tmp/redhat-source-identity-nix-checks.log`; statuses:
`/tmp/redhat-source-identity-nix-checks.exit` (both 0). Log SHA-256:
`216e5cbe53cd7fcbefc9da504bdf7769a3d3364acd5b1a126d7e6529c3f187ed`.

RuboCop inspected all five affected Ruby files with no offenses. Nixfmt,
`git diff --check`, `overcommit --diff HEAD` and final commit pre-commit and
commit-msg hooks passed without final warnings. Only message wrapping changed
between the initial source commit and its final amended head. All checks used
fresh Luna/low utilities where duration was uncertain; no operation remains.

## CI path and handoff

The existing `./test-runner.sh` builds `$ROOT#test-runner` on every invocation
(lines 13-19). `flake.nix:431` imports the local runner package;
`test-runner/nix/package.nix:14` sets `testRunnerSrc = ../.`. Its wrapper loads
that source's `lib` and executes that source's `bin/test-runner` (lines 37-44).
CI therefore receives the updated RepositorySource and command code, without
an old packaged runner gem or a workflow/package update prerequisite.

The lead owns final committed full-branch review, four local-code image tests,
publication and approved integration. The original failed image logs remain
unchanged. Git/config writer authority and the shared utility slot are released
to the lead; no tracking commit made.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)

## Final review remediation

The reviewed metadata head was `58aae8d54887a14f59fada178a833b33a6ebfa81`.
After the final report, the lead authorized both narrow corrections and folding
them into the original owner. The replacement is
`1a637e9eac4311adba2b08d60dfa7a17d07bcb52`, with the same parent
`52fba5ee5aac2e171375a780d3860a86e71e5d65`; no repair commit was added.
The old head remains at local backup branch
`2026-11-03-redhat-image-releases-reviewed-metadata`.

Only `os/modules/misc/version.nix` and `tests/source-version-eval.nix` differ
between those heads (125 insertions, 3 deletions). Exact diff:
[metadata-review-fix.patch](metadata-review-fix.patch), SHA-256
`41e5e7e4c8316eab34a08b68cc06df2b6e1ebcddcc9404398a2fd979ce3c8789`.
There are no migrations or new compatibility boundaries.

The legacy automatic Git revision/suffix definitions now use priority 1100,
below known-source mkDefault 1000 and explicit consumer 100, above option
fallbacks 1500. Security evidence uses the selected revision when its actual
Nix option priority identifies a source/consumer definition. Only the legacy
automatic directory fallback expands the seven-character display revision to
its full Git commit, preserving that existing behavior.

The regression merges the real version option declarations and definitions
with the shared module at an ordinary `.git` directory boundary. Capture A and
simulated directory HEAD B differ: revision, suffix and evidence retain A.
It also checks native provider identity, explicit full/short/null overrides,
legacy absence/unknown fallback and full legacy evidence. The original mocked
matrix and linked-worktree coverage remain.

Before correction, the added real-module regression reproduced the full-SHA
versus seven-character merge conflict (exit 1, about 15 seconds):
`/tmp/redhat-source-priority-red.log`, SHA-256
`29e82b2970b1367c5fc275613f3a9e013602c260f9260f838f5b6d83df35af19`.
After both corrections, the source-version and channel evaluations both passed
(exit 0, 41 seconds total). Log:
`/tmp/redhat-source-priority-evidence-checks.log`, SHA-256
`0cdbb8d462199a7841bd544b83972487c68a813162bf3ccb625725bbc57e03c0`;
statuses: `/tmp/redhat-source-priority-evidence-checks.exit`.
The 42-example Ruby evidence remains applicable because these corrections
change no Ruby source or input. Final amend hooks (Nixfmt, RuboCop and message
checks) and committed whitespace checks passed without warnings.

Final worktree/index are clean; original four image commits and independent
channel commit are retained. No long image/system/kernel build, push or merge
was run. All utilities/commands have finished. Git/config writer and the
utility slot are released to the lead for narrow-fix acceptance and long tests.
