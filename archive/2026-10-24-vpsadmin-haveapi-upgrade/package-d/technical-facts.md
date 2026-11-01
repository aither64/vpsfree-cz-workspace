# API KB technical facts

2026-10-26 update: current HaveAPI client version is published 0.30.2 for Python
and npm. Exact final snippets passed new controlled-transport checks on fresh
0.30.2 installs. Wheel SHA256
`4332346ea2923edd2764107e900f87b3fba780c287869432ab1cfdd265646d50`;
npm archive SHA256
`e6fc12590ebabd05b09d579cfcd62344bf60dfa0b3b05b3c75d7015e2bd5cbfa`,
attested source `321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8`.
All three version fields per language changed; executable Python/TypeScript
snippet bytes and Rust SDK0.1-series guidance did not. See current
`../kb-validation.md` and `followup-2026-10-26/` for evidence and link gaps.
Older version-specific observations below are historical.

2026-10-25 update: current Rust guidance now uses registry `vpsadmin-client =
"0.1"` (published non-yanked 0.1.0), with `version = "0.1", features =
["blocking"]` for blocking calls. Archive SHA256
`2099d96e698e23912879cc15a32097c920f0db96976c2bee671a5ce2239777d0`;
architect evidence verifies unchanged runtime/source and 690 packaged files.
The old Git installation and consumer compile below are historical 2026-10-24
evidence only. Current guards, registry-link gap and checks are in
`../kb-validation.md` and `followup-2026-10-25/focused-check.json`.

Package D evidence, 2026-10-24. Final Czech/English article wording belongs to
the lead. Local examples use fake tokens and controlled responses; they do not
establish authenticated production behavior.

## Published generic clients

| Language | Installation and public import | Runtime and behavior |
| --- | --- | --- |
| Python | `python -m pip install haveapi-client==0.30.1`; `from haveapi_client import Client, AsyncClient, TokenAuth` | Python >=3.11. Sync `Client` context / `.call(...)`; async `AsyncClient` context / `await .call(...)`; HTTPX, asyncio and Trio supported. |
| JavaScript / TypeScript | `npm install haveapi-client@0.30.1`; `import { AsyncClient } from "haveapi-client"` | One npm package contains UMD JavaScript and declarations. Promise API is `AsyncClient`; callback `Client` / `CallbackClient` also remain supported. Package declares no minimum Node version; verified here with Node24.21 / TS6.0.3. Browser usage needs the ordinary Promise/URL environment used by the async API. |

Python source: <https://github.com/vpsfreecz/haveapi/tree/master/clients/python>.
Published package: <https://pypi.org/project/haveapi-client/0.30.1/>.
The actual wheel SHA256 is
`3d44949f4d545c07ea54fbb35229e74a084d5324da89866e6d4d7a91b95eb0c0`.
Requires `httpx>=0.28.1,<1` and `anyio>=4.15,<5`; installed verification used
HTTPX0.28.1 / anyio4.15.1 / Python3.12.12. Metadata is `pypi-metadata.json`.

TypeScript source: <https://github.com/vpsfreecz/haveapi/tree/master/clients/js>.
Published package: <https://www.npmjs.com/package/haveapi-client/v/0.30.1>.
The inspected registry tarball matches integrity
`sha512-n4RMhSbaJZLRm9390wz+M1759h06sEOfh3XVG3t/wGrE0mr97uf+ozERXdJfGXGqxdxelkk765vidheYwUJBWw==`.
Runtime is `dist/haveapi-client.js`; declarations are
`dist/types/haveapi.d.ts`. No separate TypeScript package or library compilation
is needed. CommonJS uses `const {AsyncClient} = require('haveapi-client')`.

## Generated SDKs

Go: <https://github.com/vpsfreecz/vpsadmin-go-client>, module
`github.com/vpsfreecz/vpsadmin-go-client`, import
`github.com/vpsfreecz/vpsadmin-go-client/client`. This is the generated vpsAdmin
SDK; `haveapi/clients/go` is generic generator/client source. Preserve existing
correct Go behavior; the article can link both accurately. SDK README and
go.mod inspected; no new Go example or runtime support claim was checked here.

Rust: <https://github.com/vpsfreecz/vpsadmin-rust-client>, crate package
`vpsadmin-client`, import `vpsadmin_client::Client`. Rust >=1.95, SDK0.1.0 for
API7.0. Generator release0.30.1, SDK0.1.0 and API7.0 are separate versions.
crates.io's API returned HTTP404 for the crate on 2026-10-24, so installation
must name the exact public Git revision:

```toml
[dependencies]
vpsadmin-client = { git = "https://github.com/vpsfreecz/vpsadmin-rust-client", rev = "ff876abe17e3301da62c1b6afbda055ec89db9d2" }
tokio = { version = "1", features = ["macros", "rt-multi-thread"] }
```

Default client is async: `Client::builder("https://api.vpsfree.cz").token(token).build()?`,
then `api.vps().show(123).send().await?.output`. Existing tokens are supplied
explicitly; the SDK does not obtain/refresh them automatically. HTTP Basic
uses `.basic_auth(user, password)`; OAuth access token uses `.oauth2_token(token)`.
For blocking use add `features = ["blocking"]` to the same Git dependency,
import `vpsadmin_client::blocking::Client`, and call `.send()?`. Construct,
use and drop the blocking client outside an async runtime (or place its whole
lifecycle in `spawn_blocking`). TLS dependencies can require a C toolchain.

## Minimal checked methods

`snippets/python-sync.py` and `python-async.py` contain usable token examples.
The API base is `https://api.vpsfree.cz`, with `version="7.0"` passed separately.
The list call is `api.vps.list.call(params={"limit": 10})`; response rows are
read from `result.data`, then `vps["id"]` / `vps["hostname"]`.
Both sync/async fixtures passed against the actual installed wheel with HTTPX
MockTransport, discovered alias, token header, exact query and response fields.
Both standalone snippets syntax-compiled. See `python-check.txt`.

`snippets/typescript.ts` strictly typechecks against the installed package's
declarations and passes the actual published UMD runtime with controlled XHR.
Construction is `new AsyncClient("https://api.vpsfree.cz", {version: "7.0"})`.
`await api.authenticate("token", {token})` performs discovery/auth setup for an
existing token. `await api.resource("vps").action("list")({params: {limit: 10}})`
returns `{value, response}`; `value` defaults to TypeScript `unknown`.
The example narrows `value instanceof AsyncResourceList`, iterates the list,
and reads `vps.get("id")` / `vps.get("hostname")`. A shorter checked alternative
is `console.log(value)` without iteration. Explicit `setup()` before this
`authenticate()` is unnecessary. Raw `request<T>()` is another API with
`{data,meta,envelope,httpStatus}`, and needs no setup; do not conflate these
two return forms.

Python supports `BasicAuth`, `TokenAuth`, `OAuth2Auth` and explicit challenge
login; TS supports explicit authentication and challenge handling. Examples
here consume an existing `VPSADMIN_TOKEN` environment value, never a real
credential embedded in source. New API calls are reads. No password-based token
creation, live authenticated call or member mutation was performed.

The TS fixture used a fresh unauthenticated read-only OPTIONS capture from
<https://api.vpsfree.cz/v7.0/>, SHA256
`40f5a78d3156551abdfea7b1225669bcc79c70ba342de7f74f55595567dfb72e`.
Python used the HaveAPI release's captured API7.0 subset. Rust standalone
consumer compile status is recorded separately in the local watcher receipts.

## Article boundaries and WebUI applicability

Sources are cs `navody:vps:api`, en `manuals:vps:api`; both should contain
`<page>manuals:vps:api</page>`. The English original lacks that marker.
Neither article has `<kb-managed>` or is registered in contract/pages.yml at
`ce2c8cd9358c3636e5d39343e595df813a0b197f`; do not invent managed provenance.

Manual full-article scan found these browser-related passages:

- Opening paragraph explains equivalence with WebUI operations; it gives no
  instruction to operate a particular vpsAdmin control.
- Top-right login direction belongs to HaveAPI API documentation at
  `api.vpsfree.cz`; legacy PHP contract `session.login.open` is inapplicable.
- Client list mentions the old HaveAPI WebUI, without instructions to use it.
- Scope `all` reference explains a default used by the web interface.
- All actionable remaining examples are `vpsfreectl`, Ruby, shell or FUSE
  operations. Backup cross-links point elsewhere; no VPS WebUI action is given.

No semantic `<vpsadmin-nav>` binding is required for these passages. This does
not assert that the new React WebUI has the legacy PHP landmarks. Preserve the
remainder article; no screenshot scenario changes arise from these API examples.
