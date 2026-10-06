# Upstream-reference follow-up review

Verified initiative: 2026-10-02-codex-package-portal-settings in
/home/aither/workspace/ai/vpsfree.cz. Plan/state/design and prior final review
records are in this tracking directory. Review under mandatory-change-review.

User requested upstream issue/PR links in comments or commit messages and a
clear signal for removing the packaging workaround. Subsequently authorized
merging all four registered branches into their default master branches when
done, explicitly without waiting for CI. No new runtime/pin/deployment change,
source patch, automated removal, session closure or history rewrite is intended.

## Committed scope and complete inventory

Worktrees: worktrees/2026-10-02-codex-package-portal-settings/<project>.

- Generic: base869b8d4728394127ba949dc76724dce56eae136b;
  final head4bec20165387d567b761e43b11fdeabb096618d7.
  Complete series:
  22377c4417448c9f9fda2e8173d4762ce2c7b6b6 portal controls;
  4d527ae5b0d26b8eede7f6c256e5bd1686bdda6f Codex0.160 pin;
  40838aa28c8433e42a4a3fbed4586a3df0146de9 shared assembly/tests/docs;
  4bec20165387d567b761e43b11fdeabb096618d7 upstream/removal references.
- Extension: base074926d33f7306288f7cfad87c6a85e8a430e750;
  unchanged final headc56f981a950ab763b71dc91c59e8b5256d478851.
- Configuration: base2758415cc11d719f22b341cee4e8e77c773c141f;
  unchanged final head028d70b233c5b100fea7f7aa0b945fb8b6d3ec4d.
- Workspace: feature base98389138caef0576dfa7a101d1dbcdbae943b0af;
  unchanged final headc5d8bed5fcd3bc01ce18831ea680aac7edfd68ee.
  Remote base29dcc1ddfb88cbcdec06b821a77af53d9c282b86; reviewed tracking-only
  ancestors52fa4313/98389138 remain intentional. Shared master is still983.

Prior complete cross-project series/diff and cleaned history are in
final-review.md; your prior four-lane report610c839c-3a43-4054-9ed2-cc71b9482e9d
is reconciled in final-review-result.md. No other source head has changed.
The follow-up is a separate documentation-purpose commit because generic408
was already published, pinned by both consumers and deployed. Do not fold or
rewrite this externally consumed commit. Original unpublished obsolete versions
were removed before publication. No migrations in any branch, and no new
compatibility or persisted-state paths. Assess whole-branch history explicitly.

## Documentation and checks

New committed diff408..4bec changes only nix/codex-package.nix (top-level Nix
comment, outside generated shell strings) and docs/codex-package.md. The commit
body also links all three upstream references. Main context completed the
required writing pass. Existing README links to the package-contract page.
Provider owns lib.mkCodexPackage; workspace and aitherdev/system codex-ds are
known consumers. Consumer locks intentionally retain generic408: runtime
behavior did not change and this is not a documentation-only pin cascade.

Acceptance: references to llm-agents issue9887/PR9889 and Codex issue48050;
clear downstream-workaround label; selected upstream output must itself supply
a complete daemon-copyable package/materialized helpers; migrate both consumers
before removing assembly, preserve dependency roots and regression coverage.
An issue closure or version bump alone must not justify removal. No claim that
PR10132's direct-store lifecycle patch was adopted or that an upstream version
is guaranteed to contain a fix.

Quick checks passed: committed diff whitespace; Nix parse; all commit-message
lines <=80. Parsed helper before/after is exactly identical (SHA256
a0814fa30db39602922efb3ea7438fb467bc8a78d0d71cb7be5572534dedd51e).
All three links were reopened against upstream immediately before this edit.
Original full integration/browser/protocol/state/daemon/deployment gates remain
passed on the deployed sources, documented separately in rollout.md/state.md.
No long tests or CI waits are requested for this comment-only change.

## Requested independent review

Overall follow-up risk low: localized comments/docs, no executable, public
interface, security, state, dependency or deployment change. General lane only;
prior architecture/scope/risk conclusions remain unchanged. Use your retained
reviewer0 gpt-6.1-sol/xhigh/read_only settings, with no nested agents or edits.
Read the mandatory review skill and general-review reference, applicable
workspace/repository guidance and the committed diff/complete branch history.
Verify references, claims, removal criteria, runtime equivalence and commit
split independently. Explicitly conclude on obsolete history and no-migrations
lineage. Report findings/severity and actual reviewed head/settings via
report_to_lead; do not push, merge or wait for CI.
