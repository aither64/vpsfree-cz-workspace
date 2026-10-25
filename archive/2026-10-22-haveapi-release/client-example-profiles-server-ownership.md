# Shared server package ownership

Implementer0 owns the accepted server registry, mount lifecycle, private structural schema, optional-version overview and shared profile/mount/schema/HTML specs. Exact initial paths:

- servers/ruby/lib/haveapi/documentation_clients.rb
- servers/ruby/lib/haveapi/documentation_schema.rb (new, explicitly required by documentation_clients.rb; private StructuralSchema constant)
- servers/ruby/lib/haveapi/server.rb
- servers/ruby/lib/haveapi/views/version_page.erb
- servers/ruby/spec/client_examples/profiles_spec.rb
- servers/ruby/spec/client_examples/profile_mount_spec.rb (new)
- servers/ruby/spec/client_examples/structural_schema_spec.rb (new)
- servers/ruby/spec/documentation/client_examples_spec.rb
- doc/client-examples.md
- clients/go/docs/documentation.md
- clients/rust/docs/documentation.md

Optional existing authorization spec/shared fixture wiring will be listed before use. Go/Rust-only spec files remain owner2/3. doc/client-examples.md is canonical; servers/ruby/doc/client-examples.md is an ignored generated make-doc copy and is never authored. No dependency, flake, version or generated runtime edits. All source edits wait for focused quicks under owner1 setup before yield; commits remain held.
