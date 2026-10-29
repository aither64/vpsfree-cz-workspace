# Final branch inventory

Own initial base: `ae46cf27a9afb6558d386c293cec7231dd6c423d`. Remote default observed: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`. Final head: `d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038`.

## Own complete series

```text

5aa2de000c5d5e8f63103ce85c576a41d0c9cbc9 clients/js: normalize authored source with Prettier defaults
058e9315c8e348dac376e7eee05dd5456d4b0bfc clients/js: enforce shared Prettier defaults for authored source
26f578cecae02b0d82151f4bc3e00ae3af6835fb ci: cover Ruby tooling inputs in RuboCop triggers
8bd669389aeb087f63c41197e725d1fcba05d556 clients/go: cover formatting failures and canonical output
05082918c71e1571f5dc9005b4d00208901cb49b clients/php: apply canonical source formatting
08e8716de5206e36c7871d2d8311421c9613f707 clients/php: enforce style and PHP 8.0 syntax
31f2a08126789656f7aaa8274aa47e94ee4f3027 clients/typescript: format generated clients with Prettier
5e871ab42cdb348e43fd02cc46c8c42afd822a56 release: verify formatted TypeScript generator packages
86e32916da1c7236416cac1771fabc412620794e clients: align formatting tools and contributor checks
d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038 clients/rust: verify fixture formatting and failures

```

## Complete default-to-head series (including inherited redesign)

```text

51073383f063abbc24bf19ca669b9b6e46bb9555 documentation: redesign reference and client examples
78ab264add97495aa38ffb33800f16cc9870838d servers/ruby: add optional OAuth documentation sessions
2f6c18a80f3a5f8ce46449ff81183b100b60f34c servers/ruby: preserve documentation performance contracts
1b264e25a73a0ab9bca5f847bd52254f74e0931c docs: align client examples with language style
ae46cf27a9afb6558d386c293cec7231dd6c423d docs: document client example source conventions
5aa2de000c5d5e8f63103ce85c576a41d0c9cbc9 clients/js: normalize authored source with Prettier defaults
058e9315c8e348dac376e7eee05dd5456d4b0bfc clients/js: enforce shared Prettier defaults for authored source
26f578cecae02b0d82151f4bc3e00ae3af6835fb ci: cover Ruby tooling inputs in RuboCop triggers
8bd669389aeb087f63c41197e725d1fcba05d556 clients/go: cover formatting failures and canonical output
05082918c71e1571f5dc9005b4d00208901cb49b clients/php: apply canonical source formatting
08e8716de5206e36c7871d2d8311421c9613f707 clients/php: enforce style and PHP 8.0 syntax
31f2a08126789656f7aaa8274aa47e94ee4f3027 clients/typescript: format generated clients with Prettier
5e871ab42cdb348e43fd02cc46c8c42afd822a56 release: verify formatted TypeScript generator packages
86e32916da1c7236416cac1771fabc412620794e clients: align formatting tools and contributor checks
d6c2748a9e937c1c083fcc60c0e3fcc0a59a0038 clients/rust: verify fixture formatting and failures

```

## Own final diff inventory

```text

.editorconfig                                      |   10 +-
 .git-hooks/pre_commit/js_format.rb                 |   13 +
 .github/workflows/clients-js-tests.yml             |   20 +-
 .github/workflows/clients-php-phpunit.yml          |   53 +-
 .github/workflows/clients-rust.yml                 |    4 +-
 .github/workflows/rubocop.yml                      |   24 +-
 .overcommit.yml                                    |   23 +
 .php-cs-fixer.dist.php                             |    4 +-
 Makefile                                           |   21 +-
 clients/go/README.md                               |   19 +
 clients/go/spec/unit/cli_spec.rb                   |   26 +
 clients/go/spec/unit/formatter_spec.rb             |   21 +
 clients/go/spec/unit/generation_spec.rb            |    6 +
 clients/js/.prettierignore                         |    5 +
 clients/js/README.md                               |   16 +
 clients/js/bower.json                              |   26 +-
 clients/js/gulpfile.js                             |  189 ++--
 clients/js/jsdoc.json                              |   18 +-
 clients/js/jsdoc_aliases.js                        |   40 +-
 clients/js/package.json                            |  121 ++-
 clients/js/rollup.config.js                        |   12 +-
 clients/js/src/haveapi.ts                          |  117 +-
 clients/js/src/haveapi/action.ts                   |  645 ++++++-----
 clients/js/src/haveapi/action_state.ts             |  222 ++--
 clients/js/src/haveapi/async/authentication.ts     |  424 +++++---
 clients/js/src/haveapi/async/client.ts             |  476 +++++---
 clients/js/src/haveapi/async/completion.ts         |  239 ++--
 clients/js/src/haveapi/async/error.ts              |   81 +-
 clients/js/src/haveapi/async/request.ts            |  417 ++++---
 clients/js/src/haveapi/async/resource.ts           |   22 +-
 clients/js/src/haveapi/async/resource_instance.ts  |    4 +-
 clients/js/src/haveapi/async/resource_list.ts      |    2 +-
 clients/js/src/haveapi/async/resource_model.ts     | 1144 +++++++++++++-------
 clients/js/src/haveapi/async/types.ts              |  143 ++-
 clients/js/src/haveapi/authentication.ts           |  103 +-
 clients/js/src/haveapi/authentication/base.ts      |   35 +-
 clients/js/src/haveapi/authentication/basic.ts     |   42 +-
 clients/js/src/haveapi/authentication/oauth2.ts    |  112 +-
 clients/js/src/haveapi/authentication/token.ts     |  315 +++---
 clients/js/src/haveapi/base_resource.ts            |  181 ++--
 clients/js/src/haveapi/client.ts                   |  918 +++++++++-------
 clients/js/src/haveapi/client_invocation.ts        |  270 ++---
 clients/js/src/haveapi/exceptions.ts               |   53 +-
 clients/js/src/haveapi/hooks.ts                    |  143 ++-
 clients/js/src/haveapi/http.ts                     |   56 +-
 clients/js/src/haveapi/i18n.ts                     |  247 +++--
 clients/js/src/haveapi/legacy_globals.ts           |   24 +-
 clients/js/src/haveapi/local_response.ts           |   36 +-
 clients/js/src/haveapi/parameters.ts               |  638 +++++------
 clients/js/src/haveapi/protocol.ts                 |  257 +++--
 clients/js/src/haveapi/resource.ts                 |  112 +-
 clients/js/src/haveapi/resource_instance.ts        |  530 +++++----
 clients/js/src/haveapi/resource_instance_list.ts   |  136 +--
 clients/js/src/haveapi/response.ts                 |   78 +-
 clients/js/src/haveapi/transport.ts                |   40 +-
 clients/js/src/haveapi/types.ts                    |  158 +--
 clients/js/src/haveapi/validator.ts                |  125 ++-
 clients/js/src/haveapi/validators/accept.ts        |    4 +-
 clients/js/src/haveapi/validators/confirm.ts       |    6 +-
 clients/js/src/haveapi/validators/custom.ts        |    4 +-
 clients/js/src/haveapi/validators/exclude.ts       |    7 +-
 clients/js/src/haveapi/validators/format.ts        |   12 +-
 clients/js/src/haveapi/validators/include.ts       |    7 +-
 clients/js/src/haveapi/validators/length.ts        |   20 +-
 clients/js/src/haveapi/validators/number.ts        |   29 +-
 clients/js/src/haveapi/validators/present.ts       |   11 +-
 clients/js/src/haveapi/xml_http_request.ts         |   16 +-
 clients/js/test/async/core.spec.cjs                |  751 ++++++++++---
 clients/js/test/async/request_receipt.spec.cjs     |   94 +-
 clients/js/test/async/resource_save.spec.cjs       |  306 ++++--
 clients/js/test/async/validation.spec.cjs          |  219 +++-
 clients/js/test/async_resources/resource.spec.cjs  |  528 ++++++---
 .../js/test/compatibility/action_lookup.spec.cjs   |  116 +-
 .../js/test/compatibility/build_helpers.spec.cjs   |  166 ++-
 clients/js/test/compatibility/callback.spec.cjs    |  409 ++++---
 clients/js/test/compatibility/core.spec.cjs        |  313 ++++--
 .../js/test/compatibility/jsdoc_aliases.spec.cjs   |   86 +-
 .../js/test/compatibility/jsdoc_markdown.spec.cjs  |  154 ++-
 .../js/test/compatibility/module_graph.spec.cjs    |  280 +++--
 .../js/test/compatibility/mounted_paths.spec.cjs   |  481 +++++---
 .../js/test/compatibility/strict_context.spec.cjs  |  195 ++--
 clients/js/test/contract.spec.js                   |    2 +-
 clients/js/test/contract/client_contract.spec.js   |  209 ++--
 .../js/test/description_name_clobbering.spec.js    |  217 ++--
 clients/js/test/helpers/adapter_async.js           |   81 +-
 clients/js/test/helpers/adapter_callback.js        |   40 +-
 clients/js/test/helpers/async_bundle.cjs           |   84 +-
 clients/js/test/helpers/server.js                  |   76 +-
 clients/js/test/oauth2_revoke_encoding.spec.js     |  102 +-
 clients/js/test/path_construction.spec.js          |  118 +-
 clients/js/test/query_encoding.spec.js             |   38 +-
 clients/js/test/typed_input.spec.js                |  198 ++--
 clients/js/test/types/async.ts                     |   99 +-
 clients/js/test/types/callback.ts                  |  130 ++-
 clients/js/tsconfig.json                           |   39 +-
 clients/php/README.md                              |   24 +-
 clients/php/src/Client.php                         |   20 +-
 clients/php/src/Client/Action.php                  |    4 +-
 clients/php/src/Client/Authentication/OAuth2.php   |   10 +-
 clients/php/src/Client/Authentication/Token.php    |    8 +-
 .../php/src/Client/Exception/ValidationError.php   |    2 +-
 clients/php/src/Client/ResourceInstance.php        |    4 +-
 clients/php/tests/ClientIntegrationTest.php        |    6 +-
 clients/php/tests/ClientIpSecurityTest.php         |   12 +-
 .../php/tests/OAuth2AuthenticationSecurityTest.php |    8 +-
 .../php/tests/RequestConstructionSecurityTest.php  |   58 +-
 .../tests/ResourceAssociationNameCollisionTest.php |    6 +-
 clients/php/tests/TokenAuthenticationI18nTest.php  |    4 +-
 clients/rust/docs/development.md                   |   22 +-
 clients/rust/spec/integration/README.md            |    6 +
 clients/rust/spec/integration/run.rb               |    3 +
 clients/rust/spec/unit/generator_spec.rb           |   74 +-
 clients/typescript/README.md                       |   31 +
 .../lib/haveapi/typescript_client/formatter.rb     |   57 +
 .../lib/haveapi/typescript_client/generator.rb     |    8 +-
 .../lib/haveapi/typescript_client/prettier.json    |    1 +
 .../spec/unit/formatted_generation_spec.rb         |   36 +
 clients/typescript/spec/unit/formatter_spec.rb     |   99 ++
 clients/typescript/spec/unit/generator_spec.rb     |   45 +
 doc/agent-instructions/development.md              |   25 +-
 doc/agent-instructions/releases.md                 |   17 +-
 flake.nix                                          |    5 +-
 utils/check-prettier.nix                           |   28 +
 utils/release/artifacts.rb                         |    8 +-
 utils/release/spec/release_spec.rb                 |   40 +-
 utils/release/spec/typescript_spec.rb              |   29 +-
 utils/release/typescript_smoke.rb                  |   11 +-
 utils/spec/version_update_spec.rb                  |   32 +
 128 files changed, 9926 insertions(+), 5680 deletions(-)

```

## Scope and provenance

The five redesign commits preceding the initial base are inherited by user direction. This session owns ten subsequent logical commits. Mechanical JS/TS and PHP normalization remain separate. Small package.json normalization stays with its tooling commit; the moved negative-type directive stays with its wrapped fixture. Message-only local amendments replaced warning-bearing subjects/bodies; no obsolete approach or fixup commit remains in the final owned series.

No database migrations or migration files. Existing generated manifest format1 is a supported predecessor: additive provenance plus regeneration/check behavior is intentional compatibility. No release, deployment or external consumption of these own commits. No flake-lock updates, repeated dependency-pin streams or transitional schema paths. One exact Prettier dependency addition uses the existing locked Nix package.

Default-branch integration is not approved. The inherited redesign is not yet on remote master; later transplant only these own commits onto approved integrated lineage, compare patches and repeat affected checks/review.

## Review refresh

Original immutable reviewed range and accepted R1 fix are retained in [review.md](review.md). [Consolidation receipt](history-consolidation.md) binds old/new ranges, all nine unaffected patches, the exact accepted release delta and final-tree equality. Lead independently checked the complete range-diff and both equal delta hashes. Final parity/metadata rerun passed; final project index/worktree clean.
