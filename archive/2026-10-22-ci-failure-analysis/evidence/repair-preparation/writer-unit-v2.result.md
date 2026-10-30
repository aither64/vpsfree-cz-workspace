start_epoch=1792694611
end_epoch=1792694657
elapsed_seconds=46
exit_status=1

## Failure excerpt

```text
Installing rspec-core 3.13.6
Installing concurrent-ruby 1.3.8
Installing yard 0.9.45
Bundle complete! 11 Gemfile dependencies, 29 gems now installed.
Bundled gems are installed into `./.gems`
creating Makefile
compiling native.c
linking shared-object libosctl/native.so

Randomized with seed 23197
FF.....................

Failures:

  1) OsCtld::Commands::Container::Start reloads the prepared root and cleanup ownership before any CPU assignment
     Failure/Error: allow(builder_class).to receive(:new).with(rc, cmd: anything).and_return(builder)
       Wrong number of arguments. Expected 0, got 2.
     # ./spec/osctld/commands/container/start_spec.rb:66:in 'RSpec::ExampleGroups::OsCtldCommandsContainerStart#prepare_temporary_dataset'
     # ./spec/osctld/commands/container/start_spec.rb:73:in 'block (3 levels) in <top (required)>'
     # ./spec/support/tempdir_helpers.rb:5:in 'TempdirHelpers#with_tmpdir'
     # ./spec/osctld/commands/container/start_spec.rb:71:in 'block (2 levels) in <top (required)>'

  2) OsCtld::Commands::Container::Start does not publish an unprepared temporary root when preparation fails
     Failure/Error: allow(builder_class).to receive(:new).with(rc, cmd: anything).and_return(builder)
       Wrong number of arguments. Expected 0, got 2.
     # ./spec/osctld/commands/container/start_spec.rb:66:in 'RSpec::ExampleGroups::OsCtldCommandsContainerStart#prepare_temporary_dataset'
     # ./spec/osctld/commands/container/start_spec.rb:93:in 'block (3 levels) in <top (required)>'
     # ./spec/support/tempdir_helpers.rb:5:in 'TempdirHelpers#with_tmpdir'
     # ./spec/osctld/commands/container/start_spec.rb:91:in 'block (2 levels) in <top (required)>'

Finished in 0.15466 seconds (files took 0.53734 seconds to load)
23 examples, 2 failures

Failed examples:

rspec ./spec/osctld/commands/container/start_spec.rb:70 # OsCtld::Commands::Container::Start reloads the prepared root and cleanup ownership before any CPU assignment
rspec ./spec/osctld/commands/container/start_spec.rb:90 # OsCtld::Commands::Container::Start does not publish an unprepared temporary root when preparation fails

Randomized with seed 23197


```
