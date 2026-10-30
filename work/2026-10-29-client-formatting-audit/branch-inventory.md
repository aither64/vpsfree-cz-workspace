# Current branch inventory

Current master base: `c79645e0d43885c26cdc4129cbac96fdd5a13b07`. Rebased/published head: `7edb003dd5d5a058b3308510bb8a5f60387ad654`.

## Complete base-to-head series

```text
173edf81a7ed32b736153bc0fda4a2966e4994f9 clients/js: normalize authored source with Prettier defaults
a7209152fda6a32fd5ba175410a8f42653450a69 clients/js: enforce shared Prettier defaults for authored source
3ac5ef632edd0090f07e4b2a223ab31ac5026db9 ci: cover Ruby tooling inputs in RuboCop triggers
e5769f47f19558975ebb41054eb8843f031cca1a clients/go: cover formatting failures and canonical output
717d6272daee3073d00798a50a24ace3ad57150b clients/php: apply canonical source formatting
125c7723b2dba683f60eae26829e5c5f9889d2a0 clients/php: enforce style and PHP 8.0 syntax
74679a6b2d8eeb95cf4d0b092543499c3f412c58 clients/typescript: format generated clients with Prettier
8e482036546fdc8234c2621e3a8512c7fd6e4052 release: verify formatted TypeScript generator packages
108d8f0fc4bdf864c01b14b551aac1f9e8417552 clients: align formatting tools and contributor checks
7edb003dd5d5a058b3308510bb8a5f60387ad654 clients/rust: verify fixture formatting and failures
```

## Final diffstat

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

## History and migration conclusion

Exactly ten logical formatting commits; inherited redesign already integrated into master and not duplicated. Mechanical JS/PHP changes remain separate from tooling. No obsolete approach, unused compatibility path, repeated dependency stream, intermediate pin, database migration, committed library lock or version bump. Existing generated format1 is the intentionally supported predecessor. R1 is folded in its release owner. No feature deployment/publication/master integration.

## Review and evidence lineage

Original reviewed/fixed/consolidated ranges and complete inherited series are retained in [review.md](review.md) and [history-consolidation.md](history-consolidation.md). [Rebase receipt](rebase-master.md) binds old/new bases and heads, all ten equal range-diff patches, byte-identical feature delta, upstream disjointness and lead independent tree reconstruction. [Affected review](rebase-review.md) explicitly accepts unchanged review reuse and new-baseline interactions. Previous CI is retained in [ci-receipt.md](ci-receipt.md); current exact-head CI evidence follows separately.
