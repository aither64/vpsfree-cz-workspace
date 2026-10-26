# HaveAPI client README implementation brief

Accepted for implementation on 2026-10-26 following the user's "proceed".
The lead assigned independent JS/TS, Python and Rust/Go packages; implementer3
owns checkout preparation, hooks and Git operations. The lead owns the final
prose and acceptance pass. Architect0 maintains this brief and resolves material
design questions without taking over application edits.

The original advisory investigation changed no project files, branches or refs
and performed no commits, builds, tests, generation or deployment. The examples
below were checked against source and existing tests, not executed during that
investigation. Implementation and verification evidence belongs in the session's
current state and check records.

## Evidence baseline

Session identity matched `dev-session current` and both environment variables:
`2026-10-26-client-readme-improvements` in
`/home/aither/workspace/ai/vpsfree.cz`.

HaveAPI evidence comes from existing canonical bare-repository objects at
`origin/master`, commit `39e98020070fabcceca32f8fabcf0440f0d8763e` (2026-10-25).
That revision contains both the user's quoted async snippet and the Rust client.
The bare repository's local `HEAD`, `7835acafdda19779815a0f1ba905d78e0085456d`,
is older and lacks Rust; it is not the final evidence baseline. No fetch or
foreign-session worktree/ref was used. Paths and line references below refer to
`39e9802` unless identified as upstream website checks.

The reader is an application developer choosing and using a client. The README
should provide installation, construction, authentication and resource/action
examples before detailed reference or contributor material.

## JavaScript and TypeScript

The package has two interfaces, each usable from both languages. TypeScript is
not a separate async-only SDK or an API-specific client generator.

| Use | Constructor | Discovery | Calls and result |
| --- | --- | --- | --- |
| JavaScript callbacks | `CallbackClient` (`Client` remains an alias) | `setup((client, ready) => ...)`, or `authenticate(..., callback)` | `api.vps.list({limit: 10}, (client, reply) => ...)`; inspect `reply.isOk()` |
| JavaScript async | `AsyncClient` | `await setup()`, or `await authenticate(...)` | `await api.vps.list({params: {limit: 10}})` returns `{value, response}` |
| TypeScript callbacks | Same `CallbackClient` | Same callbacks | Use `CallbackClient.findResource` / `findAction` for endpoint names unknown to the compiler |
| TypeScript async | Same `AsyncClient` | Same Promises | Use `resource(name).action(name)<ResultType>(...)` and the exported result classes |

The library is authored in TypeScript and ships compiled JavaScript plus generated
`.d.ts` declarations. Those declarations describe the library API; they cannot
infer resource/action names downloaded at runtime. Dynamic direct properties
work from JavaScript. Both TypeScript callback and async consumer tests explicitly
reject arbitrary direct properties such as `client.widgets.show` without an
application-provided schema. Do not propose casts to `any` as the primary TS path.

Both dynamic clients use the server's default API version when `version` is
omitted. Give their constructors the API root, including any mount, without a
version suffix. `setup()` obtains the description. `authenticate()` can run first
and also obtains the authorized description, so a token quickstart needs no
separate setup call. Version overrides belong in an optional advanced paragraph.

Sources:

- `clients/js/src/haveapi.ts:45-56`: constructor aliases and exports.
- `clients/js/package.json:16,60`: JavaScript entry and declaration entry.
- `clients/js/src/haveapi/async/client.ts:29-38,62-66,112-150`: constructor,
  default discovery, setup, authentication and explicit resource lookup.
- `clients/js/src/haveapi/client.ts:344-363,445-458,534-578`: callback discovery,
  `(client, boolean)` completion, default version and auth-triggered setup.
- `clients/js/src/haveapi/async/resource_model.ts:11-23,186-260,450-475`:
  action options, materialization, dynamic properties, lists and iteration.
- `clients/js/test/types/callback.ts:15-35,95-106` and
  `clients/js/test/types/async.ts:4-20,35-44`: both typed interfaces and limitations.
- `clients/js/test/async_resources/resource.spec.cjs:121-153`: list output,
  `{value, response}`, item identity and differing output layouts.

### Candidate examples

These Node.js examples assume `VPSADMIN_TOKEN` contains an existing token. They
use the server's default version. VPS resource/action availability still depends
on the server description and the token's permissions. Use the same example
resource across variants to make the differences clear.

JavaScript callbacks:

```js
const { CallbackClient } = require('haveapi-client');

const api = new CallbackClient('https://api.vpsfree.cz');
api.authenticate('token', { token: process.env.VPSADMIN_TOKEN }, (client, ready) => {
  if (!ready) {
    console.error('Authentication failed');
    return;
  }
  client.vps.list({ limit: 10 }, (owner, vpses) => {
    if (!vpses.isOk()) {
      console.error('Unable to list VPSes');
      return;
    }
    vpses.each(vps => console.log(vps.id, vps.hostname));
  });
});
```

Callbacks are `(client, status)` or `(client, reply)`, not Node's error-first
callback convention. The callback API retains callback returns; it does not
become Promise-based when imported from TypeScript.

JavaScript async, suitable as the replacement for the current raw-request example:

```js
const { AsyncClient } = require('haveapi-client');

async function main() {
  const api = new AsyncClient('https://api.vpsfree.cz');
  await api.authenticate('token', { token: process.env.VPSADMIN_TOKEN });
  const { value: vpses } = await api.vps.list({ params: { limit: 10 } });
  vpses.each(vps => console.log(vps.get('id'), vps.get('hostname')));
}

main().catch(console.error);
```

For public resources use `await api.setup()` instead of authentication. Explicit
lookup is also available in JavaScript:
`api.resource('vps').action('list')({params: {limit: 10}})`.
`value` contains the materialized resource result; `response` contains `data`,
`meta`, `envelope` and `httpStatus`. `object_list` outputs become
`AsyncResourceList`; other layouts can return ordinary values. Do not describe
every action result as a list or conflate these calls with raw `request().data`.

TypeScript async, inside an async function after authentication:

```ts
import { AsyncClient, AsyncResourceList } from 'haveapi-client';

const api = new AsyncClient('https://api.vpsfree.cz');
await api.authenticate('token', { token });
const { value: vpses } = await api.resource('vps').action('list')<AsyncResourceList>({
  params: { limit: 10 }
});
vpses.each(vps => console.log(vps.get('id'), vps.get('hostname')));
```

Here `token` is a supplied string. The generic documents the expected result; it
does not generate endpoint types or add a runtime schema validator. A final
README should wrap this in a complete async function and show token acquisition
from application configuration once, without repeating setup explanations.

TypeScript callbacks, with `token` supplied by application configuration:

```ts
import { CallbackClient } from 'haveapi-client';

const api = new CallbackClient('https://api.vpsfree.cz');
api.authenticate('token', { token }, (client, ready) => {
  if (!ready) return;
  const resource = CallbackClient.findResource(client, ['vps']);
  const action = CallbackClient.findAction(resource, 'list');
  action.directInvoke({ limit: 10 }, (owner, response) => {
    if (!response.isOk()) {
      console.error(response.message());
      return;
    }
    console.log(response.response());
  });
});
```

`directInvoke` deliberately returns the raw `Response` wrapper. It is the
existing documented typed callback pattern; explain that distinction rather than
claiming it yields the dynamic list wrapper. The README can give a short typed
callback example and link the lookup details instead of duplicating a full guide.

### Proposed README order and corrections

1. Two-interface table and installation. Explain bundled declarations in one
   paragraph. Keep Node import and browser script loading instructions.
2. Callback JavaScript and async JavaScript quickstarts with resource actions.
3. TypeScript usage covering both interfaces and runtime-discovered names.
4. Authentication and basic resource operations: list, show and parameter input.
5. Short links to advanced features: metadata, associations, blocking actions,
   MFA, localization, hooks and low-level requests.
6. Contributor/check links and license.

Keep raw `request()` in `doc-async-client.md` as an advanced escape hatch for
known paths. Move detailed dependency/compiler/JSDoc compatibility notes from
the README into the existing `test/README.md` or another contributor page.
Keep mounted-URL behavior in the detailed reference, with only the API-root
construction rule in the quickstart.

The rewrite should also resolve existing misleading fragments:

- `clients/js/README.md:36-60` centers a versioned raw request and then gives an
  explicit-version discovery example despite default discovery being supported.
- The callback create example passes `101` before create input. The existing
  adapter's collection create call passes no ID
  (`test/helpers/adapter_callback.js:51-61`). Do not teach an unexplained create
  ID; use a schema-backed create example or omit this mutation from the quickstart.
- The metadata example spells `totalCount` as `tocalCount`.
- The MFA example invokes `cont(...)` and also returns another continuation in
  the same callback. Present the two alternatives as separate examples.
- Several callback examples log success or read output without first checking
  setup/auth/action status. The examples should handle failure concisely.

## Python

Python has synchronous `Client` and asynchronous `AsyncClient` with the same
dynamic resource/action interface. The package requires Python 3.11+; the README
advertises asyncio and Trio, using HTTPX/AnyIO. This investigation did not run
either backend or establish Trio test coverage. Entering `with` / `async with`
performs discovery. No version option means the server's default version.

The current first example is useful, but the following discovery section mixes
basic usage with a long GET/JSON encoding contract, mounted-route semantics and
cache migration details. Start with ordinary action calls, then show `.call()`
when metadata or request options are needed.

Candidate synchronous flow:

```python
import os
from haveapi_client import Client, TokenAuth

with Client(
    "https://api.vpsfree.cz", auth=TokenAuth(os.environ["VPSADMIN_TOKEN"])
) as api:
    for vps in api.vps.list(limit=10).data:
        print(vps["id"], vps["hostname"])
```

Candidate asynchronous flow:

```python
import asyncio
import os
from haveapi_client import AsyncClient, TokenAuth

async def main():
    async with AsyncClient(
        "https://api.vpsfree.cz", auth=TokenAuth(os.environ["VPSADMIN_TOKEN"])
    ) as api:
        result = await api.vps.list(limit=10)
        for vps in result.data:
            print(vps["id"], vps["hostname"])

asyncio.run(main())
```

Follow with `api.vps[vps_id].show()` and
`api.vps.list.call(params={"limit": 10}, meta={"count": True})`, then explain
`.data` and `.meta`. Await the same calls in async code. Do not add a guessed
`api.vps[id].network_interface` hierarchy: vpsAdmin exposes
`api.network_interface.list(vps=vps_id)` at the top level.

Proposed order: installation and requirements; sync and async quickstarts;
authentication; resources, IDs, input and results; pagination and long-running
operations; errors/timeouts; advanced reference and contributing links.
Keep the user-relevant distinctions that one call reads one page, `None` differs
from omission, association fetches are explicit, and waiting does not cancel a
server operation. Explain those briefly next to their examples.

Relocate precise Rack query/JSON shape constraints, destination resolution,
stale-handle rules and injected HTTPX ownership into a proposed
`clients/python/docs/reference.md`. These are public behavior contracts worth
preserving, even when too detailed for the README. Development and packaging
details belong in the existing `CONTRIBUTING.md`; do not hide runtime constraints
there. The lead supplied the completed public PyPI check: `haveapi-client`
0.30.2 was published on 2026-10-25 and requires Python 3.11 or newer. Remove the
stale "once a Python release is available" disclaimer and document normal
installation with `pip install haveapi-client` or `uv add haveapi-client`.
Keep local-checkout installation as a contributor option. This corrects the
publication claim; it does not authorize a new release.

Sources: `clients/python/pyproject.toml:1-19`;
`src/haveapi_client/client.py:34-66,195-203`;
`src/haveapi_client/async_client.py:34-70,201-209`;
`src/haveapi_client/_resources/state.py:170-182`;
`src/haveapi_client/_resources/__init__.py:102-150`;
`examples/list_vps.py:8-18`, `examples/list_vps_async.py:9-19`;
`tests/integration/test_vpsadmin_live.py:99-128`. Python paths after the first
reference are relative to `clients/python/`. The tests were read, not run.

## Rust and Go

Both directories provide generators for API-specific clients. Go's existing
introduction, installation, generation and usage progression is a useful model
for Rust. Rust currently puts extensive development setup before generation and
provides only a one-line action example.

Rust needs an explicit separation between generating a client and using the
generated crate. It generates for one explicit saved API version, embeds its
runtime, and supports async calls plus an optional `blocking` Cargo feature.
It performs no runtime discovery or runtime version selection. Preserve the
explicit version in Rust fetch/generation instructions. Application constructors
still receive the server root, without appending that version.

Proposed Rust order:

1. What the generator produces; async and optional blocking modes; link to the
   generated vpsAdmin crate as a concrete example.
2. Generation prerequisites and a short fetch/generate path, with links to
   `docs/generation.md` for configuration and formatter requirements.
3. A complete async use example and the corresponding blocking example.
4. Common usage: authentication, action builders, IDs, results and errors.
5. Links to runtime reference, development, integration and release guidance.

Use the existing Go README's organization, not its exact contracts. Rust uses
saved snapshots, explicit generation versions and `.send()` builders; Go uses
its own acquisition and `Prepare()` / `Call()` interfaces.

Source-backed Rust usage, using the generated vpsAdmin crate as the named example:

```rust
use vpsadmin_client::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api = Client::builder("https://api.vpsfree.cz").build()?;
    let stats = api.cluster().public_stats().send().await?.output;
    println!("VPS count: {:?}", stats.vps_count);
    Ok(())
}
```

The blocking equivalent imports `vpsadmin_client::blocking::Client`, enables the
crate's `blocking` feature, uses an ordinary `fn main`, and ends the call with
`.send()?.output`. Keep the instruction to construct, use and drop a blocking
client outside an async runtime. Link the existing detailed guidance rather
than expanding the quickstart into runtime internals.

Go can retain its current structure and gain the generated-client link near
the introduction. Its generator uses the default API description when no
`--version` is supplied, but the resulting client is fixed to the generated
routes. A generated client is constructed with `client.New(baseURL)` and invokes
resources through `api.Cluster.PublicStats.Prepare().Call()` or the action's
`Call()` convenience method. A short example should check both `err` and
`response.Status` before consuming `response.Output`.

Sources: `clients/rust/README.md:3-14,44-82`;
`clients/rust/runtime/README.md:17-21,45-49,101-105`;
`clients/rust/template/mod.rs.erb:5-28`;
`clients/rust/template/resource.rs.erb:11-30`;
`clients/go/README.md:10-64`;
`clients/go/lib/haveapi/go_client/cli.rb:6-24`;
`clients/go/lib/haveapi/go_client/generator.rb:37-44`;
`clients/go/template/client.go.erb:27-38`.

### Public generated-client links

Read-only GitHub API metadata and raw README requests succeeded on 2026-10-26:

- https://github.com/vpsfreecz/vpsadmin-go-client is public and not archived,
  with default branch `master`. Its README identifies `haveapi-go-client` as
  its generator and shows construction and resource/action calls.
- https://github.com/vpsfreecz/vpsadmin-rust-client is public and not archived,
  with default branch `main`. Its README identifies HaveAPI generation and
  documents async and optional blocking API 7.0 clients. The example above follows
  that README's public statistics example.

Use these repository-root links. Their READMEs are useful examples, but do not
copy them without checking: the Go README's first sample assigns `response` then
prints `resp`, and the Rust README has some feature-branch links. Fixing those
separate repositories is outside this request. This architect investigation
did not check generated Go/Rust package publication or execute live API actions.

## Accepted implementation packages

The user approved implementation and the lead assigned these boundaries.

| Package | Files | Dependencies and acceptance |
| --- | --- | --- |
| JS/TS README | `clients/js/README.md`; existing `doc-async-client.md`, `doc-async-resources.md`, `test/README.md` only where relocation/linking needs it | Two interfaces in both languages; accurate default discovery, callback status and async result handling; examples for every variant; advanced raw request remains discoverable |
| Python README | `clients/python/README.md`; proposed `docs/reference.md`; `CONTRIBUTING.md` only for contributor material | Inline sync and async flows; resource/action usage first; preserve public runtime constraints in linked reference; no guessed API hierarchy |
| Generated clients | `clients/rust/README.md`, `clients/go/README.md`; proposed Rust `docs/development.md` if development material needs a new home | Full Rust async/blocking examples, distinguish generation-time version from application base URL, working generated-client links, preserve generation prerequisites |

The packages have independent file boundaries and may proceed in parallel.
Implementer3 serializes shared Git operations. The lead's writing and acceptance
pass reconciles terminology and example intent after technical facts are settled.
No source, generated bundle, declaration, protocol or public-interface change
is proposed. Refer material deviations through the lead.

## Acceptance and verification brief

For the advisory pass, acceptance is source-backed coverage of all requested
variants, concrete examples, proposed information placement and verified public
link destinations. This record meets that scope. All snippets remain unexecuted.

For implementation, proportional quick checks should cover the final
Markdown diff and local links, example signatures/result layouts against current
source, JavaScript syntax and TypeScript snippets against the shipped declarations,
and Python snippet syntax. Check Rust examples against the chosen generated
crate's actual public methods and Cargo features. Use existing project check
instructions and Nix environments when selecting exact commands. Do not use
live write actions to validate documentation.

If execution evidence is needed, prefer a bounded existing fixture smoke test
for discovery and one read action in each changed interface. Broad server,
integration, browser, MSRV and packaging suites are unnecessary for this
docs-only proposal unless a later change reveals a specific uncertainty. No
long checks are selected in this investigation. Any later uncertain or long
verification must follow the watcher procedure. Final independent review applies
to completed, committed substantive README changes after quick checks, not to
this investigation record.

## Compatibility, deployment and recovery

The proposed change is documentation only. It changes no persisted state,
database schema, API or protocol, generated Nix configuration, CLI behavior or
Terraform contract. Existing callback and async consumers continue unchanged;
generated Go/Rust consumers retain their compiled API versions. There is no
deployment ordering, rolling-upgrade requirement or coordinated machine update.
Rollback would restore documentation files; no data recovery is involved.
Publishing releases and integrating feature branches remain separate future
actions. The session stays open.

Session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-client-readme-improvements/
