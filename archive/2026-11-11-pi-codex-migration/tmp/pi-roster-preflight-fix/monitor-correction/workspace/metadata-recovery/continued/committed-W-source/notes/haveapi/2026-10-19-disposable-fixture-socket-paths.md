# Keep disposable MariaDB socket paths short

The Rust generated-client vpsAdmin fixture initially inherited a deep private
TMPDIR beneath the session artifact directory. VpsAdmin::TestDb::Instance places
its socket at state_dir/mysql.sock; the resulting path exceeded 107 bytes and
MariaDB aborted before schema bootstrap. The outer readiness loop reported a
timeout even though the child had closed stdout after the database startup wait.
No generated-client assertion ran in that attempt.

The fixture now allocates its database state in a uniquely created 0700 directory
under `/tmp`, retaining the same explicit TestDb::Instance and owned cleanup.
Diagnostic logs still belong in the session's private artifact directory. The
readiness helper reports closed stdout separately from a real deadline.
Quick tests cover the short socket path, uniqueness, permissions and EOF. Actual
server acceptance remains a separate gate; those quick checks do not boot a DB.

Avoid merely increasing the readiness deadline or pointing a fixture at an
existing database. A long temporary path is safe for logs but may be unsuitable
for Unix-domain sockets.

Session: [Rust client generator](../../work/2026-10-18-rust-client-generator/state.md).
