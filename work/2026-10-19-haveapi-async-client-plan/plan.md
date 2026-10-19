# 2026-10-19-haveapi-async-client-plan

## Goal

I'd like to add support for async in haveapi javascript client. should it be a separate package, or be included in the same package? currently the client is callback-based. suggest a solution and an implementation plan.

I'd also like to know what haveapi client is used in vpsadmin-webui, if any. would it benefit from async support in haveapi client in javascript?

## Affected repositories

- `haveapi`: JavaScript client package, callback contracts, initialization,
  authentication, action results, browser/Node distribution and verification.
- `vpsadmin-webui`: consumer dependency and API abstraction (investigation only).
- `vpsadmin`: inspect only if needed to establish WebUI integration context.

## Approach

Planning and investigation only; do not implement or publish client changes.
Compare a compatible Promise interface in the existing package with a separately
published client. Ground the recommendation in current source and actual WebUI
usage, distinguish JavaScript async/await from server background actions, and
define executable implementation packages and acceptance criteria.

Backlog (all packages depend on usable session team assignment):

| Owner | Expected result | Acceptance and checks | Dependencies |
| --- | --- | --- | --- |
| implementer0 | HaveAPI client evidence | Exact ref, files/lines, callback/auth/error/transport/build/test contracts | Assignment available |
| implementer1 | WebUI consumption evidence | Exact ref, dependency/import/adapter files, benefit and migration limits | Assignment available |
| architect0 | Recommendation and design.md | Alternatives, API shape, compatibility, packages, verification brief; integrates evidence | Both evidence reports |
| lead | Acceptance and handoff | Answer both user questions, maintain records and portal link | Design/report evidence |

## Decisions

- Retain existing Full-team roster/settings; architect owns substantive design.
- No code, migration, build, release, deployment, merge or lifecycle action is
  included in the requested planning work.
- Routine planning/investigation does not require automatic final review.

## Compatibility and deployment

Assess callback source and return-value compatibility, npm entry points, runtime
requirements, initialization/authentication/error behavior, response metadata,
and operation polling. Prefer incremental consumer adoption. Verify whether the
proposal changes wire contracts, persisted state, schemas, CLI/provider behavior,
Nix modules, or mixed-version behavior; document deployment/rollback implications
without executing a rollout.

## Documentation

Readers are the user and future client implementers. Keep proposed decisions,
evidence, implementation packages and verification brief in this session's
design.md; do not describe unimplemented behavior as a supported project feature.

## Testing plan

This turn checks source evidence and proposal consistency. The design will list
callback regression tests, Promise success/failure/initialization/authentication
tests, browser/Node packaging checks and a small WebUI adoption check as needed.
