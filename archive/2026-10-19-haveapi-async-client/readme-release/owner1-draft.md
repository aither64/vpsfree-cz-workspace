# README and release documentation proposal

Read-only inventory at clean HaveAPI f94e65e35166a0bf8048a27c9d57c7d36957d65b.
Session identity verified; no project/source/Git mutation, build or test.
This is draft wording for architect/main acceptance, not a publication claim.

## Findings and smallest edit set

1. Root README.md:37 only lists a JavaScript client. Expand that one bullet and
   add a short paragraph after the client list identifying the two interfaces,
   compatibility alias, TypeScript authoring and shipped JavaScript/declarations.
   Link the existing component README and async guide; do not duplicate the
   detailed transport/auth/completion contracts.
2. clients/js/README.md:25-28 already states CallbackClient/AsyncClient and exact
   Client alias, but the intro never mentions TypeScript or shipped declarations.
   The async link is late at271-278. Add one concise build/distribution paragraph
   near installation and move/link the async quickstart near the interface choice.
   Scope “Before the client can be used, it must be set up” (line48) to the callback
   examples; low-level AsyncClient.request is setup-free. Keep callback examples,
   constructor .name compatibility and existing async/resource documentation.
3. doc/agent-instructions/releases.md:22 table says only npm/browser bundle.
   Clarify both interfaces ship in one haveapi-client npm package/UMD bundle, with
   generated declarations under dist/types. Add a concise packing-verification
   note under local packaging: normal gulp compiles TS/rebuilds JS+declarations
   before npm pack, and declaration files ship in the same archive. Retain the
   shared VERSION, one package/version, build-only/publication approval gates,
   protected environment, artifact reuse and recovery rules exactly.

No new package, compiled entry, dependency, release mechanism, version or tag is
needed. Existing package main is dist/haveapi-client.js, types points to
 dist/types/haveapi.d.ts, and files includes dist (clients/js/package.json:10-16,48).
Source exports Client and Client as CallbackClient at src/haveapi.ts:44 and
AsyncClient at50. gulpfile scripts compiles TypeScript then bundles UMD and
copies declarations; utils/release/build.sh:25-27 invokes gulp before npm pack.

## Proposed root README paragraph

The JavaScript client provides `CallbackClient` for callback-based applications
and `AsyncClient` for Promises and `async`/`await`. Both are part of the same
`haveapi-client` npm package and browser bundle. `Client` remains a compatibility
alias of `CallbackClient`, referring to the same constructor. Both interfaces
are authored in TypeScript; consumers receive generated JavaScript and TypeScript
declarations and do not need a TypeScript runtime. See the
[JavaScript client README](clients/js/README.md) and
[async client guide](clients/js/doc-async-client.md).

## Proposed component README paragraph and async example

The client is authored in TypeScript. The package ships the UMD JavaScript bundle
at `dist/haveapi-client.js` and generated declarations at `dist/types/haveapi.d.ts`.
Use it from JavaScript or TypeScript without compiling the library yourself.
Choose `CallbackClient` for callbacks or `AsyncClient` for Promises; the following
callback examples continue to work through the `Client` compatibility alias.

```js
const { AsyncClient } = require('haveapi-client');
async function main() {
  const api = new AsyncClient('https://api.example.test/v7.0');
  const result = await api.request({ method: 'GET', path: '/items' });
  console.log(result.data);
}
main().catch(console.error);
```

The CommonJS example keeps await inside an async function.
The API base includes its version for this low-level request. Description-bound
resource use has its own setup flow in the existing async guides. Native Promise
and optional cancellation availability remain documented there; ES5 output does
not imply every async runtime primitive is polyfilled.

## Release sanity-check evidence and owner0 seam

The current packaging route already rebuilds and packs both interfaces together.
It does not automatically prove every new public export/type is in the release:
utils/release/artifacts.rb:183-192 checks npm identity/repository, JS equality
and Client.Version; smoke_npm at198-209 only loads Client and constructs it.
It neither checks Client===CallbackClient/AsyncClient nor checks the declaration
entry/closure. This is a concrete release verification coverage gap, not evidence
that current source packaging is broken. Owner0 owns any accepted code/spec fix.
Do not claim the enhanced gate exists in documentation until implemented and
verified; keep registry publication safety unchanged.

After an architect/lead source release, this owner can edit only the three docs
above, send exact prose diff to main for writing pass, then run appropriate
link/diff checks and normal hooks under the serialized HaveAPI Git slot. No full
release/build/integration or publication is authorized by this proposal.
