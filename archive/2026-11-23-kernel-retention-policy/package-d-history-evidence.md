# D: final retirement history

The published but unmerged single-commit implementation at
`380c5f30180f816fa70135eb5ff078bb3bbb0c61` and its per-kernel follow-up
`3c05dce7b37d85ed2911d65b633914a32e06fe42` are represented locally by one commit,
`a435f844d017da0b418a470f20fc695c6c0eadd0`, with subject
`os: automate guarded kernel retirement on staging`. Its sole parent is C,
`be966218cb3bcafe05592a5ad32fcf53dffb6b16`. A, B and C are unchanged.

Old range: `be966218cb3bcafe05592a5ad32fcf53dffb6b16..3c05dce7b37d85ed2911d65b633914a32e06fe42`.
New range: `be966218cb3bcafe05592a5ad32fcf53dffb6b16..a435f844d017da0b418a470f20fc695c6c0eadd0`.
Both tips have the exact tree `610546fe7b01817702a4223f19fde703e028191a`;
`git diff --exit-code` across the tips passed. No migrations or behavior change.

Built the replacement in a disposable standalone checkout of C, using the old
tip's exact staged tree and copies of the repository's normal Overcommit
launchers. The pre-commit catalog check and commit-message hooks passed, as did
the exact new-tree catalog check and base-to-head whitespace check. Imported
only the new objects and used `git update-ref` with the old head as the expected
value. The shared index, config and hook checksums were unchanged; every other
ref was unchanged and the project worktree stayed clean. Discarded the
standalone checkout. No remote operations.

Prior evidence remains SHA-specific. On `380c5f301` the workspace record notes
successful RSpec/RuboCop, failed docs dependency setup, inconclusive VM prebuild,
and ten successful livepatch rows with final aggregation setup failure. See
[state](state.md) and the earlier [review](review.md); these are not checks on
the replacement. The per-kernel quick checks passed on `3c05dce7` before the
identical-tree history edit. The offline gate is rebound to the new commit and
its unchanged tree. Its script checksum is
`d14c002ce2e267f4058ad96ee120bca20db6e25cd76e242b47a94e9cdaaa2446`;
syntax and ShellCheck passed, but the full monitored gate has not been run on
the replacement.
