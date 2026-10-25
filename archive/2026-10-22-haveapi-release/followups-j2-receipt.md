# J2 circular module graph correction

Owner: implementer0. Worktree `haveapi-followups`, branch
`2026-10-22-haveapi-release-followups`, base
`b64fb25bea8d8222fb3263b99956c0b61438a859`. Implementation follows the frozen
[follow-up design](release-followups-design.md). The completed 0.30.0 release,
original worktree, artifacts and refs remain untouched.

## Final authored source yield

Exactly eight J2 paths:

- `clients/js/src/haveapi/client.ts`
- `clients/js/src/haveapi/client_invocation.ts` (new)
- `clients/js/src/haveapi.ts`
- `clients/js/src/haveapi/async/resource.ts`
- `clients/js/src/haveapi/async/resource_instance.ts`
- `clients/js/src/haveapi/async/resource_list.ts`
- `clients/js/src/haveapi/async/resource_model.ts` (new)
- `clients/js/test/compatibility/module_graph.spec.cjs` (new)

Callback invocation implementations and their documentation moved verbatim into
the entry-loaded method installer. Both paths retain dynamic lookup on the
original `Action.waitForCompletion`. The async resource, instance and list bodies
also moved verbatim into one private module; the old module paths explicitly
re-export their original names and share nominal constructor identity. A final
mechanical source comparison confirms these preserved bodies and documentation.
No protocol, authentication, path, timing, schema or public naming change.

The new spec checks the actual Rollup graph, original Action completion lookup,
CommonJS facade identity, resource-valued parameters, local references versus
request snapshots, save/list behavior and strict deep declaration consumers.
The strict consumer uses an explicit temporary tsconfig with `types: []` to
exclude unrelated installed development `@types`. Its strict checking, DOM/ES2015
libraries and full declaration checking remain enabled; no `skipLibCheck`.

J1 owns documentation of the shared build/check contract in
`clients/js/test/README.md`; no additional product documentation is needed for
the implementation-only movement. The ownership boundary and invariants above
remain in the architect's brief.

## Assembled quick evidence

J1 owns the sole npm/build/check slot and reports one cumulative product build,
with no Rollup warnings. Bundle SHA-256:
`df8012e07294e50da26165803ac44e928c9cf7b594ff5d9228ba70379a133938`.

- Final compatibility: **53 passed, 0 failed**; includes all four J2 examples.
- Async: **39 passed**; resources: **11 passed**.
- Source typecheck, public type fixtures and deep declaration consumer passed.
- ES5 parser, graph checks, loader/helper cases and actual JSDoc pages/legacy
  anchor passed.
- Owned tracked diff and all eight J2 source files have clean whitespace.

Logs: [initial batch](followups-js-quick.log),
[remaining checks](followups-js-quick-remainder.log),
[final compatibility](followups-js-compatibility-final.log).
J1's exact authored/generated inventory and hashes are in
[its receipt](followups-j1-receipt.md). The initial failures were test-fixture
issues: VM Node global setup (J1) and unrelated ambient declaration discovery
(J2). Only test source changed afterward; no rebuild or runtime correction.
An optional ambient `node --check` attempt found no ambient Node; it is not
counted as validation. Declared-Nix J1 checks above are the successful evidence.

## Shared setup delta and handoff

Separately owned `flake.nix` adds only `libffi` to the existing root release and
client-rust package lists, following the demonstrated Fiddle native-header
failure and lead grant. No input/lock change. R1 reports frozen isolated install
success (exit 0, 21.8 seconds), activating nondefault Fiddle 1.1.8. This two-shell
prerequisite belongs to the later R1 logical commit, not J2.

All J2 source is yielded. No local compiler, build, install, test or Git mutation
is active from this owner. No commits yet: await lead final owner-yield acceptance
and exact-path hooked commit grant. Preserve separate P1/J1/J2/R1 purposes and
one cumulative generated JS commit after authored JS. No migrations, long
acceptance, feature push, integration or publication performed for follow-ups.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
