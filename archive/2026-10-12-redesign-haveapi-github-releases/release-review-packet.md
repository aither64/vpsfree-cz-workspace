# Final review: HaveAPI 0.29.10 automation-only release

Review the complete committed candidate, all four lanes, independently and
read-only under /home/aither/.codex/skills/mandatory-change-review/SKILL.md.
Read all four lane references, repository AGENTS.md and its release procedure.
No nested agents. Report findings first, with severity/commit/path references,
then explicit history/consolidation and migration conclusions and test limits.

## Request and exact range

The user requested a real patch release to exercise the accepted release process,
selected automation-only 0.29.10, then said "Implement the plan." Preserve all
0.29.9 runtime behavior; exclude Elixir and unrelated master changes. The user
will approve the protected release environment after the tag build succeeds.

Session: 2026-10-12-redesign-haveapi-github-releases. Worktree:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-12-redesign-haveapi-github-releases/haveapi-release.
Repository vpsfreecz/haveapi, feature branch 2026-10-19-haveapi-0.29.10,
target refs/heads/haveapi-0.29. Base v0.29.9:
784e113c216b16586c482e710ee4a0e0a04e6f8e.
Head b27a031fa03d8d985a3abd2679ce2fc14fe53602. Worktree clean.

All four new commits, in order:

1. 974e57b037c708ba376a94177b6866a576dacc44: one Nix pin update to the exact
   already verified master lock (e73de5be04e -> fe13242281a).
2. 41e37c29c5b7193844d4d3af4ddd4d08e7baa47b: release implementation with
   provenance to 82c9e77. The only patch difference is the two Nix installer pins
   updated to v31.11.2, SHA 448cde739abec1eaf0646249e3d25bb8d9bc7702.
3. c59483ed711100885131ca0dda364df56932b58a: release docs with provenance to
   c14e7d3, adapted to this branch's inline AGENTS instructions. The canonical
   release procedure matches master; no unrelated documentation refactor.
4. b27a031fa03d8d985a3abd2679ce2fc14fe53602: maintained-component versions,
   gem dependency constraints, example dependency and changelog for 0.29.10.

No obsolete approaches/fixups or repeated input-update stream remain. One pin
commit captures the final selected input; no weekly intermediate updates were
backported. No migrations exist; none were merged, released, deployed or consumed
as part of this range. No v0.29.10 tag/package has been published. The existing
0.29.9 runtime sources/tests are preserved, including fixes absent from master.

## Boundaries, contracts and documentation

High risk: registry credentials, version immutability, PHP mirror synchronization
and cross-registry partial publication. Select general, architecture/repetition,
scope/proportionality and risk/compatibility lanes. Reviewer0 remains the retained
gpt-6-astra/xhigh read-only member, thread 01a1309b-3a6c-7cd2-917f-4426d9b48c52;
no setting overrides or fallback. Independently assess these claims.

The previous master review is context, not a substitute for this backport review:
merge-review.md. Runtime API/protocols, package identities, persisted formats and
old/new consumer compatibility are unchanged. Public interfaces are existing
gem/npm/Composer packages, shared version, tag identity, release CLI/Make targets
and the retained artifact manifest. The owned helpers live in HaveAPI and are
consumed by its workflow; PHP publishes to the separate root-layout Composer
mirror. No consumer or downstream deployment pin update is part of this release.

Preserve the one human approval job, exact saved artifacts, PHP preflight before
registry writes, immutable destination checks and no-force atomic PHP push.
Network failures and concurrent mirror changes can still partially publish;
recovery resumes original artifacts. No cross-registry transaction is promised.
Real OIDC/deploy-key use and Packagist indexing await first publication.

Owning docs: doc/agent-instructions/releases.md, README and inline AGENTS release
instructions, plus CHANGELOG.md. Temporary preparation/results remain in session
release-0.29.10.md and state.md; accepted technical brief is in design.md.
No separate deployment/migration guide is needed for unchanged runtime behavior.

## Quick evidence and remaining checks

release-quick.sh exited 0 (release-quick.log/status). Metadata, 21 helper examples
normally and 21 under GITHUB_RUN_ID=123, whole Ruby lint, shell syntax, runtime
source preservation check, Git whitespace and actionlint passed. All four commits
passed installed hooks without bypass. Source/runtime proof script:
release-runtime-check.py. Full diff: release-final.diff. Backport range comparison:
release-backport.range-diff. Inspect the repository directly as well.

Official upstream release APIs were checked for every imported action on
2026-10-19. All existing version pins remain latest except Nix installer, advanced
to v31.11.2. Its release notes describe Nix 2.35.2 -> 2.35.3 security fixes:
https://github.com/cachix/install-nix-action/releases/tag/v31.11.2.
The SHA was independently read with SSH git ls-remote. Locked Nix packages are
the already checked master toolchain (Ruby 3.3.10, Node 24/npm 11.19.0, PHP 8.3,
Go 1.26.8). Retain this branch's Node/PHP server-shell packages.

Do not start long builds or publish. Full fresh component/package checks and
safe candidate Actions follow this gate. Source tag creation and environment
approval are later steps. Review the final history and migration lineage
explicitly, including no repeated-update streams and no migrations.
