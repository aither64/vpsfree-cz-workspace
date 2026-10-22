# Fri Jul 3 2026 - version 0.29.0
## Ruby server
- Add localization support for framework-owned response messages, validation
  errors, validator descriptions and self-description strings without changing
  the response envelope.
- Add request locale negotiation from `Accept-Language` and optional
  application locale resolvers for user language preferences.
- Add scoped action parameter metadata translations with exact, shared
  resource, attribute and metadata fallback keys for application catalogs.
- Bundle English and Czech framework translations.

## Ruby client
- Send language request headers, translate local validation/authentication
  messages and expose `--language` in the CLI.

## JavaScript client
- Send language request headers and translate local validation/authentication
  messages.

## PHP client
- Send language request headers and translate local validation/authentication
  messages.

## Go client generator
- Generate language/header controls and bundled client translations.

## Localization maintenance
- Add a shared `i18n/haveapi.yml` catalog, generated package-local translation
  artifacts, i18n update/health tasks, pre-commit checks and GitHub Actions
  coverage for translation freshness.
