# Tue Oct 27 2026 - version 0.31.1

## TypeScript client generator

- Normalize only the selected documentation data instead of copying the complete
  API description for each generated example.

## Development tooling

- Test rendering work and allocation growth for every registered client example
  renderer and mode, including complete documentation pages and authorization
  filtering.
- Require these checks before paired performance comparisons and run the
  performance gate for changes in any client directory.
- Allow paired checks across synchronized HaveAPI package versions while keeping
  external dependency and runtime comparisons strict.

