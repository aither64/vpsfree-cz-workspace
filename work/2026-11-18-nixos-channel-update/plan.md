# NixOS stable channel update

## Goal and authorization

Update `nixos-stable` in `vpsfree-cz-configuration` and
`vpsadminos-org-configuration` to `release-26.05`, including the fix from
https://github.com/NixOS/nixpkgs/pull/589970. The initiating user explicitly
requested “Then merge it and tell me which systems need to be deployed”.
This authorizes integration into both repositories’ configured default branches.
Deployment itself is outside this request.

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
