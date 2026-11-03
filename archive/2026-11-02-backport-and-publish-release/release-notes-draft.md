# Mon Nov 02 2026 - version 0.32.2

## Ruby server

- Add English and Czech HTML API documentation, including translated articles,
  client guidance and comments in generated examples. The documentation language
  is independent of the API request language.
- Keep example selectors usable without JavaScript and hide detail controls
  when only one choice is available.
- Load the Ruby client before example error handlers, place Switch user before
  Sign out, and use a shorter English example-language label.
- Version documentation CSS and JavaScript URLs by content so upgrades and
  rollbacks load the matching assets.

## TypeScript client generator

- Add live API and action descriptions through the existing executor, typed
  metadata receipts, and `ClientInputError` for local validation failures.
  Preserve transport errors and the complete response envelope.
- Apply metadata namespace overrides consistently without changing Custom
  payloads or the original response envelope.
- Generated clients now require the supported `haveapi-client@0.32.0` runtime.
  Generation reserves `describe` at the API root and the new helper/type names.
  Explicit action help routes must include their matching `?method=...` selector
  and path placeholders. Existing generated clients keep working without
  regeneration; retain their matching runtime when staying on older output.

## Development tooling

- Keep performance comparisons compatible with the localized documentation
  packaging layout while retaining dependency, runtime and input checks.
