# Fri Oct 30 2026 - version 0.32.0

## Ruby server

- Redesign the HTML API reference with searchable resource navigation, action
  details, client setup guides and language-specific examples.
- Add optional OAuth sign-in for documentation through a dedicated confidential
  client, PKCE and encrypted browser sessions with expiration. Documentation
  credentials remain separate from API request authentication.
- Follow each language's source style in client examples and escape shell
  arguments in CLI and curl samples. Keep response transcripts inert when
  examples are copied into a shell.

## Ruby client

- Escape generated CLI help arguments so names and values containing shell
  syntax remain literal.

## TypeScript client generator

- Format emitted client code with Prettier 3.9.10 and record the required version
  and configuration in generation provenance. Install this formatter before
  generation; generated clients do not require it at runtime.

## Development and release tooling

- Align JavaScript, PHP, Python and Rust formatting checks and contributor
  commands. Enforce PHP 8.0-compatible source syntax.
- Check formatting in generated Go and Rust fixtures and fail generation when
  the formatter cannot run.
- Check packaged TypeScript formatter inputs and generated consumers, and
  require synchronized master major/minor metadata during release validation.
