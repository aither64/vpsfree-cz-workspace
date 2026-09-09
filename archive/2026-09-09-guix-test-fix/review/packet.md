# Guix runtime image fix review

Root: /home/aither/workspace/ai/vpsfree.cz
Initiative: work/2026-09-09-guix-test-fix
Repository: worktrees/2026-09-09-guix-test-fix/vpsfree-kb-contracts
Base: e5ed479f9d4058556dcf225b4c16afd5b9f0051a
Head: 81d6d7dfe530884aff3e1d2634e02e4b12fe28e8

The user requested a standalone fix and merge of the Guix runtime test while
leaving all password-reset changes unmerged and its independent cluster alone.
This feature starts at master, not the password-reset branch. No dependencies,
managed wiki pages, other suites, runtime framework or production code change.

The two fixture creation commands previously selected dated image 20260819.
It is absent from the live repository, which keeps four numeric Guix versions.
Latest currently resolves to 20260905. The suite promises to test current Guix.

One logical commit changes tests/suite/kb/guix.nix and its README description:
create the source container from latest, read/log its concrete version, reuse
that version for the deployment target, and assert the imported versions match.
Existing Guix retries and configuration/reconfigure/deploy assertions remain.
No old-image fallback. Both closures share a Ruby local containing the initial
image version so a later latest-tag change cannot select a different target.

This is low risk: disposable test fixture selection only, no public API, schema,
persisted production state, provider interface, deployment or compatibility
change. Required lanes are general and architecture at gpt-5.6-sol / xhigh.
The tests consume the existing pinned vpsAdminOS runner and osctl CLI. Neither
its source pin nor its API changes. Cached kernels must be used for later tests.

Quick checks passed before commit: full nix develop -c bin/check (all contract,
unit and 120 PNG checks); evaluated Guix test JSON and inspected generated Ruby;
pinned-shell ruby -c passes; git diff --check passes. No declared hook framework
or hook scripts in package.json. README edited directly with the writing skill.

Long validation is gated on this review: focused kb/guix#reconfigure in a
dedicated test VM, then full feature CI and master CI after fast-forward merge.
No long test or push has started. User authorized the merge after validation.

Read plan.md, state.md, local AGENTS.md, the committed diff, and relevant pinned
framework/CLI implementation as needed. Review directly without nested agents.
Do not edit project files, install tools, change Git refs, start tests, or touch
the password-reset worktrees/cluster. Write findings to the assigned review
artifact only. Report evidence-backed severity and location, or no findings
with concrete residual validation gaps.
