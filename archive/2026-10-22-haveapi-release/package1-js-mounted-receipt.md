# Package 1: JavaScript mounted URL correction

Owner: implementer1. Design:
[api-doc-mounted-url-contract.md](api-doc-mounted-url-contract.md), linked from
`design.md`. Lead granted execution, accepted final bounded source/quick results,
and completed the three-document main prose pass. Implementer0 exclusively owns
index/hooks/commits/history. This file is evidence, not application source.

## Implemented contract

The shared strict descriptor resolver joins to the origin root. Callback action,
token and state sends already use that resolver. Internal async RequestContext
adds optional `pathMode: 'api' | 'descriptor'`, defaulting to `api`; only published
resource/state contexts and token-description sends select `descriptor`.
Discovery, public raw requests, public RequestSpec and OAuth URL behavior remain
unchanged. No server/fixture route rewrite, prefix guess, fallback or retry.
Base userinfo rejection remains enforced when descriptor joining uses the origin.

Only one inconsistent old synthetic callback test descriptor changed from
`/v1/users/{user_id}` to actual mounted `/api/v1/users/{user_id}`; its expected
wire URL and other cases remain intact. New tests use actual Rack descriptors
and replies for mounted callback/async token challenges and nested actions.
The callback test goes through real discovery JSON parsing inside the bundle's
VM. Its first pure-test attempt used `useDescription` with host-realm arrays,
which failed the existing callback array-validator realm check before dispatch;
that was corrected at the test boundary, without runtime or schema changes.

## Exact commit path groups

Authored source/tests/docs (nine paths):

```text
clients/js/src/haveapi/protocol.ts
clients/js/src/haveapi/async/request.ts
clients/js/src/haveapi/async/client.ts
clients/js/test/compatibility/mounted_paths.spec.cjs
clients/js/test/path_construction.spec.js
clients/js/README.md
clients/js/doc-async-client.md
clients/js/test/README.md
servers/ruby/spec/client_examples/dynamic_mounted_paths_spec.rb
```

Mechanical `npm run build` output (three paths, no hand edits):

```text
clients/js/dist/haveapi-client.js
clients/js/dist/types/haveapi/protocol.d.ts
clients/js/dist/types/haveapi/async/request.d.ts
```

All paths yielded to implementer0 for hooked source and generated commits.
Final history consolidates earlier helper generation and this correction into
one cumulative generated stream before exact final `Version 0.30.0`.
The separately accepted diagnostics commit is `164a15e4`.

## Completed quick checks

All commands used the prepared tools-only root Nix shell. No installs, new
listener, long acceptance or registry/Git mutations were performed by this owner.

- `cd clients/js && npm run build`: passed, 4.51 seconds.
- `npm run test:compatibility`: **39/39**, including ten new mounted cases.
- `npm run test:async`: **39/39**.
- `npm run test:resources`: **11/11**.
- `npm run test:types`: emitted callback and async declaration configurations pass.
- `npm run typecheck`: source TypeScript passes.
- `./node_modules/.bin/mocha test/path_construction.spec.js test/oauth2_revoke_encoding.spec.js test/query_encoding.spec.js`:
  **11 passing**.
- `cd servers/ruby && bundle exec rspec spec/client_examples/dynamic_mounted_paths_spec.rb spec/client_examples/dynamic_acceptance_spec.rb`:
  **6 examples, 0 failures**, seed 7834, 2.01 seconds.
- RuboCop on the new Ruby contract spec: **no offenses**.
- `git diff --check`: passed.

Coverage includes root/mount and trailing-slash forms, exact encoded slash/space/
percent IDs, explicit/default/version-list discovery, unchanged raw request
queries and deliberate no-dedup semantics, global/versioned token challenge routes,
callback renew/revoke, callback/async state show/poll, descriptor rejection before
transport or callback credential reads, and unchanged OAuth relative/exact-trusted
origin behavior. The real Rack check exercises actual advertised paths, actual
login/continuation responses and nested action replies without listening sockets.

## Remaining gates

Commit/owned-path cleanliness and consolidated final head proof belong to
implementer0. The same reviewer must complete the affected four-lane final review
before long installed wheel/sdist rendered-snippet execution. Earlier CI/core
checks at `27b4f8f8` do not validate these corrections. No source deviation or
remaining package1 implementation blocker is known.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

Post-yield read-only observation: authored correction committed by implementer0
as `d59ba3e4` (`clients/js: resolve described routes from API origin`). All nine
authored paths are clean. The three exact generated paths were staged by
implementer0 for their separate declared output commit; final generation/history
proof remains pending its completion.

Generated correction committed as `5b1dd07c` (`clients/js: rebuild client request
URL artifacts`). Read-only `git status --short -- clients/js
servers/ruby/spec/client_examples/dynamic_mounted_paths_spec.rb` returned no
output: all twelve package paths are committed and clean. Final cumulative
history consolidation/review and long verification remain lead/implementer0-owned.
