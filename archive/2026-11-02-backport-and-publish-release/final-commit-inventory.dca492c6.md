# HaveAPI 0.32.2 complete committed inventory

Base: 9efeadf91d894e01d1d4f4a3e3fc64c6309785c7
Head: dca492c680b8d52f1e4c8b51e89cb7a97fc83c38
Target: haveapi-0.32
Source: f29c1e4675bc1f79641faa619b8c68ecec923c71

## Complete series

```text
3d94938ce2b9b6391db54bb7ec7885c43aaa7c02 servers/ruby: localize HTML documentation in English and Czech
0dbe8176bc377710fc079c88f7dcfdb88526136d doc: add Czech articles and symmetric locale source layout
f385d42c5ce72e873cf77005e2cabc3277a3d2a9 performance: normalize reviewed documentation packaging
a105ab13cbc1a64b91e6da6dc452518c271d11ac doc: localize generated comments and client guidance
8208dd45e7e837eef36c7d8bfb56ad1e670cb763 servers/ruby: apply example choices without JavaScript
3d217c32063db7661216c43e09ef20b87a5400ae servers/ruby: hide singleton example detail controls
4d59d78c8aba4aa70097cf77581302391343f244 servers/ruby: load the Ruby client before example handlers
43a171d34d337708b903946422e66238075fc045 servers/ruby: place Switch user before Sign out
a73453e50b0c9bf3d0c8f0b53e3b1e71510789d8 servers/ruby: shorten the English example language label
59e33fea09fb4b5038fa649a35fb70a5e17e7ea7 servers/ruby: version documentation entry assets by content
f4ccdeed7a8eff034fade04255d4f659c21cddf2 clients/typescript: add descriptions and typed receipts
e0f961715a39f5b778c1abe753ec1bcc56327e84 clients/typescript: clarify generated client wording
83fc752dc92589d9e968b3d1bb42391404671ba0 doc: align generated client runtime installation hint
dca492c680b8d52f1e4c8b51e89cb7a97fc83c38 release: prepare version 0.32.2
```

## Final diffstat

```text
 .github/workflows/clients-python-tests.yml         |   8 +-
 AGENTS.md                                          |   3 +-
 CHANGELOG.md                                       |  32 +
 Makefile                                           |   2 +-
 README.md                                          |  16 +-
 VERSION                                            |   2 +-
 clients/go/docs/documentation.md                   |   2 +-
 clients/go/haveapi-go-client.gemspec               |   2 +-
 clients/go/lib/haveapi/go_client/documentation.rb  | 121 +--
 clients/go/lib/haveapi/go_client/version.rb        |   2 +-
 clients/go/spec/unit/documentation_spec.rb         |  47 +-
 clients/js/dist/haveapi-client.js                  |   2 +-
 clients/js/package.json                            |   2 +-
 clients/js/src/haveapi/client.ts                   |   2 +-
 clients/php/composer.json                          |   2 +-
 clients/php/src/Client.php                         |   2 +-
 clients/python/pyproject.toml                      |   2 +-
 .../python/src/haveapi_client/_protocol/input.py   |   2 +-
 clients/ruby/lib/haveapi/client/version.rb         |   2 +-
 clients/rust/docs/documentation.md                 |   4 +-
 clients/rust/haveapi-rust-client.gemspec           |   2 +-
 .../rust/lib/haveapi/rust_client/documentation.rb  | 103 ++-
 clients/rust/lib/haveapi/rust_client/version.rb    |   2 +-
 clients/rust/spec/unit/documentation_spec.rb       |  49 +-
 clients/typescript/README.md                       |  56 +-
 clients/typescript/docs/documentation.md           |   4 +-
 .../typescript/haveapi-typescript-client.gemspec   |   2 +-
 .../lib/haveapi/typescript_client/documentation.rb |  28 +-
 .../lib/haveapi/typescript_client/emitter.rb       |  25 +-
 .../typescript/lib/haveapi/typescript_client/ir.rb |  23 +-
 .../lib/haveapi/typescript_client/naming.rb        |   6 +-
 .../lib/haveapi/typescript_client/version.rb       |   2 +-
 clients/typescript/spec/documentation/wire.mjs     |   2 +-
 clients/typescript/spec/documentation/wire.rb      |   2 +-
 .../spec/typescript/actual_runtime_wire.mjs        |  52 +-
 clients/typescript/spec/typescript/consumer.ts     |  45 +-
 clients/typescript/spec/typescript/fixtures.rb     |   2 +
 clients/typescript/spec/typescript/runtime_spy.mjs |  67 +-
 clients/typescript/spec/typescript/wire.rb         |   2 +-
 clients/typescript/spec/unit/documentation_spec.rb |  31 +
 clients/typescript/spec/unit/emitter_spec.rb       |  14 +-
 .../spec/unit/formatted_generation_spec.rb         |   2 +-
 clients/typescript/spec/unit/ir_spec.rb            |  32 +
 clients/typescript/template/action.ts.erb          |  15 +-
 clients/typescript/template/api.ts.erb             |  11 +-
 clients/typescript/template/descriptions.ts.erb    |  64 ++
 clients/typescript/template/index.ts.erb           |   4 +-
 clients/typescript/template/resource.ts.erb        |   9 +-
 clients/typescript/template/runtime.ts.erb         |  92 ++-
 doc/agent-instructions/development.md              |  23 +-
 doc/agent-instructions/documentation.md            |  38 +
 doc/agent-instructions/localization.md             |  10 +
 doc/agent-instructions/releases.md                 |   4 +-
 doc/cs/client-examples.md                          | 535 ++++++++++++
 doc/cs/create-client.md                            | 118 +++
 doc/cs/protocol.md                                 | 595 ++++++++++++++
 doc/cs/readme.md                                   | 432 ++++++++++
 doc/cs/typed-input-validation.md                   | 122 +++
 doc/{ => en}/client-examples.md                    |  30 +-
 doc/{ => en}/create-client.md                      |   0
 doc/{ => en}/documentation-oauth.md                |   0
 doc/{ => en}/documentation-ui.md                   |  48 +-
 doc/{ => en}/performance.md                        |  11 +
 doc/{ => en}/protocol.md                           |   4 +-
 doc/en/readme.md                                   | 423 ++++++++++
 doc/{ => en}/typed-input-validation.md             |   0
 doc/json-schema.erb                                |   2 +-
 examples/servers/ruby/activerecord_auth/Gemfile    |   2 +-
 i18n/haveapi.yml                                   | 894 +++++++++++++++++++++
 servers/ruby/.gitignore                            |  11 +-
 servers/ruby/README.md                             | 425 +---------
 servers/ruby/Rakefile                              |  24 +-
 servers/ruby/benchmarks/performance_compare.rb     |  33 +-
 servers/ruby/haveapi.gemspec                       |   4 +-
 servers/ruby/lib/haveapi/client_example.rb         |  23 +-
 servers/ruby/lib/haveapi/client_examples/curl.rb   |  10 +-
 .../lib/haveapi/client_examples/dynamic_helpers.rb |  20 +-
 .../ruby/lib/haveapi/client_examples/go_client.rb  |   2 +-
 servers/ruby/lib/haveapi/client_examples/http.rb   |   8 +-
 .../ruby/lib/haveapi/client_examples/js_client.rb  |  20 +-
 .../ruby/lib/haveapi/client_examples/php_client.rb |  49 +-
 .../lib/haveapi/client_examples/python_client.rb   |  22 +-
 .../ruby/lib/haveapi/client_examples/ruby_cli.rb   |  15 +-
 .../lib/haveapi/client_examples/ruby_client.rb     |  40 +-
 .../lib/haveapi/client_examples/rust_client.rb     |   2 +-
 .../haveapi/client_examples/ts_generated_client.rb |   2 +-
 servers/ruby/lib/haveapi/documentation_context.rb  |  16 +-
 servers/ruby/lib/haveapi/documentation_helpers.rb  | 107 ++-
 servers/ruby/lib/haveapi/documentation_locale.rb   |  65 ++
 servers/ruby/lib/haveapi/documentation_oauth.rb    |  24 +-
 servers/ruby/lib/haveapi/documentation_search.rb   |  10 +-
 .../ruby/lib/haveapi/documentation_validators.rb   |  76 +-
 servers/ruby/lib/haveapi/locales/cs.yml            | 468 +++++++++++
 servers/ruby/lib/haveapi/locales/en.yml            | 467 +++++++++++
 .../ruby/lib/haveapi/public/css/documentation.css  |  12 +-
 .../ruby/lib/haveapi/public/js/documentation.js    |  93 ++-
 servers/ruby/lib/haveapi/server.rb                 |  79 +-
 .../lib/haveapi/shared_documentation_helpers.rb    |  58 +-
 servers/ruby/lib/haveapi/version.rb                |   2 +-
 servers/ruby/lib/haveapi/views/doc_layout.erb      |   5 +-
 .../haveapi/views/doc_sidebars/create-client.erb   |  20 +-
 .../lib/haveapi/views/doc_sidebars/json-schema.erb |   4 +-
 .../lib/haveapi/views/doc_sidebars/protocol.erb    |  48 +-
 .../haveapi/views/documentation/search_form.erb    |   9 +-
 .../haveapi/views/documentation/search_results.erb |  12 +-
 servers/ruby/lib/haveapi/views/index.erb           |   6 +-
 servers/ruby/lib/haveapi/views/main_layout.erb     |   8 +-
 .../lib/haveapi/views/shared_documentation.erb     |  13 +-
 servers/ruby/lib/haveapi/views/shared_sidebar.erb  |  22 +-
 servers/ruby/lib/haveapi/views/version_page.erb    |  22 +-
 .../lib/haveapi/views/version_page/auth_body.erb   |  14 +-
 .../lib/haveapi/views/version_page/client_auth.erb |   2 +-
 .../haveapi/views/version_page/client_example.erb  |   2 +-
 .../lib/haveapi/views/version_page/client_init.erb |   2 +-
 .../haveapi/views/version_page/client_overview.erb |  12 +-
 .../haveapi/views/version_page/example_panels.erb  |   7 +-
 .../haveapi/views/version_page/resource_body.erb   |  48 +-
 .../views/version_page/resource_directory.erb      |   4 +-
 .../ruby/lib/haveapi/views/version_page/usage.erb  |  10 +-
 servers/ruby/lib/haveapi/views/version_sidebar.erb |  51 +-
 .../lib/haveapi/views/version_sidebar/auth_nav.erb |   4 +-
 .../version_sidebar/authentication_control.erb     |  16 +-
 .../version_sidebar/authentication_status.erb      |   2 +-
 .../lib/haveapi/views/version_sidebar/brand.erb    |  21 +-
 .../client_examples/assets/documentation_test.cjs  | 116 ++-
 .../ruby/spec/client_examples/comment_capture.rb   |  72 ++
 servers/ruby/spec/client_examples/comments_spec.rb | 162 ++++
 servers/ruby/spec/client_examples/context_spec.rb  |  20 +-
 servers/ruby/spec/client_examples/detail_spec.rb   |  68 ++
 .../spec/documentation/client_overview_spec.rb     |  60 ++
 .../spec/documentation/example_selection_spec.rb   | 192 +++++
 .../spec/documentation/language_settings_spec.rb   | 132 +++
 servers/ruby/spec/documentation/locale_spec.rb     | 367 +++++++++
 servers/ruby/spec/documentation/navigation_spec.rb |  64 +-
 servers/ruby/spec/documentation/oauth_spec.rb      |  42 +
 .../spec/documentation/search_index_routes_spec.rb |  12 +-
 servers/ruby/spec/documentation/search_spec.rb     |   2 +-
 .../ruby/spec/documentation/shared_pages_spec.rb   |  65 +-
 servers/ruby/spec/documentation/validators_spec.rb |  25 +
 .../ruby/spec/extensions/exception_mailer_spec.rb  |   4 +-
 servers/ruby/spec/packaging_spec.rb                |  77 +-
 .../ruby/spec/performance/event_baseline_spec.rb   |   2 +-
 .../ruby/spec/performance/source_versions_spec.rb  | 113 ++-
 utils/copydoc.sh                                   |  26 +-
 utils/i18n/catalog.rb                              |  53 +-
 utils/release/artifacts.rb                         |  19 +-
 utils/release/build.sh                             |   2 +-
 utils/release/spec/typescript_spec.rb              |   2 +-
 utils/release/typescript_smoke.rb                  |   8 +-
 utils/spec/i18n_catalog_spec.rb                    | 110 +++
 150 files changed, 7551 insertions(+), 1111 deletions(-)
```

## Migration/history inventory

No migrations. Twelve attributed source backports preserve existing integrated
master provenance and required cherry-pick -x traceability. One narrowly scoped
documentation correction and one coordinated release metadata commit follow.
No abandoned local approach, transitional migration, repeated input-pin stream
or redundant metadata bump is introduced. Independent reviewer must assess
these conclusions explicitly. Full diff: git diff 9efeadf91d894e01d1d4f4a3e3fc64c6309785c7 dca492c680b8d52f1e4c8b51e89cb7a97fc83c38.
