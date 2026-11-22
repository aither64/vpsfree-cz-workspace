# Isolated lifecycle spec needs the osctld exceptions constant

Related initiative: `work/2026-07-24-ct-start-hang`

Running only
`bundle exec rspec spec/osctld/container/lifecycle_spec.rb`
can fail three incarnation-mismatch examples with
`NameError: uninitialized constant OsCtld::ConfigError`.

The spec exercises `ConfigError` but does not load the file that defines it.
The normal multi-file focused set and full osctld suite load the constant
through another spec and pass. To select lifecycle examples in isolation, use
RSpec location filters for the desired examples. For complete validation, run
the standard focused set or full suite until the spec declares its own
dependency.
