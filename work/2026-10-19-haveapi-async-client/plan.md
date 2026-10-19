# 2026-10-19-haveapi-async-client

## Goal

I'd like to add support for async in haveapi javascript client. should it be a separate package, or be included in the same package? currently the client is callback-based. suggest a solution and an implementation plan.

I'd also like to know what haveapi client is used in vpsadmin-webui, if any. would it benefit from async support in haveapi client in javascript?

## Affected repositories

- `haveapi`: inspect JavaScript package, asynchronous operations and compatibility.
- `vpsadmin` and potentially the separate `vpsadmin-webui`: inspect actual WebUI
  client dependency and identify whether JavaScript changes would reach it.
- This request authorizes investigation and a proposal; implementation is a
  subsequent step.

## Approach

Architect `architect0` owns source investigation and the proposed design in
`design.md`. The lead owns scope, evidence acceptance and tracking. Inspect
canonical repository refs without using other sessions' worktrees. Compare an
additive Promise API in the existing package with a separate package, preserving
the existing callback contract. Determine the actual WebUI dependency before
claiming a benefit.

## Decisions

- Retain the current team and saved member settings.
- Do not modify application code, publish branches, deploy or merge in this pass.
- Planning and investigation do not trigger mandatory final change review.

## Compatibility and deployment

The proposal must cover callback signatures, return values, initialization,
authentication, resource/action helpers, errors, Node/browser packaging and
minimum runtime support. Distinguish JavaScript Promise support from server-side
asynchronous API actions. Identify any protocol, persisted-state or deployment
implications and confirm whether mixed old/new clients can coexist. No rollout
is authorized by this planning request.

## Documentation

Readers: the user and future implementers. Findings and implementation boundaries
belong in this session's `design.md`; accepted public client behavior and examples
would go in the HaveAPI JavaScript documentation during implementation.

## Testing plan

This pass uses source and dependency inspection with exact revision evidence.
The design must specify callback regression coverage, Promise success/error
semantics, initialization/authentication, browser/Node entry points and async
action waiting. Do not run builds or integration tests merely for planning.
