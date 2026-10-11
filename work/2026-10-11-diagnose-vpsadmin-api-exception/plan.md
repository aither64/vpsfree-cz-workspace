# 2026-10-11-diagnose-vpsadmin-api-exception

## Goal

Find the cause of the API exception reported in `api-exception-rb-sysopen.eml`
and recommend a fix. Preserve the original email outside version control and
record only relevant, sanitized evidence. Implementation, release publication
and deployment are outside this request.

## Affected repositories

- HaveAPI: Ruby documentation route, generated documentation and gem release.
- vpsAdmin: consumer of the published HaveAPI 0.29.8 gem through its API package.
- Coordination workspace: investigation records only; no feature worktrees.

## Approach

1. Extract the exception, relevant stack frame, method, path and user agent.
2. Inspect the exact installed Nix package and HaveAPI tag `v0.29.8`.
3. Compare the published RubyGems artifact with installed documentation.
4. Explain the packaging failure, why it sends email, and the smallest durable
   release and route changes that would prevent recurrence.

## Decisions

- Lead owns this investigation. The verified retained team is `lead_reviewed`.
- No application changes or production requests are necessary for diagnosis.
- Routine findings and evidence do not trigger independent final review.
- Keep the session open for follow-up; do not archive or stop it.

## Compatibility and deployment

The proposed repair packages existing documentation and adds a narrow missing
file response to a documentation route. It needs no persisted-state, database,
API action, client, daemon protocol or generated NixOS option changes. A new
HaveAPI patch release would be consumed by a subsequent vpsAdmin dependency and
gemset update, followed by ordinary API deployment. Mixed API/node versions are
unaffected; API instances may be rolled independently. Rolling back the API
package restores the old documentation behavior without data conversion.

Publication and deployment are proposals, not executed operations. Avoid editing
the immutable Nix store or suppressing unrelated exception notifications.

## Documentation

Readers are the operator receiving the alert and a developer fixing the release
process. Keep incident evidence and proposed checks in `findings.md` and current
status in `state.md`. No project documentation changes are needed for this
diagnosis-only request. A future implementation should update release guidance
alongside its automated packaging requirement.

## Testing plan

For this investigation, inspect installed files and the original published gem,
and match the email stack frame to tagged source. No long builds or integration
tests are needed. A future fix should check documentation in the built gem and
exercise documentation endpoints from the installed artifact, including the
missing-file case and absence of exception mail for that case.
