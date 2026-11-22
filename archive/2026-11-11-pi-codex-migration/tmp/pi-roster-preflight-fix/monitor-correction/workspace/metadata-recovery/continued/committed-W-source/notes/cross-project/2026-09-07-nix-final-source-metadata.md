# Compare Nix source identity without the metadata-only final marker

Initiative: `work/2026-09-05-cgroup-v1-shared-device-fix`.

Comparing the entire `locked` object from `nix flake metadata --json` against
the generated `flake.lock` node failed despite matching source identity. The
metadata output included `__final: true`, which the lockfile did not contain.

After explicitly verifying and excluding that metadata-only marker, every
source field matched: type, owner, repository, revision, NAR hash, and timestamp.
The production pin also changed only its intended input node. Do not treat a
raw object comparison failure as a revision mismatch before inspecting fields.
