# Image tests from a feature worktree

image-scripts/test@... enables host channel registration. The test runner
snapshots source in the store; a linked worktree has a .git file rather than
Git metadata directory. Raw OS evaluation cannot discover a revision there,
and channel.nix tries to interpolate its null default. This trigger exists
in the unchanged baseline version/channel/make-test/runner code.

For isolated verification of a clean, published feature commit, supply only its
actual host revision, revisionDirty=false and truthful version suffix through
VPSADMINOS_CONFIG. Template tests ordinarily select flake.tests, which fixes
configuration=null, so also use documented --test-config with an external file
returning {}. This routes mkTests through the ordinary configuration input while
preserving effective testConfig. Leave guest inputs, kernel config, assertions
and canonical image test unchanged. Prove the store source matches the clean
feature tree before claiming revisionDirty=false.

Choose an explicit short, uniquely owned --state-dir. The workspace worktree
path plus generated test subdirectory produced a173byte Unix socket path;
osvm allows at most108bytes. mktemp under /tmp provides a short unique root;
record its ownership and exact path. Never reuse/clean another session's state.

The metadata route built the canonical host image successfully, then exposed
the longsocketpath failure beforeVMboot. These were failed environment attempts,
not evidence of guest behavior or a default nooverride pass. See
work/2026-10-12-streamline-vpsadminos-config-imports/state.md, prepared command,
image-host-metadata.nix and image-attempt-{1,2}/ logs for exact source/commands.
