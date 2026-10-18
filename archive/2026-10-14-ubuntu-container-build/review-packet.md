# Final Ubuntu 26.10 branch review packet

## Outcome and scope

User requests Ubuntu 26.10 container image build script plus its image
repository config in vpsadminos. Accepted design: design.md; intent and current
state: plan.md and state.md in this directory. Exactly three files, 28 lines:
new image-scripts/images/ubuntu-26.10/{build.sh,config.sh} copied from 26.04
(changing only resolute to stonking), plus untagged 26.10 repository entry.
Preserve 26.04 latest/stable/lts and existing builder, console-getty helper,
package setup, test discovery and repository interfaces.

## Repository and complete branch inventory

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-ubuntu-container-build/vpsadminos
Branch: 2026-10-14-ubuntu-container-build
Target (not approved for integration): origin/staging, remote default.
Base: 0ffcc1da559c6d76e593e691e113d1e9349eebf1
Final head: 863e8e0d9f8a3e84814af236e437706d1ae27115
Complete base-to-head commit series (one logical release addition):
- 863e8e0d9f8a3e84814af236e437706d1ae27115 image-scripts: add Ubuntu 26.10
Full final diff: vpsadminos-final.diff (also inspect Git directly).
No superseded approaches, follow-up commits or unused compatibility paths.
No migrations, merged/released/deployed/externally used migration versions,
or migration lineage changes. No dependency/channel/input/generated update
streams. No lockfile changes. Source branch has not been published or deployed.
The implementation and repository entry form one useful release support unit.

## Evidence and quick checks

Implementer0 authored the scoped application edits, lead inspected and committed
with hooks in the declared Nix shell. Bash syntax for both new files, config cmp,
exact template diff, whitespace checks and Nix parse passed. Focused Nix eval
(with --impure for local-path import) confirms the new entry and unchanged
26.04 latest/stable/lts tags. Pre-commit Nixfmt and commit-msg hooks passed;
text-width hook warned for body lines >72 but all lines meet required <=80.
Worktree is clean. Upstream metadata confirms suite stonking and version 26.10
on both archive.ubuntu.com and cz.archive.ubuntu.com; see
upstream/ubuntu-stonking-metadata.txt.

Public listing from the default vpsadminos dev shell did not run: the shell
contains no osctl-image command and resolved the local directory. This is a
validation invocation issue, not product test failure. Targeted test discovery
and image build/boot tests are pending review and will use the repository's
prebuilt test runner through a fresh Luna/low watcher. No long tests launched.

## Compatibility, boundaries and documentation

Risk: high conservatively for a new container userspace's host/cgroup/kernel
compatibility. Lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Retained reviewer0: GPT-6.1 Sol/xhigh, read_only; independent
of authorship, no override or fallback. Perform the review yourself, no agents.

No API/client/CLI/protocol/module-schema/database/persistent format changes.
Existing tags/defaults preserved. No coordinated node rollout or production
publication/deployment authorized. A new image does not need to be published
to create the current 24.04 builder. Revert removes definitions; it does not
alter existing containers or delete a later-published artifact. No claim of
legacy cgroup support. Test compatibility with the tested current host.
Do not broaden into shared helper refactors, test matrix changes or tag
promotion without demonstrated need. No insecure bootstrap flags introduced.

Project documentation read: README.md, image-scripts/README.md,
docs/container-images/{creating,repositories}.md and image/repository specs.
No project prose change is useful because the existing workflow and interfaces
are unchanged. Design and verification evidence belong in session records.

## Review requirements

Read repository AGENTS.md and patch-series policy; workspace AGENTS.md and
applicable procedures; ~/.codex/skills/mandatory-change-review/SKILL.md and all
four selected references. Review complete series, final diff, neighboring code,
source provenance, security and compatibility. Explicitly conclude whether
obsolete branch history remains, state "no migrations", and assess absence of
repeated update streams. Report findings by Blocking/Important/Advisory with
paths/lines. Remain read-only, do not launch tests or mutate/publish files.
Report through session assignment to lead with a valid UUID message ID if needed.
