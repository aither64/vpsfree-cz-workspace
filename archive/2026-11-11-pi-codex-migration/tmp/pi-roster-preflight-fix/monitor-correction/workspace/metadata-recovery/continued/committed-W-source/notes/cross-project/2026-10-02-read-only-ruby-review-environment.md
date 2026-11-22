# Read-only Ruby review with a prepared Nix closure

Session: `work/2026-10-02-abuse-emails/`.

A read-only reviewer could not source the lead's exported `nix print-dev-env`
script: it ran shellHook, which attempted temporary-file and Bundler writes.
The prepared closure itself was available; this was a shell setup permission
issue rather than missing dependencies.

For bounded read-only reproductions, the reviewer reused the exact pinned Ruby
and the already-prepared GEM_HOME, GEM_PATH and BUNDLE_PATH values, with
BUNDLE_FROZEN=true, without running shellHook or bootstrapping. This successfully
reproduced parser defects without source edits or stored incident records.
Do not substitute ambient Ruby or install dependencies from a read-only review.
Keep the exported environment private and resolve the required paths from that
exact session's prepared closure.

A writable implementation member can source the same prepared script normally;
its shellHook is already invoked by the script and should not be evaluated a
second time. See the companion restricted-member Nix environment note for the
original cache-access workaround.

A separate writable verification wrapper used `set -u`, and the same exported
shellHook failed on `export PS1="(confctl) $PS1"` in its noninteractive shell.
Initializing `PS1=''` before sourcing preserves strict mode and satisfies that
existing hook expectation. A strict-shell source plus bundle-check smoke test
passed after this wrapper correction; no repository code change was needed.

Source the writable export from the configuration repository root containing
Gemfile. Sourcing it from the session tracking directory failed with
`mkConfigDevShell mode 'tools' requires ./Gemfile` before integration began.
The export executes a working-directory-sensitive shellHook; running from the
configuration root with PS1 initialized succeeded and the full suite passed.
