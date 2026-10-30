# M7 owner1 final history disposition

A keeps its original full inventory plus final owned core bytes:

- `servers/ruby/lib/haveapi/client_example.rb`
- `servers/ruby/lib/haveapi/client_examples/go_client.rb`
- `servers/ruby/lib/haveapi/client_examples/js_async_client.rb`
- `servers/ruby/lib/haveapi/client_examples/js_client.rb`
- `servers/ruby/lib/haveapi/client_examples/php_client.rb`
- `servers/ruby/lib/haveapi/client_examples/python_client.rb`
- `servers/ruby/lib/haveapi/client_examples/ruby_client.rb`
- `servers/ruby/lib/haveapi/client_examples/rust_client.rb`
- `servers/ruby/lib/haveapi/client_examples/ts_async_client.rb`
- `servers/ruby/lib/haveapi/client_examples/ts_generated_client.rb`
- `servers/ruby/spec/client_examples/detail_spec.rb`
- `servers/ruby/spec/client_examples/presentation_spec.rb`

Fold unchanged final HTTP/CLI global detail declarations into A too:
`servers/ruby/lib/haveapi/client_examples/http.rb` and `ruby_cli.rb`.
Keep original A4363d111 complete `doc/client-examples.md`; do not introduce the
new UI guide or UI/OAuth pointers in A. Existing Context/dynamic renderer paths
remain in A under original inventory, without wholesale old-source replacement.

B owns final whole modern server integration specs:

- `servers/ruby/spec/client_examples/go_spec.rb`
- `servers/ruby/spec/client_examples/ts_generated_client_spec.rb`
- `servers/ruby/spec/client_examples/typescript_profiles_spec.rb`
- `servers/ruby/spec/client_examples/rust_client_spec.rb`

B also owns this package's final Rust adapter source/unit spec:
`clients/rust/lib/haveapi/rust_client/documentation.rb` and
`clients/rust/spec/unit/documentation_spec.rb`, alongside owner2's Go/TS adapter
inventory. At A the four server integration specs keep the appropriate complete
passing predecessor, with final complete bytes restored in B.

C owns final `servers/ruby/spec/documentation/client_overview_spec.rb`, final
shared/UI guide projections supplied by main, and these final four follow-through
paths (their complete original predecessor snapshots remain in A):

- `servers/ruby/spec/client_examples/dynamic_acceptance.rb`
- `servers/ruby/spec/client_examples/dynamic_acceptance_spec.rb`
- `servers/ruby/spec/client_examples/dynamic_acceptance.md`
- `servers/ruby/test_support/dynamic_documentation_api.rb`

No partial harness or test disabling: C restores all final four bytes with the
HTML group metadata producer. D restores optional-OAuth pointers using main's
existing projections. No new history reconstruction was performed here.
