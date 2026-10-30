# 2026-10-29-client-formatting-audit

## Goal

I'd like you to check all haveapi clients (dynamic and generated) if they're using appropriate code style/formatting. e.g. for ruby we use rubocop, other languages have their own things. the generated clients should also generate appropriate code or use a formatter. does for example clients/go use gofmt? and rust and typescript generators? make no changes, just asses the situation and make suggestions.

## Affected repositories

- HaveAPI only. Implement the accepted formatting plan for Ruby, Go, Rust,
  JavaScript/TypeScript, generated TypeScript, Python and PHP; exclude Elixir.
- User authorized implementation after the read-only audit and planning.
- Start from the newer documentation redesign lineage, currently
  `ae46cf27a9afb6558d386c293cec7231dd6c423d` on
  `2026-10-27-api-documentation-redesign-example-instructions`, in our own
  `2026-10-29-client-formatting-audit` branch/worktree. Record the actual base.

## Approach

- Architect records design.md before substantive implementation. Retain saved
  team settings and use four bounded execution packages with exclusive files.
- implementer2: mandatory Prettier 3.9.10 in Ruby TypeScript generation, canonical
  packaged empty JSON configuration, final-byte provenance, packaging and smoke.
- implementer0: authored JS/TS normalization and format/check commands; Ruby
  invocation/CI triggers; Go formatter failure and canonical-output tests.
- implementer3: PHP PER-CS3x0 formatting, remove migration rules, generated-file
  exclusion, dry-run CI, separate PHP8.0 shipped-source syntax lane.
- implementer1: Rust formatting checks/failure tests and shared Nix/Make/hooks/
  EditorConfig/development guidance. Own shared root files; serialize Git work.
- Apply Prettier defaults, not custom indentation/quote preferences. Normalize
  all covered authored JS/TS and PHP now; isolate mechanical formatting commits.
- Add shared check-format and check-rust commands; retain Python Ruff and native
  Ruby/Go/Rust tooling. No ESLint, API renames or broad Ruby metrics tightening.

## Decisions

- Generator flow: pure emitter -> validate -> batch Prettier in temporary tree
  -> validate formatted files -> hash/check/install. PRETTIER executable or PATH;
  exact version; explicit packaged config/parser, no ambient EditorConfig/ignore.
- No network or dependency installation during generation. Fetch/help/doc
  rendering stay formatter-free. Formatter errors preserve TS destination.
- Keep manifest format1 with additive formatter provenance; old owned trees can
  regenerate, check mode reports stale without mutation. Preserve existing writer
  recovery, foreign files/symlink refusals and unchanged-output timestamps.
- Fix single-quote assumptions in JS version metadata/update/bundle tooling;
  retain old single/new double quote compatibility without changing versions.
- Generated catalogs/build outputs remain owned by their generators. PHP floor
  remains8.0; PHPUnit remains on8.3/8.4. No package publication or deployment.

## Compatibility and deployment

- No public API/wire/schema change intended. New TS generation prerequisite:
  Node plus Prettier3.9.10. Ruby gems ship config/code, not node_modules.
- Rollback TS generation with its matching owned tree and manifest. Preserve
  existing interrupted-installation contract. Go write-before-format unchanged.
- Rebase only our commits onto remote master after redesign integration; record
  base/head, patch equivalence/conflicts and repeat affected checks/review.
- Master integration requires separate explicit approval; none is granted.

## Documentation

- Readers: HaveAPI contributors and installed-generator consumers. Update
  component guides and development/release guidance for commands, prerequisites,
  formatter identity and old-tree regeneration. Follow newer example conventions.
- Keep session evidence/ownership here and in state/design/review artifacts.

## Testing plan

- Quick: native format checks, generator/unit/release specs, canonical output,
  repeat/noop/check behavior, old manifests, failure preservation, ambient-config
  independence, packaged/source identity, version-tooling regression, PHP8 syntax.
- Commit all intended changes and pass quick checks, then independent final
  review by retained reviewer0 of complete owned history/diff and migration
  provenance, including inherited redesign base. No database migrations planned.
- Then bounded watched integration: JS/type compatibility, TS consumer/wire,
  Go/Rust acceptance and runtime features/Clippy, PHP PHPUnit, Python regression,
  one clean build-only packaging batch and extracted TS generator smoke.
- Publish feature branch; stop at ready awaiting integration approval. Do not
  archive/delete/stop the session.
