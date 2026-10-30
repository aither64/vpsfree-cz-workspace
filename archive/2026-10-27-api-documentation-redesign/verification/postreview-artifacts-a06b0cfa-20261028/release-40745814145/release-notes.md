# Tue Oct 27 2026 - version 0.31.0

## Ruby server

- Add generated TypeScript client examples through an optional SDK documentation
  profile, with authorization-filtered samples and support for mounted APIs.

## Ruby client

- Add shared schema capture and portable snapshot validation for client
  generators, with explicit API version selection and sanitized saved
  descriptions.

## Go and Rust client generators

- Share schema capture through the `fetch` command and require an explicit API
  version for offline `generate`. Keep Go's positional invocation supported.
- Reject unsafe nested endpoint metadata when loading saved Rust schemas.

## TypeScript client generator

- Add the `haveapi-typescript-client` Ruby gem to generate typed resource and
  action modules from saved HaveAPI protocol 2 schemas.
- Support deterministic regeneration and `--check`, using the existing
  `haveapi-client` runtime for requests and authentication.
