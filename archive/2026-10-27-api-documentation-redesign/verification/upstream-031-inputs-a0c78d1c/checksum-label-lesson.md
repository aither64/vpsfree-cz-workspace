# Local PATH package checksum labels

The first 0.31 input refresh stopped after successful `bundle lock --local`
for the Ruby server. Its external graph comparison included the entire lock
suffix beginning at `GEM`, which also contains `CHECKSUMS`.

Bundler records local PATH packages there as version labels without SHA data.
Updating local HaveAPI packages from 0.30.0 to 0.31.0 necessarily changes those
labels as well as their PATH versions and internal constraints. This change
did not alter external dependencies, external checksums or platforms.

The corrected comparison derives ownership from the exact PATH package set,
requires unchanged ownership/remotes/dependencies except the expected local
version/constraint update, and verifies every owned checksum label is present
once at its expected predecessor/successor version. Only those label-only
lines are excluded from the external suffix comparison. All external GEM,
checksum, platform, dependency and Bundler records remain byte-exact.

Keep the initial logs, driver and full before/after locks. The accepted server
lock effect is retained; the corrected operation revalidates it and resumes at
availability/source identity without repeating successful local resolution.
