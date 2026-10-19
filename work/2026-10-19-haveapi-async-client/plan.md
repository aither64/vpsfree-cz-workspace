# 2026-10-19-haveapi-async-client

## Goal

I'd like to add support for async in haveapi javascript client. should it be a separate package, or be included in the same package? currently the client is callback-based. suggest a solution and an implementation plan.

I'd also like to know what haveapi client is used in vpsadmin-webui, if any. would it benefit from async support in haveapi client in javascript?

## Affected repositories

- `haveapi`: inspect JavaScript package, asynchronous operations and compatibility.
- The separate React `vpsadmin-webui`: inspect its actual client dependencies
  and design a supported adoption path. Legacy WebUI and console integration
  are explicitly out of scope per user direction.
  `repos/vpsadmin-webui.git` exists despite its omission from the project map;
  inspect its retained refs read-only and state their freshness limitations.
- User explicitly authorized implementation with "Implement the plan" after
  accepting TS authoring for both clients and backward compatibility as a gate.

## Approach

Architect `architect0` owns source investigation and the proposed design in
`design.md`. The lead owns scope, evidence acceptance and tracking. Inspect
canonical repository refs without using other sessions' worktrees. Compare an
separate Promise-based client object in the existing package with a separate
package, preserving the existing callback client. Focus consumers on the new
React WebUI.

## Decisions

- Retain the current team and saved member settings.
- Implement on session-owned feature branches, publish those branches after
  verification. No release, deployment or default-branch integration is authorized.
- Planning and investigation do not trigger mandatory final change review.
- Revised recommendation following user feedback: keep one `haveapi-client` npm
  package and export a separate `AsyncClient` object/class. Give its methods
  ordinary names (`setup`, `authenticate`, `request`, resource action names),
  all Promise-based for remote operations. Preserve existing `Client` callback
  and callback-free calls. This supersedes repeated `Async` method suffixes.
- User runtime direction: support up-to-date browsers, not EOL ones. Preserve
  existing Node entry points; do not expand scope into a separate runtime rewrite.
- Use a fixed `{ value, response }` result for Promise action invocations so
  dynamic API members named `then` cannot be invoked by Promise assimilation.
  Resolve initialization/authentication without returning the dynamic client.
- Promise invocation settles on the API reply. Server-side queued work requires
  a separate completion contract; a successful receipt does not prove completion.
- The React `vpsadmin-webui` already owns a Promise-based TypeScript fetch client
  and has no npm HaveAPI dependency. User explicitly wants it to be able to use
  the new client if possible. Future adoption is a design goal: include types,
  cancellation, metadata/envelope/error access and header/token extensibility;
  preserve WebUI-owned OAuth recovery and non-replayed writes. Plan a bounded
  integration trial before a broad client migration.
- Legacy PHP WebUI and console integration are excluded from this initiative;
  prior source findings are historical context only.
- User selected TypeScript authoring for BOTH the new AsyncClient and existing
  callback-based Client (called "sync client" in the request). Compile both to
  ordinary JavaScript and generate declarations in the same npm package;
  script-tag/CommonJS consumers need not install TypeScript. Preserve Client's
  callback signatures, overloads, return values, hook order, local synchronous
  throws and fire-and-forget semantics. Migrate its implementation in reviewable
  stages without mixing unrelated behavior fixes. Share a typed protocol core
  under independently owned callback and Promise client/resource surfaces.
  Dynamic endpoint schemas require explicit types/generation independently of
  the source language. Update source/build guidelines deliberately for the TS
  migration; modern browsers remain the target.

## Compatibility and deployment

The proposal must cover callback signatures, return values, initialization,
authentication, resource/action helpers, errors, Node/browser packaging and
minimum runtime support. Distinguish JavaScript Promise support from server-side
asynchronous API actions. Identify any protocol, persisted-state or deployment
implications and confirm whether mixed old/new clients can coexist. No rollout
is authorized by this planning request.

## Accepted execution defaults

- Both clients and production helpers use TypeScript. Existing Client remains
  callback-compatible, including return values, synchronous local exceptions,
  callback arguments/hooks, callable objects and fire-and-forget behavior.
- Keep gulp as build entry; compile using tsc (ES5 output, ESNext modules,
  declaration emit), bundle with Rollup to unchanged dist/haveapi-client.js.
  Preserve browser global HaveAPI, AMD and CommonJS named exports; no default
  wrapper, new engines restriction, or eager async primitive use by Client.
- Initial packages: implementer0 hook/env/build/type scaffold and core/auth;
  implementer1 original-bundle compatibility fixtures and actions/resources.
  Architect owns final interface brief. Serialize build/export/index/commits.
- Callback parity precedes typed shared-core extraction and async execution
  packages. New async resources/save/explicit association loading use Promises.
- Run committed-deliverable final independent review after quick checks, before
  long server/browser integration. Watchers run uncertain-duration verification.
- Report specific unavoidable compatibility changes or disproportionate
  preservation costs to the user before changing the compatibility contract.

## Documentation

Readers: the user and future implementers. Findings and implementation boundaries
belong in this session's `design.md`; accepted public client behavior and examples
would go in the HaveAPI JavaScript documentation during implementation.

## Testing plan

This pass uses source and dependency inspection with exact revision evidence.
The design must specify callback regression coverage, Promise success/error
semantics, initialization/authentication, browser/Node entry points and async
action waiting. Do not run builds or integration tests merely for planning.
