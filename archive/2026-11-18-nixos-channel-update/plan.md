# NixOS stable channel update

## Goal and authorization

Update `nixos-stable` in `vpsfree-cz-configuration` and
`vpsadminos-org-configuration` with a one-time pin to a `release-26.05` revision, preserving normal
`nixos-26.05` tracking and including the fix from
https://github.com/NixOS/nixpkgs/pull/589970. The initiating user explicitly
requested “Then merge it and tell me which systems need to be deployed”.
This authorizes integration into both repositories’ configured default branches.
Deployment itself is outside this request.

## User correction

The user explicitly clarified: “i did NOT ask you to change the branch, I asked
you for a one-time update to release-26.05 to get this fix sooner.” Preserve
`flake.nix` and lock original refs at `nixos-26.05`; change only the generated
locked revision/hash metadata. Superseded branch-switch work must be consolidated
out of final unmerged history. No integration had occurred at correction.

## Approach

Architect confirms PR inclusion, current channel/input mappings and compatibility,
then writes [design.md](design.md). Each repository has its own implementer,
worktree and commit window. Use confctl channel commands for generated lock updates;
keep changes restricted to the requested channel. Preserve hooks. Publish feature
branches, verify complete history, review as applicable, and fast-forward merge
under separate short repository claims. Report evaluated nginx consumers.

## Compatibility and deployment

Determine whether current pins already use the same release; assess package/module
changes before integration. No schema or application protocol change is intended.
Keep rollback to prior configuration generation available; no machine activation
is authorized. Distinguish systems using the affected nginx package from other
systems sharing this channel.

## Documentation and checks

Operators need the exact merged heads and deploy list, recorded in session state
and linked evidence. A mechanical pin update does not need new reusable project
docs. Quick checks cover generated input scope, fix inclusion and evaluated nginx
package provenance. Architect selects bounded additional checks from local guidance.
Independent whole-branch history conclusions remain required even when generated
content is exempt from substantive review. No fleet build or deployment by default.

## Forward-only follow-up design

User requested a clean solution for expected behind-channel updates to succeed
as no-update and explicitly permits locating the fix in confctl. Current scope
is a concrete solution proposal, not source implementation or additional merges.
Architect owns bounded analysis of confctl update granularity, shared input graph,
error semantics and compatibility. Prefer confctl-owned behavior over workflow
exit suppression; preserve independent forward updates and graph integrity.

## Authorized confctl implementation

User accepted D4: “acceptable. design it first and then implement it.” Formal D5
architect-owned brief precedes source edits. Add confctl as affected repository;
one complete implementation package C, implementer0. Preserve strict validator,
set and unguarded-update behavior; correct guarded UPDATE behind/equal semantics,
independent forward progress and atomic complete-graph integrity. Include focused
RSpec, CLI reporting and maintained docs/man compatibility wording. No version
release or configuration pin update assigned. Earlier merge approval names only
the two configuration repositories; confctl default integration is not yet approved.
Publish/check/review confctl feature branch and present concrete result before
seeking any additional integration approval. No deployment/workflow execution.

## Authorized confctl adoption

After confctl merge and next step naming both configuration pin updates, user
replied “yup, continue”. Proceed with generated confctl pin update in both
configuration repositories and integrate into their named master targets, as
continued configuration work with original integration direction. No deployment,
version release or workflow text change. Preserve nginx locked4077fb98 and normal
nixos-26.05 tracking, all other inputs, and already-merged history. Architect D6
settles routine mapping/command/check brief; implementer0 owns A2 and implementer1
B2, each existing worktree/feature branch brought forward without rewriting merged
history. Published confctl target d8ab7d4 only; check any upstream scope drift.
