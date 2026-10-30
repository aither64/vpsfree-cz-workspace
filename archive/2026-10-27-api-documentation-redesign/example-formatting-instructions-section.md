## Example source style

Generated examples follow the conventions of their output language. These rules
apply to initialization, authentication and action examples, including inherited
callback, sync, async and blocking variants. Keep Simple and With error handling
consistent where both are supported.

| Language | Source conventions |
| --- | --- |
| PHP | Four-space blocks and array nesting; single quotes for ordinary static strings without interpolation; spaces around concatenation. Keep escaped double quotes where control strings or newline output require them. |
| Ruby | Two-space blocks and single quotes for plain authored strings. Keep `dump`, `inspect` and PP encoding for sample data. |
| JavaScript / TypeScript | Two-space blocks, double-quoted strings and import specifiers, semicolons, and conventional spacing after commas and colons and inside import/object braces. Preserve safe computed keys and typed property access. |
| Python | Four-space suites and the existing double-quoted data encoding. Omit empty optional import slots; use one blank line before module-level executable code and two around top-level async definitions. |
| Go | Tabs, gofmt-compatible spacing and separate standard-library/client import groups. Keep native double-quoted string encoding. |
| Rust | Four-space blocks, conventional Rust spacing/imports and the existing string encoder in both async and blocking examples. |
| CLI / curl / HTTP | Preserve shell quoting, continuations and protocol/JSON whitespace, including the HTTP header/body separator. |

At known fragment boundaries, omit absent fragments and separate logical blocks
with one useful blank line, subject to the language rules above. Avoid leading
or trailing blank padding, duplicate separators and whitespace on empty lines.
Keep formatting in the owning language renderer or adapter. Do not normalize
whole rendered programs or custom-renderer output with a shared regex or
formatter, or add a runtime formatter dependency. Tests may use native formatters.

Keep encoded data separate from authored syntax. Preserve runtime values,
Unicode, apostrophes, backslashes, dollar signs, control bytes, empty values,
false, zero and null. PHP control strings may need double quotes with dollar
signs, backslashes and quotes escaped and PHP-valid control escapes; JSON
`\u` escapes are not a PHP string encoder. Never turn a newline into literal
backslash-n or let wrapper indentation change literal bytes.

Formatting changes must preserve public sample credentials, request inputs,
error handlers and control flow, direct-call/custom-adapter compatibility, and
meaningful detail choices. Do not add panels solely to show different formatting.

When changing a renderer:

- Inspect relevant initialization, authentication and action output for affected
  variants and both direct detail inputs. Cover absent optional fragments and
  literal edge cases where the change can affect them.
- Use existing [server example specs](../servers/ruby/spec/client_examples/) for
  PHP literal round trips and real handlers, Ruby syntax, Python AST/separation,
  detail behavior and custom whitespace. Use the owning
  [Go documentation specs](../clients/go/spec/unit/documentation_spec.rb),
  [TypeScript documentation specs](../clients/typescript/spec/unit/) and
  [Rust development checks](../clients/rust/docs/development.md) when affected.
  TypeScript coverage includes source, strict compilation and performance specs.
- Search neighboring HTML, fixture and performance assertions for exact source
  spelling. Update intentional quote/import/spacing expectations while retaining
  semantic assertions, traversal/allocation bounds and strict compiler checks.
- Follow [development commands](agent-instructions/development.md) and the
  existing verification requirements. Select checks by affected language and
  behavior; an unrelated edit does not require every language toolchain.

