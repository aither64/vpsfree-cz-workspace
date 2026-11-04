# Rocky release package

Owner: implementer1. Phase: two image-specific commits and quick checks complete.
Exclusive Git/config writer authority is released to the lead; all commands
have completed and no Git mutation remains running or uncertain.

Session identity verified by `dev-session current` and matching
`DEV_SESSION_SLUG` / `DEV_SESSION_WORKSPACE`. The saved same-session roster
grants implementer1 `workspace_write`; both assigned files were writable.
Read the accepted `design.md`, applicable workspace procedures, repository
`AGENTS.md`, image documentation, and release-update skill before editing.

Changes in `worktrees/2026-11-03-redhat-image-releases/vpsadminos`:

- `image-scripts/images/rocky-9/build.sh`: release RPM suffix
  `9.8-1.1.el9` to `9.8-1.2.el9`.
- `image-scripts/images/rocky-10/build.sh`: release RPM suffix
  `10.2-1.1.el10` to `10.2-1.2.el10`.

The diff contains exactly these two `RELEASE` assignment changes. Point
versions and all other script content are preserved. Upstream version evidence
is the architect's successful discovery recorded in `design.md`.

Quick checks passed on 2026-11-03 (each exited 0):

- `bash -n image-scripts/images/rocky-9/build.sh`
- `bash -n image-scripts/images/rocky-10/build.sh`
- `git diff --check`

The lead transferred Git/config writer authority at
`a3c7c77459762d1a45f323de0f3f8dd5d8447323`, with an empty index and only the
two assigned Rocky changes unstaged. Each commit staged only its image file,
used a temporary message file with `git commit -F`, and ran under the prepared
`nix develop --command` environment. Installed executable pre-commit and
commit-msg hooks were verified. Overcommit listed the enabled hooks and
`overcommit.configuration.verifysignatures` remained `1`; no bypass was used.
Nixfmt and all commit-message hooks passed for both commits. Enabled RuboCop
has no applicable Ruby files in these changes.

| Image | Final commit |
| --- | --- |
| rocky-9 | `6ede3bd22b2ed28fb28a5a912f3a7daf7743fb6a` |
| rocky-10 | `3307df52ea5bf875e1d8a23318a64f569d8b3ebc` |

The complete branch range
`dd188397abe37d0bc33f4c5dfb3605206ce5e326..3307df52ea5bf875e1d8a23318a64f569d8b3ebc`
contains four focused image commits and exactly four `RELEASE` replacements,
one each for CentOS Stream 9/10 and Rocky 9/10. No obsolete approaches,
migrations, shared-code changes, or `osvm` / `test-runner` changes are present.
Rocky syntax checks were rerun successfully and the complete committed diff
passed `git diff --check`. Final worktree status is clean and the index empty.

No pushes, merges, long image tests, or deployment performed by implementer1.
The lead owns final review and watcher scheduling; both Rocky image integration
tests remain required after final committed-deliverable review.

No product documentation update is useful for these input-version replacements;
the existing release skill and accepted design document the operation.
No design deviation or application blocker found.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-redhat-image-releases/)
