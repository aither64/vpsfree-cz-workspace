# Review routing and explicit merge approval

## Goal and scope

Make mandatory change review use an eligible persistent session reviewer when one
exists, and require the user's explicit approval before feature content enters
any repository's default branch. The affected repositories are this coordination
workspace and `vpsfree-dev-workspace` (the site-specific review/handoff skills).
No generic runtime, portal, or GitHub branch-protection change is planned.

## Design

- Select the lowest-index eligible retained `reviewerN` for a coherent change.
  Eligibility requires a ready, independent reviewer with no unrelated active
  assignment. Use that member's saved model and reasoning effort unchanged and
  retain it for follow-ups. If none is eligible, use a fresh standalone reviewer
  from the installed catalog's default development reviewer policy; do not add
  it to the roster or permit self-review. Record identity, settings, lanes,
  findings, and any fallback reason.
- Review is still required for solo sessions. The fallback review does not
  invent a team or change the session's lead settings. The mandatory adaptive
  lanes and existing finding disposition rules remain in force.
- Before merging or pushing feature content to a default branch (including a
  direct push or PR merge), require explicit user direction identifying the
  repository/target set. Up-front merge direction qualifies; plan acceptance,
  "Implement the plan", review, CI, or deployment do not. Tracking-only
  coordination commits on shared workspace master remain allowed.
- Approval covers the named repository/target set, not a frozen SHA. A clean,
  patch-equivalent rebase may retain approval after comparison and revalidation.
  A material patch, scope, repository, or target change requires renewed
  approval. Record approval provenance and final integrated heads in state.
  While awaiting approval, leave the initiative active and feature branches
  unmerged; completion criteria must not be read as permission to merge.

## Compatibility and deployment

This changes agent procedure only. It introduces no persisted format, database,
API, CLI, protocol, NixOS option, or runtime schema change. Existing sessions
can use the policy without migration. Old and new installed skill generations
may differ until the workspace user-profile package is switched; the root
workspace rules remain authoritative for integration. No fleet update or
rollback-sensitive state is involved. Pin the extension revision in this
workspace feature branch; deploy the user-profile package from the branch if
verification permits. Do not merge either branch without a later explicit
user direction.

## Verification and review

Add focused policy regression checks for routing and merge-approval wording,
run quick repository tests, then the mandatory independent review. After
findings are resolved, run the relevant Nix package checks using a fresh
Luna/low monitor for long operations. Push feature branches for CI, inspect
results, and record any unverified deployment limitations. Keep the portal
manifest and state current for handoff.
