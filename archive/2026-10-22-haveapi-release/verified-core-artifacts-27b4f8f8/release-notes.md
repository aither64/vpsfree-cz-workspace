# Thu Oct 22 2026 - version 0.30.0
## Ruby server
- Add API documentation examples for JavaScript and TypeScript callback and
  async clients, Python sync and async clients, Go, and Rust async and blocking
  clients. Go and Rust examples require a configured generated SDK profile;
  clients without a profile stay hidden.
- Remove File system examples from the generated API documentation.

## JavaScript and TypeScript clients
- Rewrite the callback client in TypeScript. Ship both clients in the existing
  `haveapi-client` npm package and browser bundle, with type declarations in
  the npm package.
- Expose `CallbackClient` explicitly and retain `Client` as an alias of the
  same constructor.
- Add `AsyncClient` with Promise-based requests, authentication, resource
  actions and action-completion waiting. See the async client guides for its
  interface and resource binding.

## Rust client generator
- Add the `haveapi-rust-client` Ruby gem to generate typed Rust clients from a
  saved HaveAPI protocol 2 description and an explicit API version.
- Generate async clients with an optional blocking interface. Each generated
  crate includes its runtime source and does not depend on Ruby or HaveAPI at
  runtime.
- Generated clients require Rust 1.95 or newer and edition 2024. Generation
  requires the formatter version recorded in the client configuration.

## Python client
- Add the `haveapi-client` Python package for Python 3.11 or newer, with
  synchronous and asynchronous clients that discover resources and actions
  from HaveAPI protocol 2.x APIs.
- Support typed input validation, authentication, response objects,
  associations, localization and action-state waiting. Async clients support
  asyncio and Trio.
