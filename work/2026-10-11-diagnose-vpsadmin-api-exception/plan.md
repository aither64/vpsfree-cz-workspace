# 2026-10-11-diagnose-vpsadmin-api-exception

## Goal

Implement the accepted fix for the missing documentation in HaveAPI packages.
Prepare and verify the development-branch fix first, then stop for the user's
review. Only after that checkpoint, backport to HaveAPI 0.29 and release,
update vpsAdmin Ruby dependencies, and update the configuration's `vpsadmin`
channel. The user handles deployment. Preserve the original exception email
outside version control; retain sanitized findings as diagnosis evidence.

## Affected repositories

- HaveAPI: Ruby documentation route, generated documentation and gem release.
- vpsAdmin: consumer of the published HaveAPI 0.29.8 gem through its API package.
- vpsfree-cz-configuration: downstream `vpsadmin` service channel, in a later phase.
- HaveAPI PHP client mirror: synchronize shared release metadata under the
  normal release procedure; prepare its branch before separate master approval.
- Coordination workspace: plan, design, state and review/verification evidence.

## Approach

1. Follow [design.md](design.md) for the HaveAPI fix on a feature branch based on
   current `master`: mandatory release documentation, direct-build checks,
   narrow JSON-schema missing-file handling, regression specs and CI coverage.
2. Commit all intended changes and pass quick checks. Obtain independent final
   review of the complete branch, then run longer verification and publish the
   feature branch for user review. Stop at this checkpoint.
3. After user review and the required integration/publication approvals,
   backport using `cherry-pick -x`, prepare the next 0.29 patch release
   (currently 0.29.9), and verify the published artifact.
4. Update existing Ruby dependency constraints and affected Nix gemsets in
   vpsAdmin with current focused Rake tasks, add packaged API documentation
   smoke checks, and complete review/verification before approved integration.
5. Update only the configuration `vpsadmin` channel with confctl. Hand off exact
   revisions and deployment checks; do not deploy or dry-activate services.

## Decisions

- Lead owns design and implementation using retained Sol/xhigh settings.
- Independent review uses retained ready `reviewer0`, Astra/xhigh, read-only.
- Long or uncertain verification uses fresh Luna/low utility watchers resolved
  from the pinned catalog; no additional team members are acquired.
- User's delivery constraint: "you should first prepare the fix. after my review,
  you will backport it to haveapi 0.29 and release it. then you will update
  vpsadmin dependencies and update vpsadmin channel in vpsfree-cz-configuration.
  I will handle deployment myself."
- No version bumps, release publication, backport, downstream changes or default
  branch integration before the initial user-review checkpoint.
- Keep the session open for follow-up; do not archive or stop it.

## Compatibility and deployment

The proposed repair packages existing documentation and adds a narrow missing
file response to a documentation route. It needs no persisted-state, database,
API action, client, daemon protocol or generated NixOS option changes. A new
HaveAPI patch release would be consumed by a subsequent vpsAdmin dependency and
gemset update, followed by ordinary API deployment. Mixed API/node versions are
unaffected; API instances may be rolled independently. Rolling back the API
package restores the old documentation behavior without data conversion.

Publication follows user review and approval of concrete release artifacts.
Deployment belongs to the user. Avoid editing the immutable Nix store or
suppressing unrelated exception notifications. There are no migrations.

## Documentation

Readers are the operator receiving the alert and a developer fixing the release
process. Keep incident evidence and proposed checks in `findings.md` and current
status in `state.md`. Update HaveAPI's release/development guidance alongside
the implementation. Keep individual review and rollout evidence in the session.

## Testing plan

Run syntax/lint checks and focused specs before final review. After review, run
the full Ruby server suite, clean packaging and extracted-artifact endpoint
checks, and exact-head CI. Later verify the vpsAdmin service package and channel
lock. See the quick and longer check definitions in [design.md](design.md).

The user passed the first review checkpoint and authorized HaveAPI/master and
release on 2026-10-12. The later affirmative answer to the concrete three-master
integration request authorized PHP release, then vpsAdmin and configuration.
Those integrations and registry checks are complete. Full integration CI waiting
was explicitly waived in favor of the passing specs and packaged checks.
Deployment stays user-owned; see [delivery.md](delivery.md). npm automation is
deferred to a later task. Session and branches remain open and retained.
