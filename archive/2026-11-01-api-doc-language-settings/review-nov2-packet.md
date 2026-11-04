# Nov2 refinement review packet

Session: 2026-11-01-api-doc-language-settings, exact thread/workspace binding.
HaveAPI feature worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-01-api-doc-language-settings/haveapi.
Prior accepted/published/live head: 51047a211d71f817ab25f2def1692517f00c15c6.
Original base/default last proved: 391b0190241cf195a69b06f7297d3e4eebec5a83.
Final new head: ef4c0cdcb349815538bb93cedab9d3964c565998.
Final tree: c20bf6110013adad017ef989b9b305b099c2c6ca.
Source/index clean; no active writers/Git commands. Delta51047→ef4:9files,
120insertions/21deletions, mostly meaningful focused regression coverage.

## User request and accepted boundary

Hide the example type/detail selector when it has only one choice; keep the
native selected value valid and restore the control dynamically for multiple
choices. Move the Ruby authentication error-handling example's require before
begin/rescue. Put Switch user above Sign out in Settings. Architect brief is
[design.md](design.md):773 onward. Lead accepted moving require at its existing
shared wrapper boundary: thorough init/auth/action all load before begin, with
construction/setup still protected. Simple output remains unchanged. This is
the only intended exception to prior exact-old-English rendered program bytes;
English/Czech noncomment equivalence remains required at the new layout.

Implementation stays in the existing sidebar/JS, Ruby renderer and account
partial, with focused checks and one corrected UI-guide paragraph. Lead directly
applied final English wording using the required writing skill. No catalog,
locale/parser/storage/interface/dependency/budget/reference/migration change.
Do not expand the package into another subsystem or extra defensive mechanism.

## Review and provenance

Retain reviewer0's saved Sol/xhigh/read-only settings and existing independence.
All four affected lanes: general, architecture/repetition, scope/proportionality,
and bounded risk/compatibility confirmation for preserved account form/security
semantics. Overall branch retains prior high-risk locale/authorization review;
new delta is reversible presentation/example behavior without API or state change.
Reviewer reads each applicable reference under mandatory-change-review skill.

Retain prior independent reports review.md, review-followup.md and
review-final-refinements.md, including lead step9 acceptance of the two narrow
remediations to prior51047. Existing five accepted commits remain byte-identical.
Three new independent requests are separate focused commits rather than unrelated
source/layout/account changes in one commit. Inventory final complete series and
explicitly conclude history/consolidation and no migrations. No new dependency,
channel or generated-artifact update stream; no pins or temporary approach.
Earlier published/preview heads are retained in receipts and never described as
literally integrated into defaults. No merge or lifecycle approval exists.

## Acceptance and verification focus

Check server+JS hiding of the entire detail label for singleton choices,
singleton native hidden field (one successful example_detail scalar), query/locale
retention, two-to-one-to-two reappearance and preserved saved Thorough preference.
Existing per-group Simple fallback must remain. No changes to language/client
selectors or persistence beyond the exact detail-wrapper request.

Check the emitted Ruby require exactly once at top level before begin, including
Basic/token continuation/reuse and init/action thorough paths; constructor/setup
remain inside and existing rescue/comment paths retained. Simple and unsupported
OAuth output stay valid. Syntax and focused failing-require execution must prove
loading errors cannot enter application rescue handlers. Avoid final-source
regex rewriting or weakening the authored emission parity tests.

Menu order uses the same existing conditional forms and DOM keyboard order.
Confirm unchanged POST action, CSRF, switch_user=1 and capability/sign-in guards;
existing switch-user/logout security checks remain relevant.

Only committed quick-green deliverables are assigned for final review; no long
new integration checks before it. After review, run required exact-final broader
checks/CI with original-base allocation comparison and unchanged timing policy.
No automatic retries of inconclusive timing. Existing preview stays running;
owner2 has prepared bounded browser acceptance (session-local harness only).
Exact committed successor candidate and live refresh follow review/check release,
with recovery retained. No new OAuth service is added to the ordinary preview:
menu capability evidence uses existing real-app OAuth fixture rendering separately.

## Exact complete series and quick evidence

1. 661f571b91606ee33c3e6f4bdc7539fd518c48a4 runtime/UI/catalog (retained).
2. 0454207e0b31516dd71144d3e367da9b50f87a38 articles/layout/package (retained).
3. 69454b95a957b29d6108165aad27f4723958af76 receipt rule (retained).
4. c85b1d1817795edca13f77437feb9048ebc96d59 context/comments/adapters (retained).
5. 51047a211d71f817ab25f2def1692517f00c15c6 native forms (retained).
6. ab4ffe1837c976f6062895a354fa656f46445cd0 hide singleton detail controls.
7. 15a148629e2d1cb821d9fc43e035fdfb5e6fbd12 Ruby load before handlers.
8. ef4c0cdcb349815538bb93cedab9d3964c565998 account action order.

No history rewrite; firstfive commits byte-identical. No migrations or repeated
pin/generated update stream. Newthree separate requests are independently
reviewable; no obsolete approach/fixup commits to consolidate. Lead inspected
source scope and wholebranch diff--check. Independently assess this disposition.

[Quick receipt](three-refinements-verification.json),
[full delta](three-refinements-final.diff),
[complete quick log](three-refinements-final-quick.log).
Declared no-install root Nix shell, make doc preparation, committed bytes match:
166/0 detail+language_settings+example_selection+navigation+overview+OAuth+identity;
4/0 Ruby syntax/real-handler checks;3/0 authored-comment/layout/token parity;
all documentation assets pass, root RuboCop4/4, allthree required precommit and
commitmsg hooks pass with no bypass. Full commands in receipt. Existing baseline
51047 full1034+214/0 and all12CI retained for that exact head only; final new
long checks/CI not yet run. Owner2 browser harness syntax-ready, no product
execution/new service or live refresh on newhead yet.

Return read-only findings and explicit fullhistory/migration conclusion; keep
prior unaffected conclusions, inspect actual newdelta and relevant consumers.
No implementation, builds, nested agents, Git/source/preview/lifecycle mutation.
